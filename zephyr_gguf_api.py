# from ctransformers import AutoModelForCausalLM
# from fastapi import FastAPI, Request
# import uvicorn


# print("Loading model...")

# model = AutoModelForCausalLM.from_pretrained(
#     "models",
#     model_file="zephyr-7b-beta.Q4_K_M.gguf",  # Use exact filename here
#     model_type="mistral",
#     gpu_layers=0  # Use 0 if you're running CPU-only
# )

# print("Model loaded.")

# app = FastAPI()

# @app.post("/chat")
# async def chat(request: Request):
#     data = await request.json()
#     prompt = f"<|user|>\n{data['message']}\n<|assistant|>\n"
#     response = model(prompt, max_new_tokens=300, temperature=0.7)
#     return {"response": response}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8001)
from ctransformers import AutoModelForCausalLM
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

print("Loading model...")

model = AutoModelForCausalLM.from_pretrained(
    "models",
    model_file="zephyr-7b-beta.Q4_K_M.gguf",
    model_type="mistral",
    gpu_layers=0
)

print("Model loaded.")

app = FastAPI()

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    prompt = f"<|user|>\nUser is feeling {data['emotion']}. Message: {data['message']}\n<|assistant|>\n"
    response = model(prompt, max_new_tokens=300, temperature=0.7)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)  # bind to localhost

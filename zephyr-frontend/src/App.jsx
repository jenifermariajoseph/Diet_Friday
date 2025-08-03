import { useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [emotion, setEmotion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch('http://localhost:8001/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, emotion }),
      });

      const data = await res.json();
      setResponse(data.response || 'No response');
    } catch (err) {
      console.error(err);
      setResponse('Error communicating with the backend');
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Zephyr Chat</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Message:</label><br />
          <input
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            style={{ width: '300px' }}
            required
          />
        </div>
        <div style={{ marginTop: '1rem' }}>
          <label>Emotion:</label><br />
          <input
            value={emotion}
            onChange={(e) => setEmotion(e.target.value)}
            style={{ width: '300px' }}
            required
          />
        </div>
        <button style={{ marginTop: '1rem' }} type="submit">
          Send
        </button>
      </form>

      <div style={{ marginTop: '2rem' }}>
        <h3>Response:</h3>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;

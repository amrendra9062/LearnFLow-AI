import { useState } from "react";
import axios from "axios";

function Chatbot({ context }) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const ask = async () => {
    try {
      const res = await axios.post("http://localhost:8000/chat", {
        question,
        context
      });

      setAnswer(res.data.answer);
    } catch (err) {
      setAnswer("Error connecting to chatbot");
    }
  };

  return (
    <div>
      <h2>Chatbot</h2>

      <input
        placeholder="Ask something..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        style={{ width: "70%", padding: "8px" }}
      />

      <button onClick={ask} style={{ marginLeft: "10px" }}>
        Ask
      </button>

      <p style={{ marginTop: "10px" }}>{answer}</p>
    </div>
  );
}

export default Chatbot;
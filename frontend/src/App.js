import React, { useState } from "react";
import Upload from "./components/Upload";
import Summary from "./components/Summary";
import Quiz from "./components/Quiz";
import Chatbot from "./components/Chatbot";
import "./App.css";

function App() {
  const [data, setData] = useState(null);

  return (
    <div className="container">
      <h1 className="title">LearnFlow AI</h1>

      <div className="card">
        <Upload setData={setData} />
      </div>

      {data && (
        <>
          <div className="card">
            <Summary summary={data.summary} />
          </div>

          <div className="card">
            <Quiz quiz={data.quiz} />
          </div>

          <div className="card">
            <Chatbot context={data.summary} />
          </div>
        </>
      )}
    </div>
  );
}

export default App;
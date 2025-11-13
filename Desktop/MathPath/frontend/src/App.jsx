import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Game from "./components/Game";
import Dashboard from "./components/Dashboard";
import TeacherDashboard from "./components/TeacherDashboard";
import PlayGames from "./components/PlayGames";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>MathPath</h1>
          <nav>
            <a href="/">Home</a>
            <a href="/play">Play Games</a>
            <a href="/dashboard">Dashboard</a>
            <a href="/teacher">Teacher Dashboard</a>
          </nav>
        </header>
        <main>
          <Routes>
            <Route
              path="/"
              element={
                <div className="home-content">
                  <h2>Welcome to MathPath</h2>
                  <p>Adaptive math learning game for secondary students</p>
                  <button
                    className="cta-button"
                    onClick={() => (window.location.href = "/play")}
                  >
                    Start Learning!
                  </button>
                </div>
              }
            />
            <Route path="/play" element={<PlayGames />} />
            <Route path="/game/:lessonId" element={<Game />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/teacher" element={<TeacherDashboard />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

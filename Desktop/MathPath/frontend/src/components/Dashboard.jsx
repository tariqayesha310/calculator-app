import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [attempts, setAttempts] = useState([]);
  const [lessons, setLessons] = useState([]);
  const navigate = useNavigate();

  const fetchUser = async () => {
    // Since no auth, simulate a user
    setUser({ username: "Student", is_teacher: false });
  };

  const fetchAttempts = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/attempts");
      setAttempts(response.data);
    } catch (error) {
      console.error("Error fetching attempts:", error);
    }
  };

  const fetchLessons = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/lessons");
      setLessons(response.data);
    } catch (error) {
      console.error("Error fetching lessons:", error);
    }
  };

  const fetchAdaptiveLessons = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/lessons/adaptive"
      );
      return response.data;
    } catch (error) {
      console.error("Error fetching adaptive lessons:", error);
      return [];
    }
  };

  useEffect(() => {
    fetchUser();
    fetchAttempts();
    fetchLessons();
  }, []);

  if (!user) return <div className="loading">Loading...</div>;

  const totalAttempts = attempts.length;
  const averageScore =
    attempts.length > 0
      ? attempts.reduce((sum, a) => sum + a.score, 0) / attempts.length
      : 0;
  const bestScore =
    attempts.length > 0 ? Math.max(...attempts.map((a) => a.score)) : 0;

  return (
    <div className="dashboard">
      <h2>Welcome, {user.username}!</h2>
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-number">{totalAttempts}</div>
          <div className="stat-label">Total Attempts</div>
        </div>
        <div className="stat-card">
          <div className="stat-number">{Math.round(averageScore * 100)}%</div>
          <div className="stat-label">Average Score</div>
        </div>
        <div className="stat-card">
          <div className="stat-number">{Math.round(bestScore * 100)}%</div>
          <div className="stat-label">Best Score</div>
        </div>
      </div>
      <h3>Available Lessons</h3>
      <div className="lessons-grid">
        {lessons.map((lesson) => (
          <div
            key={lesson.id}
            className={`lesson-card ${lesson.recommended ? "recommended" : ""}`}
          >
            <h4>{lesson.title}</h4>
            <p>{lesson.description}</p>
            <div className="lesson-meta">
              <span className={`difficulty ${lesson.difficulty}`}>
                {lesson.difficulty}
              </span>
              {lesson.recommended && (
                <span className="recommended-badge">Recommended</span>
              )}
            </div>
            <button
              className="play-button"
              onClick={() => navigate(`/game/${lesson.id}`)}
            >
              Play Now
            </button>
          </div>
        ))}
      </div>

      <h3>Your Recent Attempts</h3>
      <ul>
        {attempts.slice(-5).map((attempt) => (
          <li key={attempt.id}>
            Lesson {attempt.lesson_id}: {Math.round(attempt.score * 100)}% in{" "}
            {attempt.time_taken.toFixed(1)}s
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;

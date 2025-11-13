import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const PlayGames = () => {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    fetchLessons();
  }, []);

  const fetchLessons = async () => {
    try {
      const response = await axios.get("http://localhost:8000/api/lessons");
      setLessons(response.data);
    } catch (error) {
      console.error("Error fetching lessons:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="play-games">
        <h2>Play Games</h2>
        <div className="loading">Loading games...</div>
      </div>
    );
  }

  return (
    <div className="play-games">
      <h2>Choose a Game to Play</h2>
      <div className="games-grid">
        {lessons.map((lesson) => (
          <div key={lesson.id} className={`game-card ${lesson.difficulty}`}>
            <div className="game-header">
              <h3>{lesson.title}</h3>
              <span className={`difficulty-badge ${lesson.difficulty}`}>
                {lesson.difficulty}
              </span>
            </div>
            <p>{lesson.description}</p>
            <div className="game-status">
              <span className="status-indicator ready">Ready to Play</span>
            </div>
            <button
              className="play-button"
              onClick={() => navigate(`/game/${lesson.id}`)}
            >
              Start Game
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PlayGames;

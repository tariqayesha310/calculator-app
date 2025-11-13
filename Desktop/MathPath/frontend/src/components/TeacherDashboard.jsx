import React, { useState, useEffect } from "react";
import axios from "axios";

const TeacherDashboard = () => {
  const [attempts, setAttempts] = useState([]);

  useEffect(() => {
    fetchAllAttempts();
  }, []);

  const fetchAllAttempts = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/api/attempts/all"
      );
      setAttempts(response.data);
    } catch (error) {
      console.error("Error fetching attempts:", error);
    }
  };

  return (
    <div className="teacher-dashboard">
      <h2>Teacher Dashboard</h2>
      <h3>Student Analytics</h3>
      <table className="analytics-table">
        <thead>
          <tr>
            <th>User</th>
            <th>Lesson</th>
            <th>Score</th>
            <th>Time</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {attempts.map((attempt) => (
            <tr key={attempt.id}>
              <td>{attempt.user_id}</td>
              <td>{attempt.lesson_id}</td>
              <td>{Math.round(attempt.score * 100)}%</td>
              <td>{attempt.time_taken.toFixed(1)}s</td>
              <td>{new Date(attempt.timestamp).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TeacherDashboard;

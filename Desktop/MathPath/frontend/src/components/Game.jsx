import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const Game = () => {
  const { lessonId } = useParams();
  const [lesson, setLesson] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [startTime, setStartTime] = useState(null);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [showFeedback, setShowFeedback] = useState(false);
  const [streak, setStreak] = useState(0);

  const fetchLesson = async () => {
    try {
      const response = await axios.get(
        `http://localhost:8000/api/lessons/${lessonId}`
      );
      setLesson(response.data);
      setStartTime(Date.now());
    } catch (error) {
      console.error("Error fetching lesson:", error);
    }
  };

  useEffect(() => {
    fetchLesson();
  }, [lessonId]);

  const handleAnswer = async (selectedAnswer) => {
    const questions = JSON.parse(lesson.microgames);
    const correct = selectedAnswer === questions[currentQuestion].correct;
    setSelectedAnswer(selectedAnswer);
    setShowFeedback(true);

    if (correct) {
      setScore(score + 1);
      setStreak(streak + 1);
    } else {
      setStreak(0);
    }

    // Show feedback for 2 seconds, then proceed
    setTimeout(() => {
      setShowFeedback(false);
      setSelectedAnswer(null);

      if (currentQuestion < questions.length - 1) {
        setCurrentQuestion(currentQuestion + 1);
      } else {
        // Game finished
        const endTime = Date.now();
        const totalTime = (endTime - startTime) / 1000;
        submitAttempt(score + (correct ? 1 : 0), totalTime);
      }
    }, 2000);
  };

  const submitAttempt = async (finalScore, time) => {
    try {
      await axios.post("http://localhost:8000/api/attempts", {
        lesson_id: lesson.id,
        score: finalScore / JSON.parse(lesson.microgames).length,
        time_taken: time,
      });
      alert(
        `Game finished! Score: ${finalScore}/${
          JSON.parse(lesson.microgames).length
        }\nStreak: ${streak}`
      );
    } catch (error) {
      console.error("Error submitting attempt:", error);
    }
  };

  if (!lesson) return <div className="loading">Loading...</div>;

  const questions = JSON.parse(lesson.microgames);
  const question = questions[currentQuestion];

  return (
    <div className="game-container">
      <h2 className="game-title">{lesson.title}</h2>
      <div className="game-stats">
        <span>
          Score: {score}/{currentQuestion + (selectedAnswer ? 1 : 0)}
        </span>
        <span>Streak: {streak}</span>
      </div>
      <div className="question-card">
        <p className="question-text">{question.question}</p>
        <div className="options">
          {question.options.map((option, index) => {
            let buttonClass = "option-button";
            if (showFeedback) {
              if (option === question.correct) {
                buttonClass += " correct";
              } else if (option === selectedAnswer) {
                buttonClass += " incorrect";
              }
            }
            return (
              <button
                key={index}
                className={buttonClass}
                onClick={() => !showFeedback && handleAnswer(option)}
                disabled={showFeedback}
              >
                {option}
              </button>
            );
          })}
        </div>
        {showFeedback && (
          <div className="feedback">
            {selectedAnswer === question.correct ? (
              <span className="correct-feedback">✓ Correct!</span>
            ) : (
              <span className="incorrect-feedback">
                ✗ Incorrect. The correct answer is: {question.correct}
              </span>
            )}
          </div>
        )}
      </div>
      <div className="progress">
        Question {currentQuestion + 1} of {questions.length}
      </div>
    </div>
  );
};

export default Game;

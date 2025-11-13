# MathPath MVP Development TODO

## Project Setup
- [x] Create project directory structure (MathPath/ with backend/ and frontend/)
- [x] Initialize backend with FastAPI and dependencies
- [x] Initialize frontend with React

## Backend Development
- [x] Set up SQLAlchemy models for users, lessons, attempts, flashcards
- [x] Implement user authentication (JWT-based)
- [x] Create API endpoints for auth, lessons, attempts, SRS scheduling
- [x] Implement SM-2 spaced repetition algorithm
- [x] Add adaptive difficulty logic (simple score-based adjustment)
- [x] Seed database with sample fractions topic and micro-games
- [x] Add Algebra, Geometry, Trigonometry, Statistics, and Calculus lessons
- [x] Implement adaptive difficulty algorithm

## Frontend Development
- [x] Set up React app with routing
- [x] Create authentication components (login/signup)
- [x] Build micro-game component for fractions (multiple choice questions)
- [x] Implement progress tracking and streaks
- [x] Create teacher dashboard for analytics
- [x] Integrate with backend APIs
- [x] Add lesson selection and navigation
- [x] Create Play Games page with game status indicators

## Integration and Testing
- [x] Connect frontend to backend
- [x] Test user flow: signup -> play game -> view progress
- [x] Test SRS scheduling and adaptive difficulty
- [x] Run locally and verify functionality

## Deployment Prep
- [ ] Prepare for Vercel/Heroku deployment
- [ ] Consider PWA features for mobile
## V1 Features (3-6 months)
- [ ] Implement full SRS with review scheduling
- [ ] Add machine learning for skill prediction and personalized recommendations
- [ ] Enhance adaptive difficulty algorithm with ML
- [ ] Add more micro-game types (drag-and-drop, fill-in-the-blank)
- [ ] Implement progress badges and achievements
- [ ] Add parent dashboard alongside teacher dashboard
- [ ] Improve analytics with charts and reports

## V2 Features (Future)
- [ ] School LMS integration (Google Classroom SSO)
- [ ] Multiplayer collaborative challenges
- [ ] Offline PWA functionality
- [ ] Advanced ML for curriculum personalization
- [ ] Social features (leaderboards, friend challenges)

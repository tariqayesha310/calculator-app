# MathPath 🧮

An interactive educational gaming platform that makes learning mathematics engaging and fun through adaptive micro-games and spaced repetition.

## 🎯 Features

### Current Features
- **6 Math Subjects**: Fractions, Algebra, Geometry, Trigonometry, Statistics, Calculus
- **90 Questions**: Comprehensive question sets across all difficulty levels
- **Real-time Feedback**: Immediate visual feedback for correct/incorrect answers
- **Streak Tracking**: Track consecutive correct answers
- **Adaptive Difficulty**: Easy, Medium, Hard levels with color-coded badges
- **Modern UI**: Beautiful gradients, animations, and responsive design
- **Progress Tracking**: Live score display and question progress
- **Dynamic Lesson Selection**: Choose any subject and play instantly

### Technical Features
- **Full-Stack Architecture**: FastAPI backend with React frontend
- **Database**: SQLite with SQLAlchemy ORM
- **API**: RESTful endpoints for lessons and game data
- **Responsive Design**: Mobile-friendly interface
- **Real-time Updates**: Live game state management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tariqayesha310/MathPath.git
   cd MathPath
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python -c "from database import init_db; init_db()"
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

### Running the Application

1. **Start Backend** (Terminal 1)
   ```bash
   cd backend
   source venv/bin/activate
   uvicorn main:app --reload
   ```
   Backend will run on: http://localhost:8000

2. **Start Frontend** (Terminal 2)
   ```bash
   cd frontend
   npm run dev
   ```
   Frontend will run on: http://localhost:5173

## 🎮 How to Play

1. **Navigate to Play Games**: Click "Play Games" from the main menu
2. **Choose a Subject**: Select from 6 math subjects (Fractions, Algebra, etc.)
3. **Start Playing**: Click "Play" on any lesson card
4. **Answer Questions**: Select the correct answer from multiple choices
5. **Get Feedback**: See immediate visual feedback (green for correct, red for incorrect)
6. **Track Progress**: Monitor your score and streak in real-time
7. **Complete the Game**: Finish all questions to see final results

## 📁 Project Structure

```
MathPath/
├── backend/                 # FastAPI Backend
│   ├── main.py             # Application entry point
│   ├── models.py           # SQLAlchemy models
│   ├── database.py         # Database configuration
│   ├── auth.py             # Authentication utilities
│   ├── routers/            # API endpoints
│   │   ├── lessons.py      # Lesson management
│   │   ├── auth.py         # User authentication
│   │   └── srs.py          # Spaced repetition system
│   ├── seed.py             # Database seeding
│   ├── expand_seed.py      # Extended content seeding
│   └── mathpath.db         # SQLite database
├── frontend/                # React Frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   │   ├── Game.jsx    # Main game component
│   │   │   ├── PlayGames.jsx # Lesson selection
│   │   │   ├── Dashboard.jsx # Student dashboard
│   │   │   └── ...
│   │   ├── App.jsx         # Main application
│   │   └── App.css         # Global styles
│   ├── package.json        # Dependencies
│   └── vite.config.js      # Vite configuration
├── TODO.md                 # Feature roadmap
└── README.md              # This file
```

## 🛠️ API Endpoints

### Lessons
- `GET /api/lessons` - Get all lessons
- `GET /api/lessons/{lesson_id}` - Get specific lesson

### Authentication (Future)
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### SRS (Future)
- `GET /api/srs/reviews` - Get due reviews
- `POST /api/srs/attempts` - Submit attempt

## 🎨 UI Components

### Game Interface
- **Question Cards**: Gradient backgrounds with clear typography
- **Answer Buttons**: Interactive buttons with hover effects
- **Feedback System**: Color-coded correct/incorrect indicators
- **Progress Bar**: Visual question progression
- **Score Display**: Real-time score and streak tracking

### Dashboard
- **Lesson Grid**: Card-based lesson selection
- **Difficulty Badges**: Color-coded difficulty indicators
- **Responsive Layout**: Mobile-optimized design

## 📊 Database Schema

### Lessons Table
```sql
CREATE TABLE lessons (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    topic TEXT NOT NULL,
    description TEXT,
    difficulty TEXT CHECK(difficulty IN ('easy', 'medium', 'hard')),
    microgames TEXT NOT NULL  -- JSON string of questions
);
```

### Future Tables
- Users (authentication)
- Attempts (game sessions)
- Reviews (SRS scheduling)

## 🔧 Development

### Adding New Lessons
1. Create questions in JSON format
2. Add to `backend/expand_seed.py`
3. Run the seeding script

### Customizing UI
- Modify `frontend/src/App.css` for global styles
- Update component-specific styles in individual JSX files

### API Development
- Add new routers in `backend/routers/`
- Include in `backend/main.py`
- Update CORS settings if needed

## 📈 Roadmap

### V1 Features (3-6 months)
- [ ] Implement full SRS with review scheduling
- [ ] Add machine learning for skill prediction and personalized recommendations
- [ ] Enhance adaptive difficulty algorithm with ML
- [ ] Add more micro-game types (drag-and-drop, fill-in-the-blank)
- [ ] Implement progress badges and achievements
- [ ] Add parent dashboard alongside teacher dashboard
- [ ] Improve analytics with charts and reports

### V2 Features (Future)
- [ ] School LMS integration (Google Classroom SSO)
- [ ] Multiplayer collaborative challenges
- [ ] Offline PWA functionality
- [ ] Advanced ML for curriculum personalization
- [ ] Social features (leaderboards, friend challenges)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with FastAPI, React, and SQLAlchemy
- Inspired by educational gaming platforms
- Designed for modern web standards

## 📞 Support

For questions or support, please open an issue on GitHub or contact the maintainers.

---

**Happy Learning! 🎓**

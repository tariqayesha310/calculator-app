from main import SessionLocal
from models import Lesson, Flashcard
import json

def seed_data():
    db = SessionLocal()
    try:
        # Sample fractions lesson
        microgames = [
            {
                "type": "multiple_choice",
                "question": "What is 1/2 + 1/2?",
                "options": ["1", "1/2", "2", "0"],
                "correct": "1"
            },
            {
                "type": "multiple_choice",
                "question": "Simplify 2/4",
                "options": ["1/2", "1/4", "2/2", "4/2"],
                "correct": "1/2"
            },
            {
                "type": "multiple_choice",
                "question": "What is 3/4 - 1/4?",
                "options": ["1/2", "1/4", "2/4", "4/4"],
                "correct": "1/2"
            },
            {
                "type": "multiple_choice",
                "question": "What is 1/3 × 3?",
                "options": ["1", "1/3", "3", "0"],
                "correct": "1"
            },
            {
                "type": "multiple_choice",
                "question": "Which fraction is equivalent to 1/2?",
                "options": ["2/4", "3/6", "4/8", "All of the above"],
                "correct": "All of the above"
            }
        ]

        lesson1 = Lesson(
            topic="fractions",
            title="Basic Fractions",
            description="Learn the fundamentals of fractions",
            difficulty="easy",
            microgames=json.dumps(microgames)
        )
        db.add(lesson1)
        db.commit()
        db.refresh(lesson1)

        # Sample algebra lesson
        algebra_microgames = [
            {
                "type": "multiple_choice",
                "question": "Solve for x: 2x + 3 = 7",
                "options": ["x = 2", "x = 3", "x = 4", "x = 5"],
                "correct": "x = 2"
            },
            {
                "type": "multiple_choice",
                "question": "What is the slope of y = 2x + 1?",
                "options": ["1", "2", "3", "0"],
                "correct": "2"
            },
            {
                "type": "multiple_choice",
                "question": "Expand (x + 2)(x + 3)",
                "options": ["x² + 5x + 6", "x² + 2x + 3", "x² + 6", "2x² + 5x + 6"],
                "correct": "x² + 5x + 6"
            },
            {
                "type": "multiple_choice",
                "question": "Factor x² - 4",
                "options": ["(x-2)(x+2)", "(x-2)²", "(x+2)²", "x(x-4)"],
                "correct": "(x-2)(x+2)"
            },
            {
                "type": "multiple_choice",
                "question": "Solve: x² = 9",
                "options": ["x = 3", "x = -3", "x = ±3", "x = 9"],
                "correct": "x = ±3"
            }
        ]

        lesson2 = Lesson(
            topic="algebra",
            title="Basic Algebra",
            description="Learn fundamental algebra concepts",
            difficulty="medium",
            microgames=json.dumps(algebra_microgames)
        )
        db.add(lesson2)
        db.commit()
        db.refresh(lesson2)

        # Sample geometry lesson
        geometry_microgames = [
            {
                "type": "multiple_choice",
                "question": "What is the sum of angles in a triangle?",
                "options": ["180°", "360°", "90°", "270°"],
                "correct": "180°"
            },
            {
                "type": "multiple_choice",
                "question": "What is the area of a circle with radius 5?",
                "options": ["25π", "10π", "5π", "20π"],
                "correct": "25π"
            },
            {
                "type": "multiple_choice",
                "question": "What is the Pythagorean theorem?",
                "options": ["a² + b² = c²", "a + b = c", "a² - b² = c²", "a × b = c"],
                "correct": "a² + b² = c²"
            },
            {
                "type": "multiple_choice",
                "question": "How many sides does a hexagon have?",
                "options": ["5", "6", "7", "8"],
                "correct": "6"
            },
            {
                "type": "multiple_choice",
                "question": "What is the circumference of a circle with diameter 10?",
                "options": ["10π", "20π", "5π", "15π"],
                "correct": "10π"
            }
        ]

        lesson3 = Lesson(
            topic="geometry",
            title="Basic Geometry",
            description="Learn fundamental geometry concepts",
            difficulty="medium",
            microgames=json.dumps(geometry_microgames)
        )
        db.add(lesson3)
        db.commit()
        db.refresh(lesson3)

        # Sample trigonometry lesson
        trig_microgames = [
            {
                "type": "multiple_choice",
                "question": "What is sin(30°)?",
                "options": ["0.5", "1", "0", "√3/2"],
                "correct": "0.5"
            },
            {
                "type": "multiple_choice",
                "question": "What is cos(0°)?",
                "options": ["0", "1", "-1", "0.5"],
                "correct": "1"
            },
            {
                "type": "multiple_choice",
                "question": "What is tan(45°)?",
                "options": ["0", "1", "∞", "√3"],
                "correct": "1"
            },
            {
                "type": "multiple_choice",
                "question": "In a right triangle, what is the relationship between the sides?",
                "options": ["a² + b² = c²", "a + b = c", "a × b = c", "a/b = c"],
                "correct": "a² + b² = c²"
            },
            {
                "type": "multiple_choice",
                "question": "What is the period of sin(x)?",
                "options": ["π", "2π", "π/2", "4π"],
                "correct": "2π"
            }
        ]

        lesson4 = Lesson(
            topic="trigonometry",
            title="Basic Trigonometry",
            description="Learn trigonometric functions and identities",
            difficulty="hard",
            microgames=json.dumps(trig_microgames)
        )
        db.add(lesson4)
        db.commit()
        db.refresh(lesson4)

        # Sample statistics lesson
        stats_microgames = [
            {
                "type": "multiple_choice",
                "question": "What is the mean of [2, 4, 6, 8, 10]?",
                "options": ["6", "8", "4", "10"],
                "correct": "6"
            },
            {
                "type": "multiple_choice",
                "question": "What is the median of [1, 3, 5, 7, 9]?",
                "options": ["5", "3", "7", "9"],
                "correct": "5"
            },
            {
                "type": "multiple_choice",
                "question": "What is the mode of [1, 2, 2, 3, 3, 3, 4]?",
                "options": ["2", "3", "1", "4"],
                "correct": "3"
            },
            {
                "type": "multiple_choice",
                "question": "What is the probability of rolling a 6 on a fair die?",
                "options": ["1/6", "1/2", "1/3", "1/4"],
                "correct": "1/6"
            },
            {
                "type": "multiple_choice",
                "question": "What does a normal distribution look like?",
                "options": ["Bell curve", "Straight line", "Square", "Triangle"],
                "correct": "Bell curve"
            }
        ]

        lesson5 = Lesson(
            topic="statistics",
            title="Basic Statistics",
            description="Learn fundamental statistics and probability",
            difficulty="medium",
            microgames=json.dumps(stats_microgames)
        )
        db.add(lesson5)
        db.commit()
        db.refresh(lesson5)

        # Sample calculus lesson
        calc_microgames = [
            {
                "type": "multiple_choice",
                "question": "What is the derivative of x²?",
                "options": ["x", "2x", "x²", "2"],
                "correct": "2x"
            },
            {
                "type": "multiple_choice",
                "question": "What is the integral of 2x dx?",
                "options": ["x²", "x² + C", "2x²", "2x² + C"],
                "correct": "x² + C"
            },
            {
                "type": "multiple_choice",
                "question": "What is the limit of (x² - 1)/(x - 1) as x approaches 1?",
                "options": ["0", "1", "2", "∞"],
                "correct": "2"
            },
            {
                "type": "multiple_choice",
                "question": "What is the derivative of sin(x)?",
                "options": ["cos(x)", "-sin(x)", "tan(x)", "sec(x)"],
                "correct": "cos(x)"
            },
            {
                "type": "multiple_choice",
                "question": "What is the area under the curve f(x) = x from 0 to 1?",
                "options": ["0.5", "1", "1.5", "2"],
                "correct": "0.5"
            }
        ]

        lesson6 = Lesson(
            topic="calculus",
            title="Basic Calculus",
            description="Learn derivatives, integrals, and limits",
            difficulty="hard",
            microgames=json.dumps(calc_microgames)
        )
        db.add(lesson6)
        db.commit()
        db.refresh(lesson6)

        # Sample flashcards for fractions
        flashcards = [
            {
                "question": "What is a fraction?",
                "answer": "A fraction represents a part of a whole, written as numerator/denominator."
            },
            {
                "question": "How do you add fractions with the same denominator?",
                "answer": "Add the numerators and keep the denominator the same."
            },
            {
                "question": "How do you simplify a fraction?",
                "answer": "Divide numerator and denominator by their greatest common divisor."
            }
        ]

        for card in flashcards:
            flashcard = Flashcard(
                user_id=1,  # Assuming first user
                lesson_id=lesson1.id,
                question=card["question"],
                answer=card["answer"]
            )
            db.add(flashcard)

        # Sample flashcards for algebra
        algebra_flashcards = [
            {
                "question": "What is a variable in algebra?",
                "answer": "A variable is a symbol (usually a letter) that represents an unknown number."
            },
            {
                "question": "What is the distributive property?",
                "answer": "a(b + c) = ab + ac"
            },
            {
                "question": "What is the slope-intercept form of a line?",
                "answer": "y = mx + b, where m is slope and b is y-intercept."
            }
        ]

        for card in algebra_flashcards:
            flashcard = Flashcard(
                user_id=1,
                lesson_id=lesson2.id,
                question=card["question"],
                answer=card["answer"]
            )
            db.add(flashcard)

        # Sample flashcards for geometry
        geometry_flashcards = [
            {
                "question": "What is the area of a rectangle?",
                "answer": "Area = length × width"
            },
            {
                "question": "What is the volume of a cube?",
                "answer": "Volume = side³"
            },
            {
                "question": "What is a right triangle?",
                "answer": "A triangle with one 90-degree angle."
            }
        ]

        for card in geometry_flashcards:
            flashcard = Flashcard(
                user_id=1,
                lesson_id=lesson3.id,
                question=card["question"],
                answer=card["answer"]
            )
            db.add(flashcard)

        # Sample flashcards for trigonometry
        trig_flashcards = [
            {
                "question": "What are the three main trigonometric functions?",
                "answer": "Sine (sin), Cosine (cos), and Tangent (tan)"
            },
            {
                "question": "What is SOHCAHTOA?",
                "answer": "Sin = Opposite/Hypotenuse, Cos = Adjacent/Hypotenuse, Tan = Opposite/Adjacent"
            },
            {
                "question": "What is the unit circle?",
                "answer": "A circle with radius 1 centered at the origin, used to define trigonometric functions."
            }
        ]

        for card in trig_flashcards:
            flashcard = Flashcard(
                user_id=1,
                lesson_id=lesson4.id,
                question=card["question"],
                answer=card["answer"]
            )
            db.add(flashcard)

        # Sample flashcards for statistics
        stats_flashcards = [
            {
                "question": "What is the difference between mean and median?",
                "answer": "Mean is the average, median is the middle value when sorted."
            },
            {
                "question": "What is standard deviation?",
                "answer": "A measure of how spread out the data is from the mean."
            },
            {
                "question": "What is probability?",
                "answer": "The likelihood of an event occurring, expressed as a number between 0 and 1."
            }
        ]

        for card in stats_flashcards:
            flashcard = Flashcard(
                user_id=1,
                lesson_id=lesson5.id,
                question=card["question"],
                answer=card["answer"]
            )
            db.add(flashcard)

        # Sample flashcards for calculus
        calc_flashcards = [
            {
                "question": "What is a derivative?",
                "answer": "The rate of change of a function, or the slope of the tangent line."
            },
            {
                "question": "What is an integral?",
                "answer": "The area under a curve, or the antiderivative of a function."
            },
            {
                "question": "What is a limit?",
                "answer": "The value that a function approaches as the input approaches a certain value."
            }
        ]

        for card in calc_flashcards:
            flashcard = Flashcard(
                user_id=1,
                lesson_id=lesson6.id,
                question=card["question"],
                answer=card["answer"]
            )
            db.add(flashcard)

        db.commit()
        print("Data seeded successfully")

    finally:
        db.close()

if __name__ == "__main__":
    seed_data()

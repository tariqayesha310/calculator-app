from main import SessionLocal, engine, Base
from models import Lesson, Flashcard
import json

def expand_seed_data():
    db = SessionLocal()
    try:
        # Clear existing data
        db.query(Flashcard).delete()
        db.query(Lesson).delete()
        db.commit()

        # Expanded fractions lesson with 15 questions
        fractions_microgames = [
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
            },
            {
                "type": "multiple_choice",
                "question": "What is 2/5 ÷ 1/3?",
                "options": ["6/5", "2/15", "3/5", "5/6"],
                "correct": "6/5"
            },
            {
                "type": "multiple_choice",
                "question": "Convert 0.75 to a fraction",
                "options": ["3/4", "1/4", "1/2", "2/3"],
                "correct": "3/4"
            },
            {
                "type": "multiple_choice",
                "question": "What is the reciprocal of 5/7?",
                "options": ["7/5", "5/7", "1/5", "7"],
                "correct": "7/5"
            },
            {
                "type": "multiple_choice",
                "question": "Which is larger: 7/8 or 3/4?",
                "options": ["7/8", "3/4", "Equal", "Cannot compare"],
                "correct": "7/8"
            },
            {
                "type": "multiple_choice",
                "question": "What is 5/6 + 1/3?",
                "options": ["7/6", "5/9", "1/2", "11/6"],
                "correct": "7/6"
            },
            {
                "type": "multiple_choice",
                "question": "Simplify 12/18",
                "options": ["2/3", "1/2", "3/4", "4/6"],
                "correct": "2/3"
            },
            {
                "type": "multiple_choice",
                "question": "What is 3/8 × 4/5?",
                "options": ["12/40", "3/5", "12/5", "7/13"],
                "correct": "3/5"
            },
            {
                "type": "multiple_choice",
                "question": "Convert 1.25 to a mixed number",
                "options": ["1 1/4", "1 1/2", "2 1/4", "1 1/5"],
                "correct": "1 1/4"
            },
            {
                "type": "multiple_choice",
                "question": "What is the least common multiple of 4 and 6?",
                "options": ["12", "24", "8", "10"],
                "correct": "12"
            },
            {
                "type": "multiple_choice",
                "question": "Which fraction is in simplest terms: 8/12 or 3/9?",
                "options": ["8/12", "3/9", "Both", "Neither"],
                "correct": "Neither"
            }
        ]

        lesson1 = Lesson(
            topic="fractions",
            title="Basic Fractions",
            description="Learn the fundamentals of fractions with comprehensive practice",
            difficulty="easy",
            microgames=json.dumps(fractions_microgames)
        )
        db.add(lesson1)
        db.commit()
        db.refresh(lesson1)

        # Expanded algebra lesson with 15 questions
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
            },
            {
                "type": "multiple_choice",
                "question": "What is the y-intercept of y = 3x - 2?",
                "options": ["3", "-2", "2", "-3"],
                "correct": "-2"
            },
            {
                "type": "multiple_choice",
                "question": "Simplify: 2(x + 3) - x",
                "options": ["x + 6", "x + 3", "3x + 6", "x"],
                "correct": "x + 6"
            },
            {
                "type": "multiple_choice",
                "question": "Solve: 3x = 15",
                "options": ["x = 5", "x = 3", "x = 45", "x = 12"],
                "correct": "x = 5"
            },
            {
                "type": "multiple_choice",
                "question": "What is the domain of f(x) = 1/x?",
                "options": ["All real numbers", "x ≠ 0", "x > 0", "x < 0"],
                "correct": "x ≠ 0"
            },
            {
                "type": "multiple_choice",
                "question": "Factor: x² + 5x + 6",
                "options": ["(x+2)(x+3)", "(x+1)(x+6)", "(x-2)(x-3)", "(x+6)(x-1)"],
                "correct": "(x+2)(x+3)"
            },
            {
                "type": "multiple_choice",
                "question": "Solve: 2x - 5 = 11",
                "options": ["x = 8", "x = 3", "x = 16", "x = -3"],
                "correct": "x = 8"
            },
            {
                "type": "multiple_choice",
                "question": "What is the range of f(x) = x²?",
                "options": ["All real numbers", "x ≥ 0", "x ≤ 0", "x > 0"],
                "correct": "x ≥ 0"
            },
            {
                "type": "multiple_choice",
                "question": "Expand: (x - 1)²",
                "options": ["x² - 2x + 1", "x² + 2x + 1", "x² - 1", "x² + 1"],
                "correct": "x² - 2x + 1"
            },
            {
                "type": "multiple_choice",
                "question": "Solve: x/2 = 4",
                "options": ["x = 8", "x = 2", "x = 16", "x = 1"],
                "correct": "x = 8"
            },
            {
                "type": "multiple_choice",
                "question": "What is the vertex of y = x² + 4x + 4?",
                "options": ["(0,4)", "(-2,0)", "(2,0)", "(-4,0)"],
                "correct": "(-2,0)"
            }
        ]

        lesson2 = Lesson(
            topic="algebra",
            title="Basic Algebra",
            description="Master fundamental algebra concepts and problem-solving",
            difficulty="medium",
            microgames=json.dumps(algebra_microgames)
        )
        db.add(lesson2)
        db.commit()
        db.refresh(lesson2)

        # Expanded geometry lesson with 15 questions
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
            },
            {
                "type": "multiple_choice",
                "question": "What is the area of a square with side 4?",
                "options": ["16", "8", "12", "20"],
                "correct": "16"
            },
            {
                "type": "multiple_choice",
                "question": "What is the volume of a cube with side 3?",
                "options": ["27", "9", "18", "81"],
                "correct": "27"
            },
            {
                "type": "multiple_choice",
                "question": "What is the perimeter of a rectangle with length 5 and width 3?",
                "options": ["16", "15", "8", "24"],
                "correct": "16"
            },
            {
                "type": "multiple_choice",
                "question": "What is the area of a triangle with base 6 and height 4?",
                "options": ["12", "24", "10", "18"],
                "correct": "12"
            },
            {
                "type": "multiple_choice",
                "question": "How many degrees are in a right angle?",
                "options": ["90°", "180°", "45°", "360°"],
                "correct": "90°"
            },
            {
                "type": "multiple_choice",
                "question": "What is the surface area of a sphere with radius 2?",
                "options": ["16π", "8π", "4π", "12π"],
                "correct": "16π"
            },
            {
                "type": "multiple_choice",
                "question": "What is the volume of a cylinder with radius 3 and height 5?",
                "options": ["45π", "15π", "30π", "135π"],
                "correct": "45π"
            },
            {
                "type": "multiple_choice",
                "question": "How many faces does a cube have?",
                "options": ["6", "8", "12", "4"],
                "correct": "6"
            },
            {
                "type": "multiple_choice",
                "question": "What is the area of a parallelogram with base 7 and height 3?",
                "options": ["21", "10", "14", "24"],
                "correct": "21"
            },
            {
                "type": "multiple_choice",
                "question": "What is the circumference of a circle with radius 7?",
                "options": ["14π", "7π", "21π", "49π"],
                "correct": "14π"
            }
        ]

        lesson3 = Lesson(
            topic="geometry",
            title="Basic Geometry",
            description="Explore shapes, areas, volumes, and geometric principles",
            difficulty="medium",
            microgames=json.dumps(geometry_microgames)
        )
        db.add(lesson3)
        db.commit()
        db.refresh(lesson3)

        # Expanded trigonometry lesson with 15 questions
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
            },
            {
                "type": "multiple_choice",
                "question": "What is cos(90°)?",
                "options": ["0", "1", "-1", "0.5"],
                "correct": "0"
            },
            {
                "type": "multiple_choice",
                "question": "What is sin(90°)?",
                "options": ["0", "1", "-1", "0.5"],
                "correct": "1"
            },
            {
                "type": "multiple_choice",
                "question": "What is tan(0°)?",
                "options": ["0", "1", "∞", "undefined"],
                "correct": "0"
            },
            {
                "type": "multiple_choice",
                "question": "What is the range of sin(x)?",
                "options": ["[-1, 1]", "[0, 1]", "[-∞, ∞]", "[0, ∞]"],
                "correct": "[-1, 1]"
            },
            {
                "type": "multiple_choice",
                "question": "What is cos(60°)?",
                "options": ["0.5", "1", "0", "√3/2"],
                "correct": "0.5"
            },
            {
                "type": "multiple_choice",
                "question": "What is sin(45°)?",
                "options": ["√2/2", "1", "0.5", "√3/2"],
                "correct": "√2/2"
            },
            {
                "type": "multiple_choice",
                "question": "What is the amplitude of y = 2sin(x)?",
                "options": ["2", "1", "π", "0"],
                "correct": "2"
            },
            {
                "type": "multiple_choice",
                "question": "What is tan(30°)?",
                "options": ["√3/3", "1", "√3", "1/√3"],
                "correct": "√3/3"
            },
            {
                "type": "multiple_choice",
                "question": "What is the domain of tan(x)?",
                "options": ["All real numbers except odd multiples of π/2", "All real numbers", "x ≥ 0", "x ≤ 0"],
                "correct": "All real numbers except odd multiples of π/2"
            },
            {
                "type": "multiple_choice",
                "question": "What is cos²(x) + sin²(x)?",
                "options": ["1", "0", "2", "x²"],
                "correct": "1"
            }
        ]

        lesson4 = Lesson(
            topic="trigonometry",
            title="Basic Trigonometry",
            description="Master trigonometric functions, identities, and applications",
            difficulty="hard",
            microgames=json.dumps(trig_microgames)
        )
        db.add(lesson4)
        db.commit()
        db.refresh(lesson4)

        # Expanded statistics lesson with 15 questions
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
            },
            {
                "type": "multiple_choice",
                "question": "What is the range of [5, 2, 8, 1, 9]?",
                "options": ["8", "5", "9", "4"],
                "correct": "8"
            },
            {
                "type": "multiple_choice",
                "question": "What is variance?",
                "options": ["Average of squared differences from mean", "Square root of standard deviation", "Middle value", "Most frequent value"],
                "correct": "Average of squared differences from mean"
            },
            {
                "type": "multiple_choice",
                "question": "What is a histogram used for?",
                "options": ["Showing frequency distribution", "Comparing two variables", "Showing trends over time", "Showing parts of a whole"],
                "correct": "Showing frequency distribution"
            },
            {
                "type": "multiple_choice",
                "question": "What is the probability of flipping heads on a fair coin?",
                "options": ["1/2", "1/4", "1", "0"],
                "correct": "1/2"
            },
            {
                "type": "multiple_choice",
                "question": "What is a scatter plot used for?",
                "options": ["Showing relationship between two variables", "Showing frequency", "Showing trends", "Showing distribution"],
                "correct": "Showing relationship between two variables"
            },
            {
                "type": "multiple_choice",
                "question": "What is the interquartile range?",
                "options": ["Difference between Q3 and Q1", "Difference between max and min", "Middle 50% of data", "Average of quartiles"],
                "correct": "Difference between Q3 and Q1"
            },
            {
                "type": "multiple_choice",
                "question": "What is a box plot used for?",
                "options": ["Showing distribution and outliers", "Showing trends", "Comparing categories", "Showing correlation"],
                "correct": "Showing distribution and outliers"
            },
            {
                "type": "multiple_choice",
                "question": "What is the expected value?",
                "options": ["Long-run average", "Most likely outcome", "Middle value", "Range"],
                "correct": "Long-run average"
            },
            {
                "type": "multiple_choice",
                "question": "What is a confidence interval?",
                "options": ["Range likely to contain true population parameter", "Exact value of parameter", "Sample statistic", "Population parameter"],
                "correct": "Range likely to contain true population parameter"
            },
            {
                "type": "multiple_choice",
                "question": "What is the central limit theorem?",
                "options": ["Sample means approach normal distribution", "Data becomes more variable", "Outliers become more important", "Sample size doesn't matter"],
                "correct": "Sample means approach normal distribution"
            }
        ]

        lesson5 = Lesson(
            topic="statistics",
            title="Basic Statistics",
            description="Learn statistics, probability, and data analysis fundamentals",
            difficulty="medium",
            microgames=json.dumps(stats_microgames)
        )
        db.add(lesson5)
        db.commit()
        db.refresh(lesson5)

        # Expanded calculus lesson with 15 questions
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
            },
            {
                "type": "multiple_choice",
                "question": "What is the derivative of e^x?",
                "options": ["e^x", "x e^{x-1}", "ln(x)", "1/x"],
                "correct": "e^x"
            },
            {
                "type": "multiple_choice",
                "question": "What is the integral of 1/x dx?",
                "options": ["ln|x| + C", "x²/2 + C", "e^x + C", "x + C"],
                "correct": "ln|x| + C"
            },
            {
                "type": "multiple_choice",
                "question": "What is the second derivative of x³?",
                "options": ["6x", "3x²", "6", "x³"],
                "correct": "6x"
            },
            {
                "type": "multiple_choice",
                "question": "What is the chain rule?",
                "options": ["d/dx[f(g(x))] = f'(g(x)) * g'(x)", "d/dx[f(x) + g(x)] = f'(x) + g'(x)", "d/dx[f(x) * g(x)] = f'(x) * g(x) + f(x) * g'(x)", "d/dx[c * f(x)] = c * f'(x)"],
                "correct": "d/dx[f(g(x))] = f'(g(x)) * g'(x)"
            },
            {
                "type": "multiple_choice",
                "question": "What is the derivative of ln(x)?",
                "options": ["1/x", "x", "e^x", "x²"],
                "correct": "1/x"
            },
            {
                "type": "multiple_choice",
                "question": "What is the fundamental theorem of calculus?",
                "options": ["d/dx ∫f(t)dt = f(x)", "∫f'(x)dx = f(x) + C", "Both A and B", "Neither"],
                "correct": "Both A and B"
            },
            {
                "type": "multiple_choice",
                "question": "What is the derivative of cos(x)?",
                "options": ["-sin(x)", "sin(x)", "tan(x)", "sec²(x)"],
                "correct": "-sin(x)"
            },
            {
                "type": "multiple_choice",
                "question": "What is the integral of e^x dx?",
                "options": ["e^x + C", "x e^x + C", "ln(x) + C", "x²/2 + C"],
                "correct": "e^x + C"
            },
            {
                "type": "multiple_choice",
                "question": "What is the limit of sin(x)/x as x approaches 0?",
                "options": ["1", "0", "∞", "undefined"],
                "correct": "1"
            },
            {
                "type": "multiple_choice",
                "question": "What is the derivative of x^n?",
                "options": ["n x^{n-1}", "x^n", "n x^n", "x^{n+1}"],
                "correct": "n x^{n-1}"
            }
        ]

        lesson6 = Lesson(
            topic="calculus",
            title="Basic Calculus",
            description="Master derivatives, integrals, limits, and fundamental theorems",
            difficulty="hard",
            microgames=json.dumps(calc_microgames)
        )
        db.add(lesson6)
        db.commit()
        db.refresh(lesson6)

        # Add flashcards for each lesson
        lessons = [lesson1, lesson2, lesson3, lesson4, lesson5, lesson6]
        flashcard_data = [
            # Fractions flashcards
            [
                {"question": "What is a fraction?", "answer": "A fraction represents a part of a whole, written as numerator/denominator."},
                {"question": "How do you add fractions with the same denominator?", "answer": "Add the numerators and keep the denominator the same."},
                {"question": "How do you simplify a fraction?", "answer": "Divide numerator and denominator by their greatest common divisor."},
                {"question": "What is the reciprocal of a fraction?", "answer": "Swap the numerator and denominator."},
                {"question": "How do you multiply fractions?", "answer": "Multiply numerators together and denominators together."}
            ],
            # Algebra flashcards
            [
                {"question": "What is a variable in algebra?", "answer": "A variable is a symbol (usually a letter) that represents an unknown number."},
                {"question": "What is the distributive property?", "answer": "a(b + c) = ab + ac"},
                {"question": "What is the slope-intercept form of a line?", "answer": "y = mx + b, where m is slope and b is y-intercept."},
                {"question": "What is a quadratic equation?", "answer": "An equation of the form ax² + bx + c = 0"},
                {"question": "What is the quadratic formula?", "answer": "x = [-b ± √(b² - 4ac)] / (2a)"}
            ],
            # Geometry flashcards
            [
                {"question": "What is the area of a rectangle?", "answer": "Area = length × width"},
                {"question": "What is the volume of a cube?", "answer": "Volume = side³"},
                {"question": "What is a right triangle?", "answer": "A triangle with one 90-degree angle."},
                {"question": "What is the circumference of a circle?", "answer": "C = 2πr or C = πd"},
                {"question": "What is the Pythagorean theorem?", "answer": "In a right triangle, a² + b² = c²"}
            ],
            # Trigonometry flashcards
            [
                {"question": "What are the three main trigonometric functions?", "answer": "Sine (sin), Cosine (cos), and Tangent (tan)"},
                {"question": "What is SOHCAHTOA?", "answer": "Sin = Opposite/Hypotenuse, Cos = Adjacent/Hypotenuse, Tan = Opposite/Adjacent"},
                {"question": "What is the unit circle?", "answer": "A circle with radius 1 centered at the origin, used to define trigonometric functions."},
                {"question": "What is the period of sin(x)?", "answer": "2π"},
                {"question": "What is the range of sin(x) and cos(x)?", "answer": "[-1, 1]"}
            ],
            # Statistics flashcards
            [
                {"question": "What is the difference between mean and median?", "answer": "Mean is the average, median is the middle value when sorted."},
                {"question": "What is standard deviation?", "answer": "A measure of how spread out the data is from the mean."},
                {"question": "What is probability?", "answer": "The likelihood of an event occurring, expressed as a number between 0 and 1."},
                {"question": "What is a normal distribution?", "answer": "A bell-shaped probability distribution that is symmetric about the mean."},
                {"question": "What is the central limit theorem?", "answer": "The sampling distribution of the sample mean approaches a normal distribution as sample size increases."}
            ],
            # Calculus flashcards
            [
                {"question": "What is a derivative?", "answer": "The rate of change of a function, or the slope of the tangent line."},
                {"question": "What is an integral?", "answer": "The area under a curve, or the antiderivative of a function."},
                {"question": "What is a limit?", "answer": "The value that a function approaches as the input approaches a certain value."},
                {"question": "What is the chain rule?", "answer": "d/dx[f(g(x))] = f'(g(x)) × g'(x)"},
                {"question": "What is the fundamental theorem of calculus?", "answer": "Relates differentiation and integration"}
            ]
        ]

        for i, lesson in enumerate(lessons):
            for card in flashcard_data[i]:
                flashcard = Flashcard(
                    user_id=1,  # Assuming first user
                    lesson_id=lesson.id,
                    question=card["question"],
                    answer=card["answer"]
                )
                db.add(flashcard)

        db.commit()
        print("Expanded data seeded successfully with 15 questions per lesson!")

    finally:
        db.close()

if __name__ == "__main__":
    expand_seed_data()

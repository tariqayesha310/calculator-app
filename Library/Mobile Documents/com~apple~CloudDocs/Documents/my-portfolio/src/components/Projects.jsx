export default function Projects() {
  return (
    <section id="projects" className="max-w-6xl mx-auto px-6 py-16">
      <h2 className="text-4xl font-bold mb-12 text-center text-gray-800">Projects</h2>

      <div className="space-y-14">

        {/* Web Development */}
        <div>
          <h3 className="text-2xl font-semibold text-blue-600 mb-4">Web Development (React.js)</h3>
          <ul className="list-disc list-inside space-y-3 text-gray-700">
            <li><strong>Netflix Clone:</strong> Streaming interface clone with custom UI and routing</li>
            <li><strong>YouTube Clone:</strong> Video platform clone with search and recommendations</li>
            <li><strong>Gym App:</strong> Fitness tracker and workout planner</li>
            <li><strong>To-Do List App:</strong> Task management app with filters and status control</li>
          </ul>
        </div>

        {/* Game Development */}
        <div>
          <h3 className="text-2xl font-semibold text-green-600 mb-4">Game Development</h3>
          <ul className="list-disc list-inside space-y-3 text-gray-700">
            <li><strong>Dot and Boxes:</strong> Classic strategy game built with interactive UI</li>
            <li><strong>Dice Rolling Game:</strong> Python-based random number game</li>
            <li><strong>Number Guessing Game:</strong> Terminal-based Python game with logic handling</li>
          </ul>
        </div>

        {/* Python Projects */}
        <div>
          <h3 className="text-2xl font-semibold text-purple-600 mb-4">Python Projects</h3>
          <ul className="list-disc list-inside space-y-3 text-gray-700">
            <li><strong>QR Code Generator:</strong> Generate scannable codes for links/text</li>
            <li><strong>Password Manager:</strong> Securely store and retrieve login credentials</li>
            <li><strong>Automated File Backup:</strong> Schedule-based backup system</li>
            <li><strong>Budget Tracker App:</strong> Track expenses and visualise spending</li>
            <li><strong>Language Learning App:</strong> Vocabulary practice with spaced repetition</li>
          </ul>
        </div>

        {/* AI & ML Projects */}
        <div>
          <h3 className="text-2xl font-semibold text-pink-600 mb-4">Artificial Intelligence & Machine Learning</h3>
          <ul className="list-disc list-inside space-y-3 text-gray-700">
            <li><strong>Chatbot with LLMs:</strong> Conversational agent using large language models</li>
            <li><strong>AI Agent:</strong> Task-driven autonomous assistant</li>
            <li><strong>Resume Critiquer:</strong> AI-powered resume feedback generator</li>
            <li><strong>Image Classifier:</strong> AI model for recognising image categories</li>
            <li><strong>Smart Voice Assistant:</strong> Voice-activated ML system with command execution</li>
          </ul>
        </div>

      </div>
    </section>
  );
}

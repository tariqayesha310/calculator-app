export default function Skills() {
  const technicalSkills = [
    "HTML",
    "CSS",
    "JavaScript (Basics)",
    "React.js",
    "Node.js",
    "Python (Web & Automation)",
    "REST APIs",
    "SQL (MySQL, PostgreSQL)",
    "MongoDB",
    "Git & GitHub",
    "AWS/Azure (Basics)",
    "Docker & CI/CD",
    "AI & Machine Learning (LLMs, Generative AI)",
  ];

  const softSkills = [
    "Strategic Thinking",
    "Project Management (Agile)",
    "Digital Marketing & SEO",
    "Leadership & Team Coordination",
    "Creative Communication",
    "Time Management & Multitasking",
    "Cross-Cultural Collaboration",
    "Customer Service",
  ];

  return (
    <section id="skills" className="py-20 bg-gray-50">
      <div className="container mx-auto px-6 max-w-5xl">
        <h2 className="text-3xl font-bold text-center mb-12 text-gray-800">
          Skills & Expertise
        </h2>

        <div className="grid md:grid-cols-2 gap-12">
          {/* Technical Skills */}
          <div>
            <h3 className="text-2xl font-semibold mb-6 text-blue-600">Technical Skills</h3>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              {technicalSkills.map((skill, idx) => (
                <li key={idx}>{skill}</li>
              ))}
            </ul>
          </div>

          {/* Soft Skills */}
          <div>
            <h3 className="text-2xl font-semibold mb-6 text-blue-600">Soft Skills</h3>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              {softSkills.map((skill, idx) => (
                <li key={idx}>{skill}</li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
}

import '../styles/globals.css';
import Head from 'next/head';

export const metadata = {
  title: 'Zainab | Portfolio',
  description: 'Tech-driven portfolio of Zainab – Full Stack Developer & Digital Strategist',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="scroll-smooth bg-gradient-to-r from-purple-100 via-pink-100 to-yellow-100">
      <Head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <body className="min-h-screen flex flex-col font-sans text-gray-900">
        {/* Header with subtle shadow and backdrop blur */}
        <header className="fixed top-0 left-0 w-full bg-white/70 backdrop-blur-md shadow-md z-50">
          <div className="container mx-auto px-6 py-4 flex justify-between items-center">
            <a
              href="#hero"
              className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-purple-600 hover:from-purple-600 hover:to-pink-500 transition"
            >
              Zainab
            </a>

            <nav className="hidden md:flex space-x-8 font-medium text-gray-700">
              <a href="#about" className="hover:text-purple-600 transition">About</a>
              <a href="#projects" className="hover:text-purple-600 transition">Projects</a>
              <a href="#skills" className="hover:text-purple-600 transition">Skills</a>
              <a href="#contact" className="hover:text-purple-600 transition">Contact</a>
            </nav>
          </div>
        </header>

        {/* Push content below fixed header */}
        <main className="flex-grow pt-24 container mx-auto px-6">
          {children}
        </main>

        {/* Footer with gradient text and hover sparkle effect */}
        <footer className="bg-gradient-to-r from-purple-600 to-pink-500 text-white py-6 mt-16 shadow-inner">
          <div className="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            <p className="text-sm opacity-90 select-none">
              &copy; {new Date().getFullYear()} Zainab Tariq. All rights reserved.
            </p>

            <div className="flex space-x-6 text-lg">
              <a
                href="https://github.com/zainab102"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-yellow-300 transition-transform hover:scale-110"
                aria-label="GitHub"
              >
                🐱‍💻
              </a>
              <a
                href="https://www.linkedin.com/in/zainab-22243b366/"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-yellow-300 transition-transform hover:scale-110"
                aria-label="LinkedIn"
              >
                💼
              </a>
              <a
                href="mailto:tariqzainab1190@gmail.com"
                className="hover:text-yellow-300 transition-transform hover:scale-110"
                aria-label="Email"
              >
                📧
              </a>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}

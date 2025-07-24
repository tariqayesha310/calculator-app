export default function Footer() {
  return (
    <footer className="bg-[var(--color-dark)] text-white py-10 px-6 mt-20">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
        {/* Branding */}
        <div className="text-center md:text-left">
          <h2 className="text-2xl font-bold text-[var(--color-accent)]">Zainab.dev</h2>
          <p className="text-sm text-gray-300">© {new Date().getFullYear()} All rights reserved.</p>
        </div>

        {/* Navigation */}
        <ul className="flex flex-wrap justify-center gap-6 text-sm font-medium">
          <li><a href="#about" className="hover:text-[var(--color-accent)] transition">About</a></li>
          <li><a href="#projects" className="hover:text-[var(--color-accent)] transition">Projects</a></li>
          <li><a href="#skills" className="hover:text-[var(--color-accent)] transition">Skills</a></li>
          <li><a href="#contact" className="hover:text-[var(--color-accent)] transition">Contact</a></li>
        </ul>

        {/* Social Icons */}
        <div className="flex space-x-5">
          <a href="https://github.com/yourusername" target="_blank" rel="noopener noreferrer">
            <img src="/icons/github.svg" alt="GitHub" className="w-6 h-6 hover:opacity-80" />
          </a>
          <a href="https://linkedin.com/in/yourusername" target="_blank" rel="noopener noreferrer">
            <img src="/icons/linkedin.svg" alt="LinkedIn" className="w-6 h-6 hover:opacity-80" />
          </a>
          <a href="mailto:your@email.com">
            <img src="/icons/email.svg" alt="Email" className="w-6 h-6 hover:opacity-80" />
          </a>
        </div>
      </div>
    </footer>
  );
}

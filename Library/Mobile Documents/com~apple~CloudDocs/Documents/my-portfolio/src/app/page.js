'use client';
import Hero from '@/components/Hero';
import About from '@/components/About';
import Projects from '@/components/Projects';
import Skills from '@/components/Skills';
import Contact from '@/components/Contact';
import Footer from '@/components/Footer';

export default function Home() {
  return (
    <main className="scroll-smooth">
      {/* 🟣 Hero Section */}
      <section id="hero" className="bg-hero min-h-screen flex items-center justify-center">
        <Hero />
      </section>

      {/* 🩶 About Section */}
      <section id="about" className="bg-about">
        <About />
      </section>

      {/* 💗 Projects Section */}
      <section id="projects" className="bg-projects">
        <Projects />
      </section>

      {/* 🩵 Skills Section */}
      <section id="skills" className="bg-skills">
        <Skills />
      </section>

      {/* 🌼 Contact Section */}
      <section id="contact" className="bg-contact">
        <Contact />
      </section>

      {/* ⚫ Footer */}
      <footer className="bg-footer py-6 text-center text-sm">
        <Footer />
        <p className="mt-4 text-muted">© {new Date().getFullYear()} Zainab Tariq. All rights reserved.</p>
      </footer>
    </main>
  );
}

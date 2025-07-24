import Image from 'next/image';
// import { motion } from 'framer-motion'; // Uncomment if using animations

export default function Hero() {
  return (
    <div className="flex flex-col-reverse md:flex-row items-center justify-between gap-10 px-6 py-20 max-w-7xl mx-auto">
      {/* Text Content */}
      <div className="text-center md:text-left space-y-6">
        <h1 className="text-4xl sm:text-5xl font-bold text-[var(--color-primary)] leading-tight">
          Hi, I'm Zainab 👋
        </h1>
        <p className="text-lg sm:text-xl text-[var(--color-secondary)] max-w-xl">
          A passionate tech enthusiast blending creativity, code, and strategy. I build modern websites, apps, and AI-powered tools to make life smarter and more fun.
        </p>
        <a
          href="#projects"
          className="inline-block bg-[var(--color-accent)] text-white px-6 py-3 rounded-xl hover:bg-pink-600 transition duration-300 shadow-md"
        >
          View My Work 🚀
        </a>
      </div>

      {/* Profile Image */}
      <div className="flex-shrink-0">
        <div className="rounded-full overflow-hidden w-60 h-60 border-4 border-[var(--color-accent)] shadow-lg">
          <Image
            src="/profile.jpg"
            alt="Zainab's profile"
            width={240}
            height={240}
            className="object-cover w-full h-full"
            priority
          />
        </div>
      </div>
    </div>
  );
}

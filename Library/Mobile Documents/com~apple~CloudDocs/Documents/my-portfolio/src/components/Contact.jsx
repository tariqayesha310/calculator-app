'use client';
import { useState } from 'react';

export default function Contact() {
  const [formSubmitted, setFormSubmitted] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 via-white to-purple-100 py-10 px-6">
      <div className="max-w-2xl mx-auto bg-white p-10 rounded-xl shadow-xl">
        <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">Contact Me</h2>

        {formSubmitted ? (
          <p className="text-green-600 text-center text-lg font-medium">
            ✅ Thanks! Your message has been sent.
          </p>
        ) : (
          <form
            action="https://formspree.io/f/mgvzkepb"
            method="POST"
            onSubmit={() => setFormSubmitted(true)}
            className="space-y-6"
          >
            <div>
              <label className="block text-sm font-medium text-gray-700">Your Name</label>
              <input
                type="text"
                name="name"
                required
                className="mt-1 p-3 w-full border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Your Email</label>
              <input
                type="email"
                name="email"
                required
                className="mt-1 p-3 w-full border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700">Message</label>
              <textarea
                name="message"
                rows="5"
                required
                className="mt-1 p-3 w-full border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-400"
              ></textarea>
            </div>

            <button
              type="submit"
              className="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition-colors"
            >
              Send Message
            </button>
          </form>
        )}
      </div>
    </div>
  );
}

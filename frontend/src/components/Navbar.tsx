export default function Navbar() {
  return (
    <nav className="border-b border-slate-800 bg-slate-900">
      <div className="mx-auto flex max-w-7xl items-center justify-between p-6">

        <h1 className="text-3xl font-bold text-cyan-400">
          AI Code Review Assistant
        </h1>

        <div className="text-slate-400">
          RAG + Gemini
        </div>

      </div>
    </nav>
  );
}
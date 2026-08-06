export default function Loading() {
  return (
    <div className="flex items-center gap-3 py-8">
      <div className="h-6 w-6 animate-spin rounded-full border-4 border-cyan-500 border-t-transparent" />
      <p className="text-slate-300">
        AI is thinking...
      </p>
    </div>
  );
}
import { useState } from "react";
import { api } from "../services/api";
import Loading from "./Loading";
import MarkdownViewer from "./MarkdownViewer";

interface Props {
  repository: string;
}

export default function RepositorySummary({ repository }: Props) {
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const generateSummary = async () => {
    if (!repository.trim()) {
      alert("Please enter repository name.");
      return;
    }

    try {
      setLoading(true);
      setSummary("");
      setError("");

      const response = await api.post("/repository/summary", {
        repository,
      });

      // Supports either "summary" or "answer"
      setSummary(response.data.summary || response.data.answer || "");
    } catch (err: any) {
      console.error(err);

      if (err.response?.data?.detail) {
        setError(err.response.data.detail);
      } else {
        setError("Unable to generate repository summary.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-2xl font-bold text-cyan-400">
        📚 Repository Summary
      </h2>

      <button
        onClick={generateSummary}
        disabled={loading}
        className="rounded-lg bg-cyan-500 px-6 py-3 font-semibold text-white transition hover:bg-cyan-600 disabled:opacity-50"
      >
        {loading ? "Generating..." : "Generate Summary"}
      </button>

      <div className="mt-8">

        {loading && <Loading />}

        {error && (
          <div className="rounded-lg border border-red-500 bg-red-900/20 p-4 text-red-300">
            {error}
          </div>
        )}

        {!loading && !error && !summary && (
          <div className="rounded-lg border border-slate-700 bg-slate-950 p-6 text-slate-400">
            Click the button above to generate an AI summary of the repository.
          </div>
        )}

        {summary && (
          <div className="rounded-lg border border-slate-700 bg-slate-950 p-6">
            <MarkdownViewer text={summary} />
          </div>
        )}

      </div>

    </div>
  );
}
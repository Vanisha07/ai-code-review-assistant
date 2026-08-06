import { useState } from "react";
import { api } from "../services/api";
import Loading from "./Loading";
import MarkdownViewer from "./MarkdownViewer";

interface Props {
  repository: string;
}

export default function AIReview({ repository }: Props) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askAI = async () => {
    if (!repository.trim()) {
      alert("Please enter a repository name.");
      return;
    }

    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    try {
      setLoading(true);
      setAnswer("");

      const response = await api.post("/repository/review", {
        repository,
        question,
      });

      setAnswer(response.data.answer);
    } catch (error: any) {
      console.error(error);

      if (error.response) {
        setAnswer(
          error.response.data.detail ||
            "Backend returned an error."
        );
      } else {
        setAnswer("Unable to connect to backend.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-2xl font-bold text-cyan-400">
        🤖 AI Repository Review
      </h2>

      <textarea
        rows={5}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Example: How does authentication work?"
        className="mb-5 w-full rounded-lg border border-slate-700 bg-slate-800 p-4 outline-none transition focus:border-cyan-400"
      />

      <button
        onClick={askAI}
        disabled={loading}
        className="rounded-lg bg-cyan-500 px-6 py-3 font-semibold transition hover:bg-cyan-600 disabled:cursor-not-allowed disabled:opacity-50"
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      <div className="mt-8 rounded-lg border border-slate-700 bg-slate-950 p-6">

        {loading ? (
          <Loading />
        ) : answer ? (
          <MarkdownViewer text={answer} />
        ) : (
          <p className="text-slate-400">
            Ask any question about your repository.
          </p>
        )}

      </div>

    </div>
  );
}
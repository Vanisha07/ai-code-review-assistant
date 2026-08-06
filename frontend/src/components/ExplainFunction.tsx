import { useState } from "react";
import { api } from "../services/api";
import Loading from "./Loading";
import MarkdownViewer from "./MarkdownViewer";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

interface Props {
  repository: string;
}

interface ExplainResponse {
  file: string;
  class: string | null;
  line: number;
  signature: string;
  language: string;
  code: string;
  explanation: string;
}

export default function ExplainFunction({ repository }: Props) {
  const [functionName, setFunctionName] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<ExplainResponse | null>(null);
  const [error, setError] = useState("");

  const explainFunction = async () => {
    if (!repository.trim()) {
      alert("Enter repository name.");
      return;
    }

    if (!functionName.trim()) {
      alert("Enter function name.");
      return;
    }

    try {
      setLoading(true);
      setError("");
      setResult(null);

      const response = await api.post("/repository/explain-function", {
        repository,
        function_name: functionName,
      });

      setResult(response.data);
    } catch (err: any) {
      console.error(err);

      setError(
        err.response?.data?.detail ||
        "Unable to explain function."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-2xl font-bold text-cyan-400">
        📖 Explain Function
      </h2>

      <div className="flex gap-4">

        <input
          value={functionName}
          onChange={(e) => setFunctionName(e.target.value)}
          placeholder="Example: post"
          className="flex-1 rounded-lg border border-slate-700 bg-slate-800 p-3 text-white outline-none focus:border-cyan-400"
        />

        <button
          onClick={explainFunction}
          disabled={loading}
          className="rounded-lg bg-cyan-500 px-6 py-3 font-semibold hover:bg-cyan-600 disabled:opacity-50"
        >
          {loading ? "Explaining..." : "Explain"}
        </button>

      </div>

      <div className="mt-8">

        {loading && <Loading />}

        {error && (
          <div className="rounded-lg border border-red-500 bg-red-900/20 p-4 text-red-300">
            {error}
          </div>
        )}

        {!loading && !error && !result && (
          <div className="rounded-lg border border-slate-700 bg-slate-950 p-6 text-slate-400">
            Enter a function name and click Explain.
          </div>
        )}

        {result && (

          <div className="space-y-6">

            <div className="rounded-lg border border-slate-700 bg-slate-950 p-5">

              <h3 className="mb-4 text-xl font-bold text-cyan-400">
                📄 Function Information
              </h3>

              <div className="grid gap-2 text-slate-300">

                <div>
                  <strong>File:</strong> {result.file}
                </div>

                <div>
                  <strong>Line:</strong> {result.line}
                </div>

                <div>
                  <strong>Language:</strong> {result.language}
                </div>

                {result.class && (
                  <div>
                    <strong>Class:</strong> {result.class}
                  </div>
                )}

              </div>

            </div>

            <div className="rounded-lg border border-slate-700 bg-slate-950 p-5">

              <h3 className="mb-4 text-xl font-bold text-cyan-400">
                Function Signature
              </h3>

              <pre className="overflow-auto rounded bg-slate-900 p-4 text-green-400">
                {result.signature}
              </pre>

            </div>

            <div className="rounded-lg border border-slate-700 bg-slate-950 p-5">

              <h3 className="mb-4 text-xl font-bold text-cyan-400">
                Source Code
              </h3>

              <SyntaxHighlighter
                language={result.language.toLowerCase()}
                style={oneDark}
                customStyle={{
                  borderRadius: "10px",
                  fontSize: "14px",
                }}
              >
                {result.code}
              </SyntaxHighlighter>

            </div>

            <div className="rounded-lg border border-slate-700 bg-slate-950 p-5">

              <h3 className="mb-4 text-xl font-bold text-cyan-400">
                🤖 AI Explanation
              </h3>

              <MarkdownViewer text={result.explanation} />

            </div>

          </div>

        )}

      </div>

    </div>
  );
}
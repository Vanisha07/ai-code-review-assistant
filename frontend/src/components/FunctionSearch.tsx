import { useState } from "react";
import { api } from "../services/api";
import Loading from "./Loading";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

interface Props {
  repository: string;
}

interface FunctionMatch {
  file: string;
  line: number;
  class: string | null;
  signature: string;
  language: string;
  code: string;
}

export default function FunctionSearch({ repository }: Props) {
  const [functionName, setFunctionName] = useState("");
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState<FunctionMatch[]>([]);
  const [error, setError] = useState("");

  const searchFunction = async () => {
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
      setResults([]);

      const response = await api.post("/repository/function", {
        repository,
        function_name: functionName,
      });

      setResults(response.data.matches || []);
    } catch (err: any) {
      console.error(err);

      setError(
        err.response?.data?.detail ||
        "Unable to search function."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-2xl font-bold text-cyan-400">
        🔍 Function Search
      </h2>

      <div className="flex gap-4">

        <input
          value={functionName}
          onChange={(e) => setFunctionName(e.target.value)}
          placeholder="Example: get"
          className="flex-1 rounded-lg border border-slate-700 bg-slate-800 p-3 text-white outline-none focus:border-cyan-400"
        />

        <button
          onClick={searchFunction}
          disabled={loading}
          className="rounded-lg bg-cyan-500 px-6 py-3 font-semibold hover:bg-cyan-600 disabled:opacity-50"
        >
          {loading ? "Searching..." : "Search"}
        </button>

      </div>

      <div className="mt-8">

        {loading && <Loading />}

        {error && (
          <div className="rounded-lg border border-red-500 bg-red-900/20 p-4 text-red-300">
            {error}
          </div>
        )}

        {!loading && !error && results.length === 0 && (
          <div className="rounded-lg border border-slate-700 bg-slate-950 p-6 text-slate-400">
            Search any function in the repository.
          </div>
        )}

        <div className="space-y-8">

          {results.map((item, index) => (

            <div
              key={index}
              className="rounded-xl border border-slate-700 bg-slate-950 p-6"
            >

              <div className="mb-5 flex flex-wrap gap-3">

                <span className="rounded bg-cyan-500/20 px-3 py-1 text-cyan-300">
                  📄 {item.file}
                </span>

                <span className="rounded bg-slate-800 px-3 py-1">
                  📍 Line {item.line}
                </span>

                <span className="rounded bg-slate-800 px-3 py-1">
                  {item.language}
                </span>

                {item.class && (
                  <span className="rounded bg-slate-800 px-3 py-1">
                    🏛 {item.class}
                  </span>
                )}

              </div>

              <div className="mb-4">

                <h3 className="mb-2 text-lg font-semibold text-cyan-400">
                  Function Signature
                </h3>

                <pre className="rounded bg-slate-900 p-4 text-green-400 overflow-auto">
                  {item.signature}
                </pre>

              </div>

              {item.code && (

                <div>

                  <h3 className="mb-2 text-lg font-semibold text-cyan-400">
                    Source Code
                  </h3>

                  <SyntaxHighlighter
                    language={item.language.toLowerCase()}
                    style={oneDark}
                    customStyle={{
                      borderRadius: "10px",
                      fontSize: "14px",
                    }}
                  >
                    {item.code}
                  </SyntaxHighlighter>

                </div>

              )}

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}
import { useState } from "react";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";

import AIReview from "../components/AIReview";
import FunctionSearch from "../components/FunctionSearch";
import ExplainFunction from "../components/ExplainFunction";
import RepositorySummary from "../components/RepositorySummary";

export default function Dashboard() {
  const [repository, setRepository] = useState("requests");

  const [tab, setTab] = useState("AI Review");

  return (
    <div className="min-h-screen bg-slate-950 text-white">

      <Navbar />

      <div className="flex">

        <Sidebar
          tab={tab}
          setTab={setTab}
        />

        <main className="flex-1 p-8">

          {/* Repository */}

          <div className="mb-8 rounded-xl border border-slate-800 bg-slate-900 p-6">

            <h2 className="mb-5 text-2xl font-bold text-cyan-400">
              Repository
            </h2>

            <input
              value={repository}
              onChange={(e) =>
                setRepository(e.target.value)
              }
              placeholder="requests"
              className="w-full rounded-lg border border-slate-700 bg-slate-800 p-3 outline-none transition focus:border-cyan-400"
            />

            <p className="mt-3 text-sm text-slate-400">
              Enter the repository name that has already
              been cloned and indexed.
            </p>

          </div>

          {/* Content */}

          {tab === "AI Review" && (
            <AIReview repository={repository} />
          )}

          {tab === "Function Search" && (
            <FunctionSearch repository={repository} />
          )}

          {tab === "Explain Function" && (
            <ExplainFunction repository={repository} />
          )}

          {tab === "Repository Summary" && (
            <RepositorySummary repository={repository} />
          )}

        </main>

      </div>

    </div>
  );
}
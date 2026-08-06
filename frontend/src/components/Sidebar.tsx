interface Props {
  tab: string;
  setTab: (tab: string) => void;
}

const tabs = [
  "AI Review",
  "Function Search",
  "Explain Function",
  "Repository Summary",
];

export default function Sidebar({
  tab,
  setTab,
}: Props) {
  return (
    <aside className="w-72 border-r border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-xl font-bold">
        Features
      </h2>

      <div className="space-y-3">

        {tabs.map((item) => (

          <button
            key={item}
            onClick={() => setTab(item)}
            className={`w-full rounded-lg p-3 text-left transition

            ${
              tab === item
                ? "bg-cyan-500 text-white"
                : "bg-slate-800 hover:bg-slate-700"
            }
            `}
          >
            {item}
          </button>

        ))}

      </div>

    </aside>
  );
}
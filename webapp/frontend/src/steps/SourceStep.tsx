import PlatformCard from "../components/PlatformCard";
import Markdown from "../components/Markdown";
import type { SourcePlatform } from "../types";

interface Props {
  sources: SourcePlatform[];
  selectedId: string | null;
  onSelect: (id: string) => void;
  onNext: () => void;
}

export default function SourceStep({ sources, selectedId, onSelect, onNext }: Props) {
  const selected = sources.find((s) => s.id === selectedId) || null;

  return (
    <div className="panel">
      <h2>Choose your source platform</h2>
      <p className="subtitle">
        Where does the application you want to migrate currently live?
      </p>

      <div className="card-grid">
        {sources.map((s) => (
          <PlatformCard
            key={s.id}
            name={s.label}
            description={s.implemented ? undefined : "Coming soon"}
            badge={
              !s.implemented
                ? { text: "Coming soon", kind: "soon" }
                : s.transformation === "deterministic"
                ? { text: "Deterministic", kind: "deterministic" }
                : { text: "LLM-based", kind: "llm" }
            }
            selected={selectedId === s.id}
            disabled={!s.implemented}
            onClick={() => onSelect(s.id)}
          />
        ))}
      </div>

      {selected && (
        <div className={`banner ${selected.transformation === "llm" ? "llm" : ""}`}>
          <Markdown text={selected.banner} />
        </div>
      )}

      <div className="actions">
        <span />
        <button className="btn primary" disabled={!selected} onClick={onNext}>
          Continue →
        </button>
      </div>
    </div>
  );
}

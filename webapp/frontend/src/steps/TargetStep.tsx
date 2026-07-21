import PlatformCard from "../components/PlatformCard";
import type { TargetPlatform } from "../types";

interface Props {
  targets: TargetPlatform[];
  selectedId: string | null;
  onSelect: (id: string) => void;
  loading: boolean;
  error: string | null;
  onBack: () => void;
  onGenerate: () => void;
}

export default function TargetStep({
  targets, selectedId, onSelect, loading, error, onBack, onGenerate,
}: Props) {
  const selected = targets.find((t) => t.id === selectedId) || null;

  return (
    <div className="panel">
      <h2>Choose your target platform</h2>
      <p className="subtitle">
        The pivot model will be transformed into ready-to-import artifacts for this platform.
      </p>

      <div className="card-grid">
        {targets.map((t) => (
          <PlatformCard
            key={t.id}
            name={t.label}
            description={t.implemented ? t.output_desc : "Coming soon"}
            badge={t.implemented ? undefined : { text: "Coming soon", kind: "soon" }}
            selected={selectedId === t.id}
            disabled={!t.implemented}
            onClick={() => onSelect(t.id)}
          />
        ))}
      </div>

      {selected?.note && <div className="alert warn">{selected.note}</div>}
      {error && <div className="alert error">{error}</div>}

      <div className="actions">
        <button className="btn ghost" onClick={onBack} disabled={loading}>← Back</button>
        <button className="btn primary" onClick={onGenerate} disabled={!selected || loading}>
          {loading ? <><span className="spinner" />Generating artifacts…</> : "Generate artifacts →"}
        </button>
      </div>
    </div>
  );
}

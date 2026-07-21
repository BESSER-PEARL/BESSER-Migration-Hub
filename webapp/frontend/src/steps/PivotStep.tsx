import { pivotDownloadUrl } from "../api";
import type { PivotResponse } from "../types";

interface Props {
  pivot: PivotResponse;
  onBack: () => void;
  onNext: () => void;
}

function Stat({ value, label }: { value: number | null | undefined; label: string }) {
  if (value === null || value === undefined) return null;
  return (
    <div className="stat">
      <div className="value">{value}</div>
      <div className="label">{label}</div>
    </div>
  );
}

export default function PivotStep({ pivot, onBack, onNext }: Props) {
  const s = pivot.summary;
  const hasGui = s.screens !== null && s.screens !== undefined;

  return (
    <div className="panel">
      <h2>Pivot model generated ✓</h2>
      <p className="subtitle">
        Your source model has been transformed into the platform-independent B-UML pivot model.
      </p>

      <h3 style={{ margin: "4px 0 4px" }}>Data model</h3>
      <div className="summary-grid">
        <Stat value={s.classes} label="Classes" />
        <Stat value={s.attributes} label="Attributes" />
        <Stat value={s.associations} label="Associations" />
        <Stat value={s.enumerations} label="Enumerations" />
      </div>
      {s.class_names.length > 0 && (
        <div className="chips">
          {s.class_names.map((c) => <span key={c} className="chip">{c}</span>)}
        </div>
      )}

      {hasGui && (
        <>
          <h3 style={{ margin: "18px 0 4px" }}>GUI model</h3>
          <div className="summary-grid">
            <Stat value={s.modules} label="Modules" />
            <Stat value={s.screens} label="Screens" />
            <Stat value={s.widgets} label="Widgets" />
          </div>
        </>
      )}

      {pivot.warnings.length > 0 && (
        <div className="alert warn">
          {pivot.warnings.map((w, i) => <div key={i}>{w}</div>)}
        </div>
      )}

      <div className="field">
        <label>Download the pivot model</label>
        <div className="btn-row">
          {pivot.downloads.filter((d) => d.available).map((d) => (
            <a
              key={d.artifact}
              className="download-link"
              href={pivotDownloadUrl(pivot.session_id, d.artifact)}
            >
              ⬇ {d.artifact === "domain" ? "Domain model" : "GUI model"} ({d.filename})
            </a>
          ))}
          <a className="download-link" href={pivotDownloadUrl(pivot.session_id, "all")}>
            ⬇ All (.zip)
          </a>
        </div>
        {pivot.downloads.filter((d) => d.note).map((d) => (
          <div key={`note-${d.artifact}`} className="hint" style={{ marginTop: 8 }}>{d.note}</div>
        ))}
      </div>

      <div className="actions">
        <button className="btn ghost" onClick={onBack}>← Back</button>
        <button className="btn primary" onClick={onNext}>Choose a target platform →</button>
      </div>
    </div>
  );
}

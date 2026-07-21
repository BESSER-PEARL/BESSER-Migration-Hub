import Markdown from "../components/Markdown";
import { artifactDownloadUrl } from "../api";
import type { GenerateResponse, TargetPlatform } from "../types";

interface Props {
  result: GenerateResponse;
  target: TargetPlatform | null;
  onBack: () => void;
  onRestart: () => void;
}

export default function ArtifactsStep({ result, target, onBack, onRestart }: Props) {
  return (
    <div className="panel">
      <h2>Your artifacts are ready ✓</h2>
      <p className="subtitle">
        Generated for <strong>{target?.label ?? result.target_lcp}</strong>. Download them and follow
        the import guide below.
      </p>

      <div className="field">
        <label>Generated files</label>
        <div className="btn-row">
          {result.artifacts.map((a) => (
            <a
              key={a.name}
              className="download-link"
              href={artifactDownloadUrl(result.session_id, a.name)}
              title={a.description}
            >
              ⬇ {a.name}
            </a>
          ))}
          {result.artifacts.length > 1 && (
            <a className="download-link" href={artifactDownloadUrl(result.session_id, "all")}>
              ⬇ All (.zip)
            </a>
          )}
        </div>
      </div>

      {result.warnings.length > 0 && (
        <div className="alert warn">
          {result.warnings.map((w, i) => <div key={i}>{w}</div>)}
        </div>
      )}

      {result.tutorial && (
        <div className="tutorial">
          <Markdown text={result.tutorial} />
        </div>
      )}

      <div className="actions">
        <button className="btn ghost" onClick={onBack}>← Pick another target</button>
        <button className="btn" onClick={onRestart}>Start a new migration</button>
      </div>
    </div>
  );
}

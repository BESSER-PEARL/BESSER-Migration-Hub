import Markdown from "../components/Markdown";
import FileDropzone from "../components/FileDropzone";
import { artifactDownloadUrl } from "../api";
import type { GenerateResponse, TargetPlatform } from "../types";

interface Props {
  result: GenerateResponse;
  target: TargetPlatform | null;
  hasGuiModel: boolean;
  apexExport: File | null;
  setApexExport: (file: File | null) => void;
  guiLoading: boolean;
  guiError: string | null;
  onGenerateGui: () => void;
  onBack: () => void;
  onRestart: () => void;
}

export default function ArtifactsStep({
  result, target, hasGuiModel, apexExport, setApexExport,
  guiLoading, guiError, onGenerateGui, onBack, onRestart,
}: Props) {
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

      {target?.id === "oracle_apex" && hasGuiModel && (
        <div className="field">
          <label>Continue with Oracle APEX GUI pages</label>
          <div className="hint">
            Import and run the table SQL above in **SQL Workshop &gt; SQL Scripts**.
            Accept APEX's prompt to create the application and its pages, open
            that application, then export it with **Custom Export** and
            **Split into multiple files**. Zip the exported folder and upload it
            here. The hub will then generate the GUI page SQL for the final app.
          </div>
          <FileDropzone
            accept={[".zip"]}
            multiple={false}
            files={apexExport ? [apexExport] : []}
            onChange={(files) => setApexExport(files[0] ?? null)}
          />
          {guiError && <div className="alert error">{guiError}</div>}
          <div className="btn-row" style={{ marginTop: 12 }}>
            <button
              className="btn primary"
              onClick={onGenerateGui}
              disabled={!apexExport || guiLoading}
            >
              {guiLoading ? <><span className="spinner" />Generating GUI pages…</> : "Generate GUI page SQL"}
            </button>
          </div>
        </div>
      )}

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

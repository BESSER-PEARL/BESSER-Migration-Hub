import { useEffect, useState } from "react";
import FileDropzone from "../components/FileDropzone";
import ScopeSelector from "../components/ScopeSelector";
import { fetchMendixModules } from "../api";
import type { Scope, SourcePlatform } from "../types";

interface Props {
  source: SourcePlatform;
  /** Flat file list — used for non-split-upload sources. */
  files: File[];
  setFiles: (f: File[]) => void;
  /** Split upload — data model files only. */
  dataFiles: File[];
  setDataFiles: (f: File[]) => void;
  /** Split upload — GUI model files only. */
  guiFiles: File[];
  setGuiFiles: (f: File[]) => void;
  scope: Scope;
  setScope: (s: Scope) => void;
  moduleName: string | null;
  setModuleName: (m: string | null) => void;
  openaiToken: string;
  setOpenaiToken: (t: string) => void;
  loading: boolean;
  error: string | null;
  onBack: () => void;
  onSubmit: () => void;
}

export default function UploadStep(props: Props) {
  const {
    source,
    files, setFiles,
    dataFiles, setDataFiles,
    guiFiles, setGuiFiles,
    scope, setScope,
    moduleName, setModuleName,
    openaiToken, setOpenaiToken,
    loading, error, onBack, onSubmit,
  } = props;

  const [modules, setModules] = useState<string[]>([]);
  const [moduleError, setModuleError] = useState<string | null>(null);
  const [loadingModules, setLoadingModules] = useState(false);

  // For sources requiring a module (Mendix), inspect the uploaded JSON.
  useEffect(() => {
    if (!source.needs_module) return;
    const json = files.find((f) => f.name.toLowerCase().endsWith(".json"));
    if (!json) { setModules([]); setModuleName(null); return; }
    let cancelled = false;
    setLoadingModules(true);
    setModuleError(null);
    fetchMendixModules(json)
      .then((mods) => {
        if (cancelled) return;
        setModules(mods);
        setModuleName(moduleName && mods.includes(moduleName) ? moduleName : mods[0] ?? null);
      })
      .catch((e) => { if (!cancelled) setModuleError(e.message); })
      .finally(() => { if (!cancelled) setLoadingModules(false); });
    return () => { cancelled = true; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [files, source.needs_module]);

  const wantData = scope === "data" || scope === "both";
  const wantGui  = scope === "gui"  || scope === "both";

  let canSubmit: boolean;
  if (source.split_upload) {
    canSubmit =
      (!wantData || dataFiles.length > 0) &&
      (!wantGui  || guiFiles.length > 0) &&
      (!source.needs_openai || openaiToken.trim().length > 0) &&
      !loading;
  } else {
    canSubmit =
      files.length > 0 &&
      (!source.needs_module || !!moduleName) &&
      (!source.needs_openai || openaiToken.trim().length > 0) &&
      !loading;
  }

  return (
    <div className="panel">
      <h2>Upload your model &amp; choose the scope</h2>
      <p className="subtitle">{source.input_hint}</p>

      {/* ── Split upload: separate zones for data model and GUI ── */}
      {source.split_upload ? (
        <>
          {wantData && (
            <div className="field">
              <label>Data model files</label>
              <div className="hint">{source.data_hint}</div>
              <FileDropzone
                accept={source.data_extensions}
                multiple={source.data_allow_multiple}
                files={dataFiles}
                onChange={setDataFiles}
              />
            </div>
          )}
          {wantGui && (
            <div className="field" style={{ marginTop: wantData ? 16 : 0 }}>
              <label>GUI model files</label>
              <div className="hint">{source.gui_hint}</div>
              <FileDropzone
                accept={source.gui_extensions}
                multiple={source.gui_allow_multiple}
                files={guiFiles}
                onChange={setGuiFiles}
              />
            </div>
          )}
        </>
      ) : (
        /* ── Standard single dropzone ── */
        <FileDropzone
          accept={source.accepted_extensions.concat(source.allow_csv ? [".csv"] : [])}
          multiple={source.allow_multiple}
          files={files}
          onChange={setFiles}
        />
      )}

      {source.needs_module && (
        <div className="field">
          <label>Mendix module</label>
          <div className="hint">Detected from your export — pick the module to migrate.</div>
          {loadingModules ? (
            <div className="muted"><span className="spinner" />Reading modules…</div>
          ) : moduleError ? (
            <div className="alert error">{moduleError}</div>
          ) : (
            <select
              value={moduleName ?? ""}
              disabled={modules.length === 0}
              onChange={(e) => setModuleName(e.target.value || null)}
            >
              {modules.length === 0 && <option value="">Upload a Mendix JSON first</option>}
              {modules.map((m) => (
                <option key={m} value={m}>{m}</option>
              ))}
            </select>
          )}
        </div>
      )}

      {source.needs_openai && (
        <div className="field">
          <label>OpenAI API key</label>
          <div className="hint">Used only for this request to run the visual LLM extraction. Not stored.</div>
          <input
            type="password"
            placeholder="sk-…"
            value={openaiToken}
            onChange={(e) => setOpenaiToken(e.target.value)}
          />
        </div>
      )}

      <div className="field">
        <label>What to generate</label>
        <ScopeSelector value={scope} guiSupported={source.supports_gui} onChange={setScope} />
        {!source.supports_gui && (
          <div className="hint" style={{ marginTop: 8 }}>
            GUI extraction is not available for {source.label} yet — only the data model can be generated.
          </div>
        )}
      </div>

      {error && <div className="alert error">{error}</div>}

      <div className="actions">
        <button className="btn ghost" onClick={onBack} disabled={loading}>← Back</button>
        <button className="btn primary" onClick={onSubmit} disabled={!canSubmit}>
          {loading ? <><span className="spinner" />Generating pivot…</> : "Generate pivot model →"}
        </button>
      </div>
    </div>
  );
}

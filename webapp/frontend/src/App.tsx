import { useEffect, useState } from "react";
import Stepper from "./components/Stepper";
import SourceStep from "./steps/SourceStep";
import UploadStep from "./steps/UploadStep";
import PivotStep from "./steps/PivotStep";
import TargetStep from "./steps/TargetStep";
import ArtifactsStep from "./steps/ArtifactsStep";
import { createPivot, fetchPlatforms, generateArtifacts, uploadApexExport } from "./api";
import type {
  GenerateResponse,
  Platforms,
  PivotResponse,
  Scope,
} from "./types";

const STEPS = ["Source", "Upload", "Pivot", "Target", "Artifacts"];

export default function App() {
  const [platforms, setPlatforms] = useState<Platforms | null>(null);
  const [loadError, setLoadError] = useState<string | null>(null);

  const [step, setStep] = useState(0);

  // Wizard state
  const [sourceId, setSourceId] = useState<string | null>(null);
  const [files, setFiles] = useState<File[]>([]);
  const [scope, setScope] = useState<Scope>("data");
  const [moduleName, setModuleName] = useState<string | null>(null);
  const [openaiToken, setOpenaiToken] = useState("");

  const [pivot, setPivot] = useState<PivotResponse | null>(null);
  const [targetId, setTargetId] = useState<string | null>(null);
  const [apexExport, setApexExport] = useState<File | null>(null);
  const [generateResult, setGenerateResult] = useState<GenerateResponse | null>(null);

  const [busy, setBusy] = useState(false);
  const [stepError, setStepError] = useState<string | null>(null);
  const [guiError, setGuiError] = useState<string | null>(null);

  useEffect(() => {
    fetchPlatforms().then(setPlatforms).catch((e) => setLoadError(e.message));
  }, []);

  const source = platforms?.sources.find((s) => s.id === sourceId) ?? null;
  const target = platforms?.targets.find((t) => t.id === targetId) ?? null;

  // When the source changes, reset downstream state and default the scope.
  const selectSource = (id: string) => {
    setSourceId(id);
    const s = platforms?.sources.find((x) => x.id === id);
    setScope(s && !s.supports_gui ? "data" : "both");
    setFiles([]);
    setModuleName(null);
    setPivot(null);
    setStepError(null);
  };

  const submitPivot = async () => {
    if (!source) return;
    setBusy(true);
    setStepError(null);
    try {
      const result = await createPivot({
        sourceLcp: source.id,
        scope,
        moduleName,
        openaiToken,
        files,
      });
      setPivot(result);
      setStep(2);
    } catch (e) {
      setStepError((e as Error).message);
    } finally {
      setBusy(false);
    }
  };

  const runGenerate = async () => {
    if (!pivot || !targetId) return;
    setBusy(true);
    setStepError(null);
    try {
      const result = await generateArtifacts(pivot.session_id, targetId);
      setGenerateResult(result);
      setStep(4);
    } catch (e) {
      setStepError((e as Error).message);
    } finally {
      setBusy(false);
    }
  };

  const runApexGuiGenerate = async () => {
    if (!pivot || !apexExport) return;
    setBusy(true);
    setGuiError(null);
    try {
      await uploadApexExport(pivot.session_id, apexExport);
      const result = await generateArtifacts(pivot.session_id, "oracle_apex");
      setGenerateResult(result);
    } catch (e) {
      setGuiError((e as Error).message);
    } finally {
      setBusy(false);
    }
  };

  const selectTarget = (id: string) => {
    setTargetId(id);
    setApexExport(null);
  };

  const restart = () => {
    setStep(0);
    setSourceId(null);
    setFiles([]);
    setScope("data");
    setModuleName(null);
    setOpenaiToken("");
    setPivot(null);
    setTargetId(null);
    setApexExport(null);
    setGenerateResult(null);
    setStepError(null);
    setGuiError(null);
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1><span className="brand">BESSER</span> Migration Hub</h1>
        <p>Migrate applications across low-code platforms through the B-UML pivot model.</p>
      </header>

      <Stepper steps={STEPS} current={step} />

      {loadError && <div className="alert error">Could not load platforms: {loadError}</div>}
      {!platforms && !loadError && <div className="panel muted"><span className="spinner" />Loading…</div>}

      {platforms && step === 0 && (
        <SourceStep
          sources={platforms.sources}
          selectedId={sourceId}
          onSelect={selectSource}
          onNext={() => setStep(1)}
        />
      )}

      {platforms && step === 1 && source && (
        <UploadStep
          source={source}
          files={files}
          setFiles={setFiles}
          scope={scope}
          setScope={setScope}
          moduleName={moduleName}
          setModuleName={setModuleName}
          openaiToken={openaiToken}
          setOpenaiToken={setOpenaiToken}
          loading={busy}
          error={stepError}
          onBack={() => { setStepError(null); setStep(0); }}
          onSubmit={submitPivot}
        />
      )}

      {platforms && step === 2 && pivot && (
        <PivotStep
          pivot={pivot}
          onBack={() => setStep(1)}
          onNext={() => { setStepError(null); setStep(3); }}
        />
      )}

      {platforms && step === 3 && (
        <TargetStep
          targets={platforms.targets}
          selectedId={targetId}
          onSelect={selectTarget}
          loading={busy}
          error={stepError}
          hasDomainModel={pivot?.summary.classes !== null && pivot?.summary.classes !== undefined}
          onBack={() => { setStepError(null); setStep(2); }}
          onGenerate={runGenerate}
        />
      )}

      {platforms && step === 4 && generateResult && (
        <ArtifactsStep
          result={generateResult}
          target={target}
          hasGuiModel={pivot?.summary.screens !== null && pivot?.summary.screens !== undefined}
          apexExport={apexExport}
          setApexExport={setApexExport}
          guiLoading={busy}
          guiError={guiError}
          onGenerateGui={runApexGuiGenerate}
          onBack={() => { setStepError(null); setStep(3); }}
          onRestart={restart}
        />
      )}
    </div>
  );
}

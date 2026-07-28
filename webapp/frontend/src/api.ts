import type {
  GenerateResponse,
  Platforms,
  PivotResponse,
  Scope,
} from "./types";

async function handle<T>(res: Response): Promise<T> {
  if (!res.ok) {
    let detail = `Request failed (${res.status})`;
    try {
      const body = await res.json();
      if (body?.detail) detail = typeof body.detail === "string" ? body.detail : JSON.stringify(body.detail);
    } catch {
      /* ignore */
    }
    throw new Error(detail);
  }
  return (await res.json()) as T;
}

export async function fetchPlatforms(): Promise<Platforms> {
  return handle<Platforms>(await fetch("/api/platforms"));
}

export async function fetchMendixModules(file: File): Promise<string[]> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch("/api/mendix/modules", { method: "POST", body: form });
  const data = await handle<{ modules: string[] }>(res);
  return data.modules;
}

export interface PivotArgs {
  sourceLcp: string;
  scope: Scope;
  moduleName?: string | null;
  openaiToken?: string | null;
  files: File[];
}

export async function createPivot(args: PivotArgs): Promise<PivotResponse> {
  const form = new FormData();
  form.append("source_lcp", args.sourceLcp);
  form.append("scope", args.scope);
  if (args.moduleName) form.append("module_name", args.moduleName);
  if (args.openaiToken) form.append("openai_token", args.openaiToken);
  args.files.forEach((f) => form.append("files", f));
  return handle<PivotResponse>(
    await fetch("/api/pivot", { method: "POST", body: form })
  );
}

export async function generateArtifacts(
  sessionId: string,
  targetLcp: string
): Promise<GenerateResponse> {
  return handle<GenerateResponse>(
    await fetch(`/api/sessions/${sessionId}/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ target_lcp: targetLcp }),
    })
  );
}

export async function uploadApexExport(sessionId: string, file: File): Promise<void> {
  const form = new FormData();
  form.append("file", file);
  await handle<{ ready: boolean }>(
    await fetch(`/api/sessions/${sessionId}/apex-export`, {
      method: "POST",
      body: form,
    })
  );
}

export function pivotDownloadUrl(sessionId: string, artifact: string): string {
  return `/api/sessions/${sessionId}/download/pivot?artifact=${encodeURIComponent(artifact)}`;
}

export function artifactDownloadUrl(sessionId: string, name: string): string {
  return `/api/sessions/${sessionId}/download/artifacts?name=${encodeURIComponent(name)}`;
}

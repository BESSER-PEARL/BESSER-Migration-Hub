export interface SourcePlatform {
  id: string;
  label: string;
  transformation: "deterministic" | "llm";
  implemented: boolean;
  supports_data: boolean;
  supports_gui: boolean;
  accepted_extensions: string[];
  input_hint: string;
  allow_multiple: boolean;
  needs_module: boolean;
  needs_openai: boolean;
  allow_csv: boolean;
  banner: string;
}

export interface TargetPlatform {
  id: string;
  label: string;
  implemented: boolean;
  supports_data: boolean;
  supports_gui: boolean;
  generator: string | null;
  sql_dialect: string | null;
  output_desc: string;
  tutorial: string;
  note: string;
}

export interface Platforms {
  sources: SourcePlatform[];
  targets: TargetPlatform[];
}

export interface ModelSummary {
  classes?: number | null;
  attributes?: number | null;
  associations?: number | null;
  enumerations?: number | null;
  class_names: string[];
  modules?: number | null;
  screens?: number | null;
  widgets?: number | null;
  screen_names: string[];
}

export interface DownloadInfo {
  artifact: string;
  filename: string;
  available: boolean;
  note?: string | null;
}

export interface PivotResponse {
  session_id: string;
  source_lcp: string;
  scope: string;
  summary: ModelSummary;
  downloads: DownloadInfo[];
  warnings: string[];
}

export interface ArtifactInfo {
  name: string;
  description: string;
}

export interface GenerateResponse {
  session_id: string;
  target_lcp: string;
  artifacts: ArtifactInfo[];
  tutorial: string;
  warnings: string[];
}

export type Scope = "data" | "gui" | "both";

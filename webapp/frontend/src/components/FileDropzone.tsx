import { useRef, useState } from "react";

interface Props {
  accept: string[];        // e.g. [".json"] or [".png", ".csv"]
  multiple: boolean;
  files: File[];
  onChange: (files: File[]) => void;
}

export default function FileDropzone({ accept, multiple, files, onChange }: Props) {
  const inputRef = useRef<HTMLInputElement>(null);
  const [drag, setDrag] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const accepted = new Set(accept.map((extension) => extension.toLowerCase()));

  const add = (incoming: FileList | null) => {
    if (!incoming) return;
    const list = Array.from(incoming).filter((file) => {
      const extension = `.${file.name.split(".").pop()?.toLowerCase() ?? ""}`;
      return accepted.has(extension);
    });
    if (list.length !== incoming.length) {
      setError(`Please upload only ${accept.join(", ")} files.`);
    } else {
      setError(null);
    }
    if (list.length === 0) return;
    onChange(multiple ? [...files, ...list] : list.slice(0, 1));
  };

  const remove = (idx: number) => onChange(files.filter((_, i) => i !== idx));

  return (
    <div>
      <div
        className={`dropzone ${drag ? "drag" : ""}`}
        onClick={() => inputRef.current?.click()}
        onDragOver={(e) => { e.preventDefault(); setDrag(true); }}
        onDragLeave={() => setDrag(false)}
        onDrop={(e) => { e.preventDefault(); setDrag(false); add(e.dataTransfer.files); }}
      >
        <div className="big">Drop files here or click to browse</div>
        <div>Accepted: {accept.join(", ")}{multiple ? " · multiple allowed" : ""}</div>
        <input
          ref={inputRef}
          type="file"
          accept={accept.join(",")}
          multiple={multiple}
          style={{ display: "none" }}
          onChange={(e) => { add(e.target.files); e.target.value = ""; }}
        />
      </div>
      {error && <div className="alert error">{error}</div>}
      {files.length > 0 && (
        <ul className="file-list">
          {files.map((f, i) => (
            <li key={`${f.name}-${i}`}>
              <span>{f.name} <span className="muted">({Math.max(1, Math.round(f.size / 1024))} KB)</span></span>
              <button type="button" onClick={() => remove(i)}>remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

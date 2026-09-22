import type { Scope } from "../types";

interface Props {
  value: Scope;
  guiSupported: boolean;
  onChange: (scope: Scope) => void;
}

const OPTIONS: { value: Scope; label: string; description: string }[] = [
  { value: "data",  label: "Data model", description: "Extract the data model only." },
  { value: "both",  label: "Both",       description: "Extract the data model and the GUI model." },
];

export default function ScopeSelector({ value, guiSupported, onChange }: Props) {
  return (
    <div className="scope-options">
      {OPTIONS.map((opt) => {
        const disabled = opt.value === "both" && !guiSupported;
        return (
          <label
            key={opt.value}
            className={`scope-option ${value === opt.value ? "selected" : ""} ${disabled ? "disabled" : ""}`}
            title={disabled ? "GUI extraction is not available for this source yet." : ""}
          >
            <input
              type="radio"
              name="scope"
              checked={value === opt.value}
              disabled={disabled}
              onChange={() => onChange(opt.value)}
            />
            <span className="scope-text">
              <span className="scope-label">{opt.label}</span>
              <span className="scope-desc">{opt.description}</span>
            </span>
          </label>
        );
      })}
    </div>
  );
}

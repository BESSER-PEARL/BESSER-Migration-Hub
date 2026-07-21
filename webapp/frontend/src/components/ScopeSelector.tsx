import type { Scope } from "../types";

interface Props {
  value: Scope;
  guiSupported: boolean;
  onChange: (scope: Scope) => void;
}

const OPTIONS: { value: Scope; label: string }[] = [
  { value: "data", label: "Data model" },
  { value: "gui", label: "GUI model" },
  { value: "both", label: "Both" },
];

export default function ScopeSelector({ value, guiSupported, onChange }: Props) {
  return (
    <div className="scope-options">
      {OPTIONS.map((opt) => {
        const needsGui = opt.value === "gui" || opt.value === "both";
        const disabled = needsGui && !guiSupported;
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
            {opt.label}
          </label>
        );
      })}
    </div>
  );
}

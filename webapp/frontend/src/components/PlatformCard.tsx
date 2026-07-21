interface Props {
  name: string;
  description?: string;
  badge?: { text: string; kind: "deterministic" | "llm" | "soon" };
  selected?: boolean;
  disabled?: boolean;
  onClick?: () => void;
}

export default function PlatformCard({
  name,
  description,
  badge,
  selected,
  disabled,
  onClick,
}: Props) {
  return (
    <button
      type="button"
      className={`platform-card ${selected ? "selected" : ""}`}
      disabled={disabled}
      onClick={onClick}
    >
      {badge && <span className={`badge ${badge.kind}`}>{badge.text}</span>}
      <span className="name">{name}</span>
      {description && <span className="desc">{description}</span>}
    </button>
  );
}

interface Props {
  steps: string[];
  current: number;
}

export default function Stepper({ steps, current }: Props) {
  return (
    <div className="stepper">
      {steps.map((label, i) => {
        const cls = i === current ? "active" : i < current ? "done" : "";
        return (
          <div key={label} className={`step-pill ${cls}`}>
            <span className="num">{i < current ? "✓" : i + 1}</span>
            {label}
          </div>
        );
      })}
    </div>
  );
}

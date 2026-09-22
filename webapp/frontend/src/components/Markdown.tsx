/**
 * Minimal markdown renderer for the small subset used in banners and
 * tutorials: ### headings, ordered/unordered lists, **bold**, and `code`.
 * Avoids pulling in a full markdown dependency.
 */
interface Props {
  text: string;
}

function renderInline(text: string, keyBase: string) {
  // Split on **bold** and `code`, keeping the delimiters.
  const parts = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  return parts.map((part, i) => {
    const key = `${keyBase}-${i}`;
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={key}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith("`") && part.endsWith("`")) {
      return <code key={key}>{part.slice(1, -1)}</code>;
    }
    return <span key={key}>{part}</span>;
  });
}

export default function Markdown({ text }: Props) {
  const lines = text.split("\n");
  const blocks: JSX.Element[] = [];
  let list: { ordered: boolean; items: string[] } | null = null;

  const flushList = () => {
    if (!list) return;
    const items = list.items.map((it, i) => (
      <li key={i}>{renderInline(it, `li-${blocks.length}-${i}`)}</li>
    ));
    blocks.push(
      list.ordered ? <ol key={`b-${blocks.length}`}>{items}</ol> : <ul key={`b-${blocks.length}`}>{items}</ul>
    );
    list = null;
  };

  lines.forEach((raw) => {
    const line = raw.trimEnd();
    const h = line.match(/^(#{1,4})\s+(.*)$/);
    const ol = line.match(/^\d+\.\s+(.*)$/);
    const ul = line.match(/^[-*]\s+(.*)$/);

    if (h) {
      flushList();
      const level = h[1].length;
      const content = renderInline(h[2], `h-${blocks.length}`);
      blocks.push(
        level <= 3 ? <h3 key={`b-${blocks.length}`}>{content}</h3> : <h4 key={`b-${blocks.length}`}>{content}</h4>
      );
    } else if (ol) {
      if (!list || !list.ordered) { flushList(); list = { ordered: true, items: [] }; }
      list.items.push(ol[1]);
    } else if (ul) {
      if (!list || list.ordered) { flushList(); list = { ordered: false, items: [] }; }
      list.items.push(ul[1]);
    } else if (line.trim() === "") {
      flushList();
    } else {
      flushList();
      blocks.push(<p key={`b-${blocks.length}`}>{renderInline(line, `p-${blocks.length}`)}</p>);
    }
  });
  flushList();

  return <>{blocks}</>;
}

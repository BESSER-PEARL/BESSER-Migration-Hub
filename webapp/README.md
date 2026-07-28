# Migration Hub — Web Interface

A standalone web interface for the BESSER Migration Hub. It guides an end user
through migrating a low-code application from a **source** platform to a
**target** platform via the platform-independent **B-UML pivot model**.

It is a thin UI over the existing `migrator/` library — no migration logic is
reimplemented here.

```
webapp/
  backend/    FastAPI app wrapping the migrator parsers + generators
  frontend/   Vite + React + TypeScript wizard
```

## The 5-step wizard

1. **Source platform** — Mendix uses a *deterministic* transformation (dedicated
   parsers); screenshot-based sources use BESSER's *LLM-based mockup pipeline*.
2. **Upload & scope** — upload the Mendix export JSON (or screenshots for the LLM
   path) and choose **data model / GUI model / both**. For Mendix the module list
   is auto-detected into a dropdown.
3. **Pivot model** — see an extraction summary and download the B-UML model.
4. **Target platform** — pick where to migrate to; the fitting generator runs.
5. **Artifacts** — download the generated files and follow the import tutorial.

## Supported paths (v1)

| Source | Transformation | Data | GUI |
|--------|----------------|------|-----|
| Mendix | deterministic | ✅ | ✅ (parser)* |
| Power Apps | LLM (screenshot + CSVs, needs OpenAI key) | ✅ | 🔜 |
| OutSystems / Appian / Salesforce | LLM | 🔜 | 🔜 |

| Target | Output |
|--------|--------|
| Oracle APEX | `tables_oracle_apex.sql` |
| Power Apps (Excel) | `model.xlsx` |
| PostgreSQL / MySQL | `tables_<dialect>.sql` |
| OutSystems / Appian | 🔜 |

For Oracle APEX, the generated table script covers the data model. GUI page
generation requires a split APEX export because page SQL must be matched to an
existing application. The interface therefore uses two stages: first import
the table SQL in **SQL Workshop > SQL Scripts**, run it, and accept APEX's
prompt to create the template application and pages. Then export that app using
**Custom Export** and **Split into multiple files**, upload the resulting ZIP in
the artifacts step, generate the GUI page SQL, and run that SQL to create the
final application. For screenshot sources, the same flow is used after
`mockup_to_buml` creates the GUI pivot model.

\* GUI-model download uses BESSER's GUI code-builder when it can serialize the
model; otherwise a readable text dump is provided. Target generation is
currently wired for the **domain** model; GUI-only migrations can still download
the GUI pivot model. Screenshot GUI extraction uses BESSER's `mockup_to_buml`
pipeline and the upstream GUI-model fixer.

## Running

### Prerequisites
- Python 3.11 (3.9+)
- Node.js 18+

### 1. Backend (from the repository root)

```bash
python -m venv .venv
.\.venv\Scripts\activate           # Windows
# source .venv/bin/activate        # macOS/Linux

pip install -r requirements.txt
pip install besser
pip install -r webapp/backend/requirements.txt

# IMPORTANT: run from the repo root so the `migrator` package is importable
uvicorn webapp.backend.app.main:app --reload --port 8000
```

Check it: <http://localhost:8000/api/platforms> and interactive docs at
<http://localhost:8000/docs>.

### 2. Frontend

```bash
cd webapp/frontend
npm install
npm run dev            # http://localhost:5173
```

The dev server proxies `/api` to `http://localhost:8000`, so start the backend
first.

## Try it with the bundled example

Use `examples/mendix_to_powerapps/library.json` as the Mendix upload, pick the
`MyFirstModule` module, scope **Both**, generate the pivot, then target
**Oracle APEX** or **Power Apps (Excel)**.

## API summary

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/platforms` | Source/target registry + capabilities + tutorials |
| POST | `/api/mendix/modules` | List modules in an uploaded Mendix JSON |
| POST | `/api/pivot` | Build + serialize the pivot model (multipart) |
| GET | `/api/sessions/{id}/download/pivot?artifact=domain\|gui\|all` | Download pivot |
| POST | `/api/sessions/{id}/generate` | Run the target generator |
| GET | `/api/sessions/{id}/download/artifacts?name=<file>\|all` | Download artifacts |

## Notes

- Sessions are kept **in memory** (single process) with a temp working
  directory per migration — fine for a standalone tool; swap for a persistent
  store when embedding into the BESSER editor.
- The backend forces UTF-8 on stdout/stderr because the migrator parsers print
  progress with emoji, which crashes on Windows' default console encoding.

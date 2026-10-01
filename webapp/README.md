# Migration Hub web interface

The interface guides users through source selection, upload, B-UML inspection, target selection and artifact download. The FastAPI backend calls the shared [`migrator`](../migrator/README.md) library; the frontend uses React and Vite.

Dedicated parsers support Mendix, Oracle APEX and ReTool. Screenshot-based sources use the BESSER mockup pipeline and require an OpenAI key. Targets include Oracle APEX, ReTool, ServiceNow, spreadsheets and SQL databases. ServiceNow supports data models only.

## Run

Use Python 3.11+ and Node.js 18+. From the repository root:

```bash
python -m venv .venv
# Activate .venv, then:
python -m pip install -e . -r webapp/backend/requirements.txt
uvicorn webapp.backend.app.main:app --reload --port 8000
```

In another terminal:

```bash
cd webapp/frontend
npm install
npm run dev
```

Open <http://localhost:5173>. The frontend proxies `/api` to port 8000. Backend health is available at <http://localhost:8000/api/health>; API documentation is at <http://localhost:8000/docs>.

## Examples and imports

The [replication package](../evaluation_replication/README.md) contains native exports. Mendix JSON includes data and GUI definitions; select the module listed in its example metadata. APEX uses table DDL and page SQL. ReTool uses CSV tables and a Toolscript ZIP.

Follow the target import instructions shown after generation. APEX produces application SQL; ReTool produces CSV/schema files and a Toolscript ZIP; ServiceNow produces SDK TypeScript. APEX also supports adding GUI pages to an existing split export.

## API

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/platforms` | Platform capabilities and import instructions |
| POST | `/api/mendix/modules` | List modules in uploaded Mendix JSON |
| POST | `/api/pivot` | Extract and serialize B-UML |
| GET | `/api/sessions/{id}/download/pivot` | Download pivot artifacts |
| POST | `/api/sessions/{id}/generate` | Generate target artifacts |
| GET | `/api/sessions/{id}/download/artifacts` | Download generated artifacts |

Sessions use in-memory state and temporary working directories. The current implementation is intended for standalone use.

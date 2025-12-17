# arxiv-daily-scroll

Fetch the latest arXiv papers for selected categories, generate concise Chinese highlights with OpenAI (or other LLM APIs), and publish a static site to GitHub Pages automatically.

## What this repo does
- 📥 Pull recent arXiv papers for the tags in `tags.json` (default: `cs.CV`, `cs.RO`, `cs.AI`, `cs.LG`).
- 🤖 Call OpenAI API to produce Chinese summaries including:
  - One-line headline
  - Chinese abstract translation
  - Method explanation
  - Application scenarios
  - Experiment highlights
  - Keywords
- 🔗 Auto-extract code links (GitHub, Hugging Face, project pages).
- 💾 Save raw metadata + AI summaries under `data/YYYY-MM-DD/`.
- 🌐 Build a GitHub Pages-ready site under `docs/` organized by category and date.

## Project layout
- `main.py`: Fetch today’s arXiv window and generate AI summaries.
- `build_page.py`: Turn data into a multi-day Jekyll site (outputs to `docs/`).
- `utils/`: ArXiv querying, DeepSeek prompt logic, and helpers.
- `data/`: Dated outputs (`arxiv.json`, `ai_summary.json` per day).
- `docs/`: Generated site; set as GitHub Pages source.
- `.github/workflows/daily.yml`: CI that runs daily and pushes updates.

## Local quickstart

### 1. Install dependencies (Python 3.10+)
```bash
pip install -r requirements.txt
# or manually:
pip install -U arxiv openai tqdm requests beautifulsoup4
```

### 2. Set your DeepSeek API key
```bash
export LLM_API_KEY=your-deepseek-api-key
export LLM_BASE_URL=https://api.deepseek.com
export LLM_MODEL=deepseek-chat
```

<details>
<summary>💡 Using other LLM providers (OpenAI, Zhipu, etc.)</summary>

```bash
# OpenAI
export LLM_API_KEY=sk-your-openai-key
export LLM_BASE_URL=https://api.openai.com/v1
export LLM_MODEL=gpt-4o-mini

# Zhipu (智谱)
export LLM_API_KEY=your_zhipu_key
export LLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4
export LLM_MODEL=glm-4-flash
```
</details>

### 3. (Optional) Adjust categories
Edit `tags.json` to customize which arXiv categories to track.

### 4. Fetch & summarize today's papers
```bash
python main.py

# With options:
python main.py --thumbnails          # Fetch paper preview images
python main.py --concurrency 16      # Higher parallelism for AI analysis
python main.py --max-results 500     # Limit number of papers
```

### 5. Build the site
```bash
python build_page.py
```

Open `docs/index.html` locally, or push and enable GitHub Pages (see below).

## GitHub Actions setup (auto daily build + Pages deploy)

The workflow `.github/workflows/daily.yml` is already included. To wire it up:

### 1. Add DeepSeek API Key

Go to **Settings → Secrets and variables → Actions → New repository secret**:

| Secret Name | Value | Required |
|-------------|-------|----------|
| `DEEPSEEK_API_KEY` | Your DeepSeek API key (sk-xxx...) | ✅ Yes |

> 💡 默认使用 `deepseek-chat` 模型。DeepSeek API 价格便宜、速度快、中文效果好。

### 2. Enable GitHub Actions

If Actions are disabled, go to **Settings → Actions → General** and enable them.

### 3. Configure GitHub Pages

Go to **Settings → Pages**:
- **Source**: Deploy from a branch
- **Branch**: `main` (or your default branch)
- **Folder**: `/docs`

Click **Save**.

### 4. (Optional) Customize Schedule

Edit the cron in `daily.yml`:
```yaml
schedule:
  - cron: "30 4 * * *"  # UTC 4:30 = 北京时间 12:30
```

### 5. Run the Workflow

Two ways to trigger:
- **Manual**: Actions → "Daily arXiv cs.CV fetch & build" → Run workflow
- **Automatic**: Wait for the daily schedule

### What the workflow does:
1. ✅ Check out the repo, install Python deps
2. ✅ Run `main.py` to fetch today's arXiv papers and call DeepSeek API for Chinese summaries
3. ✅ Run `build_page.py` to regenerate the `docs/` site
4. ✅ Commit and push changes automatically

Pages will serve from `docs/` and update after each push.

## Configuration tips
- Categories: edit `tags.json`.
- Prompts: `utils/prompts/system.txt` and `utils/prompts/user.txt`.
- Concurrency/temperature: `update_ai_summary_async` in `utils/analyser.py`.
- Site title/output dirs: CLI flags in `build_page.py`.

## Data outputs

### Raw data (`data/YYYY-MM-DD/arxiv.json`)
- Title, authors, arXiv ID, abstract
- Categories, published/updated dates
- Auto-extracted code links (GitHub, Hugging Face, etc.)

### AI summaries (`data/YYYY-MM-DD/ai_summary.json`)
- `headline_zh`: One-line Chinese headline
- `summary_zh`: Chinese abstract translation
- `intro_zh`: 3 key bullet points
- `method_zh`: Method/architecture explanation
- `application_zh`: Application scenarios
- `highlight_zh`: Experiment highlights
- `tags_zh`: Chinese keywords

### Generated site (`docs/`)
Static Jekyll-compatible site organized by:
```
docs/
├── index.md              # Homepage with category cards
├── cs-CV/                # Category folder
│   ├── index.md          # Date list for this category
│   └── 2025-12-15/       # Date folder
│       ├── index.md      # Paper list table
│       └── papers/       # Individual paper pages
└── assets/style.css
```

## License
GPL-3.0. See `LICENSE`.

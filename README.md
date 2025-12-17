# 📚 arXiv Daily 中文要点汇总

<p align="center">
  <em>每日自动抓取 arXiv 论文，AI 生成中文深度解读，部署到 GitHub Pages</em>
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> •
  <a href="#-核心功能">核心功能</a> •
  <a href="#-配置指南">配置指南</a> •
  <a href="#-github-actions-自动化">自动化部署</a> •
  <a href="#-项目结构">项目结构</a>
</p>

---

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 📥 **智能抓取** | 基于 arXiv API 每日抓取指定分类的最新论文 |
| 🎯 **多支柱筛选** | 九大支柱兴趣系统，精准过滤你关注的研究方向 |
| 🤖 **多 API 支持** | Gemini / OpenAI / DeepSeek，自动故障转移 |
| 📝 **深度解读** | AI 生成一句话要点、核心内容、方法详解、应用场景等 |
| 🖼️ **图片提取** | 自动从 ar5iv 提取论文关键图片 |
| 🔗 **代码链接** | 自动识别 GitHub / HuggingFace / 项目主页链接 |
| 🌐 **静态网站** | 生成精美的 GitHub Pages 站点，支持日历导航 |
| 📊 **分组展示** | 论文按兴趣领域分组，快速定位感兴趣的内容 |
| ⭐ **收藏功能** | 支持收藏喜欢的论文，本地持久化存储 |

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/your-username/arxiv-daily.git
cd arxiv-daily
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

**依赖说明：**

| 包名 | 用途 |
|------|------|
| `arxiv>=2.1.0` | arXiv API 官方客户端 |
| `openai>=1.0.0` | 兼容多 LLM 提供商的 API 客户端 |
| `beautifulsoup4>=4.12.0` | HTML 解析（提取图片/缩略图） |
| `requests>=2.28.0` | HTTP 请求 |
| `aiohttp>=3.8.0` | 异步 HTTP（并发 AI 调用） |
| `tqdm>=4.65.0` | 进度条显示 |

### 3. 配置 API Key

程序支持多个 LLM API，会按优先级自动选择（Gemini → OpenAI → DeepSeek）：

```bash
# 主 API：Gemini（速度快，免费额度高，推荐）
export GEMINI_API_KEY="你的密钥"
export GEMINI_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai/"  # 默认值
export GEMINI_MODEL="gemini-2.0-flash"  # 默认值

# 备用 API：OpenAI
export OPENAI_API_KEY="你的密钥"
export OPENAI_BASE_URL="https://api.openai.com/v1"  # 默认值
export OPENAI_MODEL="gpt-4o-mini"  # 默认值

# 备用 API：DeepSeek（中文效果好）
export DEEPSEEK_API_KEY="你的密钥"
export DEEPSEEK_BASE_URL="https://api.deepseek.com"  # 默认值
export DEEPSEEK_MODEL="deepseek-chat"  # 默认值
```

> 💡 **Tips:** 只需设置你有的 API Key，程序会自动选择可用的 API。主 API 失败时自动切换到备用 API，确保高可用性。

### 4. 抓取并分析论文

```bash
python main.py
```

### 5. 生成网站

```bash
python build_page.py
```

### 6. 查看结果

打开 `docs/index.html` 查看生成的网站，或部署到 GitHub Pages。

---

## ⚙️ 命令行参数

### main.py - 论文抓取与 AI 分析

```bash
python main.py [OPTIONS]
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--max-results` | 1000 | 最大抓取论文数 |
| `--thumbnails` | False | 抓取论文预览缩略图（较慢） |
| `--concurrency` | 8 | AI 分析并发数 |
| `--temperature` | 0.2 | AI 生成温度（越低越稳定） |
| `--tags-file` | tags.json | arXiv 分类配置文件 |
| `--interests-file` | interests.json | 兴趣配置文件 |
| `--no-filter` | False | 不使用兴趣筛选，抓取所有论文 |
| `--skip-ai` | False | 跳过 AI 分析，仅抓取论文 |
| `--no-images` | False | 不提取论文图片 |
| `--max-images` | 3 | 每篇论文最多提取图片数 |

**使用示例：**

```bash
# 基础抓取（使用兴趣筛选）
python main.py

# 抓取所有论文，不筛选
python main.py --no-filter

# 高性能模式：提高并发数
python main.py --concurrency 16

# 完整模式：抓取缩略图 + 图片
python main.py --thumbnails --max-images 5

# 仅抓取，跳过 AI 分析
python main.py --skip-ai
```

### build_page.py - 生成静态网站

```bash
python build_page.py [OPTIONS]
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--data` | data | 数据根目录 |
| `--outdir` | docs | 输出站点目录 |
| `--tags` | tags.json | 分类配置文件 |
| `--title` | arXiv 中文要点汇总 | 站点标题 |

---

## 🎯 兴趣筛选系统

### 九大支柱架构

项目采用**多支柱筛选系统**，将论文按研究方向分为九大支柱：

| 支柱 | 领域 | 关键词示例 |
|------|------|-----------|
| 🤖 支柱一 | 机器人控制 | quadruped, humanoid, locomotion, manipulation, sim-to-real |
| 🧠 支柱二 | RL算法与架构 | PPO, SAC, offline RL, diffusion policy, world model |
| 👁️ 支柱三 | 空间感知与语义 | depth estimation, SLAM, 3DGS, NeRF, semantic mapping |
| 🎭 支柱四 | 生成式动作 | motion diffusion, text-to-motion, MDM, motion synthesis |
| 🤝 支柱五 | 交互与反应 | human-object interaction, reaction synthesis, HOI |
| 📹 支柱六 | 视频提取与匹配 | HMR, SMPL, egocentric, motion matching |
| 🔄 支柱七 | 动作重定向 | motion retargeting, human-to-robot, cross-embodiment |
| 🎮 支柱八 | 物理动画 | DeepMimic, AMP, character control, physics-based |
| 🌐 支柱九 | 具身大模型 | VLA, embodied AI, foundation model, instruction following |

### 筛选逻辑

- **OR 逻辑**：命中任意一个支柱即可通过
- **加权得分**：标题匹配权重更高（3x），摘要匹配基础权重
- **负面关键词**：医学/金融/NLP 等不相关领域自动排除
- **分数阈值**：可配置最低相关性分数

### 自定义配置

编辑 `interests.json` 自定义兴趣领域：

```json
{
    "meta": {
        "profile": "你的研究方向描述",
        "version": "1.0"
    },
    "filter_settings": {
        "min_relevance_score": 2.0,
        "title_multiplier": 3.0,
        "abstract_multiplier": 1.0
    },
    "concept_groups": [
        {
            "id": "1_your_topic",
            "name": "你的兴趣领域",
            "description": "领域描述",
            "weight": 2.0,
            "keywords": ["keyword1", "keyword2", "keyword3"]
        }
    ],
    "negative_keywords": ["unwanted_topic1", "unwanted_topic2"]
}
```

---

## 📂 arXiv 分类配置

编辑 `tags.json` 配置要抓取的 arXiv 分类：

```json
{
    "tags": [
        "cs.RO",    // 机器人
        "cs.CV",    // 计算机视觉
        "cs.GR",    // 图形学
        "cs.LG",    // 机器学习
        "cs.AI",    // 人工智能
        "cs.CL",    // 自然语言处理
        "eess.SY"   // 系统控制
    ]
}
```

**常用 arXiv 分类：**

| 分类 | 全称 | 说明 |
|------|------|------|
| cs.RO | Robotics | 机器人学 |
| cs.CV | Computer Vision | 计算机视觉 |
| cs.LG | Machine Learning | 机器学习 |
| cs.AI | Artificial Intelligence | 人工智能 |
| cs.CL | Computation and Language | 自然语言处理 |
| cs.GR | Graphics | 计算机图形学 |
| cs.NE | Neural and Evolutionary Computing | 神经与进化计算 |
| cs.HC | Human-Computer Interaction | 人机交互 |
| stat.ML | Machine Learning (Stats) | 统计机器学习 |
| eess.SY | Systems and Control | 系统与控制 |

---

## 🤖 AI 分析详解

### 生成内容

每篇论文会生成以下中文解读：

| 字段 | 说明 | 字数 |
|------|------|------|
| `headline_zh` | 一句话标题，直陈贡献与场景 | ≤50 字 |
| `summary_zh` | 中文摘要翻译，保持专业术语准确 | 150-250 字 |
| `intro_zh` | 3 条核心要点：问题、方法、效果 | 每条 30-50 字 |
| `method_zh` | 方法详解，结构化描述技术细节 | 300-500 字 |
| `application_zh` | 应用场景，潜在价值和未来影响 | 80-150 字 |
| `highlight_zh` | 实验亮点，具体性能数据 | 80-150 字 |
| `tags_zh` | 5-8 个中文关键词 | - |

### 方法详解结构

`method_zh` 字段采用结构化格式：

```
**问题定义**：论文要解决什么具体问题？现有方法的痛点是什么？

**核心思路**：论文的核心解决思路是什么？为什么这样设计？

**技术框架**：整体架构或流程是怎样的？包含哪些主要模块/阶段？

**关键创新**：最重要的技术创新点是什么？与现有方法的本质区别？

**关键设计**：有哪些关键的参数设置、损失函数、网络结构等技术细节？
```

### API 故障转移机制

程序会自动：

1. **按优先级选择可用 API**：Gemini → OpenAI → DeepSeek
2. **自动重试**：单个 API 失败时最多重试 2 次
3. **故障转移**：主 API 失败后自动切换到备用 API
4. **独立处理**：每篇论文独立处理，最大化成功率
5. **统计报告**：运行结束显示各 API 使用统计

```
[INFO] 主 API: Gemini (gemini-2.0-flash)
[INFO] 备用 API: OpenAI, DeepSeek
LLM (Gemini): 100%|████████████████████| 180/180 [03:22<00:00]

[统计] 成功: 178, 失败: 2
[统计] API 使用分布: gemini: 175, openai: 3
```

---

## 🖼️ 图片提取

### 功能说明

程序会自动从 [ar5iv](https://ar5iv.labs.arxiv.org/)（arXiv 的 HTML 版本）提取论文中的关键图片：

- 自动提取 Figure 1, Figure 2 等主要图片
- 保留图片标题（caption）
- 过滤图标、logo 等无关图片
- 优先选择有 caption 的图片

### 配置选项

```bash
# 默认提取 3 张图片
python main.py

# 提取更多图片
python main.py --max-images 5

# 禁用图片提取
python main.py --no-images
```

---

## ☁️ GitHub Actions 自动化

### 配置 Secrets

进入仓库 **Settings → Secrets and variables → Actions → New repository secret**：

| Secret 名称 | 说明 | 必需 |
|------------|------|------|
| `GEMINI_API_KEY` | Gemini API 密钥 | 推荐 |
| `GEMINI_BASE_URL` | Gemini API 地址 | 可选 |
| `GEMINI_MODEL` | Gemini 模型名 | 可选 |
| `OPENAI_API_KEY` | OpenAI API 密钥 | 推荐 |
| `OPENAI_BASE_URL` | OpenAI API 地址 | 可选 |
| `OPENAI_MODEL` | OpenAI 模型名 | 可选 |
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | 可选 |
| `DEEPSEEK_BASE_URL` | DeepSeek API 地址 | 可选 |
| `DEEPSEEK_MODEL` | DeepSeek 模型名 | 可选 |

> 💡 **建议**：至少配置两个 API Key（如 Gemini + OpenAI），确保故障转移可用。

### 创建 Workflow 文件

创建 `.github/workflows/daily.yml`：

```yaml
name: Daily arXiv Fetch & Build

on:
  schedule:
    # 每天 UTC 19:00（北京时间凌晨 3:00）
    - cron: "0 19 * * *"
  workflow_dispatch:  # 支持手动触发

jobs:
  fetch-and-build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Fetch papers
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          GEMINI_BASE_URL: ${{ secrets.GEMINI_BASE_URL }}
          GEMINI_MODEL: ${{ secrets.GEMINI_MODEL }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
          OPENAI_MODEL: ${{ secrets.OPENAI_MODEL }}
          DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
          DEEPSEEK_BASE_URL: ${{ secrets.DEEPSEEK_BASE_URL }}
          DEEPSEEK_MODEL: ${{ secrets.DEEPSEEK_MODEL }}
        run: python main.py --concurrency 8
      
      - name: Build pages
        run: python build_page.py
      
      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add data/ docs/
          git commit -m "📚 Daily update: $(date +'%Y-%m-%d')" || exit 0
          git push
```

### 配置 GitHub Pages

1. 进入 **Settings → Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `main`，**Folder**: `/docs`
4. 点击 **Save**

### 触发方式

- **自动触发**：每天 UTC 19:00（北京时间凌晨 3:00）
- **手动触发**：Actions → Daily arXiv Fetch & Build → Run workflow

---

## 📊 可选模型列表

<details>
<summary>点击展开完整模型列表</summary>

### Gemini 模型

| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `gemini-2.0-flash` | 最新快速模型 ⭐ | **默认推荐**，速度快、免费额度高 |
| `gemini-2.0-flash-lite` | 超轻量版 | 成本敏感场景 |
| `gemini-1.5-pro` | 高性能版 | 复杂任务 |
| `gemini-1.5-flash` | 平衡版 | 通用场景 |
| `gemini-1.5-flash-8b` | 轻量版 | 简单任务 |

### OpenAI 模型

| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `gpt-4o-mini` | 性价比最高 ⭐ | **默认推荐** |
| `gpt-4o` | 最强性能 | 复杂分析 |
| `gpt-4-turbo` | 高性能 | 长文本 |
| `gpt-3.5-turbo` | 经济实惠 | 简单任务 |
| `o1-mini` | 推理增强 | 深度分析 |

### DeepSeek 模型

| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `deepseek-chat` | 通用对话 ⭐ | **默认推荐**，中文效果好 |
| `deepseek-coder` | 代码专用 | 代码分析 |
| `deepseek-reasoner` | 推理增强 | 深度分析 |

### Claude 模型（需配置兼容代理）

| 模型名 | 说明 | 推荐场景 |
|--------|------|----------|
| `claude-sonnet-4-20250514` | 最新平衡版 | 通用场景 |
| `claude-3-5-sonnet-20241022` | 高性价比 | 日常使用 |
| `claude-3-opus-20240229` | 最强性能 | 复杂分析 |
| `claude-3-haiku-20240307` | 快速响应 | 简单任务 |

</details>

---

## 📁 项目结构

```
arxiv-daily/
├── main.py                 # 主程序：论文抓取 + AI 分析 + 图片提取
├── build_page.py           # 生成静态网站
├── tags.json               # arXiv 分类配置
├── interests.json          # 兴趣关键词配置（九大支柱）
├── requirements.txt        # Python 依赖
├── LICENSE                 # GPL-3.0 许可证
├── README.md               # 项目说明文档
│
├── utils/                  # 工具模块
│   ├── __init__.py
│   ├── analyser.py         # LLM API 调用（多 API + 故障转移）
│   ├── scrapy.py           # arXiv 抓取 + 兴趣筛选
│   ├── image_extractor.py  # ar5iv 图片提取
│   └── prompts/            # LLM 提示词模板
│       ├── system.txt      # 系统提示词
│       └── user.txt        # 用户提示词模板
│
├── data/                   # 数据目录（自动生成）
│   └── YYYY-MM-DD/
│       ├── arxiv.json      # 原始论文数据
│       └── ai_summary.json # AI 分析结果
│
├── docs/                   # 生成的静态网站
│   ├── index.md            # 首页
│   ├── _config.yml         # Jekyll 配置
│   ├── _layouts/
│   │   └── default.html    # 页面模板
│   ├── assets/
│   │   └── style.css       # 样式文件
│   └── cs-CV/              # 分类目录
│       ├── index.md        # 分类首页（日历视图）
│       └── YYYY-MM-DD/
│           ├── index.md    # 日期目录页
│           └── papers/     # 论文详情页
│
└── .github/
    └── workflows/
        └── daily.yml       # GitHub Actions 配置
```

---

## 📊 输出数据格式

### 原始论文数据 (`arxiv.json`)

```json
{
  "count": 150,
  "filtered": true,
  "papers": [
    {
      "title": "论文标题",
      "authors": ["作者1", "作者2"],
      "arxiv_id": "2512.14689v1",
      "summary": "英文摘要...",
      "categories": ["cs.RO", "cs.CV"],
      "primary_category": "cs.RO",
      "published": "2025-12-18",
      "updated": "2025-12-18",
      "comment": "Accepted to ICRA 2025",
      "doi": "",
      "journal_ref": "",
      "pdf_url": "https://arxiv.org/pdf/2512.14689.pdf",
      "code_links": [
        {"url": "https://github.com/user/repo", "type": "github"}
      ],
      "thumbnail": "https://...",
      "matched_interests": [
        {"name": "支柱一：机器人控制", "id": "1_robot_core", "score": 6.0}
      ],
      "relevance_score": 6.0,
      "hit_pillars": ["1_robot_core"]
    }
  ]
}
```

### AI 分析结果 (`ai_summary.json`)

```json
{
  "papers": [
    {
      "title": "论文标题",
      "arxiv_id": "2512.14689v1",
      "headline_zh": "一句话中文要点",
      "summary_zh": "中文摘要翻译...",
      "intro_zh": [
        "核心问题：现有方法的不足...",
        "方法要点：论文提出的解决方案...",
        "实验效果：主要结果和提升..."
      ],
      "method_zh": "**问题定义**：...\n\n**核心思路**：...",
      "application_zh": "应用场景描述...",
      "highlight_zh": "实验亮点，具体数据...",
      "tags_zh": ["关键词1", "关键词2", "关键词3"],
      "figures": [
        {"url": "https://...", "caption": "图片说明", "figure_id": "figure1"}
      ],
      "_used_api": "gemini",
      "_index": 0
    }
  ]
}
```

---

## 🔧 自定义配置

### 修改 LLM 提示词

编辑 `utils/prompts/` 下的文件：

- **system.txt**: 系统角色设定
- **user.txt**: 用户提示词模板，使用 `{title}`, `{authors}`, `{summary}` 占位符

### 修改网站样式

编辑 `docs/assets/style.css` 自定义网站外观。

### 修改页面模板

编辑 `docs/_layouts/default.html` 自定义页面结构。

---

## 🐛 故障排除

### 常见问题

**Q: API 调用失败怎么办？**

A: 检查以下几点：
1. 确认 API Key 正确设置
2. 确认 API 额度充足
3. 尝试降低并发数：`--concurrency 4`
4. 配置多个 API 作为备用

**Q: 抓取不到论文？**

A: 可能原因：
1. arXiv 在周末不更新论文
2. 检查 `tags.json` 分类配置
3. 检查网络连接

**Q: 兴趣筛选后论文太少？**

A: 调整 `interests.json`：
1. 降低 `min_relevance_score` 阈值
2. 添加更多关键词
3. 使用 `--no-filter` 暂时禁用筛选

**Q: 图片提取失败？**

A: ar5iv 不是所有论文都有 HTML 版本，这是正常现象。新论文可能需要几天才能有 HTML 版本。

---

## 📝 更新日志

### v5.2 (2025-12)
- ✨ 九大支柱筛选系统
- ✨ 多 API 支持 + 故障转移
- ✨ ar5iv 图片提取
- ✨ 日历视图导航
- ✨ 论文收藏功能
- 🎨 全新网站设计

---

## 📜 许可证

本项目采用 **GPL-3.0** 许可证。详见 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- [arXiv](https://arxiv.org/) - 论文数据来源
- [ar5iv](https://ar5iv.labs.arxiv.org/) - HTML 版本论文
- [Google Gemini](https://ai.google.dev/) / [OpenAI](https://openai.com/) / [DeepSeek](https://deepseek.com/) - LLM 服务
- [GitHub Pages](https://pages.github.com/) - 静态网站托管

---

<p align="center">
  Made with ❤️ for the research community
</p>

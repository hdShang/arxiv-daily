#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse, json, os, re, sys, datetime
from pathlib import Path
from typing import List, Dict, Any, Tuple
from collections import defaultdict

# =============== 基础工具 ===============

def slugify(text: str, maxlen: int = 80) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.U).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:maxlen] if maxlen else text

def read_json(p: Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def md_escape(s: str) -> str:
    return s.replace("|", r"\|")

def to_authors(auth_list) -> str:
    if isinstance(auth_list, list):
        return ", ".join(auth_list)
    return str(auth_list)

def load_tags(tags_file: Path) -> List[str]:
    """加载 tags.json 中的分类列表"""
    with tags_file.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("tags", [])

# =============== 渲染 ===============

def render_paper_md(p: Dict[str, Any]) -> str:
    """渲染论文详情页面（增强版）"""
    title = p.get("title", "").strip()
    authors = to_authors(p.get("authors", []))
    arxiv_id = p.get("arxiv_id", "")
    headline = p.get("headline_zh", "").strip()
    intro = p.get("intro_zh", [])
    tags = p.get("tags_zh", [])
    summary = p.get("summary", "").strip()
    categories = p.get("categories", [])
    
    # 新增字段
    summary_zh = p.get("summary_zh", "").strip()
    method_zh = p.get("method_zh", "").strip()
    application_zh = p.get("application_zh", "").strip()
    highlight_zh = p.get("highlight_zh", "").strip()
    thumbnail = p.get("thumbnail", "").strip()
    code_links = p.get("code_links", [])
    published = p.get("published", "").strip()
    updated = p.get("updated", "").strip()
    comment = p.get("comment", "").strip()
    doi = p.get("doi", "").strip()
    journal_ref = p.get("journal_ref", "").strip()

    lines = []
    lines.append(f"# {md_escape(title)}")
    
    # 基础信息区
    if arxiv_id:
        base_id = arxiv_id.split('v')[0]
        abs_url = f"https://arxiv.org/abs/{base_id}"
        pdf_url = f"https://arxiv.org/pdf/{base_id}.pdf"
        lines.append(f"\n**arXiv**: [{arxiv_id}]({abs_url}) | [PDF]({pdf_url})")
    
    lines.append(f"\n**作者**: {md_escape(authors)}")
    
    if categories:
        lines.append(f"\n**分类**: {', '.join(categories)}")
    
    if published:
        date_info = f"**发布日期**: {published}"
        if updated and updated != published:
            date_info += f" (更新: {updated})"
        lines.append(f"\n{date_info}")
    
    if comment:
        lines.append(f"\n**备注**: {md_escape(comment)}")
    
    if journal_ref:
        lines.append(f"\n**期刊**: {md_escape(journal_ref)}")
    
    if doi:
        lines.append(f"\n**DOI**: [{doi}](https://doi.org/{doi})")
    
    # 代码链接
    if code_links:
        links_str = " | ".join([f"[{l.get('type', 'code').upper()}]({l['url']})" for l in code_links])
        lines.append(f"\n**🔗 代码/项目**: {links_str}")
    
    lines.append("\n---\n")
    
    # 预览图片
    if thumbnail:
        lines.append(f"![论文预览图]({thumbnail})")
        lines.append("")
    
    # 一句话要点
    if headline:
        lines.append(f"## 💡 一句话要点\n")
        lines.append(f"**{md_escape(headline)}**\n")
    
    # 匹配的兴趣领域
    matched_interests = p.get("matched_interests", [])
    if matched_interests:
        interests_str = " ".join([f"**{m['name']}**" for m in matched_interests])
        lines.append(f"🎯 **匹配领域**: {interests_str}\n")
    
    # 关键词标签
    if tags:
        tags_html = " ".join([f"`{t}`" for t in tags])
        lines.append(f"**关键词**: {tags_html}\n")
    
    # 核心要点（3点简述）
    if intro and isinstance(intro, list):
        lines.append("## 📋 核心要点\n")
        for i, it in enumerate(intro, 1):
            lines.append(f"{i}. {md_escape(str(it))}")
        lines.append("")
    
    # 中文摘要
    if summary_zh:
        lines.append("## 📝 摘要（中文）\n")
        lines.append(f"{md_escape(summary_zh)}\n")
    
    # 方法详解
    if method_zh:
        lines.append("## 🔬 方法详解\n")
        # 处理换行符，将 \n\n 转换为实际换行
        method_formatted = method_zh.replace("\\n\\n", "\n\n").replace("\\n", "\n")
        lines.append(f"{method_formatted}\n")
    
    # 实验亮点
    if highlight_zh:
        lines.append("## 📊 实验亮点\n")
        lines.append(f"{md_escape(highlight_zh)}\n")
    
    # 应用场景
    if application_zh:
        lines.append("## 🎯 应用场景\n")
        lines.append(f"{md_escape(application_zh)}\n")
    
    # 原文摘要
    lines.append("## 📄 摘要（原文）\n")
    lines.append(f"> " + "\n> ".join(md_escape(summary).splitlines()))
    lines.append("")
    
    return "\n".join(lines)

def _render_paper_table_html(papers: List[Dict[str, Any]], start_idx: int = 0) -> str:
    """渲染论文表格（HTML格式，支持收藏按钮）"""
    rows = []
    for i, p in enumerate(papers, start_idx + 1):
        title = p.get("title", "").strip()
        arxiv_id = p.get("arxiv_id", "")
        slug = slugify(f"{arxiv_id}-{title}") or f"paper-{i}"
        headline = p.get("headline_zh", "").replace('"', '&quot;')
        code_links = p.get("code_links", [])
        code_icon = "✅" if code_links else ""
        # 转义标题中的特殊字符
        title_escaped = title.replace('"', '&quot;').replace("'", "&#39;")
        title_display = title.replace("<", "&lt;").replace(">", "&gt;")
        
        rows.append(f'''<tr>
  <td>{i}</td>
  <td><a href="./papers/{slug}.html">{title_display}</a></td>
  <td>{headline}</td>
  <td>{code_icon}</td>
  <td><button class="favorite-btn" data-arxiv-id="{arxiv_id}" onclick="toggleFavorite(this, '{arxiv_id}', '{title_escaped}')" title="添加到收藏夹">☆</button></td>
</tr>''')
    return "\n".join(rows)

def build_tag_date_index_md(tag: str, date_label: str, papers: List[Dict[str, Any]], site_title: str) -> str:
    """生成某分类某日期的目录页（按兴趣领域分组）"""
    lines = []
    lines.append(f"---\nlayout: default\ntitle: {site_title} - {tag} - {date_label}\n---\n")
    lines.append(f"# {tag}（{date_label}）\n")
    
    # 统计信息
    papers_with_code = sum(1 for p in papers if p.get("code_links"))
    lines.append(f"📊 共 **{len(papers)}** 篇论文")
    if papers_with_code:
        lines.append(f" | 🔗 **{papers_with_code}** 篇有代码")
    lines.append("\n")
    
    # 按兴趣领域分组
    interest_groups = defaultdict(list)
    no_interest_papers = []
    
    for p in papers:
        matched = p.get("matched_interests", [])
        if matched:
            # 使用第一个匹配的兴趣领域作为主分组
            primary_interest = matched[0].get("name", "其他")
            interest_groups[primary_interest].append(p)
        else:
            no_interest_papers.append(p)
    
    # 表格头部 HTML
    table_header = '''<table>
<thead>
<tr><th>#</th><th>题目</th><th>一句话要点</th><th>🔗</th><th>⭐</th></tr>
</thead>
<tbody>'''
    table_footer = '''</tbody>
</table>'''
    
    # 如果有兴趣领域分组，显示快速导航
    if interest_groups:
        lines.append("## 🎯 兴趣领域导航\n")
        lines.append('<div class="interest-nav">')
        for interest_name, group_papers in sorted(interest_groups.items(), key=lambda x: -len(x[1])):
            code_count = sum(1 for p in group_papers if p.get("code_links"))
            anchor = slugify(interest_name)
            code_badge = f" 🔗{code_count}" if code_count else ""
            lines.append(f'<a href="#{anchor}" class="interest-badge">{interest_name} ({len(group_papers)}{code_badge})</a>')
        if no_interest_papers:
            lines.append(f'<a href="#other" class="interest-badge">其他 ({len(no_interest_papers)})</a>')
        lines.append('</div>\n')
        lines.append("---\n")
        
        # 按兴趣领域分组显示论文
        global_idx = 0
        for interest_name, group_papers in sorted(interest_groups.items(), key=lambda x: -len(x[1])):
            anchor = slugify(interest_name)
            lines.append(f'\n<h2 id="{anchor}">🔬 {interest_name} ({len(group_papers)} 篇)</h2>\n')
            
            lines.append(table_header)
            lines.append(_render_paper_table_html(group_papers, global_idx))
            lines.append(table_footer)
            global_idx += len(group_papers)
            lines.append("")
        
        # 其他论文（未匹配兴趣领域）
        if no_interest_papers:
            lines.append('\n<h2 id="other">📄 其他</h2>\n')
            lines.append(table_header)
            lines.append(_render_paper_table_html(no_interest_papers, global_idx))
            lines.append(table_footer)
            lines.append("")
    else:
        # 没有兴趣领域信息，使用平铺方式
        lines.append(table_header)
        lines.append(_render_paper_table_html(papers, 0))
        lines.append(table_footer)
        lines.append("")
    
    lines.append(f"\n[⬅️ 返回 {tag} 首页](../index.html) · [🏠 返回主页](../../index.html)")
    return "\n".join(lines)

def build_tag_index_md(tag: str, dates: List[str], site_title: str) -> str:
    """生成某分类的首页（日历视图）"""
    from datetime import datetime
    import calendar
    
    lines = []
    lines.append(f"---\nlayout: default\ntitle: {site_title} - {tag}\n---\n")
    lines.append(f"# {tag}\n")
    lines.append("> 点击日历中高亮的日期查看论文\n")
    
    # 生成日期选择器
    latest_date = sorted(dates)[-1] if dates else ""
    options_html = "\n".join(
        [f'<option value="{d}/index.html" {"selected" if d == latest_date else ""}>{d}</option>'
         for d in sorted(dates, reverse=True)]
    )
    html_block = f"""
<div class="date-switcher">
  <label for="date-select"><strong>快速跳转：</strong></label>
  <select id="date-select" onchange="location.href=this.value;">
    {options_html}
  </select>
  <a class="btn" href="{latest_date}/index.html">前往最新（{latest_date}）</a>
</div>
"""
    lines.append(html_block)
    
    # 按月份分组生成日历
    date_set = set(dates)
    if dates:
        # 解析日期并按月份分组
        date_objs = [datetime.strptime(d, "%Y-%m-%d") for d in dates]
        months = sorted(set((d.year, d.month) for d in date_objs), reverse=True)
        
        lines.append('\n<div class="calendar-container">')
        
        for year, month in months:
            month_name = f"{year}年{month}月"
            lines.append(f'<div class="calendar-month">')
            lines.append(f'<h3 class="month-title">{month_name}</h3>')
            lines.append('<div class="calendar-grid">')
            lines.append('<div class="cal-header">日</div>')
            lines.append('<div class="cal-header">一</div>')
            lines.append('<div class="cal-header">二</div>')
            lines.append('<div class="cal-header">三</div>')
            lines.append('<div class="cal-header">四</div>')
            lines.append('<div class="cal-header">五</div>')
            lines.append('<div class="cal-header">六</div>')
            
            # 获取该月的日历
            cal = calendar.Calendar(firstweekday=6)  # 周日开始
            month_days = cal.monthdayscalendar(year, month)
            
            for week in month_days:
                for day in week:
                    if day == 0:
                        lines.append('<div class="cal-day empty"></div>')
                    else:
                        date_str = f"{year}-{month:02d}-{day:02d}"
                        if date_str in date_set:
                            lines.append(f'<a href="{date_str}/index.html" class="cal-day has-data">{day}</a>')
                        else:
                            lines.append(f'<div class="cal-day">{day}</div>')
            
            lines.append('</div>')  # calendar-grid
            lines.append('</div>')  # calendar-month
        
        lines.append('</div>')  # calendar-container
    
    lines.append("\n\n[🏠 返回主页](../index.html)")
    return "\n".join(lines)

def build_home_md(tags: List[str], tag_stats: Dict[str, Dict], site_title: str) -> str:
    """
    首页：包含分类导航，显示最近一周数据和统计信息
    
    tag_stats 结构:
    {
        "cs.RO": {
            "latest_date": "2025-12-17",
            "dates": ["2025-12-17", "2025-12-16", ...],
            "recent_papers": [...],  # 最近7天的论文
            "total_count": 100,
            "pillar_stats": {
                "机器人控制": 30,
                "空间感知": 25,
                ...
            }
        }
    }
    """
    lines = []
    lines.append(f"---\nlayout: default\ntitle: {site_title}\n---\n")
    lines.append(f"# {site_title}\n")
    
    # 只显示有数据的分类
    active_tags = [tag for tag in tags if tag in tag_stats and tag_stats[tag].get("dates")]
    
    if not active_tags:
        lines.append("> 暂无数据\n")
        return "\n".join(lines)
    
    # 为每个分类生成详细卡片
    for tag in active_tags:
        stats = tag_stats[tag]
        safe_tag = tag.replace(".", "-")
        latest_date = stats.get("latest_date", "")
        dates = stats.get("dates", [])
        total_count = stats.get("total_count", 0)
        pillar_stats = stats.get("pillar_stats", {})
        recent_papers = stats.get("recent_papers", [])
        recent_dates = stats.get("recent_dates", [])
        
        lines.append(f'<div class="tag-section" id="{safe_tag}">')
        lines.append(f'<div class="tag-header">')
        lines.append(f'<h2>{tag}</h2>')
        lines.append(f'<div class="tag-meta">')
        lines.append(f'<span class="date-range">📅 最新: {latest_date}</span>')
        lines.append(f'<span class="paper-count">📄 共 {total_count} 篇</span>')
        lines.append(f'</div>')
        lines.append(f'</div>')
        
        # 支柱统计
        if pillar_stats:
            lines.append('<div class="pillar-stats">')
            lines.append('<h4>📊 领域分布</h4>')
            lines.append('<div class="pillar-badges">')
            for pillar_name, count in sorted(pillar_stats.items(), key=lambda x: -x[1]):
                # 简化支柱名称
                short_name = pillar_name.split("：")[-1].split(" ")[0] if "：" in pillar_name else pillar_name
                lines.append(f'<span class="pillar-badge">{short_name} <strong>{count}</strong></span>')
            lines.append('</div>')
            lines.append('</div>')
        
        # 最近日期快速访问
        date_paper_counts = stats.get("date_paper_counts", {})
        if recent_dates:
            lines.append('<div class="recent-dates">')
            lines.append('<h4>📆 最近更新</h4>')
            lines.append('<div class="date-buttons">')
            for d in recent_dates[:7]:
                paper_count = date_paper_counts.get(d, 0)
                lines.append(f'<a href="{safe_tag}/{d}/index.html" class="date-btn">{d} <small>({paper_count}篇)</small></a>')
            lines.append('</div>')
            lines.append('</div>')
        
        # 最近论文预览（最多显示5篇）
        if recent_papers:
            lines.append('<div class="recent-papers">')
            lines.append('<h4>📝 最新论文</h4>')
            lines.append('<ul class="paper-list">')
            for p in recent_papers[:5]:
                title = p.get("title", "")[:60]
                if len(p.get("title", "")) > 60:
                    title += "..."
                headline = p.get("headline_zh", "")[:40]
                if len(p.get("headline_zh", "")) > 40:
                    headline += "..."
                paper_date = p.get("_date", latest_date)
                arxiv_id = p.get("arxiv_id", "")
                slug = slugify(f"{arxiv_id}-{p.get('title', '')}") or "paper"
                has_code = "🔗" if p.get("code_links") else ""
                lines.append(f'<li><a href="{safe_tag}/{paper_date}/papers/{slug}.html">{title}</a> {has_code}<br><small>{headline}</small></li>')
            lines.append('</ul>')
            lines.append('</div>')
        
        # 操作按钮
        lines.append('<div class="tag-actions">')
        lines.append(f'<a class="btn btn-primary" href="{safe_tag}/{latest_date}/index.html">查看最新</a>')
        lines.append(f'<a class="btn btn-secondary" href="{safe_tag}/index.html">更多日期 ({len(dates)})</a>')
        lines.append('</div>')
        
        lines.append('</div>')  # tag-section
        lines.append('')
    
    return "\n".join(lines)

def write_site_scaffold(docs_dir: Path):
    ensure_dir(docs_dir)
    ensure_dir(docs_dir / "assets")
    (docs_dir / "_config.yml").write_text(
        "theme: jekyll-theme-cayman\nmarkdown: kramdown\nkramdown:\n  input: GFM\n",
        encoding="utf-8"
    )
    (docs_dir / "_layouts").mkdir(exist_ok=True)
    (docs_dir / "_layouts" / "default.html").write_text(
        """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>{{ page.title }}</title>
<link rel="stylesheet" href="{{ '/assets/style.css' | relative_url }}">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<main class="container">
  {{ content }}
</main>
<footer class="footer">
  <p>Powered by GitHub Pages · Generated on {{ site.time | date: "%Y-%m-%d" }}</p>
</footer>
</body>
</html>
""",
        encoding="utf-8"
    )
    (docs_dir / "assets" / "style.css").write_text(
        """/* 基础样式 */
:root {
  --primary: #2563eb;
  --primary-dark: #1d4ed8;
  --bg: #ffffff;
  --bg-secondary: #f8fafc;
  --text: #1e293b;
  --text-secondary: #64748b;
  --border: #e2e8f0;
  --success: #22c55e;
  --code-bg: #f1f5f9;
}

.container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 1.5rem;
  font: 16px/1.7 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: var(--text);
}

h1 { font-size: 1.75rem; font-weight: 700; margin-bottom: 1rem; line-height: 1.3; }
h2 { font-size: 1.25rem; font-weight: 600; margin: 1.5rem 0 0.75rem; color: var(--text); border-bottom: 2px solid var(--primary); padding-bottom: 0.5rem; }
h3 { font-size: 1.1rem; font-weight: 600; margin: 1rem 0 0.5rem; }

a { color: var(--primary); text-decoration: none; }
a:hover { text-decoration: underline; }

/* 表格样式 */
table { border-collapse: collapse; width: 100%; margin: 1.5rem 0; font-size: 0.9rem; }
th, td { border: 1px solid var(--border); padding: 0.75rem; vertical-align: top; text-align: left; }
th { background: var(--bg-secondary); font-weight: 600; }
tr:hover { background: var(--bg-secondary); }
td:first-child { text-align: center; font-weight: 600; color: var(--text-secondary); width: 40px; }
td:last-child { text-align: center; width: 40px; }

/* 代码样式 */
code, pre { background: var(--code-bg); padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.85em; }
pre { padding: 1rem; overflow-x: auto; }

/* 引用块 - 用于原文摘要 */
blockquote {
  margin: 1rem 0;
  padding: 1rem 1.5rem;
  background: var(--bg-secondary);
  border-left: 4px solid var(--primary);
  border-radius: 0 8px 8px 0;
  color: var(--text-secondary);
  font-size: 0.9rem;
  line-height: 1.6;
}

/* 页脚 */
.footer { margin: 3rem 0 1rem; padding-top: 1rem; border-top: 1px solid var(--border); color: var(--text-secondary); font-size: 0.85rem; text-align: center; }

/* 日期选择器 */
.date-switcher {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  margin: 1.5rem 0;
  flex-wrap: wrap;
  padding: 1rem;
  background: var(--bg-secondary);
  border-radius: 8px;
}
.date-switcher select {
  padding: 0.5rem 1rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  font-size: 0.95rem;
  background: white;
}
.date-switcher .btn {
  padding: 0.5rem 1rem;
  background: var(--primary);
  color: white;
  border-radius: 6px;
  font-weight: 500;
}
.date-switcher .btn:hover { background: var(--primary-dark); text-decoration: none; }

/* 分类卡片网格 */
.tag-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.25rem;
  margin: 2rem 0;
}
.tag-card {
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 1.25rem;
  background: var(--bg);
  transition: box-shadow 0.2s, transform 0.2s;
}
.tag-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); transform: translateY(-2px); }
.tag-card h3 { margin: 0 0 0.5rem; font-size: 1.2rem; }
.tag-card h3 a { color: var(--text); }
.tag-card p { margin: 0.5rem 0; color: var(--text-secondary); font-size: 0.9rem; }
.tag-card .btn {
  display: inline-block;
  margin-top: 0.75rem;
  padding: 0.5rem 1rem;
  background: var(--primary);
  color: white;
  border-radius: 6px;
  font-weight: 500;
}
.tag-card .btn:hover { background: var(--primary-dark); text-decoration: none; }

/* 论文详情页样式 */
img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin: 1rem 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* 关键词标签 */
code {
  background: #e0f2fe;
  color: #0369a1;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-right: 0.25rem;
}

/* 信息块 */
.info-block {
  background: var(--bg-secondary);
  padding: 1rem;
  border-radius: 8px;
  margin: 1rem 0;
}

/* 兴趣领域导航 */
.interest-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0;
}
.interest-badge {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white !important;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  text-decoration: none !important;
  transition: transform 0.2s, box-shadow 0.2s;
}
.interest-badge:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
  text-decoration: none !important;
}

/* ===== 新版首页样式 ===== */

/* 分类区块 */
.tag-section {
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  background: var(--bg);
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.tag-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid var(--primary);
}

.tag-header h2 {
  margin: 0;
  padding: 0;
  border: none;
  font-size: 1.5rem;
  color: var(--primary);
}

.tag-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.tag-meta span {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

/* 支柱统计 */
.pillar-stats {
  margin: 1rem 0;
  padding: 1rem;
  background: var(--bg-secondary);
  border-radius: 12px;
}

.pillar-stats h4 {
  margin: 0 0 0.75rem;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.pillar-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.pillar-badge {
  display: inline-block;
  padding: 0.35rem 0.75rem;
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  color: #0369a1;
  border-radius: 20px;
  font-size: 0.8rem;
  border: 1px solid #bae6fd;
}

.pillar-badge strong {
  margin-left: 0.35rem;
  padding: 0.1rem 0.4rem;
  background: #0369a1;
  color: white;
  border-radius: 10px;
  font-size: 0.75rem;
}

/* 最近日期按钮 */
.recent-dates {
  margin: 1rem 0;
}

.recent-dates h4 {
  margin: 0 0 0.75rem;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.date-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.date-btn {
  display: inline-block;
  padding: 0.5rem 0.75rem;
  background: var(--bg-secondary);
  color: var(--text) !important;
  border-radius: 8px;
  font-size: 0.85rem;
  border: 1px solid var(--border);
  transition: all 0.2s;
  text-decoration: none !important;
}

.date-btn:hover {
  background: var(--primary);
  color: white !important;
  border-color: var(--primary);
}

.date-btn small {
  color: var(--text-secondary);
  margin-left: 0.25rem;
}

.date-btn:hover small {
  color: rgba(255,255,255,0.8);
}

/* 最近论文列表 */
.recent-papers {
  margin: 1rem 0;
}

.recent-papers h4 {
  margin: 0 0 0.75rem;
  font-size: 0.9rem;
  color: var(--text-secondary);
}

.paper-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.paper-list li {
  padding: 0.75rem;
  border-bottom: 1px solid var(--border);
  transition: background 0.2s;
}

.paper-list li:last-child {
  border-bottom: none;
}

.paper-list li:hover {
  background: var(--bg-secondary);
}

.paper-list a {
  font-weight: 500;
  color: var(--text);
}

.paper-list small {
  display: block;
  color: var(--text-secondary);
  font-size: 0.8rem;
  margin-top: 0.25rem;
}

/* 操作按钮 */
.tag-actions {
  display: flex;
  gap: 0.75rem;
  margin-top: 1.25rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
}

.btn {
  display: inline-block;
  padding: 0.6rem 1.25rem;
  border-radius: 8px;
  font-weight: 500;
  text-decoration: none !important;
  transition: all 0.2s;
}

.btn-primary {
  background: var(--primary);
  color: white !important;
}

.btn-primary:hover {
  background: var(--primary-dark);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.btn-secondary {
  background: var(--bg-secondary);
  color: var(--text) !important;
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  background: var(--border);
  color: var(--text) !important;
}

/* 响应式 */
@media (max-width: 768px) {
  .container { padding: 0 1rem; }
  h1 { font-size: 1.4rem; }
  table { font-size: 0.8rem; }
  th, td { padding: 0.5rem; }
  .tag-grid { grid-template-columns: 1fr; }
  .tag-header { flex-direction: column; align-items: flex-start; }
  .tag-meta { flex-direction: column; gap: 0.5rem; }
  .date-buttons { gap: 0.35rem; }
  .date-btn { padding: 0.4rem 0.6rem; font-size: 0.8rem; }
  .tag-actions { flex-direction: column; }
  .btn { text-align: center; }
}
""",
        encoding="utf-8"
    )

# =============== 站点生成 ===============

def collect_dates(data_root: Path) -> List[Tuple[str, Path]]:
    """
    扫描 data/*/ai_summary*.json，返回 [(date_label, json_path), ...]，按日期升序。
    支持两种目录格式:
    - 日期格式: data/2025-12-16/ai_summary.json
    - 月份格式: data/2025-12/ai_summary.json（会被标记为月度数据）
    """
    items = []
    for p in sorted(data_root.glob("*/ai_summary*.json")):
        # 先尝试匹配完整日期格式 YYYY-MM-DD
        m = re.search(r"(\d{4}-\d{2}-\d{2})", str(p))
        if not m:
            m = re.search(r"(\d{4}-\d{2}-\d{2})", p.parent.name)
        
        if m:
            date_label = m.group(1)
        else:
            # 尝试匹配月份格式 YYYY-MM
            m_month = re.search(r"(\d{4}-\d{2})$", p.parent.name)
            if m_month:
                # 标记为月度数据，后续会根据论文发布日期拆分
                date_label = f"MONTH:{m_month.group(1)}"
            else:
                # 实在取不到，用文件修改日期
                ts = datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()
                date_label = ts
        items.append((date_label, p))
    # 去重 & 排序
    items = sorted(list({(d, str(p)): (d, Path(p)) for d, p in items}.values()), key=lambda x: x[0])
    return items

def classify_paper(paper: Dict[str, Any], target_tags: List[str], primary_only: bool = True) -> List[str]:
    """
    判断论文属于哪些目标分类。
    
    Args:
        paper: 论文数据
        target_tags: 目标分类列表
        primary_only: 是否只使用主分类（避免重复）
    
    Returns:
        论文所属的目标分类列表
    """
    paper_categories = paper.get("categories", [])
    primary_category = paper.get("primary_category", "")
    
    # 只使用主分类模式：每篇论文只出现在一个分类下
    if primary_only:
        if primary_category in target_tags:
            return [primary_category]
        # 主分类不在目标列表中，使用第一个匹配的分类
        for cat in paper_categories:
            if cat in target_tags:
                return [cat]
        # 模糊匹配
        for cat in paper_categories:
            for tag in target_tags:
                if cat.lower() == tag.lower():
                    return [tag]
        return []
    
    # 多分类模式：论文可能出现在多个分类下
    matched = []
    if primary_category in target_tags:
        matched.append(primary_category)
    
    for cat in paper_categories:
        if cat in target_tags and cat not in matched:
            matched.append(cat)
    
    if not matched:
        for cat in paper_categories:
            for tag in target_tags:
                if cat.lower() == tag.lower() and tag not in matched:
                    matched.append(tag)
    
    return matched

def save_tag_date_site(docs_dir: Path, tag: str, date_label: str, papers: List[Dict[str, Any]], site_title: str):
    """生成某分类某日期的目录页 + 详情页"""
    safe_tag = tag.replace(".", "-")
    day_dir = docs_dir / safe_tag / date_label
    ensure_dir(day_dir)
    ensure_dir(day_dir / "papers")

    # date index
    date_md = build_tag_date_index_md(tag, date_label, papers, site_title)
    (day_dir / "index.md").write_text(date_md, encoding="utf-8")

    # per-paper pages
    for i, p in enumerate(papers, 1):
        title = p.get("title", "").strip()
        slug = slugify(f"{p.get('arxiv_id','')}-{title}") or f"paper-{i}"
        body_md = render_paper_md(p)
        md = f"---\nlayout: default\ntitle: {title}\n---\n\n{body_md}\n"
        (day_dir / "papers" / f"{slug}.md").write_text(md, encoding="utf-8")

def main():
    ap = argparse.ArgumentParser(description="Build multi-tag, multi-date GitHub Pages.")
    ap.add_argument("--data", default="data", help="数据根目录（默认 data/）")
    ap.add_argument("--outdir", default="docs", help="输出站点目录（默认 docs/）")
    ap.add_argument("--tags", default="tags.json", help="分类配置文件（默认 tags.json）")
    ap.add_argument("--title", default="arXiv 中文要点汇总", help="站点标题")
    args = ap.parse_args()

    data_root = Path(args.data)
    docs_dir = Path(args.outdir)
    tags_file = Path(args.tags)
    site_title = args.title

    # 加载目标分类
    target_tags = load_tags(tags_file)
    print(f"[INFO] 目标分类: {target_tags}")

    pairs = collect_dates(data_root)
    if not pairs:
        print("[ERR] 未找到 data/*/ai_summary*.json", file=sys.stderr)
        sys.exit(2)

    write_site_scaffold(docs_dir)

    # 按分类和日期组织论文
    # tag -> date -> [papers]
    tag_date_papers: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    
    for date_label, json_path in pairs:
        data = read_json(json_path)
        papers = data.get("papers", [])
        if not isinstance(papers, list) or not papers:
            print(f"[WARN] {json_path} 中 papers 为空，跳过 {date_label}")
            continue
        
        # 检查是否为月度数据
        is_monthly = date_label.startswith("MONTH:")
        if is_monthly:
            month_prefix = date_label.replace("MONTH:", "")
            print(f"[INFO] 发现月度数据 {month_prefix}，将根据论文发布日期拆分...")
        
        for paper in papers:
            matched_tags = classify_paper(paper, target_tags)
            if not matched_tags:
                # 没有匹配任何目标分类，放到第一个分类（作为默认）
                matched_tags = [target_tags[0]] if target_tags else []
            
            # 确定论文的日期
            if is_monthly:
                # 从论文的 published 字段获取日期
                paper_date = paper.get("published", "")
                if not paper_date or not re.match(r"\d{4}-\d{2}-\d{2}", paper_date):
                    # 如果没有有效的发布日期，使用 updated 字段
                    paper_date = paper.get("updated", "")
                if not paper_date or not re.match(r"\d{4}-\d{2}-\d{2}", paper_date):
                    # 实在没有日期，使用月份的第一天
                    paper_date = f"{month_prefix}-01"
            else:
                paper_date = date_label
            
            for tag in matched_tags:
                tag_date_papers[tag][paper_date].append(paper)
    
    # 统计
    tag_dates: Dict[str, List[str]] = {}
    for tag in target_tags:
        dates = sorted(tag_date_papers[tag].keys())
        if dates:
            tag_dates[tag] = dates
            print(f"[INFO] {tag}: {len(dates)} 个日期")

    if not tag_dates:
        print("[ERR] 没有可用的分类页面生成", file=sys.stderr)
        sys.exit(3)

    # 生成每个分类的页面
    for tag in target_tags:
        if tag not in tag_dates:
            continue
        safe_tag = tag.replace(".", "-")
        
        for date_label in tag_dates[tag]:
            papers = tag_date_papers[tag][date_label]
            save_tag_date_site(docs_dir, tag, date_label, papers, site_title)
        
        # 生成分类首页
        tag_index_md = build_tag_index_md(tag, tag_dates[tag], site_title)
        tag_dir = docs_dir / safe_tag
        ensure_dir(tag_dir)
        (tag_dir / "index.md").write_text(tag_index_md, encoding="utf-8")

    # 首页：分类导航（包含统计信息）
    tag_stats = {}
    for tag in target_tags:
        if tag not in tag_dates:
            continue
        
        dates = tag_dates[tag]
        sorted_dates = sorted(dates, reverse=True)
        latest_date = sorted_dates[0] if sorted_dates else ""
        recent_dates = sorted_dates[:7]  # 最近7天
        
        # 收集最近的论文并统计支柱分布
        recent_papers = []
        pillar_counts = defaultdict(int)
        total_count = 0
        
        for date in sorted_dates:
            papers_on_date = tag_date_papers[tag][date]
            total_count += len(papers_on_date)
            
            # 只收集最近7天的论文详情
            if date in recent_dates:
                for p in papers_on_date:
                    p_copy = dict(p)
                    p_copy["_date"] = date
                    recent_papers.append(p_copy)
            
            # 统计所有日期的支柱分布
            for p in papers_on_date:
                matched = p.get("matched_interests", [])
                if matched:
                    primary_interest = matched[0].get("name", "其他")
                    pillar_counts[primary_interest] += 1
                else:
                    pillar_counts["其他"] += 1
        
        # 按时间排序最近的论文
        recent_papers.sort(key=lambda x: x.get("_date", ""), reverse=True)
        
        # 统计每个日期的论文数
        date_paper_counts = {date: len(tag_date_papers[tag][date]) for date in sorted_dates}
        
        tag_stats[tag] = {
            "latest_date": latest_date,
            "dates": sorted_dates,
            "recent_dates": recent_dates,
            "recent_papers": recent_papers[:20],  # 只保留最近20篇用于预览
            "date_paper_counts": date_paper_counts,  # 每个日期的实际论文数
            "total_count": total_count,
            "pillar_stats": dict(pillar_counts)
        }
    
    home_md = build_home_md(target_tags, tag_stats, site_title)
    (docs_dir / "index.md").write_text(home_md, encoding="utf-8")

    total_pages = sum(len(dates) for dates in tag_dates.values())
    print(f"[OK] 生成完成。共 {len(tag_dates)} 个分类，{total_pages} 个日期页面。首页：{docs_dir}/index.md")
    print("👉 打开 GitHub → Settings → Pages，Source 选 Branch，目录选 docs/，保存即可。")

if __name__ == "__main__":
    main()

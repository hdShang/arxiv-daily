---
layout: default
title: "HumorPlanSearch: Structured Planning and HuCoT for Contextual AI Humor"
---

# HumorPlanSearch: Structured Planning and HuCoT for Contextual AI Humor

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11429" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11429v1</a>
  <a href="https://arxiv.org/pdf/2508.11429.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11429v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11429v1', 'HumorPlanSearch: Structured Planning and HuCoT for Contextual AI Humor')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shivam Dubey

**分类**: cs.CL

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**提出HumorPlanSearch以解决自动化幽默生成的上下文缺失问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `幽默生成` `上下文建模` `知识图谱` `语义嵌入` `多样性策略` `人机交互` `文化适应性`

## 📋 核心要点

1. 现有的自动化幽默生成方法常常缺乏对上下文的敏感性，导致生成的笑话显得单调和不合时宜。
2. HumorPlanSearch通过模块化设计，结合计划搜索、HuCoT模板和知识图谱等技术，显著增强幽默生成的上下文适应性。
3. 实验结果表明，HumorPlanSearch的完整管道在多个主题上提升了幽默生成评分，验证了其有效性。

## 📝 摘要（中文）

自动化幽默生成常常产生通用、重复或不合时宜的笑话，因为幽默深受听众的文化背景、心态和即时上下文的影响。本文提出HumorPlanSearch，一个模块化的管道，通过计划搜索、幽默链思维（HuCoT）模板、知识图谱、语义嵌入的新颖性过滤和迭代评审修订循环，明确建模上下文。我们提出幽默生成评分（HGS）来评估上下文敏感性和喜剧质量。在对九个主题进行的实验中，结合13位人类评审的反馈，完整管道（知识图谱+修订）使平均HGS提升了15.4%（p < 0.05），推动AI驱动的幽默朝着更连贯、适应性强和文化敏感的方向发展。

## 🔬 方法详解

**问题定义**：本文旨在解决自动化幽默生成中缺乏上下文敏感性的问题。现有方法常常生成的笑话显得通用且缺乏文化适应性，无法满足听众的期望。

**核心思路**：HumorPlanSearch的核心思路是通过模块化的管道设计，明确建模上下文，以便生成更具文化和情境适应性的幽默内容。通过引入多种技术手段，提升幽默生成的质量和多样性。

**技术框架**：该方法的整体架构包括五个主要模块：计划搜索用于制定多样化的主题策略；HuCoT模板用于捕捉文化和风格推理；知识图谱用于检索和适应历史高效策略；语义嵌入用于新颖性过滤；迭代评审修订循环用于优化生成结果。

**关键创新**：HumorPlanSearch的最大创新在于其系统性地将上下文建模融入幽默生成的每一个阶段，显著区别于传统方法的单一生成策略。

**关键设计**：在设计中，采用了多层次的语义嵌入技术来进行新颖性过滤，并通过多维度的反馈机制（如多个人格反馈和配对胜率）来评估幽默生成的质量。

## 📊 实验亮点

在实验中，HumorPlanSearch的完整管道（知识图谱+修订）使幽默生成评分（HGS）平均提升了15.4%（p < 0.05），相较于强基线表现出显著的改进，验证了其在多样化和上下文适应性方面的有效性。

## 🎯 应用场景

HumorPlanSearch的研究成果可以广泛应用于社交媒体、在线娱乐和人机交互等领域，提升自动化幽默生成的质量和用户体验。未来，该技术有望在教育、心理治疗等领域发挥作用，通过适应性幽默促进沟通和理解。

## 📄 摘要（原文）

> Automated humor generation with Large Language Models (LLMs) often yields jokes that feel generic, repetitive, or tone-deaf because humor is deeply situated and hinges on the listener's cultural background, mindset, and immediate context. We introduce HumorPlanSearch, a modular pipeline that explicitly models context through: (1) Plan-Search for diverse, topic-tailored strategies; (2) Humor Chain-of-Thought (HuCoT) templates capturing cultural and stylistic reasoning; (3) a Knowledge Graph to retrieve and adapt high-performing historical strategies; (4) novelty filtering via semantic embeddings; and (5) an iterative judge-driven revision loop. To evaluate context sensitivity and comedic quality, we propose the Humor Generation Score (HGS), which fuses direct ratings, multi-persona feedback, pairwise win-rates, and topic relevance. In experiments across nine topics with feedback from 13 human judges, our full pipeline (KG + Revision) boosts mean HGS by 15.4 percent (p < 0.05) over a strong baseline. By foregrounding context at every stage from strategy planning to multi-signal evaluation, HumorPlanSearch advances AI-driven humor toward more coherent, adaptive, and culturally attuned comedy.


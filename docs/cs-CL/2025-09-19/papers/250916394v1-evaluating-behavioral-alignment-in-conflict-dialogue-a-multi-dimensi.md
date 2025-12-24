---
layout: default
title: "Evaluating Behavioral Alignment in Conflict Dialogue: A Multi-Dimensional Comparison of LLM Agents and Humans"
---

# Evaluating Behavioral Alignment in Conflict Dialogue: A Multi-Dimensional Comparison of LLM Agents and Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16394" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16394v1</a>
  <a href="https://arxiv.org/pdf/2509.16394.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16394v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16394v1', 'Evaluating Behavioral Alignment in Conflict Dialogue: A Multi-Dimensional Comparison of LLM Agents and Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Deuksin Kwon, Kaleen Shrestha, Bin Han, Elena Hayoung Lee, Gale Lucas

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-09-19

**备注**: Accepted to EMNLP 2025 (Main Conference)

---

## 💡 一句话要点

**评估冲突对话中的行为对齐：LLM智能体与人类的多维度对比**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `行为对齐` `冲突对话` `人格化提示` `五因素人格模型`

## 📋 核心要点

1. 现有方法在情感和策略复杂的交互场景中，LLM的行为与人类行为的对齐程度研究不足。
2. 本研究通过人格化提示，使LLM在模拟冲突对话中进行谈判，从而评估其行为与人类的对齐程度。
3. 实验表明，GPT-4.1在语言风格和情感动态上与人类更接近，Claude-3.7-Sonnet在战略行为上表现更优，但仍存在差距。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被部署在社会复杂、交互驱动的任务中，但它们在情感和策略复杂情境中模仿人类行为的能力仍未得到充分探索。本研究通过模拟包含谈判的多轮冲突对话，评估了人格提示LLMs在对抗性争端解决中的行为对齐。每个LLM都由匹配的五因素人格剖面引导，以控制个体差异并增强真实感。我们从三个维度评估对齐：语言风格、情感表达（例如，愤怒动态）和战略行为。GPT-4.1在语言风格和情感动态方面与人类的对齐最为接近，而Claude-3.7-Sonnet最能反映战略行为。尽管如此，仍然存在显著的对齐差距。我们的发现为LLMs和人类在社会复杂互动中的对齐建立了基准，强调了人格条件在对话建模中的希望和局限性。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型（LLMs）在模拟冲突对话中，其行为与人类行为的对齐程度。现有方法缺乏对LLM在情感和策略复杂情境下行为对齐的深入研究，难以评估LLM在社会复杂交互任务中的表现。现有方法难以控制个体差异，缺乏真实感。

**核心思路**：论文的核心思路是通过人格化提示（personality-prompted），赋予LLM特定的人格特征（基于五因素人格模型），然后在模拟的冲突对话中观察其行为表现，并与人类的行为进行对比分析。通过控制LLM的人格特征，可以更好地理解人格对LLM行为的影响，并提高模拟的真实感。

**技术框架**：整体框架包括以下几个主要阶段：1) 人格化LLM：使用五因素人格模型为每个LLM设定特定的人格特征。2) 模拟冲突对话：构建多轮冲突对话场景，让LLM在其中进行谈判。3) 行为评估：从语言风格、情感表达和战略行为三个维度评估LLM的行为表现。4) 对比分析：将LLM的行为表现与人类的行为表现进行对比分析，评估LLM的行为对齐程度。

**关键创新**：论文的关键创新在于：1) 系统性地评估了LLM在社会复杂交互任务中的行为对齐程度，填补了现有研究的空白。2) 采用了人格化提示的方法，通过控制LLM的人格特征，提高了模拟的真实感。3) 从语言风格、情感表达和战略行为三个维度对LLM的行为进行了全面评估。

**关键设计**：论文的关键设计包括：1) 使用五因素人格模型来定义LLM的人格特征。2) 构建多轮冲突对话场景，模拟真实的谈判过程。3) 使用多种指标来评估LLM的语言风格、情感表达和战略行为，例如，使用LIWC（Linguistic Inquiry and Word Count）来分析语言风格，使用情感词典来识别情感表达，使用博弈论模型来分析战略行为。具体参数设置和损失函数未知。

## 📊 实验亮点

实验结果表明，GPT-4.1在语言风格和情感动态方面与人类的对齐最为接近，而Claude-3.7-Sonnet在战略行为方面表现最佳。然而，所有LLM在行为对齐方面都存在显著差距，表明当前LLM在社会复杂交互任务中的表现仍有待提高。具体性能数据未知。

## 🎯 应用场景

该研究成果可应用于开发更智能、更人性化的对话系统，例如，在客户服务、心理咨询、在线教育等领域。通过提高LLM的行为对齐程度，可以增强用户与对话系统的互动体验，提高沟通效率和满意度。此外，该研究还可以为评估和改进LLM的社会适应性提供参考。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in socially complex, interaction-driven tasks, yet their ability to mirror human behavior in emotionally and strategically complex contexts remains underexplored. This study assesses the behavioral alignment of personality-prompted LLMs in adversarial dispute resolution by simulating multi-turn conflict dialogues that incorporate negotiation. Each LLM is guided by a matched Five-Factor personality profile to control for individual variation and enhance realism. We evaluate alignment across three dimensions: linguistic style, emotional expression (e.g., anger dynamics), and strategic behavior. GPT-4.1 achieves the closest alignment with humans in linguistic style and emotional dynamics, while Claude-3.7-Sonnet best reflects strategic behavior. Nonetheless, substantial alignment gaps persist. Our findings establish a benchmark for alignment between LLMs and humans in socially complex interactions, underscoring both the promise and the limitations of personality conditioning in dialogue modeling.


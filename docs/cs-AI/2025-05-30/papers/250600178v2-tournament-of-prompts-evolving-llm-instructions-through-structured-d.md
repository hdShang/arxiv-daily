---
layout: default
title: "Tournament of Prompts: Evolving LLM Instructions Through Structured Debates and Elo Ratings"
---

# Tournament of Prompts: Evolving LLM Instructions Through Structured Debates and Elo Ratings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00178" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00178v2</a>
  <a href="https://arxiv.org/pdf/2506.00178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00178v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00178v2', 'Tournament of Prompts: Evolving LLM Instructions Through Structured Debates and Elo Ratings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anirudh Nair, Adi Banerjee, Laurent Mombaerts, Matthew Hagen, Tarik Borogovac

**分类**: cs.AI, cs.NE

**发布日期**: 2025-05-30 (更新: 2025-07-22)

---

## 💡 一句话要点

**提出DEEVO框架以优化大语言模型的提示工程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示工程` `大语言模型` `辩论驱动` `Elo评分` `自适应优化` `复杂任务` `机器学习`

## 📋 核心要点

1. 现有的提示工程方法在处理复杂任务时面临显著挑战，尤其是在主观质量评估方面，缺乏明确的优化目标。
2. DEEVO框架通过辩论驱动的评估和Elo评分选择，智能地演化提示，克服了传统方法的局限性。
3. 实验结果显示，DEEVO在开放式和封闭式任务中均显著优于手动提示工程和其他优化方法，提升效果明显。

## 📝 摘要（中文）

提示工程是充分发挥大型语言模型（LLMs）潜力的关键瓶颈，尤其在涉及主观质量评估的复杂任务中，明确的优化目标定义变得极具挑战性。现有的自动化提示优化方法在这些场景中表现不佳，通常依赖于明确的任务特定数值适应度函数或通用模板，无法捕捉复杂用例的细微需求。本文提出了DEEVO（基于辩论驱动的进化提示优化）框架，通过辩论驱动的评估和基于Elo评分的选择来指导提示的演变。DEEVO的设计允许在保持语义一致性的同时探索离散提示空间，结合成功与失败提示的优势进行智能交叉和战略突变。实验结果表明，DEEVO在开放式和封闭式任务上显著优于手动提示工程和其他最先进的优化方法，且无需真实反馈。通过将LLMs的推理能力与自适应优化相结合，DEEVO在提示优化研究中代表了重要的进展。

## 🔬 方法详解

**问题定义**：本文旨在解决提示工程中的优化瓶颈，尤其是在主观质量评估任务中，现有方法通常依赖于明确的适应度函数，难以适应复杂需求。

**核心思路**：DEEVO框架通过辩论驱动的反馈机制，结合Elo评分系统，智能演化提示，探索离散提示空间，同时保持语义一致性。

**技术框架**：DEEVO的整体架构包括辩论驱动的评估模块、Elo评分选择模块和提示演化模块，采用智能交叉和突变操作。

**关键创新**：DEEVO的主要创新在于通过辩论反馈进行提示演化，区别于传统方法的随机拼接，强调基于优势的选择。

**关键设计**：在设计中，DEEVO使用Elo评分作为适应度代理，确保提示种群的多样性和持续改进，具体参数设置和损失函数设计未在摘要中详细说明。

## 📊 实验亮点

实验结果表明，DEEVO在开放式和封闭式任务上均显著优于手动提示工程和其他最先进的优化方法，具体性能提升幅度未在摘要中给出，但结果显示其在无真实反馈的情况下仍能有效优化提示。

## 🎯 应用场景

DEEVO框架在多个领域具有广泛的应用潜力，尤其是在需要复杂推理和主观评估的任务中，如内容生成、对话系统和自动化问答等。其自适应优化能力将推动AI系统的持续改进，提升用户体验和任务完成度。

## 📄 摘要（原文）

> Prompt engineering represents a critical bottleneck to harness the full potential of Large Language Models (LLMs) for solving complex tasks, as it requires specialized expertise, significant trial-and-error, and manual intervention. This challenge is particularly pronounced for tasks involving subjective quality assessment, where defining explicit optimization objectives becomes fundamentally problematic. Existing automated prompt optimization methods falter in these scenarios, as they typically require well-defined task-specific numerical fitness functions or rely on generic templates that cannot capture the nuanced requirements of complex use cases. We introduce DEEVO (DEbate-driven EVOlutionary prompt optimization), a novel framework that guides prompt evolution through a debate-driven evaluation with an Elo-based selection. Contrary to prior work, DEEVOs approach enables exploration of the discrete prompt space while preserving semantic coherence through intelligent crossover and strategic mutation operations that incorporate debate-based feedback, combining elements from both successful and unsuccessful prompts based on identified strengths rather than arbitrary splicing. Using Elo ratings as a fitness proxy, DEEVO simultaneously drives improvement and preserves valuable diversity in the prompt population. Experimental results demonstrate that DEEVO significantly outperforms both manual prompt engineering and alternative state-of-the-art optimization approaches on open-ended tasks and close-ended tasks despite using no ground truth feedback. By connecting LLMs reasoning capabilities with adaptive optimization, DEEVO represents a significant advancement in prompt optimization research by eliminating the need of predetermined metrics to continuously improve AI systems.


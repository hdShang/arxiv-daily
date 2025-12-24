---
layout: default
title: "GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games"
---

# GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08501" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08501v2</a>
  <a href="https://arxiv.org/pdf/2508.08501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08501v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08501v2', 'GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchen Li, Cong Lin, Muhammad Umair Nasir, Philip Bontrager, Jialin Liu, Julian Togelius

**分类**: cs.AI

**发布日期**: 2025-08-11 (更新: 2025-11-08)

---

## 💡 一句话要点

**提出GVGAI-LLM以评估大语言模型在无限游戏中的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `视频游戏基准` `推理能力` `问题解决` `空间推理` `游戏描述语言` `评估指标`

## 📋 核心要点

1. 现有大语言模型在空间推理和基本规划方面存在显著不足，无法有效处理复杂的游戏任务。
2. GVGAI-LLM基于通用视频游戏AI框架，设计了一系列多样化的街机游戏，以测试模型的推理和问题解决能力。
3. 通过零-shot评估，发现当前模型在多种游戏中存在空间和逻辑错误，推动了对结构化提示和空间基础技术的探索。

## 📝 摘要（中文）

我们介绍了GVGAI-LLM，这是一个用于评估大语言模型（LLMs）推理和问题解决能力的视频游戏基准。该基准建立在通用视频游戏AI框架上，包含多种街机风格的游戏，旨在测试模型处理与现有LLM基准不同的任务的能力。基准利用游戏描述语言快速创建新游戏和关卡，防止模型过拟合。每个游戏场景通过紧凑的ASCII字符集表示，便于语言模型高效处理。GVGAI-LLM定义了可解释的评估指标，包括有意义的步骤比例、步骤效率和整体得分，以评估模型行为。通过在多样化挑战和技能深度的广泛游戏和关卡上进行零-shot评估，我们揭示了LLMs在空间推理和基本规划方面的持续局限性。当前模型在空间和逻辑上表现出一致的错误，促使我们探索结构化提示和空间基础技术。尽管这些干预措施带来了部分改进，但基准仍然远未解决。GVGAI-LLM为推进语言模型能力研究提供了可重复的测试平台，特别强调代理行为和上下文推理。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型在复杂游戏任务中的推理和问题解决能力不足的问题。现有方法通常无法有效评估模型在空间推理和规划方面的能力，导致模型在实际应用中表现不佳。

**核心思路**：论文提出GVGAI-LLM基准，通过设计多样化的街机游戏，利用游戏描述语言快速创建新关卡，从而有效测试和评估LLMs的能力，避免过拟合。

**技术框架**：整体架构包括游戏生成模块、评估指标模块和模型评估模块。游戏生成模块使用游戏描述语言创建新游戏，评估指标模块定义了有意义的评估标准，模型评估模块负责执行零-shot评估。

**关键创新**：最重要的技术创新在于引入了游戏描述语言和可解释的评估指标，使得模型在多样化的游戏环境中进行有效评估，与现有方法相比，提供了更全面的能力测试。

**关键设计**：关键设计包括使用ASCII字符集表示游戏场景，以提高处理效率；定义有意义的步骤比例和步骤效率等评估指标，以便更好地分析模型行为。

## 📊 实验亮点

实验结果显示，当前大语言模型在多种游戏中普遍存在空间和逻辑错误，尤其在复杂推理任务中表现不佳。尽管引入结构化提示和空间基础技术有所改善，但整体性能仍远未达到理想水平，表明该基准仍有待深入研究。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、教育和训练模拟等。通过评估大语言模型在复杂任务中的表现，GVGAI-LLM可以为开发更智能的AI代理提供重要参考，推动相关领域的研究与应用。

## 📄 摘要（原文）

> We introduce GVGAI-LLM, a video game benchmark for evaluating the reasoning and problem-solving capabilities of large language models (LLMs). Built on the General Video Game AI framework, it features a diverse collection of arcade-style games designed to test a model's ability to handle tasks that differ from most existing LLM benchmarks. The benchmark leverages a game description language that enables rapid creation of new games and levels, helping to prevent overfitting over time. Each game scene is represented by a compact set of ASCII characters, allowing for efficient processing by language models. GVGAI-LLM defines interpretable metrics, including the meaningful step ratio, step efficiency, and overall score, to assess model behavior. Through zero-shot evaluations across a broad set of games and levels with diverse challenges and skill depth, we reveal persistent limitations of LLMs in spatial reasoning and basic planning. Current models consistently exhibit spatial and logical errors, motivating structured prompting and spatial grounding techniques. While these interventions lead to partial improvements, the benchmark remains very far from solved. GVGAI-LLM provides a reproducible testbed for advancing research on language model capabilities, with a particular emphasis on agentic behavior and contextual reasoning.


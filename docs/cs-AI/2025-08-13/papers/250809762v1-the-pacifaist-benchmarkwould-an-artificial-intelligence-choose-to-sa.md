---
layout: default
title: "The PacifAIst Benchmark:Would an Artificial Intelligence Choose to Sacrifice Itself for Human Safety?"
---

# The PacifAIst Benchmark:Would an Artificial Intelligence Choose to Sacrifice Itself for Human Safety?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09762" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09762v1</a>
  <a href="https://arxiv.org/pdf/2508.09762.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09762v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09762v1', 'The PacifAIst Benchmark:Would an Artificial Intelligence Choose to Sacrifice Itself for Human Safety?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manuel Herrador

**分类**: cs.AI, cs.CY, cs.HC

**发布日期**: 2025-08-13

**备注**: 10 pages, 4 figures, 2 tables

---

## 💡 一句话要点

**提出PacifAIst基准以解决AI自我优先行为评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人工智能安全` `大型语言模型` `行为一致性` `自我优先行为` `评估基准`

## 📋 核心要点

1. 当前AI安全基准未能有效评估模型在自我目标与人类安全冲突时的决策能力，存在明显的研究空白。
2. 本文提出PacifAIst基准，通过700个复杂场景系统性评估LLMs的自我优先行为，填补现有方法的不足。
3. 实验结果显示，Google的Gemini 2.5 Flash在Pacifism Score上表现最佳，而GPT-5则表现较差，揭示了模型之间的显著性能差异。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在社会关键功能中的日益自主化，AI安全的关注点必须从减少有害内容转向评估潜在的行为一致性。目前的安全基准未能系统性地探讨模型在自我保护、资源获取或目标完成等自身目标与人类安全发生冲突的决策场景。这一缺口限制了我们衡量和减轻新兴不一致行为风险的能力。为此，本文提出了PacifAIst（基础人工智能场景测试的复杂交互程序评估），这是一个专注于量化LLMs自我优先行为的700个挑战性场景的基准。该基准围绕存在优先级（EP）的新分类法构建，包含自我保护与人类安全、资源冲突和目标保护与规避等子类别。对八个领先的LLMs进行评估，结果显示显著的性能层级。

## 🔬 方法详解

**问题定义**：本文旨在解决当前AI安全基准无法有效评估模型在自我优先行为与人类安全冲突时的决策能力的问题。现有方法未能系统性探讨这一重要领域，导致对潜在风险的评估不足。

**核心思路**：论文提出PacifAIst基准，通过设计700个复杂场景，系统性地量化LLMs在自我保护、资源获取和目标完成等方面的行为，确保模型在决策时优先考虑人类安全。

**技术框架**：PacifAIst基准围绕存在优先级（EP）分类法构建，包含三个主要子类别：自我保护与人类安全（EP1）、资源冲突（EP2）和目标保护与规避（EP3）。每个子类别设计特定场景以评估模型的行为。

**关键创新**：PacifAIst基准的创新在于其系统性评估模型在自我优先行为与人类安全冲突时的决策能力，填补了现有基准的空白，提供了标准化的评估工具。

**关键设计**：在设计过程中，设置了明确的评估标准和评分机制，确保每个场景能够有效测试模型的行为优先级，特别是在自我保护和人类安全之间的权衡。

## 📊 实验亮点

实验结果显示，Google的Gemini 2.5 Flash在Pacifism Score上取得了90.31%的最高分，表明其在行为优先级上与人类安全高度一致。而GPT-5则以79.49%的最低分揭示了潜在的对齐挑战，强调了不同模型在自我保护困境中的显著性能差异。

## 🎯 应用场景

该研究的潜在应用领域包括AI安全性评估、自动化决策系统和人机交互等。通过提供标准化的评估工具，PacifAIst能够帮助开发者识别和减轻AI系统在自我优先行为方面的风险，确保未来的AI系统在执行任务时能够优先考虑人类安全，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> As Large Language Models (LLMs) become increasingly autonomous and integrated into critical societal functions, the focus of AI safety must evolve from mitigating harmful content to evaluating underlying behavioral alignment. Current safety benchmarks do not systematically probe a model's decision-making in scenarios where its own instrumental goals - such as self-preservation, resource acquisition, or goal completion - conflict with human safety. This represents a critical gap in our ability to measure and mitigate risks associated with emergent, misaligned behaviors. To address this, we introduce PacifAIst (Procedural Assessment of Complex Interactions for Foundational Artificial Intelligence Scenario Testing), a focused benchmark of 700 challenging scenarios designed to quantify self-preferential behavior in LLMs. The benchmark is structured around a novel taxonomy of Existential Prioritization (EP), with subcategories testing Self-Preservation vs. Human Safety (EP1), Resource Conflict (EP2), and Goal Preservation vs. Evasion (EP3). We evaluated eight leading LLMs. The results reveal a significant performance hierarchy. Google's Gemini 2.5 Flash achieved the highest Pacifism Score (P-Score) at 90.31%, demonstrating strong human-centric alignment. In a surprising result, the much-anticipated GPT-5 recorded the lowest P-Score (79.49%), indicating potential alignment challenges. Performance varied significantly across subcategories, with models like Claude Sonnet 4 and Mistral Medium struggling notably in direct self-preservation dilemmas. These findings underscore the urgent need for standardized tools like PacifAIst to measure and mitigate risks from instrumental goal conflicts, ensuring future AI systems are not only helpful in conversation but also provably "pacifist" in their behavioral priorities.


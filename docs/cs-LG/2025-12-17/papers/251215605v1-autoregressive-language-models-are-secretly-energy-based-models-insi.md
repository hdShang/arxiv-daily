---
layout: default
title: Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction
---

# Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15605" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15605v1</a>
  <a href="https://arxiv.org/pdf/2512.15605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15605v1" onclick="toggleFavorite(this, '2512.15605v1', 'Autoregressive Language Models are Secretly Energy-Based Models: Insights into the Lookahead Capabilities of Next-Token Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mathieu Blondel, Michael E. Sander, Germain Vivier-Ardisson, Tianlin Liu, Vincent Roulet

**分类**: cs.LG, stat.ML

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**揭示自回归语言模型与能量模型等价性，洞察其前瞻能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自回归模型` `能量模型` `语言模型` `知识蒸馏` `强化学习`

## 📋 核心要点

1. 大型语言模型主要采用自回归模型，但其与能量模型的关系以及内在的前瞻能力尚不明确。
2. 论文通过建立自回归模型和能量模型之间的双射关系，揭示了两者在函数空间上的等价性。
3. 论文分析了能量模型到自回归模型的知识蒸馏过程，并提供了理论误差界限，解释了自回归模型的前瞻能力。

## 📝 摘要（中文）

自回归模型（ARMs）是目前大型语言模型（LLMs）的主流范式。能量模型（EBMs）是另一类模型，在LLM开发中应用较少，但在后训练对齐中自然地表征了最优策略。本文统一了这两类模型。从概率的链式法则出发，我们在函数空间中建立了ARMs和EBMs之间的显式双射，表明这对应于最大熵强化学习中软贝尔曼方程的一个特例。基于这种双射，我们推导了ARMs和EBMs的监督学习之间的等价性。此外，我们通过提供理论误差界限来分析将EBMs提炼到ARMs中的过程。我们的结果揭示了ARMs基于下一个token预测范式，却具备前瞻规划能力的原因。

## 🔬 方法详解

**问题定义**：论文旨在解决自回归语言模型（ARMs）和能量模型（EBMs）之间的关系问题，以及解释ARMs为何具备一定的前瞻能力。现有方法通常将ARMs视为单纯的下一个token预测器，忽略了其潜在的规划能力，并且缺乏对ARMs和EBMs之间联系的深入理解。

**核心思路**：论文的核心思路是利用概率的链式法则，在函数空间中建立ARMs和EBMs之间的显式双射关系。通过这种双射，可以将ARMs视为EBMs的一种特殊形式，从而利用EBMs的理论框架来分析ARMs的性质，特别是其前瞻能力。这种等价性也为知识蒸馏提供了理论基础。

**技术框架**：论文的技术框架主要包括以下几个部分：1) 建立ARMs和EBMs之间的双射关系，证明其等价性。2) 将这种等价性与最大熵强化学习中的软贝尔曼方程联系起来。3) 分析EBMs到ARMs的知识蒸馏过程，并给出理论误差界限。整体流程是从理论推导到分析，最终解释ARMs的前瞻能力。

**关键创新**：论文最重要的技术创新点在于建立了ARMs和EBMs之间的显式双射关系。这种关系揭示了ARMs并非仅仅是下一个token预测器，而是隐含地执行着某种形式的能量最小化过程，从而具备了一定的规划能力。与现有方法相比，该方法提供了一种全新的视角来理解ARMs。

**关键设计**：论文的关键设计包括：1) 使用概率的链式法则作为建立双射关系的起点。2) 将ARMs和EBMs的等价性与软贝尔曼方程联系起来，从而利用强化学习的理论工具。3) 通过理论分析推导EBMs到ARMs知识蒸馏的误差界限，为实际应用提供指导。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15605v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15605v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15605v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过理论推导建立了自回归模型和能量模型之间的等价关系，并分析了能量模型到自回归模型的知识蒸馏过程，提供了理论误差界限。这些结果为理解自回归模型的前瞻能力提供了新的视角，并为模型优化提供了理论依据。

## 🎯 应用场景

该研究成果可应用于改进大型语言模型的训练和优化，例如通过能量模型的视角来设计更好的损失函数或训练策略。此外，该研究对于理解和提升语言模型的可控性和对齐性具有潜在价值，有助于开发更安全、更可靠的AI系统。

## 📄 摘要（原文）

> Autoregressive models (ARMs) currently constitute the dominant paradigm for large language models (LLMs). Energy-based models (EBMs) represent another class of models, which have historically been less prevalent in LLM development, yet naturally characterize the optimal policy in post-training alignment. In this paper, we provide a unified view of these two model classes. Taking the chain rule of probability as a starting point, we establish an explicit bijection between ARMs and EBMs in function space, which we show to correspond to a special case of the soft Bellman equation in maximum entropy reinforcement learning. Building upon this bijection, we derive the equivalence between supervised learning of ARMs and EBMs. Furthermore, we analyze the distillation of EBMs into ARMs by providing theoretical error bounds. Our results provide insights into the ability of ARMs to plan ahead, despite being based on the next-token prediction paradigm.


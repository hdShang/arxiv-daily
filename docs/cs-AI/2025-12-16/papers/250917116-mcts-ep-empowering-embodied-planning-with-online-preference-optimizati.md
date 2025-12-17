---
layout: default
title: MCTS-EP: Empowering Embodied Planning with Online Preference Optimization
---

# MCTS-EP: Empowering Embodied Planning with Online Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17116" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17116</a>
  <a href="https://arxiv.org/pdf/2509.17116.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17116" onclick="toggleFavorite(this, '2509.17116', 'MCTS-EP: Empowering Embodied Planning with Online Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hang Xu, Zang Yu, Yehui Tang, Pengbo Hu, Yuhao Tang, Hao Dong

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**MCTS-EP：结合在线偏好优化的蒙特卡洛树搜索赋能具身智能规划**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `蒙特卡洛树搜索` `偏好优化` `多模态推理` `在线学习` `大型语言模型` `强化学习`

## 📋 核心要点

1. 现有具身智能体训练方法在探索效率和利用多模态信息方面存在不足，限制了其在复杂环境中的应用。
2. MCTS-EP利用MCTS引导探索，高效收集偏好数据，并结合多模态推理机制，实现更有效的在线学习。
3. 实验表明，MCTS-EP在ALFWorld和WebShop等基准测试中取得了显著的性能提升，并减少了交互步骤。

## 📝 摘要（中文）

本文提出了一种名为MCTS-EP的在线学习框架，该框架将大型语言模型（LLM）与蒙特卡洛树搜索（MCTS）相结合，用于训练具身智能体。MCTS-EP集成了三个关键组成部分：用于偏好数据收集的MCTS引导探索、高效的多模态推理机制以及基于偏好优化的迭代训练流程。我们从理论上证明，当损失函数是强凸函数时，MCTS-EP比传统的on-policy算法具有更好的性能界限，并证明它可以被表述为一种搜索增强的GAIL变体。MCTS-EP在多个基准测试中实现了最先进的性能。在ALFWorld中，它在文本和视觉任务中分别实现了92%和87%的成功率。在WebShop中，它达到了0.81的平均奖励。MCTS-EP还在视觉任务中将平均交互步骤从18.7/19.5步减少到10.2/9.9步。

## 🔬 方法详解

**问题定义**：现有具身智能体训练方法通常面临探索效率低下的问题，难以充分利用环境中的信息。此外，如何有效融合文本、视觉等多模态信息也是一个挑战，限制了智能体在复杂任务中的表现。传统的on-policy算法在面对非凸损失函数时，性能表现可能不佳。

**核心思路**：MCTS-EP的核心在于利用蒙特卡洛树搜索（MCTS）来指导智能体的探索过程，从而更有效地收集偏好数据。通过在线偏好优化，智能体可以逐步学习到更优的策略。同时，该方法结合多模态推理机制，充分利用环境中的各种信息。

**技术框架**：MCTS-EP框架包含三个主要组成部分：1) MCTS引导的探索模块，用于生成高质量的偏好数据；2) 多模态推理模块，用于融合文本和视觉信息，做出更明智的决策；3) 基于偏好优化的迭代训练流程，通过不断学习和改进，提升智能体的性能。整个框架采用在线学习的方式，智能体在与环境交互的过程中不断学习和优化。

**关键创新**：MCTS-EP的关键创新在于将MCTS与偏好优化相结合，实现更高效的探索和学习。与传统的on-policy算法相比，MCTS-EP在理论上具有更好的性能界限，尤其是在损失函数为强凸函数时。此外，该方法可以被视为一种搜索增强的GAIL变体，结合了生成对抗模仿学习的优势。

**关键设计**：MCTS-EP的具体实现细节包括：如何设计MCTS的奖励函数，以鼓励智能体探索更有价值的状态；如何构建多模态推理模块，以有效融合文本和视觉信息；如何选择合适的偏好优化算法，以保证学习的稳定性和效率。具体的参数设置和网络结构需要根据具体的任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.17116/framework.png" alt="fig_0" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MCTS-EP在ALFWorld文本和视觉任务中分别实现了92%和87%的成功率，显著优于现有方法。在WebShop中，MCTS-EP达到了0.81的平均奖励。此外，MCTS-EP还显著减少了交互步骤，在视觉任务中从18.7/19.5步减少到10.2/9.9步，表明其具有更高的效率。

## 🎯 应用场景

MCTS-EP具有广泛的应用前景，可应用于机器人导航、智能家居、自动驾驶等领域。通过结合大型语言模型和蒙特卡洛树搜索，该方法能够使智能体在复杂环境中进行更有效的规划和决策，从而实现更智能化的服务和应用。未来，该方法有望在更多实际场景中得到应用，提升人工智能的水平。

## 📄 摘要（原文）

> This paper introduces MCTS-EP, an online learning framework that combines large language models (LLM) with Monte Carlo Tree Search (MCTS) for training embodied agents. MCTS-EP integrates three key components: MCTS-guided exploration for preference data collection, efficient multi-modal reasoning mechanism, and iterative training pipeline based on preference optimization. We theoretically prove that MCTS-EP achieves better performance bounds than conventional on-policy algorithms when the loss function is strongly convex, and demonstrate that it can be formulated as a search-enhanced variant of GAIL. MCTS-EP achieves state-of-the-art performace across serval benchmarks. In ALFWorld, it achieves 92% and 87% success rates for textual and visual tasks. In WebShop, it reaches an average reward of 0.81. MTCS-EP also reduces average interaction steps from from 18.7/19.5 to 10.2/9.9 steps in visualthis http URLavailable at:this https URL


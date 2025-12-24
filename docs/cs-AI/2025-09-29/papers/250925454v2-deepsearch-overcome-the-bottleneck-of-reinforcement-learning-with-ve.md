---
layout: default
title: "DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search"
---

# DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25454" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25454v2</a>
  <a href="https://arxiv.org/pdf/2509.25454.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25454v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25454v2', 'DeepSearch: Overcome the Bottleneck of Reinforcement Learning with Verifiable Rewards via Monte Carlo Tree Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fang Wu, Weihao Xuan, Heli Qi, Ximing Lu, Aaron Tu, Li Erran Li, Yejin Choi

**分类**: cs.AI, cs.CL

**发布日期**: 2025-09-29 (更新: 2025-10-01)

---

## 💡 一句话要点

**DeepSearch：通过蒙特卡洛树搜索和可验证奖励克服强化学习瓶颈**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `蒙特卡洛树搜索` `可验证奖励` `大型语言模型` `推理` `探索` `信用分配`

## 📋 核心要点

1. 现有RLVR方法在训练过程中存在探索不足的问题，导致性能提升停滞，无法充分利用计算资源。
2. DeepSearch将蒙特卡洛树搜索集成到RLVR训练中，通过结构化搜索实现系统探索和细粒度信用分配。
3. 实验表明，DeepSearch在数学推理任务上取得了显著的性能提升，并大幅减少了训练所需的计算资源。

## 📝 摘要（中文）

尽管RLVR已成为开发LLM中高级推理能力的关键组成部分，但现有研究表明，经过数千次优化步骤后会出现训练停滞，尽管计算投入增加，性能提升却显著下降。这种限制源于当前RLVR实践中固有的稀疏探索模式，模型依赖于有限的rollout，这通常会错过关键的推理路径，并且无法系统地覆盖解决方案空间。我们提出了DeepSearch，一个将蒙特卡洛树搜索直接集成到RLVR训练中的框架。与仅在推理时依赖树搜索的现有方法不同，DeepSearch将结构化搜索嵌入到训练循环中，从而实现系统的探索和跨推理步骤的细粒度信用分配。通过训练时探索，DeepSearch解决了探索不足的根本瓶颈，从而导致长时间训练步骤中性能提升的降低。我们的贡献包括：（1）一种全局前沿选择策略，优先考虑搜索树中有希望的节点，（2）基于熵引导的选择，用于识别有信心的路径以进行监督，以及（3）具有解决方案缓存的自适应重放缓冲区训练以提高效率。在数学推理基准上的实验表明，DeepSearch实现了62.95%的平均准确率，并为1.5B推理模型建立了新的state-of-the-art，使用的GPU时间比扩展训练方法少5.7倍。这些结果突出了战略探索相对于蛮力扩展的重要性，并证明了算法创新在推进RLVR方法论方面的希望。DeepSearch为通过系统搜索而不是长时间计算来扩展推理能力建立了一个新的方向。

## 🔬 方法详解

**问题定义**：现有基于强化学习的可验证奖励（RLVR）方法在训练大型语言模型进行复杂推理时，面临探索空间不足的问题。模型在训练过程中容易陷入局部最优，难以发现有效的推理路径，导致训练效率低下，性能提升缓慢。现有方法依赖于有限的rollout，无法系统地覆盖解决方案空间，造成了训练瓶颈。

**核心思路**：DeepSearch的核心思路是将蒙特卡洛树搜索（MCTS）直接嵌入到RLVR的训练循环中。通过在训练时进行结构化搜索，DeepSearch能够更全面地探索推理空间，并为每个推理步骤进行细粒度的信用分配。这种方法旨在解决现有RLVR方法中探索不足的问题，从而提高训练效率和模型性能。

**技术框架**：DeepSearch的整体框架包括以下几个主要模块：1) 蒙特卡洛树搜索：用于在训练过程中进行结构化探索；2) 全局前沿选择策略：用于优先选择搜索树中有希望的节点进行扩展；3) 基于熵引导的选择：用于识别置信度高的推理路径进行监督学习；4) 自适应重放缓冲区：用于存储和重用有效的推理路径，提高训练效率。

**关键创新**：DeepSearch的关键创新在于将MCTS集成到RLVR的训练循环中。与现有方法仅在推理时使用树搜索不同，DeepSearch在训练过程中利用MCTS进行系统探索，从而解决了探索不足的根本问题。此外，全局前沿选择策略和基于熵引导的选择进一步提高了搜索效率和训练效果。

**关键设计**：DeepSearch的关键设计包括：1) 全局前沿选择策略，该策略基于节点的分数和访问次数来选择下一个要扩展的节点；2) 基于熵引导的选择，该策略利用模型对每个推理步骤的置信度来指导搜索方向；3) 自适应重放缓冲区，该缓冲区根据推理路径的质量动态调整存储概率，从而优先存储和重用有效的推理路径。

## 📊 实验亮点

DeepSearch在数学推理基准测试中取得了显著成果，平均准确率达到62.95%，为1.5B参数的推理模型建立了新的state-of-the-art。与传统的扩展训练方法相比，DeepSearch使用的GPU时间减少了5.7倍，证明了其在提高训练效率方面的优势。这些结果表明，DeepSearch能够有效地解决RLVR训练中的探索瓶颈，并显著提升模型的推理能力。

## 🎯 应用场景

DeepSearch具有广泛的应用前景，可用于提升大型语言模型在各种复杂推理任务中的性能，例如数学推理、逻辑推理、常识推理等。该方法还可以应用于机器人控制、游戏AI等领域，通过系统探索和细粒度信用分配，提高智能体的学习效率和决策能力。DeepSearch的成功表明，算法创新在提升AI系统能力方面具有重要作用。

## 📄 摘要（原文）

> Although RLVR has become an essential component for developing advanced reasoning skills in LLMs, contemporary studies have documented training plateaus that emerge following thousands of optimization steps, demonstrating notable decreases in performance gains despite increased computational investment. This limitation stems from the sparse exploration patterns inherent in current RLVR practices, where models rely on limited rollouts that often miss critical reasoning paths and fail to provide systematic coverage of the solution space. We present DeepSearch, a framework that integrates Monte Carlo Tree Search directly into RLVR training. In contrast to existing methods that rely on tree search only at inference, DeepSearch embeds structured search into the training loop, enabling systematic exploration and fine-grained credit assignment across reasoning steps. Through training-time exploration, DeepSearch addresses the fundamental bottleneck of insufficient exploration, which leads to diminishing performance improvements over prolonged training steps. Our contributions include: (1) a global frontier selection strategy that prioritizes promising nodes across the search tree, (2) selection with entropy-based guidance that identifies confident paths for supervision, and (3) adaptive replay buffer training with solution caching for efficiency. Experiments on mathematical reasoning benchmarks show that DeepSearch achieves 62.95% average accuracy and establishes a new state-of-the-art for 1.5B reasoning models - using 5.7x fewer GPU hours than extended training approaches. These results highlight the importance of strategic exploration over brute-force scaling and demonstrate the promise of algorithmic innovation for advancing RLVR methodologies. DeepSearch establishes a new direction for scaling reasoning capabilities through systematic search rather than prolonged computation.


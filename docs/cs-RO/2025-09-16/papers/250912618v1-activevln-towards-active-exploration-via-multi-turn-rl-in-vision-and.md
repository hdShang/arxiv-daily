---
layout: default
title: "ActiveVLN: Towards Active Exploration via Multi-Turn RL in Vision-and-Language Navigation"
---

# ActiveVLN: Towards Active Exploration via Multi-Turn RL in Vision-and-Language Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.12618" class="toolbar-btn" target="_blank">📄 arXiv: 2509.12618v1</a>
  <a href="https://arxiv.org/pdf/2509.12618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.12618v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.12618v1', 'ActiveVLN: Towards Active Exploration via Multi-Turn RL in Vision-and-Language Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zekai Zhang, Weiye Zhu, Hewei Pan, Xiangchen Wang, Rongtao Xu, Xing Sun, Feng Zheng

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-09-16

---

## 💡 一句话要点

**ActiveVLN：基于多轮强化学习的主动探索视觉语言导航**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言导航` `强化学习` `主动探索` `模仿学习` `多模态学习`

## 📋 核心要点

1. 现有VLN方法依赖模仿学习和DAgger，数据收集和训练成本高昂，且缺乏与环境的动态交互。
2. ActiveVLN通过多轮强化学习实现主动探索，允许智能体自主收集多样化轨迹并优化导航策略。
3. 实验表明，ActiveVLN在性能上超越了传统方法，并使用较小模型达到了与SOTA方法相当的水平。

## 📝 摘要（中文）

视觉语言导航(VLN)任务要求智能体根据自然语言指令在复杂环境中导航。现有的基于MLLM的VLN方法主要依赖于模仿学习(IL)，并经常使用DAgger进行后训练以减轻协变量偏移。虽然这些方法有效，但会产生大量的数据收集和训练成本。强化学习(RL)提供了一个有希望的替代方案。然而，先前的VLN RL方法缺乏与环境的动态交互，并且依赖于专家轨迹进行奖励塑造，而不是进行开放式的主动探索。这限制了智能体发现多样化和合理的导航路线的能力。为了解决这些限制，我们提出了ActiveVLN，一个VLN框架，通过多轮RL显式地实现主动探索。在第一阶段，使用一小部分专家轨迹进行IL来引导智能体。在第二阶段，智能体迭代地预测和执行动作，自动收集多样化的轨迹，并通过GRPO目标优化多个rollout。为了进一步提高RL效率，我们引入了一种动态提前停止策略来修剪长尾或可能失败的轨迹，以及额外的工程优化。实验表明，与基于DAgger和先前的基于RL的后训练方法相比，ActiveVLN在IL基线上实现了最大的性能提升，同时在使用较小模型的情况下达到了与最先进方法相当的性能。代码和数据即将发布。

## 🔬 方法详解

**问题定义**：现有的视觉语言导航（VLN）方法，特别是基于大型语言模型的（MLLM），主要依赖于模仿学习（IL），并使用DAgger进行后训练以解决协变量偏移问题。这些方法虽然有效，但需要大量的专家数据进行训练，成本高昂。此外，这些方法通常缺乏与环境的动态交互，依赖专家轨迹进行奖励塑造，限制了智能体探索多样化导航路线的能力。

**核心思路**：ActiveVLN的核心思路是通过多轮强化学习（RL）实现主动探索。智能体不再仅仅模仿专家轨迹，而是通过与环境的交互，自主地发现和学习更优的导航策略。通过迭代地预测和执行动作，智能体能够自动收集多样化的轨迹，并利用这些轨迹进行策略优化。

**技术框架**：ActiveVLN框架包含两个主要阶段。第一阶段，使用少量专家轨迹进行模仿学习，以引导智能体初步学习导航策略。第二阶段，智能体进入主动探索阶段，迭代地执行以下步骤：1) 智能体根据当前策略预测并执行动作；2) 智能体与环境交互，收集轨迹数据；3) 使用收集到的轨迹数据，通过GRPO目标优化策略。此外，框架还引入了动态提前停止策略，以提高RL的效率。

**关键创新**：ActiveVLN最重要的技术创新点在于其主动探索机制。与传统的依赖专家轨迹的VLN方法不同，ActiveVLN允许智能体自主地与环境交互，发现多样化的导航路线。这种主动探索机制使得智能体能够学习到更鲁棒、更适应环境变化的导航策略。此外，动态提前停止策略也是一个重要的创新，它能够有效地减少不必要的计算，提高RL的效率。

**关键设计**：ActiveVLN的关键设计包括：1) 使用GRPO（Generalized Policy Optimization）作为强化学习的目标函数，以优化智能体的导航策略；2) 引入动态提前停止策略，根据轨迹的早期表现，判断是否提前终止该轨迹的探索，从而节省计算资源；3) 使用少量专家轨迹进行模仿学习，以引导智能体初步学习导航策略，避免从零开始探索。

## 📊 实验亮点

ActiveVLN在实验中表现出显著的性能提升。与基于DAgger和先前的基于RL的后训练方法相比，ActiveVLN在IL基线上实现了最大的性能提升。更重要的是，ActiveVLN在使用较小模型的情况下，达到了与最先进方法相当的性能，证明了其高效性和有效性。这些结果表明，通过主动探索和多轮强化学习，可以显著提高VLN任务的性能。

## 🎯 应用场景

ActiveVLN的研究成果可应用于机器人导航、虚拟现实、自动驾驶等领域。例如，在机器人导航中，可以使机器人在未知环境中自主探索并完成导航任务。在虚拟现实中，可以为用户提供更自然、更智能的导航体验。在自动驾驶领域，可以提高自动驾驶系统在复杂环境中的适应性和鲁棒性。

## 📄 摘要（原文）

> The Vision-and-Language Navigation (VLN) task requires an agent to follow natural language instructions and navigate through complex environments. Existing MLLM-based VLN methods primarily rely on imitation learning (IL) and often use DAgger for post-training to mitigate covariate shift. While effective, these approaches incur substantial data collection and training costs. Reinforcement learning (RL) offers a promising alternative. However, prior VLN RL methods lack dynamic interaction with the environment and depend on expert trajectories for reward shaping, rather than engaging in open-ended active exploration. This restricts the agent's ability to discover diverse and plausible navigation routes. To address these limitations, we propose ActiveVLN, a VLN framework that explicitly enables active exploration through multi-turn RL. In the first stage, a small fraction of expert trajectories is used for IL to bootstrap the agent. In the second stage, the agent iteratively predicts and executes actions, automatically collects diverse trajectories, and optimizes multiple rollouts via the GRPO objective. To further improve RL efficiency, we introduce a dynamic early-stopping strategy to prune long-tail or likely failed trajectories, along with additional engineering optimizations. Experiments show that ActiveVLN achieves the largest performance gains over IL baselines compared to both DAgger-based and prior RL-based post-training methods, while reaching competitive performance with state-of-the-art approaches despite using a smaller model. Code and data will be released soon.


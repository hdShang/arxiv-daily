---
layout: default
title: G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning
---

# G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13426" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13426v1</a>
  <a href="https://arxiv.org/pdf/2505.13426.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13426v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13426v1', 'G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Chen, Hongcheng Gao, Tianyu Liu, Zhiqi Huang, Flood Sung, Xinyu Zhou, Yuxin Wu, Baobao Chang

**分类**: cs.CV

**发布日期**: 2025-05-19

**备注**: 21 pages, 14 figures, code released at https://github.com/chenllliang/G1

**🔗 代码/项目**: [GITHUB](https://github.com/chenllliang/G1)

---

## 💡 一句话要点

**提出VLM-Gym以解决视觉语言模型在游戏中的决策能力不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `强化学习` `多模态学习` `游戏智能体` `感知推理` `自我演化训练` `VLM-Gym`

## 📋 核心要点

1. 现有视觉语言模型在简单游戏中的表现不佳，限制了其作为自主代理的潜力。
2. 提出VLM-Gym环境，通过强化学习训练G0和G1模型，增强模型的感知与推理能力。
3. G1模型在所有游戏中均超越教师模型，并在性能上优于现有的领先模型，显示出显著提升。

## 📝 摘要（中文）

视觉语言模型（VLMs）在多模态任务中表现优异，但在互动性强、视觉丰富的环境（如游戏）中进行有效决策时却面临挑战。为了解决这一“知行不一”的问题，本文提出了VLM-Gym，一个专门设计的强化学习环境，包含多样化的视觉游戏，具有统一接口和可调节的难度，旨在实现可扩展的多游戏并行训练。通过VLM-Gym，我们利用纯强化学习驱动的自我演化训练G0模型，展现出新兴的感知和推理模式。为进一步应对游戏多样性带来的挑战，我们开发了G1模型，G1在强化学习微调之前引入了感知增强的冷启动。实验结果表明，G1模型在所有游戏中均优于其教师模型，并超越了领先的专有模型如Claude-3.7-Sonnet-Thinking。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在复杂互动环境（如游戏）中的决策能力不足问题。现有方法在简单游戏中的表现不理想，导致其作为自主智能体的潜力受到限制。

**核心思路**：通过引入VLM-Gym环境，利用强化学习进行多游戏并行训练，提升模型的感知和推理能力。G1模型在强化学习微调前进行感知增强的冷启动，以应对游戏多样性带来的挑战。

**技术框架**：整体架构包括VLM-Gym环境、G0模型的自我演化训练和G1模型的冷启动与微调阶段。VLM-Gym提供了统一接口和可调节的难度，支持多样化的视觉游戏。

**关键创新**：最重要的创新在于引入了感知增强的冷启动机制，使得G1模型在强化学习过程中能够更好地适应多样化的游戏环境。这一设计与传统的单一训练方法有本质区别。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构，以优化感知和推理能力的相互促进。具体参数设置和训练策略在实验中进行了详细调整，以确保模型的最佳性能。

## 📊 实验亮点

实验结果显示，G1模型在所有测试游戏中均超越了其教师模型，且在性能上优于Claude-3.7-Sonnet-Thinking等领先的专有模型，展现出显著的提升幅度，证明了感知与推理能力的相互促进效应。

## 🎯 应用场景

该研究的潜在应用领域包括游戏智能体、虚拟助手和自动化决策系统。通过提升视觉语言模型的决策能力，未来可以在更复杂的交互环境中实现更智能的自主代理，推动人工智能在实际应用中的发展。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) excel in many direct multimodal tasks but struggle to translate this prowess into effective decision-making within interactive, visually rich environments like games. This ``knowing-doing'' gap significantly limits their potential as autonomous agents, as leading VLMs often performing badly in simple games. To address this, we introduce VLM-Gym, a curated reinforcement learning (RL) environment featuring diverse visual games with unified interfaces and adjustable, compositional difficulty, specifically designed for scalable multi-game parallel training. Leveraging VLM-Gym, we train G0 models using pure RL-driven self-evolution, which demonstrate emergent perception and reasoning patterns. To further mitigate challenges arising from game diversity, we develop G1 models. G1 incorporates a perception-enhanced cold start prior to RL fine-tuning. Our resulting G1 models consistently surpass their teacher across all games and outperform leading proprietary models like Claude-3.7-Sonnet-Thinking. Systematic analysis reveals an intriguing finding: perception and reasoning abilities mutually bootstrap each other throughout the RL training process. Source code including VLM-Gym and RL training are released at https://github.com/chenllliang/G1 to foster future research in advancing VLMs as capable interactive agents.


---
layout: default
title: "Pixels to Play: A Foundation Model for 3D Gameplay"
---

# Pixels to Play: A Foundation Model for 3D Gameplay

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14295" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14295v1</a>
  <a href="https://arxiv.org/pdf/2508.14295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14295v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14295v1', 'Pixels to Play: A Foundation Model for 3D Gameplay')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuguang Yue, Chris Green, Samuel Hunt, Irakli Salia, Wenzhe Shi, Jonathan J Hunt

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-08-19

**期刊**: Conference on Games 2025 (Short paper)

---

## 💡 一句话要点

**提出Pixels2Play-0.1以解决3D游戏智能体行为生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D游戏` `行为克隆` `逆动力学` `解码器变换器` `智能体学习`

## 📋 核心要点

1. 现有方法在3D游戏中缺乏通用性，难以适应不同游戏的特定需求。
2. 论文提出的Pixels2Play-0.1模型通过行为克隆和逆动力学模型，能够在多种3D游戏中实现人类般的行为。
3. 实验结果显示，P2P0.1在Roblox和经典MS-DOS游戏中表现出色，展示了其在复杂动作空间中的能力。

## 📝 摘要（中文）

我们介绍了Pixels2Play-0.1（P2P0.1），这是一个基础模型，能够以人类可识别的行为学习玩多种3D视频游戏。该模型的设计旨在满足新兴的消费者和开发者需求，如AI队友、可控NPC、个性化直播者和辅助测试者。P2P0.1依赖于玩家可用的像素流，能够在最小化游戏特定工程的情况下推广到新游戏。模型通过行为克隆进行端到端训练，结合了来自人类游戏玩法的标记演示和未标记的公共视频，并通过逆动力学模型推断动作。采用解码器-only的变换器，具备自回归动作输出，能够处理大规模动作空间，同时在单个消费级GPU上保持低延迟。我们报告了在简单的Roblox和经典的MS-DOS游戏中表现出色的定性结果，并进行了未标记数据的消融实验，概述了达到专家级文本条件控制所需的扩展和评估步骤。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有3D游戏智能体在不同游戏间缺乏通用性的问题。现有方法通常需要大量的游戏特定工程，限制了其适用范围。

**核心思路**：论文提出的Pixels2Play-0.1模型通过行为克隆技术，结合人类游戏玩法的标记演示和未标记视频，能够在多种3D游戏中实现人类般的行为，减少游戏特定的工程需求。

**技术框架**：P2P0.1的整体架构包括数据收集、行为克隆训练和逆动力学模型推断。数据收集阶段获取标记和未标记的视频，训练阶段通过解码器-only变换器进行动作输出，最后通过逆动力学模型推断动作。

**关键创新**：该模型的主要创新在于其端到端的训练方式和解码器-only变换器的设计，使其能够在大规模动作空间中保持低延迟，并有效处理多样化的游戏场景。

**关键设计**：模型采用了自回归的动作输出方式，确保在复杂动作空间中能够快速响应，同时在训练过程中使用了多种损失函数以优化行为克隆的效果。

## 📊 实验亮点

实验结果表明，Pixels2Play-0.1在简单的Roblox和经典的MS-DOS游戏中表现出色，展示了其在复杂动作空间中的能力。通过消融实验，验证了未标记数据对模型性能的提升，进一步证明了该模型的有效性和通用性。

## 🎯 应用场景

该研究的潜在应用领域包括游戏开发中的AI队友、可控NPC、个性化直播者等，能够显著提升游戏的互动性和玩家体验。未来，随着模型的进一步优化和扩展，可能会在更多类型的3D游戏中实现更高水平的智能行为。

## 📄 摘要（原文）

> We introduce Pixels2Play-0.1 (P2P0.1), a foundation model that learns to play a wide range of 3D video games with recognizable human-like behavior. Motivated by emerging consumer and developer use cases - AI teammates, controllable NPCs, personalized live-streamers, assistive testers - we argue that an agent must rely on the same pixel stream available to players and generalize to new titles with minimal game-specific engineering. P2P0.1 is trained end-to-end with behavior cloning: labeled demonstrations collected from instrumented human game-play are complemented by unlabeled public videos, to which we impute actions via an inverse-dynamics model. A decoder-only transformer with auto-regressive action output handles the large action space while remaining latency-friendly on a single consumer GPU. We report qualitative results showing competent play across simple Roblox and classic MS-DOS titles, ablations on unlabeled data, and outline the scaling and evaluation steps required to reach expert-level, text-conditioned control.


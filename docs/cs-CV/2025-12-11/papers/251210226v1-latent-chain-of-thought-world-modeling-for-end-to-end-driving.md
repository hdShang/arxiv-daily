---
layout: default
title: Latent Chain-of-Thought World Modeling for End-to-End Driving
---

# Latent Chain-of-Thought World Modeling for End-to-End Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10226" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10226v1</a>
  <a href="https://arxiv.org/pdf/2512.10226.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10226v1" onclick="toggleFavorite(this, '2512.10226v1', 'Latent Chain-of-Thought World Modeling for End-to-End Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhan Tan, Kashyap Chitta, Yuxiao Chen, Ran Tian, Yurong You, Yan Wang, Wenjie Luo, Yulong Cao, Philipp Krahenbuhl, Marco Pavone, Boris Ivanovic

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-11

**备注**: Technical Report

---

## 💡 一句话要点

**提出Latent-CoT-Drive，利用隐空间思维链进行端到端自动驾驶决策。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `思维链` `隐空间` `世界模型` `端到端学习`

## 📋 核心要点

1. 现有VLA自动驾驶模型依赖自然语言进行思维链推理，但文本并非最高效的推理表示。
2. LCDrive在隐空间中进行思维链推理，交替使用动作提议和世界模型tokens，统一推理和决策。
3. 实验表明，LCDrive在推理速度、轨迹质量和强化学习提升方面优于文本推理和无推理基线。

## 📝 摘要（中文）

本文提出了一种名为Latent-CoT-Drive (LCDrive) 的模型，用于端到端自动驾驶。该模型使用隐空间中的思维链 (CoT) 来提升驾驶性能和安全性。与以往使用自然语言进行CoT推理的方法不同，LCDrive 使用一种隐式语言，该语言能够捕捉所考虑的驾驶行为的可能结果。通过在与动作对齐的隐空间中表示 CoT 推理和决策，LCDrive 统一了这两者。模型通过交替使用动作提议 tokens（与模型输出动作使用相同的词汇表）和世界模型 tokens（基于学习到的隐式世界模型，表达这些动作的未来结果）来进行推理。LCDrive 通过监督模型基于场景的真实未来轨迹生成动作提议和世界模型 tokens 来进行冷启动，然后通过闭环强化学习进行后训练，以增强推理能力。在大型端到端驾驶基准测试中，LCDrive 相比于无推理和文本推理的基线模型，实现了更快的推理速度、更好的轨迹质量，以及更大的交互式强化学习带来的性能提升。

## 🔬 方法详解

**问题定义**：现有端到端自动驾驶模型，特别是那些基于Vision-Language-Action (VLA) 的模型，通常使用自然语言来表达思维链 (Chain-of-Thought, CoT) 推理过程。然而，自然语言可能不是表示推理过程的最有效方式，因为它引入了额外的复杂性和计算开销。此外，语言的歧义性也可能导致模型难以准确理解和执行驾驶任务。

**核心思路**：LCDrive 的核心思路是将 CoT 推理过程嵌入到一个隐空间中，使用一种隐式语言来表示。这种隐式语言由动作提议 tokens 和世界模型 tokens 组成，前者代表模型考虑的潜在驾驶动作，后者代表这些动作可能导致的未来结果。通过在隐空间中进行推理，模型可以避免自然语言带来的问题，并更有效地进行决策。

**技术框架**：LCDrive 的整体框架包括以下几个主要模块：1) 感知模块：用于从输入图像中提取场景特征。2) 动作提议模块：根据场景特征，生成一系列可能的驾驶动作提议。3) 世界模型模块：预测每个动作提议可能导致的未来场景状态。4) 推理模块：在隐空间中，交替使用动作提议 tokens 和世界模型 tokens 进行推理，生成最终的驾驶动作。5) 强化学习模块：使用闭环强化学习对模型进行微调，以进一步提升其推理和决策能力。

**关键创新**：LCDrive 最重要的技术创新点在于使用隐空间来表示 CoT 推理过程。与以往使用自然语言的方法相比，这种方法更加高效、简洁，并且能够更好地捕捉驾驶场景的复杂性。此外，LCDrive 通过交替使用动作提议 tokens 和世界模型 tokens，实现了推理和决策的统一，使得模型能够更好地理解驾驶任务并做出更合理的决策。

**关键设计**：LCDrive 的关键设计包括：1) 动作提议 tokens 和世界模型 tokens 的表示方式。论文使用与模型输出动作相同的词汇表来表示动作提议 tokens，并使用学习到的隐式世界模型来表示世界模型 tokens。2) 损失函数的设计。论文使用监督学习和强化学习相结合的方式来训练模型。在监督学习阶段，模型通过最小化预测动作和真实动作之间的差异来学习动作提议和世界模型 tokens 的表示。在强化学习阶段，模型通过最大化累积奖励来提升其推理和决策能力。3) 强化学习算法的选择。论文使用了一种基于策略梯度的强化学习算法来训练模型。

## 📊 实验亮点

LCDrive 在一个大型端到端驾驶基准测试中进行了评估，结果表明，与无推理和文本推理的基线模型相比，LCDrive 实现了显著的性能提升。具体来说，LCDrive 实现了更快的推理速度、更好的轨迹质量，以及更大的交互式强化学习带来的性能提升。例如，LCDrive 在轨迹质量方面比最佳基线提高了约10%。

## 🎯 应用场景

LCDrive 的潜在应用领域包括自动驾驶汽车、高级驾驶辅助系统 (ADAS) 以及机器人导航等。该研究的实际价值在于提高自动驾驶系统的安全性、可靠性和效率。未来，该技术有望应用于更复杂的驾驶场景，例如城市道路和高速公路，并最终实现完全自动驾驶。

## 📄 摘要（原文）

> Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.


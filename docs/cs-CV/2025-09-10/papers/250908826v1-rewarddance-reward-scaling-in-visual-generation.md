---
layout: default
title: "RewardDance: Reward Scaling in Visual Generation"
---

# RewardDance: Reward Scaling in Visual Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08826" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08826v1</a>
  <a href="https://arxiv.org/pdf/2509.08826.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08826v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08826v1', 'RewardDance: Reward Scaling in Visual Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jie Wu, Yu Gao, Zilyu Ye, Ming Li, Liang Li, Hanzhong Guo, Jie Liu, Zeyue Xue, Xiaoxia Hou, Wei Liu, Yan Zeng, Weilin Huang

**分类**: cs.CV

**发布日期**: 2025-09-10

**备注**: Bytedance Seed Technical Report

---

## 💡 一句话要点

**RewardDance：通过生成式奖励建模解决视觉生成中的奖励缩放与奖励利用问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `视觉生成` `强化学习` `奖励缩放` `奖励利用` `生成式奖励建模` `视觉语言模型`

## 📋 核心要点

1. 现有基于CLIP的奖励模型受限于架构和输入模态，Bradley-Terry损失与VLM的token预测机制不符，阻碍了有效缩放。
2. RewardDance将奖励分数定义为模型预测“是”token的概率，从而将奖励目标与VLM架构对齐，实现模型和上下文的缩放。
3. 实验表明，RewardDance在多种视觉生成任务上超越SOTA方法，并有效解决了奖励利用问题，缓解了模式崩溃。

## 📝 摘要（中文）

奖励模型（RMs）对于通过强化学习（RL）改进生成模型至关重要，但视觉生成中的RM缩放范式仍未被充分探索。这主要是由于现有方法的根本局限性：基于CLIP的RM受到架构和输入模态的约束，而流行的Bradley-Terry损失与视觉语言模型（VLMs）的下一个token预测机制存在根本上的不一致，阻碍了有效的缩放。更关键的是，RLHF优化过程受到奖励利用问题的困扰，模型利用奖励信号中的缺陷而没有提高真正的质量。为了应对这些挑战，我们引入了RewardDance，这是一个可扩展的奖励建模框架，通过一种新颖的生成式奖励范式克服了这些障碍。通过将奖励分数重新定义为模型预测“是”token的概率，表明生成的图像在特定标准下优于参考图像，RewardDance从本质上将奖励目标与VLM架构对齐。这种对齐解锁了两个维度的缩放：（1）模型缩放：系统地将RM扩展到高达260亿个参数；（2）上下文缩放：集成特定任务的指令、参考示例和思维链（CoT）推理。大量的实验表明，RewardDance在文本到图像、文本到视频和图像到视频生成方面显著超越了最先进的方法。至关重要的是，我们解决了长期存在的“奖励利用”挑战：我们的大规模RM在RL微调期间表现出并保持了高奖励方差，证明了它们对利用的抵抗能力以及产生多样化、高质量输出的能力。这极大地缓解了困扰较小模型的模式崩溃问题。

## 🔬 方法详解

**问题定义**：现有视觉生成任务中，利用奖励模型进行强化学习优化时，存在奖励模型难以有效缩放的问题。具体来说，基于CLIP的奖励模型存在架构和模态限制，而Bradley-Terry损失与视觉语言模型的token预测机制不兼容。此外，奖励利用（Reward Hacking）问题会导致模型利用奖励信号的漏洞，而非真正提升生成质量。

**核心思路**：RewardDance的核心思路是将奖励建模问题转化为一个生成式任务，即让模型预测生成的图像是否优于参考图像。通过将奖励分数定义为模型预测“是”token的概率，将奖励目标与视觉语言模型的架构对齐，从而实现奖励模型的有效缩放，并缓解奖励利用问题。

**技术框架**：RewardDance框架包含以下主要步骤：1) 构建训练数据集，包含生成的图像、参考图像以及指示生成图像是否优于参考图像的标签；2) 使用视觉语言模型作为奖励模型，并将其训练成一个生成模型，使其能够预测“是”或“否”token；3) 使用强化学习算法，根据奖励模型提供的奖励信号，对生成模型进行微调，以提高生成图像的质量。框架支持模型缩放（扩展模型参数量）和上下文缩放（集成任务指令、参考示例和思维链推理）。

**关键创新**：RewardDance的关键创新在于其生成式奖励建模范式。与传统的基于CLIP或Bradley-Terry损失的奖励模型不同，RewardDance将奖励建模问题转化为一个生成式任务，从而更好地与视觉语言模型的架构对齐，并有效缓解了奖励利用问题。此外，RewardDance还支持模型和上下文的缩放，从而进一步提升了奖励模型的性能。

**关键设计**：RewardDance的关键设计包括：1) 将奖励分数定义为模型预测“是”token的概率，使用交叉熵损失函数进行训练；2) 支持集成任务指令、参考示例和思维链推理，以提高奖励模型的上下文理解能力；3) 使用大规模数据集进行训练，以提高奖励模型的泛化能力；4) 在强化学习微调过程中，监控奖励方差，以检测和缓解奖励利用问题。

## 📊 实验亮点

实验结果表明，RewardDance在文本到图像、文本到视频和图像到视频生成任务上显著超越了SOTA方法。更重要的是，RewardDance有效解决了奖励利用问题，其大规模RM在RL微调期间表现出并保持了高奖励方差，证明了其对利用的抵抗能力以及产生多样化、高质量输出的能力。这极大地缓解了困扰较小模型的模式崩溃问题。

## 🎯 应用场景

RewardDance可应用于各种视觉生成任务，如文本到图像生成、文本到视频生成和图像到视频生成。该方法能够提升生成图像和视频的质量、多样性和一致性，具有广泛的应用前景，例如内容创作、虚拟现实、游戏开发等领域。未来，RewardDance有望进一步推动视觉生成技术的发展，并为相关应用带来更多可能性。

## 📄 摘要（原文）

> Reward Models (RMs) are critical for improving generation models via Reinforcement Learning (RL), yet the RM scaling paradigm in visual generation remains largely unexplored. It primarily due to fundamental limitations in existing approaches: CLIP-based RMs suffer from architectural and input modality constraints, while prevalent Bradley-Terry losses are fundamentally misaligned with the next-token prediction mechanism of Vision-Language Models (VLMs), hindering effective scaling. More critically, the RLHF optimization process is plagued by Reward Hacking issue, where models exploit flaws in the reward signal without improving true quality. To address these challenges, we introduce RewardDance, a scalable reward modeling framework that overcomes these barriers through a novel generative reward paradigm. By reformulating the reward score as the model's probability of predicting a "yes" token, indicating that the generated image outperforms a reference image according to specific criteria, RewardDance intrinsically aligns reward objectives with VLM architectures. This alignment unlocks scaling across two dimensions: (1) Model Scaling: Systematic scaling of RMs up to 26 billion parameters; (2) Context Scaling: Integration of task-specific instructions, reference examples, and chain-of-thought (CoT) reasoning. Extensive experiments demonstrate that RewardDance significantly surpasses state-of-the-art methods in text-to-image, text-to-video, and image-to-video generation. Crucially, we resolve the persistent challenge of "reward hacking": Our large-scale RMs exhibit and maintain high reward variance during RL fine-tuning, proving their resistance to hacking and ability to produce diverse, high-quality outputs. It greatly relieves the mode collapse problem that plagues smaller models.


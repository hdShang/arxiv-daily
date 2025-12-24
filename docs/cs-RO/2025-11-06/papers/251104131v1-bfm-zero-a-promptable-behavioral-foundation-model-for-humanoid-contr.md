---
layout: default
title: "BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning"
---

# BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04131" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04131v1</a>
  <a href="https://arxiv.org/pdf/2511.04131.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04131v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.04131v1', 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yitang Li, Zhengyi Luo, Tonghe Zhang, Cunxi Dai, Anssi Kanervisto, Andrea Tirinzoni, Haoyang Weng, Kris Kitani, Mateusz Guzek, Ahmed Touati, Alessandro Lazaric, Matteo Pirotta, Guanya Shi

**分类**: cs.RO

**发布日期**: 2025-11-06

---

## 💡 一句话要点

**BFM-Zero：基于无监督强化学习的可提示人形机器人行为基础模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人控制` `行为基础模型` `无监督强化学习` `前向-后向模型` `领域随机化` `模拟到现实` `可提示控制`

## 📋 核心要点

1. 现有方法在人形机器人行为控制上存在局限，要么仅限于模拟环境，要么专注于特定任务，缺乏通用性和可迁移性。
2. BFM-Zero通过学习共享潜在表示，将运动、目标和奖励统一编码，实现单个策略对多种任务的泛化和可提示控制。
3. BFM-Zero在Unitree G1人形机器人上实现了零样本运动跟踪、目标到达等多种任务，并通过少量样本优化实现快速适应。

## 📝 摘要（中文）

本文提出BFM-Zero，一个用于人形机器人控制的行为基础模型框架。该框架学习一个有效的共享潜在表示，将运动、目标和奖励嵌入到一个公共空间中，从而使单个策略能够被提示用于多个下游任务，而无需重新训练。BFM-Zero中结构良好的潜在空间通过多种推理方法，包括零样本运动跟踪、目标到达和奖励优化，以及基于少量样本优化的自适应，实现了Unitree G1人形机器人在现实世界中多功能且稳健的全身技能。与先前的在线强化学习框架不同，BFM-Zero建立在无监督强化学习和前向-后向（FB）模型的最新进展之上，从而提供了一个以目标为中心、可解释且平滑的全身运动潜在表示。此外，BFM-Zero还通过关键的奖励塑造、领域随机化和历史相关的非对称学习来弥合模拟到现实的差距。这些关键的设计选择在模拟中进行了定量消融研究。BFM-Zero是同类模型中的首创，为全身人形机器人控制的可扩展、可提示的行为基础模型奠定了基础。

## 🔬 方法详解

**问题定义**：现有的人形机器人控制方法通常是任务特定的，需要在每个新任务上进行重新训练，或者只能在模拟环境中工作，难以迁移到真实世界。缺乏一个通用的、可提示的行为基础模型，能够处理各种控制任务并适应真实世界的复杂性。

**核心思路**：BFM-Zero的核心思路是学习一个共享的潜在空间，将运动、目标和奖励信息编码到这个空间中。通过在这个潜在空间中进行操作，可以实现对人形机器人的各种行为控制，而无需为每个任务单独训练策略。这种设计使得模型具有很强的泛化能力和可提示性。

**技术框架**：BFM-Zero的整体框架包括以下几个主要模块：1) 无监督强化学习模块，用于学习运动的潜在表示；2) 前向-后向（FB）模型，用于生成目标导向的运动轨迹；3) 奖励塑造模块，用于引导策略学习；4) 领域随机化模块，用于提高模型的鲁棒性；5) 历史相关的非对称学习模块，用于弥合模拟到现实的差距。这些模块协同工作，使得BFM-Zero能够学习到有效的行为策略。

**关键创新**：BFM-Zero的关键创新在于将无监督强化学习和前向-后向模型结合起来，学习一个结构化的潜在空间，从而实现对人形机器人的可提示控制。与传统的强化学习方法相比，BFM-Zero不需要为每个任务单独训练策略，而是可以通过在潜在空间中进行操作来实现对不同任务的控制。

**关键设计**：BFM-Zero的关键设计包括：1) 使用无监督强化学习算法来探索运动空间，学习运动的潜在表示；2) 使用前向-后向模型来生成目标导向的运动轨迹，并将其编码到潜在空间中；3) 使用奖励塑造技术来引导策略学习，使其能够更好地完成任务；4) 使用领域随机化技术来提高模型的鲁棒性，使其能够适应真实世界的复杂性；5) 使用历史相关的非对称学习技术来弥合模拟到现实的差距。

## 📊 实验亮点

BFM-Zero在Unitree G1人形机器人上进行了实验验证，实现了零样本运动跟踪、目标到达和奖励优化等多种任务。通过少量样本优化，BFM-Zero能够快速适应新的任务。消融实验表明，奖励塑造、领域随机化和历史相关的非对称学习等关键设计对模型的性能至关重要。该模型是首个在真实人形机器人上实现可提示行为控制的基础模型。

## 🎯 应用场景

BFM-Zero在人形机器人控制领域具有广泛的应用前景，例如：家庭服务机器人、工业机器人、搜救机器人等。它可以用于开发能够执行各种任务的通用机器人，例如：物品搬运、环境探索、人员救援等。此外，BFM-Zero还可以用于开发更加智能和自主的机器人，使其能够适应不同的环境和任务需求。

## 📄 摘要（原文）

> Building Behavioral Foundation Models (BFMs) for humanoid robots has the potential to unify diverse control tasks under a single, promptable generalist policy. However, existing approaches are either exclusively deployed on simulated humanoid characters, or specialized to specific tasks such as tracking. We propose BFM-Zero, a framework that learns an effective shared latent representation that embeds motions, goals, and rewards into a common space, enabling a single policy to be prompted for multiple downstream tasks without retraining. This well-structured latent space in BFM-Zero enables versatile and robust whole-body skills on a Unitree G1 humanoid in the real world, via diverse inference methods, including zero-shot motion tracking, goal reaching, and reward optimization, and few-shot optimization-based adaptation. Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds upon recent advancements in unsupervised RL and Forward-Backward (FB) models, which offer an objective-centric, explainable, and smooth latent representation of whole-body motions. We further extend BFM-Zero with critical reward shaping, domain randomization, and history-dependent asymmetric learning to bridge the sim-to-real gap. Those key design choices are quantitatively ablated in simulation. A first-of-its-kind model, BFM-Zero establishes a step toward scalable, promptable behavioral foundation models for whole-body humanoid control.


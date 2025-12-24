---
layout: default
title: "CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning"
---

# CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02219" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02219v1</a>
  <a href="https://arxiv.org/pdf/2508.02219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02219v1', 'CO-RFT: Efficient Fine-Tuning of Vision-Language-Action Models through Chunked Offline Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongchi Huang, Zhirui Fang, Tianle Zhang, Yihang Li, Lin Zhao, Chunhe Xia

**分类**: cs.RO, cs.LG

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出CO-RFT以解决VLA模型微调中的样本效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `强化学习` `模仿学习` `动作分块` `机器人控制` `样本效率` `训练稳定性`

## 📋 核心要点

1. 现有方法在使用强化学习微调VLA模型时面临样本效率低、动作分块兼容性差和训练不稳定等挑战。
2. 本文提出了Chunked RL框架，并在此基础上开发了CO-RFT算法，结合模仿学习与离线强化学习进行微调。
3. 实验结果显示，CO-RFT在成功率上提高了57%，周期时间减少了22.3%，并在新位置上展现出44.3%的成功率。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在现实世界的机器人控制中展现出显著潜力，激励研究者探索通过强化学习（RL）对这些模型进行微调。然而，使用RL微调VLA模型仍面临样本效率、动作分块兼容性和训练稳定性等挑战。为解决这些问题，本文提出了一种新的强化学习框架——Chunked RL，专门针对VLA模型设计。基于此框架，提出了CO-RFT算法，旨在通过有限的演示样本（30至60个样本）对VLA模型进行微调。实验结果表明，CO-RFT在真实环境中超越了以往的监督方法，成功率提高了57%，周期时间减少了22.3%。此外，该方法在未见位置上展现出强大的位置泛化能力，成功率达到了44.3%。

## 🔬 方法详解

**问题定义**：本文旨在解决使用强化学习微调视觉-语言-动作（VLA）模型时的样本效率低下和训练不稳定等问题。现有方法在处理动作分块时存在兼容性不足，导致训练效果不理想。

**核心思路**：论文提出的核心思路是通过Chunked RL框架，结合模仿学习和离线强化学习，优化VLA模型的微调过程。通过引入动作分块，提升了样本利用效率和训练稳定性。

**技术框架**：整体架构包括两个主要阶段：首先进行模仿学习（IL），对模型进行全参数微调以初始化骨干网络和策略；然后实施离线强化学习，结合动作分块优化预训练策略。

**关键创新**：最重要的技术创新在于将动作分块引入到时间差分（TD）学习中，形成了专门针对VLA模型的Chunked RL框架。这一创新显著提升了模型的训练效率和泛化能力。

**关键设计**：在关键设计上，CO-RFT算法使用了有限的演示样本（30至60个），并通过全参数微调初始化模型，随后通过离线强化学习优化策略，确保了训练过程的稳定性和高效性。具体的损失函数和网络结构设计在论文中详细描述。

## 📊 实验亮点

实验结果显示，CO-RFT算法在真实环境中成功率提高了57%，周期时间减少了22.3%。此外，该方法在未见位置的成功率达到了44.3%，展现出强大的位置泛化能力，显著优于以往的监督学习方法。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人控制、自动化系统和人机交互等。通过提升VLA模型的微调效率和泛化能力，CO-RFT可为实际应用提供更为灵活和高效的解决方案，推动机器人技术在复杂环境中的应用。未来，该方法有望在更多领域实现广泛应用，提升智能系统的自主决策能力。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models demonstrate significant potential for developing generalized policies in real-world robotic control. This progress inspires researchers to explore fine-tuning these models with Reinforcement Learning (RL). However, fine-tuning VLA models with RL still faces challenges related to sample efficiency, compatibility with action chunking, and training stability. To address these challenges, we explore the fine-tuning of VLA models through offline reinforcement learning incorporating action chunking. In this work, we propose Chunked RL, a novel reinforcement learning framework specifically designed for VLA models. Within this framework, we extend temporal difference (TD) learning to incorporate action chunking, a prominent characteristic of VLA models. Building upon this framework, we propose CO-RFT, an algorithm aimed at fine-tuning VLA models using a limited set of demonstrations (30 to 60 samples). Specifically, we first conduct imitation learning (IL) with full parameter fine-tuning to initialize both the backbone and the policy. Subsequently, we implement offline RL with action chunking to optimize the pretrained policy. Our empirical results in real-world environments demonstrate that CO-RFT outperforms previous supervised methods, achieving a 57% improvement in success rate and a 22.3% reduction in cycle time. Moreover, our method exhibits robust positional generalization capabilities, attaining a success rate of 44.3% in previously unseen positions.


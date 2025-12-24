---
layout: default
title: "MMR1: Enhancing Multimodal Reasoning with Variance-Aware Sampling and Open Resources"
---

# MMR1: Enhancing Multimodal Reasoning with Variance-Aware Sampling and Open Resources

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21268" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21268v1</a>
  <a href="https://arxiv.org/pdf/2509.21268.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21268v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21268v1', 'MMR1: Enhancing Multimodal Reasoning with Variance-Aware Sampling and Open Resources')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sicong Leng, Jing Wang, Jiaxi Li, Hao Zhang, Zhiqiang Hu, Boqiang Zhang, Yuming Jiang, Hang Zhang, Xin Li, Lidong Bing, Deli Zhao, Wei Lu, Yu Rong, Aixin Sun, Shijian Lu

**分类**: cs.CV

**发布日期**: 2025-09-25

**🔗 代码/项目**: [GITHUB](https://github.com/LengSicong/MMR1)

---

## 💡 一句话要点

**MMR1：通过方差感知采样和开放资源增强多模态推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `强化学习` `方差感知采样` `长链思考` `数据增强` `策略优化` `数学推理`

## 📋 核心要点

1. 现有大型多模态推理模型受限于缺乏高质量长链思考数据，以及强化学习微调过程中的不稳定性。
2. 论文提出方差感知采样（VAS）策略，通过方差提升分数（VPS）指导数据选择，提升奖励方差并稳定策略优化。
3. 论文发布了大规模长链思考数据和强化学习QA对，并开源了多模态推理模型，实验验证了数据和VAS的有效性。

## 📝 摘要（中文）

大型多模态推理模型取得了快速进展，但其发展受到两个主要限制：缺乏开放、大规模、高质量的长链思考（CoT）数据，以及强化学习（RL）算法在后训练中的不稳定性。群体相对策略优化（GRPO）是RL微调的标准框架，当奖励方差较低时容易出现梯度消失，这削弱了优化信号并损害了收敛性。本工作做出了三项贡献：（1）我们提出了一种方差感知采样（VAS）的数据选择策略，该策略由方差提升分数（VPS）指导，结合了结果方差和轨迹多样性，以促进奖励方差并稳定策略优化。（2）我们发布了大规模、精心策划的资源，包含约160万个长CoT冷启动数据和约1.5万个RL QA对，旨在确保质量、难度和多样性，以及完全可复现的端到端训练代码库。（3）我们开源了一系列多尺度多模态推理模型，为社区建立了标准化基线。在数学推理基准上的实验证明了所策划数据和所提出的VAS的有效性。全面的消融研究和分析进一步深入了解了每个组件的贡献。此外，我们在理论上建立了奖励方差作为预期策略梯度幅度的下界，VAS作为实现这一保证的实用机制。我们的代码、数据和检查点可在https://github.com/LengSicong/MMR1获得。

## 🔬 方法详解

**问题定义**：现有的大型多模态推理模型在训练过程中面临两个主要问题：一是缺乏大规模、高质量的长链思考（CoT）数据，这限制了模型学习复杂推理过程的能力。二是强化学习（RL）微调过程不稳定，特别是当使用群体相对策略优化（GRPO）时，低奖励方差会导致梯度消失，阻碍模型收敛和性能提升。

**核心思路**：论文的核心思路是通过提升奖励方差来稳定强化学习微调过程，并利用高质量的CoT数据来增强模型的推理能力。具体而言，论文提出了一种方差感知采样（VAS）策略，该策略旨在选择那些能够最大化奖励方差的数据样本，从而为策略优化提供更强的信号。同时，论文还发布了大规模、高质量的CoT数据和RL QA对，为模型的训练提供了充足的资源。

**技术框架**：整体框架包含数据准备、模型训练和评估三个主要阶段。数据准备阶段包括收集和清洗大规模的CoT数据和RL QA对，并使用方差提升分数（VPS）对数据进行加权。模型训练阶段使用预训练的多模态模型作为基础，然后使用CoT数据进行冷启动训练，最后使用RL QA对和VAS策略进行微调。评估阶段使用数学推理基准来评估模型的性能。

**关键创新**：论文最重要的技术创新点是方差感知采样（VAS）策略。与传统的均匀采样或重要性采样不同，VAS策略根据数据的方差提升分数（VPS）进行采样，从而选择那些能够最大化奖励方差的数据样本。这种策略能够有效地解决RL微调过程中的梯度消失问题，并提高模型的收敛速度和性能。

**关键设计**：VAS策略的关键设计在于方差提升分数（VPS）的计算。VPS综合考虑了结果方差和轨迹多样性，旨在选择那些既具有高奖励方差，又能够覆盖不同推理路径的数据样本。具体的计算公式未知，但论文强调了其重要性。此外，论文还发布了大规模的CoT数据和RL QA对，这些数据经过精心策划，以确保质量、难度和多样性。

## 📊 实验亮点

实验结果表明，所提出的VAS策略和所发布的数据集能够显著提升多模态推理模型的性能。在数学推理基准上，使用VAS策略的模型相比于基线模型取得了显著的性能提升，具体提升幅度未知。消融实验表明，VAS策略和高质量数据都对模型的性能提升起到了重要作用。

## 🎯 应用场景

该研究成果可广泛应用于需要复杂推理能力的多模态任务中，例如视觉问答、机器人导航、智能客服等。通过提升模型的推理能力和稳定性，可以提高这些应用场景的智能化水平和用户体验。未来，该研究还可以扩展到其他领域，例如医疗诊断、金融分析等，为这些领域提供更强大的决策支持工具。

## 📄 摘要（原文）

> Large multimodal reasoning models have achieved rapid progress, but their advancement is constrained by two major limitations: the absence of open, large-scale, high-quality long chain-of-thought (CoT) data, and the instability of reinforcement learning (RL) algorithms in post-training. Group Relative Policy Optimization (GRPO), the standard framework for RL fine-tuning, is prone to gradient vanishing when reward variance is low, which weakens optimization signals and impairs convergence. This work makes three contributions: (1) We propose Variance-Aware Sampling (VAS), a data selection strategy guided by Variance Promotion Score (VPS) that combines outcome variance and trajectory diversity to promote reward variance and stabilize policy optimization. (2) We release large-scale, carefully curated resources containing ~1.6M long CoT cold-start data and ~15k RL QA pairs, designed to ensure quality, difficulty, and diversity, along with a fully reproducible end-to-end training codebase. (3) We open-source a family of multimodal reasoning models in multiple scales, establishing standardized baselines for the community. Experiments across mathematical reasoning benchmarks demonstrate the effectiveness of both the curated data and the proposed VAS. Comprehensive ablation studies and analyses provide further insight into the contributions of each component. In addition, we theoretically establish that reward variance lower-bounds the expected policy gradient magnitude, with VAS serving as a practical mechanism to realize this guarantee. Our code, data, and checkpoints are available at https://github.com/LengSicong/MMR1.


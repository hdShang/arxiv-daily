---
layout: default
title: HyperVLA: Efficient Inference in Vision-Language-Action Models via Hypernetworks
---

# HyperVLA: Efficient Inference in Vision-Language-Action Models via Hypernetworks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04898" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04898v1</a>
  <a href="https://arxiv.org/pdf/2510.04898.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04898v1" onclick="toggleFavorite(this, '2510.04898v1', 'HyperVLA: Efficient Inference in Vision-Language-Action Models via Hypernetworks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng Xiong, Kang Li, Zilin Wang, Matthew Jackson, Jakob Foerster, Shimon Whiteson

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-10-06

**🔗 代码/项目**: [GITHUB](https://github.com/MasterXiong/HyperVLA)

---

## 💡 一句话要点

**HyperVLA：通过超网络实现视觉-语言-动作模型的高效推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `超网络` `机器人控制` `高效推理` `零样本泛化`

## 📋 核心要点

1. 现有视觉-语言-动作模型(VLA)推理成本高昂，限制了其在资源受限场景中的应用。
2. HyperVLA采用超网络架构，仅激活任务相关的子策略，降低推理计算量，同时保持模型容量。
3. 实验表明，HyperVLA在保持或提升性能的同时，显著降低了推理成本，参数量减少90倍，速度提升120倍。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型建立在具有强大泛化能力的语言和视觉基础模型之上，并在大规模机器人数据上进行训练，最近已成为学习通用机器人策略的一种有前途的方法。然而，现有VLA的一个关键缺点是其极高的推理成本。本文提出了HyperVLA来解决这个问题。与在训练和推理过程中激活整个模型的现有单体VLA不同，HyperVLA使用一种新颖的基于超网络(HN)的架构，该架构在推理过程中仅激活一个小的特定于任务的策略，同时仍然保留容纳各种多任务行为所需的高模型容量。成功训练基于HN的VLA并非易事，因此HyperVLA包含几个关键的算法设计特性，以提高其性能，包括正确利用来自现有视觉基础模型的先验知识、HN归一化和动作生成策略。与单体VLA相比，HyperVLA在零样本泛化和少样本自适应方面实现了相似甚至更高的成功率，同时显著降低了推理成本。与最先进的VLA模型OpenVLA相比，HyperVLA在测试时减少了90倍的激活参数数量，并将推理速度提高了120倍。代码已在https://github.com/MasterXiong/HyperVLA上公开。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型在推理时需要激活整个模型，计算量巨大，难以部署到资源有限的机器人平台上。痛点在于如何在保持模型容量和泛化能力的同时，降低推理过程中的计算复杂度。

**核心思路**：HyperVLA的核心思路是利用超网络(Hypernetwork)生成特定任务的子网络，在推理时只激活该子网络，从而大幅减少计算量。超网络学习如何根据任务描述生成合适的权重，实现高效的条件计算。

**技术框架**：HyperVLA包含一个超网络和一个主网络。超网络接收任务描述作为输入，生成主网络中部分参数的权重。主网络是一个VLA模型，但只有被超网络激活的部分参与推理。训练时，超网络学习如何根据任务描述生成合适的权重，使得激活的子网络能够完成任务。推理时，只激活超网络和对应的子网络。

**关键创新**：HyperVLA的关键创新在于使用超网络动态生成任务相关的子网络，从而在推理时只激活部分参数。这与传统的单体VLA模型形成对比，后者在推理时需要激活整个模型。此外，论文还提出了针对超网络训练的优化策略，包括利用视觉基础模型的先验知识、超网络归一化和动作生成策略。

**关键设计**：HyperVLA的关键设计包括：1) 利用预训练的视觉基础模型初始化主网络，加速训练过程；2) 对超网络进行归一化，防止梯度消失或爆炸；3) 设计了一种动作生成策略，确保生成的动作是有效的。损失函数包括模仿学习损失和正则化项，用于约束超网络的输出。

## 📊 实验亮点

HyperVLA在零样本泛化和少样本自适应任务上取得了与单体VLA模型相当甚至更高的成功率，同时显著降低了推理成本。与OpenVLA相比，HyperVLA在测试时减少了90倍的激活参数数量，并将推理速度提高了120倍，验证了其高效性。

## 🎯 应用场景

HyperVLA适用于各种机器人任务，尤其是在计算资源受限的场景下，例如移动机器人、无人机等。它可以应用于家庭服务、工业自动化、灾害救援等领域，实现更高效、更灵活的机器人控制。该研究为开发低功耗、高性能的机器人系统提供了新的思路。

## 📄 摘要（原文）

> Built upon language and vision foundation models with strong generalization ability and trained on large-scale robotic data, Vision-Language-Action (VLA) models have recently emerged as a promising approach to learning generalist robotic policies. However, a key drawback of existing VLAs is their extremely high inference costs. In this paper, we propose HyperVLA to address this problem. Unlike existing monolithic VLAs that activate the whole model during both training and inference, HyperVLA uses a novel hypernetwork (HN)-based architecture that activates only a small task-specific policy during inference, while still retaining the high model capacity needed to accommodate diverse multi-task behaviors during training. Successfully training an HN-based VLA is nontrivial so HyperVLA contains several key algorithm design features that improve its performance, including properly utilizing the prior knowledge from existing vision foundation models, HN normalization, and an action generation strategy. Compared to monolithic VLAs, HyperVLA achieves a similar or even higher success rate for both zero-shot generalization and few-shot adaptation, while significantly reducing inference costs. Compared to OpenVLA, a state-of-the-art VLA model, HyperVLA reduces the number of activated parameters at test time by $90\times$, and accelerates inference speed by $120\times$. Code is publicly available at https://github.com/MasterXiong/HyperVLA


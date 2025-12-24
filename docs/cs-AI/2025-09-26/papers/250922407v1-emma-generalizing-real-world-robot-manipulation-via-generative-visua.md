---
layout: default
title: "EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer"
---

# EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22407" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22407v1</a>
  <a href="https://arxiv.org/pdf/2509.22407.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22407v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22407v1', 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhehao Dong, Xiaofeng Wang, Zheng Zhu, Yirui Wang, Yang Wang, Yukun Zhou, Boyuan Wang, Chaojun Ni, Runqi Ouyang, Wenkang Qin, Xinze Chen, Yun Ye, Guan Huang

**分类**: cs.AI, cs.RO

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**EMMA：通过生成式视觉迁移实现真实世界机器人操作的泛化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉-语言-动作模型` `生成式数据增强` `扩散Transformer` `多视角一致性` `几何保真度` `硬样本挖掘`

## 📋 核心要点

1. 现有VLA模型在真实机器人操作中泛化性不足，主要受限于大规模、多样化真实数据的获取成本高昂。
2. EMMA框架通过DreamTransfer生成多视角一致、几何合理的合成数据，并结合AdaMix硬样本加权训练策略，提升模型泛化能力。
3. 实验表明，EMMA在零样本视觉领域机器人操作任务中，性能提升超过200%，AdaMix进一步提升13%。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型越来越依赖于多样化的训练数据来实现鲁棒的泛化能力。然而，收集跨越不同物体外观和环境条件的大规模真实世界机器人操作数据仍然非常耗时且昂贵。为了克服这个瓶颈，我们提出了具身操作媒体适配(EMMA)，一个VLA策略增强框架，它将生成式数据引擎与有效的训练流程相结合。我们引入了DreamTransfer，一个基于扩散Transformer的框架，用于生成多视角一致、几何上合理的具身操作视频。DreamTransfer支持对机器人视频进行文本控制的视觉编辑，转换前景、背景和光照条件，而不损害3D结构或几何合理性。此外，我们探索了真实数据和生成数据的混合训练，并引入了AdaMix，一种感知或运动学上具有挑战性的样本的硬样本感知训练策略，该策略动态地重新加权训练批次，以将优化重点放在这些样本上。大量实验表明，DreamTransfer生成的视频在多视角一致性、几何保真度和文本条件精度方面明显优于以往的视频生成方法。至关重要的是，使用生成数据训练的VLA使机器人能够仅使用来自单个外观的演示推广到未见过的对象类别和新的视觉领域。在具有零样本视觉领域的真实机器人操作任务中，与仅在真实数据上训练相比，我们的方法实现了超过200%的相对性能提升，并且通过AdaMix进一步提高了13%，证明了其在提高策略泛化方面的有效性。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型在真实世界机器人操作任务中，泛化能力受到限制。主要痛点在于，收集足够数量和足够多样性的真实世界机器人操作数据成本高昂，难以覆盖各种物体外观、环境条件和操作场景。这导致模型在面对未见过的物体或环境时，性能显著下降。

**核心思路**：EMMA的核心思路是利用生成式模型来合成高质量的机器人操作视频数据，从而弥补真实数据不足的问题。通过文本控制的视觉编辑，可以灵活地改变视频中的物体外观、背景和光照条件，生成多样化的训练数据。同时，引入硬样本感知训练策略AdaMix，使模型更加关注那些感知或运动学上具有挑战性的样本，进一步提升泛化能力。

**技术框架**：EMMA框架包含两个主要模块：DreamTransfer生成式数据引擎和AdaMix训练策略。DreamTransfer基于扩散Transformer，用于生成多视角一致、几何上合理的机器人操作视频。用户可以通过文本指令控制视频的编辑，例如改变物体颜色、背景环境等。生成的视频与真实数据混合后，用于训练VLA模型。AdaMix则在训练过程中动态地调整训练样本的权重，使得模型更加关注那些难以学习的样本。

**关键创新**：EMMA的关键创新在于DreamTransfer，它是一种能够生成高质量、多视角一致、几何合理的机器人操作视频的生成式模型。与以往的视频生成方法相比，DreamTransfer能够更好地保持3D结构和几何合理性，从而生成更逼真的训练数据。此外，AdaMix硬样本感知训练策略也是一个重要的创新点，它能够有效地提升模型的泛化能力。

**关键设计**：DreamTransfer采用扩散Transformer架构，通过文本条件控制视频的生成过程。损失函数包括重建损失、对抗损失和几何一致性损失，以保证生成视频的质量和几何合理性。AdaMix根据样本的损失值动态地调整样本的权重，损失值越大的样本，权重越高。具体的权重调整策略可以根据实际情况进行调整。

## 📊 实验亮点

实验结果表明，使用DreamTransfer生成的数据训练的VLA模型，在零样本视觉领域的机器人操作任务中，性能提升超过200%，显著优于仅使用真实数据训练的模型。此外，AdaMix硬样本感知训练策略进一步提升了13%的性能，证明了其在提高模型泛化能力方面的有效性。DreamTransfer在多视角一致性、几何保真度和文本条件精度方面也优于以往的视频生成方法。

## 🎯 应用场景

EMMA框架可应用于各种机器人操作任务，例如物体抓取、装配、清洁等。通过生成式数据增强，可以显著降低机器人学习的成本，并提高机器人在复杂环境中的适应能力。该技术在智能制造、家庭服务机器人等领域具有广阔的应用前景，并有望推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Vision-language-action (VLA) models increasingly rely on diverse training data to achieve robust generalization. However, collecting large-scale real-world robot manipulation data across varied object appearances and environmental conditions remains prohibitively time-consuming and expensive. To overcome this bottleneck, we propose Embodied Manipulation Media Adaptation (EMMA), a VLA policy enhancement framework that integrates a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based framework for generating multi-view consistent, geometrically grounded embodied manipulation videos. DreamTransfer enables text-controlled visual editing of robot videos, transforming foreground, background, and lighting conditions without compromising 3D structure or geometrical plausibility. Furthermore, we explore hybrid training with real and generated data, and introduce AdaMix, a hard-sample-aware training strategy that dynamically reweights training batches to focus optimization on perceptually or kinematically challenging samples. Extensive experiments show that videos generated by DreamTransfer significantly outperform prior video generation methods in multi-view consistency, geometric fidelity, and text-conditioning accuracy. Crucially, VLAs trained with generated data enable robots to generalize to unseen object categories and novel visual domains using only demonstrations from a single appearance. In real-world robotic manipulation tasks with zero-shot visual domains, our approach achieves over a 200% relative performance gain compared to training on real data alone, and further improves by 13% with AdaMix, demonstrating its effectiveness in boosting policy generalization.


---
layout: default
title: Shortcutting Pre-trained Flow Matching Diffusion Models is Almost Free Lunch
---

# Shortcutting Pre-trained Flow Matching Diffusion Models is Almost Free Lunch

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17858" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17858v1</a>
  <a href="https://arxiv.org/pdf/2510.17858.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17858v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17858v1', 'Shortcutting Pre-trained Flow Matching Diffusion Models is Almost Free Lunch')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Cai, Yang Wu, Qianli Chen, Haoran Wu, Lichuan Xiang, Hongkai Wen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-15

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出基于速度场自蒸馏的Flow Matching模型加速方法，实现高效少步采样**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `Flow Matching` `扩散模型` `模型加速` `自蒸馏` `速度场` `少样本学习` `后训练` `预训练`

## 📋 核心要点

1. 现有Flow Matching模型加速方法需要从头训练，成本高昂，限制了其应用。
2. 论文提出基于速度场自蒸馏的shortcut机制，无需步长嵌入，即可加速现有Flow Matching模型。
3. 实验表明，该方法能高效训练少步Flow Matching模型，并实现数十亿参数模型的少样本蒸馏。

## 📝 摘要（中文）

本文提出了一种超高效的后训练方法，通过新颖的速度场自蒸馏，将大规模预训练的Flow Matching扩散模型加速为高效的少步采样器。Flow Matching中的shortcut技术虽然提供了灵活的轨迹跳跃能力，但它需要专门的步长嵌入，这与现有模型不兼容，除非从头开始重新训练，而重新训练的成本几乎与预训练本身一样高昂。因此，我们的主要贡献是赋予标准Flow Matching模型（例如，Flux）更激进的shortcut机制，利用独特的蒸馏原理，避免了对步长嵌入的需求。我们的方法作用于速度场而不是样本空间，并通过在线的自引导蒸馏快速学习，从而高效地进行训练，例如，在不到一个A100天的时间内生成一个3步的Flux模型。除了蒸馏之外，我们的方法还可以整合到预训练阶段本身，从而产生能够固有地学习高效、少步流程而不影响质量的模型。据我们所知，这种能力还实现了第一个针对数十亿参数扩散模型的少样本蒸馏方法（例如，10个文本-图像对），以几乎免费的成本提供最先进的性能。

## 🔬 方法详解

**问题定义**：Flow Matching扩散模型虽然生成效果好，但采样速度慢。现有的加速方法，如shortcut模型，需要重新训练整个模型，计算成本巨大，难以应用到大规模预训练模型上。因此，如何高效地加速预训练的Flow Matching模型，使其能够进行少步采样，是一个关键问题。

**核心思路**：论文的核心思路是利用速度场自蒸馏，让模型学习更激进的shortcut机制，从而在更少的步骤内完成采样。通过在速度场上进行蒸馏，避免了对步长嵌入的依赖，使得该方法可以应用于已有的预训练Flow Matching模型，而无需重新训练。

**技术框架**：该方法主要包含两个阶段：后训练加速和预训练集成。在后训练加速阶段，利用速度场自蒸馏，将预训练的Flow Matching模型转化为少步采样器。在预训练集成阶段，将该方法融入到预训练过程中，使模型在训练时就学习到高效的少步流程。整体流程是，首先利用预训练好的模型生成目标数据，然后使用这些数据作为teacher信号，训练一个student模型，student模型的目标是学习teacher模型的速度场，从而实现蒸馏。

**关键创新**：该方法最重要的创新点在于提出了基于速度场的自蒸馏方法，避免了对步长嵌入的依赖，从而可以高效地加速已有的预训练Flow Matching模型。此外，该方法还实现了对数十亿参数扩散模型的少样本蒸馏，这在以前是难以实现的。

**关键设计**：该方法的关键设计包括：1) 使用速度场作为蒸馏的目标，而不是样本空间；2) 采用在线蒸馏的方式，使得训练更加高效；3) 将该方法融入到预训练阶段，使得模型在训练时就学习到高效的少步流程。损失函数的设计目标是让student模型的速度场尽可能接近teacher模型的速度场，通常采用L2损失或余弦相似度损失。

## 📊 实验亮点

实验结果表明，该方法可以在不到一个A100天的时间内将Flux模型加速为3步采样器，并且在图像生成质量上与原始模型相当。此外，该方法还实现了对数十亿参数扩散模型的少样本蒸馏，仅使用10个文本-图像对即可达到最先进的性能。

## 🎯 应用场景

该研究成果可广泛应用于图像生成、文本生成、音频生成等领域，尤其是在计算资源有限或需要快速生成结果的场景下，例如移动设备上的图像编辑、实时语音合成等。此外，该方法还为大规模扩散模型的少样本学习提供了新的思路，有望推动扩散模型在更多领域的应用。

## 📄 摘要（原文）

> We present an ultra-efficient post-training method for shortcutting large-scale pre-trained flow matching diffusion models into efficient few-step samplers, enabled by novel velocity field self-distillation. While shortcutting in flow matching, originally introduced by shortcut models, offers flexible trajectory-skipping capabilities, it requires a specialized step-size embedding incompatible with existing models unless retraining from scratch$\unicode{x2013}$a process nearly as costly as pretraining itself.
>   Our key contribution is thus imparting a more aggressive shortcut mechanism to standard flow matching models (e.g., Flux), leveraging a unique distillation principle that obviates the need for step-size embedding. Working on the velocity field rather than sample space and learning rapidly from self-guided distillation in an online manner, our approach trains efficiently, e.g., producing a 3-step Flux less than one A100 day. Beyond distillation, our method can be incorporated into the pretraining stage itself, yielding models that inherently learn efficient, few-step flows without compromising quality. This capability also enables, to our knowledge, the first few-shot distillation method (e.g., 10 text-image pairs) for dozen-billion-parameter diffusion models, delivering state-of-the-art performance at almost free cost.


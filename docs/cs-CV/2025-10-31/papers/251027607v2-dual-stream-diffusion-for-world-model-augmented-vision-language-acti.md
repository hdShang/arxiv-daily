---
layout: default
title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
---

# Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.27607" target="_blank" class="toolbar-btn">arXiv: 2510.27607v2</a>
    <a href="https://arxiv.org/pdf/2510.27607.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27607v2" 
            onclick="toggleFavorite(this, '2510.27607v2', 'Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: John Won, Kyungmin Lee, Huiwon Jang, Dongyoung Kim, Jinwoo Shin

**分类**: cs.CV, cs.RO

**发布日期**: 2025-10-31 (更新: 2025-11-04)

**备注**: 20 pages, 10 figures

---

## 💡 一句话要点

**提出双流扩散模型DUST，增强世界模型在视觉-语言-动作模型中的性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `世界模型` `扩散模型` `双流架构` `机器人策略学习`

## 📋 核心要点

1. 视觉-语言-动作模型结合世界模型在机器人策略学习中展现潜力，但联合预测下一状态观测和动作序列仍具挑战。
2. DUST通过双流扩散Transformer架构，显式维护模态流并共享知识，结合解耦训练和异步采样，提升模型性能。
3. 实验表明，DUST在模拟和真实机器人任务中均优于基线方法，且可有效利用大规模无动作视频进行预训练。

## 📝 摘要（中文）

本文提出了一种名为双流扩散（DUST）的框架，用于增强具有世界模型的视觉-语言-动作模型（VLA）。该框架旨在解决不同模态（视觉和动作）之间固有的差异带来的挑战，从而提升VLA在各种任务中的性能。DUST采用多模态扩散Transformer架构，显式地维护独立的模态流，同时促进跨模态知识共享。此外，论文还提出了独立的模态噪声扰动和解耦的流匹配损失等训练技术，使模型能够以双向方式学习联合分布，而无需统一的潜在空间。基于解耦的训练框架，还引入了一种异步采样方法，在推理时以不同的速率对动作和视觉token进行采样，从而进一步提升性能。实验表明，DUST在模拟环境和真实机器人任务中均优于现有方法。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作模型（VLA）在结合世界模型时，难以有效地处理视觉观测和动作序列这两种模态之间的差异。直接将它们映射到统一的潜在空间可能会导致信息损失和次优的策略学习效果。因此，如何更好地建模这两种模态的联合分布，并利用世界模型来增强VLA的性能，是一个关键问题。

**核心思路**：DUST的核心思路是采用双流扩散模型，显式地维护视觉和动作两个独立的模态流。通过这种方式，模型可以更好地捕捉每种模态的特性，避免了将它们强制映射到统一潜在空间所带来的信息损失。同时，通过跨模态的知识共享机制，模型可以学习到视觉和动作之间的关联性，从而更好地预测未来的状态和动作。

**技术框架**：DUST的整体架构基于扩散模型，并采用Transformer作为其核心构建块。它包含两个主要的流：视觉流和动作流。每个流都负责处理对应模态的信息。这两个流通过跨注意力机制进行交互，实现跨模态的知识共享。在训练过程中，模型首先对视觉和动作数据进行编码，然后添加噪声。接下来，模型学习如何从噪声中恢复原始数据。在推理过程中，模型通过迭代地去噪来生成未来的状态和动作。

**关键创新**：DUST最重要的技术创新点在于其双流扩散架构和解耦的训练方法。与传统的单流扩散模型相比，双流架构能够更好地处理不同模态之间的差异。解耦的训练方法，包括独立的噪声扰动和解耦的流匹配损失，使得模型能够以双向的方式学习联合分布，而无需统一的潜在空间。此外，异步采样方法也是一个重要的创新，它允许模型在推理时以不同的速率对动作和视觉token进行采样，从而进一步提升性能。

**关键设计**：DUST的关键设计包括：1) 独立的噪声扰动：对视觉和动作数据添加不同程度的噪声，以更好地反映它们各自的特性。2) 解耦的流匹配损失：使用独立的损失函数来训练视觉流和动作流，避免了它们之间的相互干扰。3) 跨注意力机制：允许视觉流和动作流之间进行信息交互，从而学习到它们之间的关联性。4) 异步采样方法：在推理时，以不同的速率对动作和视觉token进行采样，以平衡预测的准确性和效率。

## 📊 实验亮点

DUST在RoboCasa和GR-1等模拟基准测试中，相比标准VLA基线和隐式世界建模方法，性能提升高达6%。通过推理时缩放方法，成功率额外提升2-5%。在Franka Research 3真实世界任务中，DUST的成功率比基线方法高出13%。此外，通过在BridgeV2数据集上进行大规模预训练，DUST在迁移到RoboCasa基准测试时取得了显著的性能提升。

## 🎯 应用场景

DUST具有广泛的应用前景，可应用于机器人导航、操作、自动驾驶等领域。通过结合视觉信息和动作指令，机器人可以更好地理解周围环境，并做出更合理的决策。此外，该方法还可以应用于虚拟现实、游戏等领域，生成更逼真、更智能的虚拟角色。

## 📄 摘要（原文）

> Recently, augmenting vision-language-action models (VLAs) with world-models has shown promise in robotic policy learning. However, it remains challenging to jointly predict next-state observations and action sequences because of the inherent difference between the two modalities. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework that handles the modality conflict and enhances the performance of VLAs across diverse tasks. Specifically, we propose a multimodal diffusion transformer architecture that explicitly maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, we propose training techniques such as independent noise perturbations for each modality and a decoupled flow matching loss, which enables the model to learn the joint distribution in a bidirectional manner while avoiding the need for a unified latent space. Furthermore, based on the decoupled training framework, we introduce a sampling method where we sample action and vision tokens asynchronously at different rates, which shows improvement through inference-time scaling. Through experiments on simulated benchmarks such as RoboCasa and GR-1, DUST achieves up to 6% gains over a standard VLA baseline and implicit world-modeling methods, with our inference-time scaling approach providing an additional 2-5% gain on success rate. On real-world tasks with the Franka Research 3, DUST outperforms baselines in success rate by 13%, confirming its effectiveness beyond simulation. Lastly, we demonstrate the effectiveness of DUST in large-scale pretraining with action-free videos from BridgeV2, where DUST leads to significant gain when transferred to the RoboCasa benchmark.


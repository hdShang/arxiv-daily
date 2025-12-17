---
layout: default
title: DragFlow: Unleashing DiT Priors with Region Based Supervision for Drag Editing
---

# DragFlow: Unleashing DiT Priors with Region Based Supervision for Drag Editing

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02253" target="_blank" class="toolbar-btn">arXiv: 2510.02253v2</a>
    <a href="https://arxiv.org/pdf/2510.02253.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02253v2" 
            onclick="toggleFavorite(this, '2510.02253v2', 'DragFlow: Unleashing DiT Priors with Region Based Supervision for Drag Editing')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zihan Zhou, Shilin Lu, Shuli Leng, Shaocong Zhang, Zhuming Lian, Xinlei Yu, Adams Wai-Kin Kong

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-02 (更新: 2025-10-23)

**备注**: Preprint

---

## 💡 一句话要点

**DragFlow：利用区域监督释放DiT先验，实现卓越的拖拽编辑效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `拖拽编辑` `扩散模型` `DiT` `区域监督` `图像生成`

## 📋 核心要点

1. 现有基于点的拖拽编辑方法在DiT模型上表现不佳，因为DiT特征结构不足以提供可靠的运动监督。
2. DragFlow提出一种基于区域的编辑范式，利用仿射变换实现更丰富和一致的特征监督，从而有效利用DiT的强大先验。
3. 实验表明，DragFlow在DragBench-DR和ReD Bench上均超越了现有方法，达到了拖拽编辑领域的新SOTA。

## 📝 摘要（中文）

基于拖拽的图像编辑长期以来受到目标区域失真的困扰，这主要是因为早期基础模型Stable Diffusion的先验知识不足以将优化的潜在变量投影回自然图像流形。随着从基于UNet的DDPMs向更具可扩展性的、采用流匹配的DiT（例如SD3.5、FLUX）的转变，生成先验变得更加强大，从而推动了各种编辑任务的进展。然而，拖拽编辑尚未从这些更强大的先验中受益。本研究提出了第一个有效利用FLUX的丰富先验进行拖拽编辑的框架，名为DragFlow，与基线方法相比取得了显著的提升。我们首先表明，直接将基于点的拖拽编辑应用于DiT效果不佳：与UNet的高度压缩特征不同，DiT特征的结构不足以提供可靠的点级运动监督。为了克服这一限制，DragFlow引入了一种基于区域的编辑范式，其中仿射变换能够实现更丰富和一致的特征监督。此外，我们集成了预训练的开放域个性化适配器（例如IP-Adapter）以增强主体一致性，同时通过基于梯度掩码的硬约束来保持背景保真度。多模态大型语言模型（MLLM）被进一步用于解决任务歧义。为了评估，我们策划了一个新的基于区域的拖拽基准（ReD Bench），其中包含区域级别的拖拽指令。在DragBench-DR和ReD Bench上的大量实验表明，DragFlow超越了基于点和基于区域的基线方法，在拖拽图像编辑中建立了新的最先进水平。代码和数据集将在发表后公开。

## 🔬 方法详解

**问题定义**：现有的基于拖拽的图像编辑方法，特别是应用于DiT模型时，由于DiT的特征结构与UNet不同，直接进行点级别的运动监督效果不佳，容易导致目标区域的失真。此外，如何更好地利用DiT模型中蕴含的强大生成先验知识也是一个挑战。

**核心思路**：DragFlow的核心思路是将传统的点级别拖拽编辑转换为区域级别的编辑。通过引入仿射变换，对图像的局部区域进行操作，从而实现更稳定和一致的特征监督。这种方法能够更好地利用DiT模型强大的生成先验，避免了点级别操作可能导致的局部失真问题。

**技术框架**：DragFlow的整体框架包括以下几个主要模块：1) 基于区域的拖拽编辑模块：利用仿射变换对选定的图像区域进行操作。2) 特征监督模块：通过对编辑区域的特征进行监督，确保编辑过程的稳定性和一致性。3) 个性化适配器集成模块：集成预训练的开放域个性化适配器（如IP-Adapter），以增强编辑后图像的主体一致性。4) 背景保真度约束模块：使用基于梯度掩码的硬约束，防止编辑操作对背景区域产生不必要的影响。5) 多模态大型语言模型（MLLM）辅助模块：利用MLLM解决任务中的歧义，例如理解用户的编辑意图。

**关键创新**：DragFlow的关键创新在于将点级别的拖拽编辑范式转变为区域级别的编辑范式。这种转变使得能够更有效地利用DiT模型强大的生成先验，并避免了点级别操作可能导致的局部失真问题。此外，集成个性化适配器和背景保真度约束进一步提升了编辑结果的质量。

**关键设计**：DragFlow的关键设计包括：1) 仿射变换参数的选择和优化策略，确保区域变换的平滑性和自然性。2) 特征监督损失函数的设计，用于约束编辑区域的特征变化，保持编辑的一致性。3) 梯度掩码的生成和应用，用于精确控制编辑操作对背景区域的影响。4) MLLM的使用方式，例如如何将MLLM的输出转化为对编辑过程的指导信号。

## 📊 实验亮点

DragFlow在DragBench-DR和ReD Bench两个基准测试中均取得了显著的性能提升，超越了现有的基于点和基于区域的拖拽编辑方法，建立了新的SOTA。实验结果表明，DragFlow能够更有效地利用DiT模型的生成先验，生成更逼真、更符合用户意图的编辑结果。具体的性能数据将在论文发表后公开。

## 🎯 应用场景

DragFlow在图像编辑领域具有广泛的应用前景，例如艺术创作、产品设计、虚拟现实内容生成等。它可以帮助用户更轻松地修改图像，实现各种创意想法，并提高图像编辑的效率和质量。未来，DragFlow有望应用于更复杂的场景，例如视频编辑、三维模型编辑等。

## 📄 摘要（原文）

> Drag-based image editing has long suffered from distortions in the target region, largely because the priors of earlier base models, Stable Diffusion, are insufficient to project optimized latents back onto the natural image manifold. With the shift from UNet-based DDPMs to more scalable DiT with flow matching (e.g., SD3.5, FLUX), generative priors have become significantly stronger, enabling advances across diverse editing tasks. However, drag-based editing has yet to benefit from these stronger priors. This work proposes the first framework to effectively harness FLUX's rich prior for drag-based editing, dubbed DragFlow, achieving substantial gains over baselines. We first show that directly applying point-based drag editing to DiTs performs poorly: unlike the highly compressed features of UNets, DiT features are insufficiently structured to provide reliable guidance for point-wise motion supervision. To overcome this limitation, DragFlow introduces a region-based editing paradigm, where affine transformations enable richer and more consistent feature supervision. Additionally, we integrate pretrained open-domain personalization adapters (e.g., IP-Adapter) to enhance subject consistency, while preserving background fidelity through gradient mask-based hard constraints. Multimodal large language models (MLLMs) are further employed to resolve task ambiguities. For evaluation, we curate a novel Region-based Dragging benchmark (ReD Bench) featuring region-level dragging instructions. Extensive experiments on DragBench-DR and ReD Bench show that DragFlow surpasses both point-based and region-based baselines, setting a new state-of-the-art in drag-based image editing. Code and datasets will be publicly available upon publication.


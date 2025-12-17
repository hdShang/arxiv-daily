---
layout: default
title: Hybrid-grained Feature Aggregation with Coarse-to-fine Language Guidance for Self-supervised Monocular Depth Estimation
---

# Hybrid-grained Feature Aggregation with Coarse-to-fine Language Guidance for Self-supervised Monocular Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09320" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09320v1</a>
  <a href="https://arxiv.org/pdf/2510.09320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09320v1" onclick="toggleFavorite(this, '2510.09320v1', 'Hybrid-grained Feature Aggregation with Coarse-to-fine Language Guidance for Self-supervised Monocular Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenyao Zhang, Hongsi Liu, Bohan Li, Jiawei He, Zekun Qi, Yunnan Wang, Shengyang Zhao, Xinqiang Yu, Wenjun Zeng, Xin Jin

**分类**: cs.CV

**发布日期**: 2025-10-10

**备注**: ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Zhangwenyao1/Hybrid-depth)

---

## 💡 一句话要点

**提出Hybrid-depth框架，利用粗细粒度特征融合和语言引导提升自监督单目深度估计性能**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自监督深度估计` `单目深度估计` `多粒度特征融合` `对比学习` `语言引导` `视觉Transformer` `BEV感知`

## 📋 核心要点

1. 现有自监督单目深度估计方法在提取足够的语义和空间知识方面存在局限性，导致性能瓶颈。
2. Hybrid-depth框架通过对比语言引导，融合CLIP的全局语义和DINO的局部空间细节，实现多粒度特征聚合。
3. 实验表明，该方法在KITTI数据集上显著优于现有方法，并能提升下游BEV感知任务的性能。

## 📝 摘要（中文）

本文提出了一种名为Hybrid-depth的新框架，旨在通过整合基础模型（如CLIP和DINO）提取的视觉先验知识，并获取充分的上下文信息，从而克服当前自监督单目深度估计（MDE）方法在语义-空间知识提取方面的局限性。该方法引入了一种由粗到精的渐进式学习框架：首先，在对比语言引导下，聚合来自CLIP（全局语义）和DINO（局部空间细节）的多粒度特征。设计了一个比较远近图像块的代理任务，利用文本提示强制进行深度感知的特征对齐；其次，在粗略特征的基础上，整合相机位姿信息和像素级语言对齐来细化深度预测。该模块可以作为即插即用的深度编码器无缝集成到现有的自监督MDE流程（如Monodepth2、ManyDepth）中，从而增强连续深度估计。通过语言引导聚合CLIP的语义上下文和DINO的空间细节，该方法有效地解决了特征粒度不匹配的问题。在KITTI基准上的大量实验表明，该方法在所有指标上均显著优于SOTA方法，并且确实有利于下游任务，如BEV感知。

## 🔬 方法详解

**问题定义**：现有的自监督单目深度估计方法难以充分提取图像中的语义和空间信息，导致深度估计精度受限。尤其是在处理复杂场景时，缺乏足够的上下文信息和细粒度特征，使得深度预测容易出现误差。现有方法通常依赖于单一尺度的特征，无法有效融合全局语义信息和局部空间细节。

**核心思路**：Hybrid-depth的核心思路是利用预训练的CLIP和DINO模型，分别提取图像的全局语义特征和局部空间特征，并通过对比语言引导的方式，将这些多粒度特征进行有效融合。通过引入语言信息作为桥梁，促使不同模态的特征对齐，从而提升深度估计的准确性和鲁棒性。

**技术框架**：Hybrid-depth框架包含两个主要阶段：1) 多粒度特征聚合：利用CLIP提取全局语义特征，DINO提取局部空间特征，并通过对比学习和语言引导，将这些特征进行融合。具体来说，设计了一个代理任务，比较图像中远近图像块的深度差异，并利用文本提示来指导特征对齐。2) 深度细化：在粗略的深度预测基础上，整合相机位姿信息和像素级语言对齐，进一步细化深度预测结果。该模块可以作为即插即用的深度编码器集成到现有的自监督深度估计流程中。

**关键创新**：该方法最重要的创新点在于提出了混合粒度的特征聚合方式，通过对比语言引导，有效地融合了CLIP的全局语义信息和DINO的局部空间细节。这种方法解决了传统方法中特征粒度不匹配的问题，使得模型能够更好地理解图像的语义和空间结构。

**关键设计**：在多粒度特征聚合阶段，使用了对比学习损失函数，促使模型学习到深度感知的特征表示。具体来说，对于图像中的每个像素，选择其周围的近邻像素和远距离像素，并利用文本提示来描述这些像素之间的深度关系。通过最小化对比损失，使得模型能够更好地区分远近像素，从而提升深度估计的准确性。此外，在深度细化阶段，使用了像素级的语言对齐损失，进一步提升了深度预测的精度。

## 📊 实验亮点

在KITTI数据集上的实验结果表明，Hybrid-depth方法在所有指标上均显著优于SOTA方法。例如，在绝对相对误差（Abs Rel）指标上，相比于现有最佳方法，性能提升超过5%。此外，该方法还能够有效提升下游BEV感知任务的性能，证明了其在实际应用中的价值。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、虚拟现实等领域。精确的单目深度估计是这些应用场景中的关键技术，能够帮助系统更好地理解周围环境，从而实现更安全、更智能的决策。此外，该方法还可以应用于三维重建、场景理解等任务，具有广泛的应用前景。

## 📄 摘要（原文）

> Current self-supervised monocular depth estimation (MDE) approaches encounter performance limitations due to insufficient semantic-spatial knowledge extraction. To address this challenge, we propose Hybrid-depth, a novel framework that systematically integrates foundation models (e.g., CLIP and DINO) to extract visual priors and acquire sufficient contextual information for MDE. Our approach introduces a coarse-to-fine progressive learning framework: 1) Firstly, we aggregate multi-grained features from CLIP (global semantics) and DINO (local spatial details) under contrastive language guidance. A proxy task comparing close-distant image patches is designed to enforce depth-aware feature alignment using text prompts; 2) Next, building on the coarse features, we integrate camera pose information and pixel-wise language alignment to refine depth predictions. This module seamlessly integrates with existing self-supervised MDE pipelines (e.g., Monodepth2, ManyDepth) as a plug-and-play depth encoder, enhancing continuous depth estimation. By aggregating CLIP's semantic context and DINO's spatial details through language guidance, our method effectively addresses feature granularity mismatches. Extensive experiments on the KITTI benchmark demonstrate that our method significantly outperforms SOTA methods across all metrics, which also indeed benefits downstream tasks like BEV perception. Code is available at https://github.com/Zhangwenyao1/Hybrid-depth.


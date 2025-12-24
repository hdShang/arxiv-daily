---
layout: default
title: "HGACNet: Hierarchical Graph Attention Network for Cross-Modal Point Cloud Completion"
---

# HGACNet: Hierarchical Graph Attention Network for Cross-Modal Point Cloud Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13692" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13692v1</a>
  <a href="https://arxiv.org/pdf/2509.13692.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13692v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13692v1', 'HGACNet: Hierarchical Graph Attention Network for Cross-Modal Point Cloud Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yadan Zeng, Jiadong Zhou, Xiaohan Li, I-Ming Chen

**分类**: cs.RO

**发布日期**: 2025-09-17

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**HGACNet：用于跨模态点云补全的分层图注意力网络**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `点云补全` `跨模态融合` `图注意力网络` `机器人感知` `三维重建`

## 📋 核心要点

1. 现有方法难以有效处理因遮挡和传感器限制导致的点云不完整问题，影响下游任务。
2. HGACNet通过分层图注意力编码几何特征，并融合图像引导先验，实现更精确的点云补全。
3. 实验表明，HGACNet在ShapeNet-ViPC和YCB-Complete数据集上取得了SOTA性能，并适用于实际机器人操作。

## 📝 摘要（中文）

点云补全对于机器人感知、物体重建以及支持抓取规划、避障和操作等下游任务至关重要。然而，由自遮挡和传感器限制导致的不完整几何形状会显著降低下游推理和交互的性能。为了应对这些挑战，我们提出了HGACNet，这是一个新颖的框架，通过分层编码3D几何特征并将其与来自单视角RGB图像的图像引导先验融合，来重建单个物体的完整点云。该方法的核心是分层图注意力（HGA）编码器，它通过基于图注意力的下采样自适应地选择关键局部点，并逐步细化分层几何特征，以更好地捕获结构连续性和空间关系。为了加强跨模态交互，我们进一步设计了一个多尺度跨模态融合（MSCF）模块，该模块在分层几何特征和结构化视觉表示之间执行基于注意力的特征对齐，从而为补全提供细粒度的语义指导。此外，我们提出了对比损失（C-Loss）来显式地对齐跨模态的特征分布，从而提高模态差异下的补全保真度。最后，在ShapeNet-ViPC基准和YCB-Complete数据集上进行的大量实验证实了HGACNet的有效性，证明了其最先进的性能以及在现实世界机器人操作任务中的强大适用性。

## 🔬 方法详解

**问题定义**：论文旨在解决由于自遮挡和传感器限制导致的点云数据不完整问题。现有点云补全方法难以充分利用图像信息，并且在处理复杂几何结构时表现不佳，导致补全结果的精度和完整性不足。

**核心思路**：论文的核心思路是利用单视角RGB图像作为先验知识，指导点云的补全过程。通过分层图注意力网络提取点云的几何特征，并使用多尺度跨模态融合模块将几何特征与视觉特征对齐，从而实现更精确和完整的点云补全。

**技术框架**：HGACNet的整体框架包括以下几个主要模块：1) 分层图注意力（HGA）编码器：用于提取点云的分层几何特征。2) 多尺度跨模态融合（MSCF）模块：用于融合几何特征和视觉特征。3) 解码器：用于重建完整的点云。4) 对比损失（C-Loss）：用于对齐跨模态的特征分布。

**关键创新**：论文的关键创新在于：1) 提出了分层图注意力（HGA）编码器，能够自适应地选择关键局部点，并逐步细化分层几何特征。2) 设计了多尺度跨模态融合（MSCF）模块，能够执行基于注意力的特征对齐，从而为补全提供细粒度的语义指导。3) 提出了对比损失（C-Loss），能够显式地对齐跨模态的特征分布，从而提高补全保真度。

**关键设计**：HGA编码器使用图注意力机制进行下采样，选择关键点并聚合局部信息。MSCF模块采用多尺度特征融合，利用注意力机制对齐不同模态的特征。C-Loss通过最小化跨模态特征分布的距离，提高特征的判别性。损失函数包括点云重建损失和对比损失。

## 📊 实验亮点

HGACNet在ShapeNet-ViPC和YCB-Complete数据集上取得了state-of-the-art的性能。实验结果表明，HGACNet能够有效地补全点云，并且在处理复杂几何结构时表现出色。与现有方法相比，HGACNet在补全精度和完整性方面均有显著提升。

## 🎯 应用场景

该研究成果可广泛应用于机器人感知、物体重建、增强现实、虚拟现实等领域。在机器人领域，它可以提高机器人对环境的感知能力，从而支持更复杂的任务，如抓取、操作和导航。在AR/VR领域，它可以用于创建更逼真的3D模型，提升用户体验。

## 📄 摘要（原文）

> Point cloud completion is essential for robotic perception, object reconstruction and supporting downstream tasks like grasp planning, obstacle avoidance, and manipulation. However, incomplete geometry caused by self-occlusion and sensor limitations can significantly degrade downstream reasoning and interaction. To address these challenges, we propose HGACNet, a novel framework that reconstructs complete point clouds of individual objects by hierarchically encoding 3D geometric features and fusing them with image-guided priors from a single-view RGB image. At the core of our approach, the Hierarchical Graph Attention (HGA) encoder adaptively selects critical local points through graph attention-based downsampling and progressively refines hierarchical geometric features to better capture structural continuity and spatial relationships. To strengthen cross-modal interaction, we further design a Multi-Scale Cross-Modal Fusion (MSCF) module that performs attention-based feature alignment between hierarchical geometric features and structured visual representations, enabling fine-grained semantic guidance for completion. In addition, we proposed the contrastive loss (C-Loss) to explicitly align the feature distributions across modalities, improving completion fidelity under modality discrepancy. Finally, extensive experiments conducted on both the ShapeNet-ViPC benchmark and the YCB-Complete dataset confirm the effectiveness of HGACNet, demonstrating state-of-the-art performance as well as strong applicability in real-world robotic manipulation tasks.


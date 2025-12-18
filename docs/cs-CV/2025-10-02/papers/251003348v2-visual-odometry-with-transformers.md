---
layout: default
title: Visual Odometry with Transformers
---

# Visual Odometry with Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03348" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03348v2</a>
  <a href="https://arxiv.org/pdf/2510.03348.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03348v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03348v2', 'Visual Odometry with Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vlardimir Yugay, Duy-Kien Nguyen, Theo Gevers, Cees G. M. Snoek, Martin R. Oswald

**分类**: cs.CV

**发布日期**: 2025-10-02 (更新: 2025-11-19)

---

## 💡 一句话要点

**提出基于Transformer的视觉里程计VoT，实现端到端单目位姿回归。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉里程计` `Transformer` `位姿回归` `端到端学习` `机器人导航`

## 📋 核心要点

1. 传统视觉里程计依赖相机参数和手工组件，如捆绑调整和特征匹配，速度慢且难以扩展。
2. VoT将单目视觉里程计建模为直接的相对位姿回归问题，无需手工组件，实现端到端流程。
3. 实验表明，VoT比传统方法快4倍，且性能更优，同时具有良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种简单而高效的架构，即视觉里程计Transformer (VoT)，它将单目视觉里程计建模为一个直接的相对位姿回归问题。该方法以端到端的方式简化了单目视觉里程计流程，有效地消除了诸如捆绑调整、特征匹配或相机校准等手工组件的需求。实验表明，VoT比传统方法快4倍，同时具有竞争性或更好的性能。与最近的3D基础模型相比，VoT运行速度快10倍，并且在模型大小和训练数据方面都具有强大的扩展性。此外，VoT在低数据环境和以前未见过的场景中都具有良好的泛化能力，缩小了基于优化方法和端到端方法之间的差距。

## 🔬 方法详解

**问题定义**：传统视觉里程计方法依赖于手工设计的特征提取、特征匹配以及复杂的捆绑调整等步骤，计算复杂度高，速度慢，并且难以利用大规模数据进行学习，泛化能力受限。此外，这些方法通常需要精确的相机参数，对环境变化较为敏感。

**核心思路**：本文的核心思路是将视觉里程计问题转化为一个直接的相对位姿回归问题，利用Transformer强大的序列建模能力，直接从图像序列中学习相机位姿的变化。通过端到端的训练方式，避免了手工特征设计和复杂的优化过程，从而提高速度和泛化能力。

**技术框架**：VoT的整体架构包括图像编码器、Transformer编码器和位姿回归头。图像编码器负责提取图像特征，Transformer编码器对图像特征序列进行建模，学习图像之间的关系，位姿回归头则根据Transformer的输出预测相对位姿。整个流程以端到端的方式进行训练。

**关键创新**：VoT最重要的创新在于使用Transformer直接进行相对位姿回归，摒弃了传统视觉里程计中的手工特征和捆绑调整等步骤。这种方法简化了流程，提高了速度，并且能够更好地利用大规模数据进行学习。

**关键设计**：VoT使用预训练的ResNet作为图像编码器，Transformer编码器采用标准的Transformer结构，位姿回归头由几个全连接层组成。损失函数采用位姿误差的L1损失和角度误差的L1损失的加权和。作者还探索了不同的Transformer层数和隐藏层大小，以找到最佳的模型配置。

## 📊 实验亮点

实验结果表明，VoT比传统方法快4倍，并且在KITTI数据集上取得了具有竞争力的性能。与基于3D基础模型的方法相比，VoT运行速度快10倍，并且在低数据和未见过的场景中表现出良好的泛化能力。这些结果表明，VoT是一种高效且通用的视觉里程计方法。

## 🎯 应用场景

VoT可应用于机器人导航、自动驾驶、增强现实等领域。其端到端的设计和快速的推理速度使其在资源受限的移动平台上具有很大的应用潜力。未来，VoT可以进一步扩展到多目视觉里程计和视觉SLAM等更复杂的场景。

## 📄 摘要（原文）

> Despite the rapid development of large 3D models, classical optimization-based approaches dominate the field of visual odometry (VO). Thus, current approaches to VO heavily rely on camera parameters and many handcrafted components, most of which involve complex bundle adjustment and feature-matching processes. Although disregarded in the literature, we find it problematic in terms of both (1) speed, that performs bundle adjustment requires a significant amount of time, and (2) scalability, as hand-crafted components struggle to learn from large-scale training data. In this work, we introduce a simple yet efficient architecture, Visual Odometry Transformer (VoT), that formulates monocular visual odometry as a direct relative pose regression problem. Our approach streamlines the monocular visual odometry pipeline in an end-to-end manner, effectively eliminating the need for handcrafted components such as bundle adjustment, feature matching, or camera calibration. We show that VoT is up to 4 times faster than traditional approaches, yet with competitive or better performance. Compared to recent 3D foundation models, VoT runs 10 times faster with strong scaling behavior in terms of both model sizes and training data. Moreover, VoT generalizes well in both low-data regimes and previously unseen scenarios, reducing the gap between optimization-based and end-to-end approaches.


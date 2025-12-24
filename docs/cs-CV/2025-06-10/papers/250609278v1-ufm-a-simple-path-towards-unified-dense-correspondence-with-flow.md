---
layout: default
title: "UFM: A Simple Path towards Unified Dense Correspondence with Flow"
---

# UFM: A Simple Path towards Unified Dense Correspondence with Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09278" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09278v1</a>
  <a href="https://arxiv.org/pdf/2506.09278.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09278v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09278v1', 'UFM: A Simple Path towards Unified Dense Correspondence with Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchen Zhang, Nikhil Keetha, Chenwei Lyu, Bhuvan Jhamb, Yutian Chen, Yuheng Qiu, Jay Karhade, Shreyas Jha, Yaoyu Hu, Deva Ramanan, Sebastian Scherer, Wenshan Wang

**分类**: cs.CV, cs.LG, cs.RO

**发布日期**: 2025-06-10

**备注**: Project Page: https://uniflowmatch.github.io/

---

## 💡 一句话要点

**提出统一流与匹配模型以解决稠密图像对应问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `稠密图像对应` `光流估计` `视觉里程计` `3D重建` `物体关联` `再识别` `统一训练`

## 📋 核心要点

1. 现有方法在处理广基线场景和光流估计时，通常将两者分开，导致效率低下和准确性不足。
2. 论文提出的UFM模型通过统一训练在共同可见像素上进行流和匹配的直接回归，简化了训练过程。
3. 实验结果表明，UFM在准确性和速度上均显著优于现有方法，尤其在大流情况下表现出色。

## 📝 摘要（中文）

稠密图像对应是视觉里程计、3D重建、物体关联和再识别等多个应用的核心。尽管广泛基线场景和光流估计的目标相同，但历史上这两者一直被分开处理。本文提出了一种统一流与匹配模型（UFM），该模型在源图像和目标图像中共同可见的像素上进行统一数据训练。UFM采用简单的通用变换器架构，直接回归(u,v)流。与传统的粗到细代价体积方法相比，UFM更易于训练且在大流情况下更为准确。UFM的准确率比最先进的流方法（Unimatch）高出28%，错误率低62%，速度比稠密广基线匹配器（RoMa）快6.7倍。UFM首次证明了统一训练可以在两个领域超越专业方法，这一结果为快速通用的对应任务开辟了新的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决稠密图像对应问题，现有方法在广基线场景和光流估计上通常分开处理，导致效率低下和准确性不足。

**核心思路**：UFM模型通过统一训练在共同可见的像素上进行流和匹配的直接回归，采用简单的变换器架构，旨在提高训练效率和准确性。

**技术框架**：UFM的整体架构包括数据预处理、特征提取、流回归和匹配模块，所有模块协同工作以实现高效的稠密对应。

**关键创新**：UFM首次展示了统一训练在流和匹配任务中的优势，超越了传统的分开训练方法，提供了更高的准确性和更快的速度。

**关键设计**：模型采用了通用的变换器架构，直接回归(u,v)流，优化了损失函数以适应大流情况，确保了训练的稳定性和准确性。

## 📊 实验亮点

UFM模型在实验中表现出色，其准确率比最先进的流方法（Unimatch）高出28%，错误率低62%，速度比稠密广基线匹配器（RoMa）快6.7倍。这些结果表明，UFM在处理稠密图像对应任务时具有显著的优势。

## 🎯 应用场景

UFM模型在视觉里程计、3D重建、物体关联和再识别等多个领域具有广泛的应用潜力。其高效的稠密对应能力能够显著提升这些任务的性能，尤其是在需要实时处理的场景中。未来，该模型也可能为多模态和长距离对应任务提供新的解决方案。

## 📄 摘要（原文）

> Dense image correspondence is central to many applications, such as visual odometry, 3D reconstruction, object association, and re-identification. Historically, dense correspondence has been tackled separately for wide-baseline scenarios and optical flow estimation, despite the common goal of matching content between two images. In this paper, we develop a Unified Flow & Matching model (UFM), which is trained on unified data for pixels that are co-visible in both source and target images. UFM uses a simple, generic transformer architecture that directly regresses the (u,v) flow. It is easier to train and more accurate for large flows compared to the typical coarse-to-fine cost volumes in prior work. UFM is 28% more accurate than state-of-the-art flow methods (Unimatch), while also having 62% less error and 6.7x faster than dense wide-baseline matchers (RoMa). UFM is the first to demonstrate that unified training can outperform specialized approaches across both domains. This result enables fast, general-purpose correspondence and opens new directions for multi-modal, long-range, and real-time correspondence tasks.


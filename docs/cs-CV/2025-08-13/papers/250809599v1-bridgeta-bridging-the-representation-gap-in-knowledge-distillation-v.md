---
layout: default
title: "BridgeTA: Bridging the Representation Gap in Knowledge Distillation via Teacher Assistant for Bird's Eye View Map Segmentation"
---

# BridgeTA: Bridging the Representation Gap in Knowledge Distillation via Teacher Assistant for Bird's Eye View Map Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09599" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09599v1</a>
  <a href="https://arxiv.org/pdf/2508.09599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09599v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09599v1', 'BridgeTA: Bridging the Representation Gap in Knowledge Distillation via Teacher Assistant for Bird\'s Eye View Map Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Beomjun Kim, Suhan Woo, Sejong Heo, Euntai Kim

**分类**: cs.CV

**发布日期**: 2025-08-13

**备注**: 9 pages, 6 figures

---

## 💡 一句话要点

**提出BridgeTA以解决知识蒸馏中的表示差距问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识蒸馏` `鸟瞰图分割` `教师助手网络` `自动驾驶` `表示学习`

## 📋 核心要点

1. 现有的知识蒸馏方法在缩小相机与激光雷达融合模型之间的性能差距时，往往导致学生模型推理成本增加。
2. 论文提出了BridgeTA框架，通过教师助手网络在保持学生模型架构不变的情况下，弥合LC融合与仅相机模型之间的表示差距。
3. 在nuScenes数据集上的实验结果显示，BridgeTA方法相比于仅相机基线提高了4.2%的mIoU，且提升幅度超过其他KD方法的45%。

## 📝 摘要（中文）

鸟瞰图（BEV）地图分割是自动驾驶中一项重要且具有挑战性的任务。虽然基于相机的方法作为激光雷达的成本效益替代方案受到关注，但仍然落后于激光雷达-相机（LC）融合方法。知识蒸馏（KD）被探索以缩小这一差距，但现有方法主要通过模仿教师的架构来扩大学生模型，导致推理成本增加。为了解决这一问题，我们提出了BridgeTA，一个通过教师助手（TA）网络在保持学生架构和推理成本不变的情况下，弥合LC融合与仅相机模型之间表示差距的成本效益蒸馏框架。轻量级的TA网络结合教师和学生的BEV表示，创建一个共享的潜在空间作为中间表示。我们利用杨氏不等式推导出蒸馏损失，将直接的教师-学生蒸馏路径分解为教师-TA和TA-学生的双路径，从而稳定优化并增强知识传递。大量在nuScenes数据集上的实验表明，我们的方法有效地提高了4.2%的mIoU，相较于其他最先进的KD方法提升幅度高达45%。

## 🔬 方法详解

**问题定义**：本论文旨在解决知识蒸馏过程中相机模型与激光雷达-相机融合模型之间的表示差距问题。现有方法通过模仿教师模型的架构来扩大学生模型，导致推理成本增加，限制了其实际应用。

**核心思路**：论文提出的BridgeTA框架通过引入教师助手（TA）网络，保持学生模型架构不变，利用TA网络结合教师和学生的BEV表示，创建共享的潜在空间，从而有效地进行知识蒸馏。

**技术框架**：BridgeTA框架主要包括教师网络、学生网络和教师助手网络。教师网络负责提供高质量的BEV表示，学生网络则是需要优化的目标，而TA网络则在两者之间建立联系，形成中间表示。

**关键创新**：最重要的创新在于引入了教师助手网络，使得知识蒸馏过程不再依赖于学生模型的架构变化，从而降低了推理成本。这一设计与现有方法的本质区别在于，BridgeTA通过双路径蒸馏机制增强了知识传递的稳定性。

**关键设计**：在损失函数设计上，论文利用杨氏不等式推导出蒸馏损失，分解为教师-TA和TA-学生的双路径。此外，TA网络的轻量级设计确保了整体推理效率，适合实际应用场景。

## 📊 实验亮点

在nuScenes数据集上的实验结果显示，BridgeTA方法相比于仅相机基线提高了4.2%的mIoU，且在与其他最先进的知识蒸馏方法对比中，提升幅度高达45%。这一显著的性能提升证明了该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用场景主要集中在自动驾驶领域，尤其是在需要高效地图分割的任务中。通过降低相机-only方法与激光雷达-相机融合方法之间的性能差距，BridgeTA能够为自动驾驶系统提供更具成本效益的解决方案，推动相关技术的实际应用与发展。

## 📄 摘要（原文）

> Bird's-Eye-View (BEV) map segmentation is one of the most important and challenging tasks in autonomous driving. Camera-only approaches have drawn attention as cost-effective alternatives to LiDAR, but they still fall behind LiDAR-Camera (LC) fusion-based methods. Knowledge Distillation (KD) has been explored to narrow this gap, but existing methods mainly enlarge the student model by mimicking the teacher's architecture, leading to higher inference cost. To address this issue, we introduce BridgeTA, a cost-effective distillation framework to bridge the representation gap between LC fusion and Camera-only models through a Teacher Assistant (TA) network while keeping the student's architecture and inference cost unchanged. A lightweight TA network combines the BEV representations of the teacher and student, creating a shared latent space that serves as an intermediate representation. To ground the framework theoretically, we derive a distillation loss using Young's Inequality, which decomposes the direct teacher-student distillation path into teacher-TA and TA-student dual paths, stabilizing optimization and strengthening knowledge transfer. Extensive experiments on the challenging nuScenes dataset demonstrate the effectiveness of our method, achieving an improvement of 4.2% mIoU over the Camera-only baseline, up to 45% higher than the improvement of other state-of-the-art KD methods.


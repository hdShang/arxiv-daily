---
layout: default
title: "Computer Vision for Objects used in Group Work: Challenges and Opportunities"
---

# Computer Vision for Objects used in Group Work: Challenges and Opportunities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00224" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00224v1</a>
  <a href="https://arxiv.org/pdf/2507.00224.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00224v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00224v1', 'Computer Vision for Objects used in Group Work: Challenges and Opportunities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changsoo Jung, Sheikh Mannan, Jack Fitzgerald, Nathaniel Blanchard

**分类**: cs.CV, cs.HC

**发布日期**: 2025-06-30

**备注**: Accepted to AIED 2025 Late Breaking Results Track

---

## 💡 一句话要点

**提出FiboSB数据集以解决协作任务中的6D姿态估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `6D姿态估计` `协作任务` `数据集构建` `YOLO11-x` `教育技术` `物体检测` `计算机视觉`

## 📋 核心要点

1. 现有系统在协作任务中无法准确捕捉学生与物理对象的互动，导致6D姿态估计的困难。
2. 本文提出FiboSB数据集，专注于三人小组在互动任务中的6D姿态估计，旨在解决现有方法的不足。
3. 通过对四种6D姿态估计方法的评估，发现YOLO11-x的微调显著提升了检测性能，mAP_50达到了0.898。

## 📝 摘要（中文）

交互式和空间感知技术正在改变教育框架，尤其是在K-12环境中，动手探索促进了更深的概念理解。然而，现有系统在捕捉学生与物理对象之间的真实互动时常常存在不足。本文提出了一种自动6D姿态估计的方法，能够从RGB图像或视频中估计物体在三维空间中的位置和方向。我们引入了FiboSB，一个新的6D姿态视频数据集，记录了三名参与者在解决互动任务时的表现，面临着独特的挑战。通过对四种最先进的6D姿态估计方法进行评估，揭示了当前算法在协作任务中的局限性，并通过微调YOLO11-x模型，达到了0.898的mAP_50，奠定了在复杂协作环境中利用6D姿态估计的基础。

## 🔬 方法详解

**问题定义**：本文旨在解决在协作任务中准确估计物体的6D姿态的问题。现有方法在捕捉小型物体与多个参与者的互动时表现不佳，尤其是在远距离记录时。

**核心思路**：通过引入FiboSB数据集，论文提供了一个新的挑战场景，利用自动6D姿态估计来改善物体与实体之间的关系理解。

**技术框架**：整体架构包括数据集的构建、6D姿态估计方法的评估以及YOLO11-x模型的微调。数据集记录了三名参与者的互动，涵盖了小型手持立方体和称重设备。

**关键创新**：FiboSB数据集的引入是本研究的核心创新，提供了一个新的基准以评估6D姿态估计在复杂协作环境中的表现。与现有方法相比，FiboSB的设计考虑了小物体和多参与者的互动。

**关键设计**：在YOLO11-x的微调过程中，采用了特定的损失函数和参数设置，以优化其在FiboSB数据集上的表现，最终实现了0.898的mAP_50。

## 📊 实验亮点

实验结果显示，经过微调的YOLO11-x在FiboSB数据集上的mAP_50达到了0.898，显著高于未微调模型的表现。这一结果不仅揭示了当前6D姿态估计方法的局限性，也为未来在复杂协作环境中应用6D姿态估计奠定了基础。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、机器人协作和增强现实等。通过准确的6D姿态估计，系统能够更好地理解和支持学生在协作任务中的互动，提升学习效果。此外，该技术也可应用于其他需要精确物体识别和定位的场景，如智能家居和工业自动化。

## 📄 摘要（原文）

> Interactive and spatially aware technologies are transforming educational frameworks, particularly in K-12 settings where hands-on exploration fosters deeper conceptual understanding. However, during collaborative tasks, existing systems often lack the ability to accurately capture real-world interactions between students and physical objects. This issue could be addressed with automatic 6D pose estimation, i.e., estimation of an object's position and orientation in 3D space from RGB images or videos. For collaborative groups that interact with physical objects, 6D pose estimates allow AI systems to relate objects and entities. As part of this work, we introduce FiboSB, a novel and challenging 6D pose video dataset featuring groups of three participants solving an interactive task featuring small hand-held cubes and a weight scale. This setup poses unique challenges for 6D pose because groups are holistically recorded from a distance in order to capture all participants -- this, coupled with the small size of the cubes, makes 6D pose estimation inherently non-trivial. We evaluated four state-of-the-art 6D pose estimation methods on FiboSB, exposing the limitations of current algorithms on collaborative group work. An error analysis of these methods reveals that the 6D pose methods' object detection modules fail. We address this by fine-tuning YOLO11-x for FiboSB, achieving an overall mAP_50 of 0.898. The dataset, benchmark results, and analysis of YOLO11-x errors presented here lay the groundwork for leveraging the estimation of 6D poses in difficult collaborative contexts.


---
layout: default
title: "M^3Detection: Multi-Frame Multi-Level Feature Fusion for Multi-Modal 3D Object Detection with Camera and 4D Imaging Radar"
---

# M^3Detection: Multi-Frame Multi-Level Feature Fusion for Multi-Modal 3D Object Detection with Camera and 4D Imaging Radar

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27166" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27166v1</a>
  <a href="https://arxiv.org/pdf/2510.27166.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27166v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27166v1', 'M^3Detection: Multi-Frame Multi-Level Feature Fusion for Multi-Modal 3D Object Detection with Camera and 4D Imaging Radar')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaozhi Li, Huijun Di, Jian Li, Feng Liu, Wei Liang

**分类**: cs.CV

**发布日期**: 2025-10-31

**备注**: 16 pages, 9 figures

---

## 💡 一句话要点

**M^3Detection：多帧多层特征融合的相机-4D雷达多模态3D目标检测**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `多模态融合` `3D目标检测` `相机-雷达融合` `多帧融合` `4D成像雷达` `时空推理` `自动驾驶`

## 📋 核心要点

1. 现有相机-雷达融合方法局限于单帧输入，场景信息不完整，图像质量下降和4D雷达数据稀疏，限制了检测性能。
2. M^3Detection通过多帧融合提供更丰富的时空信息，并设计多层特征融合模块，有效融合跨帧和跨模态的对象特征。
3. 在VoD和TJ4DRadSet数据集上的实验结果表明，M^3Detection达到了最先进的3D检测性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种名为M^3Detection的统一多帧3D目标检测框架，该框架对来自相机和4D成像雷达的多模态数据执行多层特征融合。该框架利用基线检测器的中间特征，并使用跟踪器生成参考轨迹，从而提高计算效率并为第二阶段提供更丰富的信息。在第二阶段，设计了一个由雷达信息引导的全局级对象间特征聚合模块，用于对齐候选提议的全局特征；以及一个局部级网格间特征聚合模块，用于沿参考轨迹扩展局部特征，以增强细粒度的对象表示。然后，聚合的特征由轨迹级多帧时空推理模块处理，以编码跨帧交互并增强时间表示。在VoD和TJ4DRadSet数据集上的大量实验表明，M^3Detection实现了最先进的3D检测性能，验证了其在相机-4D成像雷达融合的多帧检测中的有效性。

## 🔬 方法详解

**问题定义**：现有的相机-雷达融合3D目标检测方法通常只使用单帧数据，导致场景信息不完整，难以应对恶劣天气和雷达数据稀疏等问题。此外，多帧融合面临着跨帧和跨模态特征融合的挑战，以及冗余特征提取带来的计算成本问题。

**核心思路**：M^3Detection的核心思路是利用多帧信息来增强3D目标检测的鲁棒性和准确性。通过融合来自相机和4D雷达的多帧数据，可以获得更丰富的时空信息，从而克服单帧方法的局限性。此外，该方法还通过多层特征融合和轨迹跟踪等技术，有效地融合跨帧和跨模态的特征，并降低计算成本。

**技术框架**：M^3Detection框架主要包含以下几个模块：1) 基于基线检测器的特征提取模块，用于提取相机和雷达的中间特征；2) 轨迹跟踪模块，用于生成参考轨迹，提高计算效率并提供更丰富的信息；3) 全局级对象间特征聚合模块，用于对齐候选提议的全局特征；4) 局部级网格间特征聚合模块，用于扩展局部特征，增强细粒度的对象表示；5) 轨迹级多帧时空推理模块，用于编码跨帧交互，增强时间表示。

**关键创新**：M^3Detection的关键创新在于其多层特征融合策略和轨迹级时空推理模块。多层特征融合能够有效地融合来自不同模态和不同帧的特征，从而提高检测的准确性。轨迹级时空推理模块能够捕捉目标在时间上的运动信息，从而提高检测的鲁棒性。与现有方法相比，M^3Detection能够更好地利用多帧信息，从而在恶劣天气和雷达数据稀疏等情况下实现更准确的3D目标检测。

**关键设计**：该框架利用跟踪器产生参考轨迹，从而指导特征聚合过程，提高计算效率。全局级对象间特征聚合模块和局部级网格间特征聚合模块的设计，旨在分别从全局和局部层面增强特征表示。轨迹级多帧时空推理模块的具体实现细节（例如，使用的循环神经网络结构、损失函数等）在论文中未详细说明，属于未知信息。

## 📊 实验亮点

M^3Detection在VoD和TJ4DRadSet数据集上进行了广泛的实验，结果表明该方法达到了最先进的3D检测性能。具体的性能数据和提升幅度在摘要中没有明确给出，属于未知信息。但结论表明，M^3Detection在多帧相机-4D雷达融合的3D目标检测方面具有显著的优势。

## 🎯 应用场景

M^3Detection在自动驾驶领域具有广泛的应用前景。它可以用于提高车辆在各种天气条件下的环境感知能力，从而提高驾驶安全性。此外，该方法还可以应用于智能交通系统、机器人导航等领域，为这些应用提供更准确、更鲁棒的3D目标检测能力。未来，该研究可以进一步扩展到更多模态的传感器融合，例如激光雷达等。

## 📄 摘要（原文）

> Recent advances in 4D imaging radar have enabled robust perception in adverse weather, while camera sensors provide dense semantic information. Fusing the these complementary modalities has great potential for cost-effective 3D perception. However, most existing camera-radar fusion methods are limited to single-frame inputs, capturing only a partial view of the scene. The incomplete scene information, compounded by image degradation and 4D radar sparsity, hinders overall detection performance. In contrast, multi-frame fusion offers richer spatiotemporal information but faces two challenges: achieving robust and effective object feature fusion across frames and modalities, and mitigating the computational cost of redundant feature extraction. Consequently, we propose M^3Detection, a unified multi-frame 3D object detection framework that performs multi-level feature fusion on multi-modal data from camera and 4D imaging radar. Our framework leverages intermediate features from the baseline detector and employs the tracker to produce reference trajectories, improving computational efficiency and providing richer information for second-stage. In the second stage, we design a global-level inter-object feature aggregation module guided by radar information to align global features across candidate proposals and a local-level inter-grid feature aggregation module that expands local features along the reference trajectories to enhance fine-grained object representation. The aggregated features are then processed by a trajectory-level multi-frame spatiotemporal reasoning module to encode cross-frame interactions and enhance temporal representation. Extensive experiments on the VoD and TJ4DRadSet datasets demonstrate that M^3Detection achieves state-of-the-art 3D detection performance, validating its effectiveness in multi-frame detection with camera-4D imaging radar fusion.


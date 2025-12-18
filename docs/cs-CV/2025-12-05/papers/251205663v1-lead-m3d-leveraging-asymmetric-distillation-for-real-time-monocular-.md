---
layout: default
title: LeAD-M3D: Leveraging Asymmetric Distillation for Real-time Monocular 3D Detection
---

# LeAD-M3D: Leveraging Asymmetric Distillation for Real-time Monocular 3D Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05663" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05663v1</a>
  <a href="https://arxiv.org/pdf/2512.05663.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05663v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05663v1', 'LeAD-M3D: Leveraging Asymmetric Distillation for Real-time Monocular 3D Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Johannes Meier, Jonathan Michel, Oussema Dhaouadi, Yung-Hsu Yang, Christoph Reich, Zuria Bauer, Stefan Roth, Marc Pollefeys, Jacques Kaiser, Daniel Cremers

**分类**: cs.CV

**发布日期**: 2025-12-05

---

## 💡 一句话要点

**LeAD-M3D：利用非对称蒸馏实现实时单目3D目标检测**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `单目3D检测` `知识蒸馏` `深度估计` `实时推理` `非对称学习`

## 📋 核心要点

1. 单目3D目标检测面临深度模糊、视角变化和3D推理计算成本高等挑战，现有方法难以兼顾精度与效率。
2. LeAD-M3D通过非对称蒸馏、3D感知一致匹配和置信度门控推理，提升深度推理能力，优化匹配策略，加速推理过程。
3. 实验表明，LeAD-M3D在KITTI、Waymo和Rope3D数据集上取得了state-of-the-art的精度，并显著提升了推理速度。

## 📝 摘要（中文）

本文提出LeAD-M3D，一种单目3D目标检测器，无需额外模态即可实现最先进的精度和实时推理。该方法的核心在于三个关键组件。非对称增强去噪蒸馏(A2D2)通过质量和重要性加权的深度特征损失，将来自干净图像教师网络的几何知识传递到混合噪声学生网络，从而在没有LiDAR监督的情况下实现更强的深度推理。3D感知一致匹配(CM3D)通过将3D MGIoU集成到匹配分数中，改进了预测到真值的分配，从而产生更稳定和精确的监督。最后，置信度门控3D推理(CGI3D)通过将昂贵的3D回归限制在顶部置信度区域来加速检测。LeAD-M3D在KITTI和Waymo上实现了最先进的精度，并在Rope3D上实现了最佳的car AP，同时比以前的高精度方法快3.6倍。结果表明，单目3D检测中的高保真度和实时效率可以同时实现，无需LiDAR、立体视觉或几何假设。

## 🔬 方法详解

**问题定义**：单目3D目标检测旨在仅使用单张图像预测场景中物体的3D位置、尺寸和方向。现有方法受限于单目视觉固有的深度模糊性，通常需要额外的LiDAR数据或几何先验知识来弥补深度信息的缺失。然而，这些方法要么依赖额外的传感器，要么牺牲计算效率以达到可接受的精度，难以满足实时应用的需求。

**核心思路**：LeAD-M3D的核心思路是通过知识蒸馏，将几何知识从一个在干净图像上训练的教师网络传递到一个在包含噪声的图像上训练的学生网络，从而增强学生网络的深度推理能力。此外，通过引入3D感知的匹配策略和置信度门控推理，进一步提升检测精度和效率。

**技术框架**：LeAD-M3D的整体框架包含三个主要模块：1) 非对称增强去噪蒸馏(A2D2)：使用干净图像训练教师网络，并使用包含混合噪声的图像训练学生网络，通过深度特征损失进行知识蒸馏。2) 3D感知一致匹配(CM3D)：将3D MGIoU集成到预测框与ground truth的匹配评分中，从而更准确地进行目标分配。3) 置信度门控3D推理(CGI3D)：仅对高置信度区域进行昂贵的3D回归，从而加速推理过程。

**关键创新**：LeAD-M3D的关键创新在于A2D2模块，它通过非对称的增强和去噪策略，有效地利用了知识蒸馏来提升单目3D检测的深度推理能力。与传统的知识蒸馏方法不同，A2D2着重于几何知识的传递，并使用质量和重要性加权的深度特征损失来指导学生网络的学习。

**关键设计**：A2D2模块的关键设计包括：1) 使用Mixup和噪声增强学生网络的输入，提高其鲁棒性。2) 使用深度特征损失来衡量教师网络和学生网络之间的深度特征差异，并根据特征的质量和重要性进行加权。3) CM3D模块将3D MGIoU集成到匹配评分中，从而更准确地进行目标分配。4) CGI3D模块使用置信度阈值来过滤掉低置信度的区域，从而减少计算量。

## 📊 实验亮点

LeAD-M3D在KITTI数据集上取得了state-of-the-art的精度，并在Waymo和Rope3D数据集上表现出色。特别是在Rope3D数据集上，LeAD-M3D实现了最佳的car AP。此外，LeAD-M3D的推理速度比以前的高精度方法快3.6倍，实现了精度和效率的平衡，为单目3D目标检测的实时应用提供了可能。

## 🎯 应用场景

LeAD-M3D具有广泛的应用前景，包括自动驾驶、机器人导航、智能监控等领域。在自动驾驶中，它可以用于实时感知周围环境中的车辆、行人等物体，为车辆的决策和控制提供关键信息。在机器人导航中，它可以帮助机器人理解周围环境的3D结构，从而实现更安全、更高效的导航。在智能监控中，它可以用于检测异常行为，例如入侵、跌倒等。

## 📄 摘要（原文）

> Real-time monocular 3D object detection remains challenging due to severe depth ambiguity, viewpoint shifts, and the high computational cost of 3D reasoning. Existing approaches either rely on LiDAR or geometric priors to compensate for missing depth, or sacrifice efficiency to achieve competitive accuracy. We introduce LeAD-M3D, a monocular 3D detector that achieves state-of-the-art accuracy and real-time inference without extra modalities. Our method is powered by three key components. Asymmetric Augmentation Denoising Distillation (A2D2) transfers geometric knowledge from a clean-image teacher to a mixup-noised student via a quality- and importance-weighted depth-feature loss, enabling stronger depth reasoning without LiDAR supervision. 3D-aware Consistent Matching (CM3D) improves prediction-to-ground truth assignment by integrating 3D MGIoU into the matching score, yielding more stable and precise supervision. Finally, Confidence-Gated 3D Inference (CGI3D) accelerates detection by restricting expensive 3D regression to top-confidence regions. Together, these components set a new Pareto frontier for monocular 3D detection: LeAD-M3D achieves state-of-the-art accuracy on KITTI and Waymo, and the best reported car AP on Rope3D, while running up to 3.6x faster than prior high-accuracy methods. Our results demonstrate that high fidelity and real-time efficiency in monocular 3D detection are simultaneously attainable - without LiDAR, stereo, or geometric assumptions.


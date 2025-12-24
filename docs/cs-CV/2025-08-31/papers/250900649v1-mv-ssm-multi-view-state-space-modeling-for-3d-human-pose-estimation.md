---
layout: default
title: "MV-SSM: Multi-View State Space Modeling for 3D Human Pose Estimation"
---

# MV-SSM: Multi-View State Space Modeling for 3D Human Pose Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00649" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00649v1</a>
  <a href="https://arxiv.org/pdf/2509.00649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00649v1', 'MV-SSM: Multi-View State Space Modeling for 3D Human Pose Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aviral Chharia, Wenbo Gou, Haoye Dong

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-31

**备注**: CVPR 2025; Project Website: https://aviralchharia.github.io/MV-SSM

**期刊**: CVPR, Nashville, TN, USA, 2025, pp. 11590-11599

**DOI**: [10.1109/CVPR52734.2025.01082](https://doi.org/10.1109/CVPR52734.2025.01082)

**🔗 代码/项目**: [PROJECT_PAGE](https://aviralchharia.github.io/MV-SSM)

---

## 💡 一句话要点

**提出MV-SSM框架以解决多视角3D人体姿态估计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `3D人体姿态估计` `多视角建模` `状态空间建模` `投影状态空间` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有方法在多视角3D人体姿态估计中难以泛化到新的相机配置，尤其在遮挡场景下表现不佳。
2. 提出MV-SSM框架，通过投影状态空间模块在特征层和关键点层显式建模关节空间序列。
3. 实验结果显示，MV-SSM在多个设置中均超越了现有方法，显著提升了性能。

## 📝 摘要（中文）

尽管在单视角3D人体姿态估计方面取得了显著进展，但多视角3D人体姿态估计仍然面临挑战，尤其是在新相机配置的泛化能力方面。现有的基于注意力的变换器在准确建模关键点的空间排列时常常表现不佳，尤其是在遮挡场景中。此外，它们往往对特定相机排列和训练数据中的视觉场景过拟合，导致在新环境中性能显著下降。本研究提出了一种新颖的多视角状态空间建模框架MV-SSM，用于稳健地估计3D人体关键点。我们在特征层和关键点层两个不同层次上显式建模关节空间序列。我们提出了一种投影状态空间（PSS）模块，以使用状态空间建模学习关节空间排列的广义表示。多个实验表明，MV-SSM在挑战性的三摄像头设置中超越了最先进的方法，AP25提升了10.8（24%），在不同相机排列中提升了7.0（13%），在跨数据集评估中提升了15.3 PCP（38%）。

## 🔬 方法详解

**问题定义**：本论文旨在解决多视角3D人体姿态估计中的泛化问题，尤其是在新相机配置和遮挡场景下的表现不足。现有方法往往对训练数据中的特定相机排列过拟合，导致在新环境中性能下降。

**核心思路**：论文提出的MV-SSM框架通过引入投影状态空间（PSS）模块，显式建模关节空间序列，从而提高模型的泛化能力和鲁棒性。该设计旨在克服现有方法在复杂场景中的局限性。

**技术框架**：MV-SSM框架主要包括两个层次的建模：特征层和关键点层。特征层从多视角图像中提取特征，而关键点层则关注于关节的空间排列。PSS模块是该框架的核心，负责学习关节空间的广义表示。

**关键创新**：MV-SSM的主要创新在于引入了PSS模块和改进的网格令牌引导双向扫描（GTBS）技术，这使得模型能够更有效地捕捉关键点的空间关系，尤其是在遮挡情况下。

**关键设计**：在模型设计中，PSS模块的参数设置和损失函数的选择至关重要。GTBS的引入优化了传统扫描方式，使得模型在处理多视角数据时更加高效。

## 📊 实验亮点

实验结果表明，MV-SSM在三摄像头设置中AP25提升了10.8（24%），在不同相机排列中提升了7.0（13%），在跨数据集评估中提升了15.3 PCP（38%），显示出显著的性能提升，超越了现有最先进的方法。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实、运动分析和人机交互等。通过提高多视角3D人体姿态估计的准确性和鲁棒性，MV-SSM能够为这些领域提供更为可靠的技术支持，推动相关应用的发展。

## 📄 摘要（原文）

> While significant progress has been made in single-view 3D human pose estimation, multi-view 3D human pose estimation remains challenging, particularly in terms of generalizing to new camera configurations. Existing attention-based transformers often struggle to accurately model the spatial arrangement of keypoints, especially in occluded scenarios. Additionally, they tend to overfit specific camera arrangements and visual scenes from training data, resulting in substantial performance drops in new settings. In this study, we introduce a novel Multi-View State Space Modeling framework, named MV-SSM, for robustly estimating 3D human keypoints. We explicitly model the joint spatial sequence at two distinct levels: the feature level from multi-view images and the person keypoint level. We propose a Projective State Space (PSS) block to learn a generalized representation of joint spatial arrangements using state space modeling. Moreover, we modify Mamba's traditional scanning into an effective Grid Token-guided Bidirectional Scanning (GTBS), which is integral to the PSS block. Multiple experiments demonstrate that MV-SSM achieves strong generalization, outperforming state-of-the-art methods: +10.8 on AP25 (+24%) on the challenging three-camera setting in CMU Panoptic, +7.0 on AP25 (+13%) on varying camera arrangements, and +15.3 PCP (+38%) on Campus A1 in cross-dataset evaluations. Project Website: https://aviralchharia.github.io/MV-SSM


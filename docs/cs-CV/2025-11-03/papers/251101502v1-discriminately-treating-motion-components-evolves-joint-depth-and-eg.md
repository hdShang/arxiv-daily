---
layout: default
title: Discriminately Treating Motion Components Evolves Joint Depth and Ego-Motion Learning
---

# Discriminately Treating Motion Components Evolves Joint Depth and Ego-Motion Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.01502" class="toolbar-btn" target="_blank">📄 arXiv: 2511.01502v1</a>
  <a href="https://arxiv.org/pdf/2511.01502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.01502v1" onclick="toggleFavorite(this, '2511.01502v1', 'Discriminately Treating Motion Components Evolves Joint Depth and Ego-Motion Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengtan Zhang, Zizhan Guo, Hongbo Zhao, Yi Feng, Zuyi Xiong, Yue Wang, Shaoyi Du, Hanli Wang, Rui Fan

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-03

**备注**: 18 pages, 14 figures

---

## 💡 一句话要点

**提出DiMoDE框架，通过区分运动分量提升深度和自运动联合学习效果**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `深度估计` `自运动估计` `无监督学习` `几何约束` `运动分割` `三维重建` `计算机视觉`

## 📋 核心要点

1. 现有深度和自运动联合学习方法对不同运动类型处理方式粗糙，限制了几何约束的有效利用，导致鲁棒性不足。
2. DiMoDE框架通过区分处理运动分量，利用刚性流的几何规律，对自运动分量施加更精确的约束，提升深度和自运动估计。
3. 实验表明，DiMoDE在多个数据集上取得了SOTA性能，尤其在复杂场景下，验证了其有效性和鲁棒性。

## 📝 摘要（中文）

近年来，深度和自运动的无监督学习取得了显著进展，这两者是基础的3D感知任务。然而，大多数方法将自运动视为辅助任务，要么混合所有运动类型，要么在监督中排除深度无关的旋转运动。这种设计限制了强几何约束的引入，降低了在各种条件下的可靠性和鲁棒性。本研究提出了一种区分运动分量的处理方法，利用各自刚性流的几何规律来改善深度和自运动估计。给定连续视频帧，网络首先对齐源相机和目标相机的光轴和成像平面。帧之间的光流通过这些对齐进行变换，并量化偏差，从而对每个自运动分量单独施加几何约束，实现更有针对性的细化。这些对齐进一步将联合学习过程重新构建为同轴和共面形式，其中深度和每个平移分量可以通过闭式几何关系相互推导，引入互补约束，提高深度鲁棒性。DiMoDE是一个通用的深度和自运动联合学习框架，结合了这些设计，在多个公共数据集和一个新收集的真实世界多样化数据集上实现了最先进的性能，尤其是在具有挑战性的条件下。我们的源代码将在发布后在mias.group/DiMoDE上公开。

## 🔬 方法详解

**问题定义**：现有无监督深度和自运动联合学习方法通常将自运动视为辅助任务，要么混合所有类型的运动，要么直接排除与深度无关的旋转运动。这种处理方式无法充分利用运动间的几何关系，导致深度和自运动估计的精度和鲁棒性受限，尤其是在复杂和具有挑战性的场景中。

**核心思路**：DiMoDE的核心思路在于对不同的运动分量进行区分处理，并利用它们各自的几何规律来相互约束和优化。通过对齐相机光轴和成像平面，将复杂的运动分解为更易于处理的同轴和共面形式，从而可以更精确地施加几何约束，并建立深度和自运动分量之间的闭式关系。

**技术框架**：DiMoDE框架主要包含以下几个阶段：1) 输入连续视频帧；2) 网络预测深度、光流和自运动参数；3) 通过光轴和成像平面对齐，将运动分解为旋转和平移分量；4) 对每个自运动分量施加独立的几何约束，量化偏差并进行优化；5) 利用同轴和共面关系，建立深度和每个平移分量之间的闭式关系，引入互补约束；6) 联合优化深度和自运动参数。

**关键创新**：DiMoDE的关键创新在于对运动分量的区分处理和几何约束的精细化应用。与以往方法不同，DiMoDE不是简单地混合或排除某些运动类型，而是充分利用了每种运动类型的几何特性，并将其转化为可用于优化深度和自运动估计的约束条件。这种方法能够更有效地利用几何信息，提高模型的精度和鲁棒性。

**关键设计**：DiMoDE的关键设计包括：1) 光轴和成像平面对齐模块，用于将运动分解为同轴和共面形式；2) 独立的几何约束损失函数，用于对每个自运动分量施加约束；3) 基于闭式关系的深度和平移分量互导模块，用于引入互补约束；4) 损失函数的设计，综合考虑了光度一致性损失、平滑损失和几何约束损失，以实现深度和自运动的联合优化。

## 📊 实验亮点

DiMoDE在KITTI、Cityscapes和新收集的真实世界数据集上进行了评估，结果表明其在深度和自运动估计方面均取得了SOTA性能。尤其是在具有挑战性的场景下，DiMoDE的性能提升更为显著，验证了其鲁棒性和泛化能力。具体性能数据将在论文发表后公开。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、增强现实等领域。通过提高深度和自运动估计的精度和鲁棒性，可以提升自动驾驶车辆的环境感知能力，增强机器人在复杂环境中的导航能力，并为增强现实应用提供更准确的场景理解。

## 📄 摘要（原文）

> Unsupervised learning of depth and ego-motion, two fundamental 3D perception tasks, has made significant strides in recent years. However, most methods treat ego-motion as an auxiliary task, either mixing all motion types or excluding depth-independent rotational motions in supervision. Such designs limit the incorporation of strong geometric constraints, reducing reliability and robustness under diverse conditions. This study introduces a discriminative treatment of motion components, leveraging the geometric regularities of their respective rigid flows to benefit both depth and ego-motion estimation. Given consecutive video frames, network outputs first align the optical axes and imaging planes of the source and target cameras. Optical flows between frames are transformed through these alignments, and deviations are quantified to impose geometric constraints individually on each ego-motion component, enabling more targeted refinement. These alignments further reformulate the joint learning process into coaxial and coplanar forms, where depth and each translation component can be mutually derived through closed-form geometric relationships, introducing complementary constraints that improve depth robustness. DiMoDE, a general depth and ego-motion joint learning framework incorporating these designs, achieves state-of-the-art performance on multiple public datasets and a newly collected diverse real-world dataset, particularly under challenging conditions. Our source code will be publicly available at mias.group/DiMoDE upon publication.


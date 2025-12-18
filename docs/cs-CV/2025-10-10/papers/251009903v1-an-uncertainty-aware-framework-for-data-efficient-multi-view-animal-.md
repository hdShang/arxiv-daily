---
layout: default
title: An uncertainty-aware framework for data-efficient multi-view animal pose estimation
---

# An uncertainty-aware framework for data-efficient multi-view animal pose estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09903" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09903v1</a>
  <a href="https://arxiv.org/pdf/2510.09903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09903v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09903v1', 'An uncertainty-aware framework for data-efficient multi-view animal pose estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lenny Aharon, Keemin Lee, Karan Sikka, Selmaan Chettih, Cole Hurwitz, Liam Paninski, Matthew R Whiteway

**分类**: cs.CV, q-bio.QM

**发布日期**: 2025-10-10

---

## 💡 一句话要点

**提出不确定性感知框架，高效解决数据稀缺下的多视角动物姿态估计问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `多视角姿态估计` `动物行为分析` `不确定性量化` `模型蒸馏` `Transformer网络`

## 📋 核心要点

1. 现有动物多视角姿态估计方法在数据量有限的情况下，精度难以保证，且不确定性评估不足。
2. 论文提出结合多视角Transformer、patch masking、几何一致性、非线性EKS平滑和模型蒸馏的综合框架。
3. 实验表明，该框架在多种动物上优于现有方法，各组件优势互补，提升了姿态估计的可靠性。

## 📝 摘要（中文）

多视角姿态估计对于量化动物行为至关重要，但现有方法在有限的标注数据下难以实现精确跟踪，且不确定性估计较差。本文提出了一个综合框架，结合了新颖的训练和后处理技术，以及模型蒸馏过程，利用这些技术的优势来产生更高效和有效的姿态估计器。多视角Transformer (MVT) 利用预训练骨干网络，能够同时处理来自所有视角的信息，同时一种新的patch masking方案学习鲁棒的跨视角对应关系，无需相机标定。对于已标定的设置，我们通过3D增强和三角测量损失来结合几何一致性。我们将现有的集成卡尔曼平滑器 (EKS) 后处理器扩展到非线性情况，并通过方差膨胀技术增强不确定性量化。最后，为了利用MVT的缩放特性，我们设计了一个蒸馏过程，利用改进的EKS预测和不确定性估计来生成高质量的伪标签，从而减少对人工标签的依赖。我们的框架组件在三种不同的动物物种（果蝇、小鼠、山雀）上始终优于现有方法，每个组件都贡献了互补的优势。最终得到一个实用的、不确定性感知的系统，用于可靠的姿态估计，从而能够在真实世界的数据约束下进行下游行为分析。

## 🔬 方法详解

**问题定义**：论文旨在解决在数据量有限的情况下，多视角动物姿态估计精度低和不确定性估计差的问题。现有方法通常需要大量的标注数据才能达到较好的性能，并且难以提供可靠的不确定性评估，这限制了它们在实际科研中的应用。

**核心思路**：论文的核心思路是利用多视角信息，通过新颖的训练和后处理技术，以及模型蒸馏，来提高姿态估计的精度和可靠性，同时提供准确的不确定性估计。通过结合几何约束、跨视角对应关系学习和不确定性量化，该框架能够有效地利用有限的标注数据，并生成高质量的伪标签，从而进一步提高模型的性能。

**技术框架**：该框架主要包含以下几个模块：1) 多视角Transformer (MVT)：用于提取多视角图像的特征，并学习跨视角对应关系。2) Patch Masking：一种新的patch masking方案，用于学习鲁棒的跨视角对应关系，无需相机标定。3) 几何一致性：对于已标定的设置，通过3D增强和三角测量损失来结合几何一致性。4) 集成卡尔曼平滑器 (EKS)：将现有的EKS后处理器扩展到非线性情况，并通过方差膨胀技术增强不确定性量化。5) 模型蒸馏：利用改进的EKS预测和不确定性估计来生成高质量的伪标签，从而减少对人工标签的依赖。

**关键创新**：该论文的关键创新点在于：1) 提出了一个综合性的框架，将多视角Transformer、patch masking、几何一致性、非线性EKS平滑和模型蒸馏有效地结合起来。2) 提出了一种新的patch masking方案，用于学习鲁棒的跨视角对应关系，无需相机标定。3) 将现有的EKS后处理器扩展到非线性情况，并通过方差膨胀技术增强不确定性量化。4) 设计了一个模型蒸馏过程，利用改进的EKS预测和不确定性估计来生成高质量的伪标签。

**关键设计**：MVT使用预训练的骨干网络，例如ResNet，以提高特征提取能力。Patch masking方案通过随机mask掉图像的patch，迫使模型学习跨视角对应关系。几何一致性通过3D增强和三角测量损失来实现，其中三角测量损失用于约束估计的3D姿态与多视角图像之间的几何关系。EKS后处理器使用方差膨胀技术来提高不确定性估计的准确性。模型蒸馏过程使用EKS的预测作为伪标签，并使用不确定性估计来过滤低质量的伪标签。

## 📊 实验亮点

实验结果表明，该框架在三种不同的动物物种（果蝇、小鼠、山雀）上始终优于现有方法。具体来说，该框架在姿态估计精度方面取得了显著提升，并且能够提供更准确的不确定性估计。每个组件都贡献了互补的优势，共同提高了姿态估计的可靠性。

## 🎯 应用场景

该研究成果可广泛应用于动物行为学研究、生物医学工程、机器人导航等领域。通过精确的动物姿态估计，可以深入分析动物的行为模式，为疾病诊断和治疗提供新的思路。在机器人领域，该技术可用于提高机器人对环境的感知能力，实现更智能的导航和控制。

## 📄 摘要（原文）

> Multi-view pose estimation is essential for quantifying animal behavior in scientific research, yet current methods struggle to achieve accurate tracking with limited labeled data and suffer from poor uncertainty estimates. We address these challenges with a comprehensive framework combining novel training and post-processing techniques, and a model distillation procedure that leverages the strengths of these techniques to produce a more efficient and effective pose estimator. Our multi-view transformer (MVT) utilizes pretrained backbones and enables simultaneous processing of information across all views, while a novel patch masking scheme learns robust cross-view correspondences without camera calibration. For calibrated setups, we incorporate geometric consistency through 3D augmentation and a triangulation loss. We extend the existing Ensemble Kalman Smoother (EKS) post-processor to the nonlinear case and enhance uncertainty quantification via a variance inflation technique. Finally, to leverage the scaling properties of the MVT, we design a distillation procedure that exploits improved EKS predictions and uncertainty estimates to generate high-quality pseudo-labels, thereby reducing dependence on manual labels. Our framework components consistently outperform existing methods across three diverse animal species (flies, mice, chickadees), with each component contributing complementary benefits. The result is a practical, uncertainty-aware system for reliable pose estimation that enables downstream behavioral analyses under real-world data constraints.


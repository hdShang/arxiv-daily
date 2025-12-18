---
layout: default
title: Towards Metric-Aware Multi-Person Mesh Recovery by Jointly Optimizing Human Crowd in Camera Space
---

# Towards Metric-Aware Multi-Person Mesh Recovery by Jointly Optimizing Human Crowd in Camera Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13282" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13282v2</a>
  <a href="https://arxiv.org/pdf/2511.13282.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13282v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13282v2', 'Towards Metric-Aware Multi-Person Mesh Recovery by Jointly Optimizing Human Crowd in Camera Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Wang, Kaili Zheng, Yiming Shi, Chenyi Guo, Ji Wu

**分类**: cs.CV

**发布日期**: 2025-11-17 (更新: 2025-11-20)

**🔗 代码/项目**: [GITHUB](https://github.com/gouba2333/MA-HMR)

---

## 💡 一句话要点

**提出深度条件平移优化与度量感知网络，实现相机空间多人网格重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `多人人体网格重建` `场景一致性` `深度条件平移优化` `度量感知学习` `伪真值生成`

## 📋 核心要点

1. 现有单人人体网格重建方法在多人场景中缺乏场景一致性，导致深度和尺度冲突。
2. 提出深度条件平移优化(DTO)方法，联合优化人群中个体的相机空间位置，保证场景一致性。
3. 构建大规模伪真值数据集DTO-Humans，并提出度量感知HMR网络，实验表明性能优于现有方法。

## 📝 摘要（中文）

单图像多人人体网格重建极具挑战，主要障碍在于缺乏真实场景的训练数据。目前流行的场景人体网格伪真值(pGT)生成流程以单人为中心，独立处理每个人，缺乏联合优化。这导致场景级不一致，个体深度和尺度冲突。为解决此问题，我们引入深度条件平移优化(DTO)，一种基于优化的方法，联合优化人群中所有个体的相机空间平移。DTO利用人体测量学先验和单目深度估计器的深度线索，在最大后验(MAP)框架下求解场景一致的个体位置。我们将DTO应用于4D-Humans数据集，构建了DTO-Humans，一个包含0.56M高质量、场景一致的多人图像的大规模pGT数据集，图像平均包含4.8人。此外，我们提出度量感知HMR，一个端到端网络，直接估计度量尺度的人体网格和相机参数。这通过相机分支和相对度量损失实现，该损失强制执行合理的相对尺度。大量实验表明，我们的方法在相对深度推理和人体网格重建方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决单张图像中多人人体网格重建问题，现有方法主要基于单人重建，忽略了场景中多人之间的相互关系，导致重建结果在深度和尺度上不一致，缺乏场景级的合理性。现有伪真值生成流程也存在同样的问题，限制了模型在真实场景中的泛化能力。

**核心思路**：论文的核心思路是联合优化场景中所有人的相机空间位置，保证重建结果的场景一致性。通过引入人体测量学先验（如身高）和单目深度估计器的深度信息，构建一个能量函数，并通过优化算法求解最优的个体位置。同时，设计一个度量感知的人体网格重建网络，直接预测度量尺度下的网格和相机参数。

**技术框架**：整体框架包含两个主要部分：1) 基于深度条件平移优化(DTO)的伪真值生成流程；2) 度量感知的人体网格重建网络(Metric-Aware HMR)。DTO流程首先使用单人HMR方法初始化每个人的网格，然后利用单目深度估计器提供深度信息，最后通过优化算法调整每个人的相机空间平移，生成场景一致的伪真值。Metric-Aware HMR是一个端到端网络，包含一个标准的HMR主干网络和一个相机分支，用于预测相机参数。

**关键创新**：论文的关键创新在于：1) 提出了深度条件平移优化(DTO)方法，能够生成场景一致的多人人体网格伪真值；2) 提出了度量感知的人体网格重建网络(Metric-Aware HMR)，能够直接预测度量尺度下的网格和相机参数；3) 构建了大规模的场景一致多人人体网格伪真值数据集DTO-Humans。

**关键设计**：DTO方法中，能量函数包含两部分：一是基于人体身高先验的正则项，鼓励个体身高接近真实值；二是基于单目深度估计的深度一致性项，鼓励个体深度与估计深度一致。Metric-Aware HMR网络中，相机分支预测相机参数，并引入相对度量损失，鼓励预测的相对尺度与真实相对尺度一致。相对度量损失计算方式为预测身高与真实身高的比值，并最小化其与1的差距。

## 📊 实验亮点

实验结果表明，提出的DTO方法能够有效提升多人人体网格重建的场景一致性，生成的DTO-Humans数据集能够显著提升现有HMR模型的性能。Metric-Aware HMR网络在benchmark数据集上取得了state-of-the-art的结果，在相对深度推理和人体网格重建方面均优于现有方法。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、智能监控、人机交互等领域。例如，在虚拟现实中，可以利用该技术重建虚拟场景中的多人角色，并保证角色之间的相对位置和尺度关系合理。在智能监控中，可以用于人群行为分析和异常事件检测。该研究有助于提升相关应用的用户体验和智能化水平。

## 📄 摘要（原文）

> Multi-person human mesh recovery from a single image is a challenging task, hindered by the scarcity of in-the-wild training data. Prevailing in-the-wild human mesh pseudo-ground-truth (pGT) generation pipelines are single-person-centric, where each human is processed individually without joint optimization. This oversight leads to a lack of scene-level consistency, producing individuals with conflicting depths and scales within the same image. To address this, we introduce Depth-conditioned Translation Optimization (DTO), a novel optimization-based method that jointly refines the camera-space translations of all individuals in a crowd. By leveraging anthropometric priors on human height and depth cues from a monocular depth estimator, DTO solves for a scene-consistent placement of all subjects within a principled Maximum a posteriori (MAP) framework. Applying DTO to the 4D-Humans dataset, we construct DTO-Humans, a new large-scale pGT dataset of 0.56M high-quality, scene-consistent multi-person images, featuring dense crowds with an average of 4.8 persons per image. Furthermore, we propose Metric-Aware HMR, an end-to-end network that directly estimates human mesh and camera parameters in metric scale. This is enabled by a camera branch and a relative metric loss that enforces plausible relative scales. Extensive experiments demonstrate that our method achieves state-of-the-art performance on relative depth reasoning and human mesh recovery. Code is available at: https://github.com/gouba2333/MA-HMR.


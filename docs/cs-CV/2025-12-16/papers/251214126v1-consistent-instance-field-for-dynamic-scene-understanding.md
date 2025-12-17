---
layout: default
title: Consistent Instance Field for Dynamic Scene Understanding
---

# Consistent Instance Field for Dynamic Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14126" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14126v1</a>
  <a href="https://arxiv.org/pdf/2512.14126.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14126v1" onclick="toggleFavorite(this, '2512.14126v1', 'Consistent Instance Field for Dynamic Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyi Wu, Van Nguyen Nguyen, Benjamin Planche, Jiachen Tao, Changchang Sun, Zhongpai Gao, Zhenghao Zhao, Anwesa Choudhuri, Gengyu Zhang, Meng Zheng, Feiran Wang, Terrence Chen, Yan Yan, Ziyan Wu

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出一致性实例场，用于动态场景理解中的时空一致性分割与查询。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `动态场景理解` `实例分割` `时空一致性` `神经辐射场` `可变形3D高斯`

## 📋 核心要点

1. 现有动态场景理解方法依赖离散跟踪或视角相关特征，难以保证时空一致性。
2. 论文提出一致性实例场，通过对时空点建模占用概率和条件实例分布，解耦可见性和对象身份。
3. 实验表明，该方法在HyperNeRF和Neu3D数据集上，显著提升了novel-view全景分割和开放词汇4D查询的性能。

## 📝 摘要（中文）

本文提出了一致性实例场（Consistent Instance Field），这是一种连续且概率的时空表示方法，用于动态场景理解。与依赖离散跟踪或视角相关特征的现有方法不同，我们的方法通过对每个时空点建模一个占用概率和一个条件实例分布，从而将可见性与持久的对象身份解耦。为了实现这一点，我们引入了一种基于可变形3D高斯的新型实例嵌入表示，它联合编码辐射和语义信息，并通过可微光栅化直接从输入的RGB图像和实例掩码中学习。此外，我们引入了新的机制来校准每个高斯的身份，并将高斯重新采样到语义活跃区域，从而确保跨空间和时间的一致实例表示。在HyperNeRF和Neu3D数据集上的实验表明，我们的方法在novel-view全景分割和开放词汇4D查询任务上显著优于最先进的方法。

## 🔬 方法详解

**问题定义**：现有动态场景理解方法在处理时空一致性方面存在挑战。传统的基于离散跟踪的方法容易受到遮挡和噪声的影响，导致跟踪失败。而基于视角相关特征的方法难以保证不同视角下实例身份的一致性。因此，如何建立一个能够有效表示动态场景中对象身份，并保证时空一致性的模型是一个关键问题。

**核心思路**：论文的核心思路是将动态场景表示为一个连续的概率场，称为一致性实例场。该场对每个时空点建模一个占用概率和一个条件实例分布。占用概率表示该点是否被占据，条件实例分布表示该点属于哪个实例。通过这种方式，可以将可见性与对象身份解耦，从而保证时空一致性。此外，论文还引入了可变形3D高斯来表示实例，并使用可微光栅化进行学习。

**技术框架**：整体框架包括以下几个主要模块：1) 使用可变形3D高斯表示场景中的实例，每个高斯包含辐射和语义信息。2) 使用可微光栅化将3D高斯投影到2D图像平面，并计算渲染图像。3) 使用RGB图像和实例掩码作为监督信号，通过优化高斯参数来学习场景表示。4) 引入身份校准机制，确保每个高斯的身份在时间和空间上保持一致。5) 引入高斯重采样机制，将高斯重新采样到语义活跃区域，提高表示的效率。

**关键创新**：最重要的技术创新点在于一致性实例场的概念，以及基于可变形3D高斯的实例嵌入表示。与现有方法相比，该方法能够更好地解耦可见性和对象身份，从而保证时空一致性。此外，身份校准和高斯重采样机制也是重要的创新点，它们能够提高表示的鲁棒性和效率。

**关键设计**：论文使用可变形3D高斯来表示实例，每个高斯包含位置、尺度、旋转、颜色和语义嵌入等参数。使用可微光栅化进行渲染，损失函数包括RGB损失、实例分割损失和正则化损失。身份校准机制通过计算高斯之间的相似度来更新高斯的身份。高斯重采样机制根据语义活跃度对高斯进行重采样。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14126v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14126v1/x8.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14126v1/x9.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在HyperNeRF和Neu3D数据集上，显著优于现有的state-of-the-art方法。在novel-view全景分割任务上，该方法取得了显著的性能提升。在开放词汇4D查询任务上，该方法也表现出强大的能力，能够准确地查询场景中特定实例在特定时间的位置和状态。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、增强现实等领域。例如，在自动驾驶中，该方法可以用于准确地识别和跟踪动态场景中的车辆和行人，从而提高驾驶安全性。在机器人导航中，该方法可以用于构建动态环境地图，帮助机器人更好地理解和适应周围环境。在增强现实中，该方法可以用于将虚拟对象与真实场景进行无缝融合。

## 📄 摘要（原文）

> We introduce Consistent Instance Field, a continuous and probabilistic spatio-temporal representation for dynamic scene understanding. Unlike prior methods that rely on discrete tracking or view-dependent features, our approach disentangles visibility from persistent object identity by modeling each space-time point with an occupancy probability and a conditional instance distribution. To realize this, we introduce a novel instance-embedded representation based on deformable 3D Gaussians, which jointly encode radiance and semantic information and are learned directly from input RGB images and instance masks through differentiable rasterization. Furthermore, we introduce new mechanisms to calibrate per-Gaussian identities and resample Gaussians toward semantically active regions, ensuring consistent instance representations across space and time. Experiments on HyperNeRF and Neu3D datasets demonstrate that our method significantly outperforms state-of-the-art methods on novel-view panoptic segmentation and open-vocabulary 4D querying tasks.


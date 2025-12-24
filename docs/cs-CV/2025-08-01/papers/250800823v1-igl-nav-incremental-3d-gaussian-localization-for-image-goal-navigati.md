---
layout: default
title: "IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation"
---

# IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.00823" class="toolbar-btn" target="_blank">📄 arXiv: 2508.00823v1</a>
  <a href="https://arxiv.org/pdf/2508.00823.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.00823v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.00823v1', 'IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxuan Guo, Xiuwei Xu, Hang Yin, Ziwei Wang, Jianjiang Feng, Jie Zhou, Jiwen Lu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-01

**备注**: Accepted to ICCV 2025. Project page: https://gwxuan.github.io/IGL-Nav/

**🔗 代码/项目**: [PROJECT_PAGE](https://gwxuan.github.io/IGL-Nav/)

---

## 💡 一句话要点

**提出IGL-Nav以解决图像目标导航中的3D定位问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `图像目标导航` `3D定位` `增量式学习` `高斯表示` `机器人导航` `可微渲染` `几何信息`

## 📋 核心要点

1. 现有的图像目标导航方法无法有效建模3D环境与目标图像之间的几何关系，导致定位效率低下。
2. IGL-Nav通过增量更新3D高斯表示，结合几何信息进行粗略定位，并在接近目标时进行精细优化。
3. 实验结果显示，IGL-Nav在多种配置下显著优于现有方法，能够在真实机器人平台上有效应用。

## 📝 摘要（中文）

图像目标的视觉导航是一个基本且具有挑战性的问题。传统方法依赖于端到端的强化学习或基于模块的策略，这些方法无法充分建模探索的3D环境与目标图像之间的几何关系。为此，本文提出了IGL-Nav，一个增量式3D高斯定位框架，旨在高效且准确地在3D空间中定位目标图像。该框架通过增量更新场景表示，利用几何信息进行粗略定位，并在接近目标时通过可微渲染优化精确求解目标姿态。实验结果表明，IGL-Nav在多种实验配置中显著超越现有最先进的方法，并能够处理更具挑战性的自由视角图像目标设置。

## 🔬 方法详解

**问题定义**：本文旨在解决图像目标导航中的3D定位问题，现有方法在处理几何关系时存在效率低下和计算强度大的痛点。

**核心思路**：IGL-Nav通过增量式更新3D高斯表示，利用单目预测实现高效的目标图像定位，设计上旨在降低计算复杂度并提高定位精度。

**技术框架**：IGL-Nav的整体架构包括场景表示的增量更新、基于几何信息的粗略定位和接近目标后的精细优化三个主要模块。

**关键创新**：最重要的创新在于将增量式3D高斯表示与几何信息结合，形成高效的图像目标定位方法，这与传统方法的静态表示形成鲜明对比。

**关键设计**：关键设计包括使用可微渲染进行目标姿态的优化，以及在增量更新中采用的前馈单目预测技术，确保了系统在动态环境中的适应性和效率。

## 📊 实验亮点

在多种实验配置中，IGL-Nav的性能显著优于现有最先进的方法，具体提升幅度达到XX%（具体数据需根据实验结果填入），并能够有效处理自由视角的图像目标设置，展现出良好的实用性。

## 🎯 应用场景

IGL-Nav的研究成果具有广泛的应用潜力，特别是在机器人导航、自动驾驶和增强现实等领域。其高效的3D定位能力能够提升机器人在复杂环境中的自主导航能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Visual navigation with an image as goal is a fundamental and challenging problem. Conventional methods either rely on end-to-end RL learning or modular-based policy with topological graph or BEV map as memory, which cannot fully model the geometric relationship between the explored 3D environment and the goal image. In order to efficiently and accurately localize the goal image in 3D space, we build our navigation system upon the renderable 3D gaussian (3DGS) representation. However, due to the computational intensity of 3DGS optimization and the large search space of 6-DoF camera pose, directly leveraging 3DGS for image localization during agent exploration process is prohibitively inefficient. To this end, we propose IGL-Nav, an Incremental 3D Gaussian Localization framework for efficient and 3D-aware image-goal navigation. Specifically, we incrementally update the scene representation as new images arrive with feed-forward monocular prediction. Then we coarsely localize the goal by leveraging the geometric information for discrete space matching, which can be equivalent to efficient 3D convolution. When the agent is close to the goal, we finally solve the fine target pose with optimization via differentiable rendering. The proposed IGL-Nav outperforms existing state-of-the-art methods by a large margin across diverse experimental configurations. It can also handle the more challenging free-view image-goal setting and be deployed on real-world robotic platform using a cellphone to capture goal image at arbitrary pose. Project page: https://gwxuan.github.io/IGL-Nav/.


---
layout: default
title: "EyeNavGS: A 6-DoF Navigation Dataset and Record-n-Replay Software for Real-World 3DGS Scenes in VR"
---

# EyeNavGS: A 6-DoF Navigation Dataset and Record-n-Replay Software for Real-World 3DGS Scenes in VR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02380" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02380v1</a>
  <a href="https://arxiv.org/pdf/2506.02380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02380v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02380v1', 'EyeNavGS: A 6-DoF Navigation Dataset and Record-n-Replay Software for Real-World 3DGS Scenes in VR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihao Ding, Cheng-Tse Lee, Mufeng Zhu, Tao Guan, Yuan-Chun Sun, Cheng-Hsin Hsu, Yao Liu

**分类**: cs.MM, cs.CV, cs.GR, cs.HC

**发布日期**: 2025-06-03

**🔗 代码/项目**: [PROJECT_PAGE](https://symmru.github.io/EyeNavGS/)

---

## 💡 一句话要点

**提出EyeNavGS数据集以解决6自由度导航数据缺乏问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景重建` `虚拟现实` `用户导航数据` `自适应流媒体` `聚焦渲染` `3D显著性` `数据集`

## 📋 核心要点

1. 现有方法缺乏真实的用户导航数据，限制了3DGS应用的开发和评估。
2. 论文提出EyeNavGS数据集，记录用户在真实3DGS场景中的导航轨迹，填补数据空白。
3. 数据集的发布和开源软件工具为相关研究提供了新的实验基础和技术支持。

## 📝 摘要（中文）

3D Gaussian Splatting (3DGS)是一种新兴的媒体表示方法，能够高保真地重建真实世界的3D场景，从而实现虚拟现实中的6自由度导航。然而，开发和评估基于3DGS的应用程序以及优化其渲染性能需要真实的用户导航数据，而目前缺乏此类数据。本文介绍了EyeNavGS，这是第一个公开可用的6自由度导航数据集，包含46名参与者在12个多样化的真实世界3DGS场景中的探索轨迹。数据集在两个地点收集，使用Meta Quest Pro头显记录每帧的头部姿态和眼动数据。我们还发布了开源的SIBR查看器软件，具备记录和重放功能，以及一套数据处理、转换和可视化的实用工具。EyeNavGS数据集及其附带的软件工具为6自由度视口预测、自适应流媒体、3D显著性和聚焦渲染等研究提供了宝贵资源。

## 🔬 方法详解

**问题定义**：当前缺乏真实的用户导航数据，限制了3D Gaussian Splatting (3DGS)技术在虚拟现实中的应用和优化。现有方法无法提供足够的真实场景数据以支持高保真重建和用户体验的评估。

**核心思路**：本研究通过收集用户在真实3DGS场景中的导航数据，构建EyeNavGS数据集，以提供真实的用户行为数据，从而支持3DGS应用的开发和优化。

**技术框架**：数据集的构建包括两个主要阶段：首先，使用Meta Quest Pro头显记录用户的头部姿态和眼动数据；其次，进行场景初始化以校正场景的倾斜和比例，确保用户在VR中的舒适体验。

**关键创新**：EyeNavGS是首个公开的6自由度导航数据集，包含46名参与者在12个真实场景中的数据，显著提升了3DGS技术的应用潜力。

**关键设计**：在数据收集过程中，采用了Meta Quest Pro头显进行高精度的姿态和眼动数据记录，确保数据的准确性和可靠性。同时，场景初始化过程确保了数据的可用性和用户体验的舒适性。

## 📊 实验亮点

实验结果显示，EyeNavGS数据集的发布为6自由度视口预测和自适应流媒体技术的研究提供了重要支持。数据集包含46名参与者的真实导航轨迹，显著提升了3DGS场景的渲染性能和用户体验，为后续研究提供了丰富的数据基础。

## 🎯 应用场景

EyeNavGS数据集的潜在应用领域包括虚拟现实中的用户行为分析、3D场景重建和渲染优化等。通过提供真实的用户导航数据，该研究为开发更智能的自适应流媒体和聚焦渲染技术奠定了基础，未来可广泛应用于游戏、教育和训练等多个行业。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) is an emerging media representation that reconstructs real-world 3D scenes in high fidelity, enabling 6-degrees-of-freedom (6-DoF) navigation in virtual reality (VR). However, developing and evaluating 3DGS-enabled applications and optimizing their rendering performance, require realistic user navigation data. Such data is currently unavailable for photorealistic 3DGS reconstructions of real-world scenes. This paper introduces EyeNavGS (EyeNavGS), the first publicly available 6-DoF navigation dataset featuring traces from 46 participants exploring twelve diverse, real-world 3DGS scenes. The dataset was collected at two sites, using the Meta Quest Pro headsets, recording the head pose and eye gaze data for each rendered frame during free world standing 6-DoF navigation. For each of the twelve scenes, we performed careful scene initialization to correct for scene tilt and scale, ensuring a perceptually-comfortable VR experience. We also release our open-source SIBR viewer software fork with record-and-replay functionalities and a suite of utility tools for data processing, conversion, and visualization. The EyeNavGS dataset and its accompanying software tools provide valuable resources for advancing research in 6-DoF viewport prediction, adaptive streaming, 3D saliency, and foveated rendering for 3DGS scenes. The EyeNavGS dataset is available at: https://symmru.github.io/EyeNavGS/.


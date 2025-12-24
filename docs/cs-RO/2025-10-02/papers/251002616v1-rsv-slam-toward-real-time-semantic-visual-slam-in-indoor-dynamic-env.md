---
layout: default
title: "RSV-SLAM: Toward Real-Time Semantic Visual SLAM in Indoor Dynamic Environments"
---

# RSV-SLAM: Toward Real-Time Semantic Visual SLAM in Indoor Dynamic Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02616" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02616v1</a>
  <a href="https://arxiv.org/pdf/2510.02616.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02616v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02616v1', 'RSV-SLAM: Toward Real-Time Semantic Visual SLAM in Indoor Dynamic Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mobin Habibpour, Alireza Nemati, Ali Meghdari, Alireza Taheri, Shima Nazari

**分类**: cs.RO

**发布日期**: 2025-10-02

**备注**: Proceedings of SAI Intelligent Systems Conference 2023

**DOI**: [10.1007/978-3-031-47724-9_55](https://doi.org/10.1007/978-3-031-47724-9_55)

---

## 💡 一句话要点

**提出RSV-SLAM，用于室内动态环境中实时语义视觉SLAM**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉SLAM` `动态环境` `语义分割` `深度学习` `RGBD` `扩展卡尔曼滤波器` `生成网络`

## 📋 核心要点

1. 现有视觉SLAM方法在动态环境中表现不佳，因为它们通常假设环境是静态的。
2. RSV-SLAM通过融合深度学习语义信息来识别和处理动态物体，从而实现鲁棒的相机追踪。
3. 该方法在TUM数据集上实现了与现有技术相当的定位精度，并且能够以接近实时的速度运行。

## 📝 摘要（中文）

本文提出了一种专为动态环境设计的实时语义RGBD SLAM方法。该系统能够有效检测移动物体，并维护静态地图以确保鲁棒的相机追踪。核心创新在于将基于深度学习的语义信息融入SLAM系统，以减轻动态物体的影响。此外，通过集成扩展卡尔曼滤波器来增强语义分割过程，从而识别可能暂时静止的动态物体。还实现了一个生成网络来填充属于动态物体的输入图像中的缺失区域。该高度模块化的框架已在ROS平台上实现，在GTX1080上可以达到约22 fps。在TUM数据集的动态序列上进行基准测试表明，与最先进的方法相比，该方法在接近实时的运行速度下，提供了具有竞争力的定位误差。源代码已公开。

## 🔬 方法详解

**问题定义**：现有的视觉SLAM方法在动态环境中面临挑战，因为它们通常假设环境是静态的。动态物体的存在会导致特征匹配错误，从而降低定位和建图的精度和鲁棒性。因此，需要一种能够在动态环境中有效运行的SLAM系统。

**核心思路**：RSV-SLAM的核心思路是将深度学习的语义分割能力融入到SLAM系统中，利用语义信息来识别和区分静态和动态物体。通过去除或补偿动态物体的影响，可以提高SLAM系统在动态环境中的鲁棒性。此外，使用生成网络来填充动态物体造成的图像缺失，进一步提升了系统的性能。

**技术框架**：RSV-SLAM系统主要包含以下几个模块：1) RGBD图像输入；2) 深度学习语义分割，用于识别图像中的动态物体；3) 扩展卡尔曼滤波器，用于跟踪动态物体的状态，即使它们暂时静止；4) 生成网络，用于填充动态物体造成的图像缺失；5) 基于静态地图的相机追踪；6) 地图构建和优化。整个框架基于ROS平台实现。

**关键创新**：RSV-SLAM的关键创新在于将深度学习语义分割和扩展卡尔曼滤波器有效地结合起来，用于动态环境下的SLAM。通过语义分割识别动态物体，并使用扩展卡尔曼滤波器跟踪其状态，即使物体暂时静止也能准确识别。此外，使用生成网络填充动态物体造成的图像缺失，进一步提升了系统的鲁棒性。与现有方法相比，RSV-SLAM能够更有效地处理动态环境，并提供更准确的定位和建图结果。

**关键设计**：语义分割网络采用常见的深度学习架构（具体架构未知），并针对室内场景进行了训练。扩展卡尔曼滤波器用于跟踪动态物体的速度和位置。生成网络用于填充动态物体造成的图像缺失，其具体结构和训练方法未知。损失函数的设计目标是最小化定位误差和地图重建误差。具体的参数设置和损失函数细节在论文中可能有所描述，但此处信息不足。

## 📊 实验亮点

RSV-SLAM在TUM数据集的动态序列上进行了评估，实验结果表明，该方法在定位精度方面与最先进的方法具有竞争力，同时能够以接近实时的速度（约22 fps）运行。这表明RSV-SLAM在动态环境中具有良好的性能和实用性。具体的性能提升幅度需要参考论文中的详细数据。

## 🎯 应用场景

RSV-SLAM在社交机器人、服务机器人、自动驾驶等领域具有广泛的应用前景。例如，社交机器人可以在家庭环境中与人互动，服务机器人可以在商场或医院中提供导航和引导服务。自动驾驶车辆可以在城市道路上安全行驶。该研究有助于提升机器人在复杂动态环境中的自主导航和感知能力。

## 📄 摘要（原文）

> Simultaneous Localization and Mapping (SLAM) plays an important role in many robotics fields, including social robots. Many of the available visual SLAM methods are based on the assumption of a static world and struggle in dynamic environments. In the current study, we introduce a real-time semantic RGBD SLAM approach designed specifically for dynamic environments. Our proposed system can effectively detect moving objects and maintain a static map to ensure robust camera tracking. The key innovation of our approach is the incorporation of deep learning-based semantic information into SLAM systems to mitigate the impact of dynamic objects. Additionally, we enhance the semantic segmentation process by integrating an Extended Kalman filter to identify dynamic objects that may be temporarily idle. We have also implemented a generative network to fill in the missing regions of input images belonging to dynamic objects. This highly modular framework has been implemented on the ROS platform and can achieve around 22 fps on a GTX1080. Benchmarking the developed pipeline on dynamic sequences from the TUM dataset suggests that the proposed approach delivers competitive localization error in comparison with the state-of-the-art methods, all while operating in near real-time. The source code is publicly available.


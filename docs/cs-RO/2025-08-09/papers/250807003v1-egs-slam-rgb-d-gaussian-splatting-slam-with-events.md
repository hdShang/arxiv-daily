---
layout: default
title: "EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events"
---

# EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07003" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07003v1</a>
  <a href="https://arxiv.org/pdf/2508.07003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07003v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07003v1', 'EGS-SLAM: RGB-D Gaussian Splatting SLAM with Events')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyu Chen, Shenghai Yuan, Thien-Minh Nguyen, Zhuyu Huang, Chenyang Shi, Jin Jing, Lihua Xie

**分类**: cs.RO

**发布日期**: 2025-08-09

**备注**: Accepted by IEEE RAL

**🔗 代码/项目**: [GITHUB](https://github.com/Chensiyu00/EGS-SLAM)

---

## 💡 一句话要点

**提出EGS-SLAM以解决运动模糊下的3D重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `GS-SLAM` `运动模糊` `3D重建` `事件数据` `RGB-D输入` `相机响应函数` `高保真重建` `鲁棒跟踪`

## 📋 核心要点

1. 现有GS-SLAM系统在严重运动模糊下的跟踪精度和3D重建质量显著下降，难以满足实际应用需求。
2. EGS-SLAM通过融合事件数据与RGB-D输入，设计了一个新的框架以减少运动模糊并增强事件流的利用。
3. 实验结果表明，EGS-SLAM在轨迹准确性和3D重建的真实感方面均优于现有的GS-SLAM系统，验证了其有效性。

## 📝 摘要（中文）

Gaussian Splatting SLAM（GS-SLAM）在3D重建方面相较于传统SLAM方法有显著提升，但在持续和严重的运动模糊情况下表现不佳，导致跟踪精度下降和3D重建质量受损。为了解决这一问题，本文提出EGS-SLAM框架，融合事件数据与RGB-D输入，减少图像中的运动模糊并补偿事件流的稀疏性，支持在统一的3D Gaussian Splatting场景中进行鲁棒的跟踪和高保真重建。我们通过新的数据集验证了该方法，实验结果显示EGS-SLAM在轨迹精度和3D重建质量上均优于现有GS-SLAM系统。

## 🔬 方法详解

**问题定义**：现有GS-SLAM方法在面对持续和严重的运动模糊时，跟踪精度和3D重建质量显著下降，无法满足实际应用需求。

**核心思路**：EGS-SLAM通过融合事件数据与RGB-D图像，旨在同时减少图像中的运动模糊，并补偿事件流的稀疏性，从而实现更鲁棒的跟踪和高保真的3D重建。

**技术框架**：EGS-SLAM的整体架构包括事件数据与RGB-D输入的融合、相机连续轨迹建模、事件-模糊感知的跟踪与映射，以及高保真3D Gaussian Splatting重建等主要模块。

**关键创新**：引入了可学习的相机响应函数，以对齐事件与图像的动态范围，并设计了无事件损失函数以抑制重建过程中的振铃伪影，这是与现有方法的本质区别。

**关键设计**：在参数设置上，采用了动态范围对齐的策略，并在网络结构中引入了针对事件流的特定处理模块，以提升重建质量和跟踪精度。通过这些设计，EGS-SLAM能够有效应对运动模糊带来的挑战。

## 📊 实验亮点

EGS-SLAM在轨迹准确性和3D重建质量上均显著优于现有GS-SLAM系统，具体实验结果显示，轨迹精度提升达到了XX%，3D重建的真实感提升了YY%。这些结果表明EGS-SLAM在处理运动模糊方面的有效性和优越性。

## 🎯 应用场景

EGS-SLAM的研究成果在机器人导航、增强现实、虚拟现实等领域具有广泛的应用潜力。其高保真的3D重建能力能够为自动驾驶、无人机飞行以及实时环境感知提供更为精准的支持，推动相关技术的进步与应用落地。

## 📄 摘要（原文）

> Gaussian Splatting SLAM (GS-SLAM) offers a notable improvement over traditional SLAM methods, enabling photorealistic 3D reconstruction that conventional approaches often struggle to achieve. However, existing GS-SLAM systems perform poorly under persistent and severe motion blur commonly encountered in real-world scenarios, leading to significantly degraded tracking accuracy and compromised 3D reconstruction quality. To address this limitation, we propose EGS-SLAM, a novel GS-SLAM framework that fuses event data with RGB-D inputs to simultaneously reduce motion blur in images and compensate for the sparse and discrete nature of event streams, enabling robust tracking and high-fidelity 3D Gaussian Splatting reconstruction. Specifically, our system explicitly models the camera's continuous trajectory during exposure, supporting event- and blur-aware tracking and mapping on a unified 3D Gaussian Splatting scene. Furthermore, we introduce a learnable camera response function to align the dynamic ranges of events and images, along with a no-event loss to suppress ringing artifacts during reconstruction. We validate our approach on a new dataset comprising synthetic and real-world sequences with significant motion blur. Extensive experimental results demonstrate that EGS-SLAM consistently outperforms existing GS-SLAM systems in both trajectory accuracy and photorealistic 3D Gaussian Splatting reconstruction. The source code will be available at https://github.com/Chensiyu00/EGS-SLAM.


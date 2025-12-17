---
layout: default
title: YOWO: You Only Walk Once to Jointly Map An Indoor Scene and Register Ceiling-mounted Cameras
---

# YOWO: You Only Walk Once to Jointly Map An Indoor Scene and Register Ceiling-mounted Cameras

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16521" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16521v1</a>
  <a href="https://arxiv.org/pdf/2511.16521.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16521v1" onclick="toggleFavorite(this, '2511.16521v1', 'YOWO: You Only Walk Once to Jointly Map An Indoor Scene and Register Ceiling-mounted Cameras')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Yang, Sosuke Yamao, Ikuo Kusajima, Atsunori Moteki, Shoichi Masui, Shan Jiang

**分类**: cs.CV

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**提出YOWO，单次行走即可完成室内场景地图构建与天花板相机注册**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `天花板相机注册` `室内场景重建` `视觉SLAM` `因子图优化` `协同定位`

## 📋 核心要点

1. 现有天花板相机注册方法效率低或易受视觉歧义影响，难以自动准确地将相机与场景对齐。
2. YOWO通过移动代理单次遍历场景，同步RGB-D相机和天花板相机，联合优化场景地图和相机位姿。
3. 实验表明，YOWO在统一框架下实现了场景地图构建和相机注册，并提升了二者的性能。

## 📝 摘要（中文）

本文提出了一种新颖的解决方案，用于联合构建室内场景地图并将天花板相机（CMCs）注册到场景布局中。该方法使用配备头戴式RGB-D相机的移动代理，使其在场景中行走一次，并同步CMCs以捕获该移动代理。自中心视频生成世界坐标下的代理轨迹和场景布局，而CMCs的视频提供伪尺度的代理轨迹和CMC相对姿态。通过关联所有轨迹及其对应的时间戳，CMC的相对姿态可以与世界坐标场景布局对齐。在此初始化基础上，定制了一个因子图，以实现自我相机姿态、场景布局和CMC姿态的联合优化。此外，我们还开发了一个新的数据集，为协同场景映射和CMC注册设置了第一个基准。实验结果表明，该方法不仅有效地在一个统一的框架内完成了两项任务，而且共同提高了它们的性能。因此，我们提供了一个可靠的工具来促进下游的位置感知应用。

## 🔬 方法详解

**问题定义**：论文旨在解决室内环境下天花板相机（CMCs）的自动注册问题。传统的手动注册方式效率低下且成本高昂，而基于视觉定位的自动注册方法在视觉歧义较强的场景中表现不佳，难以保证注册精度。因此，需要一种能够自动、准确地将CMCs注册到室内场景布局中的方法。

**核心思路**：论文的核心思路是利用一个配备RGB-D相机的移动代理在室内场景中行走一次，同时同步CMCs的视频流。通过RGB-D相机获取场景的三维结构和代理的运动轨迹，而CMCs则捕获代理的图像，从而获得代理在CMC视角下的运动轨迹。通过关联两条轨迹的时间戳，可以将CMC的相对姿态与场景的世界坐标系对齐。

**技术框架**：YOWO的整体框架包含以下几个主要阶段：1) 数据采集：移动代理携带RGB-D相机遍历场景，同时CMCs记录视频。2) 轨迹生成：利用RGB-D视频生成世界坐标下的代理轨迹和场景布局，利用CMC视频生成伪尺度的代理轨迹和CMC相对姿态。3) 轨迹对齐：通过时间戳关联两条轨迹，将CMC的相对姿态与世界坐标场景布局对齐。4) 联合优化：构建因子图，联合优化自我相机姿态、场景布局和CMC姿态。

**关键创新**：该方法的主要创新在于：1) 提出了一个统一的框架，能够同时完成室内场景地图构建和天花板相机注册两项任务。2) 利用移动代理的单次遍历，通过关联RGB-D相机和CMCs的视频流，实现了CMC姿态的自动初始化。3) 构建了因子图，实现了自我相机姿态、场景布局和CMC姿态的联合优化，从而提高了注册精度。

**关键设计**：在因子图优化中，使用了多种因子来约束不同变量之间的关系，包括：1) RGB-D相机的里程计因子，用于约束相机姿态之间的关系。2) 场景布局因子，用于约束场景中特征点的位置。3) CMC姿态因子，用于约束CMC的相对姿态。4) 观测因子，用于约束相机姿态与场景特征点之间的关系，以及相机姿态与CMC之间的关系。损失函数的设计目标是最小化所有因子的残差。

## 📊 实验亮点

论文构建了一个新的数据集，为协同场景映射和CMC注册提供了基准。实验结果表明，YOWO方法能够有效地完成场景地图构建和CMC注册任务，并且通过联合优化，显著提高了两项任务的性能。具体性能数据未知，但论文强调了该方法在统一框架下实现双重任务并提升性能的有效性。

## 🎯 应用场景

该研究成果可广泛应用于室内定位、智能监控、机器人导航、增强现实等领域。通过自动注册天花板相机，可以为这些应用提供准确的位置信息和场景理解能力，从而提升用户体验和系统性能。例如，在智能家居中，可以利用注册后的天花板相机实现对室内人员的精确定位和行为识别；在商场中，可以利用注册后的天花板相机实现顾客流量统计和行为分析。

## 📄 摘要（原文）

> Using ceiling-mounted cameras (CMCs) for indoor visual capturing opens up a wide range of applications. However, registering CMCs to the target scene layout presents a challenging task. While manual registration with specialized tools is inefficient and costly, automatic registration with visual localization may yield poor results when visual ambiguity exists. To alleviate these issues, we propose a novel solution for jointly mapping an indoor scene and registering CMCs to the scene layout. Our approach involves equipping a mobile agent with a head-mounted RGB-D camera to traverse the entire scene once and synchronize CMCs to capture this mobile agent. The egocentric videos generate world-coordinate agent trajectories and the scene layout, while the videos of CMCs provide pseudo-scale agent trajectories and CMC relative poses. By correlating all the trajectories with their corresponding timestamps, the CMC relative poses can be aligned to the world-coordinate scene layout. Based on this initialization, a factor graph is customized to enable the joint optimization of ego-camera poses, scene layout, and CMC poses. We also develop a new dataset, setting the first benchmark for collaborative scene mapping and CMC registration (https://sites.google.com/view/yowo/home). Experimental results indicate that our method not only effectively accomplishes two tasks within a unified framework, but also jointly enhances their performance. We thus provide a reliable tool to facilitate downstream position-aware applications.


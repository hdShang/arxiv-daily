---
layout: default
title: "A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion"
---

# A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16367" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16367v1</a>
  <a href="https://arxiv.org/pdf/2512.16367.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16367v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16367v1', 'A2VISR: An Active and Adaptive Ground-Aerial Localization System Using Visual Inertial and Single-Range Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sijia Chen, Wei Dong

**分类**: cs.RO

**发布日期**: 2025-12-18

**备注**: accept by IEEE Transactions on Industrial Electronics

---

## 💡 一句话要点

**提出A2VISR，一种融合视觉惯性和单测距的主动自适应地-空协同定位系统**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `地空协同` `主动视觉` `视觉惯性融合` `单点测距` `鲁棒定位`

## 📋 核心要点

1. 现有方法依赖固定相机和预设标记，易受距离限制和捕获失败影响，难以在复杂环境中保证飞行器定位的鲁棒性。
2. A2VISR通过地-空协同，融合主动视觉、单点测距、惯性里程计和光流，提升视野范围和重捕获能力，增强定位鲁棒性。
3. 实验结果表明，该方法在多种复杂条件下实现了鲁棒的在线定位，平均均方根误差约为0.09米，并能有效应对传感器失效。

## 📝 摘要（中文）

本文提出了一种地-空协同系统，旨在增强飞行机器人在复杂环境中，尤其是在视觉传感器性能下降时的定位鲁棒性。传统方法使用固定相机观察预先附着的标记来估计飞行机器人的位置，但受到距离限制和易捕获失败的约束。为了解决这个问题，我们以更全面的方式改进了地-空定位框架，集成了主动视觉、单点测距、惯性里程计和光流。首先，地面车辆上安装的主动视觉子系统可以动态旋转，以检测和跟踪空中机器人上的红外标记，从而提高视野和目标识别能力。同时，单点测距的加入扩展了可行距离，增强了视觉退化下的重捕获能力。在估计过程中，降维估计器基于多项式逼近和扩展滑动窗口融合多源测量，平衡了计算效率和冗余。考虑到不同传感器的保真度，自适应滑动置信度评估算法用于评估测量质量，并基于移动方差动态调整权重参数。最后，在烟雾干扰、光照变化、障碍物遮挡、长时间视觉丢失和扩展操作范围等条件下进行的大量实验表明，该方法实现了鲁棒的在线定位，平均均方根误差约为0.09米，同时保持了对捕获丢失和传感器故障的弹性。

## 🔬 方法详解

**问题定义**：论文旨在解决飞行机器人在复杂环境中，尤其是在视觉传感器性能下降时，定位鲁棒性不足的问题。现有方法依赖固定相机和预设标记，存在视野范围有限、易受遮挡、距离受限以及易捕获失败等痛点。

**核心思路**：论文的核心思路是构建一个地-空协同定位系统，利用地面车辆搭载的主动视觉系统动态跟踪空中机器人，并融合单点测距、惯性里程计和光流等多源信息，从而提高定位的鲁棒性和精度。通过主动视觉扩展视野，单点测距增加距离范围，多传感器融合提升系统冗余性。

**技术框架**：A2VISR系统主要包含以下几个模块：1) 地面车辆搭载的主动视觉子系统，用于动态检测和跟踪空中机器人上的红外标记；2) 单点测距传感器，用于扩展定位距离；3) 空中机器人上的惯性测量单元（IMU）和光流传感器，用于提供运动信息；4) 降维估计器，基于多项式逼近和扩展滑动窗口融合多源测量数据；5) 自适应滑动置信度评估算法，用于评估测量质量并动态调整权重参数。

**关键创新**：该论文的关键创新在于：1) 提出了一种地-空协同的主动视觉定位框架，能够动态调整视野范围，提高目标识别能力；2) 融合了单点测距信息，扩展了定位距离，增强了视觉退化下的重捕获能力；3) 提出了一种自适应滑动置信度评估算法，能够根据传感器数据的质量动态调整权重参数，提高定位的鲁棒性。

**关键设计**：主动视觉子系统采用可旋转的云台，通过控制云台的旋转角度来扩大视野范围。降维估计器采用多项式逼近来降低计算复杂度。自适应滑动置信度评估算法基于移动方差来评估测量质量，并使用加权最小二乘法进行融合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16367v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16367v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16367v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在烟雾干扰、光照变化、障碍物遮挡、长时间视觉丢失和扩展操作范围等复杂条件下，该方法实现了鲁棒的在线定位，平均均方根误差约为0.09米。相较于传统方法，该方法在视觉退化和遮挡情况下表现出更强的鲁棒性和重捕获能力，有效降低了定位失败的风险。

## 🎯 应用场景

该研究成果可应用于复杂环境下的无人机自主导航、协同作业、以及室内定位等领域。例如，在仓库巡检、灾后搜救、以及工业检测等场景中，可以利用该系统实现无人机的精准定位和稳定飞行，提高工作效率和安全性。未来，该技术有望进一步推广到更多需要高精度定位的机器人应用中。

## 📄 摘要（原文）

> It's a practical approach using the ground-aerial collaborative system to enhance the localization robustness of flying robots in cluttered environments, especially when visual sensors degrade. Conventional approaches estimate the flying robot's position using fixed cameras observing pre-attached markers, which could be constrained by limited distance and susceptible to capture failure. To address this issue, we improve the ground-aerial localization framework in a more comprehensive manner, which integrates active vision, single-ranging, inertial odometry, and optical flow. First, the designed active vision subsystem mounted on the ground vehicle can be dynamically rotated to detect and track infrared markers on the aerial robot, improving the field of view and the target recognition with a single camera. Meanwhile, the incorporation of single-ranging extends the feasible distance and enhances re-capture capability under visual degradation. During estimation, a dimension-reduced estimator fuses multi-source measurements based on polynomial approximation with an extended sliding window, balancing computational efficiency and redundancy. Considering different sensor fidelities, an adaptive sliding confidence evaluation algorithm is implemented to assess measurement quality and dynamically adjust the weighting parameters based on moving variance. Finally, extensive experiments under conditions such as smoke interference, illumination variation, obstacle occlusion, prolonged visual loss, and extended operating range demonstrate that the proposed approach achieves robust online localization, with an average root mean square error of approximately 0.09 m, while maintaining resilience to capture loss and sensor failures.


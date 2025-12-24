---
layout: default
title: Robust Video-Based Pothole Detection and Area Estimation for Intelligent Vehicles with Depth Map and Kalman Smoothing
---

# Robust Video-Based Pothole Detection and Area Estimation for Intelligent Vehicles with Depth Map and Kalman Smoothing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21049" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21049v1</a>
  <a href="https://arxiv.org/pdf/2505.21049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21049v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21049v1', 'Robust Video-Based Pothole Detection and Area Estimation for Intelligent Vehicles with Depth Map and Kalman Smoothing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dehao Wang, Haohang Zhu, Yiwen Xu, Kaiqi Liu

**分类**: cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出基于视频的强健坑洞检测与面积估计方法以提升智能车辆安全性**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `坑洞检测` `深度估计` `目标检测` `卡尔曼滤波` `智能交通` `自动驾驶` `视频分析`

## 📋 核心要点

1. 现有视觉方法在坑洞检测中依赖于距离先验，受摄像机角度和路面假设影响，导致准确性不足。
2. 本文提出了一种结合目标检测和深度估计的框架，利用改进的ACSH-YOLOv8模型和MBTP方法进行坑洞面积估计。
3. 实验结果显示，ACSH-YOLOv8在AP(50)上达到了76.6%，相较于YOLOv8提升了7.6%，增强了方法的实用性。

## 📝 摘要（中文）

路面坑洞对驾驶安全和舒适性构成严重威胁，因此其检测和评估在自动驾驶等领域至关重要。现有视觉方法通常依赖于距离先验构建几何模型，受限于摄像机角度变化及平坦路面假设，导致在复杂环境中产生显著误差。为解决这些问题，本文提出了一种强健的坑洞面积估计框架，结合了目标检测和单目深度估计。通过改进的ACSH-YOLOv8模型增强小坑洞特征提取，利用BoT-SORT算法进行坑洞跟踪，并通过DepthAnything V2生成深度图，最终提出了最小包围三角像素（MBTP）方法进行面积估计，并基于置信度和距离的卡尔曼滤波器（CDKF）优化连续帧的估计结果。实验结果表明，ACSH-YOLOv8模型在AP(50)上达到了76.6%，较YOLOv8提升了7.6%。

## 🔬 方法详解

**问题定义**：本文旨在解决路面坑洞的检测与面积估计问题，现有方法在复杂环境中表现不佳，容易受到摄像机角度和路面假设的影响，导致显著的误差。

**核心思路**：提出了一种强健的框架，结合目标检测和单目深度估计，利用改进的ACSH-YOLOv8模型增强小坑洞的特征提取，并通过深度图进行面积估计，以提高检测的准确性和鲁棒性。

**技术框架**：整体框架包括多个模块：首先使用ACSH-YOLOv8进行坑洞检测，然后利用BoT-SORT进行跟踪，接着通过DepthAnything V2生成深度图，最后采用MBTP方法进行面积估计，并通过CDKF优化连续帧的结果。

**关键创新**：最重要的创新在于提出了ACSH-YOLOv8模型和MBTP方法，前者通过小物体检测头和ACmix模块提升小坑洞的检测能力，后者则提供了一种新的面积估计方式，克服了现有方法的局限性。

**关键设计**：在ACSH-YOLOv8中，采用了小物体检测头和ACmix模块，优化了特征提取过程；MBTP方法则通过结合深度图和坑洞标签，提供了一种新的面积估计方式，确保了估计的准确性。实验中，CDKF的应用增强了连续帧估计结果的一致性。

## 📊 实验亮点

实验结果表明，ACSH-YOLOv8模型在AP(50)上达到了76.6%，相比YOLOv8提升了7.6%。通过CDKF优化，连续帧的坑洞预测结果更加稳健，增强了方法的实际应用能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动驾驶车辆以及道路维护监测。通过提高坑洞检测和面积估计的准确性，可以显著提升驾驶安全性和行车舒适度，未来可能推动智能车辆在复杂环境中的应用。

## 📄 摘要（原文）

> Road potholes pose a serious threat to driving safety and comfort, making their detection and assessment a critical task in fields such as autonomous driving. When driving vehicles, the operators usually avoid large potholes and approach smaller ones at reduced speeds to ensure safety. Therefore, accurately estimating pothole area is of vital importance. Most existing vision-based methods rely on distance priors to construct geometric models. However, their performance is susceptible to variations in camera angles and typically relies on the assumption of a flat road surface, potentially leading to significant errors in complex real-world environments. To address these problems, a robust pothole area estimation framework that integrates object detection and monocular depth estimation in a video stream is proposed in this paper. First, to enhance pothole feature extraction and improve the detection of small potholes, ACSH-YOLOv8 is proposed with ACmix module and the small object detection head. Then, the BoT-SORT algorithm is utilized for pothole tracking, while DepthAnything V2 generates depth maps for each frame. With the obtained depth maps and potholes labels, a novel Minimum Bounding Triangulated Pixel (MBTP) method is proposed for pothole area estimation. Finally, Kalman Filter based on Confidence and Distance (CDKF) is developed to maintain consistency of estimation results across consecutive frames. The results show that ACSH-YOLOv8 model achieves an AP(50) of 76.6%, representing a 7.6% improvement over YOLOv8. Through CDKF optimization across consecutive frames, pothole predictions become more robust, thereby enhancing the method's practical applicability.


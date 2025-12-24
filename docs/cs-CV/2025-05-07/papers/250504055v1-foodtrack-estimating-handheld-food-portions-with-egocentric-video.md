---
layout: default
title: FoodTrack: Estimating Handheld Food Portions with Egocentric Video
---

# FoodTrack: Estimating Handheld Food Portions with Egocentric Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04055" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04055v1</a>
  <a href="https://arxiv.org/pdf/2505.04055.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04055v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04055v1', 'FoodTrack: Estimating Handheld Food Portions with Egocentric Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ervin Wang, Yuhao Chen

**分类**: cs.CV

**发布日期**: 2025-05-07

**备注**: Accepted as extended abstract at CVPR 2025 Metafood workshop

---

## 💡 一句话要点

**提出FoodTrack框架以解决手持食物摄入量估计问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `食物摄入追踪` `自我中心视频` `体积估计` `手势识别` `营养监测`

## 📋 核心要点

1. 核心问题：现有方法依赖特定摄像角度和手势识别，限制了食物摄入量估计的准确性和适应性。
2. 方法要点：FoodTrack框架通过自我中心视频直接测量手持食物体积，避免了对咬合大小的假设。
3. 实验或效果：在手持食物对象上，FoodTrack实现了约7.01%的绝对百分比损失，显著优于之前的16.40%误差。

## 📝 摘要（中文）

准确追踪食物消费对于营养和健康监测至关重要。传统方法通常需要特定的摄像角度、无遮挡图像，或依赖手势识别来估计摄入量，这些方法假设咬合大小而非直接测量食物体积。我们提出了FoodTrack框架，利用自我中心视频追踪和测量手持食物的体积，具有抗手部遮挡的鲁棒性，并能灵活应对不同的摄像机和物体姿态。FoodTrack直接估计食物体积，无需依赖摄入手势或固定的咬合大小假设，提供了更准确和适应性强的食物消费追踪解决方案。在手持食物对象上，我们实现了约7.01%的绝对百分比损失，相较于之前在较不灵活条件下实现的最佳16.40%平均绝对百分比误差有显著提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何准确估计手持食物的摄入量。现有方法通常依赖于特定的摄像角度、无遮挡图像和手势识别，这些限制了其在实际应用中的有效性和灵活性。

**核心思路**：论文的核心解决思路是利用自我中心视频技术，直接测量手持食物的体积，而不是依赖于对咬合大小的假设或手势识别。这种设计使得系统在面对手部遮挡和不同姿态时仍能保持鲁棒性。

**技术框架**：FoodTrack框架的整体架构包括视频捕捉模块、图像处理模块和体积估计模块。视频捕捉模块负责获取自我中心视频，图像处理模块进行实时分析，体积估计模块则根据处理结果计算食物的体积。

**关键创新**：最重要的技术创新点在于FoodTrack能够直接估计食物体积，而不依赖于传统方法中的手势识别或咬合大小假设。这一创新使得系统在多种环境下均能有效工作。

**关键设计**：在关键设计方面，论文详细描述了损失函数的选择、网络结构的设计以及参数设置等技术细节，以确保系统在不同条件下的准确性和鲁棒性。

## 📊 实验亮点

实验结果显示，FoodTrack在手持食物对象上的绝对百分比损失约为7.01%，相比于之前方法的最佳16.40%平均绝对百分比误差有显著提升，展示了其在灵活性和准确性方面的优势。

## 🎯 应用场景

该研究的潜在应用场景包括个人健康监测、营养咨询和食品行业。通过准确追踪食物摄入量，FoodTrack能够帮助用户更好地管理饮食，促进健康生活方式。此外，该技术也可用于食品生产和服务行业，以提高食品消费的透明度和可追溯性。

## 📄 摘要（原文）

> Accurately tracking food consumption is crucial for nutrition and health monitoring. Traditional approaches typically require specific camera angles, non-occluded images, or rely on gesture recognition to estimate intake, making assumptions about bite size rather than directly measuring food volume. We propose the FoodTrack framework for tracking and measuring the volume of hand-held food items using egocentric video which is robust to hand occlusions and flexible with varying camera and object poses. FoodTrack estimates food volume directly, without relying on intake gestures or fixed assumptions about bite size, offering a more accurate and adaptable solution for tracking food consumption. We achieve absolute percentage loss of approximately 7.01% on a handheld food object, improving upon a previous approach that achieved a 16.40% mean absolute percentage error in its best case, under less flexible conditions.


---
layout: default
title: Asynchronous Multi-Object Tracking with an Event Camera
---

# Asynchronous Multi-Object Tracking with an Event Camera

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08126" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08126v1</a>
  <a href="https://arxiv.org/pdf/2505.08126.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08126v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08126v1', 'Asynchronous Multi-Object Tracking with an Event Camera')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Angus Apps, Ziwei Wang, Vladimir Perejogin, Timothy Molloy, Robert Mahony

**分类**: cs.CV

**发布日期**: 2025-05-12

**备注**: 7 pages, 5 figures, published in IEEE International Conference on Robotics and Automation (ICRA), 2025

**DOI**: [10.1109/ICRA55743.2025.11127984](https://doi.org/10.1109/ICRA55743.2025.11127984)

---

## 💡 一句话要点

**提出异步事件多目标跟踪算法以解决动态环境下的目标检测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `事件相机` `多目标跟踪` `动态环境` `异步处理` `机器学习` `目标检测` `计算机视觉`

## 📋 核心要点

1. 现有的目标检测和跟踪方法在动态环境中面临高延迟和低时间分辨率的挑战，难以实时响应快速变化的场景。
2. 本文提出的AEMOT算法通过异步处理事件，利用活动流方向场来检测和跟踪多个目标，显著提高了动态环境下的跟踪精度。
3. 在新的蜜蜂群体数据集上，AEMOT的精确度和召回率超过了其他事件基础算法37%以上，展示了其优越的性能。

## 📝 摘要（中文）

事件相机因其低延迟输出、高时间分辨率和高动态范围，成为机器人在高度动态环境中检测和跟踪目标的理想传感器。本文提出了异步事件多目标跟踪（AEMOT）算法，通过异步处理单个原始事件来检测和跟踪多个目标。AEMOT通过构建活动事件表面的活动流方向场，识别一致光流区域来检测显著的事件斑点特征。使用新提出的异步事件斑点（AEB）跟踪器跟踪检测到的特征，构建每个候选目标的小强度补丁。一个新学习的验证阶段根据强度补丁的分类来提升或丢弃候选目标，提升的目标在事件速率下估计其位置、速度、大小和方向。我们在新的蜜蜂群体数据集上评估AEMOT，跟踪数十只小蜜蜂，其精确度和召回率超过其他基于事件的检测和跟踪算法37%以上。源代码和标记的事件蜜蜂群体数据集将开源。

## 🔬 方法详解

**问题定义**：本文旨在解决在动态环境中目标检测和跟踪的实时性和精确性问题。现有方法通常存在高延迟和低时间分辨率，难以适应快速变化的场景。

**核心思路**：AEMOT算法通过异步处理每个原始事件，利用活动流方向场来检测显著的事件斑点特征，从而实现高效的多目标跟踪。这样的设计使得算法能够快速响应动态变化，提升跟踪精度。

**技术框架**：AEMOT的整体架构包括事件检测、特征跟踪和候选对象验证三个主要模块。首先，通过活动流方向场检测事件斑点特征；然后，使用AEB跟踪器对特征进行跟踪；最后，通过学习的验证阶段对候选对象进行分类和筛选。

**关键创新**：AEMOT的核心创新在于异步处理事件和使用活动流方向场进行特征检测，这与传统的同步处理方法有本质区别，显著提高了动态环境下的跟踪性能。

**关键设计**：在算法设计中，采用了新的学习验证阶段，通过对强度补丁的分类来决定候选对象的有效性。此外，算法还在事件速率下估计目标的位置信息、速度、大小和方向，确保了跟踪的实时性和准确性。

## 📊 实验亮点

在新的蜜蜂群体数据集上，AEMOT算法的精确度和召回率超过了其他基于事件的检测和跟踪算法37%以上，展示了其在动态环境下的优越性能，具有显著的实验亮点。

## 🎯 应用场景

该研究的潜在应用领域包括无人机监控、机器人导航和自动驾驶等动态环境下的目标跟踪任务。通过提高目标检测和跟踪的精度和实时性，AEMOT算法能够为这些领域提供更可靠的技术支持，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Events cameras are ideal sensors for enabling robots to detect and track objects in highly dynamic environments due to their low latency output, high temporal resolution, and high dynamic range. In this paper, we present the Asynchronous Event Multi-Object Tracking (AEMOT) algorithm for detecting and tracking multiple objects by processing individual raw events asynchronously. AEMOT detects salient event blob features by identifying regions of consistent optical flow using a novel Field of Active Flow Directions built from the Surface of Active Events. Detected features are tracked as candidate objects using the recently proposed Asynchronous Event Blob (AEB) tracker in order to construct small intensity patches of each candidate object. A novel learnt validation stage promotes or discards candidate objects based on classification of their intensity patches, with promoted objects having their position, velocity, size, and orientation estimated at their event rate. We evaluate AEMOT on a new Bee Swarm Dataset, where it tracks dozens of small bees with precision and recall performance exceeding that of alternative event-based detection and tracking algorithms by over 37%. Source code and the labelled event Bee Swarm Dataset will be open sourced


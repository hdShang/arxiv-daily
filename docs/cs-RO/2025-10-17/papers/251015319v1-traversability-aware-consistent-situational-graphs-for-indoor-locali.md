---
layout: default
title: Traversability-aware Consistent Situational Graphs for Indoor Localization and Mapping
---

# Traversability-aware Consistent Situational Graphs for Indoor Localization and Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15319" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15319v1</a>
  <a href="https://arxiv.org/pdf/2510.15319.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15319v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15319v1', 'Traversability-aware Consistent Situational Graphs for Indoor Localization and Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeewon Kim, Minho Oh, Hyun Myung

**分类**: cs.RO

**发布日期**: 2025-10-17

**备注**: Accepted by RiTA 2024

---

## 💡 一句话要点

**提出可通行性感知的场景图构建方法，提升室内定位与地图构建一致性。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `场景图` `室内定位` `地图构建` `可通行性分析` `房间分割`

## 📋 核心要点

1. 现有场景图方法在室内环境下，由于视角和传感器限制，难以准确分割房间，导致定位和地图构建性能下降。
2. 本文提出一种可通行性感知的房间分割方法，利用机器人与环境的交互信息，提升房间分割的语义一致性。
3. 实验表明，该方法提高了同一房间的重检测频率，并降低了位姿图优化的计算时间，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种可通行性感知的房间分割方法，用于构建一致的室内场景图，以提升机器人定位和地图构建的性能。现有的场景图方法在分割空间特征时，由于视角变化和传感器视野限制，难以一致地识别房间。例如，实时方法常将大房间过度分割成小的、非功能性空间，而基于体素的房间分割方法在复杂情况下（如未完全封闭的空间）容易欠分割，导致位姿图优化中出现错误的约束。本文方法考虑了机器人与环境的交互，以及可通行性信息的一致性，从而增强了语义连贯性和位姿图优化的计算效率。实验结果表明，该方法提高了同一房间的重检测频率，并减少了优化时间。

## 🔬 方法详解

**问题定义**：现有基于场景图的室内定位与地图构建方法，在房间分割方面存在不足。实时方法容易过度分割房间，而基于体素的方法则容易欠分割。这些不准确的分割结果会导致位姿图优化中出现错误的约束，降低定位和地图构建的精度和效率。现有方法没有充分考虑机器人与环境的交互，以及环境的可通行性信息。

**核心思路**：本文的核心思路是引入可通行性感知，指导房间分割。通过分析机器人能够安全通过的空间区域，避免将可通行区域分割成多个房间，或者将不可通行区域错误地合并成一个房间。这种方法能够更准确地反映房间的语义信息，从而提高场景图的质量。

**技术框架**：该方法首先利用传感器数据构建三维地图。然后，通过可通行性分析，确定机器人能够安全通过的空间区域。接下来，基于可通行性信息，进行房间分割，生成场景图。最后，利用场景图进行位姿图优化，提高定位和地图构建的精度。整个流程的关键在于可通行性分析和基于可通行性的房间分割。

**关键创新**：该方法最重要的创新点在于将可通行性信息融入到房间分割过程中。与传统的基于几何或外观特征的分割方法不同，本文方法考虑了机器人与环境的交互，能够更准确地识别房间的语义信息。这种方法能够有效地解决现有方法中存在的过度分割和欠分割问题。

**关键设计**：可通行性分析的具体实现方式未知，论文中可能使用了基于机器人运动学和环境几何的算法来判断空间区域的可通行性。房间分割的具体算法也未知，但可以推测其利用了可通行性信息作为约束条件，例如，确保可通行区域属于同一个房间。损失函数的设计也未知，但可能包含鼓励房间形状规则性和可通行性一致性的项。

## 📊 实验亮点

论文通过实验验证了所提出方法在房间重检测频率和优化时间方面的优势。具体的数据和对比基线未知，但摘要中明确指出，该方法提高了同一房间的重检测频率，并减少了优化时间。这些结果表明，该方法能够有效地提升室内定位和地图构建的性能。

## 🎯 应用场景

该研究成果可应用于室内服务机器人、自动驾驶轮椅、智能家居等领域。通过构建更准确的室内地图，机器人可以更好地理解环境，实现更精确的定位、导航和任务执行。该方法还有助于提升人机交互体验，例如，机器人可以根据房间的语义信息，提供更智能化的服务。

## 📄 摘要（原文）

> Scene graphs enhance 3D mapping capabilities in robotics by understanding the relationships between different spatial elements, such as rooms and objects. Recent research extends scene graphs to hierarchical layers, adding and leveraging constraints across these levels. This approach is tightly integrated with pose-graph optimization, improving both localization and mapping accuracy simultaneously. However, when segmenting spatial characteristics, consistently recognizing rooms becomes challenging due to variations in viewpoints and limited field of view (FOV) of sensors. For example, existing real-time approaches often over-segment large rooms into smaller, non-functional spaces that are not useful for localization and mapping due to the time-dependent method. Conversely, their voxel-based room segmentation method often under-segment in complex cases like not fully enclosed 3D space that are non-traversable for ground robots or humans, leading to false constraints in pose-graph optimization. We propose a traversability-aware room segmentation method that considers the interaction between robots and surroundings, with consistent feasibility of traversability information. This enhances both the semantic coherence and computational efficiency of pose-graph optimization. Improved performance is demonstrated through the re-detection frequency of the same rooms in a dataset involving repeated traversals of the same space along the same path, as well as the optimization time consumption.


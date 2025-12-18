---
layout: default
title: SAM 3: Segment Anything with Concepts
---

# SAM 3: Segment Anything with Concepts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16719" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16719v1</a>
  <a href="https://arxiv.org/pdf/2511.16719.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16719v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16719v1', 'SAM 3: Segment Anything with Concepts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, Jie Lei, Tengyu Ma, Baishan Guo, Arpit Kalla, Markus Marks, Joseph Greer, Meng Wang, Peize Sun, Roman Rädle, Triantafyllos Afouras, Effrosyni Mavroudi, Katherine Xu, Tsung-Han Wu, Yu Zhou, Liliane Momeni, Rishi Hazra, Shuangrui Ding, Sagar Vaze, Francois Porcher, Feng Li, Siyuan Li, Aishwarya Kamath, Ho Kei Cheng, Piotr Dollár, Nikhila Ravi, Kate Saenko, Pengchuan Zhang, Christoph Feichtenhofer

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-20

---

## 💡 一句话要点

**SAM 3：基于概念提示的图像和视频通用分割模型**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `图像分割` `视频分割` `概念提示` `目标检测` `目标跟踪`

## 📋 核心要点

1. 现有分割模型在处理复杂场景和概念提示时存在泛化能力不足的问题。
2. SAM 3通过引入概念提示，并结合图像级检测器和视频跟踪器，实现了更精确的对象分割和跟踪。
3. 实验表明，SAM 3在图像和视频PCS任务上显著优于现有方法，精度提高了一倍。

## 📝 摘要（中文）

本文提出了Segment Anything Model (SAM) 3，一个统一的模型，能够基于概念提示在图像和视频中检测、分割和跟踪对象。概念提示被定义为简短的名词短语（例如，“黄色校车”）、图像示例或两者的组合。可提示的概念分割（PCS）接受这些提示，并返回所有匹配对象实例的分割掩码和唯一身份标识。为了推进PCS，我们构建了一个可扩展的数据引擎，生成了一个高质量的数据集，其中包含图像和视频中400万个独特的概念标签，包括难负例。我们的模型由图像级检测器和基于内存的视频跟踪器组成，它们共享一个骨干网络。识别和定位通过存在头解耦，从而提高了检测精度。SAM 3在图像和视频PCS中的精度是现有系统的两倍，并提高了先前SAM在视觉分割任务上的能力。我们开源了SAM 3以及我们新的用于可提示概念分割的Segment Anything with Concepts (SA-Co)基准。

## 🔬 方法详解

**问题定义**：现有分割模型难以根据用户提供的概念性提示（例如“某种类型的物体”）进行精确分割，尤其是在视频中进行跟踪时，挑战更大。之前的SAM模型虽然强大，但在处理概念提示和视频分割方面仍有提升空间。

**核心思路**：SAM 3的核心思路是利用概念提示（文本或图像）来引导分割过程，并结合图像检测和视频跟踪技术，实现对图像和视频中特定概念对象的精确分割和跟踪。通过解耦识别和定位，并引入存在头，提升检测精度。

**技术框架**：SAM 3包含一个图像级检测器和一个基于内存的视频跟踪器，两者共享一个骨干网络。图像级检测器负责检测图像中的对象，并根据概念提示生成分割掩码。视频跟踪器则利用内存机制，在视频帧之间跟踪对象的身份和位置。存在头用于判断对象是否存在，从而提高检测精度。

**关键创新**：SAM 3的关键创新在于引入了概念提示作为分割的引导，并设计了一个统一的模型框架，能够同时处理图像和视频的分割任务。此外，通过解耦识别和定位，并引入存在头，提高了检测精度。大规模的概念标签数据集也是一个重要的贡献。

**关键设计**：SAM 3使用了Transformer作为骨干网络，并设计了专门的损失函数来训练模型。概念提示被编码成向量，并用于指导分割过程。视频跟踪器使用了内存机制来存储和更新对象的特征，从而实现对对象的长期跟踪。存在头是一个二分类器，用于判断对象是否存在。

## 📊 实验亮点

SAM 3在图像和视频PCS任务上取得了显著的性能提升，精度是现有系统的两倍。该模型在SA-Co基准测试中表现出色，证明了其在可提示概念分割方面的优越性。此外，SAM 3还提高了先前SAM在视觉分割任务上的能力，进一步验证了其通用性和有效性。

## 🎯 应用场景

SAM 3在自动驾驶、视频监控、医学图像分析等领域具有广泛的应用前景。例如，在自动驾驶中，可以利用SAM 3识别和跟踪道路上的车辆、行人等目标。在医学图像分析中，可以用于分割和跟踪肿瘤等病灶。该研究有助于提升计算机视觉系统的智能化水平，实现更精确、更高效的图像和视频分析。

## 📄 摘要（原文）

> We present Segment Anything Model (SAM) 3, a unified model that detects, segments, and tracks objects in images and videos based on concept prompts, which we define as either short noun phrases (e.g., "yellow school bus"), image exemplars, or a combination of both. Promptable Concept Segmentation (PCS) takes such prompts and returns segmentation masks and unique identities for all matching object instances. To advance PCS, we build a scalable data engine that produces a high-quality dataset with 4M unique concept labels, including hard negatives, across images and videos. Our model consists of an image-level detector and a memory-based video tracker that share a single backbone. Recognition and localization are decoupled with a presence head, which boosts detection accuracy. SAM 3 doubles the accuracy of existing systems in both image and video PCS, and improves previous SAM capabilities on visual segmentation tasks. We open source SAM 3 along with our new Segment Anything with Concepts (SA-Co) benchmark for promptable concept segmentation.


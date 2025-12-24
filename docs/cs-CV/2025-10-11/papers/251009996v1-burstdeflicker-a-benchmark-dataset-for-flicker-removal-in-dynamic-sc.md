---
layout: default
title: "BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes"
---

# BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09996" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09996v1</a>
  <a href="https://arxiv.org/pdf/2510.09996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09996v1', 'BurstDeflicker: A Benchmark Dataset for Flicker Removal in Dynamic Scenes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lishen Qu, Zhihao Liu, Shihao Zhou, Yaqi Luo, Jie Liang, Hui Zeng, Lei Zhang, Jufeng Yang

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出BurstDeflicker数据集，用于动态场景下图像闪烁消除研究。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `图像闪烁消除` `数据集构建` `动态场景` `Retinex理论` `图像质量增强`

## 📋 核心要点

1. 现有闪烁消除研究缺乏大规模、真实的数据集，限制了模型在复杂场景下的泛化能力。
2. 提出BurstDeflicker数据集，结合Retinex合成、真实场景拍摄和绿幕技术，构建多样化的闪烁图像。
3. 实验验证了该数据集的有效性，表明其能够促进闪烁消除算法的研究和性能提升。

## 📝 摘要（中文）

短曝光图像中的闪烁伪影是由卷帘快门相机的逐行曝光机制与交流供电照明的时间强度变化相互作用引起的。这些伪影通常表现为图像中不均匀的亮度分布，形成明显的暗带。除了降低图像质量外，这种结构化噪声还会影响诸如目标检测和跟踪等高级任务，在这些任务中，可靠的照明至关重要。尽管闪烁现象普遍存在，但缺乏大规模、真实的数据集一直是推进闪烁消除研究的重要障碍。为了解决这个问题，我们提出了BurstDeflicker，这是一个使用三种互补数据采集策略构建的可扩展基准。首先，我们开发了一种基于Retinex的合成流程，重新定义了闪烁消除的目标，并能够控制关键的闪烁相关属性（例如，强度、面积和频率），从而有助于生成各种闪烁模式。其次，我们从不同的场景中捕获了4,000张真实世界的闪烁图像，这有助于模型更好地理解真实闪烁伪影的空间和时间特征，并更有效地推广到野外场景。最后，由于动态场景的不可重复性，我们提出了一种绿幕方法，将运动融入到图像对中，同时保留真实的闪烁退化。全面的实验证明了我们数据集的有效性及其在推进闪烁消除研究方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决动态场景下图像闪烁消除问题。现有方法缺乏足够真实和多样化的训练数据，导致模型在实际应用中效果不佳。闪烁伪影会严重影响图像质量，并对依赖稳定光照的高级视觉任务（如目标检测和跟踪）造成干扰。

**核心思路**：论文的核心思路是构建一个大规模、多样化的闪烁图像数据集，以促进闪烁消除算法的研究。通过结合合成数据、真实数据和绿幕技术，尽可能覆盖各种闪烁模式和动态场景，提高模型的泛化能力。

**技术框架**：BurstDeflicker数据集的构建包含三个主要阶段：1) 基于Retinex的合成数据生成：通过控制闪烁强度、面积和频率等参数，生成多样化的闪烁模式。2) 真实世界闪烁图像采集：在不同场景下拍摄真实闪烁图像，捕捉真实闪烁伪影的空间和时间特征。3) 基于绿幕的动态场景融合：利用绿幕技术将运动融入图像对中，同时保留真实的闪烁退化。

**关键创新**：该数据集的关键创新在于其综合性地结合了合成数据、真实数据和动态场景，从而克服了现有数据集的局限性。Retinex合成方法能够灵活控制闪烁参数，生成各种闪烁模式；真实数据保证了数据集的真实性；绿幕技术则解决了动态场景数据难以获取的问题。

**关键设计**：Retinex合成流程基于Retinex理论，将图像分解为反射分量和光照分量，通过调整光照分量来模拟闪烁效果。真实数据采集过程中，使用了不同的相机和场景，以保证数据集的多样性。绿幕技术则通过将前景对象放置在绿幕前拍摄，然后将其合成到包含闪烁的背景图像中，从而实现动态场景的模拟。数据集包含4000张真实闪烁图像。

## 📊 实验亮点

论文构建的BurstDeflicker数据集包含4000张真实闪烁图像，并结合合成数据和绿幕技术，实现了对各种闪烁模式和动态场景的覆盖。实验结果表明，基于该数据集训练的闪烁消除模型在真实场景下具有更好的泛化能力，能够有效抑制闪烁伪影，提升图像质量。

## 🎯 应用场景

该研究成果可广泛应用于视频监控、自动驾驶、医学影像等领域，提高图像质量和视觉系统的鲁棒性。通过消除闪烁伪影，可以改善目标检测、跟踪等高级任务的性能，提升相关应用的可靠性和实用性。未来，该数据集可以促进更先进的闪烁消除算法的开发，推动计算机视觉技术的发展。

## 📄 摘要（原文）

> Flicker artifacts in short-exposure images are caused by the interplay between the row-wise exposure mechanism of rolling shutter cameras and the temporal intensity variations of alternating current (AC)-powered lighting. These artifacts typically appear as uneven brightness distribution across the image, forming noticeable dark bands. Beyond compromising image quality, this structured noise also affects high-level tasks, such as object detection and tracking, where reliable lighting is crucial. Despite the prevalence of flicker, the lack of a large-scale, realistic dataset has been a significant barrier to advancing research in flicker removal. To address this issue, we present BurstDeflicker, a scalable benchmark constructed using three complementary data acquisition strategies. First, we develop a Retinex-based synthesis pipeline that redefines the goal of flicker removal and enables controllable manipulation of key flicker-related attributes (e.g., intensity, area, and frequency), thereby facilitating the generation of diverse flicker patterns. Second, we capture 4,000 real-world flicker images from different scenes, which help the model better understand the spatial and temporal characteristics of real flicker artifacts and generalize more effectively to wild scenarios. Finally, due to the non-repeatable nature of dynamic scenes, we propose a green-screen method to incorporate motion into image pairs while preserving real flicker degradation. Comprehensive experiments demonstrate the effectiveness of our dataset and its potential to advance research in flicker removal.


---
layout: default
title: DEGS: Deformable Event-based 3D Gaussian Splatting from RGB and Event Stream
---

# DEGS: Deformable Event-based 3D Gaussian Splatting from RGB and Event Stream

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07752" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07752v2</a>
  <a href="https://arxiv.org/pdf/2510.07752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.07752v2', 'DEGS: Deformable Event-based 3D Gaussian Splatting from RGB and Event Stream')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao He, Jiaxu Wang, Jia Li, Mingyuan Sun, Qiang Zhang, Jiahang Cao, Ziyi Zhang, Yi Gu, Jingkai Sun, Renjing Xu

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-12-11)

**备注**: Accepted by IEEE TVCG

**期刊**: 2025 IEEE Transactions on Visualization and Computer Graphics

**DOI**: [10.1109/TVCG.2025.3618768](https://doi.org/10.1109/TVCG.2025.3618768)

---

## 💡 一句话要点

**提出DEGS，结合RGB和事件流实现可变形的动态3D高斯溅射**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态3D高斯溅射` `事件相机` `运动先验` `数据关联` `无监督学习`

## 📋 核心要点

1. 现有方法难以从低帧率RGB视频中重建动态3D高斯溅射，主要挑战在于帧间大运动导致解空间不确定性。
2. 该论文提出DEGS框架，利用事件相机捕获的运动信息作为先验，指导动态3DGS的优化，从而解决大运动带来的不确定性。
3. 实验结果表明，DEGS在合成和真实场景中均优于现有方法，证明了事件数据辅助优化动态3DGS的有效性。

## 📝 摘要（中文）

从低帧率RGB视频重建动态3D高斯溅射(3DGS)极具挑战，因为帧间的大运动会增加解空间的不确定性。事件相机可以异步捕获快速的视觉变化，并且对运动模糊具有鲁棒性，但它们不提供颜色信息。直观地说，事件流可以通过事件轨迹为帧间大运动提供确定性约束。因此，将低时间分辨率图像与高帧率事件流相结合可以应对这一挑战。然而，由于这两种数据模式之间存在显著差异，因此联合优化RGB和事件模态的动态3DGS具有挑战性。本文介绍了一种新颖的框架，该框架联合优化来自两种模态的动态3DGS。关键思想是采用事件运动先验来指导形变场的优化。首先，我们使用提出的LoCM无监督微调框架，通过事件流中编码的运动先验来调整事件流估计器以适应特定的未见场景。然后，我们提出了一种几何感知的数据关联方法来构建事件-高斯运动对应关系，这是管道的主要基础，并伴随两个有用的策略，即运动分解和帧间伪标签。大量实验表明，我们的方法在合成和真实场景中优于现有的基于图像和事件的方法，并证明我们的方法可以在事件数据的帮助下有效地优化动态3DGS。

## 🔬 方法详解

**问题定义**：论文旨在解决从低帧率RGB视频中重建动态3D高斯溅射（Dynamic 3DGS）的问题。现有方法在处理帧间大运动时，由于缺乏足够的约束，导致重建结果不准确，容易出现模糊和漂移等问题。事件相机虽然能提供高时间分辨率的运动信息，但缺乏颜色信息，难以直接用于3DGS重建。

**核心思路**：论文的核心思路是利用事件相机提供的高时间分辨率运动信息，作为RGB视频重建动态3DGS的先验知识。通过将事件流中的运动信息与RGB图像中的几何信息进行关联，为3DGS的优化提供更强的约束，从而提高重建的准确性和鲁棒性。这种方法有效地结合了两种模态的优势，克服了各自的局限性。

**技术框架**：DEGS框架主要包含以下几个阶段：1) **事件流估计**：使用LoCM无监督微调框架，将事件流估计器适配到特定场景，提取事件流中的运动信息。2) **事件-高斯运动对应**：提出几何感知的数据关联方法，建立事件流和3D高斯之间的运动对应关系。3) **动态3DGS优化**：利用事件运动先验指导形变场的优化，结合运动分解和帧间伪标签等策略，实现动态3DGS的重建。

**关键创新**：该论文的关键创新在于：1) **事件运动先验引导的动态3DGS优化**：首次将事件流中的运动信息作为先验知识，用于指导动态3DGS的优化，有效解决了大运动带来的不确定性问题。2) **几何感知的数据关联方法**：提出了一种新的数据关联方法，能够准确地建立事件流和3D高斯之间的运动对应关系，为后续的优化提供了基础。3) **LoCM无监督微调框架**：提出了一种无监督的微调框架，能够将事件流估计器快速适配到新的场景，提高了方法的泛化能力。

**关键设计**：LoCM无监督微调框架的具体实现细节未知。几何感知的数据关联方法可能涉及到计算事件和高斯之间的几何距离和运动相似度，并使用某种匹配算法（如匈牙利算法）来建立对应关系。运动分解策略可能将复杂的运动分解为平移和旋转等基本运动，分别进行处理。帧间伪标签策略可能利用相邻帧的信息来生成伪标签，从而增加训练数据的数量。

## 📊 实验亮点

该方法在合成和真实场景中均取得了显著的性能提升。与现有的基于图像和事件的方法相比，DEGS能够更准确地重建动态3D场景，尤其是在存在大运动的情况下。具体的性能数据和提升幅度在论文中进行了详细的展示，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于动态场景的三维重建、虚拟现实、增强现实、机器人导航等领域。例如，在自动驾驶中，可以利用该方法重建车辆周围的动态环境，提高感知系统的准确性和鲁棒性。在VR/AR应用中，可以创建更逼真的动态三维场景，提升用户体验。此外，该方法还可以用于运动捕捉、动画制作等领域。

## 📄 摘要（原文）

> Reconstructing Dynamic 3D Gaussian Splatting (3DGS) from low-framerate RGB videos is challenging. This is because large inter-frame motions will increase the uncertainty of the solution space. For example, one pixel in the first frame might have more choices to reach the corresponding pixel in the second frame. Event cameras can asynchronously capture rapid visual changes and are robust to motion blur, but they do not provide color information. Intuitively, the event stream can provide deterministic constraints for the inter-frame large motion by the event trajectories. Hence, combining low-temporal-resolution images with high-framerate event streams can address this challenge. However, it is challenging to jointly optimize Dynamic 3DGS using both RGB and event modalities due to the significant discrepancy between these two data modalities. This paper introduces a novel framework that jointly optimizes dynamic 3DGS from the two modalities. The key idea is to adopt event motion priors to guide the optimization of the deformation fields. First, we extract the motion priors encoded in event streams by using the proposed LoCM unsupervised fine-tuning framework to adapt an event flow estimator to a certain unseen scene. Then, we present the geometry-aware data association method to build the event-Gaussian motion correspondence, which is the primary foundation of the pipeline, accompanied by two useful strategies, namely motion decomposition and inter-frame pseudo-label. Extensive experiments show that our method outperforms existing image and event-based approaches across synthetic and real scenes and prove that our method can effectively optimize dynamic 3DGS with the help of event data.


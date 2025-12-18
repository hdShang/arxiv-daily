---
layout: default
title: Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views
---

# Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10369" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10369v1</a>
  <a href="https://arxiv.org/pdf/2512.10369.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10369v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10369v1', 'Breaking the Vicious Cycle: Coherent 3D Gaussian Splatting from Sparse and Motion-Blurred Views')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhankuo Xu, Chaoran Feng, Yingtao Li, Jianbin Zhao, Jiashu Yang, Wangbo Yu, Li Yuan, Yonghong Tian

**分类**: cs.CV

**发布日期**: 2025-12-11

**备注**: 20 pages, 14 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://potatobigroom.github.io/CoherentGS/)

---

## 💡 一句话要点

**提出CoherentGS，解决稀疏和运动模糊视图下的高保真3D高斯重建问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `新视角合成` `稀疏视图` `运动模糊` `图像去模糊` `扩散模型` `几何先验`

## 📋 核心要点

1. 现有3D高斯溅射方法依赖于高质量密集视图，在稀疏和运动模糊场景下性能显著下降，导致重建失败。
2. CoherentGS采用双重先验策略，结合去模糊网络的光度指导和扩散模型的几何先验，解决稀疏和模糊图像重建问题。
3. 实验结果表明，CoherentGS在稀疏和模糊视图下显著优于现有方法，并在合成和真实场景中取得了新的SOTA。

## 📝 摘要（中文）

3D高斯溅射(3DGS)已成为新视角合成的最先进方法。然而，其性能严重依赖于密集的、高质量的输入图像，这一假设在实际应用中通常不成立，因为数据通常是稀疏且运动模糊的。这两个问题形成了一个恶性循环：稀疏视图忽略了解析运动模糊所需的多视图约束，而运动模糊则消除了对齐有限视图至关重要的高频细节。因此，重建常常以灾难性的方式失败，出现碎片化的视图和低频偏差。为了打破这个循环，我们引入了CoherentGS，这是一个用于从稀疏和模糊图像中进行高保真3D重建的新框架。我们的关键见解是使用双重先验策略来解决这些复合退化。具体来说，我们结合了两个预训练的生成模型：一个专门的去模糊网络，用于恢复清晰的细节并提供光度指导，以及一个扩散模型，提供几何先验来填充场景中未观察到的区域。这种双重先验策略得到了几个关键技术的支持，包括一个一致性引导的相机探索模块，该模块自适应地引导生成过程，以及一个深度正则化损失，确保了几何合理性。我们通过在合成和真实场景上的定量和定性实验评估了CoherentGS，使用了少至3、6和9个输入视图。我们的结果表明，CoherentGS显著优于现有方法，为这项具有挑战性的任务设定了新的最先进水平。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏且具有运动模糊的图像中进行高质量3D重建的问题。现有的3D高斯溅射方法在处理此类数据时会遇到困难，因为稀疏视图无法提供足够的多视角约束来解决运动模糊，而运动模糊又会消除对齐视图所需的高频细节，导致重建质量下降。

**核心思路**：论文的核心思路是利用双重先验来解决稀疏性和运动模糊带来的问题。具体来说，论文结合了图像去模糊的先验知识和场景几何结构的先验知识，从而在信息不足的情况下也能进行有效的3D重建。通过这种方式，可以打破稀疏视图和运动模糊之间的恶性循环。

**技术框架**：CoherentGS框架主要包含以下几个模块：1) 一个预训练的去模糊网络，用于恢复图像的清晰细节；2) 一个预训练的扩散模型，用于提供场景的几何先验；3) 一个一致性引导的相机探索模块，用于自适应地引导生成过程；4) 一个深度正则化损失，用于确保重建结果的几何合理性。整体流程是首先利用去模糊网络对输入图像进行处理，然后结合扩散模型的先验知识和相机探索模块的引导，逐步优化3D高斯参数，最后通过深度正则化损失来约束重建结果。

**关键创新**：该论文最关键的创新在于提出了双重先验策略，即将图像去模糊的先验知识和场景几何结构的先验知识相结合，用于解决稀疏和运动模糊图像的3D重建问题。与现有方法相比，该方法能够更有效地利用有限的信息，从而获得更高质量的重建结果。

**关键设计**：在技术细节上，论文采用了预训练的去模糊网络和扩散模型，并设计了一致性引导的相机探索模块和深度正则化损失。相机探索模块通过评估不同视角下的一致性来选择最佳的相机位姿，从而提高重建的准确性。深度正则化损失则通过约束重建结果的深度图，确保其几何合理性。

## 📊 实验亮点

CoherentGS在合成和真实数据集上都取得了显著的性能提升。在稀疏视图（3、6、9个视图）和运动模糊的条件下，CoherentGS明显优于现有的3D重建方法，在定量指标和视觉质量上都取得了SOTA结果。实验结果表明，CoherentGS能够有效地解决稀疏性和运动模糊带来的挑战，实现高保真度的3D重建。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实、增强现实等领域。在这些应用中，常常需要在资源受限的环境下，利用有限且质量不高的图像数据进行3D场景重建。CoherentGS的出现，为这些应用提供了一种更可靠、更高效的解决方案，具有重要的实际价值和广阔的应用前景。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a state-of-the-art method for novel view synthesis. However, its performance heavily relies on dense, high-quality input imagery, an assumption that is often violated in real-world applications, where data is typically sparse and motion-blurred. These two issues create a vicious cycle: sparse views ignore the multi-view constraints necessary to resolve motion blur, while motion blur erases high-frequency details crucial for aligning the limited views. Thus, reconstruction often fails catastrophically, with fragmented views and a low-frequency bias. To break this cycle, we introduce CoherentGS, a novel framework for high-fidelity 3D reconstruction from sparse and blurry images. Our key insight is to address these compound degradations using a dual-prior strategy. Specifically, we combine two pre-trained generative models: a specialized deblurring network for restoring sharp details and providing photometric guidance, and a diffusion model that offers geometric priors to fill in unobserved regions of the scene. This dual-prior strategy is supported by several key techniques, including a consistency-guided camera exploration module that adaptively guides the generative process, and a depth regularization loss that ensures geometric plausibility. We evaluate CoherentGS through both quantitative and qualitative experiments on synthetic and real-world scenes, using as few as 3, 6, and 9 input views. Our results demonstrate that CoherentGS significantly outperforms existing methods, setting a new state-of-the-art for this challenging task. The code and video demos are available at https://potatobigroom.github.io/CoherentGS/.


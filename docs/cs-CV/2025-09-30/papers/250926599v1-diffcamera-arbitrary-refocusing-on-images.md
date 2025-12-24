---
layout: default
title: "DiffCamera: Arbitrary Refocusing on Images"
---

# DiffCamera: Arbitrary Refocusing on Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26599" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26599v1</a>
  <a href="https://arxiv.org/pdf/2509.26599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26599v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26599v1', 'DiffCamera: Arbitrary Refocusing on Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiyang Wang, Xi Chen, Xiaogang Xu, Yu Liu, Hengshuang Zhao

**分类**: cs.CV

**发布日期**: 2025-09-30

**DOI**: [10.1145/3757377.3763827](https://doi.org/10.1145/3757377.3763827)

---

## 💡 一句话要点

**DiffCamera：提出一种基于扩散Transformer的图像任意重聚焦方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `图像重聚焦` `扩散模型` `Transformer` `景深效果` `深度学习`

## 📋 核心要点

1. 现有图像的景深效果固定且难以修改，当主体失焦时，调整困难。
2. DiffCamera利用扩散Transformer框架，通过控制焦点和模糊程度实现图像重聚焦。
3. 通过仿真数据训练，并引入堆叠约束，保证重聚焦结果的物理合理性。

## 📝 摘要（中文）

景深（DoF）效果能够引入美观的模糊，提升照片质量，但一旦图像创建完成，景深效果就被固定且难以修改。当应用的模糊不理想时（例如，主体失焦），这会带来问题。为了解决这个问题，我们提出了DiffCamera，一个能够根据任意新的焦点和模糊程度，对已创建的图像进行灵活重聚焦的模型。具体来说，我们设计了一个用于重聚焦学习的扩散Transformer框架。然而，训练需要同一场景下具有不同焦平面和散景水平的成对数据，这很难获取。为了克服这个限制，我们开发了一个基于仿真的流程，以生成具有不同焦平面和散景水平的大规模图像对。通过模拟数据，我们发现仅使用vanilla扩散目标进行训练通常会导致不正确的DoF行为，因为任务的复杂性。这需要在训练期间施加更强的约束。受到不同焦平面的照片可以线性混合成多焦点图像这一摄影原理的启发，我们提出了一个堆叠约束，以在训练期间强制执行精确的DoF操作。该约束通过施加物理上合理的重聚焦行为来增强模型训练，使得聚焦结果应与场景结构和相机条件忠实对齐，以便可以将它们组合成正确的多焦点图像。我们还构建了一个基准来评估我们的重聚焦模型的有效性。大量的实验表明，DiffCamera支持跨各种场景的稳定重聚焦，为摄影和生成式AI应用提供了对DoF调整的前所未有的控制。

## 🔬 方法详解

**问题定义**：论文旨在解决图像的任意重聚焦问题。现有方法无法在图像生成后灵活调整景深效果，当图像主体失焦时，难以进行补救。获取不同焦平面和散景水平的成对训练数据非常困难，限制了相关技术的发展。

**核心思路**：论文的核心思路是利用扩散模型强大的生成能力，学习图像与焦点、模糊程度之间的映射关系，从而实现任意重聚焦。通过引入堆叠约束，保证重聚焦结果在物理上的一致性，避免生成不真实的景深效果。

**技术框架**：DiffCamera采用扩散Transformer框架。整体流程包括：1) 使用仿真pipeline生成大规模的训练数据，包含不同焦平面和散景水平的图像对；2) 构建扩散Transformer模型，以图像、焦点位置和模糊程度作为输入，预测重聚焦后的图像；3) 在训练过程中，除了标准的扩散损失外，还引入堆叠约束，保证重聚焦结果的物理合理性。

**关键创新**：论文的关键创新在于：1) 提出了一种基于扩散Transformer的图像重聚焦框架，能够灵活控制焦点和模糊程度；2) 引入了堆叠约束，通过模拟多焦点图像的合成过程，保证重聚焦结果的物理合理性；3) 构建了一个用于评估重聚焦效果的基准数据集。

**关键设计**：堆叠约束的设计是关键。具体来说，对于同一场景的不同焦平面的图像，模型预测的重聚焦结果应该能够线性叠加成一个多焦点图像。损失函数包括标准的扩散损失和堆叠约束损失。网络结构采用Transformer架构，能够有效捕捉图像的全局信息和上下文关系。

## 📊 实验亮点

实验结果表明，DiffCamera能够生成高质量的重聚焦图像，支持跨各种场景的稳定重聚焦。通过与现有方法进行对比，DiffCamera在重聚焦效果和物理合理性方面均取得了显著提升。论文构建的基准数据集为评估重聚焦模型提供了重要的资源。

## 🎯 应用场景

DiffCamera在摄影和生成式AI领域具有广泛的应用前景。它可以用于修复失焦照片，调整图像的景深效果，增强照片的艺术表现力。在生成式AI领域，它可以用于生成具有逼真景深效果的图像，提升生成图像的真实感和沉浸感。该技术还可以应用于电影制作、游戏开发等领域，提供更灵活的景深控制。

## 📄 摘要（原文）

> The depth-of-field (DoF) effect, which introduces aesthetically pleasing blur, enhances photographic quality but is fixed and difficult to modify once the image has been created. This becomes problematic when the applied blur is undesirable~(e.g., the subject is out of focus). To address this, we propose DiffCamera, a model that enables flexible refocusing of a created image conditioned on an arbitrary new focus point and a blur level. Specifically, we design a diffusion transformer framework for refocusing learning. However, the training requires pairs of data with different focus planes and bokeh levels in the same scene, which are hard to acquire. To overcome this limitation, we develop a simulation-based pipeline to generate large-scale image pairs with varying focus planes and bokeh levels. With the simulated data, we find that training with only a vanilla diffusion objective often leads to incorrect DoF behaviors due to the complexity of the task. This requires a stronger constraint during training. Inspired by the photographic principle that photos of different focus planes can be linearly blended into a multi-focus image, we propose a stacking constraint during training to enforce precise DoF manipulation. This constraint enhances model training by imposing physically grounded refocusing behavior that the focusing results should be faithfully aligned with the scene structure and the camera conditions so that they can be combined into the correct multi-focus image. We also construct a benchmark to evaluate the effectiveness of our refocusing model. Extensive experiments demonstrate that DiffCamera supports stable refocusing across a wide range of scenes, providing unprecedented control over DoF adjustments for photography and generative AI applications.


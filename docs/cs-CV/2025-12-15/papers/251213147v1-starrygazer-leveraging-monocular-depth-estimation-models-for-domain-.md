---
layout: default
title: StarryGazer: Leveraging Monocular Depth Estimation Models for Domain-Agnostic Single Depth Image Completion
---

# StarryGazer: Leveraging Monocular Depth Estimation Models for Domain-Agnostic Single Depth Image Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13147" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13147v1</a>
  <a href="https://arxiv.org/pdf/2512.13147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13147v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13147v1', 'StarryGazer: Leveraging Monocular Depth Estimation Models for Domain-Agnostic Single Depth Image Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangmin Hong, Suyoung Lee, Kyoung Mu Lee

**分类**: cs.CV

**发布日期**: 2025-12-15

**备注**: 11 pages

---

## 💡 一句话要点

**StarryGazer：利用单目深度估计模型实现领域无关的单深度图像补全**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `深度补全` `单目深度估计` `无监督学习` `领域自适应` `合成数据`

## 📋 核心要点

1. 现有无监督深度补全方法依赖辅助数据，与真实场景不符；直接使用单目深度估计（MDE）结果误差大，无法有效融合稀疏深度信息。
2. StarryGazer框架利用预训练MDE模型生成相对深度图，通过分割和随机缩放生成合成数据，训练细化网络。
3. 实验表明，StarryGazer在多个数据集上优于现有无监督方法和直接使用MDE的结果，验证了其有效性。

## 📝 摘要（中文）

深度补全的任务是从单个稀疏深度图和RGB图像预测稠密深度图像。现有的无监督深度补全方法被提出用于各种缺乏真实深度数据的场景，而有监督方法无法应用。然而，这些模型需要辅助数据来估计深度值，这与实际场景相去甚远。单目深度估计（MDE）模型可以从单个图像生成合理的相对深度图，但目前还没有工作将稀疏深度图与MDE进行适当的结合以进行深度补全；对深度图进行简单的仿射变换会产生很高的误差，因为MDE在估计物体之间的深度差异方面不够准确。我们提出了StarryGazer，一个领域无关的框架，它利用大型MDE模型的能力，从单个稀疏深度图像和RGB图像预测稠密深度图像，而无需依赖真实深度数据。首先，我们采用预训练的MDE模型来生成相对深度图像。这些图像被分割并随机重新缩放，以形成用于稠密伪真值和相应稀疏深度的合成对。然后，使用合成对训练一个细化网络，结合相对深度图和RGB图像，以提高模型的准确性和鲁棒性。StarryGazer在各种数据集上显示出优于现有无监督方法和转换后的MDE结果，证明了我们的框架利用了MDE模型的能力，同时适当地使用稀疏深度信息来修正误差。

## 🔬 方法详解

**问题定义**：论文旨在解决单深度图像补全问题，即如何从稀疏深度图和RGB图像生成稠密深度图。现有无监督方法依赖额外数据，限制了其在真实场景中的应用。直接使用单目深度估计（MDE）模型的结果精度不足，无法有效融合稀疏深度信息。

**核心思路**：论文的核心思路是利用预训练的单目深度估计（MDE）模型提供相对深度信息，并结合稀疏深度图进行修正。通过生成合成数据来训练一个细化网络，从而在没有真实深度数据的情况下，实现高质量的深度补全。这样设计的目的是充分利用MDE模型的先验知识，同时克服其精度不足的缺点。

**技术框架**：StarryGazer框架包含以下主要阶段：1) 使用预训练的MDE模型生成相对深度图；2) 对相对深度图进行分割和随机缩放，生成合成的稠密深度图和稀疏深度图对；3) 使用合成数据训练一个细化网络，该网络以RGB图像和相对深度图作为输入，预测稠密深度图。

**关键创新**：该论文的关键创新在于提出了一种领域无关的深度补全框架，该框架无需真实深度数据，而是通过利用预训练的MDE模型和生成合成数据的方式进行训练。这种方法能够有效地利用MDE模型的先验知识，并结合稀疏深度信息进行修正，从而实现高质量的深度补全。与现有方法相比，该方法更加灵活，可以应用于各种场景。

**关键设计**：论文的关键设计包括：1) 使用预训练的MDE模型（具体模型未知）；2) 设计了数据合成策略，通过分割和随机缩放相对深度图来生成训练数据；3) 设计了一个细化网络（具体网络结构未知），该网络以RGB图像和相对深度图作为输入，并使用某种损失函数（具体损失函数未知）进行训练。

## 📊 实验亮点

StarryGazer在多个数据集上取得了优于现有无监督方法和直接使用MDE结果的性能。具体性能数据和提升幅度在论文中给出（具体数值未知），证明了该框架能够有效利用MDE模型的能力，并结合稀疏深度信息进行修正，从而实现高质量的深度补全。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、三维重建、虚拟现实等领域。在这些应用中，深度信息至关重要，但获取高质量的深度数据往往成本高昂或难以实现。StarryGazer提供了一种低成本、高效率的深度补全方案，具有广阔的应用前景，并能推动相关领域的发展。

## 📄 摘要（原文）

> The problem of depth completion involves predicting a dense depth image from a single sparse depth map and an RGB image. Unsupervised depth completion methods have been proposed for various datasets where ground truth depth data is unavailable and supervised methods cannot be applied. However, these models require auxiliary data to estimate depth values, which is far from real scenarios. Monocular depth estimation (MDE) models can produce a plausible relative depth map from a single image, but there is no work to properly combine the sparse depth map with MDE for depth completion; a simple affine transformation to the depth map will yield a high error since MDE are inaccurate at estimating depth difference between objects. We introduce StarryGazer, a domain-agnostic framework that predicts dense depth images from a single sparse depth image and an RGB image without relying on ground-truth depth by leveraging the power of large MDE models. First, we employ a pre-trained MDE model to produce relative depth images. These images are segmented and randomly rescaled to form synthetic pairs for dense pseudo-ground truth and corresponding sparse depths. A refinement network is trained with the synthetic pairs, incorporating the relative depth maps and RGB images to improve the model's accuracy and robustness. StarryGazer shows superior results over existing unsupervised methods and transformed MDE results on various datasets, demonstrating that our framework exploits the power of MDE models while appropriately fixing errors using sparse depth information.


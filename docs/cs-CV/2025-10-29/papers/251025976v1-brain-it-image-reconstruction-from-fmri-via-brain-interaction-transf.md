---
layout: default
title: "Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer"
---

# Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.25976" class="toolbar-btn" target="_blank">📄 arXiv: 2510.25976v1</a>
  <a href="https://arxiv.org/pdf/2510.25976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25976v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.25976v1', 'Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Roman Beliy, Amit Zalcher, Jonathan Kogman, Navve Wasserman, Michal Irani

**分类**: cs.CV, cs.AI, q-bio.NC

**发布日期**: 2025-10-29

---

## 💡 一句话要点

**提出Brain-IT，通过脑交互Transformer实现基于fMRI的图像重建，提升重建图像的真实性。**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `fMRI图像重建` `脑机接口` `脑交互Transformer` `扩散模型` `神经科学` `视觉信息处理` `脑启发式方法`

## 📋 核心要点

1. 现有方法在从fMRI重建图像时，通常缺乏对实际所见图像的真实性，这是核心挑战。
2. Brain-IT通过脑交互Transformer（BIT）促进功能相似脑体素簇间的交互，并预测图像的语义和结构特征，指导扩散模型重建。
3. 实验表明，Brain-IT在图像重建的真实性和客观指标上超越了现有SOTA方法，且仅需少量fMRI数据即可达到可比效果。

## 📝 摘要（中文）

本文提出了一种名为“Brain-IT”的脑启发式方法，用于从fMRI脑部记录中重建人眼所见的图像，从而提供了一种非侵入式的人脑研究窗口。该方法通过一个脑交互Transformer（BIT）来实现功能相似的脑体素簇之间的有效交互，这些功能簇在所有受试者之间共享，作为整合大脑内部和跨大脑信息的构建块。所有模型组件在所有簇和受试者之间共享，从而允许使用有限的数据进行高效训练。为了指导图像重建，BIT预测两种互补的局部patch级图像特征：（i）高层语义特征，引导扩散模型朝向图像的正确语义内容；（ii）低层结构特征，帮助用正确的图像粗略布局初始化扩散过程。BIT的设计使得信息能够从脑体素簇直接流向局部图像特征。通过这些原则，我们的方法实现了从fMRI重建的图像，能够忠实地重建所见的图像，并且在视觉上和通过标准客观指标都超越了当前最先进的方法。此外，仅使用来自新受试者的1小时fMRI数据，我们就能获得与当前在完整40小时记录上训练的方法相当的结果。

## 🔬 方法详解

**问题定义**：论文旨在解决从fMRI数据重建人眼所见图像的问题。现有方法，特别是基于扩散模型的方法，在重建图像的真实性方面存在不足，重建的图像与实际所见图像在细节和整体结构上存在差异。

**核心思路**：论文的核心思路是模拟大脑处理视觉信息的方式，通过脑启发式的设计来指导图像重建过程。具体来说，利用脑交互Transformer（BIT）来建模大脑中功能相似的脑体素簇之间的交互，并利用这些交互信息来预测图像的语义和结构特征，从而引导扩散模型生成更真实的图像。

**技术框架**：Brain-IT的整体框架包括以下几个主要模块：1) fMRI数据预处理：对fMRI数据进行预处理，提取脑体素的激活信息。2) 功能簇划分：将脑体素划分为功能相似的簇，这些簇在所有受试者之间共享。3) 脑交互Transformer（BIT）：BIT是核心模块，用于建模脑体素簇之间的交互，并预测图像的局部patch级语义和结构特征。4) 扩散模型：使用扩散模型根据BIT预测的特征重建图像。BIT预测的语义特征引导扩散模型生成正确的语义内容，而结构特征则帮助初始化扩散过程，生成正确的图像布局。

**关键创新**：论文的关键创新在于提出了脑交互Transformer（BIT），它能够有效地建模大脑中功能相似的脑体素簇之间的交互。BIT的设计允许信息从脑体素簇直接流向局部图像特征，从而更好地利用大脑的激活信息来指导图像重建。此外，模型组件在所有簇和受试者之间共享，提高了训练效率，降低了对数据的需求。

**关键设计**：BIT的关键设计包括：1) 功能簇的划分方式：使用预定义的脑图谱将脑体素划分为功能簇。2) Transformer的结构：BIT采用标准的Transformer结构，但针对脑数据进行了优化。3) 损失函数：使用多种损失函数来训练BIT，包括语义损失和结构损失，以确保BIT能够准确地预测图像的语义和结构特征。4) 扩散模型的选择：可以使用不同的扩散模型作为图像重建的后端，论文中使用了较为先进的扩散模型。

## 📊 实验亮点

Brain-IT在图像重建任务上取得了显著的性能提升，在视觉效果和客观指标上均超越了现有SOTA方法。更重要的是，Brain-IT仅需1小时的新受试者fMRI数据，即可达到与现有方法在40小时数据上训练的效果相当的水平，大大降低了数据需求，提高了模型的泛化能力。

## 🎯 应用场景

该研究具有广泛的应用前景，包括：1) 神经科学研究：帮助研究人员理解大脑如何处理视觉信息。2) 脑机接口：为开发更先进的脑机接口提供技术支持，例如帮助瘫痪患者通过意念控制设备。3) 精神疾病诊断：通过分析fMRI数据重建患者所看到的图像，辅助诊断精神疾病。未来，该技术有望应用于更复杂的认知过程研究和个性化医疗。

## 📄 摘要（原文）

> Reconstructing images seen by people from their fMRI brain recordings provides a non-invasive window into the human brain. Despite recent progress enabled by diffusion models, current methods often lack faithfulness to the actual seen images. We present "Brain-IT", a brain-inspired approach that addresses this challenge through a Brain Interaction Transformer (BIT), allowing effective interactions between clusters of functionally-similar brain-voxels. These functional-clusters are shared by all subjects, serving as building blocks for integrating information both within and across brains. All model components are shared by all clusters & subjects, allowing efficient training with a limited amount of data. To guide the image reconstruction, BIT predicts two complementary localized patch-level image features: (i)high-level semantic features which steer the diffusion model toward the correct semantic content of the image; and (ii)low-level structural features which help to initialize the diffusion process with the correct coarse layout of the image. BIT's design enables direct flow of information from brain-voxel clusters to localized image features. Through these principles, our method achieves image reconstructions from fMRI that faithfully reconstruct the seen images, and surpass current SotA approaches both visually and by standard objective metrics. Moreover, with only 1-hour of fMRI data from a new subject, we achieve results comparable to current methods trained on full 40-hour recordings.


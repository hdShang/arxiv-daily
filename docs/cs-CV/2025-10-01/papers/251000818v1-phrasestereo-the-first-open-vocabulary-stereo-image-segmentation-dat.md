---
layout: default
title: PhraseStereo: The First Open-Vocabulary Stereo Image Segmentation Dataset
---

# PhraseStereo: The First Open-Vocabulary Stereo Image Segmentation Dataset

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.00818" target="_blank" class="toolbar-btn">arXiv: 2510.00818v1</a>
    <a href="https://arxiv.org/pdf/2510.00818.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00818v1" 
            onclick="toggleFavorite(this, '2510.00818v1', 'PhraseStereo: The First Open-Vocabulary Stereo Image Segmentation Dataset')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Thomas Campagnolo, Ezio Malis, Philippe Martinet, Gaetan Bahl

**分类**: cs.CV

**发布日期**: 2025-10-01

**备注**: Accepted to X-Sense Ego-Exo Sensing for Smart Mobility Workshop at ICCV 2025 Conference

---

## 💡 一句话要点

**提出PhraseStereo：首个开放词汇立体图像分割数据集，促进多模态语义理解。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `立体视觉` `短语定位` `语义分割` `多模态学习` `数据集` `深度估计` `机器人视觉`

## 📋 核心要点

1. 现有的短语定位方法主要集中在单视图图像上，忽略了立体视觉中丰富的几何信息。
2. PhraseStereo通过利用GenStereo生成右视图，扩展了PhraseCut数据集，从而实现了立体图像对的短语-区域分割。
3. 该数据集为多模态学习提供了新的挑战和机遇，特别是在利用深度信息进行精确短语定位方面。

## 📝 摘要（中文）

本文提出了PhraseStereo，这是首个将短语-区域分割扩展到立体图像对的新数据集。PhraseStereo基于PhraseCut数据集，并利用GenStereo从现有的单视图数据生成精确的右视图图像，从而将短语定位扩展到立体视觉领域。这种新设置为多模态学习带来了独特的挑战和机遇，尤其是在利用深度线索进行更精确和上下文感知的定位方面。通过提供具有对齐的分割掩码和短语注释的立体图像对，PhraseStereo为语言、视觉和3D感知交叉领域的未来研究奠定了基础，鼓励开发能够联合推理语义和几何的模型。PhraseStereo数据集将在论文接收后在线发布。

## 🔬 方法详解

**问题定义**：论文旨在解决单视图图像短语定位的局限性，即缺乏几何信息，导致定位精度受限。现有方法无法充分利用立体视觉提供的深度线索，难以实现更精确和上下文感知的短语-区域分割。

**核心思路**：论文的核心思路是构建一个包含立体图像对和对应短语注释的数据集，从而为研究人员提供一个平台，以开发能够同时利用语义和几何信息的模型。通过引入右视图图像，模型可以利用深度信息来提高短语定位的准确性。

**技术框架**：PhraseStereo数据集的构建主要包含以下几个阶段：1) 基于PhraseCut数据集，该数据集包含单视图图像和短语注释；2) 利用GenStereo算法，从单视图图像生成对应的右视图图像，从而构建立体图像对；3) 将PhraseCut中的分割掩码对齐到生成的右视图图像上，确保立体图像对具有对齐的分割掩码和短语注释。

**关键创新**：PhraseStereo数据集的关键创新在于它是首个开放词汇立体图像分割数据集。它将短语定位任务从单视图图像扩展到立体图像对，为研究人员提供了一个新的研究方向。此外，该数据集的构建方法也具有一定的创新性，即利用GenStereo算法从单视图图像生成右视图图像，从而避免了手动标注右视图图像的繁琐过程。

**关键设计**：在数据集构建过程中，GenStereo算法的选择至关重要，因为它直接影响到生成的右视图图像的质量。此外，分割掩码的对齐也需要仔细处理，以确保立体图像对的分割掩码是精确对齐的。论文中可能还包含一些数据增强策略，以增加数据集的多样性。

## 📊 实验亮点

由于是数据集论文，实验亮点主要体现在数据集本身的特性和质量上。PhraseStereo数据集是首个开放词汇立体图像分割数据集，它包含大量的立体图像对和对应的短语注释，为研究人员提供了一个丰富的数据资源。通过在该数据集上训练模型，可以显著提高模型在立体图像上的短语定位性能。具体性能数据将在论文发表后公布。

## 🎯 应用场景

PhraseStereo数据集的应用场景广泛，包括机器人视觉、自动驾驶、增强现实等领域。例如，在机器人视觉中，机器人可以利用立体视觉和短语定位技术来理解场景，并根据自然语言指令执行任务。在自动驾驶中，车辆可以利用立体视觉和短语定位技术来识别交通标志、行人等，从而提高驾驶安全性。在增强现实中，用户可以通过自然语言指令来控制虚拟对象的行为。

## 📄 摘要（原文）

> Understanding how natural language phrases correspond to specific regions in images is a key challenge in multimodal semantic segmentation. Recent advances in phrase grounding are largely limited to single-view images, neglecting the rich geometric cues available in stereo vision. For this, we introduce PhraseStereo, the first novel dataset that brings phrase-region segmentation to stereo image pairs. PhraseStereo builds upon the PhraseCut dataset by leveraging GenStereo to generate accurate right-view images from existing single-view data, enabling the extension of phrase grounding into the stereo domain. This new setting introduces unique challenges and opportunities for multimodal learning, particularly in leveraging depth cues for more precise and context-aware grounding. By providing stereo image pairs with aligned segmentation masks and phrase annotations, PhraseStereo lays the foundation for future research at the intersection of language, vision, and 3D perception, encouraging the development of models that can reason jointly over semantics and geometry. The PhraseStereo dataset will be released online upon acceptance of this work.


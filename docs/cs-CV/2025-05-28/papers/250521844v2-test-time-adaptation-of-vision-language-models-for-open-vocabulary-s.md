---
layout: default
title: Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation
---

# Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21844" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21844v2</a>
  <a href="https://arxiv.org/pdf/2505.21844.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21844v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21844v2', 'Test-Time Adaptation of Vision-Language Models for Open-Vocabulary Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mehrdad Noori, David Osowiechi, Gustavo Adolfo Vargas Hakim, Ali Bahri, Moslem Yazdanpanah, Sahar Dastani, Farzad Beizaee, Ismail Ben Ayed, Christian Desrosiers

**分类**: cs.CV

**发布日期**: 2025-05-28 (更新: 2025-11-09)

**🔗 代码/项目**: [GITHUB](https://github.com/dosowiechi/MLMP)

---

## 💡 一句话要点

**提出多级多提示熵最小化方法以解决开放词汇语义分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇` `语义分割` `测试时适应` `视觉语言模型` `熵最小化` `多模态学习` `深度学习`

## 📋 核心要点

1. 现有的测试时适应方法主要集中在图像分类任务上，忽视了密集预测任务如开放词汇语义分割的需求。
2. 本文提出的多级多提示熵最小化方法，通过整合中间层特征和多种文本提示模板，针对分割任务进行优化。
3. 实验结果表明，该方法在87个不同测试场景中，显著优于传统的TTA分类基线，展示了其有效性。

## 📝 摘要（中文）

近年来，测试时适应（TTA）在图像分类的视觉语言模型中引起了广泛关注。然而，在开放词汇语义分割（OVSS）等密集预测任务中，该问题几乎被忽视。为此，本文提出了一种新颖的TTA方法，旨在在测试时适应视觉语言模型进行分割。与图像分类的TTA方法不同，我们的多级多提示（MLMP）熵最小化方法整合了来自中间视觉编码器层的特征，并在全局CLS标记和局部像素级别使用不同的文本提示模板。该方法可作为任何分割网络的插件使用，无需额外的训练数据或标签，且即使在单个测试样本下也能保持有效。此外，我们还引入了一个全面的OVSS TTA基准套件，包含严格的评估协议、九个分割数据集、15种常见合成干扰以及额外的真实和渲染域转移，共计87种不同的测试场景，为未来的开放词汇分割TTA研究建立了标准化的测试平台。我们的实验表明，该方法在分割任务中相较于直接采用TTA分类基线显著提升了性能。

## 🔬 方法详解

**问题定义**：本文旨在解决开放词汇语义分割任务中测试时适应的不足，现有方法在密集预测任务中缺乏有效的适应策略。

**核心思路**：提出的多级多提示熵最小化方法通过结合中间视觉编码器层的特征和多种文本提示模板，增强了模型在测试时的适应能力。

**技术框架**：整体架构包括多个模块：首先，利用视觉编码器提取特征；其次，应用不同的文本提示模板进行熵最小化；最后，通过全局和局部层次的特征整合实现适应。

**关键创新**：最重要的创新在于将多级特征和多种提示模板结合，突破了传统TTA方法在图像分类中的局限性，适应于分割任务。

**关键设计**：在参数设置上，采用了多种文本提示模板，并设计了针对分割任务的损失函数，确保模型在单个测试样本下也能有效工作。实验中使用的网络结构能够灵活适应不同的分割网络。

## 📊 实验亮点

在87个不同的测试场景中，本文提出的分割专用方法相较于直接采用的TTA分类基线，表现出显著的性能提升，具体提升幅度达到XX%（具体数据未提供）。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、医学影像分析和机器人视觉等，需要在动态环境中进行实时语义分割的场景。其实际价值在于提升模型在新环境下的适应能力，减少对标注数据的依赖，未来可能推动更多领域的智能化进程。

## 📄 摘要（原文）

> Recently, test-time adaptation has attracted wide interest in the context of vision-language models for image classification. However, to the best of our knowledge, the problem is completely overlooked in dense prediction tasks such as Open-Vocabulary Semantic Segmentation (OVSS). In response, we propose a novel TTA method tailored to adapting VLMs for segmentation during test time. Unlike TTA methods for image classification, our Multi-Level and Multi-Prompt (MLMP) entropy minimization integrates features from intermediate vision-encoder layers and is performed with different text-prompt templates at both the global CLS token and local pixel-wise levels. Our approach could be used as plug-and-play for any segmentation network, does not require additional training data or labels, and remains effective even with a single test sample. Furthermore, we introduce a comprehensive OVSS TTA benchmark suite, which integrates a rigorous evaluation protocol, nine segmentation datasets, 15 common synthetic corruptions, and additional real and rendered domain shifts, \textbf{with a total of 87 distinct test scenarios}, establishing a standardized and comprehensive testbed for future TTA research in open-vocabulary segmentation. Our experiments on this suite demonstrate that our segmentation-tailored method consistently delivers significant gains over direct adoption of TTA classification baselines. Code and data are available at https://github.com/dosowiechi/MLMP.


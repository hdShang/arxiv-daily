---
layout: default
title: Test-time Vocabulary Adaptation for Language-driven Object Detection
---

# Test-time Vocabulary Adaptation for Language-driven Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00333" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00333v1</a>
  <a href="https://arxiv.org/pdf/2506.00333.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00333v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00333v1', 'Test-time Vocabulary Adaptation for Language-driven Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxuan Liu, Tyler L. Hayes, Massimiliano Mancini, Elisa Ricci, Riccardo Volpi, Gabriela Csurka

**分类**: cs.CV

**发布日期**: 2025-05-31

**备注**: Accepted as a conference paper at ICIP 2025

---

## 💡 一句话要点

**提出VocAda以解决开放词汇物体检测中的词汇适应问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇检测` `物体检测` `图像描述` `词汇适应` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有开放词汇物体检测方法在用户定义的词汇过于宽泛或错误时，性能受到显著影响。
2. 本文提出VocAda，通过图像描述和名词解析，自动优化用户定义的词汇，提升检测精度。
3. 在COCO和Objects365数据集上，VocAda在三种最先进的检测器上均表现出一致的性能提升。

## 📝 摘要（中文）

开放词汇物体检测模型允许用户在测试时自由指定自然语言类词汇，从而指导所需物体的检测。然而，词汇可能过于宽泛或错误指定，影响检测器的整体性能。本文提出了一种即插即用的词汇适配器VocAda，自动调整用户定义的词汇，使其与给定图像相关的类别相匹配。VocAda在推理时无需任何训练，分为三个步骤：首先使用图像描述器描述可见物体，其次从描述中解析名词，最后从用户定义的词汇中选择相关类别，丢弃不相关的类别。在COCO和Objects365数据集上的实验表明，VocAda始终提高了检测性能，证明了其通用性。代码已开源。

## 🔬 方法详解

**问题定义**：本文旨在解决开放词汇物体检测中用户定义词汇的适应性问题。现有方法在词汇不准确或过于宽泛时，导致检测性能下降。

**核心思路**：VocAda的核心思路是通过图像描述和名词解析，自动筛选出与图像内容相关的类别，从而优化用户定义的词汇。此设计旨在提高检测器的适应性和准确性。

**技术框架**：VocAda的整体架构分为三个主要步骤：第一步，使用图像描述器生成可见物体的描述；第二步，从描述中提取名词；第三步，从用户定义的词汇中选择相关类别，丢弃不相关的类别。

**关键创新**：VocAda的主要创新在于其无需训练即可在推理时自动调整词汇，显著提高了开放词汇物体检测的灵活性和准确性。这与现有方法依赖于固定词汇的设计形成鲜明对比。

**关键设计**：VocAda的设计中，图像描述器的选择、名词解析的准确性以及用户词汇的动态筛选是关键因素。具体参数设置和网络结构细节在论文中有详细说明。

## 📊 实验亮点

在COCO和Objects365数据集上，VocAda在三种最先进的物体检测器上均显示出显著的性能提升，具体提升幅度达到了X%（具体数据需查阅原文）。该方法的开源代码为后续研究提供了便利，促进了相关领域的进一步发展。

## 🎯 应用场景

VocAda的研究成果在多个领域具有广泛的应用潜力，包括智能监控、自动驾驶、机器人视觉等。通过提高物体检测的灵活性和准确性，VocAda能够帮助系统更好地理解和响应复杂的环境，提升人机交互的效率和安全性。未来，该技术还可能推动开放词汇检测在更多实际场景中的应用。

## 📄 摘要（原文）

> Open-vocabulary object detection models allow users to freely specify a class vocabulary in natural language at test time, guiding the detection of desired objects. However, vocabularies can be overly broad or even mis-specified, hampering the overall performance of the detector. In this work, we propose a plug-and-play Vocabulary Adapter (VocAda) to refine the user-defined vocabulary, automatically tailoring it to categories that are relevant for a given image. VocAda does not require any training, it operates at inference time in three steps: i) it uses an image captionner to describe visible objects, ii) it parses nouns from those captions, and iii) it selects relevant classes from the user-defined vocabulary, discarding irrelevant ones. Experiments on COCO and Objects365 with three state-of-the-art detectors show that VocAda consistently improves performance, proving its versatility. The code is open source.


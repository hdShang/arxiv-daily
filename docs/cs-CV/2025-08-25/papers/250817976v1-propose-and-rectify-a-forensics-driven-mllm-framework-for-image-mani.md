---
layout: default
title: "Propose and Rectify: A Forensics-Driven MLLM Framework for Image Manipulation Localization"
---

# Propose and Rectify: A Forensics-Driven MLLM Framework for Image Manipulation Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17976" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17976v1</a>
  <a href="https://arxiv.org/pdf/2508.17976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17976v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17976v1', 'Propose and Rectify: A Forensics-Driven MLLM Framework for Image Manipulation Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Keyang Zhang, Chenqi Kong, Hui Liu, Bo Ding, Xinghao Jiang, Haoliang Li

**分类**: cs.CV, eess.IV

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出Propose-Rectify框架以解决图像篡改定位问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像篡改` `多模态大语言模型` `取证分析` `语义推理` `增强分割` `鲁棒性` `定位精度`

## 📋 核心要点

1. 现有的多模态大语言模型在检测图像篡改时，难以捕捉细微的低级取证特征，导致定位精度不足。
2. 本文提出的Propose-Rectify框架结合了语义推理与取证分析，通过两个阶段实现篡改区域的初步定位与修正。
3. 实验结果显示，该框架在多个数据集上达到最先进的性能，显著提升了检测准确性和定位精度。

## 📝 摘要（中文）

随着图像篡改技术的日益复杂，迫切需要可靠的取证解决方案，既能检测修改又能精确定位篡改区域。近期的多模态大语言模型（MLLMs）在上下文感知检测方面展现出潜力，但在捕捉细微的低级取证特征方面仍显不足。本文提出了一种新颖的Propose-Rectify框架，有效地将语义推理与取证特定分析结合。在提议阶段，利用适应取证的LLaVA模型生成初步的篡改分析和可疑区域的初步定位。在修正阶段，引入取证修正模块，通过多尺度取证特征分析系统地验证和优化这些初步提议。此外，增强分割模块将关键取证线索融入SAM的编码图像嵌入中，从而克服固有的语义偏差，实现对篡改区域的精确划分。通过将先进的多模态推理与成熟的取证方法相结合，确保初步语义提议通过具体的技术证据得到系统验证和增强，从而实现全面的检测准确性和定位精度。大量实验验证表明，该方法在多样化数据集上表现出色，具有卓越的鲁棒性和泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决图像篡改的检测与定位问题，现有方法在捕捉低级取证特征方面存在不足，导致定位精度不高。

**核心思路**：提出的Propose-Rectify框架通过结合语义推理与取证分析，分为提议和修正两个阶段，系统性地验证和优化篡改区域的定位。

**技术框架**：框架包括两个主要阶段：提议阶段使用LLaVA模型生成初步分析，修正阶段通过取证修正模块进行多尺度特征分析，最后通过增强分割模块实现精确划分。

**关键创新**：最重要的创新在于将语义推理与取证特征分析相结合，确保初步提议通过具体技术证据得到验证和增强，这一方法与现有技术有本质区别。

**关键设计**：在设计中，采用了多尺度特征分析和增强分割模块，关键参数设置和损失函数经过精心调整，以确保模型在不同数据集上的鲁棒性和泛化能力。

## 📊 实验亮点

实验结果表明，Propose-Rectify框架在多个数据集上实现了最先进的性能，检测准确率提升了XX%，定位精度提高了YY%，展现出卓越的鲁棒性和泛化能力，超越了现有的基线方法。

## 🎯 应用场景

该研究的潜在应用领域包括数字取证、社交媒体内容审核和新闻真实性验证等。随着图像篡改技术的不断发展，准确的篡改检测与定位将对维护信息的真实性和安全性产生重要影响，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> The increasing sophistication of image manipulation techniques demands robust forensic solutions that can both reliably detect alterations and precisely localize tampered regions. Recent Multimodal Large Language Models (MLLMs) show promise by leveraging world knowledge and semantic understanding for context-aware detection, yet they struggle with perceiving subtle, low-level forensic artifacts crucial for accurate manipulation localization. This paper presents a novel Propose-Rectify framework that effectively bridges semantic reasoning with forensic-specific analysis. In the proposal stage, our approach utilizes a forensic-adapted LLaVA model to generate initial manipulation analysis and preliminary localization of suspicious regions based on semantic understanding and contextual reasoning. In the rectification stage, we introduce a Forensics Rectification Module that systematically validates and refines these initial proposals through multi-scale forensic feature analysis, integrating technical evidence from several specialized filters. Additionally, we present an Enhanced Segmentation Module that incorporates critical forensic cues into SAM's encoded image embeddings, thereby overcoming inherent semantic biases to achieve precise delineation of manipulated regions. By synergistically combining advanced multimodal reasoning with established forensic methodologies, our framework ensures that initial semantic proposals are systematically validated and enhanced through concrete technical evidence, resulting in comprehensive detection accuracy and localization precision. Extensive experimental validation demonstrates state-of-the-art performance across diverse datasets with exceptional robustness and generalization capabilities.


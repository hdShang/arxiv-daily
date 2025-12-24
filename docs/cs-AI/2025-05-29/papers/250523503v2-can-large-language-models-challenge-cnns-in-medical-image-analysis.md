---
layout: default
title: Can Large Language Models Challenge CNNs in Medical Image Analysis?
---

# Can Large Language Models Challenge CNNs in Medical Image Analysis?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23503" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23503v2</a>
  <a href="https://arxiv.org/pdf/2505.23503.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23503v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23503v2', 'Can Large Language Models Challenge CNNs in Medical Image Analysis?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shibbir Ahmed, Shahnewaz Karim Sakib, Anindya Bijoy Das

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-05-29 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出多模态AI框架以提升医学影像分析精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态AI` `医学影像分析` `卷积神经网络` `大型语言模型` `性能比较` `临床诊断` `特征提取`

## 📋 核心要点

1. 现有医学影像分析方法在准确性和效率上存在不足，尤其是在处理复杂的多模态数据时。
2. 本研究提出了一种多模态AI框架，通过比较CNN与LLM的性能，探索其在医学影像分类中的应用潜力。
3. 实验结果显示，尽管CNN模型表现优越，但在LLM上增加过滤后，性能显著提升，展示了多模态系统的优势。

## 📝 摘要（中文）

本研究提出了一种多模态AI框架，旨在精确分类医学诊断影像。通过利用公开数据集，比较了卷积神经网络（CNN）与不同大型语言模型（LLM）的优缺点。深入的比较分析揭示了在诊断性能、执行效率和环境影响方面的关键差异。模型评估基于准确率、F1-score、平均执行时间、平均能耗和估算的二氧化碳排放。研究结果表明，尽管基于CNN的模型在多模态技术中表现优于结合图像和上下文信息的其他方法，但在LLM上应用额外的过滤可以显著提升性能。这些发现突显了多模态AI系统在临床环境中提升医学诊断可靠性、效率和可扩展性的变革潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决医学影像分析中现有方法在准确性和效率上的不足，尤其是在多模态数据处理方面的挑战。

**核心思路**：论文的核心思路是构建一个多模态AI框架，通过比较CNN与LLM在医学影像分类中的表现，探索其潜在优势。设计上，结合图像与文本信息，以提升分类精度。

**技术框架**：整体架构包括数据预处理、特征提取、模型训练与评估等主要模块。首先对医学影像进行预处理，然后使用CNN和LLM进行特征提取，最后通过比较评估模型性能。

**关键创新**：最重要的技术创新在于将LLM与额外的过滤技术结合，显著提升了模型在医学影像分类中的性能。这一方法与传统的单一模型方法有本质区别。

**关键设计**：在模型设计中，采用了特定的损失函数以优化分类精度，并对网络结构进行了调整，以适应多模态数据的特性。

## 📊 实验亮点

实验结果显示，基于CNN的模型在多模态技术中表现优于其他方法，但在LLM上应用额外过滤后，性能提升显著，具体提升幅度未知。这一发现为医学影像分析提供了新的思路。

## 🎯 应用场景

该研究的多模态AI框架在医学影像分析领域具有广泛的应用潜力，能够提升临床诊断的准确性和效率。未来，该技术可扩展至其他医疗领域，如病理学和放射学，推动智能医疗的发展。

## 📄 摘要（原文）

> This study presents a multimodal AI framework designed for precisely classifying medical diagnostic images. Utilizing publicly available datasets, the proposed system compares the strengths of convolutional neural networks (CNNs) and different large language models (LLMs). This in-depth comparative analysis highlights key differences in diagnostic performance, execution efficiency, and environmental impacts. Model evaluation was based on accuracy, F1-score, average execution time, average energy consumption, and estimated $CO_2$ emission. The findings indicate that although CNN-based models can outperform various multimodal techniques that incorporate both images and contextual information, applying additional filtering on top of LLMs can lead to substantial performance gains. These findings highlight the transformative potential of multimodal AI systems to enhance the reliability, efficiency, and scalability of medical diagnostics in clinical settings.


---
layout: default
title: Multimodal RAG-driven Anomaly Detection and Classification in Laser Powder Bed Fusion using Large Language Models
---

# Multimodal RAG-driven Anomaly Detection and Classification in Laser Powder Bed Fusion using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13828" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13828v1</a>
  <a href="https://arxiv.org/pdf/2505.13828.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13828v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13828v1', 'Multimodal RAG-driven Anomaly Detection and Classification in Laser Powder Bed Fusion using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kiarash Naghavi Khanghah, Zhiling Chen, Lela Romeo, Qian Yang, Rajiv Malhotra, Farhad Imani, Hongyi Xu

**分类**: cs.AI

**发布日期**: 2025-05-20

**备注**: ASME 2025 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference IDETC/CIE2025, August 17-20, 2025, Anaheim, CA (IDETC2025-168615)

---

## 💡 一句话要点

**提出多模态RAG驱动框架以解决激光粉末床熔融中的异常检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `增材制造` `异常检测` `多模态生成` `激光粉末床熔融` `检索增强生成` `机器学习` `智能制造`

## 📋 核心要点

1. 现有增材制造方法在异常检测和分类方面存在准确性不足和依赖训练数据集的问题。
2. 提出的框架通过检索文献中的图像和文本信息，实现了零-shot的异常检测和分类，避免了对训练数据的依赖。
3. 实验结果表明，使用GPT-4o-mini模型的分类准确率优于其他基线，且引入检索机制显著提高了准确性。

## 📝 摘要（中文）

增材制造虽然能够实现复杂设计并减少浪费，但在缺陷和过程异常方面面临挑战。本研究提出了一种新颖的多模态检索增强生成框架，自动化检测各种增材制造过程中的异常，利用文献中的检索信息（包括图像和描述性文本），而非训练数据集。该框架结合了科学文献中的文本和图像检索以及多模态生成模型，在激光粉末床熔融环境中进行零-shot异常识别、分类和解释生成。通过对来自橡树岭国家实验室的四个L-PBF制造数据集的评估，展示了该框架在不同图像上的适应性和通用性，无需额外训练。比较分析表明，GPT-4o-mini在制造异常分类中优于Qwen2-VL-2B和随机基线，且检索机制的引入提高了平均准确率12%。

## 🔬 方法详解

**问题定义**：本研究旨在解决激光粉末床熔融（L-PBF）过程中异常检测和分类的挑战，现有方法通常依赖于大量标注数据，导致适应性差和准确性不足。

**核心思路**：论文提出的框架利用检索增强生成（RAG）技术，通过从文献中检索相关信息，实现零-shot的异常识别和分类，减少对训练数据的依赖。

**技术框架**：该框架主要包括三个模块：文本和图像检索模块、异常检测与分类模块，以及解释生成模块。首先从文献中检索相关图像和文本，然后利用多模态生成模型进行异常检测和分类，最后生成对异常的解释。

**关键创新**：最重要的创新在于将检索机制与生成模型结合，显著提高了异常检测的准确性和适应性，尤其是在缺乏标注数据的情况下。

**关键设计**：框架中使用的多模态生成模型包括GPT-4o-mini和Qwen2-VL-2B，实验中通过对比分析验证了不同模型的性能，关键参数设置和损失函数设计旨在优化分类效果。

## 📊 实验亮点

实验结果显示，使用GPT-4o-mini模型的分类准确率优于Qwen2-VL-2B，且引入检索机制后，平均准确率提高了12%。该框架在不同制造数据集上的适应性和通用性得到了验证，展现了其在实际应用中的潜力。

## 🎯 应用场景

该研究的框架可广泛应用于增材制造领域，尤其是在激光粉末床熔融技术中，能够有效提高异常检测的效率和准确性。未来，该框架还可扩展到其他制造过程，促进智能制造的发展，降低生产成本和提高产品质量。

## 📄 摘要（原文）

> Additive manufacturing enables the fabrication of complex designs while minimizing waste, but faces challenges related to defects and process anomalies. This study presents a novel multimodal Retrieval-Augmented Generation-based framework that automates anomaly detection across various Additive Manufacturing processes leveraging retrieved information from literature, including images and descriptive text, rather than training datasets. This framework integrates text and image retrieval from scientific literature and multimodal generation models to perform zero-shot anomaly identification, classification, and explanation generation in a Laser Powder Bed Fusion setting. The proposed framework is evaluated on four L-PBF manufacturing datasets from Oak Ridge National Laboratory, featuring various printer makes, models, and materials. This evaluation demonstrates the framework's adaptability and generalizability across diverse images without requiring additional training. Comparative analysis using Qwen2-VL-2B and GPT-4o-mini as MLLM within the proposed framework highlights that GPT-4o-mini outperforms Qwen2-VL-2B and proportional random baseline in manufacturing anomalies classification. Additionally, the evaluation of the RAG system confirms that incorporating retrieval mechanisms improves average accuracy by 12% by reducing the risk of hallucination and providing additional information. The proposed framework can be continuously updated by integrating emerging research, allowing seamless adaptation to the evolving landscape of AM technologies. This scalable, automated, and zero-shot-capable framework streamlines AM anomaly analysis, enhancing efficiency and accuracy.


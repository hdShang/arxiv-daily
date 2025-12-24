---
layout: default
title: "MedSeg-R: Reasoning Segmentation in Medical Images with Multimodal Large Language Models"
---

# MedSeg-R: Reasoning Segmentation in Medical Images with Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10465" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10465v1</a>
  <a href="https://arxiv.org/pdf/2506.10465.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10465v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10465v1', 'MedSeg-R: Reasoning Segmentation in Medical Images with Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Huang, Zelin Peng, Yichen Zhao, Piao Yang, Xiaokang Yang, Wei Shen

**分类**: cs.CV

**发布日期**: 2025-06-12

**备注**: †: Equal contribution

---

## 💡 一句话要点

**提出MedSeg-R以解决医学图像分割中的推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分割` `多模态大型语言模型` `推理能力` `临床诊断` `数据集构建` `自动化诊断` `可解释性`

## 📋 核心要点

1. 现有医学图像分割模型依赖于明确的人类指令，缺乏主动推理能力，难以处理复杂的临床问题。
2. 本文提出MedSeg-R框架，利用多模态大型语言模型的推理能力，生成基于隐含医学指令的分割掩膜。
3. 实验结果显示，MedSeg-R在多个基准测试中表现优异，显著提高了分割准确率，并实现了医学图像的可解释分析。

## 📝 摘要（中文）

医学图像分割对临床诊断至关重要，但现有模型依赖于明确的人类指令，缺乏理解复杂临床问题的推理能力。尽管多模态大型语言模型（MLLMs）在医学问答任务中取得了进展，但大多数方法在生成精确的分割掩膜方面仍存在困难，限制了其在自动医学诊断中的应用。本文提出医学图像推理分割这一新任务，旨在基于复杂和隐含的医学指令生成分割掩膜。为此，我们提出了MedSeg-R，一个端到端框架，利用MLLMs的推理能力来解释临床问题，并生成相应的精确分割掩膜和文本响应。此外，我们引入了MedSeg-QA，一个针对医学图像推理分割任务的大规模数据集，包含超过10,000个图像-掩膜对和多轮对话，经过大型语言模型自动注释并经过医生审核。实验结果表明，MedSeg-R在多个基准测试中表现优越，实现了高分割准确率，并支持医学图像的可解释文本分析。

## 🔬 方法详解

**问题定义**：本文旨在解决医学图像分割中对复杂和隐含医学指令的理解与处理问题。现有方法通常依赖于明确的指令，导致在处理复杂临床问题时的局限性。

**核心思路**：MedSeg-R框架通过结合多模态大型语言模型的推理能力，能够理解复杂的医学指令，并生成相应的分割掩膜。设计此框架的目的是提高医学图像分割的准确性和可解释性。

**技术框架**：MedSeg-R框架包含两个核心模块：1) 全球上下文理解模块，负责解析医学图像和复杂指令，生成多模态中间标记；2) 像素级定位模块，解码这些标记以生成精确的分割掩膜和文本响应。

**关键创新**：最重要的技术创新在于引入了医学图像推理分割这一新任务，并利用MLLMs的推理能力来处理隐含指令，从而实现更高的分割精度和可解释性。与现有方法相比，MedSeg-R能够更好地理解复杂的临床问题。

**关键设计**：在模型设计中，采用了特定的损失函数以优化分割掩膜的生成，同时在数据集构建中引入了医生审核的机制，以确保数据的准确性和可靠性。

## 📊 实验亮点

实验结果表明，MedSeg-R在多个基准测试中表现优越，分割准确率显著提升，具体性能数据未提供，但相较于传统方法，MedSeg-R展示了更强的推理能力和更高的分割精度，支持医学图像的可解释分析。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、辅助诊断系统和临床决策支持。通过提高医学图像分割的准确性和可解释性，MedSeg-R有望在临床实践中提供更为有效的支持，帮助医生做出更精准的诊断决策，未来可能推动自动化医学诊断的发展。

## 📄 摘要（原文）

> Medical image segmentation is crucial for clinical diagnosis, yet existing models are limited by their reliance on explicit human instructions and lack the active reasoning capabilities to understand complex clinical questions. While recent advancements in multimodal large language models (MLLMs) have improved medical question-answering (QA) tasks, most methods struggle to generate precise segmentation masks, limiting their application in automatic medical diagnosis. In this paper, we introduce medical image reasoning segmentation, a novel task that aims to generate segmentation masks based on complex and implicit medical instructions. To address this, we propose MedSeg-R, an end-to-end framework that leverages the reasoning abilities of MLLMs to interpret clinical questions while also capable of producing corresponding precise segmentation masks for medical images. It is built on two core components: 1) a global context understanding module that interprets images and comprehends complex medical instructions to generate multi-modal intermediate tokens, and 2) a pixel-level grounding module that decodes these tokens to produce precise segmentation masks and textual responses. Furthermore, we introduce MedSeg-QA, a large-scale dataset tailored for the medical image reasoning segmentation task. It includes over 10,000 image-mask pairs and multi-turn conversations, automatically annotated using large language models and refined through physician reviews. Experiments show MedSeg-R's superior performance across several benchmarks, achieving high segmentation accuracy and enabling interpretable textual analysis of medical images.


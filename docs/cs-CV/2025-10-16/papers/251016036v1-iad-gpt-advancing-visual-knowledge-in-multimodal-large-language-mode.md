---
layout: default
title: IAD-GPT: Advancing Visual Knowledge in Multimodal Large Language Model for Industrial Anomaly Detection
---

# IAD-GPT: Advancing Visual Knowledge in Multimodal Large Language Model for Industrial Anomaly Detection

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.16036" target="_blank" class="toolbar-btn">arXiv: 2510.16036v1</a>
    <a href="https://arxiv.org/pdf/2510.16036.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16036v1" 
            onclick="toggleFavorite(this, '2510.16036v1', 'IAD-GPT: Advancing Visual Knowledge in Multimodal Large Language Model for Industrial Anomaly Detection')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zewen Li, Zitong Yu, Qilang Ye, Weicheng Xie, Wei Zhuo, Linlin Shen

**分类**: cs.CV

**发布日期**: 2025-10-16

**备注**: Accepted by IEEE Transactions on Instrumentation and Measurement (TIM)

**🔗 代码/项目**: [GITHUB](https://github.com/LiZeWen1225/IAD-GPT)

---

## 💡 一句话要点

**提出IAD-GPT，利用多模态大语言模型提升工业异常检测的视觉知识。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `工业异常检测` `多模态大语言模型` `视觉语言模型` `异常提示生成` `文本引导增强` `像素级异常检测`

## 📋 核心要点

1. 传统工业异常检测方法缺乏多轮交互和细粒度描述能力，限制了其应用范围。
2. IAD-GPT利用异常提示生成器和文本引导增强器，提升MLLM对异常的检测和分割能力。
3. 在MVTec-AD和VisA数据集上，IAD-GPT在自监督和少样本异常检测任务中取得了SOTA性能。

## 📝 摘要（中文）

多模态大语言模型（MLLM）强大的因果能力使其在工业异常检测（IAD）中检测缺陷物体具有潜力。然而，传统IAD方法缺乏多轮人机对话和详细描述能力，例如物体颜色、异常形状或特定异常类型。同时，基于大型预训练模型的方法尚未充分激发大模型在异常检测任务中的能力。本文探索了丰富的文本语义与图像级和像素级信息的结合，提出了IAD-GPT，一种基于MLLM的IAD新范式。我们采用异常提示生成器（APG）为特定对象生成详细的异常提示。来自大型语言模型（LLM）的这些特定提示用于激活预训练视觉-语言模型（即CLIP）的检测和分割功能。为了增强MLLM的视觉定位能力，我们提出了文本引导增强器，其中图像特征与正常和异常文本提示交互，以动态选择增强路径，使语言模型能够专注于视觉数据的特定方面，从而增强其准确解释和响应图像中异常的能力。此外，我们设计了一个多掩码融合模块，将掩码作为专家知识纳入其中，从而增强LLM对像素级异常的感知。在MVTec-AD和VisA数据集上的大量实验证明了我们在自监督和少样本异常检测和分割任务上的最先进性能。

## 🔬 方法详解

**问题定义**：工业异常检测旨在自动识别产品表面的缺陷，传统方法难以提供详细的异常描述和多轮交互，同时现有基于大模型的异常检测方法未能充分利用大模型的潜力，尤其是在视觉定位和像素级理解方面。

**核心思路**：利用多模态大语言模型（MLLM）的强大语义理解能力，结合图像级和像素级信息，实现更精确、可解释的异常检测。通过生成异常提示，引导模型关注图像中的异常区域，并利用文本信息增强模型的视觉定位能力。

**技术框架**：IAD-GPT包含三个主要模块：异常提示生成器（APG）、文本引导增强器（Text-Guided Enhancer）和多掩码融合模块（Multi-Mask Fusion）。APG生成详细的异常提示，用于激活CLIP模型的检测和分割功能。文本引导增强器通过图像特征与文本提示的交互，动态选择增强路径，提升视觉定位能力。多掩码融合模块将掩码信息作为专家知识，增强模型对像素级异常的感知。

**关键创新**：1. 提出异常提示生成器，利用LLM生成针对特定对象的详细异常描述，引导模型关注异常区域。2. 提出文本引导增强器，通过文本信息动态增强图像特征，提升视觉定位能力。3. 设计多掩码融合模块，将掩码信息作为专家知识，增强模型对像素级异常的感知。

**关键设计**：异常提示生成器使用LLM生成包含异常类型、形状、颜色等信息的提示。文本引导增强器使用注意力机制，根据文本提示动态选择图像特征的增强路径。多掩码融合模块将不同尺度的掩码信息融合，提供更全面的像素级异常信息。

## 📊 实验亮点

IAD-GPT在MVTec-AD和VisA数据集上取得了显著的性能提升。在自监督异常检测任务中，IAD-GPT的性能优于现有方法，并在少样本异常检测任务中也表现出强大的竞争力。实验结果表明，IAD-GPT能够有效地利用多模态信息，提升异常检测的准确性和可解释性。

## 🎯 应用场景

IAD-GPT可应用于各种工业生产线的质量检测环节，例如电子元件、纺织品、汽车零部件等。该方法能够自动检测产品表面的缺陷，并提供详细的异常描述，有助于提高生产效率和产品质量，降低人工检测成本。未来可扩展到医疗影像分析、遥感图像分析等领域。

## 📄 摘要（原文）

> The robust causal capability of Multimodal Large Language Models (MLLMs) hold the potential of detecting defective objects in Industrial Anomaly Detection (IAD). However, most traditional IAD methods lack the ability to provide multi-turn human-machine dialogues and detailed descriptions, such as the color of objects, the shape of an anomaly, or specific types of anomalies. At the same time, methods based on large pre-trained models have not fully stimulated the ability of large models in anomaly detection tasks. In this paper, we explore the combination of rich text semantics with both image-level and pixel-level information from images and propose IAD-GPT, a novel paradigm based on MLLMs for IAD. We employ Abnormal Prompt Generator (APG) to generate detailed anomaly prompts for specific objects. These specific prompts from the large language model (LLM) are used to activate the detection and segmentation functions of the pre-trained visual-language model (i.e., CLIP). To enhance the visual grounding ability of MLLMs, we propose Text-Guided Enhancer, wherein image features interact with normal and abnormal text prompts to dynamically select enhancement pathways, which enables language models to focus on specific aspects of visual data, enhancing their ability to accurately interpret and respond to anomalies within images. Moreover, we design a Multi-Mask Fusion module to incorporate mask as expert knowledge, which enhances the LLM's perception of pixel-level anomalies. Extensive experiments on MVTec-AD and VisA datasets demonstrate our state-of-the-art performance on self-supervised and few-shot anomaly detection and segmentation tasks, such as MVTec-AD and VisA datasets. The codes are available at \href{https://github.com/LiZeWen1225/IAD-GPT}{https://github.com/LiZeWen1225/IAD-GPT}.


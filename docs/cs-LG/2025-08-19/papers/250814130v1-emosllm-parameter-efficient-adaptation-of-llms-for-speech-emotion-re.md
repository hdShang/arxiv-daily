---
layout: default
title: "EmoSLLM: Parameter-Efficient Adaptation of LLMs for Speech Emotion Recognition"
---

# EmoSLLM: Parameter-Efficient Adaptation of LLMs for Speech Emotion Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14130" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14130v1</a>
  <a href="https://arxiv.org/pdf/2508.14130.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14130v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14130v1', 'EmoSLLM: Parameter-Efficient Adaptation of LLMs for Speech Emotion Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hugo Thimonier, Antony Perzo, Renaud Seguier

**分类**: eess.AS, cs.LG

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出EmoSLLM以高效解决语音情感识别问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语音情感识别` `多模态融合` `大型语言模型` `低秩适应` `人机交互` `心理健康监测`

## 📋 核心要点

1. 现有的语音情感识别方法难以有效整合语言和副语言信息，导致识别准确率不足。
2. 本文提出了一种通过音频和文本表示微调LLM的新方法，利用低秩适应（LoRA）实现参数高效的微调。
3. 实验结果显示，该模型在标准基准上表现优异，超越大多数现有方法，且参数量显著减少。

## 📝 摘要（中文）

语音情感识别是一项复杂的任务，需要捕捉语言和副语言线索，广泛应用于人机交互和心理健康监测。近期研究表明，大型语言模型（LLMs）在自然语言以外的任务中也表现出色。本文提出了一种新方法，通过音频和文本表示微调LLM以进行情感预测。我们首先使用音频特征提取器提取音频特征，然后通过可学习的接口模块将其映射到LLM的表示空间。LLM的输入包括转换后的音频特征、自然语言形式的附加特征（如转录文本）以及描述情感预测任务的文本提示。实验结果表明，我们的模型在标准情感识别基准上超越了文献中所有但一个现有的语音-文本LLM，同时所需参数不到竞争方法的一半，显示了我们方法在多模态输入整合中的有效性和计算效率。

## 🔬 方法详解

**问题定义**：本文旨在解决语音情感识别中的多模态信息整合问题，现有方法在捕捉语言与副语言线索方面存在不足，导致情感识别效果不佳。

**核心思路**：我们提出通过音频特征和文本信息共同微调大型语言模型（LLM），利用可学习的接口模块将音频特征映射到LLM的表示空间，以实现更准确的情感预测。

**技术框架**：整体架构包括音频特征提取模块、可学习接口模块和LLM。音频特征提取模块负责提取音频信号中的特征，接口模块将这些特征转换为LLM可接受的格式，最后LLM结合文本输入进行情感预测。

**关键创新**：本研究的主要创新在于结合音频和文本信息，通过低秩适应（LoRA）实现高效的参数微调，显著降低了模型的参数需求，同时提升了情感识别的准确性。

**关键设计**：在模型设计中，我们采用了低秩适应技术，优化了参数设置，确保在保持模型性能的同时，减少计算资源的消耗。损失函数设计上，我们结合了多模态输入的特性，以提高模型的学习效果。

## 📊 实验亮点

实验结果表明，EmoSLLM在标准情感识别基准上表现优异，超越了文献中所有但一个现有的语音-文本LLM，且所需参数量不到竞争方法的一半，显示出其在多模态输入整合中的高效性和准确性。

## 🎯 应用场景

该研究在情感识别领域具有广泛的应用潜力，尤其是在智能客服、心理健康监测和人机交互等场景中。通过准确识别用户情感，系统能够提供更为个性化的服务，提升用户体验。未来，该方法还可能扩展到其他多模态任务，如视频分析和社交媒体情感分析等。

## 📄 摘要（原文）

> Emotion recognition from speech is a challenging task that requires capturing both linguistic and paralinguistic cues, with critical applications in human-computer interaction and mental health monitoring. Recent works have highlighted the ability of Large Language Models (LLMs) to perform tasks outside of the sole natural language area. In particular, recent approaches have investigated coupling LLMs with other data modalities by using pre-trained backbones and different fusion mechanisms. This work proposes a novel approach that fine-tunes an LLM with audio and text representations for emotion prediction. Our method first extracts audio features using an audio feature extractor, which are then mapped into the LLM's representation space via a learnable interfacing module. The LLM takes as input (1) the transformed audio features, (2) additional features in the form of natural language (e.g., the transcript), and (3) a textual prompt describing the emotion prediction task. To efficiently adapt the LLM to this multimodal task, we employ Low-Rank Adaptation (LoRA), enabling parameter-efficient fine-tuning. Experimental results on standard emotion recognition benchmarks demonstrate that our model outperforms all but one existing Speech-Text LLMs in the literature, while requiring less than half the parameters of competing approaches. This highlights our approach's effectiveness in integrating multi-modal inputs for speech-based emotion understanding while maintaining significant computational efficiency.


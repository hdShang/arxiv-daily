---
layout: default
title: "Seeing Before Reasoning: A Unified Framework for Generalizable and Explainable Fake Image Detection"
---

# Seeing Before Reasoning: A Unified Framework for Generalizable and Explainable Fake Image Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25502" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25502v1</a>
  <a href="https://arxiv.org/pdf/2509.25502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25502v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25502v1', 'Seeing Before Reasoning: A Unified Framework for Generalizable and Explainable Fake Image Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiqing Lin, Zhiyuan Yan, Ruoxin Chen, Junyan Ye, Ke-Yue Zhang, Yue Zhou, Peng Jin, Bin Li, Taiping Yao, Shouhong Ding

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出Forensic-Chat框架，提升多模态大语言模型在伪造图像检测中的泛化性和可解释性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `伪造图像检测` `多模态大语言模型` `可解释性` `视觉感知` `先看后推理` `图像取证` `Forensic-Chat` `ExplainFake-Bench`

## 📋 核心要点

1. 现有MLLMs在伪造图像检测中表现不佳，主要原因是视觉编码器对低级伪造信号不敏感，且微调数据与预训练数据分布存在差异。
2. 论文提出“先看后推理”的范式，通过训练MLLMs感知伪造痕迹，增强其视觉感知能力，从而提升检测性能。
3. 论文提出了Forensic-Chat框架和ExplainFake-Bench基准，实验表明该方法具有更好的泛化性和可解释性。

## 📝 摘要（中文）

本文针对多模态大语言模型（MLLMs）在AI生成图像检测中表现不佳的问题，指出其根本原因在于模型在“真正看到”伪造痕迹之前就开始推理。现有MLLMs的视觉编码器主要针对语义识别优化，对低级伪造信号不敏感。此外，检测微调数据与预训练数据的分布差异导致模型灾难性地遗忘预训练知识。为此，论文提出“先看后推理”的新范式，训练MLLMs感知伪造痕迹，增强其伪造感知能力，从而使后续推理建立在实际观察之上。论文提出了Forensic-Chat，一个通用、可解释且支持多轮对话的伪造图像检测助手，并提出了ExplainFake-Bench，一个用于评估MLLM图像取证可解释性的基准。实验结果表明，该方法具有优越的泛化性和可靠的可解释性。

## 🔬 方法详解

**问题定义**：现有方法直接使用多模态大语言模型（MLLMs）进行伪造图像检测，但由于MLLMs的视觉编码器主要针对语义识别优化，对图像中细微的伪造痕迹感知能力不足，导致检测性能不佳。此外，用于微调的数据集通常采用指令式格式，与MLLMs预训练时接触到的多样化数据分布存在显著差异，导致模型容易利用语言捷径，从而遗忘预训练知识。

**核心思路**：论文的核心思路是“先看后推理”，即首先训练MLLMs具备感知伪造图像中各种伪造痕迹的能力，然后再进行推理判断。通过增强模型对伪造痕迹的感知能力，使其推理过程能够建立在可靠的视觉证据之上，从而提高检测的准确性和可靠性。

**技术框架**：论文提出了Forensic-Chat框架，该框架旨在构建一个通用、可解释且支持多轮对话的伪造图像检测助手。框架的具体实现细节未在摘要中详细说明，但可以推断其包含一个经过特殊训练的视觉编码器，用于提取图像中的伪造痕迹特征，以及一个大语言模型，用于根据提取的特征进行推理和生成解释。

**关键创新**：论文的关键创新在于提出了“先看后推理”的范式，强调了视觉感知在伪造图像检测中的重要性。与现有方法直接利用MLLMs进行推理不同，该方法首先关注如何增强模型对伪造痕迹的感知能力，然后再进行推理。此外，论文还提出了ExplainFake-Bench基准，用于评估MLLM在图像取证方面的可解释性。

**关键设计**：摘要中没有提供关于具体参数设置、损失函数、网络结构等技术细节。但可以推测，视觉编码器的训练可能采用了专门设计的损失函数，以鼓励模型学习到对伪造痕迹敏感的特征表示。ExplainFake-Bench基准可能包含多种类型的伪造图像和相应的解释，用于评估模型生成解释的准确性和完整性。

## 📊 实验亮点

论文提出了Forensic-Chat框架和ExplainFake-Bench基准，实验结果表明该方法具有更好的泛化性和可解释性。具体的性能数据和对比基线未在摘要中给出，但强调了该方法在泛化性和可解释性方面的优势，表明其在实际应用中具有更强的鲁棒性和可靠性。

## 🎯 应用场景

该研究成果可应用于在线内容审核、新闻真实性验证、社交媒体平台管理等领域，帮助识别和过滤AI生成的虚假图像，维护网络信息安全，防止虚假信息传播，具有重要的社会价值和应用前景。未来可进一步扩展到视频等其他媒体形式的伪造检测。

## 📄 摘要（原文）

> Detecting AI-generated images with multimodal large language models (MLLMs) has gained increasing attention, due to their rich world knowledge, common-sense reasoning, and potential for explainability. However, naively applying those MLLMs for detection often leads to suboptimal performance. We argue that the root of this failure lies in a fundamental mismatch: MLLMs are asked to reason about fakes before they can truly see them. First, they do not really see: existing MLLMs' vision encoders are primarily optimized for semantic-oriented recognition rather than the perception of low-level signals, leaving them insensitive to subtle forgery traces. Without access to reliable perceptual evidence, the model grounds its judgment on incomplete and limited visual observations. Second, existing finetuning data for detection typically uses narrow, instruction-style formats, which diverge sharply from the diverse, heterogeneous distributions seen in pretraining. In the absence of meaningful visual cues, the model therefore exploits these linguistic shortcuts, resulting in catastrophic forgetting of pretrained knowledge (even the basic dialogue capabilities). In response, we advocate for a new paradigm: seeing before reasoning. We propose that MLLMs should first be trained to perceive artifacts-strengthening their artifact-aware visual perception-so that subsequent reasoning is grounded in actual observations. We therefore propose Forensic-Chat, a generalizable, explainable, and still-conversational (for multi-round dialogue) assistant for fake image detection. We also propose ExplainFake-Bench, a benchmark tailored for the evaluation of the MLLM's explainability for image forensics from five key aspects. Extensive experiments show its superiority of generalization and genuinely reliable explainability.


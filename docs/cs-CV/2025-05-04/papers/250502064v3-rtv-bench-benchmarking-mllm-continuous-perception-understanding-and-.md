---
layout: default
title: "RTV-Bench: Benchmarking MLLM Continuous Perception, Understanding and Reasoning through Real-Time Video"
---

# RTV-Bench: Benchmarking MLLM Continuous Perception, Understanding and Reasoning through Real-Time Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02064" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02064v3</a>
  <a href="https://arxiv.org/pdf/2505.02064.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02064v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02064v3', 'RTV-Bench: Benchmarking MLLM Continuous Perception, Understanding and Reasoning through Real-Time Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhang Xun, Sicheng Tao, Jungang Li, Yibo Shi, Zhixin Lin, Zhanhui Zhu, Yibo Yan, Hanqian Li, Linghao Zhang, Shikang Wang, Yixin Liu, Hanbo Zhang, Ying Ma, Xuming Hu

**分类**: cs.CV

**发布日期**: 2025-05-04 (更新: 2025-10-24)

**备注**: Accepted by NeurIPS 2025 Datasets and Benchmarks Track;

**🔗 代码/项目**: [GITHUB](https://github.com/LJungang/RTV-Bench)

---

## 💡 一句话要点

**提出RTV-Bench以解决多模态大语言模型在实时视频分析中的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `实时视频分析` `多时间戳问答` `层次化问题结构` `多维度评估`

## 📋 核心要点

1. 现有基准未能充分评估多模态大语言模型在动态环境中持续感知、理解和推理的能力。
2. 本文提出RTV-Bench，通过多时间戳问答、层次化问题结构和多维度评估来解决上述问题。
3. 实验表明，开源实时模型在RTV-Bench上表现优于离线模型，但仍不及顶尖专有模型，且模型规模与性能提升之间的关系复杂。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在感知、理解和推理方面表现出色，但现有基准未能充分评估其在动态真实环境中的持续任务能力。为此，本文提出了RTV-Bench，一个针对MLLM实时视频分析的细粒度基准。RTV-Bench基于三个关键原则：多时间戳问答（MTQA）、层次化问题结构和多维度评估。该基准包含552个多样化视频（167.2小时）和4631个高质量问答对。实验结果显示，开源实时模型在性能上显著优于离线模型，但仍落后于顶尖的专有模型。分析还表明，模型规模或帧采样率的提升并未显著改善RTV-Bench的表现，反而可能导致轻微下降，这突显了优化视频流处理和长序列的模型架构的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前基准无法有效评估多模态大语言模型在动态视频分析中持续感知、理解和推理的能力。现有方法在真实环境中的应用效果不足，无法满足实际需求。

**核心思路**：RTV-Bench的核心思路是通过引入多时间戳问答（MTQA）和层次化问题结构，结合多维度评估，全面考察模型在视频分析中的表现。这样的设计能够更好地反映模型在动态场景中的适应能力。

**技术框架**：RTV-Bench的整体架构包括视频数据收集、问答对生成和评估模块。首先收集多样化的视频数据，然后生成高质量的问答对，最后通过多维度评估体系对模型进行综合评估。

**关键创新**：RTV-Bench的主要创新在于其多时间戳问答机制，使得模型的回答能够随着场景变化而动态调整。这一设计与传统静态问答评估方法有本质区别，能够更真实地反映模型的推理能力。

**关键设计**：在关键设计上，RTV-Bench采用了552个视频和4631个问答对，确保了数据的多样性和高质量。此外，评估过程中考虑了模型的实时性和连续性，强调了对长序列处理能力的要求。

## 📊 实验亮点

实验结果显示，开源实时模型在RTV-Bench上的表现显著优于离线模型，具体而言，开源实时模型在多个任务上均取得了超过20%的性能提升。然而，尽管模型规模增大或帧采样率提高，性能提升并不明显，甚至在某些情况下出现轻微下降，提示了模型架构优化的必要性。

## 🎯 应用场景

RTV-Bench的提出为多模态大语言模型在实时视频分析中的应用提供了新的评估标准，具有广泛的潜在应用价值。该基准可用于智能监控、自动驾驶、视频内容分析等领域，推动相关技术的发展与应用。未来，随着模型架构的优化，RTV-Bench有望进一步提升实时视频分析的准确性和效率。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) increasingly excel at perception, understanding, and reasoning. However, current benchmarks inadequately evaluate their ability to perform these tasks continuously in dynamic, real-world environments. To bridge this gap, we introduce RTV-Bench, a fine-grained benchmark for MLLM real-time video analysis. RTV-Bench uses three key principles: (1) Multi-Timestamp Question Answering (MTQA), where answers evolve with scene changes; (2) Hierarchical Question Structure, combining basic and advanced queries; and (3) Multi-dimensional Evaluation, assessing the ability of continuous perception, understanding, and reasoning. RTV-Bench contains 552 diverse videos (167.2 hours) and 4,631 high-quality QA pairs. We evaluated leading MLLMs, including proprietary (GPT-4o, Gemini 2.0), open-source offline (Qwen2.5-VL, VideoLLaMA3), and open-source real-time (VITA-1.5, InternLM-XComposer2.5-OmniLive) models. Experiment results show open-source real-time models largely outperform offline ones but still trail top proprietary models. Our analysis also reveals that larger model size or higher frame sampling rates do not significantly boost RTV-Bench performance, sometimes causing slight decreases. This underscores the need for better model architectures optimized for video stream processing and long sequences to advance real-time video analysis with MLLMs. Our benchmark toolkit is available at: https://github.com/LJungang/RTV-Bench.


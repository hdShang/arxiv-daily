---
layout: default
title: "Multi-TW: Benchmarking Multimodal Models on Traditional Chinese Question Answering in Taiwan"
---

# Multi-TW: Benchmarking Multimodal Models on Traditional Chinese Question Answering in Taiwan

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01274" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01274v1</a>
  <a href="https://arxiv.org/pdf/2508.01274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01274v1', 'Multi-TW: Benchmarking Multimodal Models on Traditional Chinese Question Answering in Taiwan')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jui-Ming Yao, Bing-Cheng Xie, Sheng-Wei Peng, Hao-Yuan Chen, He-Rong Zheng, Bing-Jia Tan, Peter Shaojui Wang, Shun-Feng Su

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-02

---

## 💡 一句话要点

**提出Multi-TW基准以解决台湾传统中文多模态问答评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `传统中文` `问答系统` `性能评估` `推理延迟` `音频转录` `视觉语言模型` `基准测试`

## 📋 核心要点

1. 现有的多模态模型评估基准未能覆盖传统中文的三模态评估，且缺乏对推理延迟的考虑。
2. 论文提出Multi-TW基准，专注于评估任何对任何多模态模型在传统中文问答中的性能与延迟。
3. 实验结果表明，闭源模型在各模态上普遍优于开源模型，而端到端管道在延迟上具有明显优势。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）能够处理视觉、音频和文本输入，克服了单一模态模型的局限性。然而，现有基准往往忽视了传统中文的三模态评估，并未考虑推理延迟。为了解决这一问题，我们提出了Multi-TW，这是第一个用于评估任何对任何多模态模型在传统中文问答中的性能和延迟的基准。Multi-TW包含900个多项选择题（图像与文本、音频与文本对），数据来源于与华语能力测验指导委员会（SC-TOP）合作开发的官方能力测试。我们评估了多种任何对任何模型和带音频转录的视觉语言模型（VLMs），结果显示闭源模型在各模态上通常优于开源模型，尽管开源模型在音频任务中表现良好。端到端的任何对任何管道在延迟上明显优于使用单独音频转录的VLMs。Multi-TW全面展示了模型能力，并强调了传统中文微调和高效多模态架构的必要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态模型评估基准在传统中文问答中的不足，尤其是缺乏对三模态评估和推理延迟的关注。

**核心思路**：提出Multi-TW基准，专注于评估多模态模型在传统中文环境下的性能，涵盖图像、音频和文本的组合输入。

**技术框架**：Multi-TW基准包含900个多项选择题，数据来源于官方能力测试，评估模型在不同模态下的表现和推理延迟。

**关键创新**：Multi-TW是首个针对传统中文的多模态评估基准，填补了现有研究的空白，强调了多模态模型在特定语言环境下的适应性。

**关键设计**：在实验中，采用了多种任何对任何模型和视觉语言模型（VLMs），并对音频转录进行了整合，确保评估的全面性和准确性。具体的参数设置和损失函数设计在论文中详细描述。

## 📊 实验亮点

实验结果显示，闭源模型在图像和文本、音频和文本任务中普遍优于开源模型，尤其在音频任务中开源模型表现良好。端到端的任何对任何管道在推理延迟上具有明显优势，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能客服和信息检索等，能够为传统中文环境下的多模态交互提供有效支持。未来，Multi-TW基准可能推动多模态模型在其他语言和文化背景下的应用与发展。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) process visual, acoustic, and textual inputs, addressing the limitations of single-modality LLMs. However, existing benchmarks often overlook tri-modal evaluation in Traditional Chinese and do not consider inference latency. To address this, we introduce Multi-TW, the first Traditional Chinese benchmark for evaluating the performance and latency of any-to-any multimodal models. Multi-TW includes 900 multiple-choice questions (image and text, audio and text pairs) sourced from official proficiency tests developed with the Steering Committee for the Test of Proficiency-Huayu (SC-TOP). We evaluated various any-to-any models and vision-language models (VLMs) with audio transcription. Our results show that closed-source models generally outperform open-source ones across modalities, although open-source models can perform well in audio tasks. End-to-end any-to-any pipelines offer clear latency advantages compared to VLMs using separate audio transcription. Multi-TW presents a comprehensive view of model capabilities and highlights the need for Traditional Chinese fine-tuning and efficient multimodal architectures.


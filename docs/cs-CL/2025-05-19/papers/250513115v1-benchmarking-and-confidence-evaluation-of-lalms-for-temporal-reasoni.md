---
layout: default
title: Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning
---

# Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13115" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13115v1</a>
  <a href="https://arxiv.org/pdf/2505.13115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13115v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13115v1', 'Benchmarking and Confidence Evaluation of LALMs For Temporal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Debarpan Bhattacharya, Apoorva Kulkarni, Sriram Ganapathy

**分类**: cs.CL, cs.AI, cs.LG, cs.SD, eess.AS

**发布日期**: 2025-05-19

**备注**: Accepted in INTERSPEECH, 2025, Rotterdam, The Netherlands

---

## 💡 一句话要点

**提出TREA数据集以评估音频语言模型的时间推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频语言模型` `时间推理` `多模态评估` `不确定性度量` `基准测试`

## 📋 核心要点

1. 现有的大型音频语言模型在推理任务上表现不如人类，缺乏有效的评估标准。
2. 本文提出了音频的时间推理评估（TREA）数据集，并引入了一种新的不确定性度量来评估模型的鲁棒性。
3. 基准测试结果显示，开源LALMs在TREA数据集上表现不佳，强调了对模型进行全面评估的必要性。

## 📝 摘要（中文）

随着文本基础的大型语言模型（LLM）的成功，研究者们开始关注将视觉和音频等其他模态与文本结合，以实现类似的多模态能力。为此，本文提出了一种新的数据集——音频的时间推理评估（TREA），用于评估大型音频语言模型（LALMs）在推理相关任务上的表现。通过对开源LALMs的基准测试，发现它们在TREA数据集的任务上始终落后于人类能力。此外，本文还提出了一种不确定性度量，计算模型对语义上相同的输入扰动的不变性。分析表明，准确率与不确定性指标并不一定相关，因此需要对LALMs进行全面评估，以适应高风险应用场景。

## 🔬 方法详解

**问题定义**：本文旨在解决大型音频语言模型（LALMs）在时间推理任务上的评估不足，现有方法主要集中于分类或生成任务，缺乏针对推理能力的专门评估。

**核心思路**：通过构建音频的时间推理评估（TREA）数据集，论文提供了一种新的评估框架，并引入不确定性度量来分析模型对输入扰动的敏感性。

**技术框架**：整体架构包括数据集构建、基准测试和不确定性评估三个主要模块。数据集包含多种时间推理任务，基准测试则对比了多种开源LALMs的表现。

**关键创新**：最重要的创新在于提出了TREA数据集和不确定性度量，前者专注于推理能力的评估，后者揭示了模型准确率与不确定性之间的关系。

**关键设计**：在不确定性度量中，采用了对输入进行语义相似扰动的方式，评估模型的鲁棒性；同时，基准测试中使用了多种LALMs进行对比，确保评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，开源LALMs在TREA数据集上的表现明显低于人类，且准确率与不确定性指标之间并无直接相关性。这一发现强调了在高风险应用中对模型进行全面评估的必要性，推动了对LALMs的进一步研究和优化。

## 🎯 应用场景

该研究的潜在应用领域包括智能助理、自动语音识别和多模态交互系统等。通过提升音频语言模型的推理能力，可以增强这些系统在复杂场景下的表现，进而提高用户体验和系统的智能化水平。未来，该研究可能推动多模态AI的发展，促进不同模态之间的更好融合。

## 📄 摘要（原文）

> The popular success of text-based large language models (LLM) has streamlined the attention of the multimodal community to combine other modalities like vision and audio along with text to achieve similar multimodal capabilities. In this quest, large audio language models (LALMs) have to be evaluated on reasoning related tasks which are different from traditional classification or generation tasks. Towards this goal, we propose a novel dataset called temporal reasoning evaluation of audio (TREA).
>   We benchmark open-source LALMs and observe that they are consistently behind human capabilities on the tasks in the TREA dataset. While evaluating LALMs, we also propose an uncertainty metric, which computes the invariance of the model to semantically identical perturbations of the input. Our analysis shows that the accuracy and uncertainty metrics are not necessarily correlated and thus, points to a need for wholesome evaluation of LALMs for high-stakes applications.


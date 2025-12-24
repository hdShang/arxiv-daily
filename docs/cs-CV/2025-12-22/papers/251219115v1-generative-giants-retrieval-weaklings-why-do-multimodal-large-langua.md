---
layout: default
title: "Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?"
---

# Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19115" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19115v1</a>
  <a href="https://arxiv.org/pdf/2512.19115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19115v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19115v1', 'Generative Giants, Retrieval Weaklings: Why do Multimodal Large Language Models Fail at Multimodal Retrieval?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengyi Feng, Zeang Sheng, Meiyi Qiang, Wentao Zhang

**分类**: cs.CV

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**揭示多模态大语言模型在多模态检索中表现不佳的原因**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `多模态检索` `可解释性分析` `稀疏自编码器` `表示学习`

## 📋 核心要点

1. 现有的多模态大语言模型在生成任务表现出色，但在多模态检索任务中却存在不足，这是一个待解决的核心问题。
2. 论文通过稀疏自编码器分解MLLM的输出表示，分析其内在行为，揭示了文本语义主导和视觉信息不足的问题。
3. 研究发现，MLLM对图像-文本模态的过度桥接导致嵌入同质化，降低了检索所需的区分能力，并指出了干扰检索的特征成分。

## 📝 摘要（中文）

尽管多模态大语言模型(MLLMs)在生成任务中取得了显著成功，但我们观察到它们在零样本多模态检索任务中表现出一种违反直觉的缺陷。本文研究了阻碍MLLMs作为有效检索器的潜在机制。借助稀疏自编码器(SAEs)，我们将MLLM输出表示分解为可解释的语义概念，以探究其内在行为。我们的分析表明，MLLMs的表示空间主要由文本语义主导；对多模态检索至关重要的视觉信息仅占很小一部分。MLLMs过于关注图像-文本模态之间的桥接，这促进了生成，但也使嵌入同质化，最终降低了多模态检索所需的区分能力。我们进一步发现，对MLLMs相似性计算贡献最大的特定特征成分实际上是会降低检索性能的干扰因素。总的来说，我们的工作首次对多模态检索背景下MLLM表示进行了深入的可解释性分析，并为增强MLLMs的多模态检索能力提供了可能的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在多模态检索任务中表现不佳的问题。现有的MLLMs虽然在生成任务上表现出色，但在检索任务中却无法有效利用视觉信息，导致检索性能下降。现有的方法缺乏对MLLM内部表示的深入理解，无法解释其在检索任务中的失败原因。

**核心思路**：论文的核心思路是通过可解释性分析来理解MLLM在多模态检索中的失败原因。具体来说，通过稀疏自编码器（SAEs）将MLLM的输出表示分解为可解释的语义概念，从而揭示MLLM内部表示的结构和信息分布。通过分析这些语义概念，可以确定哪些信息对检索任务至关重要，以及MLLM在哪些方面存在不足。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 使用MLLM处理多模态输入（图像和文本）；2) 获取MLLM的输出表示；3) 使用稀疏自编码器（SAEs）将MLLM的输出表示分解为可解释的语义概念；4) 分析这些语义概念，评估文本和视觉信息在表示空间中的占比；5) 识别对检索性能有负面影响的干扰特征。

**关键创新**：论文最重要的技术创新点在于使用稀疏自编码器（SAEs）对MLLM的输出表示进行可解释性分析。这种方法能够将复杂的MLLM表示分解为易于理解的语义概念，从而揭示MLLM内部的信息处理机制。与传统的黑盒分析方法相比，这种方法能够提供更深入的洞察力，帮助研究人员理解MLLM在多模态检索中的失败原因。

**关键设计**：论文的关键设计包括：1) 选择合适的稀疏自编码器（SAEs）架构，以确保能够有效地分解MLLM的输出表示；2) 设计合适的评估指标，以衡量文本和视觉信息在表示空间中的占比；3) 识别对检索性能有负面影响的干扰特征，并分析其产生的原因；4) 使用标准的多模态检索数据集进行实验，以验证所提出的分析方法的有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19115v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19115v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19115v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验发现，MLLM的表示空间主要由文本语义主导，视觉信息占比很小。同时，对相似性计算贡献最大的特征成分反而会降低检索性能。这些发现为改进MLLM的多模态检索能力提供了重要的指导。

## 🎯 应用场景

该研究成果可应用于提升多模态信息检索系统的性能，例如图像搜索、视频搜索等。通过理解MLLM在检索任务中的不足，可以设计更有效的多模态检索模型，提高检索准确率和用户体验。此外，该研究也有助于开发更可靠的多模态理解和推理系统，例如智能问答、视觉对话等。

## 📄 摘要（原文）

> Despite the remarkable success of multimodal large language models (MLLMs) in generative tasks, we observe that they exhibit a counterintuitive deficiency in the zero-shot multimodal retrieval task. In this work, we investigate the underlying mechanisms that hinder MLLMs from serving as effective retrievers. With the help of sparse autoencoders (SAEs), we decompose MLLM output representations into interpretable semantic concepts to probe their intrinsic behavior. Our analysis reveals that the representation space of MLLMs is overwhelmingly dominated by textual semantics; the visual information essential for multimodal retrieval only constitutes a small portion. This imbalance is compounded by the heavy focus of MLLMs on bridging image-text modalities, which facilitates generation but homogenizes embeddings and finally diminishes the discriminative power required for multimodal retrieval. We further discover that the specific feature components that contribute most to the similarity computations for MLLMs are in fact distractors that actively degrade retrieval performance. Overall, our work provides the first in-depth interpretability analysis of MLLM representations in the context of multimodal retrieval and offers possible directions for enhancing the multimodal retrieval capabilities of MLLMs.


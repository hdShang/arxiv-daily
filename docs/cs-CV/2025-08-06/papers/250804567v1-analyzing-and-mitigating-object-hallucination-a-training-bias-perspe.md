---
layout: default
title: "Analyzing and Mitigating Object Hallucination: A Training Bias Perspective"
---

# Analyzing and Mitigating Object Hallucination: A Training Bias Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04567" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04567v1</a>
  <a href="https://arxiv.org/pdf/2508.04567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04567v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04567v1', 'Analyzing and Mitigating Object Hallucination: A Training Bias Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Li, Kun Zhou, Wayne Xin Zhao, Lei Fang, Ji-Rong Wen

**分类**: cs.CV, cs.CL

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出Obliviate以解决大视觉语言模型的物体幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型视觉语言模型` `物体幻觉` `去学习` `多模态学习` `训练偏差` `反事实图像` `模型微调`

## 📋 核心要点

1. 当前大型视觉语言模型在生成文本时存在幻觉问题，导致生成内容与视觉输入不一致。
2. 本文提出Obliviate方法，通过去学习训练偏差来减轻物体幻觉，专注于语言建模头的更新。
3. 实验结果显示，Obliviate在多个任务上显著降低幻觉现象，且仅需更新约2%的模型参数。

## 📝 摘要（中文）

随着训练数据规模的扩大，大型视觉语言模型（LVLMs）的多模态能力显著提升，但仍然存在幻觉问题，即生成与视觉输入不一致的文本。本文系统研究了训练数据在幻觉中的作用，并引入了新基准POPEv2，发现当前LVLMs存在训练偏差，无法充分利用训练数据，导致在训练中见过的图像上幻觉频繁。为此，提出了一种高效的去学习方法Obliviate，通过识别训练数据中真实标签与模型输出之间的差异来减轻物体幻觉。实验表明，Obliviate在更新约2%的参数的情况下，显著减少了幻觉现象，且在模型规模和训练数据量上具有良好的可扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型（LVLMs）在生成文本时的物体幻觉问题。现有方法未能充分利用训练数据，导致在训练中见过的图像上幻觉频繁，尤其是在处理反事实图像时表现不佳。

**核心思路**：论文提出的Obliviate方法通过去学习训练偏差来减轻物体幻觉。该方法识别训练数据中真实标签与模型输出之间的差异，作为偏差的代理，并采用高效的微调策略，仅更新语言建模头。

**技术框架**：Obliviate的整体架构包括数据收集、偏差识别和模型微调三个主要模块。首先，通过POPEv2基准收集反事实图像；然后，识别模型在这些图像上的偏差；最后，进行针对性的微调以减少幻觉现象。

**关键创新**：Obliviate的主要创新在于其高效的去学习策略，能够在不大幅度更新模型参数的情况下，显著降低幻觉现象。这与现有方法的全面重训练策略形成鲜明对比。

**关键设计**：在设计上，Obliviate仅更新约2%的模型参数，采用了参数和数据高效的微调策略。损失函数设计上，关注真实标签与模型输出的差异，确保模型在训练数据上更好地学习和适应。

## 📊 实验亮点

实验结果表明，Obliviate在多个任务上显著降低了幻觉现象，尤其是在处理反事实图像时，模型的性能提升幅度达到显著水平。尽管仅更新了约2%的参数，Obliviate在不同规模的模型（从2B到72B）和训练数据量上均表现出良好的可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括智能图像描述、视觉问答和多模态内容生成等。通过减轻幻觉现象，Obliviate能够提升这些应用的准确性和可靠性，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> As scaling up training data has significantly improved the general multimodal capabilities of Large Vision-Language Models (LVLMs), they still suffer from the hallucination issue, generating text that is inconsistent with the visual input. This phenomenon motivates us to systematically investigate the role of training data in hallucination. We introduce a new benchmark, POPEv2, which consists of counterfactual images collected from the training data of LVLMs with certain objects masked. Through comprehensive evaluation on POPEv2, we find that current LVLMs suffer from training bias: they fail to fully leverage their training data and hallucinate more frequently on images seen during training. Specifically, they perform poorly on counterfactual images, often incorrectly answering ``Yes'' to questions about masked objects. To understand this issue, we conduct probing experiments on the models' internal components, revealing that this training bias is primarily located in the language modeling (LM) head. Based on these findings, we propose Obliviate, an efficient and lightweight unlearning method designed to mitigate object hallucination via training bias unlearning. Obliviate identifies the discrepancy between ground-truth labels and model outputs on the training data as a proxy for bias and adopts a parameter- and data-efficient fine-tuning strategy that only updates the LM head. Extensive experiments demonstrate the effectiveness of our approach. While only reusing the training data and updating approximately 2\% of the parameters, Obliviate significantly reduces hallucination across both discriminative and generative tasks. Furthermore, it demonstrates strong scalability with respect to both model size (2B to 72B) and training data volume, and exhibits promising generalization to hallucination types beyond object-level hallucination. Our code and data will be publicly released.


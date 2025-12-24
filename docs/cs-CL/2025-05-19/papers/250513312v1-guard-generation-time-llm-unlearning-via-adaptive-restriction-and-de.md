---
layout: default
title: "GUARD: Generation-time LLM Unlearning via Adaptive Restriction and Detection"
---

# GUARD: Generation-time LLM Unlearning via Adaptive Restriction and Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13312" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13312v1</a>
  <a href="https://arxiv.org/pdf/2505.13312.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13312v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13312v1', 'GUARD: Generation-time LLM Unlearning via Adaptive Restriction and Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhijie Deng, Chris Yuhao Liu, Zirui Pang, Xinlei He, Lei Feng, Qi Xuan, Zhaowei Zhu, Jiaheng Wei

**分类**: cs.CL

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出GUARD框架以解决大语言模型的选择性遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `选择性遗忘` `动态检测` `文本生成` `安全性` `合规性` `知识管理`

## 📋 核心要点

1. 现有的遗忘方法通常依赖于微调，导致遗忘与保留知识之间的决策边界模糊，影响模型性能。
2. GUARD框架通过在生成时动态检测和过滤遗忘目标，避免了微调带来的负面影响，确保文本生成的流畅性。
3. 在多个数据集上的实验结果显示，GUARD在遗忘质量上表现优异，同时对模型的通用能力几乎没有影响。

## 📝 摘要（中文）

大语言模型（LLMs）在记忆大量知识方面表现出色，但选择性遗忘特定知识的能力对于确保模型的安全性和合规性至关重要。现有的遗忘方法通常需要通过微调模型来实现，这会模糊遗忘与保留知识之间的决策边界，影响整体性能。为避免微调带来的负面影响，本文提出了GUARD框架，允许在生成过程中动态地进行遗忘。该框架通过提示分类器检测遗忘目标并提取相应的禁用标记，结合标记匹配和语义匹配动态惩罚和过滤候选标记，有效防止模型泄露遗忘内容。实验结果表明，GUARD在多个任务上实现了强大的遗忘质量，同时几乎没有降低LLM的整体能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在生成过程中选择性遗忘特定知识的能力不足问题。现有方法通过微调模型来实现遗忘，但这会影响模型的整体性能和决策边界。

**核心思路**：GUARD框架的核心思想是在生成过程中动态地检测和过滤与遗忘目标相关的内容。通过使用提示分类器识别遗忘目标，GUARD能够在不影响文本流畅性的情况下，安全地防止模型生成相关响应。

**技术框架**：GUARD的整体架构包括两个主要模块：提示分类器和动态惩罚过滤机制。提示分类器负责检测遗忘目标并提取禁用标记，而动态惩罚过滤机制则在生成过程中对候选标记进行惩罚和过滤。

**关键创新**：GUARD的创新之处在于其在生成时动态进行遗忘，而不是依赖于传统的微调方法。这种方法有效地避免了遗忘与保留知识之间的决策模糊性，保持了模型的生成能力。

**关键设计**：GUARD采用了标记匹配和语义匹配的组合来动态惩罚和过滤候选标记，确保生成内容不泄露遗忘的知识。具体的参数设置和损失函数设计在实验中经过优化，以实现最佳的遗忘效果。

## 📊 实验亮点

在对哈利·波特数据集和MUSE基准的版权内容遗忘任务，以及TOFU数据集的实体遗忘任务中，GUARD表现出色，遗忘质量显著提升，同时对模型的通用能力几乎没有影响，展示了良好的遗忘与效用之间的平衡。

## 🎯 应用场景

GUARD框架具有广泛的应用潜力，特别是在需要保护敏感信息或遵循法律法规的场景中，如版权内容管理和个人隐私保护。未来，该方法可以扩展到更多领域，提升大语言模型的安全性和合规性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated strong capabilities in memorizing vast amounts of knowledge across diverse domains. However, the ability to selectively forget specific knowledge is critical for ensuring the safety and compliance of deployed models. Existing unlearning efforts typically fine-tune the model with resources such as forget data, retain data, and a calibration model. These additional gradient steps blur the decision boundary between forget and retain knowledge, making unlearning often at the expense of overall performance. To avoid the negative impact of fine-tuning, it would be better to unlearn solely at inference time by safely guarding the model against generating responses related to the forget target, without destroying the fluency of text generation. In this work, we propose Generation-time Unlearning via Adaptive Restriction and Detection (GUARD), a framework that enables dynamic unlearning during LLM generation. Specifically, we first employ a prompt classifier to detect unlearning targets and extract the corresponding forbidden token. We then dynamically penalize and filter candidate tokens during generation using a combination of token matching and semantic matching, effectively preventing the model from leaking the forgotten content. Experimental results on copyright content unlearning tasks over the Harry Potter dataset and the MUSE benchmark, as well as entity unlearning tasks on the TOFU dataset, demonstrate that GUARD achieves strong forget quality across various tasks while causing almost no degradation to the LLM's general capabilities, striking an excellent trade-off between forgetting and utility.


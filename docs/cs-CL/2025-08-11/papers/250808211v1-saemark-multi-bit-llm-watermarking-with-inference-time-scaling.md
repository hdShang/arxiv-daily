---
layout: default
title: "SAEMark: Multi-bit LLM Watermarking with Inference-Time Scaling"
---

# SAEMark: Multi-bit LLM Watermarking with Inference-Time Scaling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08211" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08211v1</a>
  <a href="https://arxiv.org/pdf/2508.08211.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08211v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08211v1', 'SAEMark: Multi-bit LLM Watermarking with Inference-Time Scaling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuohao Yu, Xingru Jiang, Weizheng Gu, Yidong Wang, Shikun Zhang, Wei Ye

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-11

**备注**: 24 pages, 12 figures, code available: https://zhuohaoyu.github.io/SAEMark

---

## 💡 一句话要点

**提出SAEMark以解决LLM水印质量与可访问性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `水印技术` `大规模语言模型` `文本生成` `特征提取` `拒绝采样` `内容归属` `虚假信息防范`

## 📋 核心要点

1. 现有的水印方法在文本质量、模型访问和日志操作上存在显著不足，限制了其在API模型和多语言场景中的应用。
2. SAEMark提出了一种后处理的多位水印框架，通过推理时的特征基础拒绝采样嵌入个性化信息，避免了对模型日志的修改。
3. 实验结果表明，SAEMark在四个数据集上均表现出色，尤其在英语文本上达到了99.7%的F1分数，展现了其强大的多位检测能力。

## 📝 摘要（中文）

为了解决大规模语言模型（LLM）生成文本的水印问题，本文提出了SAEMark框架。现有方法在文本质量、模型访问和日志操作上存在局限，无法适用于API模型和多语言场景。SAEMark通过推理时的特征基础拒绝采样嵌入个性化信息，无需修改模型日志或重新训练。该方法基于从生成文本中提取的确定性特征，选择与目标特征统计一致的输出，确保文本质量。实验结果表明，SAEMark在多个数据集上表现出色，尤其在英语文本上达到了99.7%的F1分数，展示了其在可扩展水印方面的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大规模语言模型水印方法在文本质量、模型访问和日志操作上的不足，特别是无法适用于API模型和多语言场景的问题。

**核心思路**：SAEMark通过推理时的特征基础拒绝采样来嵌入个性化信息，避免了对模型日志的修改和重新训练，从而保持了文本的质量。

**技术框架**：SAEMark的整体架构包括特征提取、目标特征统计匹配和拒绝采样三个主要模块。首先，从生成的文本中提取确定性特征，然后选择与目标特征统计一致的输出，最后通过拒绝采样生成带水印的文本。

**关键创新**：SAEMark的主要创新在于其后处理的多位水印框架，能够在不修改模型日志的情况下实现个性化信息的嵌入，这与现有方法的本质区别在于不再依赖于白盒模型访问和日志操作。

**关键设计**：在技术细节上，SAEMark使用稀疏自编码器（SAEs）作为特征提取器，并提供了与水印成功概率和计算预算相关的理论保证，确保其在任何合适的特征提取器上均有效。实验中展示了其在多个数据集上的一致性表现。

## 📊 实验亮点

SAEMark在四个数据集上的实验结果显示，其在英语文本上的F1分数高达99.7%，并且在多位检测准确性方面表现优异，显著优于现有方法。这表明SAEMark在保持文本质量的同时，能够有效实现水印功能，具有较强的实用性和可扩展性。

## 🎯 应用场景

SAEMark的研究成果在内容归属和防止虚假信息传播方面具有重要应用价值。该框架能够广泛应用于多语言和多领域的文本生成任务，尤其适用于需要保护生成内容的场景，如新闻、社交媒体和学术出版等。未来，SAEMark有望推动水印技术的标准化和普及，提升内容的可追溯性。

## 📄 摘要（原文）

> Watermarking LLM-generated text is critical for content attribution and misinformation prevention. However, existing methods compromise text quality, require white-box model access and logit manipulation. These limitations exclude API-based models and multilingual scenarios. We propose SAEMark, a general framework for post-hoc multi-bit watermarking that embeds personalized messages solely via inference-time, feature-based rejection sampling without altering model logits or requiring training. Our approach operates on deterministic features extracted from generated text, selecting outputs whose feature statistics align with key-derived targets. This framework naturally generalizes across languages and domains while preserving text quality through sampling LLM outputs instead of modifying. We provide theoretical guarantees relating watermark success probability and compute budget that hold for any suitable feature extractor. Empirically, we demonstrate the framework's effectiveness using Sparse Autoencoders (SAEs), achieving superior detection accuracy and text quality. Experiments across 4 datasets show SAEMark's consistent performance, with 99.7% F1 on English and strong multi-bit detection accuracy. SAEMark establishes a new paradigm for scalable watermarking that works out-of-the-box with closed-source LLMs while enabling content attribution.


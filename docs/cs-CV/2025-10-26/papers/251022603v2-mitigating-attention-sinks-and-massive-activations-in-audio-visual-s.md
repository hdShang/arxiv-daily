---
layout: default
title: Mitigating Attention Sinks and Massive Activations in Audio-Visual Speech Recognition with LLMs
---

# Mitigating Attention Sinks and Massive Activations in Audio-Visual Speech Recognition with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22603" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22603v2</a>
  <a href="https://arxiv.org/pdf/2510.22603.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22603v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22603v2', 'Mitigating Attention Sinks and Massive Activations in Audio-Visual Speech Recognition with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anand, Umberto Cappellazzo, Stavros Petridis, Maja Pantic

**分类**: eess.AS, cs.CV, cs.SD

**发布日期**: 2025-10-26 (更新: 2025-11-02)

**备注**: The code is available at https://github.com/umbertocappellazzo/Llama-AVSR

---

## 💡 一句话要点

**针对AVSR中LLM的Attention Sink问题，提出解耦损失以提升识别精度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视听语音识别` `大型语言模型` `注意力机制` `Attention Sink` `解耦损失`

## 📋 核心要点

1. 现有基于LLM的AVSR方法缺乏对模型内部动态的深入理解，存在Attention Sink和Massive Activation问题。
2. 论文提出一种解耦损失，旨在降低BOS token与其他token的余弦相似度，从而缓解中间sink和巨大激活。
3. 实验表明，该方法在高特征下采样率下能有效提升WER，并在低采样率下保持性能稳定。

## 📝 摘要（中文）

大型语言模型（LLM）最近在听觉语音识别（ASR）、视觉语音识别（VSR）和视听语音识别（AVSR）方面取得了进展。然而，对其微调下的内部动态的理解仍然有限。在自然语言处理中，最近的研究揭示了注意力汇聚（attention sinks），即吸引不成比例的高注意力的token，以及相关的巨大激活（massive activations），其中sink token的某些特征在LLM中表现出巨大的激活。在这项工作中，我们首次研究了多模态语音识别中的这些现象。通过对视听LLM的详细分析，我们不仅在BOS token处，而且在ASR、VSR和AVSR的中间低语义token处识别出注意力汇聚和巨大激活。我们表明，巨大激活源于MLP层，并且对应于所有sink token中的固定特征索引。我们进一步表明，中间sink token与BOS token表现出高的余弦相似度，从而放大了注意力和激活。基于这些见解，我们引入了一种简单的解耦损失，该损失降低了BOS和其他token之间的余弦相似度，从而有效地减轻了中间sink和巨大激活。此外，我们的方法在高的视听特征下采样下提高了词错误率（WER），同时在较低的下采样率下保持稳定。

## 🔬 方法详解

**问题定义**：论文旨在解决基于LLM的AVSR模型中存在的Attention Sink和Massive Activation问题。现有方法在微调LLM时，对模型内部动态理解不足，导致某些token（尤其是BOS token和中间低语义token）吸引了过多的注意力，进而引发了巨大的激活，影响了模型的性能。

**核心思路**：论文的核心思路是降低BOS token与其他token之间的余弦相似度，从而减少Attention Sink效应。作者观察到，中间sink token与BOS token具有很高的余弦相似度，这会放大注意力和激活。通过降低这种相似性，可以有效地缓解中间sink和巨大激活。

**技术框架**：论文主要研究了基于LLM的AVSR模型，并针对Attention Sink问题提出了改进方案。整体框架包括：1）使用LLM作为AVSR模型的主干网络；2）分析模型中Attention Sink和Massive Activation的现象；3）提出解耦损失函数，用于降低BOS token与其他token的余弦相似度；4）在AVSR任务上进行实验，评估所提出方法的性能。

**关键创新**：论文的关键创新在于：1）首次在多模态语音识别领域研究了Attention Sink和Massive Activation现象；2）提出了一种简单有效的解耦损失函数，用于缓解Attention Sink问题。该损失函数直接作用于token embedding空间，降低了BOS token与其他token的余弦相似度，从而减少了不必要的注意力集中。

**关键设计**：论文的关键设计在于解耦损失函数。该损失函数的目标是最小化BOS token与其他token之间的余弦相似度。具体来说，对于每个token embedding，计算其与BOS token embedding的余弦相似度，并将这些相似度作为损失项进行优化。损失函数的具体形式未知，但其核心思想是降低token embedding空间中BOS token与其他token的相似性。

## 📊 实验亮点

实验结果表明，所提出的解耦损失在高视听特征下采样率下能够显著提高AVSR模型的词错误率（WER），同时在较低的下采样率下保持性能稳定。这表明该方法能够有效地缓解Attention Sink问题，并提高模型在不同条件下的鲁棒性。具体的WER提升幅度未知。

## 🎯 应用场景

该研究成果可应用于各种视听语音识别系统，尤其是在资源受限或噪声环境下。通过缓解Attention Sink问题，可以提高AVSR模型的鲁棒性和准确性，从而改善语音助手、视频会议、字幕生成等应用的用户体验。此外，该研究对于理解和优化多模态LLM具有重要的理论价值。

## 📄 摘要（原文）

> Large language models (LLMs) have recently advanced auditory speech recognition (ASR), visual speech recognition (VSR), and audio-visual speech recognition (AVSR). However, understanding of their internal dynamics under fine-tuning remains limited. In natural language processing, recent work has revealed attention sinks, tokens that attract disproportionately high attention, and associated massive activations in which some features of sink tokens exhibit huge activation in LLMs. In this work, we are the first to study these phenomena in multimodal speech recognition. Through a detailed analysis of audio-visual LLMs, we identify attention sinks and massive activations not only at the BOS token but also at intermediate low-semantic tokens across ASR, VSR, and AVSR. We show that massive activations originate in the MLP layers and correspond to fixed feature indices across all sink tokens. We further show that intermediate sink tokens exhibit high cosine similarity to the BOS token, thereby amplifying attention and activation. Building on these insights, we introduce a simple decorrelation loss that reduces cosine similarity between BOS and other tokens, effectively mitigating intermediate sinks and massive activations. Furthermore, our method improves word error rate (WER) under high audio-visual feature downsampling while remaining stable at lower downsampling rates.


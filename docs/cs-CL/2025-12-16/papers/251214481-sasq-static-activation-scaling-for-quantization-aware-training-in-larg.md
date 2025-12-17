---
layout: default
title: SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models
---

# SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14481" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14481</a>
  <a href="https://arxiv.org/pdf/2512.14481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14481" onclick="toggleFavorite(this, '2512.14481', 'SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shizhuo Mao, Song Chen, Yi Kang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**SASQ：一种用于大语言模型量化感知训练的静态激活缩放方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `量化感知训练` `静态量化` `激活量化` `模型压缩`

## 📋 核心要点

1. 现有大模型量化方法在精度、计算开销和部署效率之间存在权衡，静态量化精度低，动态量化开销大，权重训练成本高。
2. SASQ通过仅优化激活量化因子，避免了权重训练的开销，实现了高精度和高效率的静态量化推理。
3. 实验表明，SASQ在LLaMA2-7B模型上优于现有SOTA量化方案，甚至超过了FP16模型的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言任务中表现出色，但其不断增长的规模超过了GPU内存的发展速度，给部署带来了挑战。模型量化通过降低权重和激活的精度来缓解这个问题，但现有的解决方案面临着根本性的权衡：动态量化会产生很高的计算开销，并在边缘设备上带来部署挑战，而静态量化会牺牲精度。现有的量化感知训练（QAT）方法进一步受到权重训练成本的困扰。我们提出了SASQ：一个轻量级的QAT框架，专门为激活量化因子量身定制。SASQ仅优化量化因子（不改变预训练权重），从而实现高精度的静态推理，同时保持部署效率。SASQ自适应地截断一些异常值，从而降低了量化的难度，同时保留了激活的分布特征。SASQ不仅超越了现有的SOTA量化方案，而且优于相应的FP16模型。在LLaMA2-7B上，它在WikiText2上的困惑度比QuaRot低5.2%，比FP16模型低4.7%。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型量化过程中，静态量化精度损失和动态量化计算开销大的问题。现有的量化感知训练（QAT）方法通常需要对权重进行微调，导致训练成本高昂。因此，如何在保证精度的前提下，实现高效的静态量化，是本文要解决的核心问题。

**核心思路**：SASQ的核心思路是仅优化激活的量化因子，而不改变预训练的权重。通过这种方式，可以避免权重训练带来的高昂计算成本，同时实现静态量化，从而保证部署效率。此外，SASQ还引入了自适应截断机制，以降低量化难度，并保留激活的分布特征。

**技术框架**：SASQ的整体框架包括以下几个主要步骤：1) 加载预训练的大语言模型；2) 对激活进行量化，并引入可学习的量化因子；3) 使用量化后的模型进行前向传播，计算损失；4) 仅更新量化因子，保持预训练权重不变；5) 重复步骤3和4，直到量化因子收敛。最终得到一个量化后的模型，可以进行高效的静态推理。

**关键创新**：SASQ的关键创新在于：1) 仅优化激活量化因子，避免了权重训练的开销；2) 引入自适应截断机制，降低了量化难度，并保留了激活的分布特征。与现有方法相比，SASQ在保证精度的前提下，显著提高了量化效率。

**关键设计**：SASQ的关键设计包括：1) 量化因子的初始化策略，需要保证量化后的激活值能够尽可能地接近原始激活值；2) 自适应截断机制的具体实现，需要根据激活值的分布动态调整截断阈值；3) 损失函数的选择，需要能够反映量化误差，并引导量化因子朝着最优方向更新。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14481/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14481/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14481/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SASQ在LLaMA2-7B模型上进行了实验，结果表明，SASQ在WikiText2数据集上的困惑度比QuaRot低5.2%，比FP16模型低4.7%。这表明SASQ不仅超越了现有的SOTA量化方案，而且优于相应的FP16模型，实现了显著的性能提升。

## 🎯 应用场景

SASQ适用于对计算资源和延迟有严格要求的场景，例如边缘设备上的大语言模型部署。通过高效的静态量化，SASQ可以降低模型大小和计算复杂度，从而使大语言模型能够在资源受限的设备上运行，并加速推理过程。这对于智能手机、物联网设备等应用具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) excel at natural language tasks but face deployment challenges due to their growing size outpacing GPU memory advancements. Model quantization mitigates this issue by lowering weight and activation precision, but existing solutions face fundamental trade-offs: dynamic quantization incurs high computational overhead and poses deployment challenges on edge devices, while static quantization sacrifices accuracy. Existing approaches of quantization-aware training (QAT) further suffer from weight training costs. We propose SASQ: a lightweight QAT framework specifically tailored for activation quantization factors. SASQ exclusively optimizes only the quantization factors (without changing pre-trained weights), enabling static inference with high accuracy while maintaining deployment efficiency. SASQ adaptively truncates some outliers, thereby reducing the difficulty of quantization while preserving the distributional characteristics of the activations. SASQ not only surpasses existing SOTA quantization schemes but also outperforms the corresponding FP16 models. On LLaMA2-7B, it achieves 5.2% lower perplexity than QuaRot and 4.7% lower perplexity than the FP16 model on WikiText2.


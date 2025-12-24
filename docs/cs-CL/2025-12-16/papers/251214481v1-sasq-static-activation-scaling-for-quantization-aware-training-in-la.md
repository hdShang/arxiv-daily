---
layout: default
title: "SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models"
---

# SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14481" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14481v1</a>
  <a href="https://arxiv.org/pdf/2512.14481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14481v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14481v1', 'SASQ: Static Activation Scaling for Quantization-Aware Training in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shizhuo Mao, Song Chen, Yi Kang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**SASQ：一种面向大语言模型激活量化的静态激活缩放量化感知训练方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `量化感知训练` `模型量化` `静态量化` `激活量化`

## 📋 核心要点

1. 现有大语言模型量化方法在精度、计算开销和部署效率之间存在权衡，静态量化损失精度，动态量化开销过高。
2. SASQ通过仅优化激活量化因子，避免了权重训练的开销，实现了高精度和高效率的静态量化推理。
3. 实验表明，SASQ在LLaMA2-7B上优于现有SOTA量化方案，甚至超过了FP16模型，降低了WikiText2上的困惑度。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言任务中表现出色，但其不断增长的规模超过了GPU内存的发展速度，给部署带来了挑战。模型量化通过降低权重和激活的精度来缓解这个问题，但现有的解决方案面临着根本性的权衡：动态量化会产生很高的计算开销，并且在边缘设备上部署具有挑战性，而静态量化会牺牲精度。现有的量化感知训练（QAT）方法进一步受到权重训练成本的影响。我们提出了SASQ：一个轻量级的QAT框架，专门为激活量化因子量身定制。SASQ仅优化量化因子（不改变预训练的权重），从而以高精度实现静态推理，同时保持部署效率。SASQ自适应地截断一些异常值，从而降低了量化的难度，同时保留了激活的分布特征。SASQ不仅超越了现有的SOTA量化方案，而且优于相应的FP16模型。在LLaMA2-7B上，它在WikiText2上的困惑度比QuaRot低5.2%，比FP16模型低4.7%。

## 🔬 方法详解

**问题定义**：现有的大语言模型量化方法，如动态量化，虽然能保持较高的精度，但由于需要在推理过程中进行额外的计算，导致计算开销显著增加，不适合在边缘设备上部署。静态量化虽然部署效率高，但精度损失较大。量化感知训练（QAT）虽然可以提高精度，但训练权重的成本很高，特别是对于大型语言模型来说，计算资源消耗巨大。因此，需要一种既能保持精度，又能实现高效静态推理的量化方法。

**核心思路**：SASQ的核心思路是只优化激活的量化因子，而不改变预训练模型的权重。通过这种方式，可以避免权重训练带来的巨大计算开销，同时仍然能够通过调整激活的量化范围来提高量化精度。此外，SASQ还引入了自适应截断机制，用于处理激活中的异常值，从而降低量化的难度，并保留激活的分布特征。

**技术框架**：SASQ框架主要包含以下几个阶段：1) 加载预训练的大语言模型；2) 对模型的激活进行量化，并引入可学习的量化因子；3) 使用少量数据对量化因子进行训练，同时保持预训练权重不变；4) 在推理阶段，使用固定的量化因子进行静态量化推理。

**关键创新**：SASQ最重要的技术创新在于只优化激活的量化因子，避免了权重训练的开销。与传统的QAT方法相比，SASQ大大降低了训练成本，使其能够应用于更大的模型。此外，自适应截断机制也是一个重要的创新，它能够有效地处理激活中的异常值，提高量化精度。

**关键设计**：SASQ的关键设计包括：1) 量化因子的初始化策略，需要保证量化后的激活值能够尽可能地保留原始激活的信息；2) 自适应截断阈值的选择，需要根据激活的分布动态调整，以平衡量化精度和异常值的处理；3) 损失函数的设计，需要能够有效地指导量化因子的优化，使其能够最小化量化误差。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14481v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14481v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14481v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SASQ在LLaMA2-7B模型上进行了实验，结果表明，SASQ的性能优于现有的SOTA量化方案，例如QuaRot。具体来说，SASQ在WikiText2数据集上的困惑度比QuaRot低5.2%，甚至比FP16模型低4.7%。这些结果表明，SASQ能够在保持高精度的同时，实现高效的静态量化推理。

## 🎯 应用场景

SASQ具有广泛的应用前景，尤其是在资源受限的边缘设备上部署大型语言模型。例如，可以将SASQ应用于智能手机、嵌入式系统和物联网设备，从而实现高效的自然语言处理和理解。此外，SASQ还可以用于降低云计算中心的计算成本，提高服务器的利用率。未来，SASQ有望成为大语言模型量化的主流方法之一。

## 📄 摘要（原文）

> Large language models (LLMs) excel at natural language tasks but face deployment challenges due to their growing size outpacing GPU memory advancements. Model quantization mitigates this issue by lowering weight and activation precision, but existing solutions face fundamental trade-offs: dynamic quantization incurs high computational overhead and poses deployment challenges on edge devices, while static quantization sacrifices accuracy. Existing approaches of quantization-aware training (QAT) further suffer from weight training costs. We propose SASQ: a lightweight QAT framework specifically tailored for activation quantization factors. SASQ exclusively optimizes only the quantization factors (without changing pre-trained weights), enabling static inference with high accuracy while maintaining deployment efficiency. SASQ adaptively truncates some outliers, thereby reducing the difficulty of quantization while preserving the distributional characteristics of the activations. SASQ not only surpasses existing SOTA quantization schemes but also outperforms the corresponding FP16 models. On LLaMA2-7B, it achieves 5.2% lower perplexity than QuaRot and 4.7% lower perplexity than the FP16 model on WikiText2.


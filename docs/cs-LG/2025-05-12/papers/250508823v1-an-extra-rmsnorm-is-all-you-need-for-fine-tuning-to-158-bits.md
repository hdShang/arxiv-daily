---
layout: default
title: An Extra RMSNorm is All You Need for Fine Tuning to 1.58 Bits
---

# An Extra RMSNorm is All You Need for Fine Tuning to 1.58 Bits

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08823" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08823v1</a>
  <a href="https://arxiv.org/pdf/2505.08823.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08823v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08823v1', 'An Extra RMSNorm is All You Need for Fine Tuning to 1.58 Bits')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cody Steinmetz, Gavin Childress, Aaron Herbst, Gavin Jones, Jasdeep Singh, Eli Vang, Keagan Weinstock

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出RMSNorm以稳定微调至1.58位的低比特量化模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化模型` `RMS归一化` `自然语言处理` `低比特推理` `模型微调`

## 📋 核心要点

1. 现有的量化方法在降低模型复杂度的同时，往往导致准确性显著下降，尤其是在三元量化时更为明显。
2. 本文提出在每个线性投影前插入RMS归一化，并采用逐层量化调度，以稳定微调全精度模型至低比特量化模型。
3. 实验结果表明，该方法在标准语言建模基准上与复杂的知识蒸馏方法相当或更优，且未增加模型复杂性。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理领域带来了变革，但其规模使得实际部署成本高昂。后训练量化虽然能减少内存和计算需求，但常常导致准确性下降，而量化感知训练则需要额外的训练时间。将量化推向三元（2位）范围可以获得更大的节省，但通常不稳定。基于近期研究，本文展示了在每个线性投影前插入RMS归一化，并应用逐层量化调度，可以稳定地将全精度检查点微调为三元LLMs。该方法在标准语言建模基准上与更复杂的知识蒸馏管道相匹配或超越，而无需增加模型复杂性。这些结果表明，细致的归一化可以缩小三元与全精度LLMs之间的准确性差距，使超低比特推理变得可行。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在量化过程中准确性下降的问题，尤其是在推向三元量化时的稳定性不足。现有方法在降低模型复杂度的同时，常常导致性能显著下降。

**核心思路**：论文提出在每个线性投影前插入RMS归一化，并采用逐层量化调度，以稳定地将全精度检查点微调为三元LLMs。这样的设计旨在通过细致的归一化来提高模型的稳定性和准确性。

**技术框架**：整体架构包括全精度模型的初始化、RMS归一化的插入、逐层量化调度的实施，以及最终的微调过程。主要模块包括数据预处理、模型构建、训练过程和评估阶段。

**关键创新**：最重要的技术创新点在于通过简单的RMS归一化方法，显著提高了三元量化模型的性能，缩小了与全精度模型之间的准确性差距。这与传统的知识蒸馏方法形成鲜明对比。

**关键设计**：在模型设计中，RMS归一化被应用于每个线性投影层，量化调度则是逐层进行，确保每一层的稳定性。此外，损失函数的选择和训练策略也经过精心设计，以适应低比特量化的需求。

## 📊 实验亮点

实验结果显示，采用RMS归一化的微调方法在标准语言建模基准上达到了1.58位的精度，且在性能上与更复杂的知识蒸馏管道相当或更优，展现出显著的提升幅度，验证了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能助手、自动翻译等需要高效推理的场景。通过实现超低比特量化，模型的内存和计算需求大幅降低，使得在资源受限的设备上部署大型语言模型成为可能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large language models (LLMs) have transformed natural-language processing, yet their scale makes real-world deployment costly. Post-training quantization reduces memory and computation but often degrades accuracy, while quantization-aware training can recover performance at the cost of extra training. Pushing quantization to the ternary (2-bit) regime yields even larger savings but is notoriously unstable. Building on recent work showing that a bias-free, RMS-normalized Transformer with straight-through estimation can reach 1.58-bit precision, we demonstrate that simply inserting RMS normalization before every linear projection and applying a gradual, layer-wise quantization schedule stably fine-tunes full-precision checkpoints into ternary LLMs. Our approach matches or surpasses more elaborate knowledge-distillation pipelines on standard language-modeling benchmarks without adding model complexity. These results indicate that careful normalization alone can close much of the accuracy gap between ternary and full-precision LLMs, making ultra-low-bit inference practical.


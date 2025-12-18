---
layout: default
title: Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs
---

# Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13795" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13795v3</a>
  <a href="https://arxiv.org/pdf/2510.13795.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13795v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13795v3', 'Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Zhang, Bolin Ni, Xin-Sheng Chen, Heng-Rui Zhang, Yongming Rao, Houwen Peng, Qinglin Lu, Han Hu, Meng-Hao Guo, Shi-Min Hu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-15 (更新: 2025-11-11)

**备注**: homepage: https://open-bee.github.io/

---

## 💡 一句话要点

**提出Honey-Data-15M数据集和Bee-8B模型，提升全开源多模态大语言模型性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `开源数据集` `数据清洗` `思维链` `监督微调` `数据增强` `模型训练`

## 📋 核心要点

1. 现有开源多模态大语言模型在数据质量和复杂推理能力上存在不足，限制了其性能提升。
2. 论文提出Honey-Data-15M数据集，通过清洗和双层CoT增强，提升数据质量和推理能力。
3. 训练的Bee-8B模型在全开源MLLM中达到新的SOTA，性能可与半开源模型媲美。

## 📝 摘要（中文）

当前全开源多模态大语言模型(MLLM)落后于专有模型，主要原因是监督微调(SFT)的数据质量存在显著差距。现有开源数据集通常存在大量噪声，且缺乏复杂的推理数据，如思维链(CoT)，这阻碍了高级模型能力的开发。为了解决这些挑战，本文做出了三个主要贡献。首先，我们引入了Honey-Data-15M，这是一个包含约1500万个QA对的新SFT数据集，通过多种清洗技术处理，并采用了一种新颖的双层(短和长)CoT增强策略。其次，我们介绍了HoneyPipe数据管理流程及其底层框架DataStudio，为社区提供了一种透明且适应性强的数据管理方法，超越了静态数据集的发布。最后，为了验证我们的数据集和流程，我们在Honey-Data-15M上训练了一个8B模型Bee-8B。实验表明，Bee-8B为全开源MLLM建立了一个新的最先进水平(SOTA)，其性能与最近的半开源模型(如InternVL3.5-8B)相比具有竞争力，在某些情况下甚至超过了它们。我们的工作为社区提供了一套基础资源，包括：Honey-Data-15M语料库；包含HoneyPipe和DataStudio的全栈套件；训练配方；评估工具；以及模型权重。这项工作表明，有原则地关注数据质量是开发与半开源模型具有高度竞争力的全开源MLLM的关键途径。

## 🔬 方法详解

**问题定义**：现有开源多模态大语言模型(MLLM)的性能落后于闭源模型，主要瓶颈在于高质量的监督微调(SFT)数据匮乏。现有开源数据集存在大量噪声，且缺乏复杂的推理数据，例如思维链(Chain-of-Thought, CoT)数据，这严重阻碍了模型学习复杂推理能力。

**核心思路**：论文的核心思路是通过构建一个高质量、大规模的SFT数据集来提升全开源MLLM的性能。具体而言，通过多轮数据清洗、过滤噪声数据，并采用双层CoT增强策略，生成高质量的推理数据，从而提升模型的推理能力。

**技术框架**：论文提出了一个完整的数据管理流程HoneyPipe，其底层框架是DataStudio。该流程包括数据收集、数据清洗、数据增强（特别是双层CoT增强）和数据验证等多个阶段。最终，使用Honey-Data-15M数据集训练Bee-8B模型。

**关键创新**：论文的关键创新在于：1) Honey-Data-15M数据集，该数据集经过严格清洗和双层CoT增强，具有高质量和大规模的特点。2) HoneyPipe数据管理流程和DataStudio框架，提供了一种透明且可定制的数据管理方法。3) 双层CoT增强策略，同时生成短CoT和长CoT数据，提升模型的推理能力。

**关键设计**：双层CoT增强策略是关键设计之一。短CoT侧重于直接推理步骤，而长CoT则包含更详细的解释和背景知识。这种双层结构旨在帮助模型更好地理解和学习复杂的推理过程。此外，数据清洗过程采用了多种过滤规则和启发式方法，以去除噪声数据并保留高质量的样本。具体的模型训练参数和损失函数等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，在Honey-Data-15M数据集上训练的Bee-8B模型在全开源MLLM中取得了新的SOTA，其性能与半开源模型InternVL3.5-8B相比具有竞争力，在某些情况下甚至超过了后者。这验证了高质量数据对于提升全开源MLLM性能的重要性。

## 🎯 应用场景

该研究成果可广泛应用于智能问答、图像理解、视觉推理等领域。高质量的开源数据集和模型有助于推动全开源多模态大语言模型的发展，降低研究门槛，促进相关技术的普及和应用。未来，可以进一步探索更有效的CoT生成方法和更高效的模型训练策略。

## 📄 摘要（原文）

> Fully open multimodal large language models (MLLMs) currently lag behind proprietary counterparts, primarily due to a significant gap in data quality for supervised fine-tuning (SFT). Existing open-source datasets are often plagued by widespread noise and a critical deficit in complex reasoning data, such as Chain-of-Thought (CoT), which hinders the development of advanced model capabilities. Addressing these challenges, our work makes three primary contributions. First, we introduce Honey-Data-15M, a new SFT dataset comprising approximately 15 million QA pairs, processed through multiple cleaning techniques and enhanced with a novel dual-level (short and long) CoT enrichment strategy. Second, we introduce HoneyPipe, the data curation pipeline, and its underlying framework DataStudio, providing the community with a transparent and adaptable methodology for data curation that moves beyond static dataset releases. Finally, to validate our dataset and pipeline, we train Bee-8B, an 8B model on Honey-Data-15M. Experiments show that Bee-8B establishes a new state-of-the-art (SOTA) for fully open MLLMs, achieving performance that is competitive with, and in some cases surpasses, recent semi-open models such as InternVL3.5-8B. Our work delivers to the community a suite of foundational resources, including: the Honey-Data-15M corpus; the full-stack suite comprising HoneyPipe and DataStudio; training recipes; an evaluation harness; and the model weights. This effort demonstrates that a principled focus on data quality is a key pathway to developing fully open MLLMs that are highly competitive with their semi-open counterparts.


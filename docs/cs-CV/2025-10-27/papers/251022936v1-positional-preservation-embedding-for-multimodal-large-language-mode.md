---
layout: default
title: Positional Preservation Embedding for Multimodal Large Language Models
---

# Positional Preservation Embedding for Multimodal Large Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22936" target="_blank" class="toolbar-btn">arXiv: 2510.22936v1</a>
    <a href="https://arxiv.org/pdf/2510.22936.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22936v1" 
            onclick="toggleFavorite(this, '2510.22936v1', 'Positional Preservation Embedding for Multimodal Large Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Mouxiao Huang, Borui Jiang, Dehua Zheng, Hailin Hu, Kai Han, Xinghao Chen

**分类**: cs.CV

**发布日期**: 2025-10-27

---

## 💡 一句话要点

**提出位置保持嵌入（PPE）以提升多模态大语言模型在视觉-语言任务中的效率和性能。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉-语言任务` `Token合并` `位置编码` `时空结构保持`

## 📋 核心要点

1. 现有MLLM的token合并方法忽略了位置信息，导致空间布局和时间连续性受损，影响模型性能。
2. 提出位置保持嵌入（PPE），通过在token维度中解耦编码3D位置信息，从而在压缩过程中保持时空结构。
3. 实验表明，PPE在多个视觉-语言任务上实现了2%~5%的性能提升，验证了保持位置信息的重要性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在视觉-语言任务中表现出色，但由于视觉tokens的冗余而效率低下。现有的token合并方法虽然减少了序列长度，但常常忽略位置关系，从而破坏了空间布局和时间连续性。本文提出了一种新的编码算子，称为位置保持嵌入（PPE），其主要特点是在视觉token压缩过程中保持时空结构。PPE显式地引入了3D位置的解耦编码到token维度中，使得每个压缩后的token能够封装来自多个原始token的不同位置信息。此外，我们证明了PPE可以有效地支持级联聚类——一种渐进式的token压缩策略，从而带来更好的性能保持。PPE是一种无参数且通用的算子，可以无缝集成到现有的token合并方法中，无需任何调整。应用于最先进的token合并框架后，PPE在多个视觉-语言基准测试中实现了2%~5%的一致性改进，包括MMBench（通用视觉理解）、TextVQA（布局理解）和VideoMME（时间理解）。这些结果表明，保持位置线索对于高效和有效的MLLM推理至关重要。

## 🔬 方法详解

**问题定义**：多模态大语言模型在处理视觉信息时，通常需要将图像或视频分割成多个视觉tokens。然而，过多的tokens会导致计算冗余，降低模型的效率。现有的token合并方法旨在减少tokens数量，但往往忽略了tokens之间的位置关系，破坏了图像的空间布局和视频的时间连续性，从而影响了模型的理解能力。

**核心思路**：论文的核心思路是在token合并的过程中显式地保留和利用位置信息。通过将每个token的位置信息编码到其嵌入向量中，使得模型在压缩tokens的同时，仍然能够感知原始tokens的空间和时间关系。这样可以避免因位置信息丢失而导致的性能下降。

**技术框架**：PPE可以无缝集成到现有的token合并框架中。其主要流程是：首先，对原始的视觉tokens进行位置编码，将每个token的位置信息（例如，在图像中的坐标或在视频中的帧号）嵌入到其特征向量中。然后，使用现有的token合并方法（例如，聚类或池化）对tokens进行压缩。在压缩过程中，PPE确保每个压缩后的token都包含其原始tokens的位置信息。最后，将压缩后的tokens输入到MLLM中进行后续处理。

**关键创新**：PPE的关键创新在于其显式地对3D位置信息进行解耦编码，并将其融入到token的嵌入表示中。与现有方法不同，PPE不是简单地忽略位置信息，而是将其作为一种重要的特征进行保留和利用。这种方法使得模型在压缩tokens的同时，仍然能够感知原始tokens的空间和时间关系。

**关键设计**：PPE是一种无参数的算子，这意味着它不需要额外的训练或调整。位置编码可以使用多种方法实现，例如，正弦余弦编码或可学习的位置嵌入。论文中提到PPE支持级联聚类，这是一种渐进式的token压缩策略，通过多次迭代的token合并来逐步减少tokens数量。具体的技术细节（如损失函数、网络结构）取决于所使用的token合并方法和MLLM架构，PPE作为一个通用模块，可以灵活地与它们结合使用。

## 📊 实验亮点

实验结果表明，PPE在MMBench、TextVQA和VideoMME等多个视觉-语言基准测试中实现了2%~5%的一致性改进。这些结果表明，保持位置线索对于高效和有效的MLLM推理至关重要。PPE的无参数特性使其易于集成到现有的token合并框架中，具有很强的实用价值。

## 🎯 应用场景

该研究成果可广泛应用于需要高效处理视觉信息的场景，例如智能监控、自动驾驶、视频分析、图像检索等。通过减少视觉tokens的数量，可以降低计算成本，提高模型推理速度，从而使得MLLMs能够更好地应用于资源受限的设备或实时性要求高的应用中。未来，该方法有望进一步提升多模态大语言模型在各种视觉-语言任务中的性能和效率。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have achieved strong performance on vision-language tasks, yet often suffer from inefficiencies due to redundant visual tokens. Existing token merging methods reduce sequence length but frequently disrupt spatial layouts and temporal continuity by disregarding positional relationships. In this work, we propose a novel encoding operator dubbed as \textbf{P}ositional \textbf{P}reservation \textbf{E}mbedding (\textbf{PPE}), which has the main hallmark of preservation of spatiotemporal structure during visual token compression. PPE explicitly introduces the disentangled encoding of 3D positions in the token dimension, enabling each compressed token to encapsulate different positions from multiple original tokens. Furthermore, we show that PPE can effectively support cascade clustering -- a progressive token compression strategy that leads to better performance retention. PPE is a parameter-free and generic operator that can be seamlessly integrated into existing token merging methods without any adjustments. Applied to state-of-the-art token merging framework, PPE achieves consistent improvements of $2\%\sim5\%$ across multiple vision-language benchmarks, including MMBench (general vision understanding), TextVQA (layout understanding) and VideoMME (temporal understanding). These results demonstrate that preserving positional cues is critical for efficient and effective MLLM reasoning.


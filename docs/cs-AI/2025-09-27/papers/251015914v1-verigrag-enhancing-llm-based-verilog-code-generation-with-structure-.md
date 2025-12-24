---
layout: default
title: "VeriGRAG: Enhancing LLM-Based Verilog Code Generation with Structure-Aware Soft Prompts"
---

# VeriGRAG: Enhancing LLM-Based Verilog Code Generation with Structure-Aware Soft Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15914" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15914v1</a>
  <a href="https://arxiv.org/pdf/2510.15914.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15914v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15914v1', 'VeriGRAG: Enhancing LLM-Based Verilog Code Generation with Structure-Aware Soft Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayu Zhao, Song Chen

**分类**: cs.AR, cs.AI, cs.PL

**发布日期**: 2025-09-27

**备注**: 9 pages, 5 figures

---

## 💡 一句话要点

**VeriGRAG：利用结构感知软提示增强LLM的Verilog代码生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Verilog代码生成` `大型语言模型` `图神经网络` `结构感知` `软提示`

## 📋 核心要点

1. 现有方法难以有效利用Verilog代码中蕴含的硬件电路结构信息，导致LLM生成的代码在功能和语法上存在不足。
2. VeriGRAG的核心思想是利用图神经网络提取Verilog代码的结构图嵌入，并将其融入到LLM的提示中，从而引导代码生成。
3. 实验结果表明，VeriGRAG在VerilogEval和RTLLM基准测试中均取得了显著的性能提升，达到了最先进水平。

## 📝 摘要（中文）

大型语言模型（LLM）在从自然语言描述生成Verilog代码方面表现出强大的能力。然而，Verilog代码本身编码了硬件电路的结构信息。如何有效地利用这种结构信息来提高LLM生成的Verilog代码的功能和语法正确性仍然是一个重大挑战。为了解决这个问题，我们提出了VeriGRAG，这是一个新颖的框架，它使用图神经网络（GNN）从Verilog代码中提取结构图嵌入。然后，多模态检索器选择与给定生成任务最相关的图嵌入，并通过VeriFormer模块将其与代码模态对齐，以生成结构感知的软提示。我们的实验表明，VeriGRAG显著提高了Verilog代码生成的正确性，在VerilogEval和RTLLM基准测试中均实现了最先进或更优越的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在生成Verilog代码时，由于缺乏对硬件电路结构信息的有效利用，导致生成的代码在功能和语法上存在缺陷的问题。现有方法通常直接使用自然语言描述作为LLM的输入，忽略了Verilog代码本身所蕴含的结构信息，这限制了LLM生成高质量代码的能力。

**核心思路**：论文的核心思路是利用图神经网络（GNN）从Verilog代码中提取结构图嵌入，并将这些嵌入作为软提示（soft prompts）融入到LLM的输入中。通过这种方式，LLM可以感知到硬件电路的结构信息，从而生成更准确、更符合规范的Verilog代码。这种设计思路的关键在于将结构信息以一种可学习的方式融入到LLM中，而不是简单地将结构信息作为额外的输入。

**技术框架**：VeriGRAG框架主要包含以下几个模块：1) 图神经网络（GNN）：用于从Verilog代码中提取结构图嵌入。2) 多模态检索器：用于选择与给定生成任务最相关的图嵌入。3) VeriFormer模块：用于将图嵌入与代码模态对齐，生成结构感知的软提示。4) LLM：使用结构感知的软提示生成Verilog代码。整个流程是：首先，GNN提取Verilog代码的结构图嵌入；然后，多模态检索器根据任务选择相关的嵌入；接着，VeriFormer将嵌入与代码模态对齐，生成软提示；最后，LLM利用软提示生成代码。

**关键创新**：VeriGRAG最重要的技术创新点在于提出了利用结构图嵌入作为软提示来引导LLM生成Verilog代码的方法。与现有方法相比，VeriGRAG能够更有效地利用Verilog代码中蕴含的结构信息，从而提高代码生成的质量。此外，VeriFormer模块的设计也使得结构信息能够更好地融入到LLM中。

**关键设计**：论文中GNN的具体选择、多模态检索器的相似度度量方式、VeriFormer模块的网络结构以及LLM的选择都是关键的设计细节。此外，损失函数的设计也至关重要，需要确保LLM能够有效地利用结构感知的软提示来生成代码。具体的参数设置和网络结构在论文中应该有详细的描述（未知）。

## 📊 实验亮点

VeriGRAG在VerilogEval和RTLLM基准测试中均取得了显著的性能提升。具体而言，VeriGRAG在两个基准测试中均达到了最先进或更优越的性能，表明其能够有效地提高Verilog代码生成的正确性。具体的性能数据和提升幅度需要在论文中查找（未知）。

## 🎯 应用场景

VeriGRAG的研究成果可以应用于自动化硬件设计流程，提高Verilog代码生成的效率和质量。该技术可以帮助硬件工程师快速生成符合规范的Verilog代码，从而缩短产品开发周期。此外，VeriGRAG还可以用于教育领域，帮助学生更好地理解硬件电路的结构和Verilog代码的编写。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated strong capabilities in generating Verilog code from natural language descriptions. However, Verilog code inherently encodes structural information of hardware circuits. Effectively leveraging this structural information to enhance the functional and syntactic correctness of LLM-generated Verilog code remains a significant challenge. To address this challenge, we propose VeriGRAG , a novel framework that extracts structural graph embeddings from Verilog code using graph neural networks (GNNs). A multimodal retriever then selects the graph embeddings most relevant to the given generation task, which are aligned with the code modality through the VeriFormer module to generate structure-aware soft prompts. Our experiments demonstrate that VeriGRAG substantially improves the correctness of Verilog code generation, achieving state-of-the-art or superior performance across both VerilogEval and RTLLM benchmarks.


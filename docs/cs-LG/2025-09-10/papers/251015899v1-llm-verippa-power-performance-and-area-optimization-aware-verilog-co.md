---
layout: default
title: "LLM-VeriPPA: Power, Performance, and Area Optimization aware Verilog Code Generation with Large Language Models"
---

# LLM-VeriPPA: Power, Performance, and Area Optimization aware Verilog Code Generation with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15899" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15899v1</a>
  <a href="https://arxiv.org/pdf/2510.15899.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15899v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15899v1', 'LLM-VeriPPA: Power, Performance, and Area Optimization aware Verilog Code Generation with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kiran Thorat, Jiahui Zhao, Yaotian Liu, Amit Hasan, Hongwu Peng, Xi Xie, Bin Lei, Caiwen Ding

**分类**: cs.AR, cs.LG

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**VeriPPA：利用大语言模型实现功耗、性能和面积优化的Verilog代码生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `Verilog代码生成` `功耗优化` `性能优化` `面积优化` `芯片设计` `自动化设计` `PPA优化`

## 📋 核心要点

1. 现有芯片设计方法在功耗、性能和面积（PPA）优化方面面临挑战，且Verilog代码生成过程效率较低。
2. VeriPPA框架利用LLM，通过两阶段优化流程，提升Verilog代码的语法和功能正确性，并满足PPA约束。
3. 实验结果表明，VeriPPA在语法和功能正确性方面均优于SOTA方法，并能有效优化芯片设计的PPA。

## 📝 摘要（中文）

本文介绍了一种名为VeriPPA的新框架，该框架利用大型语言模型（LLM）优化功耗、性能和面积（PPA），并生成精确的Verilog代码用于电路设计。VeriPPA采用两阶段流程：第一阶段侧重于提高生成的Verilog代码的功能和语法正确性；第二阶段专注于优化Verilog代码，以满足电路设计的PPA约束。在RTLLM数据集上，VeriPPA在代码生成方面实现了81.37%的语法正确率和62.06%的功能正确率，优于当前最先进的方法。在VerilogEval数据集上，VeriPPA实现了99.56%的语法正确率和43.79%的功能正确率，也超过了SOTA（语法正确率92.11%，功能正确率33.57%）。此外，该框架还能够优化设计的PPA。这些结果突显了LLM在处理复杂技术领域的潜力，并表明芯片设计自动化方面取得了令人鼓舞的进展。

## 🔬 方法详解

**问题定义**：论文旨在解决利用大语言模型自动生成高质量、满足功耗、性能和面积（PPA）约束的Verilog代码的问题。现有方法在生成Verilog代码时，往往存在语法错误、功能不正确以及PPA优化不足等问题，导致设计周期长、成本高。

**核心思路**：论文的核心思路是利用大语言模型强大的代码生成能力，结合两阶段优化策略，首先保证Verilog代码的语法和功能正确性，然后针对PPA约束进行优化。通过这种方式，可以显著提高Verilog代码生成的质量和效率，并满足芯片设计的性能要求。

**技术框架**：VeriPPA框架包含两个主要阶段：第一阶段是代码生成和语法/功能正确性优化阶段，利用LLM生成初始Verilog代码，并通过验证和修正机制提高代码的正确性。第二阶段是PPA优化阶段，针对生成的Verilog代码，利用LLM进行优化，以满足功耗、性能和面积的约束。整个流程通过迭代优化，最终生成高质量的Verilog代码。

**关键创新**：VeriPPA的关键创新在于其两阶段优化策略，将代码正确性优化和PPA优化解耦，使得LLM能够更有效地处理这两个任务。此外，该框架还引入了验证和修正机制，进一步提高了代码的正确性。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数或网络结构等技术细节。但是，两阶段的优化策略是关键设计，第一阶段保证代码的正确性，第二阶段优化PPA，两个阶段相互配合，最终生成高质量的Verilog代码。

## 📊 实验亮点

VeriPPA在RTLLM数据集上实现了81.37%的语法正确率和62.06%的功能正确率，在VerilogEval数据集上实现了99.56%的语法正确率和43.79%的功能正确率，均优于SOTA方法。尤其在VerilogEval数据集上，语法正确率从92.11%提升到99.56%，功能正确率从33.57%提升到43.79%。

## 🎯 应用场景

VeriPPA框架可应用于芯片设计的自动化流程中，加速Verilog代码的生成和优化，降低设计成本，缩短设计周期。该研究成果对于推动芯片设计领域的智能化发展具有重要意义，并有望在未来的集成电路设计中得到广泛应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) are gaining prominence in various fields, thanks to their ability to generate high- quality content from human instructions. This paper delves into the field of chip design using LLMs, specifically in Power- Performance-Area (PPA) optimization and the generation of accurate Verilog codes for circuit designs. We introduce a novel framework VeriPPA designed to optimize PPA and generate Verilog code using LLMs. Our method includes a two-stage process where the first stage focuses on improving the functional and syntactic correctness of the generated Verilog codes, while the second stage focuses on optimizing the Verilog codes to meet PPA constraints of circuit designs, a crucial element of chip design. Our framework achieves an 81.37% success rate in syntactic correctness and 62.06% in functional correctness for code genera- tion, outperforming current state-of-the-art (SOTA) methods. On the RTLLM dataset. On the VerilogEval dataset, our framework achieves 99.56% syntactic correctness and 43.79% functional correctness, also surpassing SOTA, which stands at 92.11% for syntactic correctness and 33.57% for functional correctness. Furthermore, Our framework able to optimize the PPA of the designs. These results highlight the potential of LLMs in handling complex technical areas and indicate an encouraging development in the automation of chip design processes.


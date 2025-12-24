---
layout: default
title: "Guaranteed Guess: A Language Modeling Approach for CISC-to-RISC Transpilation with Testing Guarantees"
---

# Guaranteed Guess: A Language Modeling Approach for CISC-to-RISC Transpilation with Testing Guarantees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14606" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14606v1</a>
  <a href="https://arxiv.org/pdf/2506.14606.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14606v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14606v1', 'Guaranteed Guess: A Language Modeling Approach for CISC-to-RISC Transpilation with Testing Guarantees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Heakl, Sarim Hashmi, Chaimaa Abi, Celine Lee, Abdulrahman Mahmoud

**分类**: cs.CL, cs.AR, cs.LG, cs.PL, cs.SE

**发布日期**: 2025-06-17

**备注**: Project page: https://ahmedheakl.github.io/Guaranteed-Guess/

---

## 💡 一句话要点

**提出GG方法以解决CISC到RISC的代码转译问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码转译` `指令集架构` `大型语言模型` `软件测试` `CISC` `RISC` `性能优化`

## 📋 核心要点

1. CISC与RISC架构之间的转译面临指令复杂性和执行范式的根本差异，现有方法难以保证翻译的正确性和效率。
2. 本文提出GG方法，通过结合大型语言模型和软件测试框架，生成高质量的代码翻译，并确保其正确性。
3. 在实验中，GG方法在HumanEval程序上实现了99%的正确率，并在BringupBench程序上达到49%的正确率，显示出显著的性能提升。

## 📝 摘要（中文）

随着硬件生态系统的快速发展，低级程序在不同指令集架构（ISA）之间的翻译变得愈发重要。CISC与RISC架构之间的转译尤为复杂，因其指令复杂性、内存模型和执行范式的根本差异。本文提出了GG（Guaranteed Guess），一种结合预训练大型语言模型（LLM）与软件测试框架的ISA中心转译管道。通过在软件测试框架中嵌入LLM生成的候选翻译，GG方法在两个多样化的数据集上实现了高代码覆盖率（>98%）和99%的功能/语义正确率，展示了其在实际CISC到RISC转译任务中的有效性。我们将开源代码、数据、模型和基准，以推动ISA级代码翻译研究的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决CISC到RISC架构的代码转译问题，现有方法在翻译的灵活性和正确性方面存在不足，尤其是在复杂指令集之间的转换。

**核心思路**：GG方法的核心在于利用预训练的大型语言模型生成候选翻译，并通过软件测试框架来验证和增强翻译的正确性，从而提高代码的可移植性和可靠性。

**技术框架**：GG方法的整体架构包括两个主要模块：首先，使用LLM生成从CISC到RISC的候选代码；其次，将这些候选代码嵌入到软件测试框架中进行验证，以确保高代码覆盖率和功能正确性。

**关键创新**：GG方法的创新在于将语言模型的生成能力与软件测试的严格性结合起来，形成了一种新的转译管道，显著提高了转译的效率和准确性。与现有的Rosetta 2框架相比，GG在性能和资源利用上表现更佳。

**关键设计**：在设计中，GG方法强调高代码覆盖率的测试策略，确保测试用例的多样性和全面性，此外，采用了适当的损失函数来优化翻译质量，确保生成代码的功能与语义的正确性。

## 📊 实验亮点

GG方法在实验中展现出优异的性能，HumanEval程序的功能正确率达到99%，BringupBench程序为49%。与Rosetta 2框架相比，GG在运行时性能上提升了1.73倍，能效提高了1.47倍，内存使用效率提升了2.41倍，显示出其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括编译器设计、软件迁移和跨平台开发等。通过提高CISC与RISC架构之间的代码转译效率，GG方法可以延长现有代码的使用寿命，促进软件的可移植性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The hardware ecosystem is rapidly evolving, with increasing interest in translating low-level programs across different instruction set architectures (ISAs) in a quick, flexible, and correct way to enhance the portability and longevity of existing code. A particularly challenging class of this transpilation problem is translating between complex- (CISC) and reduced- (RISC) hardware architectures, due to fundamental differences in instruction complexity, memory models, and execution paradigms. In this work, we introduce GG (Guaranteed Guess), an ISA-centric transpilation pipeline that combines the translation power of pre-trained large language models (LLMs) with the rigor of established software testing constructs. Our method generates candidate translations using an LLM from one ISA to another, and embeds such translations within a software-testing framework to build quantifiable confidence in the translation. We evaluate our GG approach over two diverse datasets, enforce high code coverage (>98%) across unit tests, and achieve functional/semantic correctness of 99% on HumanEval programs and 49% on BringupBench programs, respectively. Further, we compare our approach to the state-of-the-art Rosetta 2 framework on Apple Silicon, showcasing 1.73x faster runtime performance, 1.47x better energy efficiency, and 2.41x better memory usage for our transpiled code, demonstrating the effectiveness of GG for real-world CISC-to-RISC translation tasks. We will open-source our codes, data, models, and benchmarks to establish a common foundation for ISA-level code translation research.


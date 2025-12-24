---
layout: default
title: "BuildBench: Benchmarking LLM Agents on Compiling Real-World Open-Source Software"
---

# BuildBench: Benchmarking LLM Agents on Compiling Real-World Open-Source Software

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25248" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25248v1</a>
  <a href="https://arxiv.org/pdf/2509.25248.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25248v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25248v1', 'BuildBench: Benchmarking LLM Agents on Compiling Real-World Open-Source Software')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zehua Zhang, Ati Priya Bajaj, Divij Handa, Siyu Liu, Arvind S Raj, Hongkai Chen, Hulin Wang, Yibo Liu, Zion Leonahenahe Basque, Souradip Nath, Vishal Juneja, Nikhil Chapre, Yan Shoshitaishvili, Adam Doupé, Chitta Baral, Ruoyu Wang

**分类**: cs.SE, cs.AI, cs.PL

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**BuildBench：基准测试LLM Agent在编译真实世界开源软件上的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `开源软件编译` `基准测试` `软件自动化` `软件工程` `构建指令检索` `自动化构建` `代码编译`

## 📋 核心要点

1. 现有开源软件编译方法依赖手动规则，难以适应需要定制配置的复杂项目，且缺乏对多样化开源软件的有效评估。
2. 论文提出OSS-BUILD-AGENT，通过增强的构建指令检索模块，提升LLM Agent在异构开源软件编译任务中的性能。
3. BUILD-BENCH基准测试和OSS-BUILD-AGENT的结合，为评估和提升LLM在复杂软件工程任务中的能力提供了有效工具。

## 📝 摘要（中文）

自动编译开源软件(OSS)项目是一项至关重要、劳动密集且复杂的任务，这使得它成为LLM Agent的一个很好的挑战。现有方法依赖于手动管理的规则和工作流程，无法适应需要定制配置或环境设置的OSS。最近使用大型语言模型(LLM)的尝试，仅在部分高评价的OSS上进行选择性评估，低估了OSS编译的实际挑战。在实践中，编译指令通常缺失，依赖关系未记录，甚至成功的构建可能需要修补源文件或修改构建脚本。我们提出了一个更具挑战性和现实意义的基准测试BUILD-BENCH，它包含质量、规模和特性更加多样的OSS。此外，我们提出了一个强大的基于LLM的Agent基线，OSS-BUILD-AGENT，这是一个有效的系统，具有增强的构建指令检索模块，在BUILD-BENCH上实现了最先进的性能，并且能够适应异构的OSS特性。我们还提供了关于不同编译方法设计选择及其对整个任务的影响的详细分析，为指导未来的发展提供了见解。我们相信在BUILD-BENCH上的性能能够真实地反映Agent解决编译这一复杂软件工程任务的能力，因此，我们的基准测试将激发创新，对软件开发和软件安全领域的下游应用产生重大影响。

## 🔬 方法详解

**问题定义**：现有方法在自动编译开源软件时，面临着依赖手动规则、无法适应定制配置和环境设置，以及在多样化开源软件上评估不足的问题。实际编译过程中，指令缺失、依赖未记录、甚至需要修改源码等情况，都给自动化带来了挑战。

**核心思路**：论文的核心思路是构建一个更具挑战性和现实意义的基准测试BUILD-BENCH，并设计一个强大的基于LLM的Agent基线OSS-BUILD-AGENT，通过增强的构建指令检索模块，提升LLM Agent在异构开源软件编译任务中的性能。这样设计的目的是为了更真实地反映Agent在复杂软件工程任务中的能力。

**技术框架**：OSS-BUILD-AGENT包含以下主要模块：构建指令检索模块，用于从各种来源（如文档、代码注释等）检索相关的构建指令；编译执行模块，用于根据检索到的指令执行编译过程；错误处理模块，用于处理编译过程中出现的错误，并尝试修复；以及评估模块，用于评估编译结果的正确性和效率。整个流程旨在模拟真实世界中软件编译的复杂过程。

**关键创新**：最重要的技术创新点在于增强的构建指令检索模块，该模块能够更有效地从各种来源检索相关的构建指令，并能够根据不同的开源软件特性进行自适应调整。这与现有方法依赖手动规则或简单检索相比，具有更高的灵活性和适应性。

**关键设计**：论文中没有明确提及关键的参数设置、损失函数、网络结构等技术细节。构建指令检索模块的具体实现方式（例如，使用的检索算法、特征提取方法等）以及错误处理模块的修复策略（例如，基于LLM的代码修复、依赖关系推断等）是值得关注的技术细节，但论文中未详细描述。

## 📊 实验亮点

论文提出了BUILD-BENCH基准测试，包含质量、规模和特性更加多样的OSS，更真实地反映了实际编译的挑战。同时，提出的OSS-BUILD-AGENT在BUILD-BENCH上实现了最先进的性能，证明了其在异构开源软件编译任务中的有效性。具体的性能数据和对比基线在论文中未明确给出。

## 🎯 应用场景

该研究成果可应用于自动化软件构建、持续集成/持续交付(CI/CD)流程、软件漏洞挖掘与修复、以及软件安全分析等领域。通过提升LLM Agent在编译任务中的能力，可以显著降低人工成本，提高软件开发效率，并促进软件安全性的提升。未来，该技术有望应用于更广泛的软件工程任务中。

## 📄 摘要（原文）

> Automatically compiling open-source software (OSS) projects is a vital, labor-intensive, and complex task, which makes it a good challenge for LLM Agents. Existing methods rely on manually curated rules and workflows, which cannot adapt to OSS that requires customized configuration or environment setup. Recent attempts using Large Language Models (LLMs) used selective evaluation on a subset of highly rated OSS, a practice that underestimates the realistic challenges of OSS compilation. In practice, compilation instructions are often absent, dependencies are undocumented, and successful builds may even require patching source files or modifying build scripts. We propose a more challenging and realistic benchmark, BUILD-BENCH, comprising OSS that are more diverse in quality, scale, and characteristics. Furthermore, we propose a strong baseline LLM-based agent, OSS-BUILD-AGENT, an effective system with enhanced build instruction retrieval module that achieves state-of-the-art performance on BUILD-BENCH and is adaptable to heterogeneous OSS characteristics. We also provide detailed analysis regarding different compilation method design choices and their influence to the whole task, offering insights to guide future advances. We believe performance on BUILD-BENCH can faithfully reflect an agent's ability to tackle compilation as a complex software engineering tasks, and, as such, our benchmark will spur innovation with a significant impact on downstream applications in the fields of software development and software security.


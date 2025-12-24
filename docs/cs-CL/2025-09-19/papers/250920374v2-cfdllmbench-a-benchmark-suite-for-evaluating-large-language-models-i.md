---
layout: default
title: "CFDLLMBench: A Benchmark Suite for Evaluating Large Language Models in Computational Fluid Dynamics"
---

# CFDLLMBench: A Benchmark Suite for Evaluating Large Language Models in Computational Fluid Dynamics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20374" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20374v2</a>
  <a href="https://arxiv.org/pdf/2509.20374.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20374v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20374v2', 'CFDLLMBench: A Benchmark Suite for Evaluating Large Language Models in Computational Fluid Dynamics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nithin Somasekharan, Ling Yue, Yadi Cao, Weichao Li, Patrick Emami, Pochinapeddi Sai Bhargav, Anurag Acharya, Xingyu Xie, Shaowu Pan

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-19 (更新: 2025-10-10)

**🔗 代码/项目**: [GITHUB](https://github.com/NREL-Theseus/cfdllmbench/)

---

## 💡 一句话要点

**CFDLLMBench：用于评估大语言模型在计算流体动力学中应用能力的基准套件**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算流体动力学` `大语言模型` `基准测试` `科学计算` `自动化` `数值模拟` `CFD` `人工智能`

## 📋 核心要点

1. 现有方法难以自动化复杂物理系统的数值实验，尤其是在计算流体动力学（CFD）领域，该领域需要专业的知识和技能。
2. CFDLLMBench通过构建包含CFDQuery、CFDCodeBench和FoamBench三个组件的基准套件，全面评估LLM在CFD领域的应用能力。
3. 该基准套件基于真实CFD实践，能够量化LLM在代码可执行性、解决方案准确性和数值收敛行为等方面的性能。

## 📝 摘要（中文）

大语言模型（LLM）在通用自然语言处理任务中表现出强大的性能，但它们在自动化复杂物理系统数值实验中的效用——这是一个关键且劳动密集型的环节——仍未被充分探索。计算流体动力学（CFD）作为过去几十年计算科学的主要工具，为评估LLM的科学能力提供了一个独特的挑战性试验台。我们推出了CFDLLMBench，这是一个包含三个互补组件的基准套件——CFDQuery、CFDCodeBench和FoamBench——旨在全面评估LLM在三个关键能力方面的表现：研究生水平的CFD知识、CFD的数值和物理推理，以及CFD工作流程的上下文相关实现。我们的基准基于真实的CFD实践，将详细的任务分类与严格的评估框架相结合，以提供可重现的结果，并量化LLM在代码可执行性、解决方案准确性和数值收敛行为方面的性能。CFDLLMBench为开发和评估LLM驱动的复杂物理系统数值实验自动化奠定了坚实的基础。代码和数据可在https://github.com/NREL-Theseus/cfdllmbench/获取。

## 🔬 方法详解

**问题定义**：论文旨在评估大语言模型（LLM）在计算流体动力学（CFD）领域的应用能力。现有方法在自动化CFD数值实验方面存在不足，因为CFD需要深厚的领域知识、数值推理能力和代码实现能力。人工进行CFD实验耗时耗力，且容易出错。

**核心思路**：论文的核心思路是构建一个全面的基准套件，该套件能够系统地评估LLM在CFD领域的关键能力。通过设计不同类型的任务，例如CFD知识问答、代码生成和工作流程实现，来考察LLM在不同方面的表现。这样可以更准确地了解LLM在CFD领域的优势和局限性。

**技术框架**：CFDLLMBench包含三个主要组件：CFDQuery、CFDCodeBench和FoamBench。CFDQuery用于评估LLM的CFD知识水平，通过问答形式进行。CFDCodeBench用于评估LLM的代码生成能力，要求LLM根据描述生成CFD代码片段。FoamBench用于评估LLM在实际CFD工作流程中的应用能力，例如设置仿真参数、运行仿真和分析结果。这三个组件相互补充，共同构成一个完整的评估体系。

**关键创新**：该论文的关键创新在于构建了一个专门针对CFD领域的LLM评估基准。与现有的通用LLM基准不同，CFDLLMBench更加关注LLM在科学计算领域的应用，并针对CFD的特点设计了相应的评估任务。这使得评估结果更加具有针对性和参考价值。

**关键设计**：在CFDQuery中，问题涵盖了CFD的基本概念、方程和数值方法。在CFDCodeBench中，代码生成任务涉及不同的CFD算法和模型。在FoamBench中，工作流程实现任务模拟了真实的CFD实验流程，例如使用OpenFOAM进行仿真。评估指标包括代码可执行性、解决方案准确性和数值收敛行为。

## 📊 实验亮点

CFDLLMBench基准套件的推出，为评估LLM在CFD领域的应用能力提供了一个标准化的平台。该基准套件包含多种类型的任务，能够全面评估LLM在CFD知识、代码生成和工作流程实现等方面的表现。通过该基准套件，可以量化LLM在代码可执行性、解决方案准确性和数值收敛行为等方面的性能。

## 🎯 应用场景

该研究成果可应用于自动化CFD实验流程，降低CFD研究的门槛，加速新设计和新技术的开发。通过利用LLM的强大能力，可以减少人工干预，提高CFD仿真的效率和准确性。此外，该基准套件可以促进LLM在科学计算领域的应用，推动人工智能与科学研究的深度融合。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated strong performance across general NLP tasks, but their utility in automating numerical experiments of complex physical system -- a critical and labor-intensive component -- remains underexplored. As the major workhorse of computational science over the past decades, Computational Fluid Dynamics (CFD) offers a uniquely challenging testbed for evaluating the scientific capabilities of LLMs. We introduce CFDLLMBench, a benchmark suite comprising three complementary components -- CFDQuery, CFDCodeBench, and FoamBench -- designed to holistically evaluate LLM performance across three key competencies: graduate-level CFD knowledge, numerical and physical reasoning of CFD, and context-dependent implementation of CFD workflows. Grounded in real-world CFD practices, our benchmark combines a detailed task taxonomy with a rigorous evaluation framework to deliver reproducible results and quantify LLM performance across code executability, solution accuracy, and numerical convergence behavior. CFDLLMBench establishes a solid foundation for the development and evaluation of LLM-driven automation of numerical experiments for complex physical systems. Code and data are available at https://github.com/NREL-Theseus/cfdllmbench/.


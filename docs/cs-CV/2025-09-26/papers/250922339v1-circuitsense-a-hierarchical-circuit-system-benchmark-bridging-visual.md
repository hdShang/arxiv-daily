---
layout: default
title: "CircuitSense: A Hierarchical Circuit System Benchmark Bridging Visual Comprehension and Symbolic Reasoning in Engineering Design Process"
---

# CircuitSense: A Hierarchical Circuit System Benchmark Bridging Visual Comprehension and Symbolic Reasoning in Engineering Design Process

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22339" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22339v1</a>
  <a href="https://arxiv.org/pdf/2509.22339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22339v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22339v1', 'CircuitSense: A Hierarchical Circuit System Benchmark Bridging Visual Comprehension and Symbolic Reasoning in Engineering Design Process')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arman Akbari, Jian Gao, Yifei Zou, Mei Yang, Jinru Duan, Dmitrii Torbunov, Yanzhi Wang, Yihui Ren, Xuan Zhang

**分类**: cs.CV

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**CircuitSense：提出电路系统基准，桥接工程设计中的视觉理解与符号推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电路理解` `视觉推理` `符号推理` `多模态学习` `工程设计`

## 📋 核心要点

1. 多模态大语言模型在自然图像任务表现出色，但在理解工程设计图，特别是提取数学模型方面存在不足。
2. CircuitSense基准测试通过构建分层电路系统，评估模型在感知、分析和设计等工程流程中的能力，重点考察符号方程推导。
3. 实验表明，现有MLLM在视觉感知任务上表现良好，但在符号推导和分析推理方面存在显著差距，限制了其在工程设计中的应用。

## 📝 摘要（中文）

工程设计通过从系统规范到组件实现的层级抽象进行运作，需要在每个层级上进行视觉理解和数学推理。虽然多模态大型语言模型(MLLM)在自然图像任务中表现出色，但它们从技术图表中提取数学模型的能力仍未被探索。我们提出了CircuitSense，这是一个全面的基准，通过8006+个问题评估跨越组件级原理图到系统级框图的电路理解。我们的基准独特地检验了完整的工程工作流程：感知、分析和设计，特别强调了从视觉输入中推导符号方程的关键但未被充分探索的能力。我们引入了一个分层合成生成管道，包括一个基于网格的原理图生成器和一个带有自动推导符号方程标签的框图生成器。对六个最先进的MLLM（包括闭源和开源模型）的全面评估揭示了视觉到数学推理的根本局限性。闭源模型在涉及组件识别和拓扑识别的感知任务中实现了超过85%的准确率，但它们在符号推导和分析推理方面的性能低于19%，暴露了视觉解析和符号推理之间的关键差距。具有更强符号推理能力的模型始终在设计任务中获得更高的准确率，证实了数学理解在电路综合中的根本作用，并将符号推理确立为工程能力的关键指标。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLM）在理解和推理电路图方面的不足。现有方法在自然图像处理方面表现良好，但在工程设计领域，特别是从电路图等技术图表中提取数学模型并进行符号推理方面存在明显差距。这种差距限制了MLLM在工程设计自动化中的应用潜力。

**核心思路**：论文的核心思路是构建一个全面的、分层的电路系统基准测试集（CircuitSense），用于评估MLLM在电路理解方面的能力。该基准测试集涵盖了从组件级原理图到系统级框图的多个抽象层次，并侧重于评估模型从视觉输入中推导符号方程的能力。通过对不同模型的性能进行比较，揭示模型在视觉感知和符号推理之间的差距，并推动相关技术的发展。

**技术框架**：CircuitSense基准测试集包含8006+个问题，涵盖感知、分析和设计三个任务。它采用分层合成生成管道，包括一个基于网格的原理图生成器和一个带有自动推导符号方程标签的框图生成器。该管道能够自动生成带有精确标签的电路图，从而避免了手动标注的成本和误差。评估流程包括使用不同的MLLM模型解决基准测试集中的问题，并根据模型的准确率评估其性能。

**关键创新**：该论文的关键创新在于提出了一个专门针对电路理解的基准测试集，并强调了符号推理在工程设计中的重要性。与现有的多模态基准测试集相比，CircuitSense更侧重于评估模型在技术图表理解和数学推理方面的能力。此外，论文还提出了一个分层合成生成管道，能够自动生成带有精确标签的电路图，从而降低了基准测试集的构建成本。

**关键设计**：基准测试集的设计考虑了电路系统的分层结构，从组件级原理图到系统级框图，涵盖了不同的抽象层次。生成管道的设计保证了生成的电路图的合理性和标签的准确性。评估指标包括感知任务的准确率、符号推导任务的准确率和设计任务的准确率。论文还对不同的MLLM模型进行了全面的评估，并分析了它们在不同任务上的性能差异。

## 📊 实验亮点

实验结果表明，闭源模型在组件识别和拓扑识别等感知任务中达到了超过85%的准确率，但在符号推导和分析推理方面的性能低于19%。具有更强符号推理能力的模型在设计任务中表现更好，验证了数学理解在电路综合中的重要性。该研究揭示了现有MLLM在视觉到数学推理方面的局限性，并为未来的研究方向提供了指导。

## 🎯 应用场景

该研究成果可应用于电路设计自动化、故障诊断、教育培训等领域。通过提升模型对电路图的理解和推理能力，可以实现更高效的电路设计流程，降低设计成本，提高产品质量。未来，该研究有望推动人工智能在工程设计领域的更广泛应用。

## 📄 摘要（原文）

> Engineering design operates through hierarchical abstraction from system specifications to component implementations, requiring visual understanding coupled with mathematical reasoning at each level. While Multi-modal Large Language Models (MLLMs) excel at natural image tasks, their ability to extract mathematical models from technical diagrams remains unexplored. We present \textbf{CircuitSense}, a comprehensive benchmark evaluating circuit understanding across this hierarchy through 8,006+ problems spanning component-level schematics to system-level block diagrams. Our benchmark uniquely examines the complete engineering workflow: Perception, Analysis, and Design, with a particular emphasis on the critical but underexplored capability of deriving symbolic equations from visual inputs. We introduce a hierarchical synthetic generation pipeline consisting of a grid-based schematic generator and a block diagram generator with auto-derived symbolic equation labels. Comprehensive evaluation of six state-of-the-art MLLMs, including both closed-source and open-source models, reveals fundamental limitations in visual-to-mathematical reasoning. Closed-source models achieve over 85\% accuracy on perception tasks involving component recognition and topology identification, yet their performance on symbolic derivation and analytical reasoning falls below 19\%, exposing a critical gap between visual parsing and symbolic reasoning. Models with stronger symbolic reasoning capabilities consistently achieve higher design task accuracy, confirming the fundamental role of mathematical understanding in circuit synthesis and establishing symbolic reasoning as the key metric for engineering competence.


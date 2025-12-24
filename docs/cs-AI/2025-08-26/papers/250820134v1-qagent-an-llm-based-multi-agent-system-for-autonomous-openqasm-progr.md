---
layout: default
title: "QAgent: An LLM-based Multi-Agent System for Autonomous OpenQASM programming"
---

# QAgent: An LLM-based Multi-Agent System for Autonomous OpenQASM programming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20134" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20134v1</a>
  <a href="https://arxiv.org/pdf/2508.20134.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20134v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20134v1', 'QAgent: An LLM-based Multi-Agent System for Autonomous OpenQASM programming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenxiao Fu, Fan Chen, Lei Jiang

**分类**: cs.AI, cs.ET, quant-ph

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出QAgent以解决OpenQASM编程自动化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量子编程` `OpenQASM` `多代理系统` `大型语言模型` `自动化编程` `增强生成` `链式思维推理`

## 📋 核心要点

1. 现有的量子编程方法复杂，非专家难以掌握OpenQASM编程，限制了量子计算的普及。
2. QAgent通过多代理系统，结合任务规划和上下文学习，自动化OpenQASM编程，降低了编程门槛。
3. 实验结果表明，QAgent在多个LLM上提升了QASM代码生成的准确性，较静态方法提高了71.6%。

## 📝 摘要（中文）

噪声中等规模量子（NISQ）设备在解决经典难题上展现了早期量子优势，但对于非专家而言，Open量子汇编语言（OpenQASM）的编程复杂性使得实现这些优势变得困难。尽管基于大型语言模型（LLM）的代理在自动化经典编程工作流中显示出潜力，但其在量子编程中的应用仍然局限于特定任务。本文提出了QAgent，一个基于LLM的多代理系统，能够全面自动化OpenQASM编程。通过集成任务规划、上下文少样本学习、增强生成（RAG）和链式思维推理，QAgent显著提高了编译和功能正确性。评估结果显示，与之前的静态LLM方法相比，QAgent在QASM代码生成的准确性上提高了71.6%。

## 🔬 方法详解

**问题定义**：本文旨在解决非专家在编程OpenQASM时面临的复杂性和挑战。现有方法多限于特定任务，缺乏全面的自动化解决方案。

**核心思路**：QAgent通过多代理系统，利用大型语言模型的能力，自动化OpenQASM编程，集成多种技术以提升编程效率和准确性。

**技术框架**：QAgent的整体架构包括任务规划模块、上下文学习模块、增强生成模块和链式思维推理模块，各模块协同工作以实现高效编程。

**关键创新**：QAgent的主要创新在于其多代理协作机制和对长时上下文的增强生成能力，使其在量子编程领域具备更高的灵活性和准确性。

**关键设计**：在设计中，QAgent采用了预定义生成工具和链式思维推理，优化了模型的参数设置和损失函数，以确保生成的代码在功能和编译上均具备高正确性。

## 📊 实验亮点

实验结果显示，QAgent在多个不同规模的LLM上，QASM代码生成的准确性提高了71.6%。这一显著提升相较于以往的静态LLM方法，展示了QAgent在量子编程自动化中的有效性和优势。

## 🎯 应用场景

QAgent的研究成果可广泛应用于量子计算领域，尤其是在量子算法开发和量子软件工程中。通过降低编程门槛，QAgent有望促进量子计算的普及和实际应用，推动相关技术的进步与创新。

## 📄 摘要（原文）

> Noisy Intermediate-Scale Quantum (NISQ) devices have begun to exhibit early quantum advantages on classically intractable problems, spanning physics simulations to Gaussian boson sampling. Yet, realizing these benefits remains challenging for non-experts, primarily due to the complexities of programming in Open Quantum Assembly Language (OpenQASM). Although Large Language Model (LLM)-based agents have shown promise in automating classical programming workflows, their quantum counterparts have largely been restricted to specialized tasks such as quantum chemistry or error correction. In this paper, we present QAgent, an LLM-powered multi-agent system that fully automates OpenQASM programming. By integrating task planning, in-context few-shot learning, retrieval-augmented generation (RAG) for long-term context, predefined generation tools, and chain-of-thought (CoT) reasoning, the agents systematically improve both compilation and functional correctness. Our evaluations demonstrate substantial improvements: across multiple LLMs of varying sizes, QAgent enhances the accuracy of QASM code generation by 71.6\% compared to previous static LLM-based approaches. We envision this multi-agent system as a key enabler for democratizing quantum programming, bridging expertise gaps, and accelerating the practical adoption of quantum computing.


---
layout: default
title: "GENIE-ASI: Generative Instruction and Executable Code for Analog Subcircuit Identification"
---

# GENIE-ASI: Generative Instruction and Executable Code for Analog Subcircuit Identification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19393" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19393v1</a>
  <a href="https://arxiv.org/pdf/2508.19393.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19393v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19393v1', 'GENIE-ASI: Generative Instruction and Executable Code for Analog Subcircuit Identification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Phuoc Pham, Arun Venkitaraman, Chia-Yu Hsieh, Andrea Bonetti, Stefan Uhlich, Markus Leibl, Simon Hofmann, Eisaku Ohbuchi, Lorenzo Servadei, Ulf Schlichtmann, Robert Wille

**分类**: cs.AR, cs.LG

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出GENIE-ASI以解决模拟电路子电路识别问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模拟电路` `子电路识别` `大型语言模型` `上下文学习` `电子设计自动化`

## 📋 核心要点

1. 现有方法在模拟电路子电路识别中依赖大量人类专业知识和标注数据，效率低下且难以扩展。
2. GENIE-ASI通过上下文学习从示例中生成自然语言指令，并将其转化为可执行代码，实现无训练的子电路识别。
3. 实验结果显示，GENIE-ASI在简单和中等复杂度的电路中表现优异，F1-score分别达到1.0和0.81，展示了其在复杂电路中的潜力。

## 📝 摘要（中文）

模拟电路子电路识别是模拟设计中的核心任务，对于仿真、尺寸调整和布局至关重要。传统方法通常需要大量人类专业知识、基于规则的编码或大型标注数据集。为了解决这些挑战，本文提出了GENIE-ASI，这是首个基于大型语言模型（LLM）的无训练方法，用于模拟电路子电路识别。GENIE-ASI分为两个阶段：首先通过上下文学习从少量示例中推导自然语言指令，然后将其转换为可执行的Python代码，以识别未见的SPICE网表中的子电路。此外，本文还引入了一个新的基准，涵盖了多种子电路变体的运算放大器网表。实验结果表明，GENIE-ASI在简单结构上与基于规则的方法表现相当（F1-score = 1.0），在中等抽象上保持竞争力（F1-score = 0.81），在复杂子电路上也显示出潜力（F1-score = 0.31）。这些发现表明，LLM可以作为模拟设计自动化中的适应性通用工具，为基础模型在模拟设计自动化中的应用开辟新的研究方向。

## 🔬 方法详解

**问题定义**：本文旨在解决模拟电路子电路识别中的效率和准确性问题。现有方法通常需要大量的专业知识和标注数据，限制了其应用范围和灵活性。

**核心思路**：GENIE-ASI的核心思想是利用大型语言模型进行上下文学习，从少量示例中生成自然语言指令，并将其转化为可执行的Python代码，以实现对未见电路的识别。这样的设计使得方法无需大量训练数据，提升了适应性。

**技术框架**：GENIE-ASI的整体架构分为两个主要阶段：第一阶段是通过上下文学习生成自然语言指令，第二阶段是将这些指令转换为Python代码进行子电路识别。

**关键创新**：GENIE-ASI的最大创新在于其无训练的特性，利用LLM进行上下文学习，显著降低了对标注数据的依赖，与传统基于规则的方法形成鲜明对比。

**关键设计**：在设计中，GENIE-ASI采用了特定的上下文学习策略，以确保从示例中提取有效信息，并通过精心设计的代码生成模块来实现高效的子电路识别。

## 📊 实验亮点

实验结果表明，GENIE-ASI在简单结构的子电路识别中达到了F1-score为1.0，在中等复杂度的电路中保持了0.81的F1-score，显示出在复杂子电路中也有0.31的潜力，证明了其有效性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括电子设计自动化、集成电路设计以及教育领域。GENIE-ASI的无训练特性使其能够快速适应不同的电路设计任务，降低了对专业知识的依赖，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Analog subcircuit identification is a core task in analog design, essential for simulation, sizing, and layout. Traditional methods often require extensive human expertise, rule-based encoding, or large labeled datasets. To address these challenges, we propose GENIE-ASI, the first training-free, large language model (LLM)-based methodology for analog subcircuit identification. GENIE-ASI operates in two phases: it first uses in-context learning to derive natural language instructions from a few demonstration examples, then translates these into executable Python code to identify subcircuits in unseen SPICE netlists. In addition, to evaluate LLM-based approaches systematically, we introduce a new benchmark composed of operational amplifier netlists (op-amps) that cover a wide range of subcircuit variants. Experimental results on the proposed benchmark show that GENIE-ASI matches rule-based performance on simple structures (F1-score = 1.0), remains competitive on moderate abstractions (F1-score = 0.81), and shows potential even on complex subcircuits (F1-score = 0.31). These findings demonstrate that LLMs can serve as adaptable, general-purpose tools in analog design automation, opening new research directions for foundation model applications in analog design automation.


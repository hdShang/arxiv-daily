---
layout: default
title: Circuit Partitioning Using Large Language Models for Quantum Compilation and Simulations
---

# Circuit Partitioning Using Large Language Models for Quantum Compilation and Simulations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07711" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07711v1</a>
  <a href="https://arxiv.org/pdf/2505.07711.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07711v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07711v1', 'Circuit Partitioning Using Large Language Models for Quantum Compilation and Simulations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pranav Sinha, Sumit Kumar Jha, Sunny Raj

**分类**: cs.ET, cs.AI, quant-ph

**发布日期**: 2025-05-12

**备注**: 7 pages, 2 tables and 3 figures

---

## 💡 一句话要点

**利用大型语言模型进行量子电路分区以优化编译与仿真**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量子计算` `电路编译` `大型语言模型` `量子电路分区` `噪声门最小化` `机器学习` `量子算法`

## 📋 核心要点

1. 现有的量子电路编译算法在处理大型电路时面临计算挑战，限制了其应用范围。
2. 本文提出利用大型语言模型（LLMs）进行量子电路的分区，特别是通过快速分区方法来优化电路结构。
3. 实验结果显示，经过精细调优的开源LLMs在分区任务上取得53.4%的准确率，显著优于现成模型。

## 📝 摘要（中文）

在噪声中间规模量子（NISQ）时代，量子计算机受到噪声门的限制，导致最终计算结果不可靠。量子电路编译算法旨在减少噪声门的使用，但现有算法面临计算挑战，限制了其在5-6量子比特电路上的应用。因此，需要在应用噪声量子门最小化算法之前对大型电路进行分区。本文探讨了利用大型语言模型（如Llama和Mistral）进行量子电路分区的可能性，特别是通过快速分区方法来实现。实验结果表明，经过精细调优的开源大型语言模型在分区任务上的准确率达到53.4%，而现成的模型在标准的1-shot和few-shot训练方法下无法正确分区。

## 🔬 方法详解

**问题定义**：本文解决的是在量子电路编译中，如何有效地对大型电路进行分区的问题。现有的启发式算法无法考虑后续的门最小化任务，限制了其在大型电路上的应用。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）理解和生成量子电路代码，从而实现高效的电路分区。通过训练LLMs，使其能够执行快速分区方法，提升分区的准确性和效率。

**技术框架**：整体架构包括数据准备、模型训练和分区评估三个主要阶段。首先，收集量子电路数据并进行预处理；然后，使用开源LLMs进行训练，最后评估分区效果。

**关键创新**：最重要的技术创新在于将LLMs应用于量子电路分区任务，突破了传统方法的局限性，能够更好地适应复杂电路的需求。

**关键设计**：在模型训练中，采用了精细调优策略，设置了特定的损失函数以优化分区准确性，同时选择了适合量子电路的网络结构。

## 📊 实验亮点

实验结果表明，经过精细调优的开源大型语言模型在量子电路分区任务上的准确率达到53.4%，相比于现成的模型，表现出显著的提升，展示了LLMs在量子计算领域的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括量子计算机的电路优化、量子算法的高效实现以及量子仿真等。通过提高电路分区的准确性，可以显著提升量子计算的可靠性和效率，推动量子技术的实际应用和发展。

## 📄 摘要（原文）

> We are in the midst of the noisy intermediate-scale quantum (NISQ) era, where quantum computers are limited by noisy gates, some of which are more error-prone than others and can render the final computation incomprehensible. Quantum circuit compilation algorithms attempt to minimize these noisy gates when mapping quantum algorithms onto quantum hardware but face computational challenges that restrict their application to circuits with no more than 5-6 qubits, necessitating the need to partition large circuits before the application of noisy quantum gate minimization algorithms. The existing generation of these algorithms is heuristic in nature and does not account for downstream gate minimization tasks. Large language models (LLMs) have the potential to change this and help improve quantum circuit partitions. This paper investigates the use of LLMs, such as Llama and Mistral, for partitioning quantum circuits by capitalizing on their abilities to understand and generate code, including QASM. Specifically, we teach LLMs to partition circuits using the quick partition approach of the Berkeley Quantum Synthesis Toolkit. Through experimental evaluations, we show that careful fine-tuning of open source LLMs enables us to obtain an accuracy of 53.4% for the partition task while over-the-shelf LLMs are unable to correctly partition circuits, using standard 1-shot and few-shot training approaches.


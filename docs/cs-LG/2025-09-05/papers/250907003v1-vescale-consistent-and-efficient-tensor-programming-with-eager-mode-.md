---
layout: default
title: "veScale: Consistent and Efficient Tensor Programming with Eager-Mode SPMD"
---

# veScale: Consistent and Efficient Tensor Programming with Eager-Mode SPMD

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07003" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07003v1</a>
  <a href="https://arxiv.org/pdf/2509.07003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07003v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07003v1', 'veScale: Consistent and Efficient Tensor Programming with Eager-Mode SPMD')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youjie Li, Cheng Wan, Zhiqi Lin, Hongyu Zhu, Jiacheng Yang, Ziang Song, Xinyi Di, Jiawei Wu, Huiyao Shu, Wenlei Bao, Yanghua Peng, Haibin Lin, Li-Wen Chang

**分类**: cs.PL, cs.DC, cs.LG

**发布日期**: 2025-09-05

**备注**: 21 pages, 16 figures, 5 tables

---

## 💡 一句话要点

**veScale：通过Eager模式SPMD实现一致且高效的张量编程**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分布式训练` `Eager模式` `SPMD` `随机数生成` `性能优化`

## 📋 核心要点

1. 现有分布式训练系统，如PyTorch，在Eager模式下使用SPMD时，难以保证与单设备执行结果的一致性，调试困难。
2. veScale提出了一种新的分布式随机数生成（RNG）算法，该算法与任意分片算子兼容，从而确保了分布式训练结果的一致性。
3. veScale通过优化PyTorch原语开销和通信效率，显著提升了训练性能，实验表明其速度比TorchTitan快2.2倍。

## 📝 摘要（中文）

大型语言模型（LLMs）在规模和复杂性上迅速增长，需要越来越复杂的并行化方法来进行分布式训练，例如3D并行。这种复杂性促使人们转向更简单、更易于调试的编程范式，如单程序多数据（SPMD）。然而，Eager模式执行中的SPMD引入了两个关键挑战：确保与单设备执行的一致性，以及实现大规模下的高性能。本文介绍了veScale，一个Eager模式训练系统，它完全采用SPMD范式，以普及分布式张量编程。veScale通过引入一种与任意分片算子兼容的分布式随机数生成（RNG）的新算法，解决了PyTorch等系统中普遍存在的不一致结果问题。veScale还通过减少PyTorch原语的开销和提高通信效率，显著提高了训练性能。评估表明，veScale比最先进的训练系统（如TorchTitan）提速高达2.2倍，并将代码复杂性降低了78.4%，同时保持了与单设备等效的结果。

## 🔬 方法详解

**问题定义**：当前基于Eager模式的分布式训练，尤其是在SPMD范式下，面临着与单设备训练结果不一致的问题。这种不一致性使得调试和验证变得异常困难，阻碍了分布式训练的普及。现有方法在处理随机数生成和算子分片时，无法保证全局一致性，导致最终结果偏差。

**核心思路**：veScale的核心思路是通过设计一种与任意分片算子兼容的分布式随机数生成（RNG）算法，来保证分布式训练过程中随机数的一致性。同时，通过优化PyTorch原语的执行效率和通信效率，提升整体训练性能。这样既能保证结果的正确性，又能提升训练速度。

**技术框架**：veScale是一个Eager模式的分布式训练系统，它基于PyTorch构建，并完全采用SPMD范式。其主要模块包括：分布式随机数生成模块、优化的PyTorch原语执行引擎和高效的通信模块。训练流程与标准的PyTorch Eager模式类似，但veScale在底层对随机数生成、算子执行和通信进行了优化。

**关键创新**：veScale最重要的技术创新点在于其分布式随机数生成（RNG）算法。该算法能够保证在任意分片算子下，各个设备上生成的随机数序列与单设备执行时完全一致。这解决了分布式训练中结果不一致的根本问题。此外，对PyTorch原语的优化和通信效率的提升也显著提高了训练性能。

**关键设计**：veScale的分布式RNG算法采用了一种全局同步的种子生成机制，确保每个设备上的随机数生成器都使用相同的种子序列。同时，该算法还考虑了算子分片的影响，保证即使在算子被分片到不同设备上执行时，随机数序列仍然保持一致。在PyTorch原语优化方面，veScale采用了算子融合和内存复用等技术，减少了计算和内存访问的开销。在通信方面，veScale采用了高效的All-Reduce算法和数据压缩技术，降低了通信延迟。

## 📊 实验亮点

veScale在多个模型和数据集上进行了评估，实验结果表明，与最先进的训练系统TorchTitan相比，veScale实现了高达2.2倍的加速。同时，veScale的代码复杂性降低了78.4%，显著简化了分布式训练的编程难度。更重要的是，veScale保证了与单设备执行结果的一致性，解决了分布式训练中的关键问题。

## 🎯 应用场景

veScale适用于各种需要大规模分布式训练的场景，尤其是在训练大型语言模型（LLMs）时。它可以简化分布式训练的编程模型，降低调试难度，并提高训练效率。该研究成果有助于推动AI技术的普及和发展，加速LLM等复杂模型的训练和部署。

## 📄 摘要（原文）

> Large Language Models (LLMs) have scaled rapidly in size and complexity, requiring increasingly intricate parallelism for distributed training, such as 3D parallelism. This sophistication motivates a shift toward simpler, more debuggable programming paradigm like Single Program Multiple Data (SPMD). However, SPMD in eager execution introduces two key challenges: ensuring consistency with single-device execution and achieving high performance at scale. In this paper, we introduce veScale, an eager-mode training system that fully embraces SPMD paradigm to democratize distributed tensor programming. veScale addresses the prevalent issue of inconsistent results in systems like PyTorch by introducing a novel algorithm of distributed Random Number Generation (RNG) compatible with arbitrary sharded operators. veScale also significantly boosts training performance by reducing PyTorch primitive's overhead and improving communication efficiency. Evaluations show that veScale delivers up to 2.2x speedup over the state-of-the-art training systems, like TorchTitan, and cuts code complexity by 78.4%, while preserving single-device-equivalent results.


---
layout: default
title: REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning
---

# REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20613" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20613v3</a>
  <a href="https://arxiv.org/pdf/2505.20613.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20613v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20613v3', 'REAL-Prover: Retrieval Augmented Lean Prover for Mathematical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziju Shen, Naohao Huang, Fanyi Yang, Yutong Wang, Guoxiong Gao, Tianyi Xu, Jiedong Jiang, Wanyi He, Pu Yang, Mengzhou Sun, Haocheng Ju, Peihao Wu, Bryan Dai, Bin Dong

**分类**: cs.CL, cs.AI, cs.LG, cs.LO

**发布日期**: 2025-05-27 (更新: 2025-11-24)

---

## 💡 一句话要点

**提出REAL-Prover以解决高等数学定理证明问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `定理证明` `数学推理` `自然语言处理` `大型语言模型` `数据提取` `开源工具` `教育技术`

## 📋 核心要点

1. 现有的形式定理证明器在高等数学领域的应用有限，难以处理复杂的数学问题。
2. REAL-Prover通过结合微调的大型语言模型和检索系统，提升了定理证明的效率和准确性。
3. 在实验中，REAL-Prover在ProofNet数据集上取得23.7%的成功率，并在FATE-M基准上达到了56.7%的成功率，表现优异。

## 📝 摘要（中文）

近年来，形式定理证明器在高中及竞赛数学领域取得了显著进展，但在更高级的数学领域应用较少。本文提出了REAL-Prover，这是一个基于Lean 4的开源逐步定理证明器，旨在拓展这一边界。该证明器基于我们微调的大型语言模型（REAL-Prover-v1）并集成了检索系统（Leansearch-PS），显著提升了解决大学级数学问题的性能。通过开发数据提取管道HERALD-AF，将自然语言数学问题转化为形式化陈述，并创建新的开源Lean 4交互环境（Jixia-interactive）以促进数据收集。实验结果表明，使用仅经过监督微调的证明器在ProofNet数据集上取得了23.7%的成功率，且在新基准FATE-M上达到了56.7%的成功率，表现优于现有最先进模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有形式定理证明器在高等数学领域应用不足的问题，尤其是在处理复杂的数学问题时的局限性。现有方法往往无法有效推广到更高级的数学领域。

**核心思路**：REAL-Prover的核心思路是结合微调的大型语言模型与检索系统，以增强定理证明的能力。这种设计旨在通过更好地理解和处理自然语言数学问题，提升证明的成功率。

**技术框架**：REAL-Prover的整体架构包括三个主要模块：微调的大型语言模型（REAL-Prover-v1）、检索系统（Leansearch-PS）和数据提取管道（HERALD-AF）。数据提取管道负责将自然语言问题转化为形式化陈述，检索系统则用于辅助证明过程。

**关键创新**：REAL-Prover的主要创新在于其数据提取管道HERALD-AF和新创建的交互环境Jixia-interactive。这些创新使得从自然语言到形式化陈述的转换更加高效，进而提升了定理证明的整体性能。

**关键设计**：在模型训练中，采用了监督微调的方法，优化了模型的参数设置和损失函数，以确保在特定数学问题上的表现。同时，Leansearch-PS检索系统的设计也为模型提供了更丰富的上下文信息，增强了证明的准确性。

## 📊 实验亮点

在实验中，REAL-Prover在ProofNet数据集上取得了23.7%的成功率，表现与现有最先进模型相当。而在新提出的FATE-M基准上，REAL-Prover的成功率达到了56.7%，显示出显著的性能提升，证明了其在处理代数问题上的有效性。

## 🎯 应用场景

REAL-Prover的研究成果在教育、数学研究和自动化定理证明等领域具有广泛的应用潜力。它可以帮助学生和研究人员更高效地解决复杂的数学问题，推动数学教育的智能化发展。此外，随着技术的进步，REAL-Prover可能在其他领域的知识推理和自动化决策中发挥重要作用。

## 📄 摘要（原文）

> Nowadays, formal theorem provers have made monumental progress on high-school and competition-level mathematics, but few of them generalize to more advanced mathematics. In this paper, we present REAL-Prover, a new open-source stepwise theorem prover for Lean 4 to push this boundary. This prover, based on our fine-tuned large language model (REAL-Prover-v1) and integrated with a retrieval system (Leansearch-PS), notably boosts performance on solving college-level mathematics problems. To train REAL-Prover-v1, we developed HERALD-AF, a data extraction pipeline that converts natural language math problems into formal statements, and a new open-source Lean 4 interactive environment (Jixia-interactive) to facilitate synthesis data collection. In our experiments, our prover using only supervised fine-tune achieves competitive results with a 23.7% success rate (Pass@64) on the ProofNet dataset-comparable to state-of-the-art (SOTA) models. To further evaluate our approach, we introduce FATE-M, a new benchmark focused on algebraic problems, where our prover achieves a SOTA success rate of 56.7% (Pass@64).


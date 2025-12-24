---
layout: default
title: MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models
---

# MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19959" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19959v2</a>
  <a href="https://arxiv.org/pdf/2505.19959.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19959v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19959v2', 'MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongzhan Huang, Guoming Ling, Shanshan Zhong, Hefeng Wu, Liang Lin

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-07-30)

**备注**: Accepted by ACL'25 main track

**🔗 代码/项目**: [GITHUB](https://github.com/MilkThink-Lab/MiniLongBench)

---

## 💡 一句话要点

**提出MiniLongBench以降低长文本理解基准的评估成本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本理解` `大型语言模型` `基准评估` `数据压缩` `性能优化`

## 📋 核心要点

1. 现有的长文本理解基准评估成本高，影响了研究的效率和可持续性。
2. 本文提出了一种数据压缩方法，通过修剪LongBench基准，创建了MiniLongBench以降低评估成本。
3. MiniLongBench在对60多种LLM的测试中，评估成本降低至原来的4.5%，且与LongBench的相关性保持高达0.97。

## 📝 摘要（中文）

长文本理解（LCU）是当前大型语言模型（LLMs）研究的重要领域。然而，现有的LCU基准由于长文本数据的特性，往往导致评估成本过高。通过广泛实验，我们发现现有基准存在显著冗余，导致评估效率低下。本文提出了一种针对稀疏信息特征的长文本数据压缩方法，通过修剪现有的LongBench基准，创建了MiniLongBench。该基准仅包含237个测试样本，涵盖六个主要任务类别和21个不同任务。经过对60多种LLM的实证分析，MiniLongBench的评估成本降低至原来的4.5%，同时与LongBench结果的平均排名相关系数达到0.97。因此，MiniLongBench作为低成本基准，具有推动未来LLM长文本理解能力研究的巨大潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有长文本理解基准（如LongBench）评估成本过高的问题，导致研究效率低下。现有方法在测试时间和推理费用上存在显著冗余。

**核心思路**：通过提出一种针对长文本数据的压缩方法，去除冗余信息，保留关键任务样本，从而创建一个低成本的评估基准MiniLongBench。

**技术框架**：MiniLongBench的构建过程包括数据选择、样本修剪和任务分类，确保涵盖主要任务类别，同时减少样本数量。

**关键创新**：最重要的创新在于通过数据压缩技术显著降低了评估成本，同时保持了与原基准的高相关性，这是现有方法所未能实现的。

**关键设计**：在设计中，选择了237个样本，涵盖六个主要任务类别，确保评估的全面性与有效性，同时通过实证分析验证了评估成本的降低和相关性的保持。

## 📊 实验亮点

MiniLongBench在对60多种大型语言模型的评估中，成功将评估成本降低至原来的4.5%，同时与LongBench的结果保持了高达0.97的平均排名相关系数，显示出其在效率和准确性上的显著优势。

## 🎯 应用场景

MiniLongBench的研究成果可广泛应用于大型语言模型的长文本理解能力评估，尤其是在需要高效评估的场景中，如自然语言处理、信息检索和对话系统等领域。其低成本特性将推动相关研究的深入开展，促进技术的快速迭代与应用落地。

## 📄 摘要（原文）

> Long Context Understanding (LCU) is a critical area for exploration in current large language models (LLMs). However, due to the inherently lengthy nature of long-text data, existing LCU benchmarks for LLMs often result in prohibitively high evaluation costs, like testing time and inference expenses. Through extensive experimentation, we discover that existing LCU benchmarks exhibit significant redundancy, which means the inefficiency in evaluation. In this paper, we propose a concise data compression method tailored for long-text data with sparse information characteristics. By pruning the well-known LCU benchmark LongBench, we create MiniLongBench. This benchmark includes only 237 test samples across six major task categories and 21 distinct tasks. Through empirical analysis of over 60 LLMs, MiniLongBench achieves an average evaluation cost reduced to only 4.5% of the original while maintaining an average rank correlation coefficient of 0.97 with LongBench results. Therefore, our MiniLongBench, as a low-cost benchmark, holds great potential to substantially drive future research into the LCU capabilities of LLMs. See https://github.com/MilkThink-Lab/MiniLongBench for our code, data and tutorial.


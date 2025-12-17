---
layout: default
title: Estimating problem difficulty without ground truth using Large Language Model comparisons
---

# Estimating problem difficulty without ground truth using Large Language Model comparisons

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14220" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14220v1</a>
  <a href="https://arxiv.org/pdf/2512.14220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14220v1" onclick="toggleFavorite(this, '2512.14220v1', 'Estimating problem difficulty without ground truth using Large Language Model comparisons')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: 19 pages, 10 figures

---

## 💡 一句话要点

**提出LLM compare以解决问题难度估计的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `问题难度估计` `大型语言模型` `Bradley-Terry模型` `分布外问题` `人工智能应用`

## 📋 核心要点

1. 现有的难度估计方法无法有效推广到人类和LLMs无法解决的分布外问题，存在不可扩展和耗时等问题。
2. 本文提出的LLM compare方法通过LLM进行成对难度比较，计算Bradley-Terry分数，克服了现有方法的局限性。
3. 实验结果表明，LLM compare与人类标注的Pearson相关系数达到0.80以上，并且对噪声的鲁棒性良好，相关性仅下降6%。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的微调显著提升了其在基准测试中的表现，突显了对更复杂合成数据的需求。现有的难度估计方法，如人工校准或基于表现的评分，无法推广到人类和LLMs当前无法解决的分布外问题，因其不可扩展、耗时且依赖于真实标签。因此，本文提出了一种新的难度估计方法LLM compare，旨在克服这些局限性。该方法通过LLM进行成对难度比较，并基于结果计算Bradley-Terry分数。验证结果显示，LLM compare与人类标注高度一致，且对幻觉的鲁棒性良好，表现出显著的实际应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决如何在没有真实标签的情况下估计问题难度的挑战。现有方法如人工校准和基于表现的评分在处理分布外问题时表现不佳，缺乏可扩展性和效率。

**核心思路**：LLM compare方法通过大型语言模型进行成对的难度比较，利用Bradley-Terry模型计算难度分数。这一设计使得难度估计过程不依赖于真实标签，且能够动态适应不同问题。

**技术框架**：该方法的整体架构包括三个主要模块：首先，使用LLM进行成对比较；其次，基于比较结果计算Bradley-Terry分数；最后，评估和验证难度估计的准确性与鲁棒性。

**关键创新**：LLM compare是首个连续、动态、模型无关且不依赖真实标签的信息度量方法，能够有效处理分布外问题，填补了现有方法的空白。

**关键设计**：在设计中，LLM compare采用了成对比较的方式，确保了难度估计的相对性。此外，使用Bradley-Terry模型使得分数计算更加灵活，适应不同类型的问题。

## 📊 实验亮点

实验结果显示，LLM compare与人类标注的Pearson相关系数达到0.80以上，表明其在难度估计上的高一致性。此外，在进行10%的噪声注入时，相关性仅下降6%，显示出良好的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、模型评估和AI辅助研究构思等。通过提供高效的难度估计方法，LLM compare可以帮助设计更具挑战性的学习材料，优化模型训练过程，并推动人工智能在科学研究中的应用。

## 📄 摘要（原文）

> Recent advances in the finetuning of large language models (LLMs) have significantly improved their performance on established benchmarks, emphasizing the need for increasingly difficult, synthetic data. A key step in this data generation pipeline is a method for estimating problem difficulty. Current approaches, such as human calibration or performance-based scoring, fail to generalize to out-of-distribution problems, i.e. problems currently unsolvable by humans and LLMs, because they are not scalable, time-consuming, and ground truth dependent. Therefore, we propose a new method for estimating problem difficulty, LLM compare, that addresses these limitations. An LLM performs pairwise difficulty comparisons, and then Bradley-Terry scores are computed based on the outcomes. To validate our method, we first propose a conceptual framework that positions existing approaches on three orthogonal planes--construction, scale and dependence--identifying which quadrants a measure needs to occupy to score out-of-distribution problems. LLM compare naturally occupies all desirable quadrants as the first measure that is continuous and dynamic, model-agnostic and independent of ground truth information. As a second validation, we show that LLM compare demonstrates strong alignment with human annotations: Pearson $r \geq 0.80$ for $n=1876$. Thirdly, we show that LLM compare is robust to hallucinations, with less than $6\%$ degradation in Pearson correlation for $10\%$ noise injection. Our work represents a significant step towards replacing time-consuming human annotations and synthetic data generation, and will be an important driver for curriculum design, model evaluation, and AI-assisted research ideation.


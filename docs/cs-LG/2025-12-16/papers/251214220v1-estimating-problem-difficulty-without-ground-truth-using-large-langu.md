---
layout: default
title: Estimating problem difficulty without ground truth using Large Language Model comparisons
---

# Estimating problem difficulty without ground truth using Large Language Model comparisons

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14220" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14220v1</a>
  <a href="https://arxiv.org/pdf/2512.14220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14220v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14220v1', 'Estimating problem difficulty without ground truth using Large Language Model comparisons')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: 19 pages, 10 figures

---

## 💡 一句话要点

**提出LLM compare以解决无基准真值问题的难度估计**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `难度估计` `Bradley-Terry模型` `无基准真值` `人工智能` `模型评估` `教育技术`

## 📋 核心要点

1. 现有的难度估计方法无法有效推广到分布外问题，存在不可扩展和依赖基准真值的缺陷。
2. 本文提出的LLM compare方法通过LLM进行成对比较，计算Bradley-Terry评分，克服了现有方法的局限性。
3. 实验结果表明，LLM compare与人类注释高度一致，且对噪声具有良好的鲁棒性，相关性降幅小于6%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）微调技术的进步，其在标准基准上的表现显著提升，亟需生成更具挑战性的合成数据。现有的难度估计方法，如人工校准或基于性能的评分，无法有效推广到当前人类和LLMs无法解决的分布外问题，因其不可扩展、耗时且依赖基准真值。为此，本文提出了一种新的难度估计方法LLM compare，利用LLM进行成对难度比较，并基于结果计算Bradley-Terry评分。通过构建概念框架，本文验证了LLM compare在构建、规模和依赖性三个维度的优势，显示其为首个连续、动态、模型无关且独立于基准真值的信息度量。此外，LLM compare与人类注释高度一致，Pearson相关系数达到0.80以上，并对噪声具有良好的鲁棒性，降幅小于6%。

## 🔬 方法详解

**问题定义**：本文旨在解决如何在没有基准真值的情况下估计问题难度的具体问题。现有方法如人工校准和基于性能的评分在面对分布外问题时表现不佳，无法满足需求。

**核心思路**：论文提出的LLM compare方法通过大型语言模型进行成对难度比较，利用比较结果计算Bradley-Terry评分，从而实现难度的动态估计。该方法设计旨在避免对基准真值的依赖，并具备良好的扩展性。

**技术框架**：LLM compare的整体架构包括三个主要模块：首先，使用LLM进行成对问题的难度比较；其次，基于比较结果计算Bradley-Terry评分；最后，评估该评分与人类注释的相关性。

**关键创新**：LLM compare的最大创新在于其连续性和动态性，能够在没有基准真值的情况下进行有效的难度估计。这一特性使其在处理分布外问题时具备显著优势。

**关键设计**：在设计中，LLM compare采用了Bradley-Terry模型来量化比较结果，并通过实验验证其与人类注释的相关性，确保其鲁棒性和准确性。

## 📊 实验亮点

实验结果显示，LLM compare与人类注释的Pearson相关系数达到0.80以上，表明其在难度估计上的高准确性。此外，在进行10%的噪声注入实验时，相关性降幅小于6%，显示出该方法的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、模型评估和人工智能辅助研究等。通过提供一种高效的难度估计方法，LLM compare能够帮助设计更具挑战性的学习材料，优化模型训练过程，并推动AI在科研中的应用，提升研究效率。

## 📄 摘要（原文）

> Recent advances in the finetuning of large language models (LLMs) have significantly improved their performance on established benchmarks, emphasizing the need for increasingly difficult, synthetic data. A key step in this data generation pipeline is a method for estimating problem difficulty. Current approaches, such as human calibration or performance-based scoring, fail to generalize to out-of-distribution problems, i.e. problems currently unsolvable by humans and LLMs, because they are not scalable, time-consuming, and ground truth dependent. Therefore, we propose a new method for estimating problem difficulty, LLM compare, that addresses these limitations. An LLM performs pairwise difficulty comparisons, and then Bradley-Terry scores are computed based on the outcomes. To validate our method, we first propose a conceptual framework that positions existing approaches on three orthogonal planes--construction, scale and dependence--identifying which quadrants a measure needs to occupy to score out-of-distribution problems. LLM compare naturally occupies all desirable quadrants as the first measure that is continuous and dynamic, model-agnostic and independent of ground truth information. As a second validation, we show that LLM compare demonstrates strong alignment with human annotations: Pearson $r \geq 0.80$ for $n=1876$. Thirdly, we show that LLM compare is robust to hallucinations, with less than $6\%$ degradation in Pearson correlation for $10\%$ noise injection. Our work represents a significant step towards replacing time-consuming human annotations and synthetic data generation, and will be an important driver for curriculum design, model evaluation, and AI-assisted research ideation.


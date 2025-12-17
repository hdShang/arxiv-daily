---
layout: default
title: Estimating problem difficulty without ground truth using Large Language Model comparisons
---

# Estimating problem difficulty without ground truth using Large Language Model comparisons

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14220" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14220</a>
  <a href="https://arxiv.org/pdf/2512.14220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14220" onclick="toggleFavorite(this, '2512.14220', 'Estimating problem difficulty without ground truth using Large Language Model comparisons')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marthe Ballon, Andres Algaba, Brecht Verbeken, Vincent Ginis

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出LLM compare以解决无地面真相问题难度估计**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `难度估计` `Bradley-Terry模型` `无地面真相` `合成数据生成` `模型评估` `教育技术` `AI辅助研究`

## 📋 核心要点

1. 现有的难度估计方法如人工校准和表现评分无法有效处理分布外问题，缺乏可扩展性且依赖地面真相。
2. 本文提出的LLM compare方法通过LLM进行成对难度比较，计算Bradley-Terry分数，克服了现有方法的局限性。
3. 实验结果表明，LLM compare与人类注释的Pearson相关系数达到0.80以上，并且在噪声注入情况下表现出良好的鲁棒性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的微调显著提升了其在基准测试中的表现，突显了对更复杂合成数据的需求。现有的难度估计方法，如人工校准或基于表现的评分，无法推广到当前人类和LLMs无法解决的分布外问题，因为这些方法不具可扩展性、耗时且依赖于地面真相。因此，本文提出了一种新的难度估计方法LLM compare，旨在解决这些局限性。该方法通过LLM进行成对难度比较，并基于结果计算Bradley-Terry分数。我们验证了该方法的有效性，结果显示LLM compare与人类注释高度一致，且对噪声具有鲁棒性。我们的研究为替代耗时的人类注释和合成数据生成迈出了重要一步。

## 🔬 方法详解

**问题定义**：本文旨在解决如何在没有地面真相的情况下估计问题的难度。现有方法如人工校准和基于表现的评分在处理分布外问题时存在可扩展性差、耗时长和依赖地面真相等痛点。

**核心思路**：论文提出的LLM compare方法通过大型语言模型进行成对的难度比较，利用比较结果计算Bradley-Terry分数，从而实现对问题难度的估计。这种设计使得方法具备动态性和模型无关性，避免了对地面真相的依赖。

**技术框架**：该方法的整体架构包括三个主要模块：首先，使用LLM进行成对问题的难度比较；其次，基于比较结果计算Bradley-Terry分数；最后，验证该方法与人类注释的一致性及其对噪声的鲁棒性。

**关键创新**：LLM compare是首个在无地面真相情况下进行动态和连续难度估计的度量，具有模型无关性，能够有效处理分布外问题，与现有方法相比具有本质上的区别。

**关键设计**：在实现过程中，LLM compare的设计中考虑了成对比较的选择策略、Bradley-Terry模型的参数设置，以及在噪声注入情况下的性能评估等技术细节。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，LLM compare与人类注释的Pearson相关系数达到0.80以上，表明其在难度估计上的高一致性。此外，在进行10%噪声注入的情况下，Pearson相关性仅下降不到6%，显示出该方法的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括教育领域的课程设计、模型评估以及AI辅助的研究构思。通过提供一种高效的难度估计方法，研究人员和教育工作者可以更好地生成合成数据，优化学习路径和模型训练过程，提升整体研究效率。

## 📄 摘要（原文）

> Recent advances in the finetuning of large language models (LLMs) have significantly improved their performance on established benchmarks, emphasizing the need for increasingly difficult, synthetic data. A key step in this data generation pipeline is a method for estimating problem difficulty. Current approaches, such as human calibration or performance-based scoring, fail to generalize to out-of-distribution problems, i.e. problems currently unsolvable by humans and LLMs, because they are not scalable, time-consuming, and ground truth dependent. Therefore, we propose a new method for estimating problem difficulty, LLM compare, that addresses these limitations. An LLM performs pairwise difficulty comparisons, and then Bradley-Terry scores are computed based on the outcomes. To validate our method, we first propose a conceptual framework that positions existing approaches on three orthogonal planes--construction, scale and dependence--identifying which quadrants a measure needs to occupy to score out-of-distribution problems. LLM compare naturally occupies all desirable quadrants as the first measure that is continuous and dynamic, model-agnostic and independent of ground truth information. As a second validation, we show that LLM compare demonstrates strong alignment with human annotations: Pearson $r \geq 0.80$ for $n=1876$. Thirdly, we show that LLM compare is robust to hallucinations, with less than $6\%$ degradation in Pearson correlation for $10\%$ noise injection. Our work represents a significant step towards replacing time-consuming human annotations and synthetic data generation, and will be an important driver for curriculum design, model evaluation, and AI-assisted research ideation.


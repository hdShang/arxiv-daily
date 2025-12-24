---
layout: default
title: "Attributes as Textual Genes: Leveraging LLMs as Genetic Algorithm Simulators for Conditional Synthetic Data Generation"
---

# Attributes as Textual Genes: Leveraging LLMs as Genetic Algorithm Simulators for Conditional Synthetic Data Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02040" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02040v1</a>
  <a href="https://arxiv.org/pdf/2509.02040.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02040v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02040v1', 'Attributes as Textual Genes: Leveraging LLMs as Genetic Algorithm Simulators for Conditional Synthetic Data Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangzeng Han, Weisi Liu, Xiaolei Huang

**分类**: cs.CL

**发布日期**: 2025-09-02

**备注**: Accepted to EMNLP2025 Findings

---

## 💡 一句话要点

**提出Genetic Prompt，利用LLM作为遗传算法模拟器，实现条件性合成数据生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `合成数据生成` `遗传算法` `大型语言模型` `数据增强` `主动学习`

## 📋 核心要点

1. 现有合成数据生成方法难以保证数据质量和多样性，限制了其在实际应用中的效果。
2. Genetic Prompt将文本属性视为基因，利用LLM模拟遗传算法的交叉和变异，生成更优的合成数据。
3. 实验表明，Genetic Prompt在多个NLP任务上优于现有方法，并能有效提升下游模型的性能，尤其是在数据不平衡场景下。

## 📝 摘要（中文）

大型语言模型(LLMs)擅长生成合成数据，但保证其质量和多样性仍然具有挑战性。我们提出Genetic Prompt，这是一个将遗传算法与LLMs相结合以增强合成数据生成的新框架。我们的方法将语义文本属性视为基因序列，并利用LLM来模拟交叉和变异操作。这种遗传过程通过创建新的属性组合来提高数据质量和多样性，从而产生更接近真实世界数据的合成分布。为了优化父代选择，我们还集成了一种主动学习方案，以扩大后代搜索空间。我们在多个NLP任务上的实验表明：Genetic Prompt不仅显著优于最先进的基线，而且在各种生成器模型大小和规模上都表现出强大的性能。此外，我们证明了将我们的合成数据与原始训练集融合可以显著提高下游模型的性能，尤其是在类不平衡的情况下。我们的研究结果验证了Genetic Prompt是一种有效的方法，可以为各种NLP应用生成高质量的合成数据。

## 🔬 方法详解

**问题定义**：论文旨在解决合成数据生成中数据质量和多样性不足的问题。现有方法难以生成既真实又具有代表性的数据，尤其是在处理复杂或长尾分布的数据时，容易导致下游模型泛化能力下降。

**核心思路**：论文的核心思路是将文本属性视为基因，利用大型语言模型（LLM）模拟遗传算法中的交叉和变异过程。通过这种方式，可以探索新的属性组合，生成更丰富、更接近真实世界分布的合成数据。这种方法借鉴了生物进化的思想，通过不断迭代优化，提升合成数据的质量。

**技术框架**：Genetic Prompt框架主要包含以下几个阶段：1) **初始化**：选择初始的文本属性作为基因序列。2) **交叉**：利用LLM模拟基因交叉操作，将不同父代属性进行组合，生成新的后代属性。3) **变异**：利用LLM模拟基因变异操作，对现有属性进行微调或修改，引入新的属性变种。4) **评估与选择**：使用主动学习策略评估生成数据的质量，并选择优秀的后代作为下一轮迭代的父代。5) **合成数据生成**：利用LLM根据选择的属性生成最终的合成数据。

**关键创新**：该方法最重要的创新点在于将LLM与遗传算法相结合，利用LLM强大的文本生成能力和遗传算法的优化搜索能力，实现高质量、多样化的合成数据生成。与传统合成数据生成方法相比，Genetic Prompt能够更好地探索属性空间，生成更具代表性的数据。

**关键设计**：在交叉和变异操作中，论文使用了特定的Prompt工程技术，引导LLM生成符合要求的属性组合。主动学习策略用于评估生成数据的质量，并指导父代选择，从而加速优化过程。具体的损失函数和网络结构细节未在摘要中提及，属于未知信息。

## 📊 实验亮点

实验结果表明，Genetic Prompt在多个NLP任务上显著优于现有基线方法。通过将Genetic Prompt生成的合成数据与原始训练集融合，下游模型的性能得到了显著提升，尤其是在类不平衡场景下。实验还验证了Genetic Prompt在不同规模的生成器模型上的鲁棒性。

## 🎯 应用场景

该研究成果可广泛应用于自然语言处理领域，例如数据增强、文本生成、对话系统、机器翻译等。尤其是在数据稀缺或类别不平衡的情况下，Genetic Prompt能够生成高质量的合成数据，提升模型的泛化能力和鲁棒性。该方法还有潜力应用于其他领域，例如图像生成、音频生成等。

## 📄 摘要（原文）

> Large Language Models (LLMs) excel at generating synthetic data, but ensuring its quality and diversity remains challenging. We propose Genetic Prompt, a novel framework that combines genetic algorithms with LLMs to augment synthetic data generation. Our approach treats semantic text attributes as gene sequences and leverages the LLM to simulate crossover and mutation operations. This genetic process enhances data quality and diversity by creating novel attribute combinations, yielding synthetic distributions closer to real-world data. To optimize parent selection, we also integrate an active learning scheme that expands the offspring search space. Our experiments on multiple NLP tasks reveal several key findings: Genetic Prompt not only significantly outperforms state-of-the-art baselines but also shows robust performance across various generator model sizes and scales. Moreover, we demonstrate that fusing our synthetic data with the original training set significantly boosts downstream model performance, particularly for class-imbalanced scenarios. Our findings validate that Genetic Prompt is an effective method for producing high-quality synthetic data for a wide range of NLP applications.


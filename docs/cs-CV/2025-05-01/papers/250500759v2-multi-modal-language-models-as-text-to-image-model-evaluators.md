---
layout: default
title: Multi-Modal Language Models as Text-to-Image Model Evaluators
---

# Multi-Modal Language Models as Text-to-Image Model Evaluators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00759" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00759v2</a>
  <a href="https://arxiv.org/pdf/2505.00759.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00759v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00759v2', 'Multi-Modal Language Models as Text-to-Image Model Evaluators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahui Chen, Candace Ross, Reyhane Askari-Hemmat, Koustuv Sinha, Melissa Hall, Michal Drozdzal, Adriana Romero-Soriano

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-05-01 (更新: 2025-05-12)

---

## 💡 一句话要点

**提出多模态语言模型作为文本到图像模型评估工具**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态语言模型` `文本到图像生成` `模型评估` `生成对抗网络` `计算机视觉`

## 📋 核心要点

1. 现有的文本到图像生成模型评估方法依赖静态数据集，随着模型性能提升，这些方法逐渐失效。
2. 本文提出了MT2IE框架，通过多模态语言模型生成评估提示，评估图像质量和一致性。
3. 实验结果表明，MT2IE在提示生成一致性评分上与人类判断的相关性更高，同时显著减少了评估所需的提示数量。

## 📝 摘要（中文）

随着文本到图像生成模型的不断进步，依赖静态数据集的自动评估基准逐渐失效，促使研究者寻找新的评估方法。本文探讨了多模态大语言模型（MLLMs）作为评估代理的潜力，旨在评估提示生成的一致性和图像美学。我们提出了多模态文本到图像评估框架（MT2IE），该框架迭代生成评估提示，评分生成的图像，并将现有基准的T2I评估与使用的提示数量大幅减少的评估结果进行匹配。此外，我们展示了MT2IE的提示生成一致性评分与人类判断的相关性高于文献中先前提出的评分。MT2IE生成的提示在探测T2I模型性能方面效率高，仅使用1/80的提示数量即可产生与现有基准相同的相对T2I模型排名。

## 🔬 方法详解

**问题定义**：本文旨在解决传统文本到图像生成模型评估方法的局限性，尤其是依赖静态数据集导致的评估失效问题。现有方法无法适应快速发展的生成模型，缺乏灵活性和有效性。

**核心思路**：论文提出的核心思路是利用多模态大语言模型（MLLMs）作为评估代理，动态生成评估提示，以更好地评估生成图像的质量和一致性。通过这种方式，MT2IE能够更有效地适应模型的进步。

**技术框架**：MT2IE框架包括多个模块：首先，MLLMs生成用于评估的提示；其次，生成的图像通过评分机制进行评估；最后，将这些评估结果与现有基准进行对比，以验证其有效性。

**关键创新**：MT2IE的主要创新在于其提示生成的一致性评分与人类判断的相关性显著提高，同时在评估效率上大幅提升，仅使用1/80的提示数量即可获得与现有基准相同的模型排名。

**关键设计**：在设计中，MT2IE采用了高效的提示生成算法，结合了多模态学习的优势，确保生成的提示能够有效探测T2I模型的性能。具体的参数设置和损失函数设计尚未详细披露，属于未知领域。

## 📊 实验亮点

实验结果显示，MT2IE的提示生成一致性评分与人类判断的相关性显著提高，且在评估效率上表现优异，仅使用1/80的提示数量即可产生与现有基准相同的相对模型排名。这一成果为文本到图像生成模型的评估提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、生成对抗网络和人机交互等。MT2IE框架能够为文本到图像生成模型的评估提供更灵活和高效的解决方案，未来可能推动相关领域的研究进展与应用落地。

## 📄 摘要（原文）

> The steady improvements of text-to-image (T2I) generative models lead to slow deprecation of automatic evaluation benchmarks that rely on static datasets, motivating researchers to seek alternative ways to evaluate the T2I progress. In this paper, we explore the potential of multi-modal large language models (MLLMs) as evaluator agents that interact with a T2I model, with the objective of assessing prompt-generation consistency and image aesthetics. We present Multimodal Text-to-Image Eval (MT2IE), an evaluation framework that iteratively generates prompts for evaluation, scores generated images and matches T2I evaluation of existing benchmarks with a fraction of the prompts used in existing static benchmarks. Moreover, we show that MT2IE's prompt-generation consistency scores have higher correlation with human judgment than scores previously introduced in the literature. MT2IE generates prompts that are efficient at probing T2I model performance, producing the same relative T2I model rankings as existing benchmarks while using only 1/80th the number of prompts for evaluation.


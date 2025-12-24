---
layout: default
title: Integration of Large Language Models and Traditional Deep Learning for Social Determinants of Health Prediction
---

# Integration of Large Language Models and Traditional Deep Learning for Social Determinants of Health Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04655" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04655v1</a>
  <a href="https://arxiv.org/pdf/2505.04655.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04655v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04655v1', 'Integration of Large Language Models and Traditional Deep Learning for Social Determinants of Health Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Paul Landes, Jimeng Sun, Adam Cross

**分类**: cs.CL

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**结合大语言模型与传统深度学习以预测健康社会决定因素**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `健康社会决定因素` `大语言模型` `深度学习` `多标签分类` `自动预测` `临床文本分析` `合成数据`

## 📋 核心要点

1. 现有方法在提取健康社会决定因素时，往往面临处理速度慢和准确性不足的挑战。
2. 本文提出了一种结合大语言模型与传统深度学习的方法，以提高SDoH的提取效率和准确性。
3. 实验结果表明，所提模型在多标签分类任务中提升了10个百分点，并且执行时间缩短了12倍。

## 📝 摘要（中文）

健康社会决定因素（SDoH）是影响个体健康状况的经济、社会和个人环境。本文通过传统深度学习和大语言模型（LLMs）自动提取SDoH，评估各自的优缺点。我们的模型在多标签SDoH分类上超越了先前的基准，提升了10个百分点，并通过消除昂贵的LLM处理，显著加快了分类速度（执行时间缩短12倍）。我们的方法结合了LLM的精确性与传统深度学习的高效性。此外，使用合成数据补充的数据集上，我们的传统深度学习模型表现优于LLMs。我们的模型和方法为自动预测影响高风险患者的SDoH提供了新的迭代。

## 🔬 方法详解

**问题定义**：本文旨在解决在临床文本中自动提取健康社会决定因素（SDoH）的效率和准确性问题。现有方法通常依赖于昂贵的LLM处理，导致处理速度缓慢和资源消耗高。

**核心思路**：我们提出了一种新方法，结合了LLM的高精度与传统深度学习的高效性，通过优化处理流程，减少了对LLM的依赖，从而提高了分类速度。

**技术框架**：整体架构包括数据预处理、特征提取、模型训练和分类四个主要模块。首先，利用传统深度学习模型进行初步特征提取，然后通过LLM进行精细化处理，最后进行多标签分类。

**关键创新**：最重要的技术创新在于提出了一种高效的模型组合策略，能够在保持分类精度的同时，大幅度提高处理速度。这一策略与现有方法的根本区别在于减少了对LLM的频繁调用。

**关键设计**：在模型设计中，我们采用了特定的损失函数以优化多标签分类效果，并在网络结构上进行了调整，以适应合成数据的引入，确保模型在不同数据集上的泛化能力。

## 📊 实验亮点

实验结果显示，所提模型在多标签SDoH分类任务中相较于先前基准提升了10个百分点，且执行时间缩短了12倍。这表明结合传统深度学习与LLM的方法在效率和准确性上均有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、公共卫生和社会服务等。通过准确预测SDoH，医疗工作者可以更好地识别高风险患者，制定个性化的干预措施，从而改善患者的健康结果。未来，该方法有望在更广泛的健康数据分析中发挥重要作用。

## 📄 摘要（原文）

> Social Determinants of Health (SDoH) are economic, social and personal circumstances that affect or influence an individual's health status. SDoHs have shown to be correlated to wellness outcomes, and therefore, are useful to physicians in diagnosing diseases and in decision-making. In this work, we automatically extract SDoHs from clinical text using traditional deep learning and Large Language Models (LLMs) to find the advantages and disadvantages of each on an existing publicly available dataset. Our models outperform a previous reference point on a multilabel SDoH classification by 10 points, and we present a method and model to drastically speed up classification (12X execution time) by eliminating expensive LLM processing. The method we present combines a more nimble and efficient solution that leverages the power of the LLM for precision and traditional deep learning methods for efficiency. We also show highly performant results on a dataset supplemented with synthetic data and several traditional deep learning models that outperform LLMs. Our models and methods offer the next iteration of automatic prediction of SDoHs that impact at-risk patients.


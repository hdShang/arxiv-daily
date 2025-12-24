---
layout: default
title: "From Chat to Checkup: Can Large Language Models Assist in Diabetes Prediction?"
---

# From Chat to Checkup: Can Large Language Models Assist in Diabetes Prediction?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14949" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14949v1</a>
  <a href="https://arxiv.org/pdf/2506.14949.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14949v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14949v1', 'From Chat to Checkup: Can Large Language Models Assist in Diabetes Prediction?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shadman Sakib, Oishy Fatema Akhand, Ajwad Abrar

**分类**: cs.CL

**发布日期**: 2025-06-17

**备注**: Accepted in 1st IEEE QPAIN 2025

---

## 💡 一句话要点

**利用大型语言模型辅助糖尿病预测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `糖尿病预测` `机器学习` `深度学习` `医疗应用` `提示工程` `性能评估`

## 📋 核心要点

1. 现有的糖尿病预测方法主要依赖传统机器学习模型，存在性能和适应性不足的问题。
2. 本研究探索了大型语言模型在糖尿病预测中的应用，采用不同的提示方法进行实验。
3. 实验结果显示，专有LLMs在准确性和F1-score上优于传统机器学习模型，尤其是Gemma-2-27B表现突出。

## 📝 摘要（中文）

尽管机器学习和深度学习模型在糖尿病预测中得到了广泛应用，但大型语言模型（LLMs）在结构化数值数据中的应用仍未得到充分探索。本研究测试了LLMs在糖尿病预测中的有效性，采用零-shot、one-shot和three-shot提示方法，并使用Pima Indian Diabetes Database（PIDD）进行实证分析。我们评估了六种LLMs，包括四种开源模型和两种专有模型，并与三种传统机器学习模型进行比较。结果表明，专有LLMs的表现优于开源模型，尤其是GPT-4o和Gemma-2-27B在少量样本设置中取得了最高准确率。尽管如此，提示策略的性能变化和领域特定微调的需求仍然是问题所在。此研究表明LLMs在医疗预测任务中具有潜力，并鼓励未来在提示工程和混合方法方面的研究。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在糖尿病预测中的应用不足，尤其是在处理结构化数值数据时的挑战。现有方法主要依赖传统机器学习模型，存在性能和适应性不足的问题。

**核心思路**：论文提出通过零-shot、one-shot和three-shot提示方法，评估大型语言模型在糖尿病预测中的有效性，探索其在医疗预测任务中的潜力。

**技术框架**：整体架构包括数据预处理、模型选择、提示设计和性能评估四个主要模块。使用Pima Indian Diabetes Database进行实证分析，比较不同模型的预测效果。

**关键创新**：最重要的创新点在于将大型语言模型应用于结构化数值数据的糖尿病预测任务，尤其是通过不同的提示策略进行性能评估，填补了这一领域的研究空白。

**关键设计**：在实验中，选择了六种大型语言模型（包括开源和专有模型），并与传统机器学习模型（如随机森林、逻辑回归和支持向量机）进行比较。评估指标包括准确率、精确率、召回率和F1-score。

## 📊 实验亮点

实验结果显示，专有大型语言模型（如GPT-4o和Gemma-2-27B）在少量样本设置中取得了最高准确率，Gemma-2-27B在F1-score上也超越了传统机器学习模型。这表明LLMs在糖尿病预测任务中具有显著的优势，尤其是在处理复杂数据时。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、糖尿病管理和智能诊断系统。通过利用大型语言模型，能够提高糖尿病预测的准确性和效率，为医生提供更可靠的决策支持，进而改善患者的健康管理。未来，随着提示工程和混合方法的进一步研究，LLMs在医疗领域的应用前景将更加广阔。

## 📄 摘要（原文）

> While Machine Learning (ML) and Deep Learning (DL) models have been widely used for diabetes prediction, the use of Large Language Models (LLMs) for structured numerical data is still not well explored. In this study, we test the effectiveness of LLMs in predicting diabetes using zero-shot, one-shot, and three-shot prompting methods. We conduct an empirical analysis using the Pima Indian Diabetes Database (PIDD). We evaluate six LLMs, including four open-source models: Gemma-2-27B, Mistral-7B, Llama-3.1-8B, and Llama-3.2-2B. We also test two proprietary models: GPT-4o and Gemini Flash 2.0. In addition, we compare their performance with three traditional machine learning models: Random Forest, Logistic Regression, and Support Vector Machine (SVM). We use accuracy, precision, recall, and F1-score as evaluation metrics. Our results show that proprietary LLMs perform better than open-source ones, with GPT-4o and Gemma-2-27B achieving the highest accuracy in few-shot settings. Notably, Gemma-2-27B also outperforms the traditional ML models in terms of F1-score. However, there are still issues such as performance variation across prompting strategies and the need for domain-specific fine-tuning. This study shows that LLMs can be useful for medical prediction tasks and encourages future work on prompt engineering and hybrid approaches to improve healthcare predictions.


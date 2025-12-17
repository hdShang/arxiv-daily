---
layout: default
title: Lost in Translation and Noise: A Deep Dive into the Failure Modes of VLMs on Real-World Tables
---

# Lost in Translation and Noise: A Deep Dive into the Failure Modes of VLMs on Real-World Tables

**arXiv**: [2511.17238v1](https://arxiv.org/abs/2511.17238) | [PDF](https://arxiv.org/pdf/2511.17238.pdf)

**作者**: Anshul Singh, Rohan Chaudhary, Gagneet Singh, Abhay Kumary

---

## 💡 一句话要点

**提出MirageTVQA基准以评估视觉语言模型在真实世界多语言和噪声表格中的表现**

**关键词**: `视觉语言模型` `表格问答` `多语言基准` `视觉噪声` `性能评估` `真实世界场景`

## 📋 核心要点

1. 现有表格问答数据集多为英语且格式完美，与现实场景存在差距
2. 构建多语言含噪声表格基准，包含近6万QA对和24种语言
3. 评估显示模型在视觉噪声下性能下降超35%，存在英语优先偏见

## 📄 摘要（原文）

> The impressive performance of VLMs is largely measured on benchmarks that fail to capture the complexities of real-world scenarios. Existing datasets for tabular QA, such as WikiTableQuestions and FinQA, are overwhelmingly monolingual (English) and present tables in a digitally perfect, clean format. This creates a significant gap between research and practice. To address this, we present \textbf{MirageTVQA}, a new benchmark designed to evaluate VLMs on these exact dimensions. Featuring nearly 60,000 QA pairs across 24 languages, MirageTVQA challenges models with tables that are not only multilingual but also visually imperfect, incorporating realistic noise to mimic scanned documents. Our evaluation of the leading VLMs reveals two primary failure points: a severe degradation in performance (over 35\% drop for the best models) when faced with visual noise and a consistent English-first bias where reasoning abilities fail to transfer to other languages. MirageTVQA provides a benchmark for measuring and driving progress towards more robust VLM models for table reasoning. The dataset and the code are available at: https://github.com/anshulsc/MirageTVQA.


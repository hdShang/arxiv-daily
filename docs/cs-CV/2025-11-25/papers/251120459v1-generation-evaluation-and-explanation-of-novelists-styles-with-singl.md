---
layout: default
title: Generation, Evaluation, and Explanation of Novelists' Styles with Single-Token Prompts
---

# Generation, Evaluation, and Explanation of Novelists' Styles with Single-Token Prompts

**arXiv**: [2511.20459v1](https://arxiv.org/abs/2511.20459) | [PDF](https://arxiv.org/pdf/2511.20459.pdf)

**作者**: Mosab Rezaei, Mina Rajaei Moghadam, Abdul Rahman Shaikh, Hamed Alhoori, Reva Freedman

---

## 💡 一句话要点

**提出单令牌提示框架以生成和评估19世纪小说家风格文本**

**关键词**: `风格生成` `单令牌提示` `Transformer检测器` `可解释AI` `19世纪小说家` `风格评估`

## 📋 核心要点

1. 核心问题：无配对数据时生成风格文本及非人工评估方法
2. 方法要点：微调大语言模型，使用单令牌提示生成作者风格句子
3. 实验或效果：基于Transformer检测器评估，生成文本反映作者独特模式

## 📄 摘要（原文）

> Recent advances in large language models have created new opportunities for stylometry, the study of writing styles and authorship. Two challenges, however, remain central: training generative models when no paired data exist, and evaluating stylistic text without relying only on human judgment. In this work, we present a framework for both generating and evaluating sentences in the style of 19th-century novelists. Large language models are fine-tuned with minimal, single-token prompts to produce text in the voices of authors such as Dickens, Austen, Twain, Alcott, and Melville. To assess these generative models, we employ a transformer-based detector trained on authentic sentences, using it both as a classifier and as a tool for stylistic explanation. We complement this with syntactic comparisons and explainable AI methods, including attention-based and gradient-based analyses, to identify the linguistic cues that drive stylistic imitation. Our findings show that the generated text reflects the authors' distinctive patterns and that AI-based evaluation offers a reliable alternative to human assessment. All artifacts of this work are published online.


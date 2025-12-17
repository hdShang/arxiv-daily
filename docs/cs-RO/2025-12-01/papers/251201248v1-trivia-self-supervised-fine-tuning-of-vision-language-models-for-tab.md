---
layout: default
title: TRivia: Self-supervised Fine-tuning of Vision-Language Models for Table Recognition
---

# TRivia: Self-supervised Fine-tuning of Vision-Language Models for Table Recognition

**arXiv**: [2512.01248v1](https://arxiv.org/abs/2512.01248) | [PDF](https://arxiv.org/pdf/2512.01248.pdf)

**作者**: Junyuan Zhang, Bin Wang, Qintong Zhang, Fan Wu, Zichen Wen, Jialin Lu, Junjie Shan, Ziqi Zhao, Shuya Yang, Ziling Wang, Ziyang Miao, Huaping Zhong, Yuhang Zang, Xiaoyi Dong, Ka-Ho Chow, Conghui He

---

## 💡 一句话要点

**提出TRivia自监督微调方法，利用无标注表格图像提升视觉语言模型的表格识别性能。**

**关键词**: `表格识别` `自监督学习` `视觉语言模型` `微调方法` `开源模型`

## 📋 核心要点

1. 核心问题：表格识别依赖大规模标注数据，开源模型因资源限制性能落后。
2. 方法要点：基于Group Relative Policy Optimization，通过问答奖励机制自动选择有效样本，无需人工标注。
3. 实验或效果：TRivia-3B模型在三个基准测试中超越现有系统，如Gemini 2.5 Pro。

## 📄 摘要（原文）

> Table recognition (TR) aims to transform table images into semi-structured representations such as HTML or Markdown. As a core component of document parsing, TR has long relied on supervised learning, with recent efforts dominated by fine-tuning vision-language models (VLMs) using labeled data. While VLMs have brought TR to the next level, pushing performance further demands large-scale labeled data that is costly to obtain. Consequently, although proprietary models have continuously pushed the performance boundary, open-source models, often trained with limited resources and, in practice, the only viable option for many due to privacy regulations, still lag far behind. To bridge this gap, we introduce TRivia, a self-supervised fine-tuning method that enables pretrained VLMs to learn TR directly from unlabeled table images in the wild. Built upon Group Relative Policy Optimization, TRivia automatically identifies unlabeled samples that most effectively facilitate learning and eliminates the need for human annotations through a question-answering-based reward mechanism. An attention-guided module generates diverse questions for each table image, and the ability to interpret the recognition results and answer them correctly provides feedback to optimize the TR model. This closed-loop process allows the TR model to autonomously learn to recognize, structure, and reason over tables without labeled data. Leveraging this pipeline, we present TRivia-3B, an open-sourced, compact, and state-of-the-art TR model that surpasses existing systems (e.g., Gemini 2.5 Pro, MinerU2.5) on three popular benchmarks. Model and code are released at: https://github.com/opendatalab/TRivia


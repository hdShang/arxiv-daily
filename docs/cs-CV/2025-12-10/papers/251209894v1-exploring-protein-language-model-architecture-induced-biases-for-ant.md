---
layout: default
title: Exploring Protein Language Model Architecture-Induced Biases for Antibody Comprehension
---

# Exploring Protein Language Model Architecture-Induced Biases for Antibody Comprehension

**arXiv**: [2512.09894v1](https://arxiv.org/abs/2512.09894) | [PDF](https://arxiv.org/pdf/2512.09894.pdf)

**作者**: Mengren, Liu, Yixiang Zhang, Yiming, Zhang

---

## 💡 一句话要点

**探索蛋白质语言模型架构诱导的偏见以提升抗体理解能力**

**关键词**: `蛋白质语言模型` `抗体理解` `架构偏见` `注意力归因分析` `计算抗体设计`

## 📋 核心要点

1. 核心问题：不同蛋白质语言模型架构如何影响抗体特异性生物特征的捕获能力
2. 方法要点：系统评估AntiBERTa、BioBERT、ESM2和GPT-2在抗体靶标特异性预测任务中的表现
3. 实验或效果：通过注意力归因分析揭示模型在V基因使用、体细胞超突变和同种型信息上的偏见

## 📄 摘要（原文）

> Recent advances in protein language models (PLMs) have demonstrated remarkable capabilities in understanding protein sequences. However, the extent to which different model architectures capture antibody-specific biological properties remains unexplored. In this work, we systematically investigate how architectural choices in PLMs influence their ability to comprehend antibody sequence characteristics and functions. We evaluate three state-of-the-art PLMs-AntiBERTa, BioBERT, and ESM2--against a general-purpose language model (GPT-2) baseline on antibody target specificity prediction tasks. Our results demonstrate that while all PLMs achieve high classification accuracy, they exhibit distinct biases in capturing biological features such as V gene usage, somatic hypermutation patterns, and isotype information. Through attention attribution analysis, we show that antibody-specific models like AntiBERTa naturally learn to focus on complementarity-determining regions (CDRs), while general protein models benefit significantly from explicit CDR-focused training strategies. These findings provide insights into the relationship between model architecture and biological feature extraction, offering valuable guidance for future PLM development in computational antibody design.


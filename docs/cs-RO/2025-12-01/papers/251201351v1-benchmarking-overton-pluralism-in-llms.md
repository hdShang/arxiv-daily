---
layout: default
title: Benchmarking Overton Pluralism in LLMs
---

# Benchmarking Overton Pluralism in LLMs

**arXiv**: [2512.01351v1](https://arxiv.org/abs/2512.01351) | [PDF](https://arxiv.org/pdf/2512.01351.pdf)

**作者**: Elinor Poole-Dayan, Jiayi Wu, Taylor Sorensen, Jiaxin Pei, Michiel A. Bakker

---

## 💡 一句话要点

**提出OvertonScore框架以评估大语言模型中的观点多样性**

**关键词**: `观点多样性评估` `大语言模型基准` `集合覆盖度量` `人类研究` `自动化评估` `模型对齐`

## 📋 核心要点

1. 核心问题：如何量化大语言模型输出中的观点多样性（Overton pluralism）。
2. 方法要点：定义OvertonScore作为集合覆盖度量，并开发自动化基准以复现人类判断。
3. 实验或效果：在8个LLMs上进行大规模人类研究，模型平均得分0.35-0.41，自动化基准与人类判断高度相关（ρ=0.88）。

## 📄 摘要（原文）

> We introduce a novel framework for measuring Overton pluralism in LLMs--the extent to which diverse viewpoints are represented in model outputs. We (i) formalize Overton pluralism as a set coverage metric (OvertonScore), (ii) conduct a large-scale U.S.-representative human study (N = 1209; 60 questions; 8 LLMs), and (iii) develop an automated benchmark that closely reproduces human judgments. On average, models achieve OvertonScores of 0.35--0.41, with DeepSeek V3 performing best; yet all models remain far below the theoretical maximum of 1.0, revealing substantial headroom for improvement. Because repeated large-scale human studies are costly and slow, scalable evaluation tools are essential for model development. Hence, we propose an automated benchmark that achieves high rank correlation with human judgments ($ρ=0.88$), providing a practical proxy without replacing human assessment. By turning pluralistic alignment from a normative aim into a measurable benchmark, our work establishes a foundation for systematic progress toward more pluralistic LLMs.


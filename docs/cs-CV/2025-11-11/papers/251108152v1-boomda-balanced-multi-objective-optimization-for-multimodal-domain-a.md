---
layout: default
title: Boomda: Balanced Multi-objective Optimization for Multimodal Domain Adaptation
---

# Boomda: Balanced Multi-objective Optimization for Multimodal Domain Adaptation

**arXiv**: [2511.08152v1](https://arxiv.org/abs/2511.08152) | [PDF](https://arxiv.org/pdf/2511.08152.pdf)

**作者**: Jun Sun, Xinxin Zhang, Simin Hong, Jian Zhu, Xiang Gao

---

## 💡 一句话要点

**提出Boomda方法以平衡多模态领域适应中的多目标优化问题**

**关键词**: `多模态学习` `无监督领域适应` `多目标优化` `信息瓶颈` `相关性对齐`

## 📋 核心要点

1. 核心问题：多模态学习中不同模态的领域偏移不一致，导致无监督领域适应困难
2. 方法要点：使用信息瓶颈和相关性对齐，将多目标优化简化为二次规划问题求解
3. 实验或效果：在多个数据集上验证，Boomda优于现有方法，代码已开源

## 📄 摘要（原文）

> Multimodal learning, while contributing to numerous success stories across various fields, faces the challenge of prohibitively expensive manual annotation. To address the scarcity of annotated data, a popular solution is unsupervised domain adaptation, which has been extensively studied in unimodal settings yet remains less explored in multimodal settings. In this paper, we investigate heterogeneous multimodal domain adaptation, where the primary challenge is the varying domain shifts of different modalities from the source to the target domain. We first introduce the information bottleneck method to learn representations for each modality independently, and then match the source and target domains in the representation space with correlation alignment. To balance the domain alignment of all modalities, we formulate the problem as a multi-objective task, aiming for a Pareto optimal solution. By exploiting the properties specific to our model, the problem can be simplified to a quadratic programming problem. Further approximation yields a closed-form solution, leading to an efficient modality-balanced multimodal domain adaptation algorithm. The proposed method features \textbf{B}alanced multi-\textbf{o}bjective \textbf{o}ptimization for \textbf{m}ultimodal \textbf{d}omain \textbf{a}daptation, termed \textbf{Boomda}. Extensive empirical results showcase the effectiveness of the proposed approach and demonstrate that Boomda outperforms the competing schemes. The code is is available at: https://github.com/sunjunaimer/Boomda.git.


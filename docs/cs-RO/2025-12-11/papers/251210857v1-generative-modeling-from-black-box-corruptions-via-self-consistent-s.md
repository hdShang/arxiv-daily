---
layout: default
title: Generative Modeling from Black-box Corruptions via Self-Consistent Stochastic Interpolants
---

# Generative Modeling from Black-box Corruptions via Self-Consistent Stochastic Interpolants

**arXiv**: [2512.10857v1](https://arxiv.org/abs/2512.10857) | [PDF](https://arxiv.org/pdf/2512.10857.pdf)

**作者**: Chirag Modi, Jiequn Han, Eric Vanden-Eijnden, Joan Bruna

---

## 💡 一句话要点

**提出自洽随机插值法，通过黑盒噪声通道从损坏数据生成清洁数据模型**

**关键词**: `生成建模` `逆问题` `随机插值` `传输映射` `黑盒优化` `数据反演`

## 📋 核心要点

1. 核心问题：在科学和工程领域，数据常被噪声或病态通道损坏，需从损坏分布反演清洁数据生成模型
2. 方法要点：基于随机插值，迭代更新损坏与清洁数据间的传输映射，仅需黑盒访问损坏通道，实现自洽反演
3. 实验或效果：在自然图像处理和科学重建逆问题上表现优异，计算高效且具理论保证

## 📄 摘要（原文）

> Transport-based methods have emerged as a leading paradigm for building generative models from large, clean datasets. However, in many scientific and engineering domains, clean data are often unavailable: instead, we only observe measurements corrupted through a noisy, ill-conditioned channel. A generative model for the original data thus requires solving an inverse problem at the level of distributions. In this work, we introduce a novel approach to this task based on Stochastic Interpolants: we iteratively update a transport map between corrupted and clean data samples using only access to the corrupted dataset as well as black box access to the corruption channel. Under appropriate conditions, this iterative procedure converges towards a self-consistent transport map that effectively inverts the corruption channel, thus enabling a generative model for the clean data. We refer to the resulting method as the self-consistent stochastic interpolant (SCSI). It (i) is computationally efficient compared to variational alternatives, (ii) highly flexible, handling arbitrary nonlinear forward models with only black-box access, and (iii) enjoys theoretical guarantees. We demonstrate superior performance on inverse problems in natural image processing and scientific reconstruction, and establish convergence guarantees of the scheme under appropriate assumptions.


---
layout: default
title: Common Structure Discovery in Collections of Bipartite Networks: Application to Pollination Systems
---

# Common Structure Discovery in Collections of Bipartite Networks: Application to Pollination Systems

**arXiv**: [2512.01716v1](https://arxiv.org/abs/2512.01716) | [PDF](https://arxiv.org/pdf/2512.01716.pdf)

**作者**: Louis Lacoste, Pierre Barbillon, Sophie Donnet

---

## 💡 一句话要点

**提出colBiSBM模型以发现二分网络集合中的共同结构，应用于植物-传粉者系统分析。**

**关键词**: `二分网络` `共同结构发现` `潜在块模型` `变分EM算法` `生态网络分析` `模型选择`

## 📋 核心要点

1. 核心问题：现有方法忽略二分网络集合中的共享模式，难以比较网络组织。
2. 方法要点：扩展潜在块模型，假设网络共享块间连接参数，开发变分EM算法和ICL准则。
3. 实验或效果：模拟显示能恢复共同结构、提升聚类和链接预测；应用揭示生态角色和网络分组。

## 📄 摘要（原文）

> Bipartite networks are widely used to encode the ecological interactions. Being able to compare the organization of bipartite networks is a first step toward a better understanding of how environmental factors shape community structure and resilience. Yet current methods for structure detection in bipartite networks overlook shared patterns across collections of networks. We introduce the \emph{colBiSBM}, a family of probabilistic models for collections of bipartite networks that extends the classical Latent Block Model (LBM). The proposed framework assumes that networks are independent realizations of a shared mesoscale structure, encoded through common inter-block connectivity parameters. We establish identifiability conditions for the different variants of \emph{colBiSBM} and develop a variational EM algorithm for parameter estimation, coupled with an adaptation of the Integrated Classification Likelihood (ICL) criterion for model selection. We demonstrate how our approach can be used to classify networks based on their topology or organization. Simulation studies highlight the ability of \emph{colBiSBM} to recover common structures, improve clustering performance, and enhance link prediction by borrowing strength across networks. An application to plant--pollinator networks highlights how the method uncovers shared ecological roles and partitions networks into sub-collections with similar connectivity patterns. These results illustrate the methodological and practical advantages of joint modeling over separate network analyses in the study of bipartite systems.


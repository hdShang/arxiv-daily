---
layout: default
title: On Evolution-Based Models for Experimentation Under Interference
---

# On Evolution-Based Models for Experimentation Under Interference

**arXiv**: [2511.21675v1](https://arxiv.org/abs/2511.21675) | [PDF](https://arxiv.org/pdf/2511.21675.pdf)

**作者**: Sadegh Shirani, Mohsen Bayati

---

## 💡 一句话要点

**提出基于演化的模型以估计网络系统中的因果效应，补偿未观测干扰结构。**

**关键词**: `因果效应估计` `网络干扰` `演化模型` `暴露映射` `随机化实验` `溢出效应`

## 📋 核心要点

1. 核心问题：网络系统中因果效应估计因未观测干扰结构而复杂。
2. 方法要点：利用结果演化和暴露映射，无需恢复精确网络结构。
3. 实验或效果：通过随机化处理学习异质溢出效应，扩展至密集和影响者网络。

## 📄 摘要（原文）

> Causal effect estimation in networked systems is central to data-driven decision making. In such settings, interventions on one unit can spill over to others, and in complex physical or social systems, the interaction pathways driving these interference structures remain largely unobserved. We argue that for identifying population-level causal effects, it is not necessary to recover the exact network structure; instead, it suffices to characterize how those interactions contribute to the evolution of outcomes. Building on this principle, we study an evolution-based approach that investigates how outcomes change across observation rounds in response to interventions, hence compensating for missing network information. Using an exposure-mapping perspective, we give an axiomatic characterization of when the empirical distribution of outcomes follows a low-dimensional recursive equation, and identify minimal structural conditions under which such evolution mappings exist. We frame this as a distributional counterpart to difference-in-differences. Rather than assuming parallel paths for individual units, it exploits parallel evolution patterns across treatment scenarios to estimate counterfactual trajectories. A key insight is that treatment randomization plays a role beyond eliminating latent confounding; it induces an implicit sampling from hidden interference channels, enabling consistent learning about heterogeneous spillover effects. We highlight causal message passing as an instantiation of this method in dense networks while extending to more general interference structures, including influencer networks where a small set of units drives most spillovers. Finally, we discuss the limits of this approach, showing that strong temporal trends or endogenous interference can undermine identification.


---
layout: default
title: LGDC: Latent Graph Diffusion via Spectrum-Preserving Coarsening
---

# LGDC: Latent Graph Diffusion via Spectrum-Preserving Coarsening

**arXiv**: [2512.01190v1](https://arxiv.org/abs/2512.01190) | [PDF](https://arxiv.org/pdf/2512.01190.pdf)

**作者**: Nagham Osman, Keyue Jiang, Davide Buffelli, Xiaowen Dong, Laura Toni

---

## 💡 一句话要点

**提出LGDC混合框架，结合自回归与扩散模型优势，高效生成兼具局部和全局结构的图**

**关键词**: `图生成` `扩散模型` `自回归模型` `谱保持粗化` `混合框架` `潜在空间`

## 📋 核心要点

1. 分析图生成任务中自回归与扩散模型的权衡：自回归擅长局部结构，扩散擅长全局模式
2. 提出LGDC，通过谱保持粗化-反粗化双向映射，在潜在空间用扩散生成图后恢复细节
3. 实验验证LGDC在局部结构数据集（Tree）和全局结构数据集（Planar, Community-20）上均表现优异

## 📄 摘要（原文）

> Graph generation is a critical task across scientific domains. Existing methods fall broadly into two categories: autoregressive models, which iteratively expand graphs, and one-shot models, such as diffusion, which generate the full graph at once. In this work, we provide an analysis of these two paradigms and reveal a key trade-off: autoregressive models stand out in capturing fine-grained local structures, such as degree and clustering properties, whereas one-shot models excel at modeling global patterns, such as spectral distributions. Building on this, we propose LGDC (latent graph diffusion via spectrum-preserving coarsening), a hybrid framework that combines strengths of both approaches. LGDC employs a spectrum-preserving coarsening-decoarsening to bidirectionally map between graphs and a latent space, where diffusion efficiently generates latent graphs before expansion restores detail. This design captures both local and global properties with improved efficiency. Empirically, LGDC matches autoregressive models on locally structured datasets (Tree) and diffusion models on globally structured ones (Planar, Community-20), validating the benefits of hybrid generation.


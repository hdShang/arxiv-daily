---
layout: default
title: TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion Models
---

# TreeGRPO: Tree-Advantage GRPO for Online RL Post-Training of Diffusion Models

**arXiv**: [2512.08153v1](https://arxiv.org/abs/2512.08153) | [PDF](https://arxiv.org/pdf/2512.08153.pdf)

**作者**: Zheng Ding, Weirui Ye

---

## 💡 一句话要点

**提出TreeGRPO以高效解决扩散模型在线强化学习后训练的计算成本问题**

**关键词**: `强化学习后训练` `扩散模型对齐` `树结构搜索` `样本效率` `信用分配` `计算优化`

## 📋 核心要点

1. 核心问题：强化学习后训练计算成本高，阻碍生成模型与人类偏好的对齐。
2. 方法要点：将去噪过程重构为搜索树，通过分支生成候选轨迹并重用公共前缀，实现高效样本利用和细粒度信用分配。
3. 实验或效果：在扩散和流模型中，训练速度提升2.4倍，在效率-奖励权衡空间建立更优帕累托前沿。

## 📄 摘要（原文）

> Reinforcement learning (RL) post-training is crucial for aligning generative models with human preferences, but its prohibitive computational cost remains a major barrier to widespread adoption. We introduce \textbf{TreeGRPO}, a novel RL framework that dramatically improves training efficiency by recasting the denoising process as a search tree. From shared initial noise samples, TreeGRPO strategically branches to generate multiple candidate trajectories while efficiently reusing their common prefixes. This tree-structured approach delivers three key advantages: (1) \emph{High sample efficiency}, achieving better performance under same training samples (2) \emph{Fine-grained credit assignment} via reward backpropagation that computes step-specific advantages, overcoming the uniform credit assignment limitation of trajectory-based methods, and (3) \emph{Amortized computation} where multi-child branching enables multiple policy updates per forward pass. Extensive experiments on both diffusion and flow-based models demonstrate that TreeGRPO achieves \textbf{2.4$\times$ faster training} while establishing a superior Pareto frontier in the efficiency-reward trade-off space. Our method consistently outperforms GRPO baselines across multiple benchmarks and reward models, providing a scalable and effective pathway for RL-based visual generative model alignment. The project website is available at treegrpo.github.io.


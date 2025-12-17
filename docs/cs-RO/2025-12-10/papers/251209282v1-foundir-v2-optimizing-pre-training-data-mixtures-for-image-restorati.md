---
layout: default
title: FoundIR-v2: Optimizing Pre-Training Data Mixtures for Image Restoration Foundation Model
---

# FoundIR-v2: Optimizing Pre-Training Data Mixtures for Image Restoration Foundation Model

**arXiv**: [2512.09282v1](https://arxiv.org/abs/2512.09282) | [PDF](https://arxiv.org/pdf/2512.09282.pdf)

**作者**: Xiang Chen, Jinshan Pan, Jiangxin Dong, Jian Yang, Jinhui Tang

---

## 💡 一句话要点

**提出FoundIR-v2，通过数据均衡调度优化预训练数据混合比例以提升图像修复基础模型性能**

**关键词**: `图像修复基础模型` `数据混合优化` `扩散模型` `混合专家调度` `任务自适应先验` `多任务泛化`

## 📋 核心要点

1. 核心问题：图像修复基础模型中，不同任务数据混合比例直接影响整体性能，需优化以平衡泛化能力
2. 方法要点：采用数据均衡调度范式动态优化混合比例，并引入MoE驱动的调度器分配任务自适应扩散先验
3. 实验或效果：在超过50个子任务中验证，在广泛真实场景下实现一致泛化，性能优于先进方法

## 📄 摘要（原文）

> Recent studies have witnessed significant advances in image restoration foundation models driven by improvements in the scale and quality of pre-training data. In this work, we find that the data mixture proportions from different restoration tasks are also a critical factor directly determining the overall performance of all-in-one image restoration models. To this end, we propose a high-capacity diffusion-based image restoration foundation model, FoundIR-v2, which adopts a data equilibrium scheduling paradigm to dynamically optimize the proportions of mixed training datasets from different tasks. By leveraging the data mixing law, our method ensures a balanced dataset composition, enabling the model to achieve consistent generalization and comprehensive performance across diverse tasks. Furthermore, we introduce an effective Mixture-of-Experts (MoE)-driven scheduler into generative pre-training to flexibly allocate task-adaptive diffusion priors for each restoration task, accounting for the distinct degradation forms and levels exhibited by different tasks. Extensive experiments demonstrate that our method can address over 50 sub-tasks across a broader scope of real-world scenarios and achieves favorable performance against state-of-the-art approaches.


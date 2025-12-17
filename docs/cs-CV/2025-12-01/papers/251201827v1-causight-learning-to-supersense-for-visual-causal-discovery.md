---
layout: default
title: CauSight: Learning to Supersense for Visual Causal Discovery
---

# CauSight: Learning to Supersense for Visual Causal Discovery

**arXiv**: [2512.01827v1](https://arxiv.org/abs/2512.01827) | [PDF](https://arxiv.org/pdf/2512.01827.pdf)

**作者**: Yize Zhang, Meiqi Chen, Sirui Chen, Bo Peng, Yanxi Zhang, Tianyu Li, Chaochao Lu

---

## 💡 一句话要点

**提出CauSight模型以解决视觉因果发现任务，通过因果感知推理提升AI系统理解视觉场景中的因果关系。**

**关键词**: `视觉因果发现` `因果推理` `数据集构建` `强化学习` `视觉语言模型`

## 📋 核心要点

1. 核心问题：视觉因果发现任务要求模型从图像中推断实体间的因果关系，而非仅感知存在。
2. 方法要点：构建VCG-32K数据集，结合Tree-of-Causal-Thought和强化学习训练CauSight模型进行因果推理。
3. 实验或效果：CauSight在视觉因果发现上超越GPT-4.1，性能提升超过三倍（绝对增益21%）。

## 📄 摘要（原文）

> Causal thinking enables humans to understand not just what is seen, but why it happens. To replicate this capability in modern AI systems, we introduce the task of visual causal discovery. It requires models to infer cause-and-effect relations among visual entities across diverse scenarios instead of merely perceiving their presence. To this end, we first construct the Visual Causal Graph dataset (VCG-32K), a large-scale collection of over 32,000 images annotated with entity-level causal graphs, and further develop CauSight, a novel vision-language model to perform visual causal discovery through causally aware reasoning. Our training recipe integrates three components: (1) training data curation from VCG-32K, (2) Tree-of-Causal-Thought (ToCT) for synthesizing reasoning trajectories, and (3) reinforcement learning with a designed causal reward to refine the reasoning policy. Experiments show that CauSight outperforms GPT-4.1 on visual causal discovery, achieving over a threefold performance boost (21% absolute gain). Our code, model, and dataset are fully open-sourced at project page: https://github.com/OpenCausaLab/CauSight.


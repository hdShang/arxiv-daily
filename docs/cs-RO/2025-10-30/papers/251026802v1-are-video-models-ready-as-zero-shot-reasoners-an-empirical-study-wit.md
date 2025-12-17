---
layout: default
title: Are Video Models Ready as Zero-Shot Reasoners? An Empirical Study with the MME-CoF Benchmark
---

# Are Video Models Ready as Zero-Shot Reasoners? An Empirical Study with the MME-CoF Benchmark

**arXiv**: [2510.26802v1](https://arxiv.org/abs/2510.26802) | [PDF](https://arxiv.org/pdf/2510.26802.pdf)

**作者**: Ziyu Guo, Xinyan Chen, Renrui Zhang, Ruichuan An, Yu Qi, Dongzhi Jiang, Xiangtai Li, Manyuan Zhang, Hongsheng Li, Pheng-Ann Heng

---

## 💡 一句话要点

**评估视频模型在零样本推理中的能力，揭示其在MME-CoF基准上的表现**

**关键词**: `视频模型评估` `零样本推理` `MME-CoF基准` `链式帧推理` `视觉推理能力`

## 📋 核心要点

1. 核心问题：视频模型是否可作为零样本推理器处理复杂视觉推理场景
2. 方法要点：使用Veo-3模型，在12个维度上系统评估推理行为
3. 实验或效果：模型在短时空间一致性表现良好，但长时因果推理能力有限

## 📄 摘要（原文）

> Recent video generation models can produce high-fidelity, temporally coherent
> videos, indicating that they may encode substantial world knowledge. Beyond
> realistic synthesis, they also exhibit emerging behaviors indicative of visual
> perception, modeling, and manipulation. Yet, an important question still
> remains: Are video models ready to serve as zero-shot reasoners in challenging
> visual reasoning scenarios? In this work, we conduct an empirical study to
> comprehensively investigate this question, focusing on the leading and popular
> Veo-3. We evaluate its reasoning behavior across 12 dimensions, including
> spatial, geometric, physical, temporal, and embodied logic, systematically
> characterizing both its strengths and failure modes. To standardize this study,
> we curate the evaluation data into MME-CoF, a compact benchmark that enables
> in-depth and thorough assessment of Chain-of-Frame (CoF) reasoning. Our
> findings reveal that while current video models demonstrate promising reasoning
> patterns on short-horizon spatial coherence, fine-grained grounding, and
> locally consistent dynamics, they remain limited in long-horizon causal
> reasoning, strict geometric constraints, and abstract logic. Overall, they are
> not yet reliable as standalone zero-shot reasoners, but exhibit encouraging
> signs as complementary visual engines alongside dedicated reasoning models.
> Project page: https://video-cof.github.io


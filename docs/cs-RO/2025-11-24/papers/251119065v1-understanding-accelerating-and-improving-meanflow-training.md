---
layout: default
title: Understanding, Accelerating, and Improving MeanFlow Training
---

# Understanding, Accelerating, and Improving MeanFlow Training

**arXiv**: [2511.19065v1](https://arxiv.org/abs/2511.19065) | [PDF](https://arxiv.org/pdf/2511.19065.pdf)

**作者**: Jin-Young Kim, Hyojun Go, Lea Bogensperger, Julius Erbach, Nikolai Kalischek, Federico Tombari, Konrad Schindler, Dominik Narnhofer

---

## 💡 一句话要点

**提出改进MeanFlow训练方案以加速收敛并提升少步生成质量**

**关键词**: `生成模型` `速度场学习` `训练加速` `少步生成` `图像合成`

## 📋 核心要点

1. 分析MeanFlow中瞬时与平均速度场交互，揭示学习依赖关系与退化条件
2. 设计训练策略，先加速瞬时速度形成，再转向长间隔平均速度学习
3. 实验显示FID降至2.87，训练时间缩短2.5倍，或使用更小骨干网络

## 📄 摘要（原文）

> MeanFlow promises high-quality generative modeling in few steps, by jointly learning instantaneous and average velocity fields. Yet, the underlying training dynamics remain unclear. We analyze the interaction between the two velocities and find: (i) well-established instantaneous velocity is a prerequisite for learning average velocity; (ii) learning of instantaneous velocity benefits from average velocity when the temporal gap is small, but degrades as the gap increases; and (iii) task-affinity analysis indicates that smooth learning of large-gap average velocities, essential for one-step generation, depends on the prior formation of accurate instantaneous and small-gap average velocities. Guided by these observations, we design an effective training scheme that accelerates the formation of instantaneous velocity, then shifts emphasis from short- to long-interval average velocity. Our enhanced MeanFlow training yields faster convergence and significantly better few-step generation: With the same DiT-XL backbone, our method reaches an impressive FID of 2.87 on 1-NFE ImageNet 256x256, compared to 3.43 for the conventional MeanFlow baseline. Alternatively, our method matches the performance of the MeanFlow baseline with 2.5x shorter training time, or with a smaller DiT-L backbone.


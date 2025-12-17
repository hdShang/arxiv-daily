---
layout: default
title: XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations
---

# XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations

**arXiv**: [2511.02776v1](https://arxiv.org/abs/2511.02776) | [PDF](https://arxiv.org/pdf/2511.02776.pdf)

**作者**: Shichao Fan, Kun Wu, Zhengping Che, Xinhua Wang, Di Wu, Fei Liao, Ning Liu, Yixue Zhang, Zhen Zhao, Zhiyuan Xu, Meng Li, Qingjie Liu, Shanghang Zhang, Min Wan, Jian Tang

---

## 💡 一句话要点

**提出XR-1框架，通过统一视觉-运动表示解决机器人视觉-语言-动作模型中的动作生成与数据异构挑战。**

**关键词**: `视觉-语言-动作模型` `统一视觉-运动表示` `双分支VQ-VAE` `跨机器人学习` `多模态对齐` `机器人操作任务`

## 📋 核心要点

1. 核心问题：现有VLA模型难以从高维观察生成精确低级动作，且跨异构数据源存在领域差距。
2. 方法要点：引入统一视觉-运动代码，通过双分支VQ-VAE联合编码视觉动态与机器人运动。
3. 实验或效果：在六种机器人上验证，优于多个基线，泛化能力强于新对象和背景变化。

## 📄 摘要（原文）

> Recent progress in large-scale robotic datasets and vision-language models
> (VLMs) has advanced research on vision-language-action (VLA) models. However,
> existing VLA models still face two fundamental challenges: (i) producing
> precise low-level actions from high-dimensional observations, (ii) bridging
> domain gaps across heterogeneous data sources, including diverse robot
> embodiments and human demonstrations. Existing methods often encode latent
> variables from either visual dynamics or robotic actions to guide policy
> learning, but they fail to fully exploit the complementary multi-modal
> knowledge present in large-scale, heterogeneous datasets. In this work, we
> present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable
> VLA learning across diverse robots, tasks, and environments. XR-1 introduces
> the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation
> learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and
> robotic motion. UVMC addresses these challenges by (i) serving as an
> intermediate representation between the observations and actions, and (ii)
> aligning multimodal dynamic information from heterogeneous data sources to
> capture complementary knowledge. To effectively exploit UVMC, we propose a
> three-stage training paradigm: (i) self-supervised UVMC learning, (ii)
> UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and
> (iii) task-specific post-training. We validate XR-1 through extensive
> real-world experiments with more than 14,000 rollouts on six different robot
> embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently
> outperforms state-of-the-art baselines such as $\pi_{0.5}$, $\pi_0$, RDT,
> UniVLA, and GR00T-N1.5 while demonstrating strong generalization to novel
> objects, background variations, distractors, and illumination changes. Our
> project is at https://xr-1-vla.github.io/.


---
layout: default
title: PAN: A World Model for General, Interactable, and Long-Horizon World Simulation
---

# PAN: A World Model for General, Interactable, and Long-Horizon World Simulation

**arXiv**: [2511.09057v1](https://arxiv.org/abs/2511.09057) | [PDF](https://arxiv.org/pdf/2511.09057.pdf)

**作者**: PAN Team, Jiannan Xiang, Yi Gu, Zihan Liu, Zeyu Feng, Qiyue Gao, Yiyan Hu, Benhao Huang, Guangyi Liu, Yichi Yang, Kun Zhou, Davit Abrahamyan, Arif Ahmad, Ganesh Bannur, Junrong Chen, Kimi Chen, Mingkai Deng, Ruobing Han, Xinqi Huang, Haoqiang Kang, Zheqi Li, Enze Ma, Hector Ren, Yashowardhan Shinde, Rohan Shingre, Ramsundar Tanikella, Kaiming Tao, Dequan Yang, Xinle Yu, Cong Zeng, Binglin Zhou, Hector Liu, Zhiting Hu, Eric P. Xing

---

## 💡 一句话要点

**提出PAN世界模型，实现基于语言动作的通用、交互式长时程世界模拟**

**关键词**: `世界模型` `视频生成` `语言条件化` `长时程模拟` `潜在空间推理`

## 📋 核心要点

1. 核心问题：现有视频生成模型缺乏因果控制和长时程一致性，世界模型局限于特定领域。
2. 方法要点：结合自回归潜在动态骨干和视频扩散解码器，支持语言条件化动作模拟。
3. 实验或效果：在动作条件模拟和长时程预测中表现优异，优于其他模型。

## 📄 摘要（原文）

> A world model enables an intelligent agent to imagine, predict, and reason about how the world evolves in response to its actions, and accordingly to plan and strategize. While recent video generation models produce realistic visual sequences, they typically operate in the prompt-to-full-video manner without causal control, interactivity, or long-horizon consistency required for purposeful reasoning. Existing world modeling efforts, on the other hand, often focus on restricted domains (e.g., physical, game, or 3D-scene dynamics) with limited depth and controllability, and struggle to generalize across diverse environments and interaction formats. In this work, we introduce PAN, a general, interactable, and long-horizon world model that predicts future world states through high-quality video simulation conditioned on history and natural language actions. PAN employs the Generative Latent Prediction (GLP) architecture that combines an autoregressive latent dynamics backbone based on a large language model (LLM), which grounds simulation in extensive text-based knowledge and enables conditioning on language-specified actions, with a video diffusion decoder that reconstructs perceptually detailed and temporally coherent visual observations, to achieve a unification between latent space reasoning (imagination) and realizable world dynamics (reality). Trained on large-scale video-action pairs spanning diverse domains, PAN supports open-domain, action-conditioned simulation with coherent, long-term dynamics. Extensive experiments show that PAN achieves strong performance in action-conditioned world simulation, long-horizon forecasting, and simulative reasoning compared to other video generators and world models, taking a step towards general world models that enable predictive simulation of future world states for reasoning and acting.


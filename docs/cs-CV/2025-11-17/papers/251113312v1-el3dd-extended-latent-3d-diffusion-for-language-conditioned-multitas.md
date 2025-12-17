---
layout: default
title: EL3DD: Extended Latent 3D Diffusion for Language Conditioned Multitask Manipulation
---

# EL3DD: Extended Latent 3D Diffusion for Language Conditioned Multitask Manipulation

**arXiv**: [2511.13312v1](https://arxiv.org/abs/2511.13312) | [PDF](https://arxiv.org/pdf/2511.13312.pdf)

**作者**: Jonas Bode, Raphael Memmesheimer, Sven Behnke

---

## 💡 一句话要点

**提出扩展潜在3D扩散模型，以语言条件实现多任务机器人操作**

**关键词**: `扩散模型` `机器人操作` `语言条件控制` `多任务学习` `视觉运动策略`

## 📋 核心要点

1. 核心问题：机器人需在人类环境中理解自然语言并执行物理任务
2. 方法要点：融合视觉与文本输入，利用扩散模型生成精确机器人轨迹
3. 实验或效果：在CALVIN数据集上验证，提升多任务操作性能和长时成功率

## 📄 摘要（原文）

> Acting in human environments is a crucial capability for general-purpose robots, necessitating a robust understanding of natural language and its application to physical tasks. This paper seeks to harness the capabilities of diffusion models within a visuomotor policy framework that merges visual and textual inputs to generate precise robotic trajectories. By employing reference demonstrations during training, the model learns to execute manipulation tasks specified through textual commands within the robot's immediate environment. The proposed research aims to extend an existing model by leveraging improved embeddings, and adapting techniques from diffusion models for image generation. We evaluate our methods on the CALVIN dataset, proving enhanced performance on various manipulation tasks and an increased long-horizon success rate when multiple tasks are executed in sequence. Our approach reinforces the usefulness of diffusion models and contributes towards general multitask manipulation.


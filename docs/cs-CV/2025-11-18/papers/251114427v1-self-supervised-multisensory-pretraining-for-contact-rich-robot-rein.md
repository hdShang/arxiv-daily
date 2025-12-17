---
layout: default
title: Self-Supervised Multisensory Pretraining for Contact-Rich Robot Reinforcement Learning
---

# Self-Supervised Multisensory Pretraining for Contact-Rich Robot Reinforcement Learning

**arXiv**: [2511.14427v1](https://arxiv.org/abs/2511.14427) | [PDF](https://arxiv.org/pdf/2511.14427.pdf)

**作者**: Rickmer Krohn, Vignesh Prasad, Gabriele Tiboni, Georgia Chalvatzaki

---

## 💡 一句话要点

**提出多感官动态预训练框架以解决接触丰富机器人强化学习中的多感官融合问题**

**关键词**: `多感官融合` `强化学习` `机器人操作` `掩码自编码` `Transformer` `跨模态预测`

## 📋 核心要点

1. 核心问题：强化学习在接触丰富操作中难以处理多感官噪声和动态变化
2. 方法要点：基于掩码自编码和Transformer，通过重建多感官观测实现跨模态预测
3. 实验或效果：在仿真和真实机器人任务中展示高鲁棒性和快速学习能力

## 📄 摘要（原文）

> Effective contact-rich manipulation requires robots to synergistically leverage vision, force, and proprioception. However, Reinforcement Learning agents struggle to learn in such multisensory settings, especially amidst sensory noise and dynamic changes. We propose MultiSensory Dynamic Pretraining (MSDP), a novel framework for learning expressive multisensory representations tailored for task-oriented policy learning. MSDP is based on masked autoencoding and trains a transformer-based encoder by reconstructing multisensory observations from only a subset of sensor embeddings, leading to cross-modal prediction and sensor fusion. For downstream policy learning, we introduce a novel asymmetric architecture, where a cross-attention mechanism allows the critic to extract dynamic, task-specific features from the frozen embeddings, while the actor receives a stable pooled representation to guide its actions. Our method demonstrates accelerated learning and robust performance under diverse perturbations, including sensor noise, and changes in object dynamics. Evaluations in multiple challenging, contact-rich robot manipulation tasks in simulation and the real world showcase the effectiveness of MSDP. Our approach exhibits strong robustness to perturbations and achieves high success rates on the real robot with as few as 6,000 online interactions, offering a simple yet powerful solution for complex multisensory robotic control.


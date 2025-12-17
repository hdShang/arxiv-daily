---
layout: default
title: Multi-Domain Motion Embedding: Expressive Real-Time Mimicry for Legged Robots
---

# Multi-Domain Motion Embedding: Expressive Real-Time Mimicry for Legged Robots

**arXiv**: [2512.07673v1](https://arxiv.org/abs/2512.07673) | [PDF](https://arxiv.org/pdf/2512.07673.pdf)

**作者**: Matthias Heyrman, Chenhao Li, Victor Klemm, Dongho Kang, Stelian Coros, Marco Hutter

---

## 💡 一句话要点

**提出多域运动嵌入以解决腿式机器人实时模仿中运动表示不足的问题**

**关键词**: `运动表示学习` `实时机器人模仿` `多域嵌入` `小波编码` `概率嵌入` `零样本部署`

## 📋 核心要点

1. 核心问题：现有运动控制器忽略运动固有模式，难以联合捕捉结构化周期模式和非规则变化
2. 方法要点：使用基于小波的编码器和概率嵌入并行统一嵌入结构化和非结构化特征
3. 实验或效果：在类人形和四足机器人上实现无重定向实时模仿，优于先前方法，支持零样本部署

## 📄 摘要（原文）

> Effective motion representation is crucial for enabling robots to imitate expressive behaviors in real time, yet existing motion controllers often ignore inherent patterns in motion. Previous efforts in representation learning do not attempt to jointly capture structured periodic patterns and irregular variations in human and animal movement. To address this, we present Multi-Domain Motion Embedding (MDME), a motion representation that unifies the embedding of structured and unstructured features using a wavelet-based encoder and a probabilistic embedding in parallel. This produces a rich representation of reference motions from a minimal input set, enabling improved generalization across diverse motion styles and morphologies. We evaluate MDME on retargeting-free real-time motion imitation by conditioning robot control policies on the learned embeddings, demonstrating accurate reproduction of complex trajectories on both humanoid and quadruped platforms. Our comparative studies confirm that MDME outperforms prior approaches in reconstruction fidelity and generalizability to unseen motions. Furthermore, we demonstrate that MDME can reproduce novel motion styles in real-time through zero-shot deployment, eliminating the need for task-specific tuning or online retargeting. These results position MDME as a generalizable and structure-aware foundation for scalable real-time robot imitation.


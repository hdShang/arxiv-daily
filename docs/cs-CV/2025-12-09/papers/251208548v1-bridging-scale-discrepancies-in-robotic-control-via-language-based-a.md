---
layout: default
title: Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations
---

# Bridging Scale Discrepancies in Robotic Control via Language-Based Action Representations

**arXiv**: [2512.08548v1](https://arxiv.org/abs/2512.08548) | [PDF](https://arxiv.org/pdf/2512.08548.pdf)

**作者**: Yuchi Zhang, Churui Sun, Shiqi Liang, Diyuan Liu, Chao Ji, Wei-Nan Zhang, Ting Liu

---

## 💡 一句话要点

**提出基于语言的动作表示以解决机器人控制中的尺度差异问题**

**关键词**: `机器人操作` `动作表示` `预训练` `泛化性能` `语言模型`

## 📋 核心要点

1. 核心问题：机器人动作数据因平台和任务差异导致数值尺度变化，阻碍预训练知识迁移。
2. 方法要点：采用语义基础的语言表示，忽略数值尺度，强调方向性，以归一化动作。
3. 实验或效果：在基准测试中，该方法显著提升机器人操作任务的泛化性能和可转移性。

## 📄 摘要（原文）

> Recent end-to-end robotic manipulation research increasingly adopts architectures inspired by large language models to enable robust manipulation. However, a critical challenge arises from severe distribution shifts between robotic action data, primarily due to substantial numerical variations in action commands across diverse robotic platforms and tasks, hindering the effective transfer of pretrained knowledge. To address this limitation, we propose a semantically grounded linguistic representation to normalize actions for efficient pretraining. Unlike conventional discretized action representations that are sensitive to numerical scales, the motion representation specifically disregards numeric scale effects, emphasizing directionality instead. This abstraction mitigates distribution shifts, yielding a more generalizable pretraining representation. Moreover, using the motion representation narrows the feature distance between action tokens and standard vocabulary tokens, mitigating modality gaps. Multi-task experiments on two benchmarks demonstrate that the proposed method significantly improves generalization performance and transferability in robotic manipulation tasks.


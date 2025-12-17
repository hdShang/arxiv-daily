---
layout: default
title: Task-Aware Multi-Expert Architecture For Lifelong Deep Learning
---

# Task-Aware Multi-Expert Architecture For Lifelong Deep Learning

**arXiv**: [2512.11243v1](https://arxiv.org/abs/2512.11243) | [PDF](https://arxiv.org/pdf/2512.11243.pdf)

**作者**: Jianyu Wang, Jacob Nean-Hua Sheikh, Cat P. Le, Hoda Bidkhori

---

## 💡 一句话要点

**提出任务感知多专家架构以解决终身深度学习中的灾难性遗忘问题**

**关键词**: `终身深度学习` `灾难性遗忘` `多专家架构` `任务相似性` `重播缓冲` `注意力机制`

## 📋 核心要点

1. 核心问题：终身深度学习需顺序学习任务同时避免遗忘旧知识
2. 方法要点：基于任务相似性选择专家，结合重播缓冲和注意力机制
3. 实验或效果：在CIFAR-100二分类任务上提升新任务准确率并维持旧任务性能

## 📄 摘要（原文）

> Lifelong deep learning (LDL) trains neural networks to learn sequentially across tasks while preserving prior knowledge. We propose Task-Aware Multi-Expert (TAME), a continual learning algorithm that leverages task similarity to guide expert selection and knowledge transfer. TAME maintains a pool of pretrained neural networks and activates the most relevant expert for each new task. A shared dense layer integrates features from the chosen expert to generate predictions. To reduce catastrophic forgetting, TAME uses a replay buffer that stores representative samples and embeddings from previous tasks and reuses them during training. An attention mechanism further prioritizes the most relevant stored information for each prediction. Together, these components allow TAME to adapt flexibly while retaining important knowledge across evolving task sequences. Experiments on binary classification tasks derived from CIFAR-100 show that TAME improves accuracy on new tasks while sustaining performance on earlier ones, highlighting its effectiveness in balancing adaptation and retention in lifelong learning settings.


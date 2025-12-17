---
layout: default
title: Maglev-Pentabot: Magnetic Levitation System for Non-Contact Manipulation using Deep Reinforcement Learning
---

# Maglev-Pentabot: Magnetic Levitation System for Non-Contact Manipulation using Deep Reinforcement Learning

**arXiv**: [2511.21149v1](https://arxiv.org/abs/2511.21149) | [PDF](https://arxiv.org/pdf/2511.21149.pdf)

**作者**: Guoming Huang, Qingyi Zhou, Dianjing Liu, Shuai Zhang, Ming Zhou, Zongfu Yu

---

## 💡 一句话要点

**提出磁悬浮系统Maglev-Pentabot，使用深度强化学习实现克级物体的非接触操控**

**关键词**: `磁悬浮系统` `深度强化学习` `非接触操控` `动作重映射` `工业机器人`

## 📋 核心要点

1. 核心问题：现有非接触操控技术多限于毫克级微观尺度，难以处理克级物体
2. 方法要点：采用深度强化学习优化控制策略，并引入动作重映射解决磁场非线性问题
3. 实验或效果：系统展示灵活操控能力，可泛化至未训练任务，并支持扩展到工业规模

## 📄 摘要（原文）

> Non-contact manipulation has emerged as a transformative approach across various industrial fields. However, current flexible 2D and 3D non-contact manipulation techniques are often limited to microscopic scales, typically controlling objects in the milligram range. In this paper, we present a magnetic levitation system, termed Maglev-Pentabot, designed to address this limitation. The Maglev-Pentabot leverages deep reinforcement learning (DRL) to develop complex control strategies for manipulating objects in the gram range. Specifically, we propose an electromagnet arrangement optimized through numerical analysis to maximize controllable space. Additionally, an action remapping method is introduced to address sample sparsity issues caused by the strong nonlinearity in magnetic field intensity, hence allowing the DRL controller to converge. Experimental results demonstrate flexible manipulation capabilities, and notably, our system can generalize to transport tasks it has not been explicitly trained for. Furthermore, our approach can be scaled to manipulate heavier objects using larger electromagnets, offering a reference framework for industrial-scale robotic applications.


---
layout: default
title: MACEval: A Multi-Agent Continual Evaluation Network for Large Models
---

# MACEval: A Multi-Agent Continual Evaluation Network for Large Models

**arXiv**: [2511.09139v1](https://arxiv.org/abs/2511.09139) | [PDF](https://arxiv.org/pdf/2511.09139.pdf)

**作者**: Zijian Chen, Yuze Sun, Yuan Tian, Wenjun Zhang, Guangtao Zhai

---

## 💡 一句话要点

**提出MACEval多智能体持续评估网络以动态评估大模型**

**关键词**: `大模型评估` `多智能体系统` `持续评估` `自动评估` `评估基准`

## 📋 核心要点

1. 核心问题：现有大模型评估基准封闭、易过拟合，且维护成本高。
2. 方法要点：采用多智能体网络，通过角色分配和路由实现自动交互评估。
3. 实验或效果：在9个开放任务中验证，实现高效、灵活和可扩展评估。

## 📄 摘要（原文）

> Hundreds of benchmarks dedicated to evaluating large models from multiple perspectives have been presented over the past few years. Albeit substantial efforts, most of them remain closed-ended and are prone to overfitting due to the potential data contamination in the ever-growing training corpus of large models, thereby undermining the credibility of the evaluation. Moreover, the increasing scale and scope of current benchmarks with transient metrics, as well as the heavily human-dependent curation procedure, pose significant challenges for timely maintenance and adaptation to gauge the advancing capabilities of large models. In this paper, we introduce MACEval, a \Multi-Agent Continual Evaluation network for dynamic evaluation of large models, and define a new set of metrics to quantify performance longitudinally and sustainably. MACEval adopts an interactive and autonomous evaluation mode that employs role assignment, in-process data generation, and evaluation routing through a cascaded agent network. Extensive experiments on 9 open-ended tasks with 23 participating large models demonstrate that MACEval is (1) human-free and automatic, mitigating laborious result processing with inter-agent judgment guided; (2) efficient and economical, reducing a considerable amount of data and overhead to obtain similar results compared to related benchmarks; and (3) flexible and scalable, migrating or integrating existing benchmarks via customized evaluation topologies. We hope that MACEval can broaden future directions of large model evaluation.


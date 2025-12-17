---
layout: default
title: OneThinker: All-in-one Reasoning Model for Image and Video
---

# OneThinker: All-in-one Reasoning Model for Image and Video

**arXiv**: [2512.03043v1](https://arxiv.org/abs/2512.03043) | [PDF](https://arxiv.org/pdf/2512.03043.pdf)

**作者**: Kaituo Feng, Manyuan Zhang, Hongyu Li, Kaixuan Fan, Shuang Chen, Yilei Jiang, Dian Zheng, Peiwen Sun, Yiyuan Zhang, Haoze Sun, Yan Feng, Peng Pei, Xunliang Cai, Xiangyu Yue

---

## 💡 一句话要点

**提出OneThinker统一模型，通过EMA-GRPO方法解决多模态视觉任务中的推理泛化问题。**

**关键词**: `多模态大语言模型` `视觉推理统一模型` `多任务强化学习` `图像视频理解` `奖励异质性处理` `零样本泛化`

## 📋 核心要点

1. 现有方法需为不同任务训练独立模型，限制了多模态推理的通用性和知识共享。
2. 构建OneThinker-600k训练语料，采用EMA-GRPO处理多任务强化学习中的奖励异质性。
3. 在31个基准测试中表现强劲，展示任务间知识转移和初步零样本泛化能力。

## 📄 摘要（原文）

> Reinforcement learning (RL) has recently achieved remarkable success in eliciting visual reasoning within Multimodal Large Language Models (MLLMs). However, existing approaches typically train separate models for different tasks and treat image and video reasoning as disjoint domains. This results in limited scalability toward a multimodal reasoning generalist, which restricts practical versatility and hinders potential knowledge sharing across tasks and modalities. To this end, we propose OneThinker, an all-in-one reasoning model that unifies image and video understanding across diverse fundamental visual tasks, including question answering, captioning, spatial and temporal grounding, tracking, and segmentation. To achieve this, we construct the OneThinker-600k training corpus covering all these tasks and employ commercial models for CoT annotation, resulting in OneThinker-SFT-340k for SFT cold start. Furthermore, we propose EMA-GRPO to handle reward heterogeneity in multi-task RL by tracking task-wise moving averages of reward standard deviations for balanced optimization. Extensive experiments on diverse visual benchmarks show that OneThinker delivers strong performance on 31 benchmarks, across 10 fundamental visual understanding tasks. Moreover, it exhibits effective knowledge transfer between certain tasks and preliminary zero-shot generalization ability, marking a step toward a unified multimodal reasoning generalist. All code, model, and data are released.


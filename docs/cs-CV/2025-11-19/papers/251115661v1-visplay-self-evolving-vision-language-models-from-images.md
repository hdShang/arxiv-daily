---
layout: default
title: VisPlay: Self-Evolving Vision-Language Models from Images
---

# VisPlay: Self-Evolving Vision-Language Models from Images

**arXiv**: [2511.15661v1](https://arxiv.org/abs/2511.15661) | [PDF](https://arxiv.org/pdf/2511.15661.pdf)

**作者**: Yicheng He, Chengsong Huang, Zongxia Li, Jiaxin Huang, Yonghui Yang

---

## 💡 一句话要点

**提出VisPlay框架，使视觉语言模型利用未标注图像自主提升推理能力**

**关键词**: `视觉语言模型` `强化学习` `自进化框架` `未标注数据` `多模态推理` `幻觉减少`

## 📋 核心要点

1. 现有强化学习方法依赖人工标注或启发式奖励，成本高且难以扩展
2. VisPlay将模型分为图像条件提问者和多模态推理者，通过GRPO联合训练
3. 在多个基准测试中实现视觉推理、组合泛化和幻觉减少的改进

## 📄 摘要（原文）

> Reinforcement learning (RL) provides a principled framework for improving Vision-Language Models (VLMs) on complex reasoning tasks. However, existing RL approaches often rely on human-annotated labels or task-specific heuristics to define verifiable rewards, both of which are costly and difficult to scale. We introduce VisPlay, a self-evolving RL framework that enables VLMs to autonomously improve their reasoning abilities using large amounts of unlabeled image data. Starting from a single base VLM, VisPlay assigns the model into two interacting roles: an Image-Conditioned Questioner that formulates challenging yet answerable visual questions, and a Multimodal Reasoner that generates silver responses. These roles are jointly trained with Group Relative Policy Optimization (GRPO), which incorporates diversity and difficulty rewards to balance the complexity of generated questions with the quality of the silver answers. VisPlay scales efficiently across two model families. When trained on Qwen2.5-VL and MiMo-VL, VisPlay achieves consistent improvements in visual reasoning, compositional generalization, and hallucination reduction across eight benchmarks, including MM-Vet and MMMU, demonstrating a scalable path toward self-evolving multimodal intelligence. The project page is available at https://bruno686.github.io/VisPlay/


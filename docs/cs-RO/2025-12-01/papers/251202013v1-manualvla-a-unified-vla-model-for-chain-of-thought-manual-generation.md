---
layout: default
title: ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation
---

# ManualVLA: A Unified VLA Model for Chain-of-Thought Manual Generation and Robotic Manipulation

**arXiv**: [2512.02013v1](https://arxiv.org/abs/2512.02013) | [PDF](https://arxiv.org/pdf/2512.02013.pdf)

**作者**: Chenyang Gu, Jiaming Liu, Hao Chen, Runzhong Huang, Qingpo Wuwu, Zhuoyang Liu, Xiaoqi Li, Ying Li, Renrui Zhang, Peng Jia, Pheng-Ann Heng, Shanghang Zhang

---

## 💡 一句话要点

**提出ManualVLA统一框架，通过生成多模态手册解决长时程机器人任务规划与执行问题。**

**关键词**: `视觉-语言-动作模型` `长时程任务规划` `多模态手册生成` `机器人操作` `3D高斯溅射` `数字孪生工具`

## 📋 核心要点

1. 核心问题：现有VLA模型在长时程任务中难以协调高层规划与精确操作。
2. 方法要点：基于Mixture-of-Transformers架构，集成规划专家生成多模态手册，并通过ManualCoT推理指导动作执行。
3. 实验或效果：在LEGO组装和物体重排任务中，平均成功率比基线高32%。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have recently emerged, demonstrating strong generalization in robotic scene understanding and manipulation. However, when confronted with long-horizon tasks that require defined goal states, such as LEGO assembly or object rearrangement, existing VLA models still face challenges in coordinating high-level planning with precise manipulation. Therefore, we aim to endow a VLA model with the capability to infer the "how" process from the "what" outcomes, transforming goal states into executable procedures. In this paper, we introduce ManualVLA, a unified VLA framework built upon a Mixture-of-Transformers (MoT) architecture, enabling coherent collaboration between multimodal manual generation and action execution. Unlike prior VLA models that directly map sensory inputs to actions, we first equip ManualVLA with a planning expert that generates intermediate manuals consisting of images, position prompts, and textual instructions. Building upon these multimodal manuals, we design a Manual Chain-of-Thought (ManualCoT) reasoning process that feeds them into the action expert, where each manual step provides explicit control conditions, while its latent representation offers implicit guidance for accurate manipulation. To alleviate the burden of data collection, we develop a high-fidelity digital-twin toolkit based on 3D Gaussian Splatting, which automatically generates manual data for planning expert training. ManualVLA demonstrates strong real-world performance, achieving an average success rate 32% higher than the previous hierarchical SOTA baseline on LEGO assembly and object rearrangement tasks.


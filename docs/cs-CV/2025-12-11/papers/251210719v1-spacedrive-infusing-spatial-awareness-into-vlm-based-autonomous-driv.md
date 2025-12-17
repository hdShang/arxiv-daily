---
layout: default
title: SpaceDrive: Infusing Spatial Awareness into VLM-based Autonomous Driving
---

# SpaceDrive: Infusing Spatial Awareness into VLM-based Autonomous Driving

**arXiv**: [2512.10719v1](https://arxiv.org/abs/2512.10719) | [PDF](https://arxiv.org/pdf/2512.10719.pdf)

**作者**: Peizheng Li, Zhenghao Zhang, David Holtz, Hang Yu, Yutong Yang, Yuzhi Lai, Rui Song, Andreas Geiger, Andreas Zell

---

## 💡 一句话要点

**提出SpaceDrive框架，通过空间位置编码增强VLM在自动驾驶中的3D空间理解能力。**

**关键词**: `自动驾驶` `视觉语言模型` `空间位置编码` `3D空间理解` `轨迹规划`

## 📋 核心要点

1. 当前VLM在自动驾驶中难以理解细粒度3D空间关系，影响物理世界交互。
2. SpaceDrive将空间信息作为显式位置编码，结合语义与空间表示进行联合推理。
3. 在nuScenes数据集上实现最优开环性能，Bench2Drive闭环基准得分78.02。

## 📄 摘要（原文）

> End-to-end autonomous driving methods built on vision language models (VLMs) have undergone rapid development driven by their universal visual understanding and strong reasoning capabilities obtained from the large-scale pretraining. However, we find that current VLMs struggle to understand fine-grained 3D spatial relationships which is a fundamental requirement for systems interacting with the physical world. To address this issue, we propose SpaceDrive, a spatial-aware VLM-based driving framework that treats spatial information as explicit positional encodings (PEs) instead of textual digit tokens, enabling joint reasoning over semantic and spatial representations. SpaceDrive employs a universal positional encoder to all 3D coordinates derived from multi-view depth estimation, historical ego-states, and text prompts. These 3D PEs are first superimposed to augment the corresponding 2D visual tokens. Meanwhile, they serve as a task-agnostic coordinate representation, replacing the digit-wise numerical tokens as both inputs and outputs for the VLM. This mechanism enables the model to better index specific visual semantics in spatial reasoning and directly regress trajectory coordinates rather than generating digit-by-digit, thereby enhancing planning accuracy. Extensive experiments validate that SpaceDrive achieves state-of-the-art open-loop performance on the nuScenes dataset and the second-best Driving Score of 78.02 on the Bench2Drive closed-loop benchmark over existing VLM-based methods.


---
layout: default
title: EditThinker: Unlocking Iterative Reasoning for Any Image Editor
---

# EditThinker: Unlocking Iterative Reasoning for Any Image Editor

**arXiv**: [2512.05965v1](https://arxiv.org/abs/2512.05965) | [PDF](https://arxiv.org/pdf/2512.05965.pdf)

**作者**: Hongyu Li, Manyuan Zhang, Dian Zheng, Ziyu Guo, Yimeng Jia, Kaituo Feng, Hao Yu, Yexin Liu, Yan Feng, Peng Pei, Xunliang Cai, Linjiang Huang, Hongsheng Li, Si Liu

---

## 💡 一句话要点

**提出EditThinker框架，通过迭代推理提升任意图像编辑模型的指令遵循能力。**

**关键词**: `指令图像编辑` `迭代推理` `多模态大语言模型` `强化学习对齐` `批判-精炼循环`

## 📋 核心要点

1. 核心问题：基于指令的图像编辑中，单次编辑成功率受随机性和缺乏深思限制。
2. 方法要点：训练多模态大语言模型EditThinker，执行Think-while-Edit循环，联合生成批判、推理和精炼指令。
3. 实验或效果：在四个基准测试中显著提升指令遵循能力，并计划开源数据、框架和模型。

## 📄 摘要（原文）

> Instruction-based image editing has emerged as a prominent research area, which, benefiting from image generation foundation models, have achieved high aesthetic quality, making instruction-following capability the primary challenge. Existing approaches improve instruction adherence via supervised or reinforcement learning, yet single-turn success rates remain limited due to inherent stochasticity and a lack of deliberation. In this work, we propose a deliberative editing framework to 'think' while they edit, which simulates the human cognitive loop by iteratively executing a Think-while-Edit cycle: Critiquing results and Refining instructions , followed by Repeating the generation until satisfactory. Specifically, we train a single MLLM, EditThinker, to act as the reasoning engine of this framework, which jointly produce the critique score, reasoning process, and refined instructions. We employ reinforcement learning to align the EditThinker's thinking with its editing, thereby generating more targeted instruction improvements. Extensive experiments on four benchmarks demonstrate that our approach significantly improves the instruction-following capability of any image editing model by a large margin. We will release our data construction framework, datasets, and models to benefit the community.


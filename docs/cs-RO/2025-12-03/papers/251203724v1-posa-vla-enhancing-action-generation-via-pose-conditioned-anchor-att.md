---
layout: default
title: PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention
---

# PosA-VLA: Enhancing Action Generation via Pose-Conditioned Anchor Attention

**arXiv**: [2512.03724v1](https://arxiv.org/abs/2512.03724) | [PDF](https://arxiv.org/pdf/2512.03724.pdf)

**作者**: Ziwen Li, Xin Wang, Hanlue Zhang, Runnan Chen, Runqi Lin, Xiao He, Han Huang, Yandong Guo, Fakhri Karray, Tongliang Liu, Mingming Gong

---

## 💡 一句话要点

**提出PosA-VLA框架，通过姿态条件锚定注意力增强动作生成，解决VLA模型在复杂环境中动作冗余问题。**

**关键词**: `视觉-语言-动作模型` `姿态条件注意力` `机器人操作` `动作生成` `轻量架构` `泛化能力`

## 📋 核心要点

1. 核心问题：现有VLA模型因空间均匀感知场，在复杂环境中易受目标无关对象干扰，导致动作冗余和不稳定。
2. 方法要点：引入姿态条件锚定注意力机制，引导模型聚焦任务相关区域，无需辅助感知模块，实现轻量高效推理。
3. 实验或效果：在多样化机器人操作基准测试中验证，方法能生成精确、高效动作，并在挑战性环境中展现鲁棒泛化能力。

## 📄 摘要（原文）

> The Vision-Language-Action (VLA) models have demonstrated remarkable performance on embodied tasks and shown promising potential for real-world applications. However, current VLAs still struggle to produce consistent and precise target-oriented actions, as they often generate redundant or unstable motions along trajectories, limiting their applicability in time-sensitive scenarios.In this work, we attribute these redundant actions to the spatially uniform perception field of existing VLAs, which causes them to be distracted by target-irrelevant objects, especially in complex environments.To address this issue, we propose an efficient PosA-VLA framework that anchors visual attention via pose-conditioned supervision, consistently guiding the model's perception toward task-relevant regions. The pose-conditioned anchor attention mechanism enables the model to better align instruction semantics with actionable visual cues, thereby improving action generation precision and efficiency. Moreover, our framework adopts a lightweight architecture and requires no auxiliary perception modules (e.g., segmentation or grounding networks), ensuring efficient inference. Extensive experiments verify that our method executes embodied tasks with precise and time-efficient behavior across diverse robotic manipulation benchmarks and shows robust generalization in a variety of challenging environments.


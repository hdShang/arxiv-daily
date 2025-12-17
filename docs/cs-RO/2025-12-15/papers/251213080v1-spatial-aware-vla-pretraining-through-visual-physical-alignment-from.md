---
layout: default
title: Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos
---

# Spatial-Aware VLA Pretraining through Visual-Physical Alignment from Human Videos

**arXiv**: [2512.13080v1](https://arxiv.org/abs/2512.13080) | [PDF](https://arxiv.org/pdf/2512.13080.pdf)

**作者**: Yicheng Feng, Wanpeng Zhang, Ye Wang, Hao Luo, Haoqi Yuan, Sipeng Zheng, Zongqing Lu

---

## 💡 一句话要点

**提出空间感知VLA预训练范式，通过人类视频的视觉-物理对齐解决2D视觉与3D动作的鸿沟。**

**关键词**: `视觉-语言-动作模型` `空间感知预训练` `3D视觉编码` `机器人学习` `人类视频数据`

## 📋 核心要点

1. 核心问题：现有VLA模型依赖2D视觉输入在3D环境中执行动作，导致感知与动作基础之间存在显著差距。
2. 方法要点：利用大规模人类演示视频提取3D视觉和动作标注，通过双编码器架构VIPA-VLA增强3D空间理解。
3. 实验或效果：在下游机器人任务中，VIPA-VLA显著提升2D视觉与3D动作的基础性，实现更鲁棒和可泛化的策略。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models provide a promising paradigm for robot learning by integrating visual perception with language-guided policy learning. However, most existing approaches rely on 2D visual inputs to perform actions in 3D physical environments, creating a significant gap between perception and action grounding. To bridge this gap, we propose a Spatial-Aware VLA Pretraining paradigm that performs explicit alignment between visual space and physical space during pretraining, enabling models to acquire 3D spatial understanding before robot policy learning. Starting from pretrained vision-language models, we leverage large-scale human demonstration videos to extract 3D visual and 3D action annotations, forming a new source of supervision that aligns 2D visual observations with 3D spatial reasoning. We instantiate this paradigm with VIPA-VLA, a dual-encoder architecture that incorporates a 3D visual encoder to augment semantic visual representations with 3D-aware features. When adapted to downstream robot tasks, VIPA-VLA achieves significantly improved grounding between 2D vision and 3D action, resulting in more robust and generalizable robotic policies.


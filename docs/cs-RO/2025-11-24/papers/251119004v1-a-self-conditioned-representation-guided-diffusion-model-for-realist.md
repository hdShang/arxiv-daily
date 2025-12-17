---
layout: default
title: A Self-Conditioned Representation Guided Diffusion Model for Realistic Text-to-LiDAR Scene Generation
---

# A Self-Conditioned Representation Guided Diffusion Model for Realistic Text-to-LiDAR Scene Generation

**arXiv**: [2511.19004v1](https://arxiv.org/abs/2511.19004) | [PDF](https://arxiv.org/pdf/2511.19004.pdf)

**作者**: Wentao Qu, Guofeng Mei, Yang Wu, Yongshun Gong, Xiaoshui Huang, Liang Xiao

---

## 💡 一句话要点

**提出自条件表示引导扩散模型，用于文本到LiDAR场景生成，提升细节与可控性。**

**关键词**: `文本到LiDAR生成` `扩散模型` `自条件表示引导` `场景生成` `可控性评估` `多条件任务`

## 📋 核心要点

1. 文本-LiDAR数据稀缺导致生成场景过于平滑，低质量文本描述影响生成质量。
2. 引入自条件表示引导，在训练中对去噪网络提供软监督，推理时解耦以感知几何结构。
3. 构建T2nuScenes基准，实验显示模型在无条件与条件生成中优于现有方法。

## 📄 摘要（原文）

> Text-to-LiDAR generation can customize 3D data with rich structures and diverse scenes for downstream tasks. However, the scarcity of Text-LiDAR pairs often causes insufficient training priors, generating overly smooth 3D scenes. Moreover, low-quality text descriptions may degrade generation quality and controllability. In this paper, we propose a Text-to-LiDAR Diffusion Model for scene generation, named T2LDM, with a Self-Conditioned Representation Guidance (SCRG). Specifically, SCRG, by aligning to the real representations, provides the soft supervision with reconstruction details for the Denoising Network (DN) in training, while decoupled in inference. In this way, T2LDM can perceive rich geometric structures from data distribution, generating detailed objects in scenes. Meanwhile, we construct a content-composable Text-LiDAR benchmark, T2nuScenes, along with a controllability metric. Based on this, we analyze the effects of different text prompts for LiDAR generation quality and controllability, providing practical prompt paradigms and insights. Furthermore, a directional position prior is designed to mitigate street distortion, further improving scene fidelity. Additionally, by learning a conditional encoder via frozen DN, T2LDM can support multiple conditional tasks, including Sparse-to-Dense, Dense-to-Sparse, and Semantic-to-LiDAR generation. Extensive experiments in unconditional and conditional generation demonstrate that T2LDM outperforms existing methods, achieving state-of-the-art scene generation.


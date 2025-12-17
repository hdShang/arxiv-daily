---
layout: default
title: LAMP: Language-Assisted Motion Planning for Controllable Video Generation
---

# LAMP: Language-Assisted Motion Planning for Controllable Video Generation

**arXiv**: [2512.03619v1](https://arxiv.org/abs/2512.03619) | [PDF](https://arxiv.org/pdf/2512.03619.pdf)

**作者**: Muhammed Burak Kizil, Enes Sanli, Niloy J. Mitra, Erkut Erdem, Aykut Erdem, Duygu Ceylan

---

## 💡 一句话要点

**提出LAMP框架，利用大语言模型将自然语言转换为3D轨迹以增强视频生成的运动可控性。**

**关键词**: `视频生成` `运动规划` `大语言模型` `程序合成` `3D轨迹` `可控性`

## 📋 核心要点

1. 核心问题：视频生成中运动控制（对象动态和相机轨迹）的接口有限，难以从自然语言直接生成复杂场景。
2. 方法要点：定义运动领域特定语言，利用大语言模型程序合成能力，将自然语言描述映射为结构化运动程序和3D轨迹。
3. 实验或效果：构建大规模程序化数据集，实验显示LAMP在运动可控性和用户意图对齐方面优于现有方法。

## 📄 摘要（原文）

> Video generation has achieved remarkable progress in visual fidelity and controllability, enabling conditioning on text, layout, or motion. Among these, motion control - specifying object dynamics and camera trajectories - is essential for composing complex, cinematic scenes, yet existing interfaces remain limited. We introduce LAMP that leverages large language models (LLMs) as motion planners to translate natural language descriptions into explicit 3D trajectories for dynamic objects and (relatively defined) cameras. LAMP defines a motion domain-specific language (DSL), inspired by cinematography conventions. By harnessing program synthesis capabilities of LLMs, LAMP generates structured motion programs from natural language, which are deterministically mapped to 3D trajectories. We construct a large-scale procedural dataset pairing natural text descriptions with corresponding motion programs and 3D trajectories. Experiments demonstrate LAMP's improved performance in motion controllability and alignment with user intent compared to state-of-the-art alternatives establishing the first framework for generating both object and camera motions directly from natural language specifications.


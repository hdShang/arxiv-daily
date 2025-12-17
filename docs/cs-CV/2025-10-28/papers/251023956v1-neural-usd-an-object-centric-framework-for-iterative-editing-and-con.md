---
layout: default
title: Neural USD: An object-centric framework for iterative editing and control
---

# Neural USD: An object-centric framework for iterative editing and control

**arXiv**: [2510.23956v1](https://arxiv.org/abs/2510.23956) | [PDF](https://arxiv.org/pdf/2510.23956.pdf)

**作者**: Alejandro Escontrela, Shrinu Kushagra, Sjoerd van Steenkiste, Yulia Rubanova, Aleksander Holynski, Kelsey Allen, Kevin Murphy, Thomas Kipf

---

## 💡 一句话要点

**提出Neural USD框架以解决生成模型中精确迭代对象编辑的挑战**

**关键词**: `可控生成模型` `对象编辑` `分层表示` `解耦控制` `迭代工作流程`

## 📋 核心要点

1. 核心问题：当前可控生成模型在对象编辑时易导致场景全局意外变化
2. 方法要点：采用分层结构化表示场景和对象，支持外观、几何和姿态的独立控制
3. 实验或效果：评估设计选项，展示框架支持迭代增量工作流程

## 📄 摘要（原文）

> Amazing progress has been made in controllable generative modeling,
> especially over the last few years. However, some challenges remain. One of
> them is precise and iterative object editing. In many of the current methods,
> trying to edit the generated image (for example, changing the color of a
> particular object in the scene or changing the background while keeping other
> elements unchanged) by changing the conditioning signals often leads to
> unintended global changes in the scene. In this work, we take the first steps
> to address the above challenges. Taking inspiration from the Universal Scene
> Descriptor (USD) standard developed in the computer graphics community, we
> introduce the "Neural Universal Scene Descriptor" or Neural USD. In this
> framework, we represent scenes and objects in a structured, hierarchical
> manner. This accommodates diverse signals, minimizes model-specific
> constraints, and enables per-object control over appearance, geometry, and
> pose. We further apply a fine-tuning approach which ensures that the above
> control signals are disentangled from one another. We evaluate several design
> considerations for our framework, demonstrating how Neural USD enables
> iterative and incremental workflows. More information at:
> https://escontrela.me/neural_usd .


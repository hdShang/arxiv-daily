---
layout: default
title: Uni-Inter: Unifying 3D Human Motion Synthesis Across Diverse Interaction Contexts
---

# Uni-Inter: Unifying 3D Human Motion Synthesis Across Diverse Interaction Contexts

**arXiv**: [2511.13032v1](https://arxiv.org/abs/2511.13032) | [PDF](https://arxiv.org/pdf/2511.13032.pdf)

**作者**: Sheng Liu, Yuanzhi Liang, Jiepeng Wang, Sidan Du, Chi Zhang, Xuelong Li

---

## 💡 一句话要点

**提出Uni-Inter统一框架，支持人-人、人-物、人-场景交互的3D人体运动合成。**

**关键词**: `3D人体运动合成` `统一交互建模` `体积表示` `关系推理` `复合交互` `任务无关架构`

## 📋 核心要点

1. 现有方法依赖任务特定设计，泛化能力有限，无法统一处理多种交互场景。
2. 引入统一交互体积（UIV）表示，编码异质实体到共享空间，实现关系推理和复合交互建模。
3. 在三种交互任务实验中，模型性能竞争性强，并能泛化到新实体组合。

## 📄 摘要（原文）

> We present Uni-Inter, a unified framework for human motion generation that supports a wide range of interaction scenarios: including human-human, human-object, and human-scene-within a single, task-agnostic architecture. In contrast to existing methods that rely on task-specific designs and exhibit limited generalization, Uni-Inter introduces the Unified Interactive Volume (UIV), a volumetric representation that encodes heterogeneous interactive entities into a shared spatial field. This enables consistent relational reasoning and compound interaction modeling. Motion generation is formulated as joint-wise probabilistic prediction over the UIV, allowing the model to capture fine-grained spatial dependencies and produce coherent, context-aware behaviors. Experiments across three representative interaction tasks demonstrate that Uni-Inter achieves competitive performance and generalizes well to novel combinations of entities. These results suggest that unified modeling of compound interactions offers a promising direction for scalable motion synthesis in complex environments.


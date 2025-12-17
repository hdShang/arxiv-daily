---
layout: default
title: Topology-Agnostic Animal Motion Generation from Text Prompt
---

# Topology-Agnostic Animal Motion Generation from Text Prompt

**arXiv**: [2512.10352v1](https://arxiv.org/abs/2512.10352) | [PDF](https://arxiv.org/pdf/2512.10352.pdf)

**作者**: Keyi Chen, Mingze Sun, Zhenyu Liu, Zhangquan Chen, Ruqi Huang

---

## 💡 一句话要点

**提出OmniZoo数据集与拓扑无关运动生成框架，以解决动物运动生成中骨架拓扑固定和缺乏统一模型的问题。**

**关键词**: `动物运动生成` `拓扑无关建模` `文本驱动动画` `骨架嵌入` `跨物种迁移`

## 📋 核心要点

1. 核心问题：现有方法依赖固定骨架模板，无法泛化到不同或扰动拓扑，且缺乏大规模异构动物运动数据和统一生成框架。
2. 方法要点：引入OmniZoo大规模动物运动数据集，并提出基于拓扑感知骨架嵌入模块的自回归生成框架，融合文本语义生成任意骨架的运动。
3. 实验或效果：模型能生成时间连贯、物理合理、语义对齐的运动，并支持跨物种运动风格迁移，具体性能指标未知。

## 📄 摘要（原文）

> Motion generation is fundamental to computer animation and widely used across entertainment, robotics, and virtual environments. While recent methods achieve impressive results, most rely on fixed skeletal templates, which prevent them from generalizing to skeletons with different or perturbed topologies. We address the core limitation of current motion generation methods - the combined lack of large-scale heterogeneous animal motion data and unified generative frameworks capable of jointly modeling arbitrary skeletal topologies and textual conditions. To this end, we introduce OmniZoo, a large-scale animal motion dataset spanning 140 species and 32,979 sequences, enriched with multimodal annotations. Building on OmniZoo, we propose a generalized autoregressive motion generation framework capable of producing text-driven motions for arbitrary skeletal topologies. Central to our model is a Topology-aware Skeleton Embedding Module that encodes geometric and structural properties of any skeleton into a shared token space, enabling seamless fusion with textual semantics. Given a text prompt and a target skeleton, our method generates temporally coherent, physically plausible, and semantically aligned motions, and further enables cross-species motion style transfer.


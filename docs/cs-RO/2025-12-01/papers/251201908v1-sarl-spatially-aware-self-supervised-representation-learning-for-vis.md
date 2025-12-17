---
layout: default
title: SARL: Spatially-Aware Self-Supervised Representation Learning for Visuo-Tactile Perception
---

# SARL: Spatially-Aware Self-Supervised Representation Learning for Visuo-Tactile Perception

**arXiv**: [2512.01908v1](https://arxiv.org/abs/2512.01908) | [PDF](https://arxiv.org/pdf/2512.01908.pdf)

**作者**: Gurmeher Khurana, Lan Wei, Dandan Zhang

---

## 💡 一句话要点

**提出SARL框架，通过空间感知自监督学习提升融合视觉-触觉感知能力**

**关键词**: `自监督学习` `视觉-触觉感知` `空间感知表示` `机器人操作` `特征图对齐` `几何一致性`

## 📋 核心要点

1. 核心问题：现有自监督学习框架压缩特征图为全局向量，丢弃空间结构，不适用于需要局部几何信息的机器人操作任务。
2. 方法要点：基于BYOL架构，引入三个地图级目标（SAL、PPDA、RAM），保持跨视图的注意力焦点、部件组合和几何关系一致性。
3. 实验效果：在六个下游任务中优于九个基线，在几何敏感的边缘姿态回归任务上MAE为0.3955，相对提升30%，接近监督上限。

## 📄 摘要（原文）

> Contact-rich robotic manipulation requires representations that encode local geometry. Vision provides global context but lacks direct measurements of properties such as texture and hardness, whereas touch supplies these cues. Modern visuo-tactile sensors capture both modalities in a single fused image, yielding intrinsically aligned inputs that are well suited to manipulation tasks requiring visual and tactile information. Most self-supervised learning (SSL) frameworks, however, compress feature maps into a global vector, discarding spatial structure and misaligning with the needs of manipulation. To address this, we propose SARL, a spatially-aware SSL framework that augments the Bootstrap Your Own Latent (BYOL) architecture with three map-level objectives, including Saliency Alignment (SAL), Patch-Prototype Distribution Alignment (PPDA), and Region Affinity Matching (RAM), to keep attentional focus, part composition, and geometric relations consistent across views. These losses act on intermediate feature maps, complementing the global objective. SARL consistently outperforms nine SSL baselines across six downstream tasks with fused visual-tactile data. On the geometry-sensitive edge-pose regression task, SARL achieves a Mean Absolute Error (MAE) of 0.3955, a 30% relative improvement over the next-best SSL method (0.5682 MAE) and approaching the supervised upper bound. These findings indicate that, for fused visual-tactile data, the most effective signal is structured spatial equivariance, in which features vary predictably with object geometry, which enables more capable robotic perception.


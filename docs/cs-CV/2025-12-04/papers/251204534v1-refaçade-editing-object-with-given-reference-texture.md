---
layout: default
title: Refaçade: Editing Object with Given Reference Texture
---

# Refaçade: Editing Object with Given Reference Texture

**arXiv**: [2512.04534v1](https://arxiv.org/abs/2512.04534) | [PDF](https://arxiv.org/pdf/2512.04534.pdf)

**作者**: Youze Huang, Penghui Ruan, Bojia Zi, Xianbiao Qi, Jianan Wang, Rong Xiao

---

## 💡 一句话要点

**提出Refaçade方法，通过纹理移除和拼图置换实现图像和视频中对象的精确纹理编辑。**

**关键词**: `对象重纹理` `扩散模型` `纹理移除` `拼图置换` `视频编辑` `可控编辑`

## 📋 核心要点

1. 核心问题：现有方法在对象重纹理任务中因参考图像结构干扰和纹理-结构解耦不足导致可控性受限。
2. 方法要点：使用纹理移除器保留源几何和运动，结合拼图置换破坏参考全局布局以聚焦局部纹理统计。
3. 实验或效果：在定量和人工评估中优于基线，展示出优越的视觉质量、精确编辑和可控性。

## 📄 摘要（原文）

> Recent advances in diffusion models have brought remarkable progress in image and video editing, yet some tasks remain underexplored. In this paper, we introduce a new task, Object Retexture, which transfers local textures from a reference object to a target object in images or videos. To perform this task, a straightforward solution is to use ControlNet conditioned on the source structure and the reference texture. However, this approach suffers from limited controllability for two reasons: conditioning on the raw reference image introduces unwanted structural information, and it fails to disentangle the visual texture and structure information of the source. To address this problem, we propose Refaçade, a method that consists of two key designs to achieve precise and controllable texture transfer in both images and videos. First, we employ a texture remover trained on paired textured/untextured 3D mesh renderings to remove appearance information while preserving the geometry and motion of source videos. Second, we disrupt the reference global layout using a jigsaw permutation, encouraging the model to focus on local texture statistics rather than the global layout of the object. Extensive experiments demonstrate superior visual quality, precise editing, and controllability, outperforming strong baselines in both quantitative and human evaluations. Code is available at https://github.com/fishZe233/Refacade.


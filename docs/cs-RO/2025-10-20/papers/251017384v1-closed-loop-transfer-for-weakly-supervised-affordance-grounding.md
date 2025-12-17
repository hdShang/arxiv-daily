---
layout: default
title: Closed-Loop Transfer for Weakly-supervised Affordance Grounding
---

# Closed-Loop Transfer for Weakly-supervised Affordance Grounding

**arXiv**: [2510.17384v1](https://arxiv.org/abs/2510.17384) | [PDF](https://arxiv.org/pdf/2510.17384.pdf)

**作者**: Jiajin Tang, Zhengxuan Wei, Ge Zheng, Sibei Yang

---

## 💡 一句话要点

**提出LoopTrans闭环框架以解决弱监督可承受性接地在复杂交互场景中的局限性**

**关键词**: `弱监督学习` `可承受性接地` `闭环知识转移` `跨模态定位` `知识蒸馏` `遮挡处理`

## 📋 核心要点

1. 核心问题：现有方法仅从外中心图像单向转移知识，限制在复杂交互场景的应用。
2. 方法要点：引入闭环框架，双向转移知识，并采用统一跨模态定位和去噪知识蒸馏机制。
3. 实验效果：在图像和视频基准上实现指标一致提升，处理完全遮挡场景。

## 📄 摘要（原文）

> Humans can perform previously unexperienced interactions with novel objects
> simply by observing others engage with them. Weakly-supervised affordance
> grounding mimics this process by learning to locate object regions that enable
> actions on egocentric images, using exocentric interaction images with
> image-level annotations. However, extracting affordance knowledge solely from
> exocentric images and transferring it one-way to egocentric images limits the
> applicability of previous works in complex interaction scenarios. Instead, this
> study introduces LoopTrans, a novel closed-loop framework that not only
> transfers knowledge from exocentric to egocentric but also transfers back to
> enhance exocentric knowledge extraction. Within LoopTrans, several innovative
> mechanisms are introduced, including unified cross-modal localization and
> denoising knowledge distillation, to bridge domain gaps between object-centered
> egocentric and interaction-centered exocentric images while enhancing knowledge
> transfer. Experiments show that LoopTrans achieves consistent improvements
> across all metrics on image and video benchmarks, even handling challenging
> scenarios where object interaction regions are fully occluded by the human
> body.


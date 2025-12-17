---
layout: default
title: Memory-Guided Point Cloud Completion for Dental Reconstruction
---

# Memory-Guided Point Cloud Completion for Dental Reconstruction

**arXiv**: [2512.03598v1](https://arxiv.org/abs/2512.03598) | [PDF](https://arxiv.org/pdf/2512.03598.pdf)

**作者**: Jianan Sun, Yukang Huang, Dongzhihan Wang, Mingyu Fan

---

## 💡 一句话要点

**提出基于原型记忆的点云补全框架，以解决牙齿重建中因遮挡和扫描限制导致的缺失区域问题。**

**关键词**: `点云补全` `牙齿重建` `原型记忆` `编码器-解码器` `置信度门控` `结构先验`

## 📋 核心要点

1. 核心问题：部分牙齿点云存在大范围缺失，导致全局特征偏差和解码器结构幻觉。
2. 方法要点：在编码器-解码器流程中集成可学习原型记忆，通过置信度门控加权融合检索特征以提供结构先验。
3. 实验或效果：在自建Teeth3DS基准上，Chamfer距离改善，可视化显示更锐利的牙尖、脊和邻接过渡。

## 📄 摘要（原文）

> Partial dental point clouds often suffer from large missing regions caused by occlusion and limited scanning views, which bias encoder-only global features and force decoders to hallucinate structures. We propose a retrieval-augmented framework for tooth completion that integrates a prototype memory into standard encoder--decoder pipelines. After encoding a partial input into a global descriptor, the model retrieves the nearest manifold prototype from a learnable memory and fuses it with the query feature through confidence-gated weighting before decoding. The memory is optimized end-to-end and self-organizes into reusable tooth-shape prototypes without requiring tooth-position labels, thereby providing structural priors that stabilize missing-region inference and free decoder capacity for detail recovery. The module is plug-and-play and compatible with common completion backbones, while keeping the same training losses. Experiments on a self-processed Teeth3DS benchmark demonstrate consistent improvements in Chamfer Distance, with visualizations showing sharper cusps, ridges, and interproximal transitions. Our approach provides a simple yet effective way to exploit cross-sample regularities for more accurate and faithful dental point-cloud completion.


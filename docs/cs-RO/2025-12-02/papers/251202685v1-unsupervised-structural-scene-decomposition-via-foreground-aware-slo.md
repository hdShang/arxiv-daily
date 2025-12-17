---
layout: default
title: Unsupervised Structural Scene Decomposition via Foreground-Aware Slot Attention with Pseudo-Mask Guidance
---

# Unsupervised Structural Scene Decomposition via Foreground-Aware Slot Attention with Pseudo-Mask Guidance

**arXiv**: [2512.02685v1](https://arxiv.org/abs/2512.02685) | [PDF](https://arxiv.org/pdf/2512.02685.pdf)

**作者**: Huankun Sheng, Ming Li, Yixiang Wei, Yeying Fan, Yu-Hui Wen, Tieliang Gong, Yong-Jin Liu

---

## 💡 一句话要点

**提出前景感知槽注意力框架，通过伪掩码引导解决无监督场景分解中的背景干扰问题**

**关键词**: `无监督场景分解` `槽注意力` `前景背景分离` `伪掩码引导` `对象中心表示学习`

## 📋 核心要点

1. 现有槽注意力方法对前景和背景区域不加区分，导致背景干扰和实例发现性能不佳
2. 采用两阶段框架：第一阶段通过双槽竞争机制粗分解场景，第二阶段引入掩码槽注意力机制分离背景与前景对象
3. 在合成和真实数据集上实验表明，该方法优于现有技术，验证了显式前景建模和伪掩码引导的有效性

## 📄 摘要（原文）

> Recent advances in object-centric representation learning have shown that slot attention-based methods can effectively decompose visual scenes into object slot representations without supervision. However, existing approaches typically process foreground and background regions indiscriminately, often resulting in background interference and suboptimal instance discovery performance on real-world data. To address this limitation, we propose Foreground-Aware Slot Attention (FASA), a two-stage framework that explicitly separates foreground from background to enable precise object discovery. In the first stage, FASA performs a coarse scene decomposition to distinguish foreground from background regions through a dual-slot competition mechanism. These slots are initialized via a clustering-based strategy, yielding well-structured representations of salient regions. In the second stage, we introduce a masked slot attention mechanism where the first slot captures the background while the remaining slots compete to represent individual foreground objects. To further address over-segmentation of foreground objects, we incorporate pseudo-mask guidance derived from a patch affinity graph constructed with self-supervised image features to guide the learning of foreground slots. Extensive experiments on both synthetic and real-world datasets demonstrate that FASA consistently outperforms state-of-the-art methods, validating the effectiveness of explicit foreground modeling and pseudo-mask guidance for robust scene decomposition and object-coherent representation. Code will be made publicly available.


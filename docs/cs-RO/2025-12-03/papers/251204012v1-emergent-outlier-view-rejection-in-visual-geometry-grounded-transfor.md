---
layout: default
title: Emergent Outlier View Rejection in Visual Geometry Grounded Transformers
---

# Emergent Outlier View Rejection in Visual Geometry Grounded Transformers

**arXiv**: [2512.04012v1](https://arxiv.org/abs/2512.04012) | [PDF](https://arxiv.org/pdf/2512.04012.pdf)

**作者**: Jisang Han, Sunghwan Hong, Jaewoo Jung, Wooseok Jang, Honggyu An, Qianqian Wang, Seungryong Kim, Chen Feng

---

## 💡 一句话要点

**发现前馈三维重建模型VGGT隐含离群视图抑制能力，无需额外训练即可提升野外图像重建鲁棒性。**

**关键词**: `三维重建` `离群视图抑制` `前馈模型` `视觉几何` `Transformer` `野外图像处理`

## 📋 核心要点

1. 核心问题：野外图像集合中的噪声图像（如无重叠视图）会降低前馈三维重建模型的性能。
2. 方法要点：分析VGGT模型，识别出特定层自然编码离群抑制表示，直接用于离群视图过滤。
3. 实验或效果：在受控和野外数据集上验证该隐含过滤机制的一致性和泛化能力。

## 📄 摘要（原文）

> Reliable 3D reconstruction from in-the-wild image collections is often hindered by "noisy" images-irrelevant inputs with little or no view overlap with others. While traditional Structure-from-Motion pipelines handle such cases through geometric verification and outlier rejection, feed-forward 3D reconstruction models lack these explicit mechanisms, leading to degraded performance under in-the-wild conditions. In this paper, we discover that the existing feed-forward reconstruction model, e.g., VGGT, despite lacking explicit outlier-rejection mechanisms or noise-aware training, can inherently distinguish distractor images. Through an in-depth analysis under varying proportions of synthetic distractors, we identify a specific layer that naturally exhibits outlier-suppressing behavior. Further probing reveals that this layer encodes discriminative internal representations that enable an effective noise-filtering capability, which we simply leverage to perform outlier-view rejection in feed-forward 3D reconstruction without any additional fine-tuning or supervision. Extensive experiments on both controlled and in-the-wild datasets demonstrate that this implicit filtering mechanism is consistent and generalizes well across diverse scenarios.


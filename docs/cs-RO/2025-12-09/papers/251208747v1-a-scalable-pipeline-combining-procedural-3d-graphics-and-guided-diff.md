---
layout: default
title: A Scalable Pipeline Combining Procedural 3D Graphics and Guided Diffusion for Photorealistic Synthetic Training Data Generation in White Button Mushroom Segmentation
---

# A Scalable Pipeline Combining Procedural 3D Graphics and Guided Diffusion for Photorealistic Synthetic Training Data Generation in White Button Mushroom Segmentation

**arXiv**: [2512.08747v1](https://arxiv.org/abs/2512.08747) | [PDF](https://arxiv.org/pdf/2512.08747.pdf)

**作者**: Artúr I. Károly, Péter Galambos

---

## 💡 一句话要点

**提出结合3D渲染与约束扩散的流程，以生成逼真合成数据用于蘑菇分割。**

**关键词**: `合成数据生成` `3D渲染` `扩散模型` `蘑菇分割` `农业计算机视觉`

## 📋 核心要点

1. 工业蘑菇种植需大量标注数据，但真实数据获取成本高且合成数据常缺乏真实感。
2. 方法集成Blender 3D渲染与约束扩散模型，自动生成高质量逼真合成图像，保留场景控制。
3. 在零样本设置下，基于合成数据训练的Mask R-CNN在真实数据集上达到先进分割性能。

## 📄 摘要（原文）

> Industrial mushroom cultivation increasingly relies on computer vision for monitoring and automated harvesting. However, developing accurate detection and segmentation models requires large, precisely annotated datasets that are costly to produce. Synthetic data provides a scalable alternative, yet often lacks sufficient realism to generalize to real-world scenarios. This paper presents a novel workflow that integrates 3D rendering in Blender with a constrained diffusion model to automatically generate high-quality annotated, photorealistic synthetic images of Agaricus Bisporus mushrooms. This approach preserves full control over 3D scene configuration and annotations while achieving photorealism without the need for specialized computer graphics expertise. We release two synthetic datasets (each containing 6,000 images depicting over 250k mushroom instances) and evaluate Mask R-CNN models trained on them in a zero-shot setting. When tested on two independent real-world datasets (including a newly collected benchmark), our method achieves state-of-the-art segmentation performance (F1 = 0.859 on M18K), despite using only synthetic training data. Although the approach is demonstrated on Agaricus Bisporus mushrooms, the proposed pipeline can be readily adapted to other mushroom species or to other agricultural domains, such as fruit and leaf detection.


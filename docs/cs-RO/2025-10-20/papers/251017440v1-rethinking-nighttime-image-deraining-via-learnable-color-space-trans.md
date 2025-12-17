---
layout: default
title: Rethinking Nighttime Image Deraining via Learnable Color Space Transformation
---

# Rethinking Nighttime Image Deraining via Learnable Color Space Transformation

**arXiv**: [2510.17440v1](https://arxiv.org/abs/2510.17440) | [PDF](https://arxiv.org/pdf/2510.17440.pdf)

**作者**: Qiyuan Guan, Xiang Chen, Guiyue Jin, Jiyu Jin, Shumin Fan, Tianyu Song, Jinshan Pan

---

## 💡 一句话要点

**提出CST-Net和HQ-NightRain数据集以解决夜间图像去雨问题**

**关键词**: `夜间图像去雨` `颜色空间转换` `隐式光照引导` `高质量数据集` `深度学习`

## 📋 核心要点

1. 夜间图像去雨面临雨与光照耦合的复杂性和高质量数据集缺乏的核心问题
2. 方法要点包括可学习颜色空间转换器在Y通道去雨和隐式光照引导增强鲁棒性
3. 实验验证新数据集的高质量与模型在复杂场景中的有效性

## 📄 摘要（原文）

> Compared to daytime image deraining, nighttime image deraining poses
> significant challenges due to inherent complexities of nighttime scenarios and
> the lack of high-quality datasets that accurately represent the coupling effect
> between rain and illumination. In this paper, we rethink the task of nighttime
> image deraining and contribute a new high-quality benchmark, HQ-NightRain,
> which offers higher harmony and realism compared to existing datasets. In
> addition, we develop an effective Color Space Transformation Network (CST-Net)
> for better removing complex rain from nighttime scenes. Specifically, we
> propose a learnable color space converter (CSC) to better facilitate rain
> removal in the Y channel, as nighttime rain is more pronounced in the Y channel
> compared to the RGB color space. To capture illumination information for
> guiding nighttime deraining, implicit illumination guidance is introduced
> enabling the learned features to improve the model's robustness in complex
> scenarios. Extensive experiments show the value of our dataset and the
> effectiveness of our method. The source code and datasets are available at
> https://github.com/guanqiyuan/CST-Net.


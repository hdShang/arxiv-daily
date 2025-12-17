---
layout: default
title: Eevee: Towards Close-up High-resolution Video-based Virtual Try-on
---

# Eevee: Towards Close-up High-resolution Video-based Virtual Try-on

**arXiv**: [2511.18957v1](https://arxiv.org/abs/2511.18957) | [PDF](https://arxiv.org/pdf/2511.18957.pdf)

**作者**: Jianhao Zeng, Yancheng Bai, Ruidong Chen, Xuanpu Zhang, Lei Sun, Dongyang Jin, Ryan Xu, Nannan Zhang, Dan Song, Xiangxiang Chu

---

## 💡 一句话要点

**提出高分辨率视频虚拟试穿数据集与VGID指标，以提升服装细节真实性与一致性。**

**关键词**: `视频虚拟试穿` `高分辨率数据集` `服装一致性评估` `近景视频生成` `纹理细节保留`

## 📋 核心要点

1. 核心问题：现有虚拟试穿依赖单张服装图像，无法准确捕捉纹理细节，且缺乏近景视频。
2. 方法要点：构建包含高清图像、文本描述及全/近景视频的数据集，并设计VGID指标评估一致性。
3. 实验或效果：实验验证数据集提升模型纹理提取能力，基准测试揭示现有方法在细节保留上的不足。

## 📄 摘要（原文）

> Video virtual try-on technology provides a cost-effective solution for creating marketing videos in fashion e-commerce. However, its practical adoption is hindered by two critical limitations. First, the reliance on a single garment image as input in current virtual try-on datasets limits the accurate capture of realistic texture details. Second, most existing methods focus solely on generating full-shot virtual try-on videos, neglecting the business's demand for videos that also provide detailed close-ups. To address these challenges, we introduce a high-resolution dataset for video-based virtual try-on. This dataset offers two key features. First, it provides more detailed information on the garments, which includes high-fidelity images with detailed close-ups and textual descriptions; Second, it uniquely includes full-shot and close-up try-on videos of real human models. Furthermore, accurately assessing consistency becomes significantly more critical for the close-up videos, which demand high-fidelity preservation of garment details. To facilitate such fine-grained evaluation, we propose a new garment consistency metric VGID (Video Garment Inception Distance) that quantifies the preservation of both texture and structure. Our experiments validate these contributions. We demonstrate that by utilizing the detailed images from our dataset, existing video generation models can extract and incorporate texture features, significantly enhancing the realism and detail fidelity of virtual try-on results. Furthermore, we conduct a comprehensive benchmark of recent models. The benchmark effectively identifies the texture and structural preservation problems among current methods.


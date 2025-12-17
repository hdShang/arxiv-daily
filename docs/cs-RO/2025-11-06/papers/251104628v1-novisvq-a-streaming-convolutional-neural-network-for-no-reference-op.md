---
layout: default
title: NovisVQ: A Streaming Convolutional Neural Network for No-Reference Opinion-Unaware Frame Quality Assessment
---

# NovisVQ: A Streaming Convolutional Neural Network for No-Reference Opinion-Unaware Frame Quality Assessment

**arXiv**: [2511.04628v1](https://arxiv.org/abs/2511.04628) | [PDF](https://arxiv.org/pdf/2511.04628.pdf)

**作者**: Kylie Cancilla, Alexander Moore, Amar Saini, Carmen Carrano

---

## 💡 一句话要点

**提出NovisVQ流式卷积网络，用于无参考无意见视频质量评估**

**关键词**: `视频质量评估` `无参考方法` `时序建模` `流式卷积网络` `合成数据训练`

## 📋 核心要点

1. 现有视频质量评估方法依赖参考视频或人类意见标签，难以扩展
2. 使用合成退化数据训练时序感知卷积网络，直接预测全参考指标
3. 在DAVIS数据集上验证，优于图像基线和BRISQUE，强调时序建模价值

## 📄 摘要（原文）

> Video quality assessment (VQA) is vital for computer vision tasks, but
> existing approaches face major limitations: full-reference (FR) metrics require
> clean reference videos, and most no-reference (NR) models depend on training on
> costly human opinion labels. Moreover, most opinion-unaware NR methods are
> image-based, ignoring temporal context critical for video object detection. In
> this work, we present a scalable, streaming-based VQA model that is both
> no-reference and opinion-unaware. Our model leverages synthetic degradations of
> the DAVIS dataset, training a temporal-aware convolutional architecture to
> predict FR metrics (LPIPS , PSNR, SSIM) directly from degraded video, without
> references at inference. We show that our streaming approach outperforms our
> own image-based baseline by generalizing across diverse degradations,
> underscoring the value of temporal modeling for scalable VQA in real-world
> vision systems. Additionally, we demonstrate that our model achieves higher
> correlation with full-reference metrics compared to BRISQUE, a widely-used
> opinion-aware image quality assessment baseline, validating the effectiveness
> of our temporal, opinion-unaware approach.


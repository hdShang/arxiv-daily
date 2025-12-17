---
layout: default
title: Zero-Shot CFC: Fast Real-World Image Denoising based on Cross-Frequency Consistency
---

# Zero-Shot CFC: Fast Real-World Image Denoising based on Cross-Frequency Consistency

**arXiv**: [2510.12646v1](https://arxiv.org/abs/2510.12646) | [PDF](https://arxiv.org/pdf/2510.12646.pdf)

**作者**: Yanlin Jiang, Yuchen Liu, Mingren Liu

---

## 💡 一句话要点

**提出基于跨频一致性的零样本去噪方法，以高效处理真实世界图像噪声**

**关键词**: `零样本去噪` `跨频一致性` `真实世界图像` `轻量网络` `噪声分布未知`

## 📋 核心要点

1. 现有零样本去噪方法训练时间长且依赖噪声独立性假设，限制真实场景应用
2. 利用图像纹理在频带间的一致性，设计跨频一致性损失和轻量网络实现去噪
3. 实验显示在真实数据集上，该方法在计算效率和去噪性能上优于其他先进方法

## 📄 摘要（原文）

> Zero-shot denoisers address the dataset dependency of deep-learning-based
> denoisers, enabling the denoising of unseen single images. Nonetheless,
> existing zero-shot methods suffer from long training times and rely on the
> assumption of noise independence and a zero-mean property, limiting their
> effectiveness in real-world denoising scenarios where noise characteristics are
> more complicated. This paper proposes an efficient and effective method for
> real-world denoising, the Zero-Shot denoiser based on Cross-Frequency
> Consistency (ZSCFC), which enables training and denoising with a single noisy
> image and does not rely on assumptions about noise distribution. Specifically,
> image textures exhibit position similarity and content consistency across
> different frequency bands, while noise does not. Based on this property, we
> developed cross-frequency consistency loss and an ultralight network to realize
> image denoising. Experiments on various real-world image datasets demonstrate
> that our ZSCFC outperforms other state-of-the-art zero-shot methods in terms of
> computational efficiency and denoising performance.


---
layout: default
title: ATAC: Augmentation-Based Test-Time Adversarial Correction for CLIP
---

# ATAC: Augmentation-Based Test-Time Adversarial Correction for CLIP

**arXiv**: [2511.17362v1](https://arxiv.org/abs/2511.17362) | [PDF](https://arxiv.org/pdf/2511.17362.pdf)

**作者**: Linxiang Su, András Balogh

---

## 💡 一句话要点

**提出ATAC方法以增强CLIP在测试时对抗扰动的鲁棒性**

**关键词**: `测试时防御` `对抗鲁棒性` `CLIP模型` `嵌入空间校正` `图像增强`

## 📋 核心要点

1. CLIP在零样本图像-文本匹配中易受图像对抗扰动攻击
2. ATAC在嵌入空间计算增强诱导漂移向量，基于角度一致性校正嵌入
3. 实验显示ATAC鲁棒性显著提升，平均超越先前方法近50%，计算开销低

## 📄 摘要（原文）

> Despite its remarkable success in zero-shot image-text matching, CLIP remains highly vulnerable to adversarial perturbations on images. As adversarial fine-tuning is prohibitively costly, recent works explore various test-time defense strategies; however, these approaches still exhibit limited robustness. In this work, we revisit this problem and propose a simple yet effective strategy: Augmentation-based Test-time Adversarial Correction (ATAC). Our method operates directly in the embedding space of CLIP, calculating augmentation-induced drift vectors to infer a semantic recovery direction and correcting the embedding based on the angular consistency of these latent drifts. Across a wide range of benchmarks, ATAC consistently achieves remarkably high robustness, surpassing that of previous state-of-the-art methods by nearly 50\% on average, all while requiring minimal computational overhead. Furthermore, ATAC retains state-of-the-art robustness in unconventional and extreme settings and even achieves nontrivial robustness against adaptive attacks. Our results demonstrate that ATAC is an efficient method in a novel paradigm for test-time adversarial defenses in the embedding space of CLIP.


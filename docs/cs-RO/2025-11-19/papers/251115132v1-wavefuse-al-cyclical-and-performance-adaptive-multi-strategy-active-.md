---
layout: default
title: WaveFuse-AL: Cyclical and Performance-Adaptive Multi-Strategy Active Learning for Medical Images
---

# WaveFuse-AL: Cyclical and Performance-Adaptive Multi-Strategy Active Learning for Medical Images

**arXiv**: [2511.15132v1](https://arxiv.org/abs/2511.15132) | [PDF](https://arxiv.org/pdf/2511.15132.pdf)

**作者**: Nishchala Thakur, Swati Kochhar, Deepti R. Bathula, Sukrit Gupta

---

## 💡 一句话要点

**提出WaveFuse-AL框架，通过自适应融合多策略降低医学图像标注成本**

**关键词**: `主动学习` `医学图像分析` `多策略融合` `自适应学习` `样本选择`

## 📋 核心要点

1. 主动学习中单一策略在不同阶段表现不一致，影响样本选择效率
2. 融合BALD、BADGE、Entropy和CoreSet策略，结合周期性和性能自适应调整权重
3. 在三个医学图像基准测试中，显著优于单策略和交替策略基线

## 📄 摘要（原文）

> Active learning reduces annotation costs in medical imaging by strategically selecting the most informative samples for labeling. However, individual acquisition strategies often exhibit inconsistent behavior across different stages of the active learning cycle. We propose Cyclical and Performance-Adaptive Multi-Strategy Active Learning (WaveFuse-AL), a novel framework that adaptively fuses multiple established acquisition strategies-BALD, BADGE, Entropy, and CoreSet throughout the learning process. WaveFuse-AL integrates cyclical (sinusoidal) temporal priors with performance-driven adaptation to dynamically adjust strategy importance over time. We evaluate WaveFuse-AL on three medical imaging benchmarks: APTOS-2019 (multi-class classification), RSNA Pneumonia Detection (binary classification), and ISIC-2018 (skin lesion segmentation). Experimental results demonstrate that WaveFuse-AL consistently outperforms both single-strategy and alternating-strategy baselines, achieving statistically significant performance improvements (on ten out of twelve metric measurements) while maximizing the utility of limited annotation budgets.


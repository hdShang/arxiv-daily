---
layout: default
title: Towards Generalizable Deepfake Detection via Forgery-aware Audio-Visual Adaptation: A Variational Bayesian Approach
---

# Towards Generalizable Deepfake Detection via Forgery-aware Audio-Visual Adaptation: A Variational Bayesian Approach

**arXiv**: [2511.19080v1](https://arxiv.org/abs/2511.19080) | [PDF](https://arxiv.org/pdf/2511.19080.pdf)

**作者**: Fan Nie, Jiangqun Ni, Jian Zhang, Bin Zhang, Weizhe Zhang, Bin Li

---

## 💡 一句话要点

**提出FoVB框架以提升音视频深度伪造检测的泛化性**

**关键词**: `深度伪造检测` `音视频相关性学习` `变分贝叶斯估计` `多模态学习` `泛化性提升`

## 📋 核心要点

1. 核心问题：多模态深度伪造检测中，音视频不一致性难以泛化识别。
2. 方法要点：采用变分贝叶斯估计音视频相关性，分解模态特定与相关性变量。
3. 实验效果：在多个基准测试中优于现有方法，验证了泛化性能。

## 📄 摘要（原文）

> The widespread application of AIGC contents has brought not only unprecedented opportunities, but also potential security concerns, e.g., audio-visual deepfakes. Therefore, it is of great importance to develop an effective and generalizable method for multi-modal deepfake detection. Typically, the audio-visual correlation learning could expose subtle cross-modal inconsistencies, e.g., audio-visual misalignment, which serve as crucial clues in deepfake detection. In this paper, we reformulate the correlation learning with variational Bayesian estimation, where audio-visual correlation is approximated as a Gaussian distributed latent variable, and thus develop a novel framework for deepfake detection, i.e., Forgery-aware Audio-Visual Adaptation with Variational Bayes (FoVB). Specifically, given the prior knowledge of pre-trained backbones, we adopt two core designs to estimate audio-visual correlations effectively. First, we exploit various difference convolutions and a high-pass filter to discern local and global forgery traces from both modalities. Second, with the extracted forgery-aware features, we estimate the latent Gaussian variable of audio-visual correlation via variational Bayes. Then, we factorize the variable into modality-specific and correlation-specific ones with orthogonality constraint, allowing them to better learn intra-modal and cross-modal forgery traces with less entanglement. Extensive experiments demonstrate that our FoVB outperforms other state-of-the-art methods in various benchmarks.


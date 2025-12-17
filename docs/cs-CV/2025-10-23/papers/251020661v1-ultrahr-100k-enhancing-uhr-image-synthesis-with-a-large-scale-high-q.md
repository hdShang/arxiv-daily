---
layout: default
title: UltraHR-100K: Enhancing UHR Image Synthesis with A Large-Scale High-Quality Dataset
---

# UltraHR-100K: Enhancing UHR Image Synthesis with A Large-Scale High-Quality Dataset

**arXiv**: [2510.20661v1](https://arxiv.org/abs/2510.20661) | [PDF](https://arxiv.org/pdf/2510.20661.pdf)

**作者**: Chen Zhao, En Ci, Yunzhe Xu, Tiehan Fan, Shanyan Guan, Yanhao Ge, Jian Yang, Ying Tai

---

## 💡 一句话要点

**提出UltraHR-100K数据集和频率感知后训练方法以增强超高清图像合成**

**关键词**: `超高清图像合成` `文本到图像生成` `扩散模型` `频率正则化` `数据集构建` `细节增强`

## 📋 核心要点

1. 核心问题：缺乏大规模高质量超高清文本到图像数据集和针对细节合成的训练策略。
2. 方法要点：引入100K超高清图像数据集，并设计细节导向时间步采样和软加权频率正则化。
3. 实验或效果：在UltraHR-eval4K基准上显著提升细节质量和整体保真度。

## 📄 摘要（原文）

> Ultra-high-resolution (UHR) text-to-image (T2I) generation has seen notable
> progress. However, two key challenges remain : 1) the absence of a large-scale
> high-quality UHR T2I dataset, and (2) the neglect of tailored training
> strategies for fine-grained detail synthesis in UHR scenarios. To tackle the
> first challenge, we introduce \textbf{UltraHR-100K}, a high-quality dataset of
> 100K UHR images with rich captions, offering diverse content and strong visual
> fidelity. Each image exceeds 3K resolution and is rigorously curated based on
> detail richness, content complexity, and aesthetic quality. To tackle the
> second challenge, we propose a frequency-aware post-training method that
> enhances fine-detail generation in T2I diffusion models. Specifically, we
> design (i) \textit{Detail-Oriented Timestep Sampling (DOTS)} to focus learning
> on detail-critical denoising steps, and (ii) \textit{Soft-Weighting Frequency
> Regularization (SWFR)}, which leverages Discrete Fourier Transform (DFT) to
> softly constrain frequency components, encouraging high-frequency detail
> preservation. Extensive experiments on our proposed UltraHR-eval4K benchmarks
> demonstrate that our approach significantly improves the fine-grained detail
> quality and overall fidelity of UHR image generation. The code is available at
> \href{https://github.com/NJU-PCALab/UltraHR-100k}{here}.


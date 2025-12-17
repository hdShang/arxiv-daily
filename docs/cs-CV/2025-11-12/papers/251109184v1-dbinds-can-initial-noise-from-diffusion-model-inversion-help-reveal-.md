---
layout: default
title: DBINDS - Can Initial Noise from Diffusion Model Inversion Help Reveal AI-Generated Videos?
---

# DBINDS - Can Initial Noise from Diffusion Model Inversion Help Reveal AI-Generated Videos?

**arXiv**: [2511.09184v1](https://arxiv.org/abs/2511.09184) | [PDF](https://arxiv.org/pdf/2511.09184.pdf)

**作者**: Yanlin Wu, Xiaogang Yuan, Dezhi An

---

## 💡 一句话要点

**提出DBINDS基于扩散模型反演检测AI生成视频，提升跨生成器泛化能力**

**关键词**: `AI生成视频检测` `扩散模型反演` `潜在空间分析` `跨生成器泛化` `特征优化` `LightGBM分类器`

## 📋 核心要点

1. AI生成视频快速发展，对内容安全和取证分析构成挑战，现有检测器泛化性差
2. DBINDS利用扩散反演恢复初始噪声序列，分析潜在空间动态而非像素特征
3. 在GenVidBench上，DBINDS单生成器训练实现强跨生成器性能，泛化性和鲁棒性良好

## 📄 摘要（原文）

> AI-generated video has advanced rapidly and poses serious challenges to content security and forensic analysis. Existing detectors rely mainly on pixel-level visual cues and generalize poorly to unseen generators. We propose DBINDS, a diffusion-model-inversion based detector that analyzes latent-space dynamics rather than pixels. We find that initial noise sequences recovered by diffusion inversion differ systematically between real and generated videos. Building on this, DBINDS forms an Initial Noise Difference Sequence (INDS) and extracts multi-domain, multi-scale features. With feature optimization and a LightGBM classifier tuned by Bayesian search, DBINDS (trained on a single generator) achieves strong cross-generator performance on GenVidBench, demonstrating good generalization and robustness in limited-data settings.


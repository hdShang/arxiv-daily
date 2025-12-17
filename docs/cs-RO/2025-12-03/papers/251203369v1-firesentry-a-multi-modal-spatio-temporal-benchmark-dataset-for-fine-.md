---
layout: default
title: FireSentry: A Multi-Modal Spatio-temporal Benchmark Dataset for Fine-Grained Wildfire Spread Forecasting
---

# FireSentry: A Multi-Modal Spatio-temporal Benchmark Dataset for Fine-Grained Wildfire Spread Forecasting

**arXiv**: [2512.03369v1](https://arxiv.org/abs/2512.03369) | [PDF](https://arxiv.org/pdf/2512.03369.pdf)

**作者**: Nan Zhou, Huandong Wang, Jiahao Li, Han Li, Yali Song, Qiuhua Wang, Yong Li, Xinlei Chen

---

## 💡 一句话要点

**提出FireSentry数据集与FiReDiff范式以解决细粒度野火蔓延预测问题**

**关键词**: `野火蔓延预测` `多模态数据集` `细粒度建模` `生成模型` `视频预测` `掩码分割`

## 📋 核心要点

1. 现有野火预测研究依赖低分辨率数据，难以建模局部动态，限制了高精度预测能力。
2. FireSentry提供亚米级空间和亚秒级时间分辨率的多模态数据，包括可见光/红外视频和环境测量。
3. FiReDiff通过先预测红外视频再分割火掩码，在生成模型中显著提升视频质量和掩码准确性。

## 📄 摘要（原文）

> Fine-grained wildfire spread prediction is crucial for enhancing emergency response efficacy and decision-making precision. However, existing research predominantly focuses on coarse spatiotemporal scales and relies on low-resolution satellite data, capturing only macroscopic fire states while fundamentally constraining high-precision localized fire dynamics modeling capabilities. To bridge this gap, we present FireSentry, a provincial-scale multi-modal wildfire dataset characterized by sub-meter spatial and sub-second temporal resolution. Collected using synchronized UAV platforms, FireSentry provides visible and infrared video streams, in-situ environmental measurements, and manually validated fire masks. Building on FireSentry, we establish a comprehensive benchmark encompassing physics-based, data-driven, and generative models, revealing the limitations of existing mask-only approaches. Our analysis proposes FiReDiff, a novel dual-modality paradigm that first predicts future video sequences in the infrared modality, and then precisely segments fire masks in the mask modality based on the generated dynamics. FiReDiff achieves state-of-the-art performance, with video quality gains of 39.2% in PSNR, 36.1% in SSIM, 50.0% in LPIPS, 29.4% in FVD, and mask accuracy gains of 3.3% in AUPRC, 59.1% in F1 score, 42.9% in IoU, and 62.5% in MSE when applied to generative models. The FireSentry benchmark dataset and FiReDiff paradigm collectively advance fine-grained wildfire forecasting and dynamic disaster simulation. The processed benchmark dataset is publicly available at: https://github.com/Munan222/FireSentry-Benchmark-Dataset.


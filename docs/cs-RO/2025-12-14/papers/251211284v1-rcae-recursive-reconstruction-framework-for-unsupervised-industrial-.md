---
layout: default
title: RcAE: Recursive Reconstruction Framework for Unsupervised Industrial Anomaly Detection
---

# RcAE: Recursive Reconstruction Framework for Unsupervised Industrial Anomaly Detection

**arXiv**: [2512.11284v1](https://arxiv.org/abs/2512.11284) | [PDF](https://arxiv.org/pdf/2512.11284.pdf)

**作者**: Rongcheng Wu, Hao Zhu, Shiying Zhang, Mingzhe Wang, Zhidong Li, Hui Li, Jianlong Zhou, Jiangtao Cui, Fang Chen, Pingyang Sun, Qiyu Liao, Ye Lin

---

## 💡 一句话要点

**提出递归自编码器框架RcAE，通过迭代重建渐进抑制工业异常，实现高效无监督检测**

**关键词**: `无监督异常检测` `工业视觉` `递归自编码器` `渐进重建` `细节保留` `高效推理`

## 📋 核心要点

1. 传统自编码器单次解码难以有效处理不同严重程度和尺度的异常，导致异常抑制不完整和细节丢失
2. RcAE采用递归架构迭代重建，逐步抑制异常并细化正常结构，结合跨递归检测模块和细节保留网络提升检测能力
3. 实验表明该方法显著优于现有非扩散方法，性能与扩散模型相当但参数量仅10%，推理速度大幅提升

## 📄 摘要（原文）

> Unsupervised industrial anomaly detection requires accurately identifying defects without labeled data. Traditional autoencoder-based methods often struggle with incomplete anomaly suppression and loss of fine details, as their single-pass decoding fails to effectively handle anomalies with varying severity and scale. We propose a recursive architecture for autoencoder (RcAE), which performs reconstruction iteratively to progressively suppress anomalies while refining normal structures. Unlike traditional single-pass models, this recursive design naturally produces a sequence of reconstructions, progressively exposing suppressed abnormal patterns. To leverage this reconstruction dynamics, we introduce a Cross Recursion Detection (CRD) module that tracks inconsistencies across recursion steps, enhancing detection of both subtle and large-scale anomalies. Additionally, we incorporate a Detail Preservation Network (DPN) to recover high-frequency textures typically lost during reconstruction. Extensive experiments demonstrate that our method significantly outperforms existing non-diffusion methods, and achieves performance on par with recent diffusion models with only 10% of their parameters and offering substantially faster inference. These results highlight the practicality and efficiency of our approach for real-world applications.


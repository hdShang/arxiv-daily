---
layout: default
title: Autoregressive Video Autoencoder with Decoupled Temporal and Spatial Context
---

# Autoregressive Video Autoencoder with Decoupled Temporal and Spatial Context

**arXiv**: [2512.11293v1](https://arxiv.org/abs/2512.11293) | [PDF](https://arxiv.org/pdf/2512.11293.pdf)

**作者**: Cuifeng Shen, Lumin Xu, Xingguo Zhu, Gengdai Liu

---

## 💡 一句话要点

**提出自回归视频自编码器，通过解耦时空上下文以提升视频重建质量与效率。**

**关键词**: `视频自编码器` `时空解耦` `自回归模型` `视频压缩` `视频生成`

## 📋 核心要点

1. 现有视频自编码器常纠缠时空信息，导致时间一致性差和性能受限。
2. ARVAE采用自回归方式逐帧处理，结合流场和空间补偿实现高效无损压缩。
3. 实验显示模型轻量、数据需求小，重建质量优，下游生成任务潜力强。

## 📄 摘要（原文）

> Video autoencoders compress videos into compact latent representations for efficient reconstruction, playing a vital role in enhancing the quality and efficiency of video generation. However, existing video autoencoders often entangle spatial and temporal information, limiting their ability to capture temporal consistency and leading to suboptimal performance. To address this, we propose Autoregressive Video Autoencoder (ARVAE), which compresses and reconstructs each frame conditioned on its predecessor in an autoregressive manner, allowing flexible processing of videos with arbitrary lengths. ARVAE introduces a temporal-spatial decoupled representation that combines downsampled flow field for temporal coherence with spatial relative compensation for newly emerged content, achieving high compression efficiency without information loss. Specifically, the encoder compresses the current and previous frames into the temporal motion and spatial supplement, while the decoder reconstructs the original frame from the latent representations given the preceding frame. A multi-stage training strategy is employed to progressively optimize the model. Extensive experiments demonstrate that ARVAE achieves superior reconstruction quality with extremely lightweight models and small-scale training data. Moreover, evaluations on video generation tasks highlight its strong potential for downstream applications.


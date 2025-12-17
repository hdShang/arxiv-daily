---
layout: default
title: Temporal-Visual Semantic Alignment: A Unified Architecture for Transferring Spatial Priors from Vision Models to Zero-Shot Temporal Tasks
---

# Temporal-Visual Semantic Alignment: A Unified Architecture for Transferring Spatial Priors from Vision Models to Zero-Shot Temporal Tasks

**arXiv**: [2511.19856v1](https://arxiv.org/abs/2511.19856) | [PDF](https://arxiv.org/pdf/2511.19856.pdf)

**作者**: Xiangkai Ma, Han Zhang, Wenzhong Li, Sanglu Lu

---

## 💡 一句话要点

**提出TimeArtist框架，实现时间序列与视觉语义对齐，用于零样本时序任务和图像生成。**

**关键词**: `时间序列分析` `跨模态对齐` `零样本学习` `图像生成` `语义级表示` `自监督训练`

## 📋 核心要点

1. 核心问题：现有方法将时间序列转为伪图像，但缺乏语义级对齐，无法捕捉时序波动与视觉概念的关系。
2. 方法要点：采用预热对齐范式，先自监督学习模态共享表示，再冻结编码器并引入投影实现表示级对齐。
3. 实验或效果：在图像生成指标上表现满意，并在零样本时序任务中取得优越结果，验证了跨模态生成能力。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) have achieved remarkable progress in aligning and generating content across text and image modalities. However, the potential of using non-visual, continuous sequential, as a conditioning signal for high-fidelity image generation remains largely unexplored. Furthermore, existing methods that convert series into "pseudo-images" for temporal forecasting fail to establish semantic-level alignment. In this paper, we propose TimeArtist, a temporal-visual conversion framework that pioneers semantic-level alignment between time series fluctuations and visual concepts. It pioneers a "warmup-align" paradigm: first, a dual-autoencoder and shared quantizer are self-supervised trained on large-scale datasets to learn modality-shared representations. Then, the encoders and quantizer are frozen, and a projection is introduced to align temporal and visual samples at the representation level. TimeArtist establishes a versatile cross-modal framework, enabling high-quality, diverse image generation directly from time series, while capturing temporal fluctuation patterns to render images as styles transfer. Extensive experiments show that TimeArtist achieves satisfactory performance in image generation metrics, while also attaining superior results in zero-shot temporal tasks. Our work establishes a new paradigm for cross-modal generation, bridging the gap between temporal dynamics and visual semantics.


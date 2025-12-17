---
layout: default
title: MMSD3.0: A Multi-Image Benchmark for Real-World Multimodal Sarcasm Detection
---

# MMSD3.0: A Multi-Image Benchmark for Real-World Multimodal Sarcasm Detection

**arXiv**: [2510.23299v1](https://arxiv.org/abs/2510.23299) | [PDF](https://arxiv.org/pdf/2510.23299.pdf)

**作者**: Haochen Zhao, Yuyao Kong, Yongxiu Xu, Gaopeng Gou, Hongbo Xu, Yubin Wang, Haoliang Zhang

---

## 💡 一句话要点

**提出MMSD3.0多图像基准和CIRM模型以解决真实世界多模态讽刺检测问题**

**关键词**: `多模态讽刺检测` `多图像基准` `跨图像推理` `跨模态融合` `真实世界数据集`

## 📋 核心要点

1. 现有方法多关注单图像场景，忽略多图像间的语义和情感关系，导致真实世界讽刺检测不足
2. 引入跨图像推理模型CIRM，通过序列建模和相关性引导的跨模态融合捕获图像间连接
3. 在MMSD系列基准上实验，CIRM实现先进性能，验证其在单图像和多图像场景的有效性

## 📄 摘要（原文）

> Despite progress in multimodal sarcasm detection, existing datasets and
> methods predominantly focus on single-image scenarios, overlooking potential
> semantic and affective relations across multiple images. This leaves a gap in
> modeling cases where sarcasm is triggered by multi-image cues in real-world
> settings. To bridge this gap, we introduce MMSD3.0, a new benchmark composed
> entirely of multi-image samples curated from tweets and Amazon reviews. We
> further propose the Cross-Image Reasoning Model (CIRM), which performs targeted
> cross-image sequence modeling to capture latent inter-image connections. In
> addition, we introduce a relevance-guided, fine-grained cross-modal fusion
> mechanism based on text-image correspondence to reduce information loss during
> integration. We establish a comprehensive suite of strong and representative
> baselines and conduct extensive experiments, showing that MMSD3.0 is an
> effective and reliable benchmark that better reflects real-world conditions.
> Moreover, CIRM demonstrates state-of-the-art performance across MMSD, MMSD2.0
> and MMSD3.0, validating its effectiveness in both single-image and multi-image
> scenarios.


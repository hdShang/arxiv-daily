---
layout: default
title: LongVie 2: Multimodal Controllable Ultra-Long Video World Model
---

# LongVie 2: Multimodal Controllable Ultra-Long Video World Model

**arXiv**: [2512.13604v1](https://arxiv.org/abs/2512.13604) | [PDF](https://arxiv.org/pdf/2512.13604.pdf)

**作者**: Jianxiong Gao, Zhaoxi Chen, Xian Liu, Junhao Zhuang, Chengming Xu, Jianfeng Feng, Yu Qiao, Yanwei Fu, Chenyang Si, Ziwei Liu

---

## 💡 一句话要点

**提出LongVie 2以解决长视频世界模型的可控性、视觉质量和时间一致性问题**

**关键词**: `长视频世界模型` `多模态可控生成` `自回归框架` `时间一致性` `视觉质量保持`

## 📋 核心要点

1. 核心问题：构建视频世界模型需兼顾可控性、长期视觉质量和时间一致性
2. 方法要点：采用三阶段自回归训练，集成多模态引导、退化感知训练和历史上下文引导
3. 实验或效果：在LongVGenBench上实现先进性能，支持长达五分钟的连续视频生成

## 📄 摘要（原文）

> Building video world models upon pretrained video generation systems represents an important yet challenging step toward general spatiotemporal intelligence. A world model should possess three essential properties: controllability, long-term visual quality, and temporal consistency. To this end, we take a progressive approach-first enhancing controllability and then extending toward long-term, high-quality generation. We present LongVie 2, an end-to-end autoregressive framework trained in three stages: (1) Multi-modal guidance, which integrates dense and sparse control signals to provide implicit world-level supervision and improve controllability; (2) Degradation-aware training on the input frame, bridging the gap between training and long-term inference to maintain high visual quality; and (3) History-context guidance, which aligns contextual information across adjacent clips to ensure temporal consistency. We further introduce LongVGenBench, a comprehensive benchmark comprising 100 high-resolution one-minute videos covering diverse real-world and synthetic environments. Extensive experiments demonstrate that LongVie 2 achieves state-of-the-art performance in long-range controllability, temporal coherence, and visual fidelity, and supports continuous video generation lasting up to five minutes, marking a significant step toward unified video world modeling.


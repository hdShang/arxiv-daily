---
layout: default
title: OmniZip: Audio-Guided Dynamic Token Compression for Fast Omnimodal Large Language Models
---

# OmniZip: Audio-Guided Dynamic Token Compression for Fast Omnimodal Large Language Models

**arXiv**: [2511.14582v1](https://arxiv.org/abs/2511.14582) | [PDF](https://arxiv.org/pdf/2511.14582.pdf)

**作者**: Keda Tao, Kele Shao, Bohan Yu, Weiqiang Wang, Jian liu, Huan Wang

---

## 💡 一句话要点

**提出OmniZip音频引导动态令牌压缩框架以加速全模态大语言模型推理**

**关键词**: `全模态大语言模型` `令牌压缩` `音频引导` `推理加速` `跨模态相似性`

## 📋 核心要点

1. 全模态大语言模型处理音视频令牌序列时计算开销大，成为瓶颈
2. 无需训练，通过音频令牌识别和保留分数动态引导视频令牌剪枝
3. 实验显示推理速度提升3.42倍，内存减少1.4倍，性能保持

## 📄 摘要（原文）

> Omnimodal large language models (OmniLLMs) have attracted increasing research attention of late towards unified audio-video understanding, wherein processing audio-video token sequences creates a significant computational bottleneck, however. Existing token compression methods have yet to accommodate this emerging need of jointly compressing multimodal tokens. To bridge this gap, we present OmniZip, a training-free, audio-guided audio-visual token-compression framework that optimizes multimodal token representation and accelerates inference. Specifically, OmniZip first identifies salient audio tokens, then computes an audio retention score for each time group to capture information density, thereby dynamically guiding video token pruning and preserving cues from audio anchors enhanced by cross-modal similarity. For each time window, OmniZip compresses the video tokens using an interleaved spatio-temporal scheme. Extensive empirical results demonstrate the merits of OmniZip - it achieves 3.42X inference speedup and 1.4X memory reduction over other top-performing counterparts, while maintaining performance with no training.


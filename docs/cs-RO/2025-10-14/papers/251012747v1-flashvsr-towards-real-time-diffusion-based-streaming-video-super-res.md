---
layout: default
title: FlashVSR: Towards Real-Time Diffusion-Based Streaming Video Super-Resolution
---

# FlashVSR: Towards Real-Time Diffusion-Based Streaming Video Super-Resolution

**arXiv**: [2510.12747v1](https://arxiv.org/abs/2510.12747) | [PDF](https://arxiv.org/pdf/2510.12747.pdf)

**作者**: Junhao Zhuang, Shi Guo, Xin Cai, Xiaohui Li, Yihao Liu, Chun Yuan, Tianfan Xue

---

## 💡 一句话要点

**提出FlashVSR以实现实时扩散视频超分辨率**

**关键词**: `视频超分辨率` `扩散模型` `实时处理` `蒸馏训练` `稀疏注意力` `高效解码`

## 📋 核心要点

1. 扩散模型在视频超分辨率中面临高延迟、计算量大和泛化差问题
2. 采用三阶段蒸馏、稀疏注意力和微小解码器提升效率与实时性
3. 实验显示在A100 GPU上达17 FPS，性能领先且速度提升12倍

## 📄 摘要（原文）

> Diffusion models have recently advanced video restoration, but applying them
> to real-world video super-resolution (VSR) remains challenging due to high
> latency, prohibitive computation, and poor generalization to ultra-high
> resolutions. Our goal in this work is to make diffusion-based VSR practical by
> achieving efficiency, scalability, and real-time performance. To this end, we
> propose FlashVSR, the first diffusion-based one-step streaming framework
> towards real-time VSR. FlashVSR runs at approximately 17 FPS for 768x1408
> videos on a single A100 GPU by combining three complementary innovations: (i) a
> train-friendly three-stage distillation pipeline that enables streaming
> super-resolution, (ii) locality-constrained sparse attention that cuts
> redundant computation while bridging the train-test resolution gap, and (iii) a
> tiny conditional decoder that accelerates reconstruction without sacrificing
> quality. To support large-scale training, we also construct VSR-120K, a new
> dataset with 120k videos and 180k images. Extensive experiments show that
> FlashVSR scales reliably to ultra-high resolutions and achieves
> state-of-the-art performance with up to 12x speedup over prior one-step
> diffusion VSR models. We will release the code, pretrained models, and dataset
> to foster future research in efficient diffusion-based VSR.


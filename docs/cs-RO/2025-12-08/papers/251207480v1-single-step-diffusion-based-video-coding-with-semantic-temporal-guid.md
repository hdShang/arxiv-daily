---
layout: default
title: Single-step Diffusion-based Video Coding with Semantic-Temporal Guidance
---

# Single-step Diffusion-based Video Coding with Semantic-Temporal Guidance

**arXiv**: [2512.07480v1](https://arxiv.org/abs/2512.07480) | [PDF](https://arxiv.org/pdf/2512.07480.pdf)

**作者**: Naifu Xue, Zhaoyang Jia, Jiahao Li, Bin Li, Zihan Zheng, Yuan Zhang, Yan Lu

---

## 💡 一句话要点

**提出S2VC单步扩散视频编码器，结合语义与时序指导，在低码率下实现高效高质量视频压缩。**

**关键词**: `视频编码` `扩散模型` `语义指导` `时序一致性` `低码率压缩` `单步生成`

## 📋 核心要点

1. 传统与神经视频编码在低码率下感知质量提升困难，现有方法存在生成能力不足或采样复杂度高的问题。
2. S2VC采用条件编码框架与单步扩散生成器，引入上下文语义指导和时序一致性指导，提升生成真实性与稳定性。
3. 实验表明S2VC在感知质量上达到先进水平，相比先前方法平均节省52.73%码率，验证单步扩散在视频压缩中的高效性。

## 📄 摘要（原文）

> While traditional and neural video codecs (NVCs) have achieved remarkable rate-distortion performance, improving perceptual quality at low bitrates remains challenging. Some NVCs incorporate perceptual or adversarial objectives but still suffer from artifacts due to limited generation capacity, whereas others leverage pretrained diffusion models to improve quality at the cost of heavy sampling complexity. To overcome these challenges, we propose S2VC, a Single-Step diffusion based Video Codec that integrates a conditional coding framework with an efficient single-step diffusion generator, enabling realistic reconstruction at low bitrates with reduced sampling cost. Recognizing the importance of semantic conditioning in single-step diffusion, we introduce Contextual Semantic Guidance to extract frame-adaptive semantics from buffered features. It replaces text captions with efficient, fine-grained conditioning, thereby improving generation realism. In addition, Temporal Consistency Guidance is incorporated into the diffusion U-Net to enforce temporal coherence across frames and ensure stable generation. Extensive experiments show that S2VC delivers state-of-the-art perceptual quality with an average 52.73% bitrate saving over prior perceptual methods, underscoring the promise of single-step diffusion for efficient, high-quality video compression.


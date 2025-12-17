---
layout: default
title: AaPE: Aliasing-aware Patch Embedding for Self-Supervised Audio Representation Learning
---

# AaPE: Aliasing-aware Patch Embedding for Self-Supervised Audio Representation Learning

**arXiv**: [2512.03637v1](https://arxiv.org/abs/2512.03637) | [PDF](https://arxiv.org/pdf/2512.03637.pdf)

**作者**: Kohei Yamamoto, Kosuke Okusa

---

## 💡 一句话要点

**提出AaPE以缓解Transformer音频自监督学习中的混叠问题并保留高频信息**

**关键词**: `音频自监督学习` `混叠缓解` `Transformer模型` `频谱图处理` `自适应分块嵌入` `掩码师生学习`

## 📋 核心要点

1. 核心问题：Transformer音频SSL模型将频谱图视为图像，卷积分块导致时间下采样，降低有效奈奎斯特频率并引入混叠，而简单低通滤波会丢失任务相关高频线索。
2. 方法要点：AaPE通过带限复正弦核和双指数窗口动态生成特征，增强标准分块令牌，自适应分析易混叠频带，无缝集成到掩码师生自监督学习中。
3. 实验或效果：在AudioSet预训练后，下游任务微调和线性探测评估显示，在部分任务上达到SOTA，其余任务表现竞争性，表明AaPE有效缓解混叠且保留高频信息。

## 📄 摘要（原文）

> Transformer-based audio SSL (self-supervised learning) models often treat spectrograms as images, applying convolutional patchification with heavy temporal downsampling. This lowers the effective Nyquist frequency and introduces aliasing, while naïve low-pass filtering removes task-relevant high-frequency cues. In this study, we present Aliasing-aware Patch Embedding (AaPE), a drop-in patch stem that mitigates aliasing while preserving high-frequency information. AaPE augments standard patch tokens with features produced by a band-limited complex sinusoidal kernel using a two-sided exponential window that dynamically targets alias-prone bands. Frequency and decay parameters of the kernel are estimated from the input, enabling parallel, adaptive subband analysis whose outputs are fused with the standard patch tokens. AaPE integrates seamlessly into the masked teacher-student self-supervised learning. In addition, we combine a multi-mask strategy with a contrastive objective to enforce consistency across diverse mask patterns, stabilizing training. Pre-training on AudioSet followed by fine-tuning evaluation across diverse downstream benchmarks, which spanned categories, such as environmental sounds and other common audio domains. This approach yields state-of-the-art performance on a subset of tasks and competitive results across the remainder. Complementary linear probing evaluation mirrors this pattern, yielding clear gains on several benchmarks and strong performance elsewhere. The collective analysis of these results indicates that AaPE serves to mitigate the effects of aliasing without discarding of informative high-frequency content.


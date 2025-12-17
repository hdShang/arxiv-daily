---
layout: default
title: JEPA as a Neural Tokenizer: Learning Robust Speech Representations with Density Adaptive Attention
---

# JEPA as a Neural Tokenizer: Learning Robust Speech Representations with Density Adaptive Attention

**arXiv**: [2512.07168v1](https://arxiv.org/abs/2512.07168) | [PDF](https://arxiv.org/pdf/2512.07168.pdf)

**作者**: Georgios Ioannides, Christos Constantinou, Aman Chadha, Aaron Elkins, Linsey Pang, Ravid Shwartz-Ziv, Yann LeCun

---

## 💡 一句话要点

**提出结合JEPA与密度自适应注意力的两阶段自监督框架，用于学习鲁棒语音表示和高效令牌化。**

**关键词**: `自监督学习` `语音表示学习` `神经音频编解码` `注意力机制` `令牌化`

## 📋 核心要点

1. 核心问题：未知，但旨在学习鲁棒语音表示以支持高效压缩和语言模型友好性。
2. 方法要点：第一阶段使用JEPA与密度自适应注意力进行潜在空间掩码预测，第二阶段利用FSQ和混合基数打包进行令牌化，结合HiFi-GAN解码器重建波形。
3. 实验或效果：模型在2.5 Hz低帧率下实现自适应时间特征选择和分层结构发现，令牌速率47.5 tokens/sec，与现有神经音频编解码器竞争且更高效。

## 📄 摘要（原文）

> We introduce a two-stage self-supervised framework that combines the Joint-Embedding Predictive Architecture (JEPA) with a Density Adaptive Attention Mechanism (DAAM) for learning robust speech representations. Stage~1 uses JEPA with DAAM to learn semantic audio features via masked prediction in latent space, fully decoupled from waveform reconstruction. Stage~2 leverages these representations for efficient tokenization using Finite Scalar Quantization (FSQ) and a mixed-radix packing scheme, followed by high-fidelity waveform reconstruction with a HiFi-GAN decoder. By integrating Gaussian mixture-based density-adaptive gating into the JEPA encoder, the model performs adaptive temporal feature selection and discovers hierarchical speech structure at a low frame rate of 2.5~Hz. The resulting tokens (47.5 tokens/sec) provide a reversible, highly compressed, and language-model-friendly representation that is competitive with, and often more efficient than, existing neural audio codecs.


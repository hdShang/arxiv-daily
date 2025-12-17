---
layout: default
title: FAIRY2I: Universal Extremely-Low Bit QAT framework via Widely-Linear Representation and Phase-Aware Quantization
---

# FAIRY2I: Universal Extremely-Low Bit QAT framework via Widely-Linear Representation and Phase-Aware Quantization

**arXiv**: [2512.02901v1](https://arxiv.org/abs/2512.02901) | [PDF](https://arxiv.org/pdf/2512.02901.pdf)

**作者**: Feiyu Wang, Xinyu Tan, Bokai Huang, Yihao Zhang, Guoan Wang, Peizhuang Cong, Tong Yang

---

## 💡 一句话要点

**提出Fairy2i框架，通过广泛线性表示和相位感知量化，实现预训练实值模型的极低比特量化。**

**关键词**: `极低比特量化` `广泛线性表示` `相位感知量化` `复值神经网络` `预训练模型转换` `高效推理`

## 📋 核心要点

1. 核心问题：大语言模型量化至单比特极限时，复值模型需从头训练，无法利用预训练实值模型生态。
2. 方法要点：证明实值与广泛线性映射的数学等价性，转换Transformer至复域，采用基于单位四次根的相位感知量化方案。
3. 实验或效果：在LLaMA-2 7B上，2比特精度恢复性能接近全精度基线，优于现有实值二值化和三值化方法。

## 📄 摘要（原文）

> Large language models (LLMs) have revolutionized artificial intelligence, yet their massive memory and computational demands necessitate aggressive quantization, increasingly pushing representations toward the theoretical limit of a single bit. While complex-valued LLMs, such as iFairy, offer a superior chance for low-bit representation compared to real-valued counterparts, they require training from scratch, preventing the utilization of the vast ecosystem of pre-trained real-valued foundation models. Here we present Fairy2i, a universal framework that transforms pre-trained real-valued layers into an equivalent widely-linear complex form, enabling extremely low-bit quantization while reusing existing checkpoints. By proving a lossless mathematical equivalence between real and widely-linear maps, we convert standard Transformers into the complex domain and employ a phase-aware quantization scheme with a highly efficient codebook of fourth roots of unity. Furthermore, we introduce a recursive residual quantization mechanism that iteratively minimizes quantization error, allowing inference to proceed via efficient multiplication-free accumulation. We demonstrate that Fairy2i restores the performance of LLaMA-2 7B at an effective 2-bit precision to levels nearly comparable with full-precision baselines, significantly outperforming state-of-the-art real-valued binary and ternary quantization methods. This work bridges the gap between the representational efficiency of complex-valued arithmetic and the practical utility of pre-trained models, paving a new way for efficient inference on commodity hardware.


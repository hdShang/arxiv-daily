---
layout: default
title: MambaEye: A Size-Agnostic Visual Encoder with Causal Sequential Processing
---

# MambaEye: A Size-Agnostic Visual Encoder with Causal Sequential Processing

**arXiv**: [2511.19963v1](https://arxiv.org/abs/2511.19963) | [PDF](https://arxiv.org/pdf/2511.19963.pdf)

**作者**: Changho Choi, Minho Kim, Jinkyu Kim

---

## 💡 一句话要点

**提出MambaEye视觉编码器，通过因果序列处理实现输入尺寸无关的图像编码。**

**关键词**: `视觉编码器` `因果序列处理` `输入尺寸无关` `相对移动嵌入` `线性复杂度` `图像分类`

## 📋 核心要点

1. 核心问题：现有视觉编码器难以实现输入尺寸无关，限制了模型灵活性。
2. 方法要点：采用单向因果处理和相对移动嵌入，增强平移不变性和分辨率适应性。
3. 实验或效果：在ImageNet-1K上高分辨率表现稳健，保持线性复杂度。

## 📄 摘要（原文）

> Despite decades of progress, a truly input-size agnostic visual encoder-a fundamental characteristic of human vision-has remained elusive. We address this limitation by proposing \textbf{MambaEye}, a novel, causal sequential encoder that leverages the low complexity and causal-process based pure Mamba2 backbone. Unlike previous Mamba-based vision encoders that often employ bidirectional processing, our strictly unidirectional approach preserves the inherent causality of State Space Models, enabling the model to generate a prediction at any point in its input sequence. A core innovation is our use of relative move embedding, which encodes the spatial shift between consecutive patches, providing a strong inductive bias for translation invariance and making the model inherently adaptable to arbitrary image resolutions and scanning patterns. To achieve this, we introduce a novel diffusion-inspired loss function that provides dense, step-wise supervision, training the model to build confidence as it gathers more visual evidence. We demonstrate that MambaEye exhibits robust performance across a wide range of image resolutions, especially at higher resolutions such as $1536^2$ on the ImageNet-1K classification task. This feat is achieved while maintaining linear time and memory complexity relative to the number of patches.


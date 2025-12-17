---
layout: default
title: VLF-MSC: Vision-Language Feature-Based Multimodal Semantic Communication System
---

# VLF-MSC: Vision-Language Feature-Based Multimodal Semantic Communication System

**arXiv**: [2511.10074v1](https://arxiv.org/abs/2511.10074) | [PDF](https://arxiv.org/pdf/2511.10074.pdf)

**作者**: Gwangyeon Ahn, Jiwan Seo, Joonhyuk Kang

---

## 💡 一句话要点

**提出基于视觉语言特征的多模态语义通信系统，以统一表示支持图像和文本生成，提升频谱效率。**

**关键词**: `多模态语义通信` `视觉语言特征` `图像生成` `文本生成` `频谱效率` `信道噪声鲁棒性`

## 📋 核心要点

1. 核心问题：现有语义通信系统需独立处理图像和文本，导致频谱效率低和适应性差。
2. 方法要点：使用预训练视觉语言模型编码图像为紧凑特征，传输后驱动文本和图像生成。
3. 实验或效果：在低信噪比下，系统优于单模态基线，语义准确度高且带宽显著减少。

## 📄 摘要（原文）

> We propose Vision-Language Feature-based Multimodal Semantic Communication (VLF-MSC), a unified system that transmits a single compact vision-language representation to support both image and text generation at the receiver. Unlike existing semantic communication techniques that process each modality separately, VLF-MSC employs a pre-trained vision-language model (VLM) to encode the source image into a vision-language semantic feature (VLF), which is transmitted over the wireless channel. At the receiver, a decoder-based language model and a diffusion-based image generator are both conditioned on the VLF to produce a descriptive text and a semantically aligned image. This unified representation eliminates the need for modality-specific streams or retransmissions, improving spectral efficiency and adaptability. By leveraging foundation models, the system achieves robustness to channel noise while preserving semantic fidelity. Experiments demonstrate that VLF-MSC outperforms text-only and image-only baselines, achieving higher semantic accuracy for both modalities under low SNR with significantly reduced bandwidth.


---
layout: default
title: DGS-Net: Distillation-Guided Gradient Surgery for CLIP Fine-Tuning in AI-Generated Image Detection
---

# DGS-Net: Distillation-Guided Gradient Surgery for CLIP Fine-Tuning in AI-Generated Image Detection

**arXiv**: [2511.13108v1](https://arxiv.org/abs/2511.13108) | [PDF](https://arxiv.org/pdf/2511.13108.pdf)

**作者**: Jiazhen Yan, Ziqiang Li, Fan Wang, Boyu Wang, Zhangjie Fu

---

## 💡 一句话要点

**提出DGS-Net以解决CLIP微调中的灾难性遗忘问题，提升AI生成图像检测性能**

**关键词**: `AI生成图像检测` `CLIP微调` `梯度手术` `蒸馏学习` `灾难性遗忘` `跨域泛化`

## 📋 核心要点

1. 核心问题：CLIP微调导致灾难性遗忘，损害预训练先验并限制跨域泛化
2. 方法要点：通过梯度空间分解，投影有害方向并对齐有益方向，实现先验保持与无关抑制
3. 实验或效果：在50个生成模型上实验，平均性能提升6.6，检测与泛化能力优越

## 📄 摘要（原文）

> The rapid progress of generative models such as GANs and diffusion models has led to the widespread proliferation of AI-generated images, raising concerns about misinformation, privacy violations, and trust erosion in digital media. Although large-scale multimodal models like CLIP offer strong transferable representations for detecting synthetic content, fine-tuning them often induces catastrophic forgetting, which degrades pre-trained priors and limits cross-domain generalization. To address this issue, we propose the Distillation-guided Gradient Surgery Network (DGS-Net), a novel framework that preserves transferable pre-trained priors while suppressing task-irrelevant components. Specifically, we introduce a gradient-space decomposition that separates harmful and beneficial descent directions during optimization. By projecting task gradients onto the orthogonal complement of harmful directions and aligning with beneficial ones distilled from a frozen CLIP encoder, DGS-Net achieves unified optimization of prior preservation and irrelevant suppression. Extensive experiments on 50 generative models demonstrate that our method outperforms state-of-the-art approaches by an average margin of 6.6, achieving superior detection performance and generalization across diverse generation techniques.


---
layout: default
title: ZEBRA: Towards Zero-Shot Cross-Subject Generalization for Universal Brain Visual Decoding
---

# ZEBRA: Towards Zero-Shot Cross-Subject Generalization for Universal Brain Visual Decoding

**arXiv**: [2510.27128v1](https://arxiv.org/abs/2510.27128) | [PDF](https://arxiv.org/pdf/2510.27128.pdf)

**作者**: Haonan Wang, Jingyu Lu, Hongrui Li, Xiaomeng Li

---

## 💡 一句话要点

**提出ZEBRA框架以实现零样本跨被试通用脑视觉解码**

**关键词**: `脑视觉解码` `零样本学习` `fMRI重建` `对抗训练` `跨被试泛化`

## 📋 核心要点

1. 当前脑视觉解码方法依赖被试特定模型或微调，限制可扩展性
2. ZEBRA通过对抗训练分解fMRI表示，分离被试相关与语义相关成分
3. 实验显示ZEBRA在零样本下性能优于基线，接近全微调模型

## 📄 摘要（原文）

> Recent advances in neural decoding have enabled the reconstruction of visual
> experiences from brain activity, positioning fMRI-to-image reconstruction as a
> promising bridge between neuroscience and computer vision. However, current
> methods predominantly rely on subject-specific models or require
> subject-specific fine-tuning, limiting their scalability and real-world
> applicability. In this work, we introduce ZEBRA, the first zero-shot brain
> visual decoding framework that eliminates the need for subject-specific
> adaptation. ZEBRA is built on the key insight that fMRI representations can be
> decomposed into subject-related and semantic-related components. By leveraging
> adversarial training, our method explicitly disentangles these components to
> isolate subject-invariant, semantic-specific representations. This
> disentanglement allows ZEBRA to generalize to unseen subjects without any
> additional fMRI data or retraining. Extensive experiments show that ZEBRA
> significantly outperforms zero-shot baselines and achieves performance
> comparable to fully finetuned models on several metrics. Our work represents a
> scalable and practical step toward universal neural decoding. Code and model
> weights are available at: https://github.com/xmed-lab/ZEBRA.


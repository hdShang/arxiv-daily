---
layout: default
title: Knowledge-Informed Neural Network for Complex-Valued SAR Image Recognition
---

# Knowledge-Informed Neural Network for Complex-Valued SAR Image Recognition

**arXiv**: [2510.20284v1](https://arxiv.org/abs/2510.20284) | [PDF](https://arxiv.org/pdf/2510.20284.pdf)

**作者**: Haodong Yang, Zhongling Huang, Shaojie Guo, Zhe Zhang, Gong Cheng, Junwei Han

---

## 💡 一句话要点

**提出知识通知神经网络以解决复杂SAR图像识别中的表示三难问题**

**关键词**: `复杂SAR图像识别` `知识通知神经网络` `表示三难问题` `参数高效模型` `物理先验嵌入` `自蒸馏学习`

## 📋 核心要点

1. 核心问题：数据有限和领域偏移下，SAR图像识别的泛化、可解释性和效率难以兼顾
2. 方法要点：采用压缩-聚合-压缩架构，嵌入物理先验提取稀疏特征，提升效率与可解释性
3. 实验或效果：在五个SAR基准测试中，参数高效识别达到SOTA，泛化能力强

## 📄 摘要（原文）

> Deep learning models for complex-valued Synthetic Aperture Radar (CV-SAR)
> image recognition are fundamentally constrained by a representation trilemma
> under data-limited and domain-shift scenarios: the concurrent, yet conflicting,
> optimization of generalization, interpretability, and efficiency. Our work is
> motivated by the premise that the rich electromagnetic scattering features
> inherent in CV-SAR data hold the key to resolving this trilemma, yet they are
> insufficiently harnessed by conventional data-driven models. To this end, we
> introduce the Knowledge-Informed Neural Network (KINN), a lightweight framework
> built upon a novel "compression-aggregation-compression" architecture. The
> first stage performs a physics-guided compression, wherein a novel dictionary
> processor adaptively embeds physical priors, enabling a compact unfolding
> network to efficiently extract sparse, physically-grounded signatures. A
> subsequent aggregation module enriches these representations, followed by a
> final semantic compression stage that utilizes a compact classification head
> with self-distillation to learn maximally task-relevant and discriminative
> embeddings. We instantiate KINN in both CNN (0.7M) and Vision Transformer
> (0.95M) variants. Extensive evaluations on five SAR benchmarks confirm that
> KINN establishes a state-of-the-art in parameter-efficient recognition,
> offering exceptional generalization in data-scarce and out-of-distribution
> scenarios and tangible interpretability, thereby providing an effective
> solution to the representation trilemma and offering a new path for trustworthy
> AI in SAR image analysis.


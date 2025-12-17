---
layout: default
title: Purrturbed but Stable: Human-Cat Invariant Representations Across CNNs, ViTs and Self-Supervised ViTs
---

# Purrturbed but Stable: Human-Cat Invariant Representations Across CNNs, ViTs and Self-Supervised ViTs

**arXiv**: [2511.02404v1](https://arxiv.org/abs/2511.02404) | [PDF](https://arxiv.org/pdf/2511.02404.pdf)

**作者**: Arya Shah, Vaibhav Tripathi

---

## 💡 一句话要点

**提出统一基准评估猫与人类视觉表征对齐，发现自监督ViT在跨物种对齐中表现最佳**

**关键词**: `跨物种视觉对齐` `表征相似性分析` `自监督视觉Transformer` `卷积神经网络` `视觉Transformer基准`

## 📋 核心要点

1. 核心问题：猫与人类眼部解剖差异如何影响视觉表征对齐，尤其在跨物种场景中
2. 方法要点：使用冻结编码器基准，结合CKA和RSA分析多种模型表征相似性
3. 实验或效果：DINO ViT-B/16对齐度最高，自监督ViT优于CNN和窗口Transformer

## 📄 摘要（原文）

> Cats and humans differ in ocular anatomy. Most notably, Felis Catus (domestic
> cats) have vertically elongated pupils linked to ambush predation; yet, how
> such specializations manifest in downstream visual representations remains
> incompletely understood. We present a unified, frozen-encoder benchmark that
> quantifies feline-human cross-species representational alignment in the wild,
> across convolutional networks, supervised Vision Transformers, windowed
> transformers, and self-supervised ViTs (DINO), using layer-wise Centered Kernel
> Alignment (linear and RBF) and Representational Similarity Analysis, with
> additional distributional and stability tests reported in the paper. Across
> models, DINO ViT-B/16 attains the most substantial alignment (mean CKA-RBF
> $\approx0.814$, mean CKA-linear $\approx0.745$, mean RSA $\approx0.698$),
> peaking at early blocks, indicating that token-level self-supervision induces
> early-stage features that bridge species-specific statistics. Supervised ViTs
> are competitive on CKA yet show weaker geometric correspondence than DINO
> (e.g., ViT-B/16 RSA $\approx0.53$ at block8; ViT-L/16 $\approx0.47$ at
> block14), revealing depth-dependent divergences between similarity and
> representational geometry. CNNs remain strong baselines but below plain ViTs on
> alignment, and windowed transformers underperform plain ViTs, implicating
> architectural inductive biases in cross-species alignment. Results indicate
> that self-supervision coupled with ViT inductive biases yields representational
> geometries that more closely align feline and human visual systems than widely
> used CNNs and windowed Transformers, providing testable neuroscientific
> hypotheses about where and how cross-species visual computations converge. We
> release our code and dataset for reference and reproducibility.


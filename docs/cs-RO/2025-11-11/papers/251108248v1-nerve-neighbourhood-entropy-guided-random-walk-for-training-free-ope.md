---
layout: default
title: NERVE: Neighbourhood & Entropy-guided Random-walk for training free open-Vocabulary sEgmentation
---

# NERVE: Neighbourhood & Entropy-guided Random-walk for training free open-Vocabulary sEgmentation

**arXiv**: [2511.08248v1](https://arxiv.org/abs/2511.08248) | [PDF](https://arxiv.org/pdf/2511.08248.pdf)

**作者**: Kunal Mahatha, Jose Dolz, Christian Desrosiers

---

## 💡 一句话要点

**提出NERVE方法以解决开放词汇语义分割中训练免费方法的局限性**

**关键词**: `开放词汇语义分割` `训练免费方法` `随机游走优化` `自注意力图` `零样本学习` `语义分割基准`

## 📋 核心要点

1. 现有方法依赖计算昂贵的亲和力优化和固定高斯核，导致局部平滑性不足
2. NERVE结合全局与局部信息，利用自注意力图进行随机游走优化亲和力
3. 在7个基准测试中实现零样本分割SOTA性能，无需后处理如CRF或PAMR

## 📄 摘要（原文）

> Despite recent advances in Open-Vocabulary Semantic Segmentation (OVSS), existing training-free methods face several limitations: use of computationally expensive affinity refinement strategies, ineffective fusion of transformer attention maps due to equal weighting or reliance on fixed-size Gaussian kernels to reinforce local spatial smoothness, enforcing isotropic neighborhoods. We propose a strong baseline for training-free OVSS termed as NERVE (Neighbourhood \& Entropy-guided Random-walk for open-Vocabulary sEgmentation), which uniquely integrates global and fine-grained local information, exploiting the neighbourhood structure from the self-attention layer of a stable diffusion model. We also introduce a stochastic random walk for refining the affinity rather than relying on fixed-size Gaussian kernels for local context. This spatial diffusion process encourages propagation across connected and semantically related areas, enabling it to effectively delineate objects with arbitrary shapes. Whereas most existing approaches treat self-attention maps from different transformer heads or layers equally, our method uses entropy-based uncertainty to select the most relevant maps. Notably, our method does not require any conventional post-processing techniques like Conditional Random Fields (CRF) or Pixel-Adaptive Mask Refinement (PAMR). Experiments are performed on 7 popular semantic segmentation benchmarks, yielding an overall state-of-the-art zero-shot segmentation performance, providing an effective approach to open-vocabulary semantic segmentation.


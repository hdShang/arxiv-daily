---
layout: default
title: Alpha Divergence Losses for Biometric Verification
---

# Alpha Divergence Losses for Biometric Verification

**arXiv**: [2511.13621v1](https://arxiv.org/abs/2511.13621) | [PDF](https://arxiv.org/pdf/2511.13621.pdf)

**作者**: Dimitrios Koutsianos, Ladislav Mosner, Yannis Panagakis, Themos Stafylakis

---

## 💡 一句话要点

**提出基于α-散度的Q-Margin和A3M损失函数，提升生物特征验证性能**

**关键词**: `生物特征验证` `α-散度损失` `角度间隔` `人脸验证` `说话人验证` `训练稳定性`

## 📋 核心要点

1. 核心问题：α-散度损失难以集成角度间隔，影响人脸和说话人验证性能
2. 方法要点：通过参考度量或logits集成间隔，并解决A3M训练不稳定性
3. 实验或效果：在IJB-B、IJB-C和VoxCeleb基准上显著提升性能，尤其在低误接受率下

## 📄 摘要（原文）

> Performance in face and speaker verification is largely driven by margin based softmax losses like CosFace and ArcFace. Recently introduced $α$-divergence loss functions offer a compelling alternative, particularly for their ability to induce sparse solutions (when $α>1$). However, integrating an angular margin-crucial for verification tasks-is not straightforward. We find this integration can be achieved in at least two distinct ways: via the reference measure (prior probabilities) or via the logits (unnormalized log-likelihoods). In this paper, we explore both pathways, deriving two novel margin-based $α$-divergence losses: Q-Margin (margin in the reference measure) and A3M (margin in the logits). We identify and address a critical training instability in A3M-caused by the interplay of penalized logits and sparsity-with a simple yet effective prototype re-initialization strategy. Our methods achieve significant performance gains on the challenging IJB-B and IJB-C face verification benchmarks. We demonstrate similarly strong performance in speaker verification on VoxCeleb. Crucially, our models significantly outperform strong baselines at low false acceptance rates (FAR). This capability is crucial for practical high-security applications, such as banking authentication, when minimizing false authentications is paramount.


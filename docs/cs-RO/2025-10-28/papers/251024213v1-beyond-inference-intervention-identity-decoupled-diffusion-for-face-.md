---
layout: default
title: Beyond Inference Intervention: Identity-Decoupled Diffusion for Face Anonymization
---

# Beyond Inference Intervention: Identity-Decoupled Diffusion for Face Anonymization

**arXiv**: [2510.24213v1](https://arxiv.org/abs/2510.24213) | [PDF](https://arxiv.org/pdf/2510.24213.pdf)

**作者**: Haoxin Yang, Yihong Lin, Jingdan Kang, Xuemiao Xu, Yue Li, Cheng Xu, Shengfeng He

---

## 💡 一句话要点

**提出ID²Face框架以解决人脸匿名化中身份与非身份属性纠缠问题**

**关键词**: `人脸匿名化` `扩散模型` `身份解耦` `潜在空间学习` `推理优化`

## 📋 核心要点

1. 核心问题：现有扩散模型依赖推理时干预，导致分布偏移和属性纠缠，降低视觉保真度。
2. 方法要点：设计条件扩散模型，通过身份解耦潜在重组器实现身份与非身份属性的显式解缠。
3. 实验或效果：ID²Face在视觉质量、身份抑制和效用保持方面优于现有方法。

## 📄 摘要（原文）

> Face anonymization aims to conceal identity information while preserving
> non-identity attributes. Mainstream diffusion models rely on inference-time
> interventions such as negative guidance or energy-based optimization, which are
> applied post-training to suppress identity features. These interventions often
> introduce distribution shifts and entangle identity with non-identity
> attributes, degrading visual fidelity and data utility. To address this, we
> propose \textbf{ID\textsuperscript{2}Face}, a training-centric anonymization
> framework that removes the need for inference-time optimization. The rationale
> of our method is to learn a structured latent space where identity and
> non-identity information are explicitly disentangled, enabling direct and
> controllable anonymization at inference. To this end, we design a conditional
> diffusion model with an identity-masked learning scheme. An Identity-Decoupled
> Latent Recomposer uses an Identity Variational Autoencoder to model identity
> features, while non-identity attributes are extracted from same-identity pairs
> and aligned through bidirectional latent alignment. An Identity-Guided Latent
> Harmonizer then fuses these representations via soft-gating conditioned on
> noisy feature prediction. The model is trained with a recomposition-based
> reconstruction loss to enforce disentanglement. At inference, anonymization is
> achieved by sampling a random identity vector from the learned identity space.
> To further suppress identity leakage, we introduce an Orthogonal Identity
> Mapping strategy that enforces orthogonality between sampled and source
> identity vectors. Experiments demonstrate that ID\textsuperscript{2}Face
> outperforms existing methods in visual quality, identity suppression, and
> utility preservation.


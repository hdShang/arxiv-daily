---
layout: default
title: UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions
---

# UniAVGen: Unified Audio and Video Generation with Asymmetric Cross-Modal Interactions

**arXiv**: [2511.03334v1](https://arxiv.org/abs/2511.03334) | [PDF](https://arxiv.org/pdf/2511.03334.pdf)

**作者**: Guozhen Zhang, Zixiang Zhou, Teng Hu, Ziqiao Peng, Youliang Zhang, Yi Chen, Yuan Zhou, Qinglin Lu, Limin Wang

---

## 💡 一句话要点

**提出UniAVGen框架以解决音视频生成中的跨模态同步与语义一致性问题**

**关键词**: `音视频生成` `跨模态交互` `扩散变换器` `唇部同步` `语义一致性` `联合合成`

## 📋 核心要点

1. 现有方法因跨模态建模不足，导致唇部同步和语义一致性差
2. 采用双分支扩散变换器与不对称跨模态交互机制，增强时空对齐
3. 实验显示，训练样本少但音视频同步、音色和情感一致性更优

## 📄 摘要（原文）

> Due to the lack of effective cross-modal modeling, existing open-source
> audio-video generation methods often exhibit compromised lip synchronization
> and insufficient semantic consistency. To mitigate these drawbacks, we propose
> UniAVGen, a unified framework for joint audio and video generation. UniAVGen is
> anchored in a dual-branch joint synthesis architecture, incorporating two
> parallel Diffusion Transformers (DiTs) to build a cohesive cross-modal latent
> space. At its heart lies an Asymmetric Cross-Modal Interaction mechanism, which
> enables bidirectional, temporally aligned cross-attention, thus ensuring
> precise spatiotemporal synchronization and semantic consistency. Furthermore,
> this cross-modal interaction is augmented by a Face-Aware Modulation module,
> which dynamically prioritizes salient regions in the interaction process. To
> enhance generative fidelity during inference, we additionally introduce
> Modality-Aware Classifier-Free Guidance, a novel strategy that explicitly
> amplifies cross-modal correlation signals. Notably, UniAVGen's robust joint
> synthesis design enables seamless unification of pivotal audio-video tasks
> within a single model, such as joint audio-video generation and continuation,
> video-to-audio dubbing, and audio-driven video synthesis. Comprehensive
> experiments validate that, with far fewer training samples (1.3M vs. 30.1M),
> UniAVGen delivers overall advantages in audio-video synchronization, timbre
> consistency, and emotion consistency.


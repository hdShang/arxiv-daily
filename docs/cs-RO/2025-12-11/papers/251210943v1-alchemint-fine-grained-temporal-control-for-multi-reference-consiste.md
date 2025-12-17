---
layout: default
title: AlcheMinT: Fine-grained Temporal Control for Multi-Reference Consistent Video Generation
---

# AlcheMinT: Fine-grained Temporal Control for Multi-Reference Consistent Video Generation

**arXiv**: [2512.10943v1](https://arxiv.org/abs/2512.10943) | [PDF](https://arxiv.org/pdf/2512.10943.pdf)

**作者**: Sharath Girish, Viacheslav Ivanov, Tsai-Shien Chen, Hao Chen, Aliaksandr Siarohin, Sergey Tulyakov

---

## 💡 一句话要点

**提出AlcheMinT框架，通过时间戳条件实现多主体视频生成的细粒度时序控制**

**关键词**: `视频生成` `时序控制` `主题驱动` `扩散模型` `多主体一致性`

## 📋 核心要点

1. 现有主题驱动视频生成方法缺乏对主体出现和消失的细粒度时序控制
2. 引入新颖位置编码机制，结合时间戳和主体描述文本，实现时序区间编码
3. 实验表明AlcheMinT在保持视觉质量的同时，首次实现视频内多主体生成的精确时序控制

## 📄 摘要（原文）

> Recent advances in subject-driven video generation with large diffusion models have enabled personalized content synthesis conditioned on user-provided subjects. However, existing methods lack fine-grained temporal control over subject appearance and disappearance, which are essential for applications such as compositional video synthesis, storyboarding, and controllable animation. We propose AlcheMinT, a unified framework that introduces explicit timestamps conditioning for subject-driven video generation. Our approach introduces a novel positional encoding mechanism that unlocks the encoding of temporal intervals, associated in our case with subject identities, while seamlessly integrating with the pretrained video generation model positional embeddings. Additionally, we incorporate subject-descriptive text tokens to strengthen binding between visual identity and video captions, mitigating ambiguity during generation. Through token-wise concatenation, AlcheMinT avoids any additional cross-attention modules and incurs negligible parameter overhead. We establish a benchmark evaluating multiple subject identity preservation, video fidelity, and temporal adherence. Experimental results demonstrate that AlcheMinT achieves visual quality matching state-of-the-art video personalization methods, while, for the first time, enabling precise temporal control over multi-subject generation within videos. Project page is at https://snap-research.github.io/Video-AlcheMinT


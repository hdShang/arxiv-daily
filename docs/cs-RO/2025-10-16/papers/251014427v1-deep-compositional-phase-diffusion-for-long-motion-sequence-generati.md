---
layout: default
title: Deep Compositional Phase Diffusion for Long Motion Sequence Generation
---

# Deep Compositional Phase Diffusion for Long Motion Sequence Generation

**arXiv**: [2510.14427v1](https://arxiv.org/abs/2510.14427) | [PDF](https://arxiv.org/pdf/2510.14427.pdf)

**作者**: Ho Yin Au, Jie Chen, Junkun Jiang, Jingyu Xiang

---

## 💡 一句话要点

**提出组合相位扩散方法以解决长运动序列生成中的过渡不连续问题**

**关键词**: `运动序列生成` `扩散模型` `相位扩散` `组合运动` `过渡连续性` `运动插值`

## 📋 核心要点

1. 核心问题：现有模型生成多语义运动序列时，过渡边界处运动动态不连续，产生突兀伪影。
2. 方法要点：利用SPDM和TPDM在潜在运动频域中逐步融入语义指导和相邻运动相位细节。
3. 实验或效果：框架在生成语义对齐的组合运动序列中表现竞争性，保持相位过渡连续性。

## 📄 摘要（原文）

> Recent research on motion generation has shown significant progress in
> generating semantically aligned motion with singular semantics. However, when
> employing these models to create composite sequences containing multiple
> semantically generated motion clips, they often struggle to preserve the
> continuity of motion dynamics at the transition boundaries between clips,
> resulting in awkward transitions and abrupt artifacts. To address these
> challenges, we present Compositional Phase Diffusion, which leverages the
> Semantic Phase Diffusion Module (SPDM) and Transitional Phase Diffusion Module
> (TPDM) to progressively incorporate semantic guidance and phase details from
> adjacent motion clips into the diffusion process. Specifically, SPDM and TPDM
> operate within the latent motion frequency domain established by the
> pre-trained Action-Centric Motion Phase Autoencoder (ACT-PAE). This allows them
> to learn semantically important and transition-aware phase information from
> variable-length motion clips during training. Experimental results demonstrate
> the competitive performance of our proposed framework in generating
> compositional motion sequences that align semantically with the input
> conditions, while preserving phase transitional continuity between preceding
> and succeeding motion clips. Additionally, motion inbetweening task is made
> possible by keeping the phase parameter of the input motion sequences fixed
> throughout the diffusion process, showcasing the potential for extending the
> proposed framework to accommodate various application scenarios. Codes are
> available at https://github.com/asdryau/TransPhase.


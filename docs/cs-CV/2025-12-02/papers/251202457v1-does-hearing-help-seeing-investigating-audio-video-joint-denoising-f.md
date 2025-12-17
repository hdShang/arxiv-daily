---
layout: default
title: Does Hearing Help Seeing? Investigating Audio-Video Joint Denoising for Video Generation
---

# Does Hearing Help Seeing? Investigating Audio-Video Joint Denoising for Video Generation

**arXiv**: [2512.02457v1](https://arxiv.org/abs/2512.02457) | [PDF](https://arxiv.org/pdf/2512.02457.pdf)

**作者**: Jianzong Wu, Hao Lian, Dachao Hao, Ye Tian, Qingyu Shi, Biaolong Chen, Hao Jiang

---

## 💡 一句话要点

**提出音频-视频联合去噪训练方法，以提升视频生成质量，尤其在复杂运动场景中。**

**关键词**: `音频-视频联合去噪` `视频生成` `跨模态训练` `参数高效架构` `物理世界建模`

## 📋 核心要点

1. 核心问题：音频-视频联合去噪训练是否能提升仅关注视频质量的生成效果。
2. 方法要点：设计参数高效的AVFullDiT架构，结合预训练T2V和T2A模块进行联合去噪。
3. 实验或效果：在大型和物体接触运动子集上，音频-视频联合训练带来视频质量一致提升。

## 📄 摘要（原文）

> Recent audio-video generative systems suggest that coupling modalities benefits not only audio-video synchrony but also the video modality itself. We pose a fundamental question: Does audio-video joint denoising training improve video generation, even when we only care about video quality? To study this, we introduce a parameter-efficient Audio-Video Full DiT (AVFullDiT) architecture that leverages pre-trained text-to-video (T2V) and text-to-audio (T2A) modules for joint denoising. We train (i) a T2AV model with AVFullDiT and (ii) a T2V-only counterpart under identical settings. Our results provide the first systematic evidence that audio-video joint denoising can deliver more than synchrony. We observe consistent improvements on challenging subsets featuring large and object contact motions. We hypothesize that predicting audio acts as a privileged signal, encouraging the model to internalize causal relationships between visual events and their acoustic consequences (e.g., collision $\times$ impact sound), which in turn regularizes video dynamics. Our findings suggest that cross-modal co-training is a promising approach to developing stronger, more physically grounded world models. Code and dataset will be made publicly available.


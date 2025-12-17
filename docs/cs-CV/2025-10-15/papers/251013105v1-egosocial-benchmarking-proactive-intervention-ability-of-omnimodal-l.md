---
layout: default
title: EgoSocial: Benchmarking Proactive Intervention Ability of Omnimodal LLMs via Egocentric Social Interaction Perception
---

# EgoSocial: Benchmarking Proactive Intervention Ability of Omnimodal LLMs via Egocentric Social Interaction Perception

**arXiv**: [2510.13105v1](https://arxiv.org/abs/2510.13105) | [PDF](https://arxiv.org/pdf/2510.13105.pdf)

**作者**: Xijun Wang, Tanay Sharma, Achin Kulshrestha, Abhimitra Meka, Aveek Purohit, Dinesh Manocha

---

## 💡 一句话要点

**提出EgoSocial基准与EgoSoD方法以提升AR/VR中AI的主动干预能力**

**关键词**: `第一人称社交感知` `多模态大语言模型` `主动干预基准` `社交动态建模` `视频问答数据集`

## 📋 核心要点

1. 当前LLMs缺乏从第一人称视角感知社交动态的能力，导致干预时机不当
2. 提出EgoSoD方法，整合多模态线索构建社交图，动态建模交互与参与者
3. 实验显示EgoSoD显著提升干预时机检测性能，如Phi-4提高45.6%

## 📄 摘要（原文）

> As AR/VR technologies become integral to daily life, there's a growing need
> for AI that understands human social dynamics from an egocentric perspective.
> However, current LLMs often lack the social awareness to discern when to
> intervene as AI assistant. This leads to constant, socially unaware responses
> that may disrupt natural conversation and negatively impact user focus. To
> address these limitations, we introduce EgoSocial, a large-scale egocentric
> dataset with 13,500 social video-question pairs, specifically designed to
> benchmark intervention in social interaction perception. We also present an
> in-depth analysis of current omnimodal LLMs (OLLMs) to assess their
> effectiveness in detecting diverse social contextual cues. Experiments show
> that OLLMs still struggle to detect the intervention timing (14.4% for Gemini
> 2.5 Pro). We also propose EgoSoD (EgoSocial Detection), an end-to-end method
> for robustly discerning social dynamics. Informed by our OLLM analysis, EgoSoD
> integrates multimodal contextual cues (e.g., audio and visual cues) into a
> social thinking graph, dynamically modeling participants and interactions. Our
> method proactively detects intervention timing and social interactions,
> precisely determining when to intervene. Our EgoSoD improves Phi-4 by 45.6% and
> Gemini 2.5 Pro by 9.9% on Intervention Timing performance, and improves Phi-4
> by 20.4% and Gemini 2.5 Pro by 6.9% on overall Social Interaction performance.
> We will release the dataset and code soon.


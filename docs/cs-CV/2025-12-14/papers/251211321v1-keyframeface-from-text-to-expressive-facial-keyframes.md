---
layout: default
title: KeyframeFace: From Text to Expressive Facial Keyframes
---

# KeyframeFace: From Text to Expressive Facial Keyframes

**arXiv**: [2512.11321v1](https://arxiv.org/abs/2512.11321) | [PDF](https://arxiv.org/pdf/2512.11321.pdf)

**作者**: Jingchao Wu, Zejian Kang, Haibo Liu, Yuanchen Fei, Xiangru Huang

---

## 💡 一句话要点

**提出KeyframeFace数据集与LLM框架，以解决文本到表情动画的语义与时间结构问题。**

**关键词**: `文本到动画` `面部动画` `关键帧监督` `多模态数据集` `LLM先验` `ARKit系数`

## 📋 核心要点

1. 核心问题：现有方法缺乏语义基础和时间结构，难以从文本生成动态3D面部动画。
2. 方法要点：构建大规模多模态数据集，并利用LLM先验实现可解释的面部运动合成。
3. 实验或效果：通过关键帧监督和ARKit系数，实现高保真、上下文感知的动画生成。

## 📄 摘要（原文）

> Generating dynamic 3D facial animation from natural language requires understanding both temporally structured semantics and fine-grained expression changes. Existing datasets and methods mainly focus on speech-driven animation or unstructured expression sequences and therefore lack the semantic grounding and temporal structures needed for expressive human performance generation. In this work, we introduce KeyframeFace, a large-scale multimodal dataset designed for text-to-animation research through keyframe-level supervision. KeyframeFace provides 2,100 expressive scripts paired with monocular videos, per-frame ARKit coefficients, contextual backgrounds, complex emotions, manually defined keyframes, and multi-perspective annotations based on ARKit coefficients and images via Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs). Beyond the dataset, we propose the first text-to-animation framework that explicitly leverages LLM priors for interpretable facial motion synthesis. This design aligns the semantic understanding capabilities of LLMs with the interpretable structure of ARKit's coefficients, enabling high-fidelity expressive animation. KeyframeFace and our LLM-based framework together establish a new foundation for interpretable, keyframe-guided, and context-aware text-to-animation. Code and data are available at https://github.com/wjc12345123/KeyframeFace.


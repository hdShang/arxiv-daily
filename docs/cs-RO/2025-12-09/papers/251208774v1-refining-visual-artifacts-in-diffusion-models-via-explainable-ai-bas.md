---
layout: default
title: Refining Visual Artifacts in Diffusion Models via Explainable AI-based Flaw Activation Maps
---

# Refining Visual Artifacts in Diffusion Models via Explainable AI-based Flaw Activation Maps

**arXiv**: [2512.08774v1](https://arxiv.org/abs/2512.08774) | [PDF](https://arxiv.org/pdf/2512.08774.pdf)

**作者**: Seoyeon Lee, Gwangyeol Yu, Chaewon Kim, Jonghyuk Park

---

## 💡 一句话要点

**提出基于可解释AI的自精炼扩散框架，以检测并修复扩散模型中的视觉伪影和不真实区域。**

**关键词**: `扩散模型` `图像合成` `可解释AI` `缺陷检测` `图像精炼`

## 📋 核心要点

1. 扩散模型在图像合成中面临伪影和不真实区域的关键挑战。
2. 利用可解释AI生成缺陷激活图，在正向过程放大噪声，反向过程聚焦修复。
3. 在多种模型和任务上实现Fréchet inception距离提升，最高达27.3%。

## 📄 摘要（原文）

> Diffusion models have achieved remarkable success in image synthesis. However, addressing artifacts and unrealistic regions remains a critical challenge. We propose self-refining diffusion, a novel framework that enhances image generation quality by detecting these flaws. The framework employs an explainable artificial intelligence (XAI)-based flaw highlighter to produce flaw activation maps (FAMs) that identify artifacts and unrealistic regions. These FAMs improve reconstruction quality by amplifying noise in flawed regions during the forward process and by focusing on these regions during the reverse process. The proposed approach achieves up to a 27.3% improvement in Fréchet inception distance across various diffusion-based models, demonstrating consistently strong performance on diverse datasets. It also shows robust effectiveness across different tasks, including image generation, text-to-image generation, and inpainting. These results demonstrate that explainable AI techniques can extend beyond interpretability to actively contribute to image refinement. The proposed framework offers a versatile and effective approach applicable to various diffusion models and tasks, significantly advancing the field of image synthesis.


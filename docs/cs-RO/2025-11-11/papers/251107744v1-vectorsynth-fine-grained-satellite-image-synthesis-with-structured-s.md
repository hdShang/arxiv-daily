---
layout: default
title: VectorSynth: Fine-Grained Satellite Image Synthesis with Structured Semantics
---

# VectorSynth: Fine-Grained Satellite Image Synthesis with Structured Semantics

**arXiv**: [2511.07744v1](https://arxiv.org/abs/2511.07744) | [PDF](https://arxiv.org/pdf/2511.07744.pdf)

**作者**: Daniel Cher, Brian Wei, Srikumar Sastry, Nathan Jacobs

---

## 💡 一句话要点

**提出VectorSynth框架，基于扩散模型实现多边形标注下的精细卫星图像合成。**

**关键词**: `卫星图像合成` `扩散模型` `语义向量几何` `视觉语言对齐` `空间编辑` `像素级嵌入`

## 📋 核心要点

1. 核心问题：现有文本或布局条件模型难以实现像素级精确的卫星图像合成与编辑。
2. 方法要点：通过视觉语言对齐模块生成像素级嵌入，结合语义向量几何指导图像生成。
3. 实验或效果：在语义保真度和结构真实感上优于先前方法，支持交互式空间编辑。

## 📄 摘要（原文）

> We introduce VectorSynth, a diffusion-based framework for pixel-accurate satellite image synthesis conditioned on polygonal geographic annotations with semantic attributes. Unlike prior text- or layout-conditioned models, VectorSynth learns dense cross-modal correspondences that align imagery and semantic vector geometry, enabling fine-grained, spatially grounded edits. A vision language alignment module produces pixel-level embeddings from polygon semantics; these embeddings guide a conditional image generation framework to respect both spatial extents and semantic cues. VectorSynth supports interactive workflows that mix language prompts with geometry-aware conditioning, allowing rapid what-if simulations, spatial edits, and map-informed content generation. For training and evaluation, we assemble a collection of satellite scenes paired with pixel-registered polygon annotations spanning diverse urban scenes with both built and natural features. We observe strong improvements over prior methods in semantic fidelity and structural realism, and show that our trained vision language model demonstrates fine-grained spatial grounding. The code and data are available at https://github.com/mvrl/VectorSynth.


---
layout: default
title: Taming Identity Consistency and Prompt Diversity in Diffusion Models via Latent Concatenation and Masked Conditional Flow Matching
---

# Taming Identity Consistency and Prompt Diversity in Diffusion Models via Latent Concatenation and Masked Conditional Flow Matching

**arXiv**: [2511.08061v1](https://arxiv.org/abs/2511.08061) | [PDF](https://arxiv.org/pdf/2511.08061.pdf)

**作者**: Aditi Singhania, Arushi Jain, Krutik Malani, Riddhi Dhawan, Souymodip Chakraborty, Vineet Batra, Ankit Phogat

---

## 💡 一句话要点

**提出潜在连接与掩码条件流匹配方法，以解决主题驱动图像生成中身份一致性与提示多样性的权衡问题。**

**关键词**: `主题驱动图像生成` `扩散模型` `潜在连接` `条件流匹配` `数据蒸馏` `图像质量评估`

## 📋 核心要点

1. 核心问题：主题驱动图像生成中，身份一致性与提示多样性存在根本性权衡。
2. 方法要点：使用LoRA微调扩散模型，结合潜在连接策略和掩码条件流匹配目标。
3. 实验或效果：引入蒸馏数据策展框架和CHARIS评估，提升生成质量和多样性。

## 📄 摘要（原文）

> Subject-driven image generation aims to synthesize novel depictions of a specific subject across diverse contexts while preserving its core identity features. Achieving both strong identity consistency and high prompt diversity presents a fundamental trade-off. We propose a LoRA fine-tuned diffusion model employing a latent concatenation strategy, which jointly processes reference and target images, combined with a masked Conditional Flow Matching (CFM) objective. This approach enables robust identity preservation without architectural modifications. To facilitate large-scale training, we introduce a two-stage Distilled Data Curation Framework: the first stage leverages data restoration and VLM-based filtering to create a compact, high-quality seed dataset from diverse sources; the second stage utilizes these curated examples for parameter-efficient fine-tuning, thus scaling the generation capability across various subjects and contexts. Finally, for filtering and quality assessment, we present CHARIS, a fine-grained evaluation framework that performs attribute-level comparisons along five key axes: identity consistency, prompt adherence, region-wise color fidelity, visual quality, and transformation diversity.


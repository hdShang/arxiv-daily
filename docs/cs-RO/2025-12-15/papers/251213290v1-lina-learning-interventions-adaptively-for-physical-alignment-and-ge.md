---
layout: default
title: LINA: Learning INterventions Adaptively for Physical Alignment and Generalization in Diffusion Models
---

# LINA: Learning INterventions Adaptively for Physical Alignment and Generalization in Diffusion Models

**arXiv**: [2512.13290v1](https://arxiv.org/abs/2512.13290) | [PDF](https://arxiv.org/pdf/2512.13290.pdf)

**作者**: Shu Yu, Chaochao Lu

---

## 💡 一句话要点

**提出LINA框架，通过自适应学习干预解决扩散模型物理对齐和分布外指令遵循问题。**

**关键词**: `扩散模型` `物理对齐` `因果推理` `自适应干预` `分布外指令遵循` `因果场景图`

## 📋 核心要点

1. 核心问题：扩散模型在物理对齐和分布外指令遵循上表现不佳，源于因果方向学习和因子解耦的失败。
2. 方法要点：引入因果场景图和物理对齐探测数据集进行诊断，基于洞察设计自适应干预预测框架，结合提示与视觉潜在空间引导及因果感知去噪调度。
3. 实验或效果：在图像和视频扩散模型中实现物理对齐和分布外指令遵循，在因果生成任务和Winoground数据集上达到最先进性能。

## 📄 摘要（原文）

> Diffusion models (DMs) have achieved remarkable success in image and video generation. However, they still struggle with (1) physical alignment and (2) out-of-distribution (OOD) instruction following. We argue that these issues stem from the models' failure to learn causal directions and to disentangle causal factors for novel recombination. We introduce the Causal Scene Graph (CSG) and the Physical Alignment Probe (PAP) dataset to enable diagnostic interventions. This analysis yields three key insights. First, DMs struggle with multi-hop reasoning for elements not explicitly determined in the prompt. Second, the prompt embedding contains disentangled representations for texture and physics. Third, visual causal structure is disproportionately established during the initial, computationally limited denoising steps. Based on these findings, we introduce LINA (Learning INterventions Adaptively), a novel framework that learns to predict prompt-specific interventions, which employs (1) targeted guidance in the prompt and visual latent spaces, and (2) a reallocated, causality-aware denoising schedule. Our approach enforces both physical alignment and OOD instruction following in image and video DMs, achieving state-of-the-art performance on challenging causal generation tasks and the Winoground dataset. Our project page is at https://opencausalab.github.io/LINA.


---
layout: default
title: Bi-Erasing: A Bidirectional Framework for Concept Removal in Diffusion Models
---

# Bi-Erasing: A Bidirectional Framework for Concept Removal in Diffusion Models

**arXiv**: [2512.13039v1](https://arxiv.org/abs/2512.13039) | [PDF](https://arxiv.org/pdf/2512.13039.pdf)

**作者**: Hao Chen, Yiwei Wang, Songze Li

---

## 💡 一句话要点

**提出双向图像引导概念擦除框架以解决扩散模型中概念移除与生成质量的平衡问题**

**关键词**: `扩散模型` `概念擦除` `文本到图像生成` `安全增强` `双向优化` `图像引导`

## 📋 核心要点

1. 现有概念擦除方法多为单向策略，难以平衡移除效果与生成质量
2. 提出双向框架，通过负分支抑制有害概念、正分支引导安全替代，同时优化互补方向
3. 实验表明该方法在概念移除效果与视觉保真度平衡上优于基线方法

## 📄 摘要（原文）

> Concept erasure, which fine-tunes diffusion models to remove undesired or harmful visual concepts, has become a mainstream approach to mitigating unsafe or illegal image generation in text-to-image models.However, existing removal methods typically adopt a unidirectional erasure strategy by either suppressing the target concept or reinforcing safe alternatives, making it difficult to achieve a balanced trade-off between concept removal and generation quality. To address this limitation, we propose a novel Bidirectional Image-Guided Concept Erasure (Bi-Erasing) framework that performs concept suppression and safety enhancement simultaneously. Specifically, based on the joint representation of text prompts and corresponding images, Bi-Erasing introduces two decoupled image branches: a negative branch responsible for suppressing harmful semantics and a positive branch providing visual guidance for safe alternatives. By jointly optimizing these complementary directions, our approach achieves a balance between erasure efficacy and generation usability. In addition, we apply mask-based filtering to the image branches to prevent interference from irrelevant content during the erasure process. Across extensive experiment evaluations, the proposed Bi-Erasing outperforms baseline methods in balancing concept removal effectiveness and visual fidelity.


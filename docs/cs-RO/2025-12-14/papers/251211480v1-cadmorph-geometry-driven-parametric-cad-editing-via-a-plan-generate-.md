---
layout: default
title: CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop
---

# CADMorph: Geometry-Driven Parametric CAD Editing via a Plan-Generate-Verify Loop

**arXiv**: [2512.11480v1](https://arxiv.org/abs/2512.11480) | [PDF](https://arxiv.org/pdf/2512.11480.pdf)

**作者**: Weijian Ma, Shizhao Sun, Ruiyu Wang, Jiang Bian

---

## 💡 一句话要点

**提出CADMorph框架，通过计划-生成-验证循环解决几何驱动参数化CAD编辑问题**

**关键词**: `参数化CAD编辑` `几何驱动设计` `计划-生成-验证框架` `预训练模型` `形状保真度` `数据稀缺处理`

## 📋 核心要点

1. 核心问题：几何驱动参数化CAD编辑需在数据稀缺下同步调整几何形状与参数序列，保持结构、语义和保真度
2. 方法要点：利用预训练P2S和MPP模型，通过计划、生成、验证三阶段迭代编辑，无需三元组数据训练
3. 实验或效果：超越GPT-4o和专用基线，支持迭代编辑和逆向工程增强等应用

## 📄 摘要（原文）

> A Computer-Aided Design (CAD) model encodes an object in two coupled forms: a parametric construction sequence and its resulting visible geometric shape. During iterative design, adjustments to the geometric shape inevitably require synchronized edits to the underlying parametric sequence, called geometry-driven parametric CAD editing. The task calls for 1) preserving the original sequence's structure, 2) ensuring each edit's semantic validity, and 3) maintaining high shape fidelity to the target shape, all under scarce editing data triplets. We present CADMorph, an iterative plan-generate-verify framework that orchestrates pretrained domain-specific foundation models during inference: a parameter-to-shape (P2S) latent diffusion model and a masked-parameter-prediction (MPP) model. In the planning stage, cross-attention maps from the P2S model pinpoint the segments that need modification and offer editing masks. The MPP model then infills these masks with semantically valid edits in the generation stage. During verification, the P2S model embeds each candidate sequence in shape-latent space, measures its distance to the target shape, and selects the closest one. The three stages leverage the inherent geometric consciousness and design knowledge in pretrained priors, and thus tackle structure preservation, semantic validity, and shape fidelity respectively. Besides, both P2S and MPP models are trained without triplet data, bypassing the data-scarcity bottleneck. CADMorph surpasses GPT-4o and specialized CAD baselines, and supports downstream applications such as iterative editing and reverse-engineering enhancement.


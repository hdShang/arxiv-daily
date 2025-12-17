---
layout: default
title: Bridging Fidelity-Reality with Controllable One-Step Diffusion for Image Super-Resolution
---

# Bridging Fidelity-Reality with Controllable One-Step Diffusion for Image Super-Resolution

**arXiv**: [2512.14061v1](https://arxiv.org/abs/2512.14061) | [PDF](https://arxiv.org/pdf/2512.14061.pdf)

**作者**: Hao Chen, Junyang Chen, Jinshan Pan, Jiangxin Dong

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://github.com/Chanson94/CODSR

---

## 💡 一句话要点

**提出CODSR可控一步扩散网络，通过LQ引导特征调制、区域自适应生成先验激活和文本匹配指导，解决图像超分辨率中保真度与感知质量平衡问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `图像超分辨率` `扩散模型` `一步推理` `可控生成` `特征调制` `生成先验激活` `文本指导` `保真度-感知平衡`

## 📋 核心要点

1. 现有基于扩散的一步超分辨率方法存在保真度不足、生成先验激活不充分和文本提示与语义区域错位三大问题，限制了性能提升。
2. CODSR通过LQ引导特征调制模块、区域自适应生成先验激活和文本匹配指导策略，整合原始信息、增强感知并优化文本条件，实现可控超分辨率。
3. 实验显示CODSR在一步推理下达到卓越感知质量和竞争性保真度，显著优于现有方法，验证了其有效性和效率。

## 📝 摘要（中文）

近年来，基于扩散的一步方法在图像超分辨率领域取得了显著进展，但仍受限于三个关键问题：(1) 由于低质量输入压缩编码导致的信息损失，造成保真度性能下降；(2) 生成先验的区域判别性激活不足；(3) 文本提示与其对应语义区域之间的错位。为解决这些限制，我们提出了CODSR，一种用于图像超分辨率的可控一步扩散网络。首先，我们提出了一个LQ引导的特征调制模块，利用低质量输入的原始未压缩信息为扩散过程提供高保真度条件。然后，我们开发了一种区域自适应的生成先验激活方法，以在不牺牲局部结构保真度的情况下有效增强感知丰富度。最后，我们采用文本匹配指导策略，充分利用文本提示的条件潜力。大量实验表明，CODSR在高效一步推理下，相比最先进方法实现了卓越的感知质量和有竞争力的保真度。

## 🔬 方法详解

CODSR是一个可控的一步扩散网络，整体框架基于扩散模型，通过一步推理实现图像超分辨率。关键技术创新包括：LQ引导特征调制模块，直接利用低质量输入的未压缩信息提供高保真度条件；区域自适应生成先验激活方法，动态调整生成先验的激活强度以平衡感知丰富度和局部结构；文本匹配指导策略，确保文本提示与图像语义区域对齐。与现有方法的主要区别在于，它综合解决了信息损失、先验激活不足和文本错位问题，通过模块化设计实现更精确的条件控制和性能提升。

## 📊 实验亮点

CODSR在标准数据集上进行了广泛实验，结果显示其感知质量显著优于现有一步扩散方法，同时保真度指标保持竞争力，在一步推理下实现了高效与高质量的平衡，验证了所提模块的有效性。

## 🎯 应用场景

该研究可应用于图像增强、视频超分辨率、医学影像分析和数字媒体修复等领域，提升低质量图像的视觉质量和细节还原能力，具有实际价值如改善监控视频清晰度、增强老旧照片或优化遥感图像。

## 📄 摘要（原文）

> Recent diffusion-based one-step methods have shown remarkable progress in the field of image super-resolution, yet they remain constrained by three critical limitations: (1) inferior fidelity performance caused by the information loss from compression encoding of low-quality (LQ) inputs; (2) insufficient region-discriminative activation of generative priors; (3) misalignment between text prompts and their corresponding semantic regions. To address these limitations, we propose CODSR, a controllable one-step diffusion network for image super-resolution. First, we propose an LQ-guided feature modulation module that leverages original uncompressed information from LQ inputs to provide high-fidelity conditioning for the diffusion process. We then develop a region-adaptive generative prior activation method to effectively enhance perceptual richness without sacrificing local structural fidelity. Finally, we employ a text-matching guidance strategy to fully harness the conditioning potential of text prompts. Extensive experiments demonstrate that CODSR achieves superior perceptual quality and competitive fidelity compared with state-of-the-art methods with efficient one-step inference.


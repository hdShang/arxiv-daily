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

**提出CODSR可控一步扩散网络，通过LQ引导特征调制、区域自适应生成先验激活和文本匹配指导，解决图像超分辨率中保真度不足、生成先验激活不充分和文本提示错位问题。**

**关键词**: `图像超分辨率` `扩散模型` `一步推理` `保真度增强` `生成先验激活` `文本指导` `可控网络` `区域自适应`

## 📋 核心要点

1. 现有一步扩散方法在图像超分辨率中面临保真度不足、生成先验激活不充分和文本提示错位三大挑战。
2. CODSR通过LQ引导特征调制、区域自适应生成先验激活和文本匹配指导，提升保真度和感知质量。
3. 实验显示CODSR在一步推理下实现卓越感知质量和有竞争力保真度，优于现有方法。

## 📝 摘要（中文）

近期基于扩散的一步方法在图像超分辨率领域取得了显著进展，但仍受限于三个关键问题：(1) 由于低质量输入压缩编码导致的信息损失，造成保真度性能不佳；(2) 生成先验的区域判别性激活不足；(3) 文本提示与其对应语义区域之间的错位。为解决这些限制，我们提出了CODSR，一种可控的一步扩散网络用于图像超分辨率。首先，我们提出了一个LQ引导的特征调制模块，利用低质量输入的原始未压缩信息为扩散过程提供高保真度条件。然后，我们开发了一种区域自适应的生成先验激活方法，以有效增强感知丰富性而不牺牲局部结构保真度。最后，我们采用文本匹配指导策略，充分利用文本提示的条件潜力。大量实验表明，CODSR在高效一步推理下，相比最先进方法实现了卓越的感知质量和有竞争力的保真度。

## 🔬 方法详解

CODSR是一个可控的一步扩散网络，整体框架基于扩散模型，通过一步推理实现图像超分辨率。关键技术创新包括：LQ引导特征调制模块，利用低质量输入的未压缩信息增强保真度；区域自适应生成先验激活方法，针对不同区域调整生成先验以平衡感知丰富性和结构保真度；文本匹配指导策略，优化文本提示与语义区域的对应关系。与现有方法的主要区别在于，CODSR综合解决了保真度损失、先验激活不足和文本错位问题，通过模块化设计实现高效可控的超分辨率。

## 📊 实验亮点

CODSR在一步推理下，相比最先进方法，实现了卓越的感知质量和有竞争力的保真度，实验验证了其在效率和性能上的优势，特别是在处理复杂场景时表现出色。

## 🎯 应用场景

该研究可应用于图像增强、视频修复、医学成像和数字媒体处理等领域，提升低分辨率图像的视觉质量和细节恢复能力，具有实际价值如改善监控视频清晰度或增强历史照片。

## 📄 摘要（原文）

> Recent diffusion-based one-step methods have shown remarkable progress in the field of image super-resolution, yet they remain constrained by three critical limitations: (1) inferior fidelity performance caused by the information loss from compression encoding of low-quality (LQ) inputs; (2) insufficient region-discriminative activation of generative priors; (3) misalignment between text prompts and their corresponding semantic regions. To address these limitations, we propose CODSR, a controllable one-step diffusion network for image super-resolution. First, we propose an LQ-guided feature modulation module that leverages original uncompressed information from LQ inputs to provide high-fidelity conditioning for the diffusion process. We then develop a region-adaptive generative prior activation method to effectively enhance perceptual richness without sacrificing local structural fidelity. Finally, we employ a text-matching guidance strategy to fully harness the conditioning potential of text prompts. Extensive experiments demonstrate that CODSR achieves superior perceptual quality and competitive fidelity compared with state-of-the-art methods with efficient one-step inference.


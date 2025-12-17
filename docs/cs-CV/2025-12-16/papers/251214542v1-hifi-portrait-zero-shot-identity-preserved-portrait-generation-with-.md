---
layout: default
title: HiFi-Portrait: Zero-shot Identity-preserved Portrait Generation with High-fidelity Multi-face Fusion
---

# HiFi-Portrait: Zero-shot Identity-preserved Portrait Generation with High-fidelity Multi-face Fusion

**arXiv**: [2512.14542v1](https://arxiv.org/abs/2512.14542) | [PDF](https://arxiv.org/pdf/2512.14542.pdf)

**作者**: Yifang Xu, Benxiang Zhai, Yunzhuo Sun, Ming Li, Yang Li, Sidan Du

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Accepted by CVPR 2025

---

## 💡 一句话要点

**提出HiFi-Portrait方法，通过高保真多脸融合解决零样本身份保持肖像生成中的保真度和属性控制问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `身份保持肖像生成` `零样本学习` `高保真融合` `多脸特征` `3D面部地标` `扩散模型` `可控生成` `SDXL兼容`

## 📋 核心要点

1. 现有方法在使用多张参考图像时，生成肖像保真度低且难以精确控制面部属性。
2. 引入面部精炼器和地标生成器获取细粒度特征，设计HiFi-Net融合特征并与地标对齐。
3. 实验显示，方法在面部相似性和可控性上超越SOTA，并与SDXL兼容。

## 📝 摘要（中文）

基于扩散技术的进步，身份保持肖像生成（IPG）已取得显著进展，但在使用同一身份的多张参考图像时，现有方法通常生成保真度较低的肖像，且难以精确定制面部属性。为解决这些问题，本文提出HiFi-Portrait，一种用于零样本肖像生成的高保真方法。具体而言，我们首先引入面部精炼器和地标生成器，以获取细粒度的多脸特征和3D感知的面部地标，这些地标包括参考身份和目标属性。然后，我们设计HiFi-Net来融合多脸特征并与地标对齐，从而提高身份保真度和面部控制。此外，我们开发了一个自动化流程来构建基于身份的数据集，用于训练HiFi-Portrait。大量实验结果表明，我们的方法在面部相似性和可控性方面超越了最先进的方法。此外，我们的方法也与之前基于SDXL的工作兼容。

## 🔬 方法详解

HiFi-Portrait的整体框架包括面部精炼器、地标生成器和HiFi-Net。面部精炼器从多张参考图像中提取细粒度特征，地标生成器生成3D感知的面部地标以编码身份和属性信息。HiFi-Net作为核心模块，融合多脸特征并与地标对齐，通过特征融合和地标对齐机制提升身份保真度和控制精度。关键技术创新在于细粒度多脸特征提取和3D感知地标引导的融合策略，与现有方法相比，它更注重高保真度和精确属性控制，而非仅依赖单一参考或粗粒度特征。

## 📊 实验亮点

实验结果表明，HiFi-Portrait在面部相似性和可控性指标上显著超越现有SOTA方法，同时保持与SDXL的兼容性，验证了其高保真和精确控制的有效性。

## 🎯 应用场景

该方法可应用于数字娱乐、虚拟现实、个性化内容创作等领域，如生成高保真虚拟角色、定制化肖像艺术或增强社交媒体内容，具有提升用户体验和创意表达的潜力。

## 📄 摘要（原文）

> Recent advancements in diffusion-based technologies have made significant strides, particularly in identity-preserved portrait generation (IPG). However, when using multiple reference images from the same ID, existing methods typically produce lower-fidelity portraits and struggle to customize face attributes precisely. To address these issues, this paper presents HiFi-Portrait, a high-fidelity method for zero-shot portrait generation. Specifically, we first introduce the face refiner and landmark generator to obtain fine-grained multi-face features and 3D-aware face landmarks. The landmarks include the reference ID and the target attributes. Then, we design HiFi-Net to fuse multi-face features and align them with landmarks, which improves ID fidelity and face control. In addition, we devise an automated pipeline to construct an ID-based dataset for training HiFi-Portrait. Extensive experimental results demonstrate that our method surpasses the SOTA approaches in face similarity and controllability. Furthermore, our method is also compatible with previous SDXL-based works.


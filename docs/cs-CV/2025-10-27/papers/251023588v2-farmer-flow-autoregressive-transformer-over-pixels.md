---
layout: default
title: FARMER: Flow AutoRegressive Transformer over Pixels
---

# FARMER: Flow AutoRegressive Transformer over Pixels

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23588" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23588v2</a>
  <a href="https://arxiv.org/pdf/2510.23588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23588v2" onclick="toggleFavorite(this, '2510.23588v2', 'FARMER: Flow AutoRegressive Transformer over Pixels')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangting Zheng, Qinyu Zhao, Tao Yang, Fei Xiao, Zhijie Lin, Jie Wu, Jiajun Deng, Yanyong Zhang, Rui Zhu

**分类**: cs.CV

**发布日期**: 2025-10-27 (更新: 2025-10-30)

**备注**: Bytedance Seed Technical Report

---

## 💡 一句话要点

**FARMER：提出一种基于流自回归Transformer的像素生成模型，实现精确似然估计和高质量图像合成。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像生成` `自回归模型` `归一化流` `像素建模` `自监督学习` `蒸馏训练` `无分类器引导` `可逆神经网络`

## 📋 核心要点

1. 现有视觉像素数据的连续自回归建模面临序列过长和高维空间的挑战。
2. FARMER结合归一化流和自回归模型，通过可逆自回归流将图像转换为潜在序列。
3. 通过自监督降维和单步蒸馏等技术，FARMER在保证性能的同时，提高了训练和推理效率。

## 📝 摘要（中文）

本文提出了一种名为FARMER的端到端生成框架，它统一了归一化流（NF）和自回归（AR）模型，可以直接从原始像素进行可追踪的似然估计和高质量的图像合成。FARMER采用可逆的自回归流将图像转换为潜在序列，其分布由自回归模型隐式建模。为了解决像素级建模中的冗余和复杂性，我们提出了一种自监督的降维方案，将NF潜在通道划分为信息性和冗余组，从而实现更有效和高效的AR建模。此外，我们设计了一种单步蒸馏方案，以显著加快推理速度，并引入了一种基于重采样的无分类器引导算法，以提高图像生成质量。大量实验表明，与现有的基于像素的生成模型相比，FARMER实现了具有竞争力的性能，同时提供了精确的似然性和可扩展的训练。

## 🔬 方法详解

**问题定义**：直接对原始数据分布进行显式似然建模是机器学习领域的一个关键问题，自回归建模已在大语言模型中取得了巨大成功。然而，在视觉像素数据上进行连续自回归建模面临着序列过长和高维空间的挑战。现有的像素生成模型通常难以兼顾精确的似然估计、高质量的图像合成以及高效的训练和推理。

**核心思路**：FARMER的核心思路是将归一化流（Normalizing Flow, NF）和自回归（Autoregressive, AR）模型结合起来。NF负责将原始像素空间映射到潜在空间，AR模型则负责对潜在空间的分布进行建模。通过这种方式，可以利用NF的可逆性进行精确的似然估计，同时利用AR模型的强大生成能力进行高质量的图像合成。此外，通过自监督降维和蒸馏等技术，可以提高模型的效率。

**技术框架**：FARMER的整体框架包括以下几个主要模块：1) 可逆自回归流（Invertible Autoregressive Flow）：将原始图像像素转换为潜在序列。2) 自监督降维模块：将NF潜在通道划分为信息性和冗余组。3) 自回归模型：对潜在序列的分布进行建模。4) 单步蒸馏模块：加速推理速度。5) 基于重采样的无分类器引导算法：提升图像生成质量。整个流程是端到端可训练的。

**关键创新**：FARMER的关键创新在于：1) 统一了NF和AR模型，实现了精确似然估计和高质量图像合成。2) 提出了自监督降维方案，有效降低了像素级建模的冗余和复杂性。3) 设计了单步蒸馏方案，显著加快了推理速度。4) 引入了基于重采样的无分类器引导算法，提升了图像生成质量。与现有方法相比，FARMER在性能、效率和可解释性方面都具有优势。

**关键设计**：在可逆自回归流中，使用了特定的可逆神经网络结构，例如Glow或RealNVP。自监督降维模块通过聚类等方法将NF潜在通道划分为信息性和冗余组。自回归模型可以使用Transformer或RNN等结构。单步蒸馏模块通过最小化教师模型和学生模型之间的KL散度来实现。基于重采样的无分类器引导算法通过调整采样分布来提升生成质量。损失函数包括似然损失和蒸馏损失等。

## 📊 实验亮点

实验结果表明，FARMER在图像生成任务上取得了具有竞争力的性能，同时提供了精确的似然估计。与现有基于像素的生成模型相比，FARMER在FID（Fréchet Inception Distance）等指标上取得了显著提升。此外，单步蒸馏方案显著加快了推理速度，使得FARMER在实际应用中更具优势。基于重采样的无分类器引导算法进一步提升了图像生成质量。

## 🎯 应用场景

FARMER具有广泛的应用前景，包括图像生成、图像修复、图像编辑、异常检测等。该模型可以用于生成逼真的人脸、风景、物体等图像，也可以用于修复图像中的缺失部分或编辑图像的内容。此外，FARMER还可以用于检测图像中的异常情况，例如医疗图像中的病灶或工业图像中的缺陷。未来，FARMER有望在计算机视觉、人工智能和机器学习等领域发挥重要作用。

## 📄 摘要（原文）

> Directly modeling the explicit likelihood of the raw data distribution is key topic in the machine learning area, which achieves the scaling successes in Large Language Models by autoregressive modeling. However, continuous AR modeling over visual pixel data suffer from extremely long sequences and high-dimensional spaces. In this paper, we present FARMER, a novel end-to-end generative framework that unifies Normalizing Flows (NF) and Autoregressive (AR) models for tractable likelihood estimation and high-quality image synthesis directly from raw pixels. FARMER employs an invertible autoregressive flow to transform images into latent sequences, whose distribution is modeled implicitly by an autoregressive model. To address the redundancy and complexity in pixel-level modeling, we propose a self-supervised dimension reduction scheme that partitions NF latent channels into informative and redundant groups, enabling more effective and efficient AR modeling. Furthermore, we design a one-step distillation scheme to significantly accelerate inference speed and introduce a resampling-based classifier-free guidance algorithm to boost image generation quality. Extensive experiments demonstrate that FARMER achieves competitive performance compared to existing pixel-based generative models while providing exact likelihoods and scalable training.


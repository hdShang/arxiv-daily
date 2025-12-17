---
layout: default
title: Optimizing Rank for High-Fidelity Implicit Neural Representations
---

# Optimizing Rank for High-Fidelity Implicit Neural Representations

**arXiv**: [2512.14366v1](https://arxiv.org/abs/2512.14366) | [PDF](https://arxiv.org/pdf/2512.14366.pdf)

**作者**: Julian McGinnis, Florian A. Hölzl, Suprosanna Shit, Florentin Bieder, Paul Friedrich, Mark Mühlau, Björn Menze, Daniel Rueckert, Benedikt Wiestler

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出通过优化网络秩来提升隐式神经表示的高频信号保真度，挑战传统架构限制观点。**

**关键词**: `隐式神经表示` `多层感知机` `秩优化` `高频信号` `图像重建` `新视角合成` `优化器设计` `计算机视觉`

## 📋 核心要点

1. 现有方法认为普通MLPs因架构限制无法表示高频信号，依赖复杂干预如坐标嵌入。
2. 论文提出高频学习受限源于训练中秩退化，通过优化器如Muon调节秩来提升保真度。
3. 实验显示该方法在图像和新视角合成中PSNR提升高达9 dB，验证了简单MLPs的潜力。

## 📝 摘要（中文）

基于普通多层感知机（MLPs）的隐式神经表示（INRs）被广泛认为无法表示高频内容，这引导研究转向坐标嵌入或特殊激活函数等架构干预。本文挑战了普通MLPs的低频偏差是学习高频内容的内在架构限制这一观点，认为这是训练过程中稳定秩退化的症状。我们通过实验证明，在训练期间调节网络的秩显著提高了学习信号的保真度，使即使是简单的MLP架构也具有表达力。大量实验表明，使用像Muon这样的优化器，具有高秩、近正交更新，能持续增强INRs架构，甚至超越简单的ReLU MLPs。这些显著改进适用于多种领域，包括自然和医学图像以及新视角合成，与先前最先进方法相比，PSNR提升高达9 dB。我们的项目页面包含代码和实验结果，可在https://muon-inrs.github.io访问。

## 🔬 方法详解

论文整体框架基于隐式神经表示（INRs），使用普通多层感知机（MLPs）作为基础架构。关键技术创新点在于挑战传统观点，将高频学习限制归因于训练过程中的稳定秩退化，而非MLPs的固有架构缺陷。为此，提出通过优化器（如Muon）调节网络秩，实现高秩、近正交的权重更新，从而增强信号保真度。与现有方法的主要区别在于，不依赖额外的架构干预（如坐标嵌入或特殊激活函数），而是通过优化训练过程本身来提升性能，使简单MLP架构也能有效表示高频内容。

## 📊 实验亮点

实验结果显示，使用优化器如Muon调节秩后，在多种领域（自然图像、医学图像、新视角合成）中，PSNR提升高达9 dB，显著超越先前最先进方法，验证了秩优化对提升INRs性能的有效性。

## 🎯 应用场景

该研究在计算机视觉和人工智能领域具有广泛潜在应用，包括自然图像处理、医学图像分析以及新视角合成等任务。通过提升隐式神经表示的高频保真度，可应用于高质量图像重建、3D场景表示和虚拟现实，为实际应用提供更精确和高效的解决方案。

## 📄 摘要（原文）

> Implicit Neural Representations (INRs) based on vanilla Multi-Layer Perceptrons (MLPs) are widely believed to be incapable of representing high-frequency content. This has directed research efforts towards architectural interventions, such as coordinate embeddings or specialized activation functions, to represent high-frequency signals. In this paper, we challenge the notion that the low-frequency bias of vanilla MLPs is an intrinsic, architectural limitation to learn high-frequency content, but instead a symptom of stable rank degradation during training. We empirically demonstrate that regulating the network's rank during training substantially improves the fidelity of the learned signal, rendering even simple MLP architectures expressive. Extensive experiments show that using optimizers like Muon, with high-rank, near-orthogonal updates, consistently enhances INR architectures even beyond simple ReLU MLPs. These substantial improvements hold across a diverse range of domains, including natural and medical images, and novel view synthesis, with up to 9 dB PSNR improvements over the previous state-of-the-art. Our project page, which includes code and experimental results, is available at: (https://muon-inrs.github.io).


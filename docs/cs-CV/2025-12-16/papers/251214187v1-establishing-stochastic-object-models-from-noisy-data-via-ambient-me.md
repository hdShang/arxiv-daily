---
layout: default
title: Establishing Stochastic Object Models from Noisy Data via Ambient Measurement-Integrated Diffusion
---

# Establishing Stochastic Object Models from Noisy Data via Ambient Measurement-Integrated Diffusion

**arXiv**: [2512.14187v1](https://arxiv.org/abs/2512.14187) | [PDF](https://arxiv.org/pdf/2512.14187.pdf)

**作者**: Jianwei Sun, Xiaoning Lei, Wenhao Cai, Xichen Xu, Yanshu Wang, Hu Gao

**分类**: cs.GR, cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出AMID方法，通过环境测量集成扩散从噪声数据中建立干净随机对象模型，以解决医学成像质量评估中的解剖变异性建模问题。**

**关键词**: `随机对象模型` `无监督学习` `扩散模型` `医学成像` `噪声解耦` `图像质量评估` `环境测量集成` `解剖变异性`

## 📋 核心要点

1. 核心问题：传统数学随机对象模型无法捕捉真实解剖结构，数据驱动方法需要干净数据，但临床数据通常含有噪声，难以直接建模。
2. 方法要点：提出AMID方法，通过测量集成策略对齐噪声与扩散轨迹，显式建模噪声耦合，从噪声数据中学习干净随机对象模型。
3. 实验或效果：在真实CT和乳腺X光数据集上，AMID在生成保真度和任务图像质量评估可靠性方面优于现有方法。

## 📝 摘要（中文）

基于任务的图像质量（IQ）度量对于评估医学成像系统至关重要，这些系统必须考虑包括解剖变异性在内的随机性。随机对象模型（SOMs）提供了这种变异性的统计描述，但传统的数学SOMs无法捕捉真实的解剖结构，而数据驱动方法通常需要临床任务中很少可用的干净数据。为了应对这一挑战，我们提出了AMID，一种具有噪声解耦的无监督环境测量集成扩散方法，直接从噪声测量中建立干净的SOMs。AMID引入了一种测量集成策略，将测量噪声与扩散轨迹对齐，并显式建模测量噪声和扩散噪声在步骤间的耦合，基于此设计了环境损失来学习干净的SOMs。在真实CT和乳腺X光数据集上的实验表明，AMID在生成保真度方面优于现有方法，并产生更可靠的基于任务的IQ评估，展示了其在无监督医学成像分析中的潜力。

## 🔬 方法详解

AMID的整体框架基于无监督扩散模型，核心创新点包括测量集成策略和环境损失设计。测量集成策略将测量噪声与扩散过程轨迹对齐，确保噪声在训练中被有效利用；同时，方法显式建模测量噪声和扩散噪声在步骤间的耦合关系，通过设计环境损失函数来解耦噪声，从而直接从噪声数据中学习干净的随机对象模型。与现有方法的主要区别在于，传统方法依赖干净数据或简单噪声假设，而AMID能处理真实临床噪声数据，无需干净数据先验，实现了更实用的无监督学习。

## 📊 实验亮点

实验在真实CT和乳腺X光数据集上进行，AMID在生成保真度方面显著优于现有方法，具体表现为更高的图像质量指标和更可靠的基于任务的评估结果，验证了其从噪声数据中学习干净模型的优势。

## 🎯 应用场景

该研究主要应用于医学成像领域，特别是CT和乳腺X光等成像系统的任务图像质量评估。通过建立干净的随机对象模型，AMID能更准确地模拟解剖变异性，提升成像系统设计和优化的可靠性，具有在无监督医学图像分析、设备性能评估和临床决策支持中的潜在价值。

## 📄 摘要（原文）

> Task-based measures of image quality (IQ) are critical for evaluating medical imaging systems, which must account for randomness including anatomical variability. Stochastic object models (SOMs) provide a statistical description of such variability, but conventional mathematical SOMs fail to capture realistic anatomy, while data-driven approaches typically require clean data rarely available in clinical tasks. To address this challenge, we propose AMID, an unsupervised Ambient Measurement-Integrated Diffusion with noise decoupling, which establishes clean SOMs directly from noisy measurements. AMID introduces a measurement-integrated strategy aligning measurement noise with the diffusion trajectory, and explicitly models coupling between measurement and diffusion noise across steps, an ambient loss is thus designed base on it to learn clean SOMs. Experiments on real CT and mammography datasets show that AMID outperforms existing methods in generation fidelity and yields more reliable task-based IQ evaluation, demonstrating its potential for unsupervised medical imaging analysis.


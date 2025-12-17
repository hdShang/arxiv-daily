---
layout: default
title: Synthetic Electrogram Generation with Variational Autoencoders for ECGI
---

# Synthetic Electrogram Generation with Variational Autoencoders for ECGI

**arXiv**: [2512.14537v1](https://arxiv.org/abs/2512.14537) | [PDF](https://arxiv.org/pdf/2512.14537.pdf)

**作者**: Miriam Gutiérrez Fernández, Karen López-Linares, Carlos Fambuena Santos, María S. Guillem, Andreu M. Climent, Óscar Barquero Pérez

**分类**: cs.LG, eess.SP

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于变分自编码器的合成心内电图生成方法，以缓解非侵入性电生理成像中的数据稀缺问题。**

**关键词**: `变分自编码器` `合成心内电图生成` `非侵入性电生理成像` `数据增强` `心房颤动` `深度学习` `心内电图重建` `节律条件生成`

## 📋 核心要点

1. 核心问题：非侵入性电生理成像中，配对体表电位与心内电图数据稀缺，限制了深度学习方法的进展。
2. 方法要点：提出两种变分自编码器模型，分别针对窦性心律和节律条件生成合成心内电图，以扩充数据集。
3. 实验或效果：VAE-S在仿真数据上保真度更高，VAE-C支持节律特异性生成，数据增强提升了下游任务性能。

## 📝 摘要（中文）

心房颤动是最常见的持续性心律失常，其临床评估需要准确表征心房电活动。非侵入性心电图成像结合深度学习方法，从体表电位估计心内电图已显示出潜力，但进展受限于配对体表电位-心内电图数据集的有限可用性。为应对这一限制，本研究探索了变分自编码器用于生成合成多通道心房心内电图。提出了两种模型：针对窦性心律的特定VAE和针对窦性心律与心房颤动信号的类别条件VAE。生成的合成心内电图通过形态、频谱和分布相似性指标进行评估。VAE-S在仿真心内电图方面实现了更高的保真度，而VAE-C以降低窦性重建质量为代价，实现了节律特异性生成。作为概念验证，生成的合成心内电图被用于下游非侵入性心内电图重建任务的数据增强，其中适度增强提高了估计性能。这些结果证明了基于VAE的生成模型在缓解数据稀缺和增强基于深度学习的非侵入性心电图成像流程方面的潜力。

## 🔬 方法详解

论文提出基于变分自编码器的生成模型框架，用于合成多通道心房心内电图。整体框架包括两个模型：VAE-S专门针对窦性心律信号进行训练，VAE-C则通过类别条件机制同时处理窦性心律和心房颤动信号，实现节律特异性生成。关键技术创新点在于利用VAE的潜在空间表示来建模心内电图的复杂分布，并通过条件控制生成特定节律的合成数据。与现有方法的主要区别在于，传统方法依赖有限真实数据，而本方法通过生成合成数据直接缓解数据稀缺问题，且VAE-C首次在非侵入性电生理成像中实现多节律条件生成，增强了模型的适用性和灵活性。

## 📊 实验亮点

VAE-S在仿真心内电图上的形态、频谱和分布相似性指标表现最佳，保真度更高；VAE-C成功实现节律特异性生成，但窦性重建质量略有下降。在下游非侵入性心内电图重建任务中，使用生成数据进行适度数据增强，显著提高了估计性能，验证了方法的有效性。

## 🎯 应用场景

该研究主要应用于非侵入性电生理成像领域，特别是心房颤动的诊断和治疗规划。通过生成合成心内电图，可以扩充训练数据集，提升深度学习模型的泛化能力和准确性，从而优化临床评估流程，支持更精准的心脏电活动分析。

## 📄 摘要（原文）

> Atrial fibrillation (AF) is the most prevalent sustained cardiac arrhythmia, and its clinical assessment requires accurate characterization of atrial electrical activity. Noninvasive electrocardiographic imaging (ECGI) combined with deep learning (DL) approaches for estimating intracardiac electrograms (EGMs) from body surface potentials (BSPMs) has shown promise, but progress is hindered by the limited availability of paired BSPM-EGM datasets. To address this limitation, we investigate variational autoencoders (VAEs) for the generation of synthetic multichannel atrial EGMs. Two models are proposed: a sinus rhythm-specific VAE (VAE-S) and a class-conditioned VAE (VAE-C) trained on both sinus rhythm and AF signals. Generated EGMs are evaluated using morphological, spectral, and distributional similarity metrics. VAE-S achieves higher fidelity with respect to in silico EGMs, while VAE-C enables rhythm-specific generation at the expense of reduced sinus reconstruction quality. As a proof of concept, the generated EGMs are used for data augmentation in a downstream noninvasive EGM reconstruction task, where moderate augmentation improves estimation performance. These results demonstrate the potential of VAE-based generative modeling to alleviate data scarcity and enhance deep learning-based ECGI pipelines.


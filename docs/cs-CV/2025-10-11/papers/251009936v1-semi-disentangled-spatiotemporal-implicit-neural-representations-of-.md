---
layout: default
title: Semi-disentangled spatiotemporal implicit neural representations of longitudinal neuroimaging data for trajectory classification
---

# Semi-disentangled spatiotemporal implicit neural representations of longitudinal neuroimaging data for trajectory classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09936" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09936v1</a>
  <a href="https://arxiv.org/pdf/2510.09936.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09936v1" onclick="toggleFavorite(this, '2510.09936v1', 'Semi-disentangled spatiotemporal implicit neural representations of longitudinal neuroimaging data for trajectory classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agampreet Aulakh, Nils D. Forkert, Matthias Wilms

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: Accepted at the MICCAI 2025 Learning with Longitudinal Medical Images and Data Workshop

---

## 💡 一句话要点

**提出一种半解耦时空隐式神经表示方法，用于纵向神经影像数据的轨迹分类。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `隐式神经表示` `纵向神经影像` `轨迹分类` `脑衰老` `半解耦表示`

## 📋 核心要点

1. 纵向神经影像数据分析面临个体内部和群体间不同的空间和时间采样模式的挑战，传统深度学习方法难以有效建模连续的生物过程。
2. 论文提出一种基于隐式神经表示(INR)的方法，将纵向MRI数据建模为连续函数，并设计了能够部分解耦空间和时间轨迹参数的INR架构。
3. 在模拟的脑衰老轨迹分类任务中，该方法在非规则采样实验中达到了81.3%的准确率，优于基线模型，验证了方法的有效性。

## 📝 摘要（中文）

本文提出了一种全新的、完全数据驱动的方法，通过使用隐式神经表示（INRs）将受试者特定的纵向T1加权MRI数据建模为连续函数，从而表示整个大脑的衰老轨迹。为此，作者引入了一种新颖的INR架构，能够部分解耦空间和时间轨迹参数，并设计了一个高效的框架，该框架直接在INRs的参数空间上运行，以对大脑衰老轨迹进行分类。为了在受控数据环境中评估该方法，作者开发了一种生物学上合理的轨迹模拟，并生成了450名健康和痴呆样受试者在规则和不规则采样时间点的T1加权3D MRI数据。在更真实的非规则采样实验中，基于INR的方法在脑衰老轨迹分类任务中实现了81.3%的准确率，优于标准深度学习基线模型（73.7%）。

## 🔬 方法详解

**问题定义**：论文旨在解决纵向神经影像数据分析中，由于数据采样不规则和传统深度学习方法难以建模连续生物过程的问题。现有方法难以有效处理个体内部和群体间不同的空间和时间采样模式，限制了对大脑衰老轨迹的准确分类。

**核心思路**：论文的核心思路是利用隐式神经表示（INRs）将离散的纵向MRI数据表示为连续函数。通过将大脑结构随时间的变化建模为连续的时空函数，可以克服传统方法对数据采样一致性的要求，并更好地捕捉大脑衰老轨迹的动态变化。

**技术框架**：该方法主要包含以下几个阶段：1) 使用INR将每个受试者的纵向MRI数据编码为连续的时空表示。2) 设计一种新颖的INR架构，该架构能够部分解耦空间和时间轨迹参数。3) 在INRs的参数空间上直接进行大脑衰老轨迹分类。4) 使用模拟的纵向MRI数据对方法进行评估。

**关键创新**：该方法最重要的创新点在于使用半解耦的时空隐式神经表示来建模纵向神经影像数据。与传统的深度学习方法相比，该方法能够处理不规则采样的数据，并更好地捕捉大脑衰老轨迹的连续变化。此外，直接在INRs的参数空间上进行分类，避免了对原始图像数据的直接操作，提高了计算效率。

**关键设计**：论文设计了一种能够部分解耦空间和时间轨迹参数的INR架构。具体来说，该架构将空间坐标和时间点作为输入，输出对应位置的图像强度值。通过特定的网络结构设计，使得网络能够学习到空间和时间之间的解耦表示。此外，论文还设计了一种生物学上合理的轨迹模拟方法，用于生成用于评估的纵向MRI数据。

## 📊 实验亮点

该方法在模拟的脑衰老轨迹分类任务中取得了显著的成果。在更真实的非规则采样实验中，基于INR的方法达到了81.3%的准确率，相比于标准深度学习基线模型（73.7%）有显著提升。这一结果表明，该方法能够有效地处理不规则采样的数据，并更好地捕捉大脑衰老轨迹的动态变化。

## 🎯 应用场景

该研究成果可应用于神经退行性疾病的早期诊断和风险预测，例如阿尔茨海默病。通过对个体大脑衰老轨迹的精确建模和分类，可以帮助医生识别高风险人群，并制定个性化的干预方案。此外，该方法还可以用于评估药物或生活方式干预对大脑衰老的影响。

## 📄 摘要（原文）

> The human brain undergoes dynamic, potentially pathology-driven, structural changes throughout a lifespan. Longitudinal Magnetic Resonance Imaging (MRI) and other neuroimaging data are valuable for characterizing trajectories of change associated with typical and atypical aging. However, the analysis of such data is highly challenging given their discrete nature with different spatial and temporal image sampling patterns within individuals and across populations. This leads to computational problems for most traditional deep learning methods that cannot represent the underlying continuous biological process. To address these limitations, we present a new, fully data-driven method for representing aging trajectories across the entire brain by modelling subject-specific longitudinal T1-weighted MRI data as continuous functions using Implicit Neural Representations (INRs). Therefore, we introduce a novel INR architecture capable of partially disentangling spatial and temporal trajectory parameters and design an efficient framework that directly operates on the INRs' parameter space to classify brain aging trajectories. To evaluate our method in a controlled data environment, we develop a biologically grounded trajectory simulation and generate T1-weighted 3D MRI data for 450 healthy and dementia-like subjects at regularly and irregularly sampled timepoints. In the more realistic irregular sampling experiment, our INR-based method achieves 81.3% accuracy for the brain aging trajectory classification task, outperforming a standard deep learning baseline model (73.7%).


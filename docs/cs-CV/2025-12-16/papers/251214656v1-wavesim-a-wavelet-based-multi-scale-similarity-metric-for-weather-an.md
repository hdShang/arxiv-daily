---
layout: default
title: WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields
---

# WaveSim: A Wavelet-based Multi-scale Similarity Metric for Weather and Climate Fields

**arXiv**: [2512.14656v1](https://arxiv.org/abs/2512.14656) | [PDF](https://arxiv.org/pdf/2512.14656.pdf)

**作者**: Gabriele Accarino, Viviana Acquaviva, Sara Shamekh, Duncan Watson-Parris, David Lawrence

**分类**: physics.ao-ph, cs.CV, physics.data-an

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/gabrieleaccarino/wavesim)

---

## 💡 一句话要点

**提出WaveSim，一种基于小波变换的多尺度相似性度量，用于评估天气和气候场。**

🎯 **匹配领域**: **动作生成与物理动画 (Animation & Physics)** **3D感知与状态估计 (Perception & State Est)**

**关键词**: `小波变换` `相似性度量` `气候模型评估` `天气预报验证` `多尺度分析` `空间场` `地球系统模型`

## 📋 核心要点

1. 传统点式度量无法将天气和气候场中的误差归因于特定的物理尺度或模式，限制了诊断能力。
2. WaveSim利用小波变换将场分解为多尺度分量，并从幅度、位移和结构三个正交维度评估相似性。
3. 实验表明WaveSim在合成数据和地球系统模型中均有效，能提供可解释的相似性评估结果。

## 📝 摘要（中文）

本文介绍了一种名为WaveSim的多尺度相似性度量，用于评估天气和气候应用中的空间场。WaveSim利用小波变换将输入场分解为特定尺度的小波系数。该度量通过将从这些系数导出的三个正交分量相乘构建：幅度（Magnitude），量化系数能量分布的相似性，即场的强度；位移（Displacement），通过比较归一化能量分布的质心来捕获空间位移；以及结构（Structure），评估独立于位置和幅度的模式组织。每个分量产生一个尺度特定的相似性得分，范围从0（无相似性）到1（完全相似性），然后跨尺度组合以产生整体相似性度量。我们首先使用合成测试用例评估WaveSim，应用受控的空间和时间扰动来系统地评估其灵敏度和预期行为。然后，我们展示了它在地球系统模型中气候变率关键模式的物理相关案例研究中的适用性。传统的点式度量缺乏将误差归因于物理尺度或不同相似性模式的机制。通过在小波域中操作并沿独立轴分解信号，WaveSim绕过了这些限制，并提供了一个可解释且诊断丰富的框架，用于评估复杂场中的相似性。此外，WaveSim框架允许用户强调特定尺度或分量，并适用于用户特定的模型互比较、模型评估以及预测系统的校准和训练。我们提供了一个PyTorch-ready的WaveSim实现，以及所有评估脚本，地址为：https://github.com/gabrieleaccarino/wavesim。

## 🔬 方法详解

**问题定义**：论文旨在解决天气和气候模型评估中，传统点式度量无法有效捕捉空间场的结构性差异，以及难以将误差归因于特定物理尺度的问题。现有方法对空间位移和幅度变化敏感，缺乏对模式组织相似性的有效评估手段。

**核心思路**：论文的核心思路是利用小波变换将空间场分解到不同尺度上，然后在小波域中，通过分析幅度、位移和结构三个正交分量，来评估不同场之间的相似性。这种多尺度分析方法能够捕捉不同尺度的空间结构，并提供更具诊断性的相似性度量。

**技术框架**：WaveSim的整体框架包括以下几个主要阶段：1) 小波变换：使用小波变换将输入场分解为不同尺度的小波系数。2) 分量提取：从每个尺度的小波系数中提取幅度、位移和结构三个分量。幅度反映能量分布，位移反映空间偏移，结构反映模式组织。3) 相似性计算：分别计算每个尺度上幅度、位移和结构的相似性得分。4) 尺度融合：将不同尺度的相似性得分进行加权平均，得到最终的相似性度量。

**关键创新**：WaveSim的关键创新在于其多尺度分析和正交分量分解。传统方法通常直接比较原始场，而WaveSim通过小波变换将场分解到不同尺度，从而能够捕捉不同尺度的空间结构。此外，通过将相似性分解为幅度、位移和结构三个正交分量，WaveSim能够提供更具诊断性的相似性度量，帮助用户理解不同场之间的差异。

**关键设计**：WaveSim的关键设计包括：1) 小波基的选择：论文中可能使用了特定的小波基，例如Daubechies小波，以实现有效的多尺度分解。2) 能量归一化：在计算位移分量时，需要对能量分布进行归一化，以消除幅度差异的影响。3) 尺度加权：在尺度融合阶段，需要对不同尺度的相似性得分进行加权，以反映不同尺度对整体相似性的贡献。4) 相似性度量函数：论文可能使用了特定的相似性度量函数，例如余弦相似度或相关系数，来计算幅度、位移和结构的相似性得分。

## 📊 实验亮点

论文通过合成测试用例系统地评估了WaveSim的灵敏度，并展示了其在地球系统模型中气候变率关键模式评估中的适用性。结果表明，WaveSim能够有效捕捉空间场的结构性差异，并提供可解释的相似性度量。与传统点式度量相比，WaveSim能够提供更具诊断性的信息，帮助用户理解不同场之间的差异。

## 🎯 应用场景

WaveSim可应用于气候模型评估、天气预报验证、以及地球系统模型的互比较。它能够帮助研究人员诊断模型误差的来源，并改进模型的参数化方案。此外，WaveSim还可用于校准和训练预测系统，提高预测的准确性和可靠性。该方法具有广泛的应用前景，能够促进气候科学和气象学的发展。

## 📄 摘要（原文）

> We introduce WaveSim, a multi-scale similarity metric for the evaluation of spatial fields in weather and climate applications. WaveSim exploits wavelet transforms to decompose input fields into scale-specific wavelet coefficients. The metric is built by multiplying three orthogonal components derived from these coefficients: Magnitude, which quantifies similarities in the energy distribution of the coefficients, i.e., the intensity of the field; Displacement, which captures spatial shift by comparing the centers of mass of normalized energy distributions; and Structure, which assesses pattern organization independent of location and amplitude. Each component yields a scale-specific similarity score ranging from 0 (no similarity) to 1 (perfect similarity), which are then combined across scales to produce an overall similarity measure. We first evaluate WaveSim using synthetic test cases, applying controlled spatial and temporal perturbations to systematically assess its sensitivity and expected behavior. We then demonstrate its applicability to physically relevant case studies of key modes of climate variability in Earth System Models. Traditional point-wise metrics lack a mechanism for attributing errors to physical scales or modes of dissimilarity. By operating in the wavelet domain and decomposing the signal along independent axes, WaveSim bypasses these limitations and provides an interpretable and diagnostically rich framework for assessing similarity in complex fields. Additionally, the WaveSim framework allows users to place emphasis on a specific scale or component, and lends itself to user-specific model intercomparison, model evaluation, and calibration and training of forecasting systems. We provide a PyTorch-ready implementation of WaveSim, along with all evaluation scripts, at: https://github.com/gabrieleaccarino/wavesim.


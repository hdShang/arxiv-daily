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

**提出WaveSim，一种基于小波变换的多尺度相似性度量方法，用于评估天气和气候空间场。**

**关键词**: `小波变换` `多尺度相似性度量` `天气气候场评估` `模型比较` `预测系统训练` `空间场分析` `正交分量分解`

## 📋 核心要点

1. 传统逐点度量无法将误差归因于物理尺度或差异模式，限制了天气和气候场评估的深度诊断能力。
2. WaveSim利用小波变换分解场，通过幅度、位移和结构三个正交分量量化多尺度相似性，提供可解释的评估框架。
3. 在合成测试和气候变率案例中，WaveSim表现出对空间和时间扰动的敏感性，并成功应用于模型比较和预测系统训练。

## 📝 摘要（中文）

我们介绍了WaveSim，一种用于评估天气和气候应用中空间场的多尺度相似性度量方法。WaveSim利用小波变换将输入场分解为尺度特定的小波系数。该度量通过乘以从这些系数导出的三个正交分量构建：幅度，量化系数能量分布的相似性，即场的强度；位移，通过比较归一化能量分布的质量中心来捕捉空间偏移；以及结构，评估独立于位置和幅度的模式组织。每个分量产生一个尺度特定的相似性得分，范围从0（无相似性）到1（完美相似性），然后跨尺度组合以产生整体相似性度量。我们首先使用合成测试案例评估WaveSim，应用受控的空间和时间扰动来系统评估其敏感性和预期行为。然后，我们展示了其在物理相关案例研究中的适用性，这些案例研究涉及地球系统模型中关键的气候变率模式。传统的逐点度量缺乏将误差归因于物理尺度或差异模式的机制。通过在小波域操作并沿独立轴分解信号，WaveSim绕过了这些限制，并为评估复杂场中的相似性提供了一个可解释且诊断丰富的框架。此外，WaveSim框架允许用户强调特定尺度或分量，并适用于用户特定的模型比较、模型评估以及预测系统的校准和训练。我们提供了WaveSim的PyTorch就绪实现，以及所有评估脚本，网址为：https://github.com/gabrieleaccarino/wavesim。

## 🔬 方法详解

WaveSim的整体框架基于小波变换，将输入空间场分解为尺度特定的小波系数。关键技术创新点在于从系数中提取三个正交分量：幅度分量量化能量分布相似性，反映场强度；位移分量通过比较归一化能量分布的质量中心来捕捉空间偏移；结构分量评估模式组织，独立于位置和振幅。这些分量分别计算尺度特定相似性得分（0到1），然后跨尺度组合形成整体度量。与现有方法的主要区别在于，传统逐点度量（如均方误差）缺乏多尺度分解和正交分量分析，而WaveSim通过小波域操作提供了更丰富、可解释的相似性评估，能够区分不同物理尺度的差异模式。

## 📊 实验亮点

WaveSim在合成测试中表现出对空间和时间扰动的敏感性，验证了其预期行为。在气候变率案例研究中，成功应用于评估地球系统模型，提供了比传统度量更丰富的诊断信息，支持用户强调特定尺度或分量。

## 🎯 应用场景

WaveSim适用于天气和气候领域的模型比较、模型评估、预测系统校准和训练。其多尺度分析能力有助于诊断地球系统模型中的气候变率模式，提升模型性能优化和物理过程理解。

## 📄 摘要（原文）

> We introduce WaveSim, a multi-scale similarity metric for the evaluation of spatial fields in weather and climate applications. WaveSim exploits wavelet transforms to decompose input fields into scale-specific wavelet coefficients. The metric is built by multiplying three orthogonal components derived from these coefficients: Magnitude, which quantifies similarities in the energy distribution of the coefficients, i.e., the intensity of the field; Displacement, which captures spatial shift by comparing the centers of mass of normalized energy distributions; and Structure, which assesses pattern organization independent of location and amplitude. Each component yields a scale-specific similarity score ranging from 0 (no similarity) to 1 (perfect similarity), which are then combined across scales to produce an overall similarity measure. We first evaluate WaveSim using synthetic test cases, applying controlled spatial and temporal perturbations to systematically assess its sensitivity and expected behavior. We then demonstrate its applicability to physically relevant case studies of key modes of climate variability in Earth System Models. Traditional point-wise metrics lack a mechanism for attributing errors to physical scales or modes of dissimilarity. By operating in the wavelet domain and decomposing the signal along independent axes, WaveSim bypasses these limitations and provides an interpretable and diagnostically rich framework for assessing similarity in complex fields. Additionally, the WaveSim framework allows users to place emphasis on a specific scale or component, and lends itself to user-specific model intercomparison, model evaluation, and calibration and training of forecasting systems. We provide a PyTorch-ready implementation of WaveSim, along with all evaluation scripts, at: https://github.com/gabrieleaccarino/wavesim.


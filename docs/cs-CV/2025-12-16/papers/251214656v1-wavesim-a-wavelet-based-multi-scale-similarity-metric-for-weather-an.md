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

**提出WaveSim，一种基于小波变换的多尺度相似性度量方法，用于评估天气和气候空间场的相似性。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `小波变换` `多尺度相似性度量` `天气气候场评估` `模型诊断` `空间场分析` `正交分量分解` `可解释性框架` `PyTorch实现`

## 📋 核心要点

1. 传统逐点度量无法将误差归因于物理尺度或差异模式，限制了天气和气候场评估的深度分析。
2. WaveSim利用小波变换分解场，通过幅度、位移和结构三个正交分量量化多尺度相似性。
3. 在合成测试和气候变率案例中，WaveSim表现出高敏感性和可解释性，支持模型评估和校准。

## 📝 摘要（中文）

我们介绍了WaveSim，一种用于评估天气和气候应用中空间场的多尺度相似性度量方法。WaveSim利用小波变换将输入场分解为特定尺度的小波系数。该度量通过乘以从这些系数导出的三个正交分量来构建：幅度，量化系数能量分布的相似性，即场的强度；位移，通过比较归一化能量分布的质量中心来捕捉空间偏移；以及结构，评估独立于位置和幅度的模式组织。每个分量产生一个特定尺度的相似性得分，范围从0（无相似性）到1（完美相似性），然后跨尺度组合以产生整体相似性度量。我们首先使用合成测试案例评估WaveSim，应用受控的空间和时间扰动来系统评估其敏感性和预期行为。然后，我们通过地球系统模型中关键气候变率模式的物理相关案例研究来展示其适用性。传统的逐点度量缺乏将误差归因于物理尺度或差异模式的机制。通过在小波域中操作并沿独立轴分解信号，WaveSim克服了这些限制，并为评估复杂场中的相似性提供了一个可解释且诊断丰富的框架。此外，WaveSim框架允许用户强调特定尺度或分量，并适用于用户特定的模型比较、模型评估以及预测系统的校准和训练。我们提供了WaveSim的PyTorch就绪实现以及所有评估脚本，网址为：https://github.com/gabrieleaccarino/wavesim。

## 🔬 方法详解

**问题定义**：论文旨在解决天气和气候空间场相似性评估中的问题，传统逐点度量（如均方误差）缺乏多尺度分析和误差归因能力，无法区分强度、位置和结构差异，限制了模型诊断和比较的深度。

**核心思路**：论文提出基于小波变换的多尺度相似性度量WaveSim，通过分解场到不同尺度，并设计三个正交分量（幅度、位移、结构）来独立量化相似性，从而提供可解释的、尺度感知的评估框架。

**技术框架**：整体流程包括：1) 输入空间场；2) 应用小波变换分解为多尺度小波系数；3) 从系数计算幅度、位移和结构三个分量，每个分量产生尺度特定相似性得分（0-1）；4) 跨尺度组合得分生成整体相似性度量；5) 支持用户自定义权重以强调特定尺度或分量。

**关键创新**：最重要的创新是将小波变换与正交分量分解结合，实现多尺度、可解释的相似性度量，与现有方法相比，本质区别在于能同时捕捉强度、空间偏移和模式结构的差异，并提供诊断性分析。

**关键设计**：关键设计包括：使用小波变换（如Daubechies小波）进行多尺度分解；幅度分量基于能量分布相似性；位移分量通过归一化能量分布的质量中心比较；结构分量独立于位置和幅度评估模式组织；得分范围标准化为0-1；提供PyTorch实现以支持高效计算和集成。

## 📊 实验亮点

在合成测试中，WaveSim对受控扰动表现出高敏感性，能准确量化不同尺度相似性；在气候变率案例研究中，成功评估了关键模式（如ENSO）的相似性，相比传统度量提供更丰富的诊断信息，具体性能数据未在摘要中提供，但框架已通过开源代码验证。

## 🎯 应用场景

WaveSim适用于天气和气候领域的模型比较、模型评估、预测系统校准和训练，例如地球系统模型的气候变率模式分析。其多尺度特性支持诊断性评估，帮助识别模型误差来源，提升预测准确性，未来可扩展至其他空间场分析领域。

## 📄 摘要（原文）

> We introduce WaveSim, a multi-scale similarity metric for the evaluation of spatial fields in weather and climate applications. WaveSim exploits wavelet transforms to decompose input fields into scale-specific wavelet coefficients. The metric is built by multiplying three orthogonal components derived from these coefficients: Magnitude, which quantifies similarities in the energy distribution of the coefficients, i.e., the intensity of the field; Displacement, which captures spatial shift by comparing the centers of mass of normalized energy distributions; and Structure, which assesses pattern organization independent of location and amplitude. Each component yields a scale-specific similarity score ranging from 0 (no similarity) to 1 (perfect similarity), which are then combined across scales to produce an overall similarity measure. We first evaluate WaveSim using synthetic test cases, applying controlled spatial and temporal perturbations to systematically assess its sensitivity and expected behavior. We then demonstrate its applicability to physically relevant case studies of key modes of climate variability in Earth System Models. Traditional point-wise metrics lack a mechanism for attributing errors to physical scales or modes of dissimilarity. By operating in the wavelet domain and decomposing the signal along independent axes, WaveSim bypasses these limitations and provides an interpretable and diagnostically rich framework for assessing similarity in complex fields. Additionally, the WaveSim framework allows users to place emphasis on a specific scale or component, and lends itself to user-specific model intercomparison, model evaluation, and calibration and training of forecasting systems. We provide a PyTorch-ready implementation of WaveSim, along with all evaluation scripts, at: https://github.com/gabrieleaccarino/wavesim.


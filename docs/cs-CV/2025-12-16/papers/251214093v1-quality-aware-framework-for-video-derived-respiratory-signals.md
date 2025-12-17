---
layout: default
title: Quality-Aware Framework for Video-Derived Respiratory Signals
---

# Quality-Aware Framework for Video-Derived Respiratory Signals

**arXiv**: [2512.14093v1](https://arxiv.org/abs/2512.14093) | [PDF](https://arxiv.org/pdf/2512.14093.pdf)

**作者**: Nhi Nguyen, Constantino Álvarez Casado, Le Nguyen, Manuel Lage Cañellas, Miguel Bordallo López

**分类**: cs.CV, eess.SP

**发布日期**: 2025-12-16

**备注**: 6 pages, 1 figure, 2 tables, conference

---

## 💡 一句话要点

**提出质量感知框架以解决视频呼吸信号估计中信号质量不一致的问题，实现自适应融合与过滤。**

**关键词**: `视频呼吸率估计` `质量感知框架` `信号融合` `远程光电容积描记术` `机器学习模型` `频谱分析` `自适应过滤` `呼吸监测`

## 📋 核心要点

1. 核心问题：视频呼吸率估计因信号提取方法多样导致质量不一致，影响可靠性和准确性。
2. 方法要点：整合多源信号，动态评估质量，通过机器学习模型预测准确性并自适应融合信号。
3. 实验或效果：在三个数据集上验证，框架降低估计误差，性能提升依赖于数据集特性。

## 📝 摘要（中文）

基于视频的呼吸率估计常因不同提取方法产生的信号质量不一致而不可靠。本文提出一个预测性、质量感知的框架，整合了异质信号源并动态评估其可靠性。从面部远程光电容积描记术、上半身运动和深度学习流程中提取十种信号，并使用四种频谱估计器进行分析：Welch方法、多重信号分类、快速傅里叶变换和峰值检测。然后，利用片段级质量指标训练机器学习模型，以预测准确性或选择最可靠的信号。这实现了自适应信号融合和基于质量的片段过滤。在三个公共数据集上的实验表明，该框架在大多数情况下比个体方法实现了更低的呼吸率估计误差，性能提升取决于数据集特性。这些发现突显了质量驱动的预测建模在提供可扩展和泛化的视频呼吸监测解决方案方面的潜力。

## 🔬 方法详解

论文提出一个质量感知框架，整体包括信号提取、频谱分析和质量评估三部分。关键技术创新点在于从面部rPPG、上半身运动和深度学习流程中提取十种异质信号，使用Welch方法、MUSIC、FFT和峰值检测四种频谱估计器进行分析，并基于片段级质量指标训练机器学习模型进行准确性预测或信号选择。与现有方法的主要区别在于动态评估信号可靠性，实现自适应融合和过滤，而非依赖单一信号源或固定融合策略。

## 📊 实验亮点

在OMuSense-23、COHFACE和MAHNOB-HCI三个公共数据集上的实验显示，框架在大多数情况下比个体方法降低了呼吸率估计误差，性能提升因数据集特性而异，突显了质量驱动建模的有效性。

## 🎯 应用场景

该研究可应用于远程医疗监测、健康管理、运动生理学和智能家居等领域，提供非接触式、可扩展的呼吸监测解决方案，提升视频呼吸信号估计的准确性和泛化能力。

## 📄 摘要（原文）

> Video-based respiratory rate (RR) estimation is often unreliable due to inconsistent signal quality across extraction methods. We present a predictive, quality-aware framework that integrates heterogeneous signal sources with dynamic assessment of reliability. Ten signals are extracted from facial remote photoplethysmography (rPPG), upper-body motion, and deep learning pipelines, and analyzed using four spectral estimators: Welch's method, Multiple Signal Classification (MUSIC), Fast Fourier Transform (FFT), and peak detection. Segment-level quality indices are then used to train machine learning models that predict accuracy or select the most reliable signal. This enables adaptive signal fusion and quality-based segment filtering. Experiments on three public datasets (OMuSense-23, COHFACE, MAHNOB-HCI) show that the proposed framework achieves lower RR estimation errors than individual methods in most cases, with performance gains depending on dataset characteristics. These findings highlight the potential of quality-driven predictive modeling to deliver scalable and generalizable video-based respiratory monitoring solutions.


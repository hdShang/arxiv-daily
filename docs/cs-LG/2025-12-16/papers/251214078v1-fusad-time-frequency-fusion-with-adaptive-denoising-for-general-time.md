---
layout: default
title: FusAD: Time-Frequency Fusion with Adaptive Denoising for General Time Series Analysis
---

# FusAD: Time-Frequency Fusion with Adaptive Denoising for General Time Series Analysis

**arXiv**: [2512.14078v1](https://arxiv.org/abs/2512.14078) | [PDF](https://arxiv.org/pdf/2512.14078.pdf)

**作者**: Da Zhang, Bingyu Li, Zhiyuan Zhao, Feiping Nie, Junyu Gao, Xuelong Li

**分类**: cs.LG

**发布日期**: 2025-12-16

**备注**: Paper has been accepted by ICDE2026

**🔗 代码/项目**: [GITHUB](https://github.com/zhangda1018/FusAD)

---

## 💡 一句话要点

**提出FusAD统一框架，通过自适应时频融合与去噪解决多任务时间序列分析难题**

🎯 **匹配领域**: **强化学习**

**关键词**: `时间序列分析` `时频融合` `自适应去噪` `多任务学习` `傅里叶变换` `小波变换` `掩码预训练` `统一框架`

## 📋 核心要点

1. 现有方法多为单任务或特定数据类型设计，难以统一处理多任务和多样化时间序列。
2. 提出自适应时频融合与去噪机制，结合傅里叶/小波变换和掩码预训练，实现稳健特征提取。
3. 在分类、预测和异常检测任务上，FusAD在主流基准测试中持续优于最先进模型。

## 📝 摘要（中文）

时间序列分析在金融、医疗、工业和气象等领域至关重要，支撑着分类、预测和异常检测等关键任务。尽管深度学习模型近年来在这些领域取得了显著进展，但构建一个高效、多任务兼容且可泛化的统一框架仍面临重大挑战。现有方法通常针对单一任务或特定数据类型设计，难以同时处理多任务建模并有效整合不同类型时间序列的信息。此外，现实世界数据常受噪声、复杂频率成分和多尺度动态模式影响，进一步增加了稳健特征提取和分析的难度。为应对这些挑战，我们提出了FusAD，一个为多样化时间序列任务设计的统一分析框架。FusAD采用自适应时频融合机制，结合傅里叶和小波变换，高效捕捉全局-局部和多尺度动态特征。通过自适应去噪机制，FusAD自动感知并过滤各类噪声，突出关键序列变化，在复杂环境中实现稳健特征提取。此外，该框架整合了通用信息融合与解码结构，结合掩码预训练，促进多粒度表示的高效学习和迁移。大量实验表明，FusAD在主流时间序列基准测试中，在分类、预测和异常检测任务上持续优于最先进模型，同时保持高效率和可扩展性。代码可在https://github.com/zhangda1018/FusAD获取。

## 🔬 方法详解

FusAD是一个统一的时间序列分析框架，整体架构包括自适应时频融合、自适应去噪、信息融合与解码模块。关键技术创新点在于：1）自适应时频融合机制，同时利用傅里叶变换捕捉全局频率特征和小波变换提取局部多尺度动态；2）自适应去噪机制，自动检测并过滤噪声，增强特征鲁棒性；3）通用信息融合与解码结构，结合掩码预训练，促进多粒度表示学习。与现有方法的主要区别在于其多任务兼容性和泛化能力，通过统一设计有效整合时频信息，而非针对单一任务或数据类型的定制化方案。

## 📊 实验亮点

实验显示，FusAD在UCR时间序列分类、ETT电力预测和Yahoo异常检测等主流基准测试中，性能持续超越现有最先进模型，验证了其高效性和可扩展性。

## 🎯 应用场景

该研究可广泛应用于金融风险预测、医疗健康监测、工业设备故障检测和气象数据分析等领域，为复杂时间序列任务提供高效、稳健的解决方案，提升实际应用中的准确性和可靠性。

## 📄 摘要（原文）

> Time series analysis plays a vital role in fields such as finance, healthcare, industry, and meteorology, underpinning key tasks including classification, forecasting, and anomaly detection. Although deep learning models have achieved remarkable progress in these areas in recent years, constructing an efficient, multi-task compatible, and generalizable unified framework for time series analysis remains a significant challenge. Existing approaches are often tailored to single tasks or specific data types, making it difficult to simultaneously handle multi-task modeling and effectively integrate information across diverse time series types. Moreover, real-world data are often affected by noise, complex frequency components, and multi-scale dynamic patterns, which further complicate robust feature extraction and analysis. To ameliorate these challenges, we propose FusAD, a unified analysis framework designed for diverse time series tasks. FusAD features an adaptive time-frequency fusion mechanism, integrating both Fourier and Wavelet transforms to efficiently capture global-local and multi-scale dynamic features. With an adaptive denoising mechanism, FusAD automatically senses and filters various types of noise, highlighting crucial sequence variations and enabling robust feature extraction in complex environments. In addition, the framework integrates a general information fusion and decoding structure, combined with masked pre-training, to promote efficient learning and transfer of multi-granularity representations. Extensive experiments demonstrate that FusAD consistently outperforms state-of-the-art models on mainstream time series benchmarks for classification, forecasting, and anomaly detection tasks, while maintaining high efficiency and scalability. Code is available at https://github.com/zhangda1018/FusAD.


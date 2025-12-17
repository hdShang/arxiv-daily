---
layout: default
title: GRAFT: Grid-Aware Load Forecasting with Multi-Source Textual Alignment and Fusion
---

# GRAFT: Grid-Aware Load Forecasting with Multi-Source Textual Alignment and Fusion

**arXiv**: [2512.14400v1](https://arxiv.org/abs/2512.14400) | [PDF](https://arxiv.org/pdf/2512.14400.pdf)

**作者**: Fangzhou Lin, Guoshun He, Zhenyu Guo, Zhe Huang, Jinsong Tao

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出GRAFT模型，通过多源文本对齐与融合解决电网负荷预测中外部因素影响建模不足的问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `电网负荷预测` `多源文本对齐` `交叉注意力融合` `外部记忆接口` `时序预测` `可解释人工智能` `能源系统优化`

## 📋 核心要点

1. 现有负荷预测方法难以有效整合多源文本信息（如新闻、社交媒体、政策）以建模外部因素对电网负荷的复杂影响。
2. GRAFT通过严格对齐多源文本与负荷数据，并利用交叉注意力实现文本引导的融合，同时提供可扩展的外部记忆接口。
3. 实验显示GRAFT在多个区域和预测尺度上显著优于基线，达到或超越最先进水平，并支持文本影响的时序定位和解释。

## 📝 摘要（中文）

电力负荷同时受到天气、日历节律、突发事件和政策等多时间尺度外生因素的影响。为此，本文提出GRAFT（基于文本的电网感知预测）模型，改进STanHOP以更好地支持电网感知预测和多源文本干预。具体而言，GRAFT将每日聚合的新闻、社交媒体和政策文本与半小时负荷数据严格对齐，并通过训练和滚动预测期间的交叉注意力实现文本引导的融合到特定时间位置。此外，GRAFT提供即插即用的外部记忆接口，以适应实际部署中的不同信息源。我们构建并发布了一个覆盖2019-2021年澳大利亚五个州的统一对齐基准数据集（包括半小时负荷、每日对齐的天气/日历变量以及三类外部文本），并在统一协议下进行了系统、可重复的评估，涵盖小时、日和月三个尺度，以比较不同区域、外部源和时间尺度。实验结果表明，GRAFT显著优于强基线模型，并在多个区域和预测时间范围内达到或超越最先进水平。此外，该模型在事件驱动场景中表现稳健，并通过注意力读出实现文本对负荷影响的时序定位和源级解释。我们发布基准数据集、预处理脚本和预测结果，以促进电网负荷预测的标准化实证评估和可重复性。

## 🔬 方法详解

GRAFT基于改进的STanHOP框架，整体架构包括负荷序列编码、多源文本对齐与融合模块。关键技术创新点在于：严格对齐每日聚合的新闻、社交媒体和政策文本到半小时负荷时间点，通过交叉注意力机制在训练和滚动预测中实现文本信息到特定时间位置的引导融合；提供即插即用的外部记忆接口，便于集成不同信息源。与现有方法的主要区别在于其电网感知特性，能够更精细地处理多源文本干预，并支持实时部署中的灵活扩展。

## 📊 实验亮点

GRAFT在澳大利亚五个州的统一基准测试中，于小时、日、月三个预测尺度上均显著优于强基线，达到或超越最先进水平；模型在事件驱动场景下表现稳健，并通过注意力机制实现文本影响的时序定位和源级解释，增强了可解释性。

## 🎯 应用场景

该研究主要应用于智能电网管理和能源系统优化，可提升电力负荷预测的准确性和鲁棒性，帮助电网运营商应对天气变化、突发事件和政策调整等外部因素，实现更高效的能源调度和需求响应。

## 📄 摘要（原文）

> Electric load is simultaneously affected across multiple time scales by exogenous factors such as weather and calendar rhythms, sudden events, and policies. Therefore, this paper proposes GRAFT (GRid-Aware Forecasting with Text), which modifies and improves STanHOP to better support grid-aware forecasting and multi-source textual interventions. Specifically, GRAFT strictly aligns daily-aggregated news, social media, and policy texts with half-hour load, and realizes text-guided fusion to specific time positions via cross-attention during both training and rolling forecasting. In addition, GRAFT provides a plug-and-play external-memory interface to accommodate different information sources in real-world deployment. We construct and release a unified aligned benchmark covering 2019--2021 for five Australian states (half-hour load, daily-aligned weather/calendar variables, and three categories of external texts), and conduct systematic, reproducible evaluations at three scales -- hourly, daily, and monthly -- under a unified protocol for comparison across regions, external sources, and time scales. Experimental results show that GRAFT significantly outperforms strong baselines and reaches or surpasses the state of the art across multiple regions and forecasting horizons. Moreover, the model is robust in event-driven scenarios and enables temporal localization and source-level interpretation of text-to-load effects through attention read-out. We release the benchmark, preprocessing scripts, and forecasting results to facilitate standardized empirical evaluation and reproducibility in power grid load forecasting.


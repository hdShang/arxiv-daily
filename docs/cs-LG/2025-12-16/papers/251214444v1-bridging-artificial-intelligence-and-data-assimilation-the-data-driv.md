---
layout: default
title: Bridging Artificial Intelligence and Data Assimilation: The Data-driven Ensemble Forecasting System ClimaX-LETKF
---

# Bridging Artificial Intelligence and Data Assimilation: The Data-driven Ensemble Forecasting System ClimaX-LETKF

**arXiv**: [2512.14444v1](https://arxiv.org/abs/2512.14444) | [PDF](https://arxiv.org/pdf/2512.14444.pdf)

**作者**: Akira Takeshima, Kenta Shiraishi, Atsushi Okazaki, Tadashi Tsuyuki, Shunji Kotsuki

**分类**: cs.LG

**发布日期**: 2025-12-16

**备注**: 14 pages and 5 figures for the main text and 13 pages and 7 figures as supplementary materials

---

## 💡 一句话要点

**提出ClimaX-LETKF数据驱动集合天气预报系统，首次实现基于机器学习的纯数据驱动集合预报并稳定运行多年。**

**关键词**: `机器学习天气预报` `数据同化` `集合预报` `ClimaX-LETKF` `松弛到先验扰动` `数值天气预报` `大气吸引子` `气象观测`

## 📋 核心要点

1. 现有MLWP模型在同化真实观测或集合预报方面研究不足，缺乏独立于NWP的稳定数据驱动系统。
2. 提出ClimaX-LETKF，基于机器学习构建纯数据驱动集合预报框架，通过同化NCEP观测实现长期稳定运行。
3. 实验显示RTPP比RTPS在MLWP中更优，提升稳定性和准确性，但MLWP恢复大气吸引子能力弱于NWP。

## 📝 摘要（中文）

尽管基于机器学习的天气预报（MLWP）已取得显著进展，但在MLWP模型中同化真实观测或集合预报的研究仍然有限。我们介绍了ClimaX-LETKF，这是首个纯数据驱动的基于机器学习的集合天气预报系统。该系统通过同化NCEP ADP全球高空和地面天气观测，能够稳定运行多年，独立于数值天气预报（NWP）模型。实验表明，与松弛到先验扩展（RTPS）相比，使用松弛到先验扰动（RTPP）时系统表现出更高的稳定性和准确性，而NWP模型通常更稳定于RTPS。RTPP将分析扰动替换为分析和背景扰动的加权混合，而RTPS仅简单缩放分析扰动。我们的实验揭示，MLWP模型在将大气场恢复到其吸引子方面的能力不如NWP模型。这项工作为增强MLWP集合预报系统提供了宝贵见解，并代表了其实际应用的重要一步。

## 🔬 方法详解

ClimaX-LETKF是一个纯数据驱动的机器学习集合天气预报系统，核心框架基于局部集合变换卡尔曼滤波（LETKF）进行数据同化，结合机器学习模型生成预报。关键创新在于首次在MLWP中实现独立于NWP的长期稳定集合预报，通过同化NCEP ADP全球观测数据。与现有方法的主要区别在于：传统MLWP依赖NWP初始化或缺乏集合预报能力，而ClimaX-LETKF完全数据驱动，并引入RTPP（松弛到先验扰动）技术优化扰动更新，相比RTPS（松弛到先验扩展）更适应MLWP特性。

## 📊 实验亮点

ClimaX-LETKF在多年运行中表现稳定，RTPP相比RTPS显著提升MLWP集合预报的准确性和稳定性，但实验发现MLWP恢复大气吸引子能力弱于NWP，这为未来优化提供了关键方向。

## 🎯 应用场景

该研究可应用于气象预报、气候建模和灾害预警等领域，通过提升MLWP集合预报的稳定性和准确性，推动数据驱动天气预报系统的实际部署，减少对传统NWP的依赖，为极端天气事件预测和长期气候分析提供新工具。

## 📄 摘要（原文）

> While machine learning-based weather prediction (MLWP) has achieved significant advancements, research on assimilating real observations or ensemble forecasts within MLWP models remains limited. We introduce ClimaX-LETKF, the first purely data-driven ML-based ensemble weather forecasting system. It operates stably over multiple years, independently of numerical weather prediction (NWP) models, by assimilating the NCEP ADP Global Upper Air and Surface Weather Observations. The system demonstrates greater stability and accuracy with relaxation to prior perturbation (RTPP) than with relaxation to prior spread (RTPS), while NWP models tend to be more stable with RTPS. RTPP replaces an analysis perturbation with a weighted blend of analysis and background perturbations, whereas RTPS simply rescales the analysis perturbation. Our experiments reveal that MLWP models are less capable of restoring the atmospheric field to its attractor than NWP models. This work provides valuable insights for enhancing MLWP ensemble forecasting systems and represents a substantial step toward their practical applications.


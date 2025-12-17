---
layout: default
title: Synergistic Neural Forecasting of Air Pollution with Stochastic Sampling
---

# Synergistic Neural Forecasting of Air Pollution with Stochastic Sampling

**arXiv**: [2510.23977v1](https://arxiv.org/abs/2510.23977) | [PDF](https://arxiv.org/pdf/2510.23977.pdf)

**作者**: Yohan Abeysinghe, Muhammad Akhtar Munir, Sanoojan Baliah, Ron Sarafian, Fahad Shahbaz Khan, Yinon Rudich, Salman Khan

---

## 💡 一句话要点

**提出SynCast模型以改进空气污染预测，尤其针对极端事件。**

**关键词**: `空气污染预测` `神经网络模型` `极端事件处理` `Transformer架构` `扩散模型` `PM浓度预测`

## 📋 核心要点

1. 现有模型常低估罕见但危险的空气污染事件，如野火和沙尘暴。
2. 基于Transformer和扩散随机细化模块，捕捉PM浓度的非线性动态。
3. 使用ERA5和CAMS数据，在多种PM变量上显著提升预测准确性。

## 📄 摘要（原文）

> Air pollution remains a leading global health and environmental risk,
> particularly in regions vulnerable to episodic air pollution spikes due to
> wildfires, urban haze and dust storms. Accurate forecasting of particulate
> matter (PM) concentrations is essential to enable timely public health warnings
> and interventions, yet existing models often underestimate rare but hazardous
> pollution events. Here, we present SynCast, a high-resolution neural
> forecasting model that integrates meteorological and air composition data to
> improve predictions of both average and extreme pollution levels. Built on a
> regionally adapted transformer backbone and enhanced with a diffusion-based
> stochastic refinement module, SynCast captures the nonlinear dynamics driving
> PM spikes more accurately than existing approaches. Leveraging on harmonized
> ERA5 and CAMS datasets, our model shows substantial gains in forecasting
> fidelity across multiple PM variables (PM$_1$, PM$_{2.5}$, PM$_{10}$),
> especially under extreme conditions. We demonstrate that conventional loss
> functions underrepresent distributional tails (rare pollution events) and show
> that SynCast, guided by domain-aware objectives and extreme value theory,
> significantly enhances performance in highly impacted regions without
> compromising global accuracy. This approach provides a scalable foundation for
> next-generation air quality early warning systems and supports climate-health
> risk mitigation in vulnerable regions.


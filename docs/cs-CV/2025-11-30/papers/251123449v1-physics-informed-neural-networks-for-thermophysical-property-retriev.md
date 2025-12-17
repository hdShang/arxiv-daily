---
layout: default
title: Physics-Informed Neural Networks for Thermophysical Property Retrieval
---

# Physics-Informed Neural Networks for Thermophysical Property Retrieval

**arXiv**: [2511.23449v1](https://arxiv.org/abs/2511.23449) | [PDF](https://arxiv.org/pdf/2511.23449.pdf)

**作者**: Ali Waseem, Malcolm Mielle

---

## 💡 一句话要点

**提出基于PINN的迭代框架以原位估计墙体导热系数**

**关键词**: `逆热问题` `物理信息神经网络` `导热系数估计` `原位测量` `热像图分析` `建筑能效`

## 📋 核心要点

1. 核心问题：非侵入式原位数据下逆热问题求解易受环境变化影响，现有方法存在侵入性、耗时或敏感性问题。
2. 方法要点：使用PINN交替估计固定导热系数下的正向热问题和通过比较热像图与预测温度优化导热系数，直至收敛。
3. 实验或效果：利用天气站数据和模拟数据，在接近稳态条件下准确预测导热系数，最大MAE为4.0851，展示了原位可靠估计潜力。

## 📄 摘要（原文）

> Inverse heat problems refer to the estimation of material thermophysical properties given observed or known heat diffusion behaviour. Inverse heat problems have wide-ranging uses, but a critical application lies in quantifying how building facade renovation reduces thermal transmittance, a key determinant of building energy efficiency. However, solving inverse heat problems with non-invasive data collected in situ is error-prone due to environmental variability or deviations from theoretically assumed conditions. Hence, current methods for measuring thermal conductivity are either invasive, require lengthy observation periods, or are sensitive to environmental and experimental conditions. Here, we present a PINN-based iterative framework to estimate the thermal conductivity k of a wall from a set of thermographs; our framework alternates between estimating the forward heat problem with a PINN for a fixed k, and optimizing k by comparing the thermographs and surface temperatures predicted by the PINN, repeating until the estimated k's convergence. Using both environmental data captured by a weather station and data generated from Finite-Volume-Method software simulations, we accurately predict k across different environmental conditions and data collection sampling times, given the temperature profile of the wall at dawn is close to steady state. Although violating the steady-state assumption impacts the accuracy of k's estimation, we show that our proposed framework still only exhibits a maximum MAE of 4.0851. Our work demonstrates the potential of PINN-based methods for reliable estimation of material properties in situ and under realistic conditions, without lengthy measurement campaigns. Given the lack of research on using machine learning, and more specifically on PINNs, for solving in-situ inverse problems, we expect our work to be a starting point for more research on the topic.


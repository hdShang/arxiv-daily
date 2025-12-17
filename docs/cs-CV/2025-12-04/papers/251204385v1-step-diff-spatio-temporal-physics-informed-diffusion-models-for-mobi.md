---
layout: default
title: STeP-Diff: Spatio-Temporal Physics-Informed Diffusion Models for Mobile Fine-Grained Pollution Forecasting
---

# STeP-Diff: Spatio-Temporal Physics-Informed Diffusion Models for Mobile Fine-Grained Pollution Forecasting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04385" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04385v1</a>
  <a href="https://arxiv.org/pdf/2512.04385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04385v1" onclick="toggleFavorite(this, '2512.04385v1', 'STeP-Diff: Spatio-Temporal Physics-Informed Diffusion Models for Mobile Fine-Grained Pollution Forecasting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nan Zhou, Weijie Hong, Huandong Wang, Jianfeng Zheng, Qiuhua Wang, Yali Song, Xiao-Ping Zhang, Yong Li, Xinlei Chen

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**STeP-Diff：时空物理信息扩散模型用于移动细粒度污染预测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `空气污染预测` `扩散模型` `物理信息` `时空建模` `移动传感器` `DeepONet` `偏微分方程`

## 📋 核心要点

1. 现有方法难以处理移动传感器数据的不完整性和时间不一致性，导致细粒度空气污染预测精度不足。
2. STeP-Diff结合DeepONet和PDE约束的扩散模型，利用物理信息指导去噪过程，从而预测时空污染场。
3. 实验表明，STeP-Diff在空气污染预测的MAE、RMSE和MAPE指标上，显著优于现有方法，最高提升分别达到89.12%、82.30%和25.00%。

## 📝 摘要（中文）

本文提出了一种时空物理信息扩散模型（STeP-Diff），用于解决移动平台细粒度空气污染预测问题。利用部署在汽车和公交车等移动平台上的便携式传感器，可以低成本、易维护、广覆盖地收集数据。然而，由于这些非专用移动平台的随机和不可控的运动模式，导致传感器数据通常不完整且时间上不一致。STeP-Diff通过探索扩散模型逆过程中的潜在训练模式，并结合DeepONet来建模测量值的空间序列，以及基于偏微分方程（PDE）的扩散模型来预测来自不完整和时变数据的时空场。通过PDE约束的正则化框架，去噪过程渐近收敛到对流扩散动力学，确保预测既基于真实世界的测量，又符合控制污染扩散的基本物理规律。在两个城市部署了59个自设计的便携式传感设备，运行14天收集空气污染数据，实验结果表明，与第二好的算法相比，该模型在MAE、RMSE和MAPE方面分别提高了89.12%、82.30%和25.00%。

## 🔬 方法详解

**问题定义**：论文旨在解决利用移动传感器进行细粒度空气污染预测时，由于传感器数据不完整和时间不一致导致的预测精度问题。现有方法难以有效利用这些非结构化数据，无法准确捕捉污染的时空动态变化。

**核心思路**：论文的核心思路是将物理信息融入扩散模型中，利用偏微分方程（PDE）约束扩散过程，使得模型在去噪的同时，也符合污染扩散的基本物理规律。同时，利用DeepONet建模空间序列，从而更好地处理不完整的数据。

**技术框架**：STeP-Diff的整体框架包含两个主要部分：DeepONet和PDE-informed Diffusion Model。首先，利用DeepONet对移动传感器收集到的空间序列数据进行建模。然后，将DeepONet的输出作为PDE-informed Diffusion Model的输入，该模型通过扩散过程逐步添加噪声，再通过逆扩散过程进行去噪和预测。在逆扩散过程中，利用PDE约束正则化框架，确保预测结果符合物理规律。

**关键创新**：该论文的关键创新在于将物理信息（通过PDE约束）融入到扩散模型中。传统的扩散模型主要依赖数据驱动，而STeP-Diff通过PDE约束，使得模型在学习数据分布的同时，也学习了污染扩散的物理规律，从而提高了预测的准确性和鲁棒性。

**关键设计**：论文中关键的设计包括：1) 使用DeepONet来处理不规则的空间数据；2) 构建PDE约束的损失函数，该损失函数包含数据损失项和PDE损失项，用于指导扩散模型的训练；3) 扩散模型的具体实现细节，包括噪声添加策略、去噪网络的结构等。具体参数设置和网络结构在论文中未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，STeP-Diff在两个城市的空气污染预测任务中，显著优于现有方法。具体而言，与第二好的算法相比，STeP-Diff在平均绝对误差（MAE）方面提高了高达89.12%，在均方根误差（RMSE）方面提高了高达82.30%，在平均绝对百分比误差（MAPE）方面提高了高达25.00%。这些结果表明，STeP-Diff能够有效地捕捉空气污染场的时空依赖性，并提供更准确的预测。

## 🎯 应用场景

STeP-Diff可应用于城市环境监测、健康建筑设计、公共卫生管理等领域。通过部署低成本的移动传感器网络，可以实时监测城市空气质量，为政府决策提供数据支持。此外，该模型还可以用于预测室内空气质量，为健康建筑的设计和运行提供指导，从而改善人们的生活质量。

## 📄 摘要（原文）

> Fine-grained air pollution forecasting is crucial for urban management and the development of healthy buildings. Deploying portable sensors on mobile platforms such as cars and buses offers a low-cost, easy-to-maintain, and wide-coverage data collection solution. However, due to the random and uncontrollable movement patterns of these non-dedicated mobile platforms, the resulting sensor data are often incomplete and temporally inconsistent. By exploring potential training patterns in the reverse process of diffusion models, we propose Spatio-Temporal Physics-Informed Diffusion Models (STeP-Diff). STeP-Diff leverages DeepONet to model the spatial sequence of measurements along with a PDE-informed diffusion model to forecast the spatio-temporal field from incomplete and time-varying data. Through a PDE-constrained regularization framework, the denoising process asymptotically converges to the convection-diffusion dynamics, ensuring that predictions are both grounded in real-world measurements and aligned with the fundamental physics governing pollution dispersion. To assess the performance of the system, we deployed 59 self-designed portable sensing devices in two cities, operating for 14 days to collect air pollution data. Compared to the second-best performing algorithm, our model achieved improvements of up to 89.12% in MAE, 82.30% in RMSE, and 25.00% in MAPE, with extensive evaluations demonstrating that STeP-Diff effectively captures the spatio-temporal dependencies in air pollution fields.


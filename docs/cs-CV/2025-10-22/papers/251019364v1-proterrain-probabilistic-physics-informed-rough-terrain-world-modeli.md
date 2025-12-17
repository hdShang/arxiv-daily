---
layout: default
title: ProTerrain: Probabilistic Physics-Informed Rough Terrain World Modeling
---

# ProTerrain: Probabilistic Physics-Informed Rough Terrain World Modeling

**arXiv**: [2510.19364v1](https://arxiv.org/abs/2510.19364) | [PDF](https://arxiv.org/pdf/2510.19364.pdf)

**作者**: Golnaz Raja, Ruslan Agishev, Miloš Prágr, Joni Pajarinen, Karel Zimmermann, Arun Kumar Singh, Reza Ghabcheloo

---

## 💡 一句话要点

**提出概率物理信息粗糙地形世界建模框架，以提升非结构化环境中的机器人运动预测准确性。**

**关键词**: `概率世界建模` `空间不确定性` `可微分物理引擎` `轨迹预测` `粗糙地形导航`

## 📋 核心要点

1. 核心问题：现有方法忽略3D空间数据的局部相关性，导致不确定地形预测不可靠。
2. 方法要点：建模空间相关随机不确定性，并通过可微分物理引擎传播以预测轨迹。
3. 实验或效果：在公开数据集上显著改进不确定性估计和轨迹预测精度。

## 📄 摘要（原文）

> Uncertainty-aware robot motion prediction is crucial for downstream
> traversability estimation and safe autonomous navigation in unstructured,
> off-road environments, where terrain is heterogeneous and perceptual
> uncertainty is high. Most existing methods assume deterministic or spatially
> independent terrain uncertainties, ignoring the inherent local correlations of
> 3D spatial data and often producing unreliable predictions. In this work, we
> introduce an efficient probabilistic framework that explicitly models spatially
> correlated aleatoric uncertainty over terrain parameters as a probabilistic
> world model and propagates this uncertainty through a differentiable physics
> engine for probabilistic trajectory forecasting. By leveraging structured
> convolutional operators, our approach provides high-resolution multivariate
> predictions at manageable computational cost. Experimental evaluation on a
> publicly available dataset shows significantly improved uncertainty estimation
> and trajectory prediction accuracy over aleatoric uncertainty estimation
> baselines.


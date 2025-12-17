---
layout: default
title: Incorporating Ephemeral Traffic Waves in A Data-Driven Framework for Microsimulation in CARLA
---

# Incorporating Ephemeral Traffic Waves in A Data-Driven Framework for Microsimulation in CARLA

**arXiv**: [2511.23236v1](https://arxiv.org/abs/2511.23236) | [PDF](https://arxiv.org/pdf/2511.23236.pdf)

**作者**: Alex Richardson, Azhar Hasan, Gabor Karsai, Jonathan Sprinkle

---

## 💡 一句话要点

**提出基于CARLA的数据驱动交通微观仿真框架，利用I-24 MOTION数据重构真实交通波动态。**

**关键词**: `交通微观仿真` `数据驱动仿真` `CARLA仿真` `交通波动态` `协同仿真` `边界控制`

## 📋 核心要点

1. 核心问题：传统微观仿真校准难以大规模复现交通波等短暂现象。
2. 方法要点：使用真实交通数据作为边界条件，通过协同仿真模块注入交通信息。
3. 实验或效果：在低和高拥堵场景中模拟波形成与消散，行为接近真实交通。

## 📄 摘要（原文）

> This paper introduces a data-driven traffic microsimulation framework in CARLA that reconstructs real-world wave dynamics using high-fidelity time-space data from the I-24 MOTION testbed. Calibration of road networks in microsimulators to reproduce ephemeral phenomena such as traffic waves for large-scale simulation is a process that is fraught with challenges. This work reconsiders the existence of the traffic state data as boundary conditions on an ego vehicle moving through previously recorded traffic data, rather than reproducing those traffic phenomena in a calibrated microsim. Our approach is to autogenerate a 1 mile highway segment corresponding to I-24, and use the I-24 data to power a cosimulation module that injects traffic information into the simulation. The CARLA and cosimulation simulations are centered around an ego vehicle sampled from the empirical data, with autogeneration of "visible" traffic within the longitudinal range of the ego vehicle. Boundary control beyond these visible ranges is achieved using ghost cells behind (upstream) and ahead (downstream) of the ego vehicle. Unlike prior simulation work that focuses on local car-following behavior or abstract geometries, our framework targets full time-space diagram fidelity as the validation objective. Leveraging CARLA's rich sensor suite and configurable vehicle dynamics, we simulate wave formation and dissipation in both low-congestion and high-congestion scenarios for qualitative analysis. The resulting emergent behavior closely mirrors that of real traffic, providing a novel cosimulation framework for evaluating traffic control strategies, perception-driven autonomy, and future deployment of wave mitigation solutions. Our work bridges microscopic modeling with physical experimental data, enabling the first perceptually realistic, boundary-driven simulation of empirical traffic wave phenomena in CARLA.


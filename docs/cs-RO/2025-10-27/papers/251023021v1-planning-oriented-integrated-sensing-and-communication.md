---
layout: default
title: Planning Oriented Integrated Sensing and Communication
---

# Planning Oriented Integrated Sensing and Communication

**arXiv**: [2510.23021v1](https://arxiv.org/abs/2510.23021) | [PDF](https://arxiv.org/pdf/2510.23021.pdf)

**作者**: Xibin Jin, Guoliang Li, Shuai Wang, Fan Liu, Miaowen Wen, Huseyin Arslan, Derrick Wing Kwan Ng, Chengzhong Xu

---

## 💡 一句话要点

**提出规划导向集成感知通信框架，以提升自动驾驶车辆的安全与效率**

**关键词**: `集成感知与通信` `自动驾驶规划` `功率分配优化` `安全边界建模` `双层优化问题`

## 📋 核心要点

1. 现有ISAC设计忽视关键障碍对运动效率的影响，导致感知与规划脱节
2. 基于Cramér-Rao Bound和占用膨胀原理，推导安全边界并构建双层优化问题
3. 仿真显示PISAC在成功率和通行时间上优于基准方法，验证其有效性

## 📄 摘要（原文）

> Integrated sensing and communication (ISAC) enables simultaneous
> localization, environment perception, and data exchange for connected
> autonomous vehicles. However, most existing ISAC designs prioritize sensing
> accuracy and communication throughput, treating all targets uniformly and
> overlooking the impact of critical obstacles on motion efficiency. To overcome
> this limitation, we propose a planning-oriented ISAC (PISAC) framework that
> reduces the sensing uncertainty of planning-bottleneck obstacles and expands
> the safe navigable path for the ego-vehicle, thereby bridging the gap between
> physical-layer optimization and motion-level planning. The core of PISAC lies
> in deriving a closed-form safety bound that explicitly links ISAC transmit
> power to sensing uncertainty, based on the Cram\'er-Rao Bound and occupancy
> inflation principles. Using this model, we formulate a bilevel power allocation
> and motion planning (PAMP) problem, where the inner layer optimizes the ISAC
> beam power distribution and the outer layer computes a collision-free
> trajectory under uncertainty-aware safety constraints. Comprehensive
> simulations in high-fidelity urban driving environments demonstrate that PISAC
> achieves up to 40% higher success rates and over 5% shorter traversal times
> than existing ISAC-based and communication-oriented benchmarks, validating its
> effectiveness in enhancing both safety and efficiency.


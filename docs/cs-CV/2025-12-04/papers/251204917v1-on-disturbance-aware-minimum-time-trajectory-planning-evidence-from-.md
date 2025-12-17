---
layout: default
title: On Disturbance-Aware Minimum-Time Trajectory Planning: Evidence from Tests on a Dynamic Driving Simulator
---

# On Disturbance-Aware Minimum-Time Trajectory Planning: Evidence from Tests on a Dynamic Driving Simulator

**arXiv**: [2512.04917v1](https://arxiv.org/abs/2512.04917) | [PDF](https://arxiv.org/pdf/2512.04917.pdf)

**作者**: Matteo Masoni, Vincenzo Palermo, Marco Gabiccini, Martino Gulisano, Giorgio Previati, Massimiliano Gobbi, Francesco Comolli, Gianpiero Mastinu, Massimo Guiggiani

---

## 💡 一句话要点

**提出扰动感知最小时间轨迹规划框架，在动态驾驶模拟器中评估专业驾驶员执行效果**

**关键词**: `扰动感知规划` `最小时间轨迹` `驾驶模拟器` `鲁棒性控制` `轨迹优化` `驾驶性能评估`

## 📋 核心要点

1. 研究扰动感知轨迹规划对驾驶性能的影响，比较名义最优、轨道限界鲁棒和摩擦限界鲁棒轨迹
2. 采用最小圈时目标与转向平滑正则化，通过专业驾驶员在虚拟赛道上执行轨迹进行实验
3. 结果显示摩擦限界鲁棒轨迹在圈时与转向努力间达到高效平衡，证实参考轨迹提升驾驶效率

## 📄 摘要（原文）

> This work investigates how disturbance-aware, robustness-embedded reference trajectories translate into driving performance when executed by professional drivers in a dynamic simulator. Three planned reference trajectories are compared against a free-driving baseline (NOREF) to assess trade-offs between lap time (LT) and steering effort (SE): NOM, the nominal time-optimal trajectory; TLC, a track-limit-robust trajectory obtained by tightening margins to the track edges; and FLC, a friction-limit-robust trajectory obtained by tightening against axle and tire saturation. All trajectories share the same minimum lap-time objective with a small steering-smoothness regularizer and are evaluated by two professional drivers using a high-performance car on a virtual track. The trajectories derive from a disturbance-aware minimum-lap-time framework recently proposed by the authors, where worst-case disturbance growth is propagated over a finite horizon and used to tighten tire-friction and track-limit constraints, preserving performance while providing probabilistic safety margins. LT and SE are used as performance indicators, while RMS lateral deviation, speed error, and drift angle characterize driving style. Results show a Pareto-like LT-SE trade-off: NOM yields the shortest LT but highest SE; TLC minimizes SE at the cost of longer LT; FLC lies near the efficient frontier, substantially reducing SE relative to NOM with only a small LT increase. Removing trajectory guidance (NOREF) increases both LT and SE, confirming that reference trajectories improve pace and control efficiency. Overall, the findings highlight reference-based and disturbance-aware planning, especially FLC, as effective tools for training and for achieving fast yet stable trajectories.


---
layout: default
title: A Cross-Embodiment Gripper Benchmark for Rigid-Object Manipulation in Aerial and Industrial Robotics
---

# A Cross-Embodiment Gripper Benchmark for Rigid-Object Manipulation in Aerial and Industrial Robotics

**arXiv**: [2512.01598v1](https://arxiv.org/abs/2512.01598) | [PDF](https://arxiv.org/pdf/2512.01598.pdf)

**作者**: Marek Vagas, Martin Varga, Jaroslav Romancik, Ondrej Majercak, Alejandro Suarez, Anibal Ollero, Bram Vanderborght, Ivan Virgala

---

## 💡 一句话要点

**提出跨具身夹爪基准以评估异构机器人系统中的夹爪性能与能量效率**

**关键词**: `跨具身基准` `夹爪性能评估` `能量效率` `机器人操作` `空中机器人` `工业机器人`

## 📋 核心要点

1. 现有基准如YCB和NIST未评估跨具身可转移性或能量感知性能，限制了移动和空中操作应用
2. 引入CEGB基准，扩展YCB和NIST指标，包括转移时间、能耗和理想载荷评估
3. 实验显示原型夹爪转移快、能耗低、抓取成功率高，验证基准的实用性和可重复性

## 📄 摘要（原文）

> Robotic grippers are increasingly deployed across industrial, collaborative, and aerial platforms, where each embodiment imposes distinct mechanical, energetic, and operational constraints. Established YCB and NIST benchmarks quantify grasp success, force, or timing on a single platform, but do not evaluate cross-embodiment transferability or energy-aware performance, capabilities essential for modern mobile and aerial manipulation. This letter introduces the Cross-Embodiment Gripper Benchmark (CEGB), a compact and reproducible benchmarking suite extending YCB and selected NIST metrics with three additional components: a transfer-time benchmark measuring the practical effort required to exchange embodiments, an energy-consumption benchmark evaluating grasping and holding efficiency, and an intent-specific ideal payload assessment reflecting design-dependent operational capability. Together, these metrics characterize both grasp performance and the suitability of reusing a single gripper across heterogeneous robotic systems. A lightweight self-locking gripper prototype is implemented as a reference case. Experiments demonstrate rapid embodiment transfer (median ~= 17.6 s across user groups), low holding energy for gripper prototype (~= 1.5 J per 10 s), and consistent grasp performance with cycle times of 3.2 - 3.9 s and success rates exceeding 90%. CEGB thus provides a reproducible foundation for cross-platform, energy-aware evaluation of grippers in aerial and manipulators domains.


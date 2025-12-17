---
layout: default
title: CoLD Fusion: A Real-time Capable Spline-based Fusion Algorithm for Collective Lane Detection
---

# CoLD Fusion: A Real-time Capable Spline-based Fusion Algorithm for Collective Lane Detection

**arXiv**: [2512.14355v1](https://arxiv.org/abs/2512.14355) | [PDF](https://arxiv.org/pdf/2512.14355.pdf)

**作者**: Jörg Gamerdinger, Sven Teufel, Georg Volk, Oliver Bringmann

**分类**: cs.RO

**发布日期**: 2025-12-16

**备注**: Accepted at IEEE IV 2023

**DOI**: [10.1109/IV55152.2023.10186632](https://doi.org/10.1109/IV55152.2023.10186632)

---

## 💡 一句话要点

**提出基于样条的实时集体车道检测融合算法，以扩展自动驾驶车辆在传感器受限场景下的感知范围。**

🎯 **匹配领域**: **自动驾驶** **视觉里程计**

**关键词**: `集体感知` `车道检测` `样条估计` `车对车通信` `实时融合` `自动驾驶` `传感器融合` `道路建模`

## 📋 核心要点

1. 现有方法在传感器范围受限、遮挡和弯道场景下难以实现完整车道感知，导致自动驾驶车辆依赖局部信息，影响安全规划。
2. 论文提出基于样条的集体车道检测融合算法，通过车对车通信整合多车感知数据，实时估计未检测道路段，扩展感知范围。
3. 实验在多种道路类型下进行，算法实现实时运行，感知范围提升高达200%，验证了集体感知的有效性和实用性。

## 📝 摘要（中文）

全面的环境感知对于自动驾驶车辆的安全运行至关重要，需要检测动态道路使用者和静态对象如交通标志或车道，以支持安全运动规划。然而，在许多情况下，由于传感器范围有限、遮挡和弯道等因素，无法实现对其他对象或车道的完整感知。在无法精确定位或没有高清地图的道路场景中，自动驾驶车辆必须仅依赖其感知的道路信息。因此，通过车对车通信利用集体感知来扩展本地感知能力是一种有前景的策略，但尚未在车道检测中得到探索。为此，我们提出了一种实时可行的集体车道感知方法，使用基于样条的估计来预测未检测到的道路段。我们在多种情况和道路类型下评估了所提出的融合算法，实现了实时能力，并将感知范围扩展了高达200%。

## 🔬 方法详解

论文提出CoLD Fusion算法，整体框架基于车对车通信实现集体车道检测。核心方法采用样条曲线建模道路几何，通过融合多车传感器数据，实时估计未检测区域的车道线。关键技术创新点在于将样条估计与集体感知结合，动态更新道路模型，以应对传感器局限。与现有方法的主要区别在于首次将集体感知应用于车道检测，并实现实时处理，避免了依赖高清地图或单一车辆感知的不足。

## 📊 实验亮点

实验结果显示，CoLD Fusion算法在多种道路场景下实现实时运行，感知范围扩展高达200%，显著提升了车道检测的覆盖率和鲁棒性，验证了集体感知策略的有效性。

## 🎯 应用场景

该研究主要应用于自动驾驶领域，特别是在传感器受限、无高清地图或复杂道路环境中，如城市弯道、高速公路遮挡区域，能提升车辆安全性和规划能力，支持智能交通系统的发展。

## 📄 摘要（原文）

> Comprehensive environment perception is essential for autonomous vehicles to operate safely. It is crucial to detect both dynamic road users and static objects like traffic signs or lanes as these are required for safe motion planning. However, in many circumstances a complete perception of other objects or lanes is not achievable due to limited sensor ranges, occlusions, and curves. In scenarios where an accurate localization is not possible or for roads where no HD maps are available, an autonomous vehicle must rely solely on its perceived road information. Thus, extending local sensing capabilities through collective perception using vehicle-to-vehicle communication is a promising strategy that has not yet been explored for lane detection. Therefore, we propose a real-time capable approach for collective perception of lanes using a spline-based estimation of undetected road sections. We evaluate our proposed fusion algorithm in various situations and road types. We were able to achieve real-time capability and extend the perception range by up to 200%.


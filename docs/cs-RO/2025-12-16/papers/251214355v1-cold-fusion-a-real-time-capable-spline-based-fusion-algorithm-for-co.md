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

**提出基于样条的实时集体车道检测融合算法，以扩展自动驾驶车辆在传感器受限或高精度地图缺失场景下的感知范围。**

**关键词**: `集体感知` `车道检测` `样条估计` `车对车通信` `实时融合` `自动驾驶` `环境感知` `传感器融合`

## 📋 核心要点

1. 现有车道检测方法受限于传感器范围、遮挡和弯道，导致感知不完整，尤其在无高精度地图或定位不准时，自动驾驶车辆面临安全风险。
2. 论文提出基于样条的集体感知融合算法，通过车对车通信整合多车数据，实时估计未检测道路段，以扩展感知范围。
3. 实验表明，该方法在多种道路场景下实现实时处理，感知范围提升高达200%，显著增强了自动驾驶系统的环境感知能力。

## 📝 摘要（中文）

全面的环境感知对于自动驾驶车辆的安全运行至关重要，需要检测动态道路使用者和静态对象如交通标志或车道，以支持安全运动规划。然而，由于传感器范围有限、遮挡和弯道等因素，在许多情况下无法实现对其他对象或车道的完整感知。在无法精确定位或没有高精度地图的道路场景中，自动驾驶车辆必须仅依赖其感知的道路信息。因此，通过车对车通信利用集体感知扩展本地感知能力是一种有前景的策略，但尚未在车道检测中得到探索。为此，我们提出了一种实时可行的集体车道感知方法，使用基于样条的估计来预测未检测到的道路段。我们在多种情况和道路类型下评估了所提出的融合算法，实现了实时能力，并将感知范围扩展了高达200%。

## 🔬 方法详解

论文提出CoLD Fusion算法，整体框架基于车对车通信实现集体感知，核心是使用样条曲线对未检测车道段进行估计和融合。关键技术创新点在于结合实时样条拟合与多源数据融合，优化了计算效率，确保在动态环境中快速响应。与现有方法的主要区别在于首次将集体感知应用于车道检测，通过通信扩展本地感知，而非仅依赖单一车辆传感器或静态地图。

## 📊 实验亮点

实验结果显示，CoLD Fusion算法在多种道路类型下均能实现实时处理，感知范围扩展高达200%，有效克服了传统方法的局限性，显著提升了自动驾驶车辆在复杂环境中的感知能力。

## 🎯 应用场景

该研究主要应用于自动驾驶领域，特别是在传感器受限、遮挡严重或缺乏高精度地图的城市和乡村道路场景中，通过集体感知提升车道检测的可靠性和安全性，支持更稳健的运动规划和决策。

## 📄 摘要（原文）

> Comprehensive environment perception is essential for autonomous vehicles to operate safely. It is crucial to detect both dynamic road users and static objects like traffic signs or lanes as these are required for safe motion planning. However, in many circumstances a complete perception of other objects or lanes is not achievable due to limited sensor ranges, occlusions, and curves. In scenarios where an accurate localization is not possible or for roads where no HD maps are available, an autonomous vehicle must rely solely on its perceived road information. Thus, extending local sensing capabilities through collective perception using vehicle-to-vehicle communication is a promising strategy that has not yet been explored for lane detection. Therefore, we propose a real-time capable approach for collective perception of lanes using a spline-based estimation of undetected road sections. We evaluate our proposed fusion algorithm in various situations and road types. We were able to achieve real-time capability and extend the perception range by up to 200%.


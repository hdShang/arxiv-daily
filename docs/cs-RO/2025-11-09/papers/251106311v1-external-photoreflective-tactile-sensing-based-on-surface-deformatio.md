---
layout: default
title: External Photoreflective Tactile Sensing Based on Surface Deformation Measurement
---

# External Photoreflective Tactile Sensing Based on Surface Deformation Measurement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06311" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06311v1</a>
  <a href="https://arxiv.org/pdf/2511.06311.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06311v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06311v1', 'External Photoreflective Tactile Sensing Based on Surface Deformation Measurement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seiichi Yamamoto, Hiroki Ishizuka, Takumi Kawasetsu, Koh Hosoda, Takayuki Kameoka, Kango Yanagida, Takato Horii, Sei Ikeda, Osamu Oshiro

**分类**: cs.RO

**发布日期**: 2025-11-09

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**提出一种基于表面形变测量的外置光反射触觉传感方法，用于软体机器人。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `触觉传感` `软体机器人` `表面形变` `光反射` `力估计`

## 📋 核心要点

1. 软体机器人触觉感知面临传感器易损坏、集成复杂、维护困难等问题。
2. 该方法通过外置光反射模块读取硅胶皮肤的表面形变来估计接触力，无需嵌入传感器。
3. 实验验证了该方法具有良好的力输出特性、低滞后、高重复性，并成功集成到软体机器人夹爪上。

## 📝 摘要（中文）

本文提出了一种触觉传感方法，该方法利用软体机器人的机械柔顺性。一个可外部连接的光反射模块读取硅胶皮肤的表面形变，从而估计接触力，而无需嵌入触觉传感器。将传感器置于接触界面之外，降低了损坏风险，保持了柔软性，并简化了制造和维护。首先，对光学传感元件和柔顺皮肤进行表征，然后确定原型触觉传感器的设计。压缩实验验证了该方法，展示了与理论一致的单调力输出关系、低滞后、重复循环的高重复性以及小的响应压痕速度。进一步演示了在软体机器人夹爪上的集成，该模块可靠地检测抓取事件。与液体填充或嵌入导线的触觉皮肤相比，所提出的模块化附加架构增强了耐用性，降低了布线复杂性，并支持在各种机器人几何形状中直接部署。由于传感原理读取皮肤应变模式，因此也暗示了对其他体感线索的扩展，例如从表面形变估计关节角度或执行器状态。总而言之，利用表面柔顺性和外部光学模块为软体机器人配备力感知提供了一种实用且稳健的途径，同时保持了结构灵活性和可制造性，为机器人应用和安全的人机协作铺平了道路。

## 🔬 方法详解

**问题定义**：软体机器人需要可靠的触觉感知能力，但传统的触觉传感器存在易损坏、集成复杂、影响机器人本体柔软性等问题。现有方法如液体填充或嵌入导线的触觉皮肤，在耐用性、布线复杂性和通用性方面存在局限性。因此，需要一种更鲁棒、易于集成和维护的触觉传感方案。

**核心思路**：该论文的核心思路是利用软体机器人表面的形变与接触力之间的关系，通过非接触式光学方法测量表面形变，从而推断接触力的大小和位置。将传感器模块外置，避免了直接接触带来的损坏风险，同时保持了机器人本体的柔软性。

**技术框架**：该触觉传感系统的整体架构包括：1) 柔顺的硅胶皮肤，作为力传递和形变发生的介质；2) 外置的光反射模块，用于测量硅胶皮肤的表面形变；3) 信号处理和力估计模块，将形变数据转换为接触力信息。光反射模块通常包含光源和图像传感器，通过分析反射光的图案变化来确定表面形变。

**关键创新**：该方法最重要的创新点在于将触觉传感从传统的嵌入式方案转变为外置式方案。通过非接触式光学测量，避免了传感器与接触界面的直接接触，显著提高了传感器的耐用性和可靠性。此外，该方案的模块化设计使得传感器易于集成和维护，并可应用于不同几何形状的软体机器人。

**关键设计**：硅胶皮肤的材料选择和几何形状设计至关重要，需要保证在一定力范围内产生可测量的形变，同时避免过度形变导致测量误差。光反射模块的光源类型、图像传感器分辨率和镜头参数需要根据实际应用场景进行优化，以获得清晰的形变图像。力估计算法需要根据硅胶皮肤的力学特性进行标定，建立形变与力之间的准确映射关系。

## 📊 实验亮点

实验结果表明，该触觉传感器具有良好的力输出特性，表现出与理论一致的单调关系。重复压缩实验显示出低滞后和高重复性。在软体机器人夹爪上的集成实验中，该模块能够可靠地检测抓取事件。这些结果验证了该方法在软体机器人触觉感知方面的有效性和实用性。

## 🎯 应用场景

该研究成果可广泛应用于软体机器人、人机协作、医疗康复等领域。例如，在软体机器人夹爪上集成该触觉传感器，可以实现对物体的精确抓取和操作，避免损坏脆弱物体。在医疗康复领域，可以用于开发具有触觉反馈的假肢或康复机器人，提高患者的生活质量。此外，该技术还可以扩展到其他体感线索的估计，例如关节角度或执行器状态。

## 📄 摘要（原文）

> We present a tactile sensing method enabled by the mechanical compliance of soft robots; an externally attachable photoreflective module reads surface deformation of silicone skin to estimate contact force without embedding tactile transducers. Locating the sensor off the contact interface reduces damage risk, preserves softness, and simplifies fabrication and maintenance. We first characterize the optical sensing element and the compliant skin, thendetermine the design of a prototype tactile sensor. Compression experiments validate the approach, exhibiting a monotonic force output relationship consistent with theory, low hysteresis, high repeatability over repeated cycles, and small response indentation speeds. We further demonstrate integration on a soft robotic gripper, where the module reliably detects grasp events. Compared with liquid filled or wireembedded tactile skins, the proposed modular add on architecture enhances durability, reduces wiring complexity, and supports straightforward deployment across diverse robot geometries. Because the sensing principle reads skin strain patterns, it also suggests extensions to other somatosensory cues such as joint angle or actuator state estimation from surface deformation. Overall, leveraging surface compliance with an external optical module provides a practical and robust route to equip soft robots with force perception while preserving structural flexibility and manufacturability, paving the way for robotic applications and safe human robot collaboration.


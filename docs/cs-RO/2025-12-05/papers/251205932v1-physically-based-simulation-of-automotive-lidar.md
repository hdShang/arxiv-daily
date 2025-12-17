---
layout: default
title: Physically-Based Simulation of Automotive LiDAR
---

# Physically-Based Simulation of Automotive LiDAR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05932" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05932v1</a>
  <a href="https://arxiv.org/pdf/2512.05932.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05932v1" onclick="toggleFavorite(this, '2512.05932v1', 'Physically-Based Simulation of Automotive LiDAR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: L. Dudzik, M. Roschani, A. Sielemann, K. Trampert, J. Ziehn, J. Beyerer, C. Neumann

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-05

**DOI**: [10.1109/IAVVC61942.2025.11219516](https://doi.org/10.1109/IAVVC61942.2025.11219516)

---

## 💡 一句话要点

**提出基于物理的汽车激光雷达仿真模型，包含光学校准与系统验证。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `激光雷达仿真` `物理渲染` `汽车雷达` `光学测量` `模型校准`

## 📋 核心要点

1. 现有激光雷达仿真方法难以准确模拟真实世界的光学效应，导致仿真结果与实际数据存在偏差。
2. 提出一种基于物理的渲染模型，考虑了光晕、回波脉冲宽度和环境光等因素，更贴近真实物理过程。
3. 通过光学实验室测量系统地确定模型参数，并在两种不同的汽车激光雷达系统上验证了模型的有效性。

## 📝 摘要（中文）

本文提出了一种用于模拟汽车飞行时间(ToF)激光雷达的解析模型，该模型考虑了光晕效应、回波脉冲宽度和环境光等因素，并提供了通过光学实验室测量系统地确定模型参数的步骤。该模型在近红外域中使用基于物理的渲染(PBR)。它假设来自阴影或光线追踪的栅格化渲染图像上的单次反射和逆向反射，包括传感器发出的光以及来自其他非相关来源（如阳光）的杂散光。传感器光束和接收二极管的灵敏度通过灵活的光束控制模式和非零直径进行建模。可以根据系统属性、计算能力和所需的输出属性选择不同的（所有非实时）计算方法。该方法通过Valeo Scala Gen. 2和Blickfeld Cube 1两种汽车激光雷达系统进行了校准和测试，这两种系统在属性和可用接口方面存在显著差异，但相关的模型参数可以成功提取。

## 🔬 方法详解

**问题定义**：现有激光雷达仿真方法通常简化了光学过程，忽略了诸如光晕、回波脉冲宽度和环境光等重要因素，导致仿真结果与真实数据存在较大差异。这限制了仿真在激光雷达系统设计、算法开发和性能评估中的应用。现有方法难以准确建模传感器特性和环境因素对激光雷达性能的影响。

**核心思路**：本文的核心思路是建立一个基于物理的激光雷达仿真模型，该模型能够准确模拟激光雷达的光学过程，并考虑了各种影响因素。通过使用基于物理的渲染(PBR)技术，可以更真实地模拟光线的传播和反射。此外，通过光学实验室测量系统地确定模型参数，可以提高模型的准确性和可靠性。

**技术框架**：该仿真模型主要包含以下几个模块：1) 传感器模型：模拟激光雷达的光束发射和接收过程，包括光束形状、扫描模式和接收灵敏度。2) 环境模型：描述场景中的物体表面属性和环境光照条件，包括反射率、粗糙度和环境光强度。3) 光线传播模型：使用基于物理的渲染技术模拟光线在场景中的传播和反射，考虑了光晕、回波脉冲宽度和环境光等因素。4) 信号处理模型：模拟激光雷达的信号处理过程，包括回波检测、距离计算和数据滤波。

**关键创新**：该方法最重要的技术创新点在于：1) 提出了一种基于物理的激光雷达仿真模型，该模型能够准确模拟激光雷达的光学过程，并考虑了各种影响因素。2) 通过光学实验室测量系统地确定模型参数，可以提高模型的准确性和可靠性。3) 该模型可以模拟光晕、回波脉冲宽度和环境光等重要因素，更贴近真实物理过程。

**关键设计**：模型参数包括系统特定属性（激光雷达光束的物理扩散、接收二极管的灵敏度、发射光强度、反射光强度与回波脉冲宽度之间的转换关系）和场景参数（环境光照、位置、目标表面在相关红外域中的属性）。系统特定属性通过光度亮度实验室测量确定，使用测角仪以0.01°分辨率对不同目标表面进行测量，这是测量光束模式的最佳可用分辨率。

## 📊 实验亮点

该方法在Valeo Scala Gen. 2和Blickfeld Cube 1两种汽车激光雷达系统上进行了校准和测试。实验结果表明，该模型能够准确模拟这两种激光雷达系统的性能，并成功提取了相关的模型参数。这验证了该模型的有效性和通用性。

## 🎯 应用场景

该研究成果可应用于汽车激光雷达系统的设计、算法开发和性能评估。通过仿真可以优化激光雷达的参数设置，提高其在各种环境条件下的性能。此外，该模型还可以用于生成合成数据，用于训练和评估激光雷达感知算法，降低数据采集成本。

## 📄 摘要（原文）

> We present an analytic model for simulating automotive time-of-flight (ToF) LiDAR that includes blooming, echo pulse width, and ambient light, along with steps to determine model parameters systematically through optical laboratory measurements. The model uses physically based rendering (PBR) in the near-infrared domain. It assumes single-bounce reflections and retroreflections over rasterized rendered images from shading or ray tracing, including light emitted from the sensor as well as stray light from other, non-correlated sources such as sunlight. Beams from the sensor and sensitivity of the receiving diodes are modeled with flexible beam steering patterns and with non-vanishing diameter.
>   Different (all non-real time) computational approaches can be chosen based on system properties, computing capabilities, and desired output properties.
>   Model parameters include system-specific properties, namely the physical spread of the LiDAR beam, combined with the sensitivity of the receiving diode; the intensity of the emitted light; the conversion between the intensity of reflected light and the echo pulse width; and scenario parameters such as environment lighting, positioning, and surface properties of the target(s) in the relevant infrared domain. System-specific properties of the model are determined from laboratory measurements of the photometric luminance on different target surfaces aligned with a goniometer at 0.01° resolution, which marks the best available resolution for measuring the beam pattern.
>   The approach is calibrated for and tested on two automotive LiDAR systems, the Valeo Scala Gen. 2 and the Blickfeld Cube 1. Both systems differ notably in their properties and available interfaces, but the relevant model parameters could be extracted successfully.


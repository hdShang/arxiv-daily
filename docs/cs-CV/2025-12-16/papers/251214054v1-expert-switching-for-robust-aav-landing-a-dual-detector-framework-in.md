---
layout: default
title: Expert Switching for Robust AAV Landing: A Dual-Detector Framework in Simulation
---

# Expert Switching for Robust AAV Landing: A Dual-Detector Framework in Simulation

**arXiv**: [2512.14054v1](https://arxiv.org/abs/2512.14054) | [PDF](https://arxiv.org/pdf/2512.14054.pdf)

**作者**: Humaira Tasnim, Ashik E Rasul, Bruce Jo, Hyung-Jin Yoon

**分类**: cs.RO, cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于双检测器的专家切换框架，以解决自主空中车辆在降落过程中因尺度变化导致的停机坪检测鲁棒性问题。**

**关键词**: `自主空中车辆` `停机坪检测` `尺度自适应` `双专家框架` `几何门控` `视觉感知` `仿真评估` `YOLOv8`

## 📋 核心要点

1. 核心问题：单检测器在AAV降落过程中因停机坪尺度剧烈变化（从高空小目标到近地大目标）导致检测鲁棒性不足。
2. 方法要点：提出双专家感知框架，训练两个YOLOv8专家分别处理远距离和近距离尺度，通过几何门控机制自适应切换专家。
3. 实验或效果：在CARLA与GUAM集成的仿真环境中，相比单检测器基线，显著提升了对齐稳定性、降落精度和整体鲁棒性。

## 📝 摘要（中文）

可靠的停机坪检测对于自主空中车辆（AAV）降落至关重要，尤其是在GPS失效或视觉条件退化的情况下。虽然现代检测器如YOLOv8提供了强大的基线性能，但单模型管道在降落过程中经历的极端尺度转换下难以保持鲁棒性，其中停机坪在高空时显得小而低分辨率，在接近着陆时则占据视野主导。为应对这一限制，本文提出了一种尺度自适应的双专家感知框架，将检测任务分解为远距离和近距离两个阶段。两个YOLOv8专家在HelipadCat数据集的尺度专门化版本上进行训练，使一个模型擅长检测小而低分辨率的停机坪，另一个在目标主导视野时提供高精度定位。在推理过程中，两个专家并行运行，几何门控机制选择与AAV视点最一致的预测专家。这种自适应路由防止了单检测器系统在宽高度范围内操作时常见的性能退化。双专家感知模块在闭环降落环境中进行评估，该环境集成了CARLA的光真实感渲染与NASA的GUAM飞行动力学引擎。结果显示，与单检测器基线相比，在对齐稳定性、降落精度和整体鲁棒性方面有显著提升。通过引入针对降落问题定制的尺度感知专家路由策略，这项工作推进了自主下降的弹性视觉感知，并为未来多专家AAV框架奠定了基础。

## 🔬 方法详解

论文提出一种尺度自适应的双专家感知框架，整体框架包括两个并行运行的YOLOv8检测器，分别作为远距离和近距离专家，训练于HelipadCat数据集的尺度专门化版本。关键技术创新点是几何门控机制，它基于AAV的视点（如高度和视角）动态选择最一致的专家预测，实现自适应路由。与现有方法的主要区别在于，传统单检测器系统难以处理降落过程中的极端尺度变化，而本框架通过专家分解和切换策略，专门针对尺度变化问题进行了优化，提升了检测鲁棒性和精度。

## 📊 实验亮点

在CARLA与NASA GUAM集成的闭环仿真环境中，双专家框架相比单检测器基线，在停机坪检测上实现了显著提升：对齐稳定性增强，降落精度提高，整体鲁棒性改善，验证了尺度自适应策略的有效性。

## 🎯 应用场景

该研究主要应用于自主空中车辆的视觉引导降落场景，特别是在GPS失效或恶劣视觉条件下，如军事侦察、紧急救援或无人机物流。其潜在价值在于提高AAV在复杂环境中的自主性和安全性，为未来多专家感知系统提供基础。

## 📄 摘要（原文）

> Reliable helipad detection is essential for Autonomous Aerial Vehicle (AAV) landing, especially under GPS-denied or visually degraded conditions. While modern detectors such as YOLOv8 offer strong baseline performance, single-model pipelines struggle to remain robust across the extreme scale transitions that occur during descent, where helipads appear small at high altitude and large near touchdown. To address this limitation, we propose a scale-adaptive dual-expert perception framework that decomposes the detection task into far-range and close-range regimes. Two YOLOv8 experts are trained on scale-specialized versions of the HelipadCat dataset, enabling one model to excel at detecting small, low-resolution helipads and the other to provide high-precision localization when the target dominates the field of view. During inference, both experts operate in parallel, and a geometric gating mechanism selects the expert whose prediction is most consistent with the AAV's viewpoint. This adaptive routing prevents the degradation commonly observed in single-detector systems when operating across wide altitude ranges. The dual-expert perception module is evaluated in a closed-loop landing environment that integrates CARLA's photorealistic rendering with NASA's GUAM flight-dynamics engine. Results show substantial improvements in alignment stability, landing accuracy, and overall robustness compared to single-detector baselines. By introducing a scale-aware expert routing strategy tailored to the landing problem, this work advances resilient vision-based perception for autonomous descent and provides a foundation for future multi-expert AAV frameworks.


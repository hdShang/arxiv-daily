---
layout: default
title: Ariel-ML: Computing Parallelization with Embedded Rust for Neural Networks on Heterogeneous Multi-core Microcontrollers
---

# Ariel-ML: Computing Parallelization with Embedded Rust for Neural Networks on Heterogeneous Multi-core Microcontrollers

**arXiv**: [2512.09800v1](https://arxiv.org/abs/2512.09800) | [PDF](https://arxiv.org/pdf/2512.09800.pdf)

**作者**: Zhaolan Huang, Kaspar Schleiser, Gyungmin Myung, Emmanuel Baccelli

---

## 💡 一句话要点

**提出Ariel-ML工具包，在异构多核微控制器上实现嵌入式Rust的神经网络并行化推理**

**关键词**: `嵌入式Rust` `多核微控制器` `TinyML推理` `并行化计算` `边缘AI`

## 📋 核心要点

1. 问题：现有嵌入式Rust平台缺乏自动化并行化工具，无法在多核MCU上高效执行TinyML模型推理
2. 方法：结合通用TinyML流程与嵌入式Rust平台，支持多种32位微控制器架构（如Arm Cortex-M、RISC-V、ESP-32）的多核优化
3. 效果：在推理延迟上优于现有方法，内存占用与嵌入式C/C++工具包相当，提供开源实现和基准测试

## 📄 摘要（原文）

> Low-power microcontroller (MCU) hardware is currently evolving from single-core architectures to predominantly multi-core architectures. In parallel, new embedded software building blocks are more and more written in Rust, while C/C++ dominance fades in this domain. On the other hand, small artificial neural networks (ANN) of various kinds are increasingly deployed in edge AI use cases, thus deployed and executed directly on low-power MCUs. In this context, both incremental improvements and novel innovative services will have to be continuously retrofitted using ANNs execution in software embedded on sensing/actuating systems already deployed in the field. However, there was so far no Rust embedded software platform automating parallelization for inference computation on multi-core MCUs executing arbitrary TinyML models. This paper thus fills this gap by introducing Ariel-ML, a novel toolkit we designed combining a generic TinyML pipeline and an embedded Rust software platform which can take full advantage of multi-core capabilities of various 32bit microcontroller families (Arm Cortex-M, RISC-V, ESP-32). We published the full open source code of its implementation, which we used to benchmark its capabilities using a zoo of various TinyML models. We show that Ariel-ML outperforms prior art in terms of inference latency as expected, and we show that, compared to pre-existing toolkits using embedded C/C++, Ariel-ML achieves comparable memory footprints. Ariel-ML thus provides a useful basis for TinyML practitioners and resource-constrained embedded Rust developers.


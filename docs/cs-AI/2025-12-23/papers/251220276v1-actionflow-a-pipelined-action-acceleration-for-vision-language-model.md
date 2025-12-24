---
layout: default
title: ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge
---

# ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20276" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20276v1</a>
  <a href="https://arxiv.org/pdf/2512.20276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20276v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20276v1', 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuntao Dai, Hang Gu, Teng Wang, Qianyu Cheng, Yifei Zheng, Zhiyong Qiu, Lei Gong, Wenqi Lou, Xuehai Zhou

**分类**: cs.AI, cs.RO

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**ActionFlow：边缘设备上视觉语言模型流水线式动作加速框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `边缘计算` `模型推理加速` `流水线调度` `机器人控制`

## 📋 核心要点

1. VLA模型推理速度慢，难以满足边缘设备上实时机器人控制的需求，现有优化方法常需重训练或牺牲精度。
2. ActionFlow通过跨请求流水线调度，将VLA推理分解为微请求宏流水线，优化内存和计算资源的利用。
3. ActionFlow在OpenVLA-7B模型上实现了2.55倍的FPS提升，无需重新训练，支持边缘设备上的实时动态操作。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型已成为机器人感知和控制的统一范式，实现了涌现泛化和长时程任务执行。然而，由于推理延迟高，它们在动态、真实世界环境中的部署受到严重阻碍。平滑的机器人交互需要20到30Hz的控制频率，但由于自回归解码的内存限制，当前的VLA模型在边缘设备上通常仅以3-5Hz运行。现有的优化方法通常需要大量的重新训练或牺牲模型精度。为了弥合这一差距，我们引入了ActionFlow，这是一个为资源受限的边缘平台量身定制的系统级推理框架。ActionFlow的核心是一种跨请求流水线策略，这是一种新颖的调度器，它将VLA推理重新定义为微请求的宏流水线。该策略智能地将内存受限的解码阶段与计算受限的预填充阶段在连续的时间步长上进行批处理，以最大限度地提高硬件利用率。此外，为了支持这种调度，我们提出了一种跨请求状态打包前向算子和一个统一的KV环形缓冲区，它们将碎片化的内存操作融合为高效的密集计算。实验结果表明，ActionFlow在OpenVLA-7B模型上实现了2.55倍的FPS提升，无需重新训练，从而能够在边缘硬件上实现实时的动态操作。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作(VLA)模型在边缘设备上推理速度慢，无法满足实时机器人控制的需求。自回归解码过程中的内存访问成为瓶颈，导致推理延迟高。现有的优化方法，如模型压缩或量化，通常需要大量的重新训练，或者会降低模型的精度。因此，如何在资源受限的边缘设备上加速VLA模型的推理，同时保持模型精度，是一个亟待解决的问题。

**核心思路**：ActionFlow的核心思路是将VLA模型的推理过程视为一个流水线，通过跨请求的调度，将内存受限的解码阶段和计算受限的预填充阶段进行并行处理，从而提高硬件资源的利用率。这种流水线式的处理方式可以有效地隐藏内存访问的延迟，并减少计算资源的空闲时间。通过将多个请求的解码和预填充阶段进行批处理，可以进一步提高硬件的利用率。

**技术框架**：ActionFlow的整体框架包括以下几个主要模块：1) 跨请求流水线调度器：负责将VLA模型的推理过程分解为微请求，并根据硬件资源的利用情况，对这些微请求进行调度。2) 跨请求状态打包前向算子：将多个请求的状态信息打包在一起，减少内存访问的次数，提高计算效率。3) 统一的KV环形缓冲区：用于存储VLA模型在推理过程中产生的键值对(KV)信息，采用环形缓冲区的结构可以有效地管理内存，并减少内存分配和释放的开销。

**关键创新**：ActionFlow最重要的技术创新点在于其跨请求流水线调度策略。与传统的推理方法不同，ActionFlow不是一次性处理一个请求，而是将多个请求的解码和预填充阶段进行批处理，从而提高硬件资源的利用率。此外，跨请求状态打包前向算子和统一的KV环形缓冲区也是重要的创新点，它们可以有效地减少内存访问的次数，并提高计算效率。

**关键设计**：ActionFlow的关键设计包括：1) 流水线调度器的调度策略，需要根据硬件资源的利用情况，动态地调整解码和预填充阶段的批处理大小。2) 跨请求状态打包前向算子的打包策略，需要考虑不同请求之间的依赖关系，避免出现数据竞争。3) 统一的KV环形缓冲区的大小，需要根据VLA模型的规模和请求的数量进行调整，以保证内存的有效利用。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20276v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20276v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20276v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ActionFlow在OpenVLA-7B模型上实现了显著的性能提升，在不进行任何模型重训练的情况下，FPS提高了2.55倍。这意味着在相同的硬件条件下，ActionFlow可以使VLA模型的推理速度提高一倍以上，从而满足实时机器人控制的需求。实验结果表明，ActionFlow是一种有效的VLA模型加速框架，可以在边缘设备上实现高性能的推理。

## 🎯 应用场景

ActionFlow可广泛应用于机器人、自动驾驶、智能家居等领域。通过加速VLA模型在边缘设备上的推理速度，可以实现更快速、更流畅的机器人控制和人机交互。例如，在机器人操作场景中，ActionFlow可以使机器人能够实时地感知环境，并根据指令做出相应的动作，从而提高机器人的工作效率和安全性。在自动驾驶领域，ActionFlow可以使车辆能够更快地识别交通信号和障碍物，从而提高驾驶的安全性。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.


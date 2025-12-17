---
layout: default
title: GATO: GPU-Accelerated and Batched Trajectory Optimization for Scalable Edge Model Predictive Control
---

# GATO: GPU-Accelerated and Batched Trajectory Optimization for Scalable Edge Model Predictive Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07625" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07625v1</a>
  <a href="https://arxiv.org/pdf/2510.07625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07625v1" onclick="toggleFavorite(this, '2510.07625v1', 'GATO: GPU-Accelerated and Batched Trajectory Optimization for Scalable Edge Model Predictive Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexander Du, Emre Adabag, Gabriel Bravo, Brian Plancher

**分类**: cs.RO, eess.SY

**发布日期**: 2025-10-08

---

## 💡 一句话要点

**GATO：用于可扩展边缘模型预测控制的GPU加速批量轨迹优化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `轨迹优化` `GPU加速` `批量求解` `实时控制`

## 📋 核心要点

1. 现有GPU加速的轨迹优化方法在实时性和模型通用性上存在局限，无法满足中等批量大小的MPC应用需求。
2. GATO通过算法、软件和硬件协同设计，利用块级、warp级和线程级并行性，实现了GPU加速的批量轨迹优化。
3. 实验表明，GATO相比CPU基线加速18-21倍，相比GPU基线加速1.4-16倍，并在工业机械臂上验证了其有效性。

## 📝 摘要（中文）

模型预测控制(MPC)在机器人应用中表现出色，但在线求解非线性轨迹优化(TO)问题仍然计算密集。现有的GPU加速方法通常(i)并行化单个求解以满足实时性要求，(ii)以低于实时的速率扩展到非常大的批次，或(iii)通过限制模型通用性(例如，质点动力学或单个线性化)来提高速度。这使得许多需要实时处理数十到数百个批次求解的先进MPC应用在求解器性能方面存在巨大差距。因此，我们提出了GATO，一个开源的、GPU加速的、批量TO求解器，它在算法、软件和计算硬件上协同设计，为这些中等批量大小的场景提供实时吞吐量。我们的方法利用块级、warp级和线程级并行性，在求解内部和跨求解之间实现超高性能。我们通过以下方式证明了我们方法的有效性：模拟基准测试显示，随着批次大小的增加，相对于CPU基线加速18-21倍，相对于GPU基线加速1.4-16倍；案例研究突出了改进的抗扰动性和收敛行为；最后是在使用工业机械臂的硬件上进行验证。我们开源GATO以支持可重复性和采用。

## 🔬 方法详解

**问题定义**：论文旨在解决模型预测控制（MPC）中，在线求解批量非线性轨迹优化（TO）问题时，现有GPU加速方法无法兼顾实时性、模型通用性和中等批量大小处理能力的问题。现有方法要么只能并行化单个求解，要么只能处理非常大的批次但速度较慢，要么限制模型通用性，无法满足实际应用需求。

**核心思路**：GATO的核心思路是利用GPU的并行计算能力，通过算法、软件和硬件的协同设计，实现对中等批量大小的轨迹优化问题进行实时求解。它通过在求解内部和跨求解之间利用块级、warp级和线程级并行性，最大化GPU的利用率，从而提高计算效率。

**技术框架**：GATO的整体框架包含以下几个关键部分：首先，它采用了一种适合GPU并行计算的轨迹优化算法。其次，它在软件层面针对GPU架构进行了优化，包括内存访问模式和线程调度。最后，它在硬件层面充分利用GPU的计算资源，例如CUDA核心和共享内存。整个框架的目标是实现高性能的批量轨迹优化。

**关键创新**：GATO的关键创新在于其多层次的并行策略，包括块级、warp级和线程级并行。这种策略能够充分利用GPU的计算资源，从而实现更高的计算效率。此外，GATO的算法、软件和硬件协同设计也是一个重要的创新点，它能够更好地适应GPU的架构特点，从而提高性能。

**关键设计**：GATO的关键设计包括：(1) 针对GPU架构优化的内存访问模式，减少内存访问延迟；(2) 精细的线程调度策略，避免线程之间的冲突；(3) 优化的轨迹优化算法，减少计算量；(4) 可配置的参数设置，允许用户根据具体应用场景调整求解器的性能。

## 📊 实验亮点

GATO在模拟基准测试中表现出色，相对于CPU基线加速18-21倍，相对于GPU基线加速1.4-16倍，加速效果随着批次大小的增加而更加明显。案例研究表明，GATO能够提高抗扰动性和收敛行为。此外，GATO还在工业机械臂上进行了硬件验证，证明了其在实际应用中的有效性。

## 🎯 应用场景

GATO适用于需要实时模型预测控制的机器人应用，例如工业机械臂控制、自动驾驶、无人机控制等。通过提高轨迹优化速度，GATO可以使这些应用更加稳定、高效和可靠。此外，GATO的开源特性也有助于推动相关领域的研究和发展，促进更多创新应用的出现。

## 📄 摘要（原文）

> While Model Predictive Control (MPC) delivers strong performance across robotics applications, solving the underlying (batches of) nonlinear trajectory optimization (TO) problems online remains computationally demanding. Existing GPU-accelerated approaches typically (i) parallelize a single solve to meet real-time deadlines, (ii) scale to very large batches at slower-than-real-time rates, or (iii) achieve speed by restricting model generality (e.g., point-mass dynamics or a single linearization). This leaves a large gap in solver performance for many state-of-the-art MPC applications that require real-time batches of tens to low-hundreds of solves. As such, we present GATO, an open source, GPU-accelerated, batched TO solver co-designed across algorithm, software, and computational hardware to deliver real-time throughput for these moderate batch size regimes. Our approach leverages a combination of block-, warp-, and thread-level parallelism within and across solves for ultra-high performance. We demonstrate the effectiveness of our approach through a combination of: simulated benchmarks showing speedups of 18-21x over CPU baselines and 1.4-16x over GPU baselines as batch size increases; case studies highlighting improved disturbance rejection and convergence behavior; and finally a validation on hardware using an industrial manipulator. We open source GATO to support reproducibility and adoption.


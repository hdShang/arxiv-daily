---
layout: default
title: "Unfolding Generative Flows with Koopman Operators: Fast and Interpretable Sampling"
---

# Unfolding Generative Flows with Koopman Operators: Fast and Interpretable Sampling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22304" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22304v2</a>
  <a href="https://arxiv.org/pdf/2506.22304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22304v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22304v2', 'Unfolding Generative Flows with Koopman Operators: Fast and Interpretable Sampling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Erkan Turan, Aristotelis Siozopoulos, Louis Martinez, Julien Gaubil, Emery Pierson, Maks Ovsjanikov

**分类**: cs.LG, cs.CV

**发布日期**: 2025-06-27 (更新: 2025-10-21)

---

## 💡 一句话要点

**提出基于Koopman算子的生成流展开方法以加速采样**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `生成建模` `Koopman算子` `连续归一化流` `快速采样` `可解释性` `谱分析` `机器学习`

## 📋 核心要点

1. 现有的连续归一化流方法在采样速度上存在显著瓶颈，导致生成单个样本需要耗费大量计算资源。
2. 本文通过Koopman理论将流动态全局线性化，提出了一种新的采样方法，能够在更高维空间中实现快速并行采样。
3. 实验证明，所提方法在样本质量上与现有技术相当，同时在速度上实现了显著提升，且具备谱分析能力。

## 📝 摘要（中文）

连续归一化流（CNFs）在生成建模中具有优雅的表现，但在采样速度上存在瓶颈：生成单个样本需要解决非线性常微分方程，涉及数百次函数评估。近期方法如Rectified Flow和OT-CFM通过拉直轨迹加速采样，但学习到的动态仍然是非线性的黑箱，限制了效率和可解释性。本文提出通过Koopman理论全局线性化流动态的全新视角。将条件流匹配（CFM）提升至更高维的Koopman空间，用单一线性算子表示其演化。这带来了两个关键好处：首先，采样变为一步且可并行计算，通过矩阵指数以封闭形式实现；其次，Koopman算子提供了生成的谱蓝图，通过其特征值和模式实现新的可解释性。我们推导出一种实用的无仿真训练目标，强制与教师动态的无穷小一致性，展示该对齐在整个生成路径上保持保真度，区别于仅基于边界的蒸馏。实证结果表明，我们的方法在样本质量上具有竞争力，并显著加速，同时独特地实现了生成流的谱分析。

## 🔬 方法详解

**问题定义**：本文旨在解决连续归一化流（CNFs）在生成样本时的慢采样问题，现有方法如Rectified Flow和OT-CFM虽然加速了采样，但仍然面临非线性动态的黑箱问题，限制了效率和可解释性。

**核心思路**：通过Koopman理论将流的动态全局线性化，将条件流匹配（CFM）提升至更高维的Koopman空间，利用单一线性算子来表示其演化，从而实现快速采样和可解释性。

**技术框架**：整体架构包括将CFM提升至Koopman空间、利用矩阵指数进行快速采样、以及通过Koopman算子的特征值和模式实现可解释性。主要模块包括动态提升、线性演化表示和谱分析。

**关键创新**：最重要的技术创新在于通过Koopman算子实现流的全局线性化，使得采样过程变为一步并可并行计算，显著提高了效率，并提供了新的可解释性视角。

**关键设计**：设计中采用了无仿真训练目标，确保与教师动态的无穷小一致性，损失函数的设置旨在保持生成路径的保真度，避免了传统方法中仅基于边界的蒸馏问题。具体的网络结构和参数设置在实验部分进行了详细描述。

## 📊 实验亮点

实验结果显示，所提方法在样本质量上与现有技术相当，同时在采样速度上实现了显著提升，具体表现为在相同条件下，采样速度提高了数倍。此外，方法还具备独特的谱分析能力，为生成流的理解提供了新的视角。

## 🎯 应用场景

该研究的潜在应用领域包括生成建模、数据增强和模拟等，能够在需要快速生成样本的场景中发挥重要作用。通过提高采样速度和可解释性，未来可能推动更多基于生成模型的实际应用，如图像生成、视频合成和虚拟现实等。

## 📄 摘要（原文）

> Continuous Normalizing Flows (CNFs) enable elegant generative modeling but remain bottlenecked by slow sampling: producing a single sample requires solving a nonlinear ODE with hundreds of function evaluations. Recent approaches such as Rectified Flow and OT-CFM accelerate sampling by straightening trajectories, yet the learned dynamics remain nonlinear black boxes, limiting both efficiency and interpretability. We propose a fundamentally different perspective: globally linearizing flow dynamics via Koopman theory. By lifting Conditional Flow Matching (CFM) into a higher-dimensional Koopman space, we represent its evolution with a single linear operator. This yields two key benefits. First, sampling becomes one-step and parallelizable, computed in closed form via the matrix exponential. Second, the Koopman operator provides a spectral blueprint of generation, enabling novel interpretability through its eigenvalues and modes. We derive a practical, simulation-free training objective that enforces infinitesimal consistency with the teacher's dynamics and show that this alignment preserves fidelity along the full generative path, distinguishing our method from boundary-only distillation. Empirically, our approach achieves competitive sample quality with dramatic speedups, while uniquely enabling spectral analysis of generative flows.


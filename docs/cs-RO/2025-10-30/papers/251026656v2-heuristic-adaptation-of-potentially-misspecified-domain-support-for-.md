---
layout: default
title: Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems
---

# Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26656" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26656v2</a>
  <a href="https://arxiv.org/pdf/2510.26656.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26656v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.26656v2', 'Heuristic Adaptation of Potentially Misspecified Domain Support for Likelihood-Free Inference in Stochastic Dynamical Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Georgios Kamaras, Craig Innes, Subramanian Ramamoorthy

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-30 (更新: 2025-11-11)

**备注**: 20 pages, 18 figures, algorithm lines cleveref fixed for pdflatex 2025

---

## 💡 一句话要点

**提出三种启发式LFI变体，自适应调整领域支持，提升随机动力系统中的无似然推理性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无似然推理` `领域自适应` `随机动力系统` `机器人操作` `可变形物体`

## 📋 核心要点

1. 传统LFI方法假设固定的采样支持域，但若该域错误指定，会导致次优甚至错误的后验分布。
2. 论文提出EDGE、MODE和CENTRE三种启发式LFI变体，通过后验模式偏移自适应调整支持域。
3. 实验表明，该方法在DLO操作任务中，能更准确地进行参数推理和策略学习，提升智能体性能。

## 📝 摘要（中文）

在机器人领域，无似然推理(LFI)可以提供领域分布，从而在参数化部署条件下调整学习到的智能体。LFI假设一个任意的采样支持域，该支持域在初始通用先验被迭代细化为更具描述性的后验时保持不变。然而，一个可能错误指定的支持域可能导致次优但错误地确定的后验。为了解决这个问题，我们提出了三种启发式LFI变体：EDGE、MODE和CENTRE。每种方法都以其自身的方式解释推理步骤中的后验模式偏移，并在集成到LFI步骤中时，自适应地调整支持域以及后验推理。我们首先揭示了支持域错误指定问题，并使用随机动力学基准评估了我们的启发式方法。然后，我们评估了启发式支持域自适应对动态可变形线性对象(DLO)操作任务的参数推理和策略学习的影响。推理结果为参数化DLO集合提供了更精细的长度和刚度分类。当将生成的后验用作基于模拟的策略学习的领域分布时，它们可以带来更强大的以对象为中心的智能体性能。

## 🔬 方法详解

**问题定义**：论文旨在解决在随机动力系统中，由于无似然推理(LFI)方法中预设的领域支持域(support)可能与真实情况不符，导致后验分布估计不准确的问题。现有LFI方法通常假设一个固定的、任意的领域支持域，这在实际应用中可能导致次优甚至错误的推理结果，尤其是在处理复杂动力系统时。

**核心思路**：论文的核心思路是根据LFI迭代过程中后验分布的模式(mode)变化，自适应地调整领域支持域。通过观察后验分布的模式在迭代过程中的偏移，可以推断出初始设定的支持域可能存在偏差，从而动态地调整支持域的范围，使其更接近真实的参数空间。

**技术框架**：整体框架是在标准的LFI流程中加入一个支持域自适应的模块。该模块在每次LFI迭代后，根据后验分布的模式偏移情况，使用三种不同的启发式方法（EDGE、MODE和CENTRE）来调整支持域的范围。调整后的支持域将用于下一次LFI迭代的采样过程，从而逐步优化后验分布的估计。

**关键创新**：论文的关键创新在于提出了三种启发式方法，用于根据后验分布的模式偏移自适应地调整LFI的支持域。这三种方法分别从不同的角度解释了模式偏移的含义，并采取不同的策略来调整支持域的范围。与传统的固定支持域的LFI方法相比，该方法能够更好地适应真实参数空间，提高后验分布估计的准确性。

**关键设计**：三种启发式方法EDGE、MODE和CENTRE的具体设计是关键。EDGE方法关注后验分布边缘的变化，MODE方法直接利用后验分布的模式位置，CENTRE方法则关注后验分布中心的变化。具体参数设置取决于具体的应用场景和动力系统特性，需要根据实验结果进行调整。

## 📊 实验亮点

实验结果表明，所提出的启发式LFI变体在DLO操作任务中，能够更准确地进行参数推理，实现更精细的长度和刚度分类。与传统LFI方法相比，使用自适应支持域的LFI方法能够显著提高策略学习的性能，使智能体在不同DLO参数下的操作任务中表现出更强的鲁棒性。

## 🎯 应用场景

该研究成果可应用于机器人操作、控制和仿真等领域，尤其是在处理具有不确定性和复杂动力学的系统时。例如，可用于提高机器人对柔性物体的操作能力，优化控制策略，以及更准确地进行系统建模和仿真。该方法能够提升智能体在未知环境中的适应性和鲁棒性，具有重要的实际应用价值。

## 📄 摘要（原文）

> In robotics, likelihood-free inference (LFI) can provide the domain distribution that adapts a learnt agent in a parametric set of deployment conditions. LFI assumes an arbitrary support for sampling, which remains constant as the initial generic prior is iteratively refined to more descriptive posteriors. However, a potentially misspecified support can lead to suboptimal, yet falsely certain, posteriors. To address this issue, we propose three heuristic LFI variants: EDGE, MODE, and CENTRE. Each interprets the posterior mode shift over inference steps in its own way and, when integrated into an LFI step, adapts the support alongside posterior inference. We first expose the support misspecification issue and evaluate our heuristics using stochastic dynamical benchmarks. We then evaluate the impact of heuristic support adaptation on parameter inference and policy learning for a dynamic deformable linear object (DLO) manipulation task. Inference results in a finer length and stiffness classification for a parametric set of DLOs. When the resulting posteriors are used as domain distributions for sim-based policy learning, they lead to more robust object-centric agent performance.


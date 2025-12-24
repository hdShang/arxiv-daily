---
layout: default
title: "FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control"
---

# FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19926" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19926v1</a>
  <a href="https://arxiv.org/pdf/2508.19926.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19926v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19926v1', 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tan Jing, Shiting Chen, Yangfan Li, Weisheng Xu, Renjing Xu

**分类**: cs.RO

**发布日期**: 2025-08-27

**🔗 代码/项目**: [GITHUB](https://github.com/Colin-Jing/FARM)

---

## 💡 一句话要点

**提出FARM框架以解决高动态人形控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人形控制` `物理仿真` `机器学习` `动作捕捉` `机器人技术` `专家混合模型` `数据集构建`

## 📋 核心要点

1. 现有的基于物理的人形控制器在处理高动态动作时表现不佳，限制了其实际应用。
2. FARM框架通过帧加速增强和残差专家混合模型，提升了对高动态动作的跟踪能力。
3. 在HDHM数据集上，FARM显著降低了跟踪失败率和位置误差，展示了其优越性能。

## 📝 摘要（中文）

统一的基于物理的人形控制器在机器人和角色动画中至关重要，但在处理高动态动作时，现有模型往往表现不佳，限制了其在现实世界中的应用。为此，本文提出了FARM（帧加速增强与残差专家混合模型），这是一个端到端的框架，包含帧加速增强、稳健的基础控制器和残差专家混合模型。帧加速增强通过扩大帧间间隔，使模型能够应对高速姿态变化。基础控制器可靠地跟踪日常低动态动作，而残差专家混合模型则自适应地分配额外的网络容量以处理高动态动作，从而显著提高跟踪精度。我们还构建了高动态人形运动（HDHM）数据集，包含3593个物理上合理的片段。在HDHM数据集上，FARM将跟踪失败率降低了42.8%，并使全局每关节位置误差降低了14.6%，同时在低动态动作上保持近乎完美的准确性。这些结果确立了FARM作为高动态人形控制的新基准，并引入了首个专门针对这一挑战的公开基准。

## 🔬 方法详解

**问题定义**：本文旨在解决现有基于物理的人形控制器在高动态动作下的跟踪失败问题。现有方法在处理快速、剧烈的动作时，往往无法保持准确性，导致实际应用受限。

**核心思路**：FARM框架通过引入帧加速增强技术，使模型能够适应高速姿态变化，同时结合残差专家混合模型，动态分配网络资源以应对复杂动作，从而提升整体跟踪精度。

**技术框架**：FARM框架由三个主要模块组成：帧加速增强模块、基础控制器和残差专家混合模型。帧加速增强模块通过扩大帧间间隔，增加模型对高动态动作的暴露；基础控制器负责稳定跟踪低动态动作；残差专家混合模型则在需要时提供额外的网络能力。

**关键创新**：FARM的核心创新在于结合了帧加速增强与残差专家混合模型，使得模型在处理高动态动作时能够自适应调整网络资源，显著提高了跟踪精度。这一方法与传统的单一控制器设计有本质区别。

**关键设计**：在设计中，帧加速增强模块的参数设置经过精心调整，以确保模型能够有效应对高速变化；损失函数的设计考虑了低动态与高动态动作的不同需求，确保模型在两者之间的平衡。

## 📊 实验亮点

在HDHM数据集上，FARM框架将跟踪失败率降低了42.8%，全局每关节位置误差降低了14.6%，同时在低动态动作上保持了近乎完美的准确性。这些实验结果表明，FARM在高动态人形控制方面具有显著的性能提升，确立了新的研究基准。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、虚拟角色动画以及增强现实等场景。通过提升人形控制器在高动态动作下的表现，FARM框架能够为机器人在复杂环境中的自主导航和交互提供更可靠的技术支持，推动相关领域的发展。

## 📄 摘要（原文）

> Unified physics-based humanoid controllers are pivotal for robotics and character animation, yet models that excel on gentle, everyday motions still stumble on explosive actions, hampering real-world deployment. We bridge this gap with FARM (Frame-Accelerated Augmentation and Residual Mixture-of-Experts), an end-to-end framework composed of frame-accelerated augmentation, a robust base controller, and a residual mixture-of-experts (MoE). Frame-accelerated augmentation exposes the model to high-velocity pose changes by widening inter-frame gaps. The base controller reliably tracks everyday low-dynamic motions, while the residual MoE adaptively allocates additional network capacity to handle challenging high-dynamic actions, significantly enhancing tracking accuracy. In the absence of a public benchmark, we curate the High-Dynamic Humanoid Motion (HDHM) dataset, comprising 3593 physically plausible clips. On HDHM, FARM reduces the tracking failure rate by 42.8\% and lowers global mean per-joint position error by 14.6\% relative to the baseline, while preserving near-perfect accuracy on low-dynamic motions. These results establish FARM as a new baseline for high-dynamic humanoid control and introduce the first open benchmark dedicated to this challenge. The code and dataset will be released at https://github.com/Colin-Jing/FARM.


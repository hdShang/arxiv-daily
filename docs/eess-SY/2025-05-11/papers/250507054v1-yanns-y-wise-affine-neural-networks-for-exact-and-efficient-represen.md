---
layout: default
title: "YANNs: Y-wise Affine Neural Networks for Exact and Efficient Representations of Piecewise Linear Functions"
---

# YANNs: Y-wise Affine Neural Networks for Exact and Efficient Representations of Piecewise Linear Functions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07054" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07054v1</a>
  <a href="https://arxiv.org/pdf/2505.07054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07054v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07054v1', 'YANNs: Y-wise Affine Neural Networks for Exact and Efficient Representations of Piecewise Linear Functions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Austin Braniff, Yuhe Tian

**分类**: eess.SY, cs.LG, math.OC

**发布日期**: 2025-05-11

---

## 💡 一句话要点

**提出Y-wise仿射神经网络以精确高效表示分段线性函数**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `仿射神经网络` `分段线性函数` `模型预测控制` `实时推理` `控制理论` `可解释性` `算法可扩展性`

## 📋 核心要点

1. 现有方法在表示分段线性函数时通常依赖于近似，缺乏精确性和可解释性。
2. YANNs通过无训练的方式实现分段仿射函数的精确表示，确保了控制律的可行性和稳定性。
3. 实验结果表明，YANNs在实时推理速度上显著优于传统方法，且在多参数控制中表现出色。

## 📝 摘要（中文）

本文正式介绍了Y-wise仿射神经网络（YANNs），这是一种完全可解释的网络架构，能够连续且高效地表示具有多面体子域的分段仿射函数。研究表明，YANNs的开发无需训练即可实现功能等效的表示，因此保持了原始公式的所有数学属性。YANNs在多参数模型预测控制中的应用展示了其理论上计算状态、输出、设定点和干扰的最优控制律作为分段仿射函数的能力。通过精确表示多参数控制律，YANNs保留了递归可行性和稳定性等重要控制理论保证，显著区别于现有利用神经网络近似最优控制律的研究。通过优化网络推理速度，YANNs在实时评估中显著快于传统的分段仿射函数计算。数值案例研究展示了算法在输入/输出维度和子域数量方面的可扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在表示分段线性函数时的精确性不足和可解释性缺失的问题。传统神经网络通常依赖于近似，无法保证控制律的稳定性和可行性。

**核心思路**：YANNs的核心思想是通过无训练的方式实现分段仿射函数的精确表示，保持原始数学属性，同时确保控制理论的保证。这样的设计使得网络在推理时能够高效且准确地计算控制律。

**技术框架**：YANNs的整体架构包括输入层、多个仿射变换模块和输出层。每个模块负责处理特定的子域，确保在不同状态下的输出一致性。

**关键创新**：YANNs的主要创新在于其能够精确表示多参数控制律，而不是依赖于近似。这一特性使得YANNs在控制理论中具有独特的优势，能够确保递归可行性和稳定性。

**关键设计**：YANNs的设计包括多个仿射变换模块，每个模块对应一个多面体子域。网络结构中没有复杂的损失函数设计，主要依赖于数学性质的保持，确保了高效的推理速度。整体架构优化了推理过程，使得实时评估速度显著提升。

## 📊 实验亮点

实验结果显示，YANNs在实时推理速度上比传统分段仿射函数计算快得多，且在多参数控制中能够保持递归可行性和稳定性。具体性能数据表明，YANNs在处理高维输入时的可扩展性优于现有方法，提升幅度显著。

## 🎯 应用场景

YANNs在多参数模型预测控制中具有广泛的应用潜力，能够为数据驱动建模和控制提供高效且可解释的起点。其精确的控制律表示使得在复杂系统中的应用成为可能，尤其是在需要高可靠性和实时响应的场景中。

## 📄 摘要（原文）

> This work formally introduces Y-wise Affine Neural Networks (YANNs), a fully-explainable network architecture that continuously and efficiently represent piecewise affine functions with polytopic subdomains. Following from the proofs, it is shown that the development of YANNs requires no training to achieve the functionally equivalent representation. YANNs thus maintain all mathematical properties of the original formulations. Multi-parametric model predictive control is utilized as an application showcase of YANNs, which theoretically computes optimal control laws as a piecewise affine function of states, outputs, setpoints, and disturbances. With the exact representation of multi-parametric control laws, YANNs retain essential control-theoretic guarantees such as recursive feasibility and stability. This sets YANNs apart from the existing works which apply neural networks for approximating optimal control laws instead of exactly representing them. By optimizing the inference speed of the networks, YANNs can evaluate substantially faster in real-time compared to traditional piecewise affine function calculations. Numerical case studies are presented to demonstrate the algorithmic scalability with respect to the input/output dimensions and the number of subdomains. YANNs represent a significant advancement in control as the first neural network-based controller that inherently ensures both feasibility and stability. Future applications can leverage them as an efficient and interpretable starting point for data-driven modeling/control.


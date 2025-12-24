---
layout: default
title: "Canonical Policy: Learning Canonical 3D Representation for SE(3)-Equivariant Policy"
---

# Canonical Policy: Learning Canonical 3D Representation for SE(3)-Equivariant Policy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18474" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18474v2</a>
  <a href="https://arxiv.org/pdf/2505.18474.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18474v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18474v2', 'Canonical Policy: Learning Canonical 3D Representation for SE(3)-Equivariant Policy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Zhang, Zhengtong Xu, Jai Nanda Lakamsani, Yu She

**分类**: cs.RO

**发布日期**: 2025-05-24 (更新: 2025-11-08)

**🔗 代码/项目**: [PROJECT_PAGE](https://zhangzhiyuanzhang.github.io/cp-website/)

---

## 💡 一句话要点

**提出规范策略以解决3D等变模仿学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉模仿学习` `3D点云` `等变策略` `机器人操作` `泛化能力` `样本效率` `生成模型`

## 📋 核心要点

1. 现有的等变方法在集成等变组件时缺乏结构化，导致可解释性和严谨性不足。
2. 本文提出的规范策略框架通过规范化3D点云观察，建立了等变观察到动作的映射理论。
3. 在多项任务中，规范策略在模拟和真实世界实验中分别实现了18.0%和39.7%的性能提升。

## 📝 摘要（中文）

视觉模仿学习在机器人操作中取得了显著进展，但在未见对象、场景布局和相机视角的泛化能力方面仍面临挑战。为此，本文提出了规范策略（canonical policy），这是一个统一3D点云观察的框架，能够实现等变观察到动作的映射。通过在12个多样化的模拟任务和4个真实世界操作任务中进行验证，规范策略在模拟中平均提升了18.0%，在真实实验中提升了39.7%，展现了优越的泛化能力和样本效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有模仿学习方法在面对未见对象和不同场景布局时的泛化能力不足问题。现有方法往往缺乏对3D点云的有效利用，导致在新环境中的表现不佳。

**核心思路**：规范策略通过建立3D规范表示，统一不同的点云观察，从而实现等变的观察到动作映射。该方法利用几何对称性和现代生成模型的表达能力，提升了模仿学习的效果。

**技术框架**：整体架构包括三个主要模块：首先是3D规范表示的建立，其次是基于该表示的策略学习管道，最后是通过生成模型进行动作生成。每个模块都紧密结合，以确保信息的有效传递和利用。

**关键创新**：最重要的创新在于提出了规范策略框架，系统性地将3D点云观察整合到一个规范表示中，解决了现有方法在可解释性和结构化方面的不足。

**关键设计**：在设计中，采用了特定的损失函数来优化等变映射，同时利用现代生成模型的灵活性来增强策略的表达能力。网络结构上，结合了几何对称性以提高学习效率。

## 📊 实验亮点

实验结果显示，规范策略在12个模拟任务中平均提升了18.0%的性能，在4个真实世界操作任务中提升了39.7%。这些结果表明，规范策略在泛化能力和样本效率方面优于现有的最先进模仿学习策略。

## 🎯 应用场景

该研究的潜在应用领域包括机器人抓取、自动化装配和人机交互等场景。通过提升机器人对未知环境的适应能力，规范策略能够在实际操作中显著提高效率和安全性，未来可能推动智能机器人在复杂环境中的广泛应用。

## 📄 摘要（原文）

> Visual Imitation learning has achieved remarkable progress in robotic manipulation, yet generalization to unseen objects, scene layouts, and camera viewpoints remains a key challenge. Recent advances address this by using 3D point clouds, which provide geometry-aware, appearance-invariant representations, and by incorporating equivariance into policy architectures to exploit spatial symmetries. However, existing equivariant approaches often lack interpretability and rigor due to unstructured integration of equivariant components. We introduce canonical policy, a principled framework for 3D equivariant imitation learning that unifies 3D point cloud observations under a canonical representation. We first establish a theory of 3D canonical representations, enabling equivariant observation-to-action mappings by grouping both seen and novel point clouds to a canonical representation. We then propose a flexible policy learning pipeline that leverages geometric symmetries from canonical representation and the expressiveness of modern generative models. We validate canonical policy on 12 diverse simulated tasks and 4 real-world manipulation tasks across 16 configurations, involving variations in object color, shape, camera viewpoint, and robot platform. Compared to state-of-the-art imitation learning policies, canonical policy achieves an average improvement of 18.0% in simulation and 39.7% in real-world experiments, demonstrating superior generalization capability and sample efficiency. For more details, please refer to the project website: https://zhangzhiyuanzhang.github.io/cp-website/.


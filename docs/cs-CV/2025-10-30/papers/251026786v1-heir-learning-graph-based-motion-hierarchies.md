---
layout: default
title: HEIR: Learning Graph-Based Motion Hierarchies
---

# HEIR: Learning Graph-Based Motion Hierarchies

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.26786" target="_blank" class="toolbar-btn">arXiv: 2510.26786v1</a>
    <a href="https://arxiv.org/pdf/2510.26786.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26786v1" 
            onclick="toggleFavorite(this, '2510.26786v1', 'HEIR: Learning Graph-Based Motion Hierarchies')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Cheng Zheng, William Koch, Baiang Li, Felix Heide

**分类**: cs.CV, cs.GR, cs.LG

**发布日期**: 2025-10-30

**备注**: Code link: https://github.com/princeton-computational-imaging/HEIR

**期刊**: Advances in Neural Information Processing Systems 38 (NeurIPS 2025)

---

## 💡 一句话要点

**提出HEIR，学习基于图的运动层次结构，实现数据驱动的运动建模。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `运动建模` `层次结构学习` `图神经网络` `运动分解` `动态场景重建`

## 📋 核心要点

1. 现有运动建模方法依赖手动定义或启发式规则，缺乏对不同任务的泛化能力。
2. HEIR方法通过图神经网络学习运动层次结构，将全局运动分解为继承模式和局部残差。
3. 实验表明，HEIR在1D/2D运动重建中能恢复内在结构，在3D动态场景变形中表现更优。

## 📝 摘要（中文）

本文提出了一种通用的分层运动建模方法，该方法直接从数据中学习结构化的、可解释的运动关系。该方法使用基于图的层次结构来表示观察到的运动，将全局绝对运动显式地分解为父节点继承的模式和局部运动残差。我们将层次结构推断建模为一个可微的图学习问题，其中顶点表示基本运动，有向边通过图神经网络捕获学习到的父子依赖关系。我们在三个例子上评估了我们的分层重建方法：1D平移运动、2D旋转运动以及通过高斯溅射实现的动态3D场景变形。实验结果表明，我们的方法重建了1D和2D案例中的内在运动层次结构，并且与动态3D高斯溅射场景上的基线相比，产生了更逼真和可解释的变形。通过提供一种适应性强、数据驱动的分层建模范例，我们的方法提供了一种适用于广泛的以运动为中心任务的公式。

## 🔬 方法详解

**问题定义**：现有运动建模方法通常依赖于手动定义的或启发式的层次结构，以及固定的运动原语，这限制了它们在不同任务中的泛化能力。论文旨在解决如何自动地、数据驱动地学习运动的层次结构，从而更好地建模复杂运动动力学的问题。

**核心思路**：论文的核心思路是将复杂的运动分解为一系列具有层次关系的简单运动单元，并通过图结构来表示这些单元之间的依赖关系。通过学习图的结构，可以自动地发现运动的内在层次结构，从而实现更灵活和可解释的运动建模。

**技术框架**：HEIR方法的整体框架包括以下几个主要步骤：1) 使用图结构表示运动，其中节点代表基本运动单元，边代表单元间的依赖关系；2) 使用图神经网络学习图的结构，即学习节点间的连接关系；3) 将全局运动分解为父节点继承的运动模式和局部运动残差；4) 通过最小化重建误差来优化图的结构和运动分解。

**关键创新**：该方法最重要的创新点在于使用图神经网络来学习运动的层次结构。与传统方法相比，该方法能够自动地从数据中学习运动单元之间的依赖关系，而无需手动定义或使用启发式规则。此外，该方法还能够将全局运动分解为可解释的运动模式和残差，从而更好地理解运动的本质。

**关键设计**：在图神经网络的设计上，论文使用了可微的图学习方法，使得整个模型可以进行端到端的训练。损失函数主要包括重建损失和正则化项，其中重建损失用于保证运动的重建精度，正则化项用于约束图的结构，例如稀疏性。具体的网络结构和参数设置在论文中有详细描述，需要根据具体的应用场景进行调整。

## 📊 实验亮点

实验结果表明，HEIR方法在1D和2D运动重建任务中能够准确地恢复内在的运动层次结构。在动态3D高斯溅射场景中，HEIR方法生成的变形效果比基线方法更逼真和可解释。这些结果验证了HEIR方法在运动建模方面的有效性和优越性。

## 🎯 应用场景

该研究成果可应用于计算机视觉、图形学和机器人等领域，例如动作识别、运动预测、动画生成、机器人控制等。通过学习运动的层次结构，可以更好地理解和建模复杂的运动动力学，从而提高相关任务的性能和鲁棒性。未来，该方法有望应用于更广泛的运动相关任务，例如自动驾驶、虚拟现实等。

## 📄 摘要（原文）

> Hierarchical structures of motion exist across research fields, including computer vision, graphics, and robotics, where complex dynamics typically arise from coordinated interactions among simpler motion components. Existing methods to model such dynamics typically rely on manually-defined or heuristic hierarchies with fixed motion primitives, limiting their generalizability across different tasks. In this work, we propose a general hierarchical motion modeling method that learns structured, interpretable motion relationships directly from data. Our method represents observed motions using graph-based hierarchies, explicitly decomposing global absolute motions into parent-inherited patterns and local motion residuals. We formulate hierarchy inference as a differentiable graph learning problem, where vertices represent elemental motions and directed edges capture learned parent-child dependencies through graph neural networks. We evaluate our hierarchical reconstruction approach on three examples: 1D translational motion, 2D rotational motion, and dynamic 3D scene deformation via Gaussian splatting. Experimental results show that our method reconstructs the intrinsic motion hierarchy in 1D and 2D cases, and produces more realistic and interpretable deformations compared to the baseline on dynamic 3D Gaussian splatting scenes. By providing an adaptable, data-driven hierarchical modeling paradigm, our method offers a formulation applicable to a broad range of motion-centric tasks. Project Page: https://light.princeton.edu/HEIR/


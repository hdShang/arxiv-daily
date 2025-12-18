---
layout: default
title: Cooperative Task Spaces for Multi-Arm Manipulation Control based on Similarity Transformations
---

# Cooperative Task Spaces for Multi-Arm Manipulation Control based on Similarity Transformations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26362" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26362v1</a>
  <a href="https://arxiv.org/pdf/2510.26362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26362v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.26362v1', 'Cooperative Task Spaces for Multi-Arm Manipulation Control based on Similarity Transformations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Löw, Cem Bilaloglu, Sylvain Calinon

**分类**: cs.RO, eess.SY

**发布日期**: 2025-10-30

---

## 💡 一句话要点

**提出基于相似变换的协作任务空间，用于多臂操作控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多臂机器人` `协作控制` `共形几何代数` `相似变换` `操作空间控制`

## 📋 核心要点

1. 多臂协作系统自由度高，运动协调建模困难，现有方法难以有效控制。
2. 利用共形几何代数定义几何基元，通过相似变换抽象复杂系统，简化控制。
3. 通过实验验证了该方法在双臂机械手、人形机器人和多指手上的有效性。

## 📝 摘要（中文）

本文提出了一种基于共形几何代数的几何基元的多臂机器人系统协作任务空间的理论基础。利用这些协作几何基元的相似变换，我们推导出复杂机器人系统的抽象表示，使其能够以直接对应于单臂系统的方式表示这些系统。通过推导相关的解析和几何雅可比矩阵，我们展示了该方法与基于操作空间控制的经典控制技术的直接集成。我们通过双臂机械手、人形机器人和多指手在最优控制实验中演示了这一点，以达到所需的几何基元，并在使用微分运动学控制的遥操作实验中演示了这一点。然后，我们讨论了几何基元如何自然地将零空间结构嵌入到控制器中，这些结构可以被利用来引入次要控制目标。这项工作代表了这种协作操作控制框架的理论基础，因此实验以抽象的方式呈现，同时给出了潜在未来应用的指示。

## 🔬 方法详解

**问题定义**：多臂机器人系统，如双臂机械手、人形机器人和多指手，在执行复杂任务时需要协同操作。由于这些系统通常具有非常高的自由度，因此协调它们的运动非常困难。现有的建模方法难以有效地表示和控制这些复杂系统，尤其是在需要多个机械臂协同完成任务时，例如搬运大型物体或进行灵巧的在手操作。

**核心思路**：本文的核心思路是利用共形几何代数（CGA）来定义协作任务空间的几何基元，并通过相似变换来抽象复杂的多臂机器人系统。通过这种方式，可以将多臂系统简化为类似于单臂系统的表示，从而更容易进行控制。CGA提供了一种简洁而强大的方式来表示几何对象和变换，使得可以方便地推导出控制所需的雅可比矩阵。

**技术框架**：该方法的技术框架主要包括以下几个步骤：1) 使用CGA定义协作任务空间的几何基元，例如点、线、面等。2) 利用相似变换将多臂机器人系统的运动学映射到这些几何基元上。3) 推导与这些几何基元相关的解析和几何雅可比矩阵。4) 将这些雅可比矩阵集成到经典的控制技术中，例如操作空间控制。5) 利用几何基元自然嵌入的零空间结构来引入次要控制目标。

**关键创新**：该方法最重要的技术创新点在于使用CGA和相似变换来抽象多臂机器人系统，从而简化了控制问题。与传统的直接对多自由度系统进行建模和控制的方法相比，该方法能够更有效地表示和控制复杂的多臂系统。此外，该方法还利用了几何基元自然嵌入的零空间结构，从而可以方便地引入次要控制目标。

**关键设计**：在具体实现中，需要选择合适的几何基元来表示任务空间。例如，可以使用点来表示目标位置，使用线来表示目标方向。此外，还需要仔细设计相似变换，以确保多臂机器人系统的运动学能够准确地映射到几何基元上。在控制器的设计中，需要选择合适的控制律和参数，以实现期望的控制性能。论文中虽然没有给出具体的参数设置，但是强调了该框架可以与现有的操作空间控制方法相结合。

## 📊 实验亮点

论文通过双臂机械手、人形机器人和多指手的最优控制和遥操作实验验证了该方法的有效性。虽然实验以抽象方式呈现，没有给出具体的性能数据，但结果表明该方法能够成功地控制多臂系统达到期望的几何基元，并能够利用零空间结构引入次要控制目标。这为未来的实际应用奠定了基础。

## 🎯 应用场景

该研究成果可应用于各种需要多臂协同操作的场景，如工业自动化中的装配、搬运，医疗机器人中的手术辅助，以及服务机器人中的物体操作等。通过简化多臂系统的控制，可以提高操作效率和精度，降低开发成本，并为更复杂的机器人任务提供可能性。

## 📄 摘要（原文）

> Many tasks in human environments require collaborative behavior between multiple kinematic chains, either to provide additional support for carrying big and bulky objects or to enable the dexterity that is required for in-hand manipulation. Since these complex systems often have a very high number of degrees of freedom coordinating their movements is notoriously difficult to model. In this article, we present the derivation of the theoretical foundations for cooperative task spaces of multi-arm robotic systems based on geometric primitives defined using conformal geometric algebra. Based on the similarity transformations of these cooperative geometric primitives, we derive an abstraction of complex robotic systems that enables representing these systems in a way that directly corresponds to single-arm systems. By deriving the associated analytic and geometric Jacobian matrices, we then show the straightforward integration of our approach into classical control techniques rooted in operational space control. We demonstrate this using bimanual manipulators, humanoids and multi-fingered hands in optimal control experiments for reaching desired geometric primitives and in teleoperation experiments using differential kinematics control. We then discuss how the geometric primitives naturally embed nullspace structures into the controllers that can be exploited for introducing secondary control objectives. This work, represents the theoretical foundations of this cooperative manipulation control framework, and thus the experiments are presented in an abstract way, while giving pointers towards potential future applications.


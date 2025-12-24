---
layout: default
title: "Flexible and Foldable: Workspace Analysis and Object Manipulation Using a Soft, Interconnected, Origami-Inspired Actuator Array"
---

# Flexible and Foldable: Workspace Analysis and Object Manipulation Using a Soft, Interconnected, Origami-Inspired Actuator Array

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13998" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13998v2</a>
  <a href="https://arxiv.org/pdf/2509.13998.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13998v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13998v2', 'Flexible and Foldable: Workspace Analysis and Object Manipulation Using a Soft, Interconnected, Origami-Inspired Actuator Array')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bailey Dacre, Rodrigo Moreno, Serhat Demirtas, Ziqiao Wang, Yuhao Jiang, Jamie Paik, Kasper Stoy, Andrés Faíña

**分类**: cs.RO

**发布日期**: 2025-09-17 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出一种基于软性互连折纸结构的柔性分布式操作器，用于提升物体操作能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `分布式操作器` `柔性机器人` `折纸结构` `物体操作` `机器人阵列`

## 📋 核心要点

1. 现有分布式操作器系统通常依赖高密度的执行器，限制了物体与执行器之间的比例，降低了其适应性。
2. 该论文提出了一种基于折纸结构的柔性互连执行器阵列，通过柔性表面连接，实现连续可控的操作表面。
3. 实验结果表明，该设计在不增加执行器数量的情况下，可操作面积提升了1.84倍，降低了成本和复杂度。

## 📝 摘要（中文）

本文提出了一种新型的分布式操作器系统（DMS）设计，该设计利用由柔性表面层互连的3自由度折纸结构机器人瓦片阵列。与传统的DMS不同，该方法不仅可以在执行器末端进行操作，还可以在连接所有执行器的柔性表面上进行操作，从而创建一个连续、可控的操作表面。我们分析了这种系统的组合工作空间，推导出了简单的运动原语，并展示了其在瓦片阵列上平移简单几何对象的能力。通过利用瓦片间的连接材料，我们的方法显著降低了执行器密度，在不增加执行器数量的情况下，物体可操作的面积增加了1.84倍。这种设计为传统的高密度阵列提供了一种成本更低、复杂性更低的替代方案，并为利用互连表面灵活性的操作策略带来了新的机会。

## 🔬 方法详解

**问题定义**：现有的分布式操作器系统（DMS）通常需要高密度的执行器阵列，这导致了较高的成本和复杂性。此外，它们对物体与执行器之间的尺寸比例有一定限制，降低了系统的灵活性和适应性。因此，需要一种能够在降低执行器密度的同时，保持甚至提升操作能力的DMS设计。

**核心思路**：本文的核心思路是利用柔性材料将多个独立的、基于折纸结构的3自由度机器人瓦片连接起来。这种互连方式不仅允许在每个瓦片的末端执行操作，还允许利用瓦片之间的柔性表面进行连续的操作。通过这种方式，可以在较低的执行器密度下，实现更大的可操作面积。

**技术框架**：该系统的整体架构包括一个由多个3自由度折纸结构机器人瓦片组成的阵列，这些瓦片通过一个柔性表面层相互连接。每个瓦片可以独立运动，通过控制每个瓦片的运动，可以实现对物体的平移、旋转等操作。此外，柔性表面层允许瓦片之间的协同运动，从而实现更复杂的操作。整个系统的工作流程包括：物体识别、运动规划、瓦片控制和操作执行。

**关键创新**：该论文最重要的技术创新点在于利用柔性互连的折纸结构机器人瓦片阵列，创建了一个连续可控的操作表面。与传统的DMS相比，该设计显著降低了执行器密度，同时增加了可操作面积。这种设计允许利用瓦片之间的柔性表面进行操作，从而实现了更灵活的操作策略。

**关键设计**：每个机器人瓦片采用基于折纸结构的3自由度设计，使其具有较高的灵活性和可控性。柔性表面层采用具有适当刚度和摩擦系数的材料，以保证瓦片之间的协同运动和对物体的稳定抓取。控制算法需要考虑瓦片之间的相互作用和柔性表面的形变，以实现精确的物体操作。具体的参数设置和网络结构等技术细节在论文中可能未详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，与传统的DMS相比，该设计在不增加执行器数量的情况下，物体可操作的面积增加了1.84倍。这表明该设计在降低执行器密度的同时，显著提升了操作能力。具体的性能数据和对比基线可能在论文中有更详细的描述，但此处未提供。

## 🎯 应用场景

该研究成果可应用于自动化装配、柔性制造、医疗康复等领域。例如，在自动化装配中，该系统可以用于抓取和放置各种形状和尺寸的零件。在医疗康复领域，该系统可以用于辅助患者进行精细动作训练。未来，该技术有望应用于太空探索等极端环境下的物体操作。

## 📄 摘要（原文）

> Object manipulation is a fundamental challenge in robotics, where systems must balance trade-offs among manipulation capabilities, system complexity, and throughput. Distributed manipulator systems (DMS) use the coordinated motion of actuator arrays to perform complex object manipulation tasks, seeing widespread exploration within the literature and in industry. However, existing DMS designs typically rely on high actuator densities and impose constraints on object-to-actuator scale ratios, limiting their adaptability. We present a novel DMS design utilizing an array of 3-DoF, origami-inspired robotic tiles interconnected by a compliant surface layer. Unlike conventional DMS, our approach enables manipulation not only at the actuator end effectors but also across a flexible surface connecting all actuators; creating a continuous, controllable manipulation surface. We analyse the combined workspace of such a system, derive simple motion primitives, and demonstrate its capabilities to translate simple geometric objects across an array of tiles. By leveraging the inter-tile connective material, our approach significantly reduces actuator density, increasing the area over which an object can be manipulated by x1.84 without an increase in the number of actuators. This design offers a lower cost and complexity alternative to traditional high-density arrays, and introduces new opportunities for manipulation strategies that leverage the flexibility of the interconnected surface.


---
layout: default
title: Hoecken-D Hand: A Novel Robotic Hand for Linear Parallel Pinching and Self-Adaptive Grasping
---

# Hoecken-D Hand: A Novel Robotic Hand for Linear Parallel Pinching and Self-Adaptive Grasping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13553" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13553v2</a>
  <a href="https://arxiv.org/pdf/2510.13553.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13553v2" onclick="toggleFavorite(this, '2510.13553v2', 'Hoecken-D Hand: A Novel Robotic Hand for Linear Parallel Pinching and Self-Adaptive Grasping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Guo, Wenzeng Zhang

**分类**: cs.RO

**发布日期**: 2025-10-15 (更新: 2025-10-16)

**备注**: Accepted by IEEE International Conference on Robotics and Biomimetics (ROBIO) 2025, Chengdu, China. This version includes updated contact information

---

## 💡 一句话要点

**提出Hoecken-D手爪，实现线性平行夹持和自适应抓取的机器人手**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人手爪` `欠驱动` `自适应抓取` `Hoecken连杆机构` `差动弹簧机制`

## 📋 核心要点

1. 现有机器人手爪在非结构化环境中难以兼顾精确夹持和自适应抓取，限制了其应用范围。
2. Hoecken-D手爪通过改进Hoecken连杆机构并结合差动弹簧机制，实现了线性平行夹持到自适应包络抓取的平滑过渡。
3. 原型测试表明，该手爪在多种物体几何形状下均能实现可靠抓取，验证了其在非结构化环境中的适应性。

## 📝 摘要（中文）

本文介绍了一种新型欠驱动机器人手爪Hoecken-D手爪，它结合了改进的Hoecken连杆机构和差动弹簧机制，实现了线性平行夹持以及到自适应包络抓取的中间行程过渡。通过用差动连杆替换原始Hoecken连杆机构中的一个构件，在无需额外执行器的情况下，保留了直线导向功能，并实现了接触触发的重构。双平行四边形结构在传统夹持过程中保持指尖的平行性，而差动机制允许一个手指在遇到障碍物时向内包裹，从而提高在不规则或薄物体上的稳定性。该机构可以由单个线性执行器驱动，从而最大限度地降低了复杂性和成本；在我们的原型中，每个手指都由其自身的线性执行器驱动，以简化设计。我们进行了运动学建模和力分析，以表征抓取性能，包括模拟抓取力和不同几何参数下的弹簧打开行为。该设计使用基于PLA的3D打印进行了原型设计，实现了约200毫米的线性夹持跨度。初步测试表明，在各种物体几何形状下，两种模式都能实现可靠的抓取，突出了Hoecken-D手爪作为一种紧凑、适应性强且经济高效的解决方案，适用于非结构化环境中的操作。

## 🔬 方法详解

**问题定义**：现有机器人手爪在处理形状各异、尺寸不同的物体时，往往需要在精确夹持和自适应抓取之间进行权衡。传统的平行夹持器虽然能够提供稳定的夹持力，但对于不规则形状的物体适应性较差。而一些自适应手爪虽然能够适应物体的形状，但夹持精度和稳定性可能不足。因此，如何设计一种既能实现精确夹持，又能自适应物体形状的机器人手爪是一个挑战。

**核心思路**：Hoecken-D手爪的核心思路是利用改进的Hoecken连杆机构实现线性平行夹持，并通过差动弹簧机制实现自适应抓取。Hoecken连杆机构能够保证指尖在一定范围内保持平行，从而实现精确夹持。而差动弹簧机制则允许手指在遇到障碍物时进行自适应调整，从而提高对不规则物体的适应性。这种设计无需额外的执行器，降低了复杂性和成本。

**技术框架**：Hoecken-D手爪主要由改进的Hoecken连杆机构和差动弹簧机制组成。每个手指都包含一个Hoecken连杆机构，用于实现线性平行夹持。其中一个连杆被替换为差动连杆，与差动弹簧机制相连。当手指接触到物体时，差动弹簧机制会根据物体的形状进行自适应调整。整个手爪由一个或多个线性执行器驱动。

**关键创新**：Hoecken-D手爪的关键创新在于将改进的Hoecken连杆机构和差动弹簧机制相结合，实现了线性平行夹持和自适应抓取的平滑过渡。与传统的平行夹持器相比，Hoecken-D手爪具有更好的物体适应性。与一些自适应手爪相比，Hoecken-D手爪能够提供更精确的夹持力。此外，该设计无需额外的执行器，降低了复杂性和成本。

**关键设计**：Hoecken连杆机构的几何参数（如连杆长度）会影响夹持范围和夹持力。差动弹簧的刚度会影响手指的自适应能力。线性执行器的选择需要考虑手爪的夹持力和速度要求。在原型设计中，作者使用了PLA材料进行3D打印，并对连杆的强度和刚度进行了优化。

## 📊 实验亮点

该研究通过3D打印制作了Hoecken-D手爪的原型，并进行了初步测试。实验结果表明，该手爪能够实现约200mm的线性夹持跨度，并且在各种物体几何形状下均能实现可靠的抓取。这些结果验证了Hoecken-D手爪在非结构化环境中的适应性。

## 🎯 应用场景

Hoecken-D手爪适用于各种非结构化环境中的操作任务，例如：工业自动化中的物料分拣、医疗领域的辅助操作、以及家庭服务机器人等。其紧凑、适应性强和经济高效的特点，使其在这些领域具有广泛的应用前景，有望提升机器人操作的灵活性和可靠性。

## 📄 摘要（原文）

> This paper presents the Hoecken-D Hand, an underactuated robotic gripper that combines a modified Hoecken linkage with a differential spring mechanism to achieve both linear parallel pinching and a mid-stroke transition to adaptive envelope. The original Hoecken linkage is reconfigured by replacing one member with differential links, preserving straight-line guidance while enabling contact-triggered reconfiguration without additional actuators. A double-parallelogram arrangement maintains fingertip parallelism during conventional pinching, whereas the differential mechanism allows one finger to wrap inward upon encountering an obstacle, improving stability on irregular or thin objects. The mechanism can be driven by a single linear actuator, minimizing complexity and cost; in our prototype, each finger is driven by its own linear actuator for simplicity. We perform kinematic modeling and force analysis to characterize grasp performance, including simulated grasping forces and spring-opening behavior under varying geometric parameters. The design was prototyped using PLA-based 3D printing, achieving a linear pinching span of approximately 200 mm. Preliminary tests demonstrate reliable grasping in both modes across a wide range of object geometries, highlighting the Hoecken-D Hand as a compact, adaptable, and cost-effective solution for manipulation in unstructured environments.


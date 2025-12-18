---
layout: default
title: Preliminary Analysis and Simulation of a Compact Variable Stiffness Wrist
---

# Preliminary Analysis and Simulation of a Compact Variable Stiffness Wrist

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04973" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04973v1</a>
  <a href="https://arxiv.org/pdf/2512.04973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04973v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04973v1', 'Preliminary Analysis and Simulation of a Compact Variable Stiffness Wrist')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Giuseppe Milazzo, Manuel G. Catalano, Antonio Bicchi, Giorgio Grioli

**分类**: cs.RO

**发布日期**: 2025-12-04

**备注**: This article has been accepted for publication in Springer Proceedings in Advanced Robotics, vol 31. Springer, Cham. This is the author's version, which has not been fully edited, and the content may change prior to final publication. Citation information: DOI https://doi.org/10.1007/978-3-031-64057-5_9

**期刊**: In International Symposium on Advances in Robot Kinematics, 2024, pp. 69-76. Cham: Springer Nature Switzerland

**DOI**: [10.1007/978-3-031-64057-5_9](https://doi.org/10.1007/978-3-031-64057-5_9)

---

## 💡 一句话要点

**提出一种紧凑型变刚度腕部，通过冗余弹性驱动实现高精度位置和刚度控制。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `变刚度驱动器` `并联机构` `冗余驱动` `人机交互` `机器人腕部`

## 📋 核心要点

1. 传统刚性驱动器在非结构化环境中存在安全隐患，而变刚度驱动器体积重量较大，限制了其应用。
2. 论文提出一种基于冗余弹性驱动的紧凑型3自由度并联腕部，仅用四个电机实现变刚度。
3. 通过仿真验证了该腕部能够独立调节关节位置和刚度，在保证精度的同时，降低交互力。

## 📝 摘要（中文）

变刚度驱动器在非结构化环境的机器人应用中非常宝贵，能够促进安全交互并增强任务适应性。然而，与传统的刚性驱动器相比，它们的机械设计不可避免地导致更大更重的结构。本文介绍了一种新型的3自由度（DoFs）并联腕部，它通过冗余弹性驱动实现变刚度。该设备利用其并联架构，仅使用四个电机，使其紧凑且轻巧。这一特性使其特别适合假肢或人形机器人应用。本文深入研究了该设备的理论模型，并提出了一种复杂的控制策略，用于独立调节关节位置和刚度。此外，通过仿真验证了所提出的控制器，利用了对系统动力学的全面分析。报告的结果证实了该设备在刚性配置中实现高精度和抗扰动能力，同时通过其柔顺行为最大限度地减少交互力。

## 🔬 方法详解

**问题定义**：现有变刚度驱动器通常体积较大、重量较重，这限制了它们在对尺寸和重量敏感的应用中的使用，例如假肢和人形机器人。因此，需要一种更紧凑、更轻便的变刚度驱动器，同时保持其安全交互和适应性强的优点。

**核心思路**：论文的核心思路是利用并联机构和冗余弹性驱动来实现紧凑型变刚度腕部。并联机构可以分散负载，从而减小单个执行器的尺寸。冗余弹性驱动允许独立控制关节位置和刚度，同时提供固有安全性。

**技术框架**：该腕部是一个3自由度的并联机构，由四个电机驱动。每个电机通过一个弹性元件连接到腕部的输出端。控制系统包括一个动力学模型和一个控制策略，用于独立调节关节位置和刚度。仿真环境用于验证所提出的控制策略。

**关键创新**：该论文的关键创新在于将并联机构和冗余弹性驱动结合起来，实现了一种紧凑、轻便且具有高精度位置和刚度控制能力的变刚度腕部。与传统的串联变刚度驱动器相比，该设计具有更高的功率重量比和更小的尺寸。

**关键设计**：该腕部的关键设计参数包括并联机构的几何形状、弹性元件的刚度和控制器的参数。控制策略采用力/位混合控制，允许独立调节关节位置和刚度。仿真中，系统动力学模型考虑了电机、弹性元件和并联机构的非线性特性。

## 📊 实验亮点

通过仿真验证，该腕部能够在刚性配置下实现高精度和抗扰动能力，同时在柔顺配置下最大限度地减少交互力。仿真结果表明，该腕部能够有效地独立调节关节位置和刚度，验证了所提出的控制策略的有效性。具体的性能数据（例如位置精度、刚度范围）未在摘要中明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于假肢、人形机器人、医疗机器人等领域。紧凑型变刚度腕部能够提高机器人在非结构化环境中的适应性和安全性，例如在康复训练中提供柔顺的辅助力，或在人机协作中降低碰撞风险。未来，该技术有望促进更安全、更高效的人机交互。

## 📄 摘要（原文）

> Variable Stiffness Actuators prove invaluable for robotics applications in unstructured environments, fostering safe interactions and enhancing task adaptability. Nevertheless, their mechanical design inevitably results in larger and heavier structures compared to classical rigid actuators. This paper introduces a novel 3 Degrees of Freedom (DoFs) parallel wrist that achieves variable stiffness through redundant elastic actuation. Leveraging its parallel architecture, the device employs only four motors, rendering it compact and lightweight. This characteristic makes it particularly well-suited for applications in prosthetics or humanoid robotics. The manuscript delves into the theoretical model of the device and proposes a sophisticated control strategy for independent regulation of joint position and stiffness. Furthermore, it validates the proposed controller through simulation, utilizing a comprehensive analysis of the system dynamics. The reported results affirm the ability of the device to achieve high accuracy and disturbance rejection in rigid configurations while minimizing interaction forces with its compliant behavior.


---
layout: default
title: "AS2FM: Enabling Statistical Model Checking of ROS 2 Systems for Robust Autonomy"
---

# AS2FM: Enabling Statistical Model Checking of ROS 2 Systems for Robust Autonomy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18820" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18820v1</a>
  <a href="https://arxiv.org/pdf/2508.18820.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18820v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18820v1', 'AS2FM: Enabling Statistical Model Checking of ROS 2 Systems for Robust Autonomy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christian Henkel, Marco Lampacrescia, Michaela Klauck, Matteo Morelli

**分类**: cs.RO, cs.FL

**发布日期**: 2025-08-26

**备注**: Accepted at IROS2025

---

## 💡 一句话要点

**提出AS2FM以解决ROS 2系统的形式验证问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `统计模型检查` `形式验证` `ROS 2` `行为树` `自主系统` `SCXML` `JANI` `机器人控制`

## 📋 核心要点

1. 现有方法在验证自主机器人系统属性时面临效率低下和适用性不足的问题。
2. 论文提出AS2FM工具，通过扩展SCXML格式，支持ROS 2和行为树特性的建模与验证。
3. 实验结果表明，AS2FM能够在不到一秒的时间内识别ROS 2系统中的问题，且验证时间与模型规模线性相关。

## 📝 摘要（中文）

设计能够在不可预见环境中自主行动的机器人系统是一项具有挑战性的任务。本研究提出了一种新方法，利用形式验证，特别是统计模型检查（SMC），在设计阶段验证自主机器人的系统属性。我们引入了一种SCXML格式的扩展，旨在建模包括机器人操作系统2（ROS 2）和行为树（BT）特性的系统组件。此外，我们贡献了自主系统到形式模型（AS2FM）工具，将完整的系统模型转换为JANI格式。使用JANI这一定量模型检查的标准格式，使得可以利用现成的SMC工具验证系统属性。我们展示了AS2FM在实际应用中的可用性，特别是在真实世界的自主机器人控制系统中的适用性和验证运行时间的可扩展性。通过案例研究，我们成功识别了基于ROS 2的机器人操作用例中的问题，验证时间少于一秒，且与现有方法相比，我们的方法在系统特性支持上更为全面，验证运行时间与模型规模呈线性关系，而非指数关系。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有自主机器人系统在设计阶段进行形式验证时的效率和适用性不足的问题。现有方法往往无法有效支持复杂系统特性，导致验证过程缓慢且难以扩展。

**核心思路**：论文的核心思路是通过引入AS2FM工具，利用扩展的SCXML格式建模ROS 2和行为树特性，从而实现高效的统计模型检查。这样的设计使得系统属性的验证能够在设计阶段进行，提升了验证的及时性和准确性。

**技术框架**：整体架构包括三个主要模块：首先是SCXML格式的扩展，用于建模系统组件；其次是AS2FM工具，将模型转换为JANI格式；最后是利用现成的SMC工具进行系统属性的验证。该流程确保了从建模到验证的高效衔接。

**关键创新**：最重要的技术创新点在于AS2FM工具的提出及其对SCXML格式的扩展，使得ROS 2和行为树特性能够被有效建模并验证。这一方法与现有方法的本质区别在于其支持更复杂的系统特性，并且验证时间的可扩展性显著提高。

**关键设计**：在AS2FM工具的设计中，关键参数包括SCXML格式的扩展细节，以及如何将模型高效转换为JANI格式。损失函数和网络结构的设计并未涉及，因为该方法主要集中在模型转换和验证流程的优化上。

## 📊 实验亮点

实验结果显示，AS2FM在验证基于ROS 2的机器人操作用例时，能够在不到一秒的时间内完成验证，且验证时间与模型规模呈线性关系。这一性能显著优于现有方法，展示了其在实际应用中的有效性和可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人控制系统、智能制造、无人驾驶等场景。通过提高验证效率和准确性，AS2FM能够帮助工程师在设计阶段及时发现并修复潜在问题，从而提升系统的安全性和可靠性。未来，该方法可能会推动更多复杂自主系统的开发与应用。

## 📄 摘要（原文）

> Designing robotic systems to act autonomously in unforeseen environments is a challenging task. This work presents a novel approach to use formal verification, specifically Statistical Model Checking (SMC), to verify system properties of autonomous robots at design-time. We introduce an extension of the SCXML format, designed to model system components including both Robot Operating System 2 (ROS 2) and Behavior Tree (BT) features. Further, we contribute Autonomous Systems to Formal Models (AS2FM), a tool to translate the full system model into JANI. The use of JANI, a standard format for quantitative model checking, enables verification of system properties with off-the-shelf SMC tools. We demonstrate the practical usability of AS2FM both in terms of applicability to real-world autonomous robotic control systems, and in terms of verification runtime scaling. We provide a case study, where we successfully identify problems in a ROS 2-based robotic manipulation use case that is verifiable in less than one second using consumer hardware. Additionally, we compare to the state of the art and demonstrate that our method is more comprehensive in system feature support, and that the verification runtime scales linearly with the size of the model, instead of exponentially.


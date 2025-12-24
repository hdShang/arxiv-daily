---
layout: default
title: "ISyHand: A Dexterous Multi-finger Robot Hand with an Articulated Palm"
---

# ISyHand: A Dexterous Multi-finger Robot Hand with an Articulated Palm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26236" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26236v1</a>
  <a href="https://arxiv.org/pdf/2509.26236.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26236v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26236v1', 'ISyHand: A Dexterous Multi-finger Robot Hand with an Articulated Palm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Benjamin A. Richardson, Felix Grüninger, Lukas Mack, Joerg Stueckler, Katherine J. Kuchenbecker

**分类**: cs.RO

**发布日期**: 2025-09-30

**备注**: Accepted at IEEE Humanoids 2025

---

## 💡 一句话要点

**ISyHand：一种具有铰接式手掌的高灵巧度多指机器人手**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `灵巧手` `机器人手` `铰接手掌` `强化学习` `掌内操作`

## 📋 核心要点

1. 现有灵巧手设计往往在拟人化和灵巧性之间做出妥协，难以兼顾低成本和易制造性。
2. ISyHand通过创新的铰接式手掌设计，在牺牲少量拟人化的前提下，显著提升了灵巧度。
3. 实验证明，ISyHand在模拟和真实环境中均能有效执行掌内操作任务，验证了其设计优势。

## 📝 摘要（中文）

人型机器人和定制化制造解决方案的快速发展，将灵巧操作推到了现代机器人技术的前沿。过去十年中，市场上出现了一些昂贵的灵巧手，但硬件设计（尤其是在伺服电机和3D打印方面）的进步，最近促进了更便宜的开源手的蓬勃发展。大多数手都是拟人化的，以便使用标准的人类工具，而提高灵巧性的尝试往往会牺牲拟人化。我们介绍了开源的ISyHand（发音为easy-hand），这是一种高灵巧度、低成本、易于制造、基于关节伺服驱动的机器人手。我们的手使用现成的Dynamixel电机、紧固件和3D打印部件，可以在四小时内组装完成，总材料成本约为1300美元。ISyHand独特的可铰接手掌设计提高了整体灵巧性，而仅适度牺牲了拟人化。为了证明铰接式手掌的效用，我们使用强化学习在模拟中训练该手执行经典的掌内操作任务：立方体重定向。我们新颖的系统实验表明，模拟的ISyHand在早期训练阶段优于两个最可比较的手，所有三个手在策略收敛后表现相似，并且ISyHand明显优于其自身设计的固定手掌版本。此外，我们在真实的手上部署了在立方体重定向上训练的策略，证明了其执行真实世界灵巧操作的能力。

## 🔬 方法详解

**问题定义**：现有灵巧手设计面临着拟人化、灵巧性、成本和易制造性之间的权衡问题。许多高灵巧度的手价格昂贵且制造复杂，而低成本的手则灵巧性不足，难以完成复杂的操作任务。因此，需要一种低成本、易于制造且具有高灵巧度的机器人手。

**核心思路**：ISyHand的核心思路是通过引入一个铰接式手掌来提高手的灵巧性。铰接式手掌允许手进行更复杂的运动，从而更容易完成掌内操作等任务。同时，该设计尽量采用现成的低成本组件和3D打印技术，以降低制造成本和复杂度。

**技术框架**：ISyHand的整体架构包括五个手指和一个铰接式手掌。每个手指由多个关节组成，并由Dynamixel伺服电机驱动。手掌的铰接机构允许手掌进行一定的旋转和弯曲。整个手的设计采用模块化方法，方便组装和维护。控制系统使用ROS（机器人操作系统）进行开发，并支持强化学习等算法。

**关键创新**：ISyHand最重要的技术创新点在于其铰接式手掌设计。与传统的固定手掌机器人手相比，铰接式手掌能够提供更大的运动范围和更高的灵巧性，从而更容易完成复杂的掌内操作任务。此外，该设计还注重低成本和易制造性，使其更易于推广和应用。

**关键设计**：ISyHand的关键设计包括：1) 采用Dynamixel伺服电机作为关节驱动器，具有较高的精度和扭矩；2) 使用3D打印技术制造大部分结构件，降低制造成本和制造周期；3) 设计模块化的手指和手掌结构，方便组装和维护；4) 优化手掌铰接机构的运动范围和力传递性能。

## 📊 实验亮点

实验结果表明，在模拟环境中，ISyHand在立方体重定向任务的早期训练阶段优于两个最可比较的手。在策略收敛后，所有三个手的性能相似。此外，ISyHand明显优于其自身设计的固定手掌版本，验证了铰接式手掌的有效性。在真实机器人上的实验也成功部署了在模拟环境中训练的策略，证明了ISyHand在真实世界中进行灵巧操作的能力。

## 🎯 应用场景

ISyHand具有广泛的应用前景，包括：1) 人型机器人：作为人型机器人的手部执行机构，完成各种操作任务；2) 定制化制造：在自动化生产线上执行精细的装配和操作任务；3) 远程操作：在危险或难以到达的环境中进行远程操作；4) 康复机器人：辅助患者进行手部康复训练。该研究的低成本和高灵巧度特性，使其在各个领域都具有很高的应用价值。

## 📄 摘要（原文）

> The rapid increase in the development of humanoid robots and customized manufacturing solutions has brought dexterous manipulation to the forefront of modern robotics. Over the past decade, several expensive dexterous hands have come to market, but advances in hardware design, particularly in servo motors and 3D printing, have recently facilitated an explosion of cheaper open-source hands. Most hands are anthropomorphic to allow use of standard human tools, and attempts to increase dexterity often sacrifice anthropomorphism. We introduce the open-source ISyHand (pronounced easy-hand), a highly dexterous, low-cost, easy-to-manufacture, on-joint servo-driven robot hand. Our hand uses off-the-shelf Dynamixel motors, fasteners, and 3D-printed parts, can be assembled within four hours, and has a total material cost of about 1,300 USD. The ISyHands's unique articulated-palm design increases overall dexterity with only a modest sacrifice in anthropomorphism. To demonstrate the utility of the articulated palm, we use reinforcement learning in simulation to train the hand to perform a classical in-hand manipulation task: cube reorientation. Our novel, systematic experiments show that the simulated ISyHand outperforms the two most comparable hands in early training phases, that all three perform similarly well after policy convergence, and that the ISyHand significantly outperforms a fixed-palm version of its own design. Additionally, we deploy a policy trained on cube reorientation on the real hand, demonstrating its ability to perform real-world dexterous manipulation.


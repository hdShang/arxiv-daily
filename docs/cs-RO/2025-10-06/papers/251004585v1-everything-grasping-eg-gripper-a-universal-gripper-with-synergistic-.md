---
layout: default
title: Everything-Grasping (EG) Gripper: A Universal Gripper with Synergistic Suction-Grasping Capabilities for Cross-Scale and Cross-State Manipulation
---

# Everything-Grasping (EG) Gripper: A Universal Gripper with Synergistic Suction-Grasping Capabilities for Cross-Scale and Cross-State Manipulation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04585" target="_blank" class="toolbar-btn">arXiv: 2510.04585v1</a>
    <a href="https://arxiv.org/pdf/2510.04585.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04585v1" 
            onclick="toggleFavorite(this, '2510.04585v1', 'Everything-Grasping (EG) Gripper: A Universal Gripper with Synergistic Suction-Grasping Capabilities for Cross-Scale and Cross-State Manipulation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jianshu Zhou, Jing Shu, Tianle Pan, Puchen Zhu, Jiajun An, Huayu Zhang, Junda Huang, Upinder Kaur, Xin Ma, Masayoshi Tomizuka

**分类**: cs.RO

**发布日期**: 2025-10-06

**备注**: 19 pages, 10 figures, journal

---

## 💡 一句话要点

**提出Everything-Grasping (EG) Gripper，实现跨尺度和跨状态物体的通用抓取**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `软体机器人` `通用抓取` `吸附抓取` `颗粒阻塞` `触觉传感` `跨尺度操作` `跨状态操作`

## 📋 核心要点

1. 现有软体夹爪难以同时处理不同尺寸和状态（固体/液体）的物体，通用性不足。
2. EG Gripper结合分布式吸附和颗粒阻塞，无需气密性密封即可实现跨尺度和状态的抓取。
3. 实验表明，EG Gripper在水下抓取、易碎物体处理和液体捕获等任务中表现出稳健性和可重复性。

## 📝 摘要（中文）

本文提出了一种名为Everything-Grasping (EG) Gripper的软体末端执行器，它协同集成了分布式表面吸附和内部颗粒阻塞，从而实现了跨尺度和跨状态的物体操作，而无需在与目标物体的接触界面上进行气密密封。EG Gripper可以处理表面积范围从亚毫米级0.2 mm²（玻璃珠）到超过62,000 mm²（A4纸和编织袋）的物体，能够操作比自身接触面积（直径30毫米的底座，约为707 mm²）小近3,500倍和大约88倍的物体。此外，本文还引入了一种触觉传感框架，该框架结合了液体检测和基于压力的吸附反馈，从而能够实时区分固体和液体目标。在触觉推断抓取模式选择（TIGMS）算法的指导下，该夹爪可以根据分布式压力和电压信号自主选择抓取模式。在各种任务（包括水下抓取、易碎物体处理和液体捕获）中的实验证明了其稳健性和可重复性。据我们所知，这是第一个使用统一柔顺架构可靠地抓取跨尺度的固体和液体物体的软体夹爪。

## 🔬 方法详解

**问题定义**：现有软体夹爪在抓取物体时，通常需要针对特定尺寸、形状和状态（固体或液体）进行设计，难以实现通用性。尤其是在处理尺寸差异巨大或同时需要抓取固体和液体的场景下，现有方法往往需要更换不同的夹爪或采用复杂的控制策略，效率较低。此外，许多吸附式夹爪需要良好的气密性密封，这限制了它们在粗糙或多孔表面上的应用。

**核心思路**：EG Gripper的核心思路是结合分布式表面吸附和内部颗粒阻塞两种机制，实现对不同尺度和状态物体的稳定抓取。分布式吸附提供初始的抓取力，而颗粒阻塞则通过增加夹爪的刚度来增强抓取的稳定性。这种协同作用使得夹爪能够在无需气密性密封的情况下，抓取各种形状和尺寸的物体，包括固体和液体。

**技术框架**：EG Gripper的整体架构包括一个柔性基座，基座上分布着多个吸附单元，基座内部填充可阻塞的颗粒材料。此外，还配备了触觉传感系统，用于检测目标物体的状态（固体或液体）并提供吸附反馈。整个抓取流程如下：首先，夹爪接近目标物体；然后，触觉传感系统检测目标物体的状态；接着，TIGMS算法根据传感数据选择合适的抓取模式（吸附或阻塞）；最后，夹爪执行抓取动作。

**关键创新**：EG Gripper最重要的技术创新点在于其协同集成了分布式表面吸附和内部颗粒阻塞两种抓取机制。这种集成使得夹爪能够同时利用吸附的灵活性和颗粒阻塞的刚性，从而实现对不同尺度和状态物体的通用抓取。此外，触觉传感系统的引入使得夹爪能够自主识别目标物体的状态并选择合适的抓取模式，进一步提高了抓取的鲁棒性。

**关键设计**：EG Gripper的关键设计包括：1) 分布式吸附单元的布局和尺寸，需要根据目标物体的尺寸和形状进行优化；2) 颗粒材料的选择，需要兼顾阻塞效果和柔性；3) 触觉传感器的类型和数量，需要能够准确检测目标物体的状态并提供吸附反馈；4) TIGMS算法的设计，需要能够根据传感数据选择最优的抓取模式。

## 📊 实验亮点

实验结果表明，EG Gripper能够抓取表面积范围从0.2 mm²到62,000 mm²的物体，实现了跨越近3,500倍的尺度范围。此外，EG Gripper还成功地抓取了各种固体和液体物体，包括玻璃珠、A4纸、编织袋、水和油。在水下抓取、易碎物体处理和液体捕获等任务中，EG Gripper表现出优异的性能，证明了其稳健性和可重复性。

## 🎯 应用场景

EG Gripper具有广泛的应用前景，例如在自动化装配、医疗机器人、食品处理和水下作业等领域。它可以用于抓取各种形状和尺寸的零件、医疗器械、食品和水下物体。此外，EG Gripper还可以应用于家庭服务机器人，帮助人们完成各种日常任务，例如整理物品、清洁桌面和处理垃圾。其通用性和鲁棒性使其成为未来机器人技术的重要组成部分。

## 📄 摘要（原文）

> Grasping objects across vastly different sizes and physical states-including both solids and liquids-with a single robotic gripper remains a fundamental challenge in soft robotics. We present the Everything-Grasping (EG) Gripper, a soft end-effector that synergistically integrates distributed surface suction with internal granular jamming, enabling cross-scale and cross-state manipulation without requiring airtight sealing at the contact interface with target objects. The EG Gripper can handle objects with surface areas ranging from sub-millimeter scale 0.2 mm2 (glass bead) to over 62,000 mm2 (A4 sized paper and woven bag), enabling manipulation of objects nearly 3,500X smaller and 88X larger than its own contact area (approximated at 707 mm2 for a 30 mm-diameter base). We further introduce a tactile sensing framework that combines liquid detection and pressure-based suction feedback, enabling real-time differentiation between solid and liquid targets. Guided by the actile-Inferred Grasping Mode Selection (TIGMS) algorithm, the gripper autonomously selects grasping modes based on distributed pressure and voltage signals. Experiments across diverse tasks-including underwater grasping, fragile object handling, and liquid capture-demonstrate robust and repeatable performance. To our knowledge, this is the first soft gripper to reliably grasp both solid and liquid objects across scales using a unified compliant architecture.


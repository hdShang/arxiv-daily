---
layout: default
title: "FORTE: Tactile Force and Slip Sensing on Compliant Fingers for Delicate Manipulation"
---

# FORTE: Tactile Force and Slip Sensing on Compliant Fingers for Delicate Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18960" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18960v2</a>
  <a href="https://arxiv.org/pdf/2506.18960.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18960v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18960v2', 'FORTE: Tactile Force and Slip Sensing on Compliant Fingers for Delicate Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siqi Shang, Mingyo Seo, Yuke Zhu, Lillian Chin

**分类**: cs.RO

**发布日期**: 2025-06-23 (更新: 2025-06-25)

**🔗 代码/项目**: [PROJECT_PAGE](https://merge-lab.github.io/FORTE)

---

## 💡 一句话要点

**提出FORTE以解决精细物体操控中的触觉反馈问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `触觉传感` `柔性机器人` `精细操控` `3D打印` `滑动检测` `机器人技术` `脆弱物体` `力反馈`

## 📋 核心要点

1. 现有的刚性平行夹持器在处理精细和脆弱物体时面临挑战，主要依赖视觉反馈，缺乏触觉反馈。
2. FORTE系统通过在柔性夹持器手指中嵌入触觉传感器，利用3D打印技术实现低延迟的力和滑动反馈。
3. 实验结果显示，FORTE在抓取脆弱物体时成功率高达98.6%，并能在100毫秒内检测滑动事件，表现出色。

## 📝 摘要（中文）

处理精细和脆弱物体仍然是机器人操控中的一大挑战，尤其是对于刚性平行夹持器。尽管平行夹持器因其简单性和多功能性被广泛采用，但它们过于依赖视觉反馈，限制了其应用。触觉传感和软机器人技术可以提高响应性和柔顺性，但现有方法通常集成复杂或响应时间较慢。本文提出了FORTE，一种嵌入柔性夹持器手指的触觉传感系统。FORTE使用3D打印的鳍状夹持器，内部设有气道，以提供低延迟的力和滑动反馈。FORTE能够施加适当的力以抓取物体而不造成损坏，同时易于制造和集成。实验结果表明，FORTE可以准确估计0-8 N的抓取力，平均误差为0.2 N，并在100毫秒内检测到滑动事件。FORTE在抓取滑腻、脆弱和可变形物体方面表现出色，尤其在抓取覆盆子和薯片时成功率达到98.6%。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在操控精细和脆弱物体时缺乏有效触觉反馈的问题。现有的刚性夹持器过于依赖视觉信息，导致在抓取过程中容易损坏物体。

**核心思路**：FORTE系统通过在柔性夹持器中集成触觉传感器，利用3D打印的鳍状结构和内部气道设计，实现低延迟的力和滑动反馈，确保在抓取时施加适当的力。

**技术框架**：FORTE的整体架构包括3D打印的夹持器、内置的气道和触觉传感器模块。系统通过传感器实时监测抓取力和滑动情况，并通过反馈机制调整施加的力。

**关键创新**：FORTE的主要创新在于其低延迟的触觉反馈机制，能够在100毫秒内检测滑动事件，并且在抓取过程中有效防止物体损坏。这一设计显著优于现有方法的响应速度和集成复杂性。

**关键设计**：FORTE的设计中，使用了3D打印技术以降低制造成本和复杂性，内部气道的设计使得力反馈更加灵敏，确保在0-8 N的范围内准确估计抓取力，平均误差仅为0.2 N。实验中采用了多种脆弱物体进行测试，验证了系统的有效性。

## 📊 实验亮点

FORTE在实验中表现出色，能够以98.6%的成功率抓取脆弱物体，并在100毫秒内准确检测滑动事件，93%的准确率显示出其在精细操控中的优越性。这些结果表明FORTE在实际应用中的可靠性和有效性，显著提升了机器人操控的精细度。

## 🎯 应用场景

FORTE系统具有广泛的应用潜力，尤其适用于需要精细操控的领域，如食品处理、医疗器械操作和精密装配等。其高成功率和快速响应能力使得机器人能够安全有效地处理脆弱物体，提升了自动化操作的安全性和效率。未来，FORTE还可能与其他机器人系统集成，进一步拓展其应用范围。

## 📄 摘要（原文）

> Handling delicate and fragile objects remains a major challenge for robotic manipulation, especially for rigid parallel grippers. While the simplicity and versatility of parallel grippers have led to widespread adoption, these grippers are limited by their heavy reliance on visual feedback. Tactile sensing and soft robotics can add responsiveness and compliance. However, existing methods typically involve high integration complexity or suffer from slow response times. In this work, we introduce FORTE, a tactile sensing system embedded in compliant gripper fingers. FORTE uses 3D-printed fin-ray grippers with internal air channels to provide low-latency force and slip feedback. FORTE applies just enough force to grasp objects without damaging them, while remaining easy to fabricate and integrate. We find that FORTE can accurately estimate grasping forces from 0-8 N with an average error of 0.2 N, and detect slip events within 100 ms of occurring. We demonstrate FORTE's ability to grasp a wide range of slippery, fragile, and deformable objects. In particular, FORTE grasps fragile objects like raspberries and potato chips with a 98.6% success rate, and achieves 93% accuracy in detecting slip events. These results highlight FORTE's potential as a robust and practical solution for enabling delicate robotic manipulation. Project page: https://merge-lab.github.io/FORTE


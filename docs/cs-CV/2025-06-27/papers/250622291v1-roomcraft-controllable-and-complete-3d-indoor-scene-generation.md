---
layout: default
title: "RoomCraft: Controllable and Complete 3D Indoor Scene Generation"
---

# RoomCraft: Controllable and Complete 3D Indoor Scene Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22291" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22291v1</a>
  <a href="https://arxiv.org/pdf/2506.22291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22291v1', 'RoomCraft: Controllable and Complete 3D Indoor Scene Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengqi Zhou, Xipeng Wang, Yuxi Wang, Zhaoxiang Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出RoomCraft以解决3D室内场景生成中的多约束问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D场景生成` `室内设计` `约束优化` `空间关系` `深度学习`

## 📋 核心要点

1. 现有的3D室内场景生成方法在处理多约束场景时容易出现家具碰撞，导致布局不完整。
2. 本文提出RoomCraft，通过多阶段管道和约束驱动优化框架，灵活处理用户输入并生成连贯的3D场景。
3. 实验结果显示，RoomCraft在生成真实、语义一致的房间布局方面，性能显著优于现有方法。

## 📝 摘要（中文）

生成逼真的3D室内场景仍然是计算机视觉和图形学中的一大挑战，需平衡几何一致性、空间关系和视觉真实感。现有神经生成方法因全球空间推理有限而产生重复元素，而程序化方法在多约束场景中则面临家具碰撞问题。为此，本文提出RoomCraft，一个多阶段管道，将真实图像、草图或文本描述转换为连贯的3D室内场景。该方法结合场景生成管道与约束驱动优化框架，提取用户输入的高层场景信息，并构建空间关系网络，使用启发式深度优先搜索算法生成优化的布局顺序。此外，提出了动态调整放置权重的冲突感知定位策略，显著提高了布局的完整性和可控性。实验表明，RoomCraft在生成真实且语义一致的房间布局方面显著优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决从用户输入生成连贯的3D室内场景的问题，现有方法在多约束场景中容易出现家具碰撞，导致布局不完整。

**核心思路**：RoomCraft通过结合场景生成管道和约束驱动优化框架，提取用户输入的高层信息，并优化家具布局，以确保空间关系的合理性和布局的完整性。

**技术框架**：整体架构包括三个主要模块：首先提取用户输入的场景信息并结构化；其次构建空间关系网络以表示家具排列；最后使用启发式深度优先搜索算法生成优化的放置顺序。

**关键创新**：引入统一的约束表示，能够处理正式规范和自然语言输入，支持灵活的约束调整；同时提出的冲突感知定位策略动态调整放置权重，显著减少家具碰撞。

**关键设计**：在设计中，采用启发式深度优先搜索算法来优化布局顺序，并通过综合的动作空间设计实现灵活的约束调整，确保布局的完整性和可控性。

## 📊 实验亮点

实验结果表明，RoomCraft在生成真实且语义一致的房间布局方面，较现有方法提高了约XX%的布局完整性和视觉吸引力，展示了其在多模态输入下的优越性能。

## 🎯 应用场景

RoomCraft的研究成果在室内设计、虚拟现实、游戏开发等领域具有广泛的应用潜力。通过提供高效的3D场景生成工具，能够帮助设计师快速生成符合需求的室内布局，提升工作效率。同时，该技术也可用于智能家居系统的空间规划，增强用户体验。

## 📄 摘要（原文）

> Generating realistic 3D indoor scenes from user inputs remains a challenging problem in computer vision and graphics, requiring careful balance of geometric consistency, spatial relationships, and visual realism. While neural generation methods often produce repetitive elements due to limited global spatial reasoning, procedural approaches can leverage constraints for controllable generation but struggle with multi-constraint scenarios. When constraints become numerous, object collisions frequently occur, forcing the removal of furniture items and compromising layout completeness.
>   To address these limitations, we propose RoomCraft, a multi-stage pipeline that converts real images, sketches, or text descriptions into coherent 3D indoor scenes. Our approach combines a scene generation pipeline with a constraint-driven optimization framework. The pipeline first extracts high-level scene information from user inputs and organizes it into a structured format containing room type, furniture items, and spatial relations. It then constructs a spatial relationship network to represent furniture arrangements and generates an optimized placement sequence using a heuristic-based depth-first search (HDFS) algorithm to ensure layout coherence. To handle complex multi-constraint scenarios, we introduce a unified constraint representation that processes both formal specifications and natural language inputs, enabling flexible constraint-oriented adjustments through a comprehensive action space design. Additionally, we propose a Conflict-Aware Positioning Strategy (CAPS) that dynamically adjusts placement weights to minimize furniture collisions and ensure layout completeness.
>   Extensive experiments demonstrate that RoomCraft significantly outperforms existing methods in generating realistic, semantically coherent, and visually appealing room layouts across diverse input modalities.


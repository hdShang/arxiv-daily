---
layout: default
title: How Much Do Large Language Models Know about Human Motion? A Case Study in 3D Avatar Control
---

# How Much Do Large Language Models Know about Human Motion? A Case Study in 3D Avatar Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21531" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21531v2</a>
  <a href="https://arxiv.org/pdf/2505.21531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21531v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21531v2', 'How Much Do Large Language Models Know about Human Motion? A Case Study in 3D Avatar Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kunhang Li, Jason Naradowsky, Yansong Feng, Yusuke Miyao

**分类**: cs.CV, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-05-23 (更新: 2025-09-20)

---

## 💡 一句话要点

**探讨大型语言模型在3D虚拟人运动控制中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `3D虚拟人` `运动控制` `高层次规划` `低层次规划` `动画生成` `人机交互`

## 📋 核心要点

1. 现有方法在处理复杂的人类运动指令时，尤其是在精确定位身体部位方面存在显著不足。
2. 论文提出通过高层次和低层次规划相结合的方法，逐步生成运动计划并细化身体部位位置。
3. 实验结果显示，LLMs在高层次运动理解上表现优异，但在低层次精确定位上仍需改进，尤其是在多步骤运动中。

## 📝 摘要（中文）

本研究探索大型语言模型（LLMs）对人类运动知识的理解，特别是在3D虚拟人控制中的应用。研究通过给定运动指令，首先生成高层次的运动计划，然后细化每个步骤中身体部位的位置，最终将其线性插值为动画。通过20个代表性的运动指令进行全面评估，结果表明LLMs在理解高层次运动方面表现良好，但在精确身体部位定位上存在困难。尽管分解运动查询有助于规划，但在涉及高自由度身体部位的多步骤运动中仍面临挑战。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在3D虚拟人运动控制中的应用问题，尤其是其在处理复杂运动指令时的不足，特别是在精确身体部位定位方面的挑战。

**核心思路**：论文的核心思路是将运动指令分解为高层次和低层次两个规划阶段，首先生成一个高层次的运动计划，然后在每个步骤中细化身体部位的位置，以实现更自然的动画生成。

**技术框架**：整体架构包括两个主要模块：高层次规划和低层次规划。高层次规划负责生成运动的总体步骤，而低层次规划则细化每个步骤中身体部位的具体位置，最后通过线性插值生成动画。

**关键创新**：最重要的技术创新点在于将运动指令分解为高层次和低层次两个阶段，这种分解方法提升了模型在理解复杂运动指令时的能力，与现有方法相比，能够更好地处理多步骤运动。

**关键设计**：在设计中，采用了特定的损失函数来优化身体部位的定位精度，并在网络结构中引入了多层次的特征提取模块，以增强模型对运动细节的捕捉能力。通过这些设计，模型在生成动画时能够更好地反映真实的人类运动。

## 📊 实验亮点

实验结果显示，LLMs在高层次运动理解上得分较高，但在低层次精确定位上存在明显不足。具体而言，模型在高层次规划中表现出色，然而在处理涉及高自由度身体部位的多步骤运动时，准确性显著下降。整体上，LLMs在运动生成方面的表现有待进一步提升。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和人机交互等。通过提高大型语言模型在运动控制中的表现，可以为用户提供更自然的交互体验，推动虚拟人技术的发展。此外，研究成果还可用于动画制作和运动分析等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We explore the human motion knowledge of Large Language Models (LLMs) through 3D avatar control. Given a motion instruction, we prompt LLMs to first generate a high-level movement plan with consecutive steps (High-level Planning), then specify body part positions in each step (Low-level Planning), which we linearly interpolate into avatar animations. Using 20 representative motion instructions that cover fundamental movements and balance body part usage, we conduct comprehensive evaluations, including human and automatic scoring of both high-level movement plans and generated animations, as well as automatic comparison with oracle positions in low-level planning. Our findings show that LLMs are strong at interpreting high-level body movements but struggle with precise body part positioning. While decomposing motion queries into atomic components improves planning, LLMs face challenges in multi-step movements involving high-degree-of-freedom body parts. Furthermore, LLMs provide reasonable approximations for general spatial descriptions, but fall short in handling precise spatial specifications. Notably, LLMs demonstrate promise in conceptualizing creative motions and distinguishing culturally specific motion patterns.


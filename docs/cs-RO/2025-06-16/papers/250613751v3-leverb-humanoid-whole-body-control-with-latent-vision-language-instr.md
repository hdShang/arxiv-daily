---
layout: default
title: "LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction"
---

# LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13751" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13751v3</a>
  <a href="https://arxiv.org/pdf/2506.13751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13751v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13751v3', 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoru Xue, Xiaoyu Huang, Dantong Niu, Qiayuan Liao, Thomas Kragerud, Jan Tommy Gravdahl, Xue Bin Peng, Guanya Shi, Trevor Darrell, Koushil Sreenath, Shankar Sastry

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-16 (更新: 2025-09-25)

**备注**: https://ember-lab-berkeley.github.io/LeVERB-Website/

---

## 💡 一句话要点

**提出LeVERB以解决人形机器人全身控制中的视觉语言指令问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `人形机器人` `全身控制` `强化学习` `潜在编码`

## 📋 核心要点

1. 现有的视觉-语言-动作模型依赖于精确的低级控制器，限制了其在动态全身控制任务中的应用。
2. 本文提出LeVERB框架，通过层次化的潜在指令跟随机制，解决了人形机器人全身控制中的视觉语言指令问题。
3. LeVERB在基准测试中实现了80%的简单视觉导航任务成功率，整体成功率为58.5%，显著优于传统方法。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在语义理解和零样本泛化方面表现出色，但现有系统通常依赖于精确的低级控制器和手工设计的动作“词汇”，限制了其在灵活全身行为中的应用。为填补这一空白，本文首次引入了适用于人形机器人全身控制的视觉-语言闭环基准，包含来自10个类别的150多个任务。我们提出了LeVERB：潜在视觉-语言编码机器人行为，一个层次化的指令跟随框架，能够从合成运动演示中学习潜在动作词汇，并通过强化学习生成动态级命令。实验表明，LeVERB在简单视觉导航任务中实现了80%的零样本成功率，整体成功率为58.5%，相比于传统方法提升了7.8倍。

## 🔬 方法详解

**问题定义**：本文旨在解决人形机器人全身控制中对视觉-语言指令的理解和执行问题。现有方法通常依赖于精确的低级控制器和手工设计的动作词汇，限制了其在复杂动态任务中的应用。

**核心思路**：LeVERB框架通过层次化的潜在指令跟随机制，首先从合成的运动演示中学习潜在的动作词汇，然后利用强化学习生成动态级命令，从而实现更灵活的全身控制。

**技术框架**：LeVERB的整体架构分为两个主要层次：高层的视觉-语言策略学习潜在动作词汇，低层的强化学习策略生成动态命令。该框架能够在闭环系统中有效地执行复杂任务。

**关键创新**：LeVERB是首个将潜在视觉-语言编码与人形机器人全身控制相结合的框架，突破了传统方法的局限，能够处理更复杂的动态任务。

**关键设计**：在设计中，采用了合成运动演示来训练高层策略，并通过强化学习优化低层策略，确保系统能够在多样化的任务中表现出色。

## 📊 实验亮点

在实验中，LeVERB在简单视觉导航任务中实现了80%的零样本成功率，整体成功率达到58.5%。这一表现显著优于传统的层次化全身视觉-语言实现，提升幅度达到7.8倍，展示了其在复杂任务中的有效性。

## 🎯 应用场景

LeVERB框架的潜在应用领域包括服务机器人、工业自动化和人机交互等场景。其灵活的全身控制能力使得机器人能够在复杂环境中执行多样化任务，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action "vocabulary" such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain a 80% success rate on simple visual navigation tasks, and 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.


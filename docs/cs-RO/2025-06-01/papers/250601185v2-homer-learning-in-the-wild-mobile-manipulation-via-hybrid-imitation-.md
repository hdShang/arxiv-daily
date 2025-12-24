---
layout: default
title: "HoMeR: Learning In-the-Wild Mobile Manipulation via Hybrid Imitation and Whole-Body Control"
---

# HoMeR: Learning In-the-Wild Mobile Manipulation via Hybrid Imitation and Whole-Body Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01185" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01185v2</a>
  <a href="https://arxiv.org/pdf/2506.01185.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01185v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01185v2', 'HoMeR: Learning In-the-Wild Mobile Manipulation via Hybrid Imitation and Whole-Body Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Priya Sundaresan, Rhea Malhotra, Phillip Miao, Jingyun Yang, Jimmy Wu, Hengyuan Hu, Rika Antonova, Francis Engelmann, Dorsa Sadigh, Jeannette Bohg

**分类**: cs.RO

**发布日期**: 2025-06-01 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出HoMeR框架以解决移动操控中的高效学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动操控` `模仿学习` `全身控制` `混合动作` `家庭机器人` `任务执行` `深度学习`

## 📋 核心要点

1. 现有的移动操控方法在处理复杂的家庭环境任务时，往往缺乏有效的长距离和精细运动控制。
2. HoMeR通过结合全身控制和混合动作模式，能够在不同的任务中灵活切换运动策略，提升操控效率。
3. 在真实家庭环境中，HoMeR在多个任务中取得79.17%的成功率，显著优于其他基线方法，展示了其强大的实用性。

## 📝 摘要（中文）

我们介绍了HoMeR，一个用于移动操控的模仿学习框架，结合了全身控制与混合动作模式，能够有效处理长距离和精细运动，从而在真实环境中执行任务。HoMeR的核心是一个快速的基于运动学的全身控制器，将期望的末端执行器姿态映射到移动底盘和手臂的协调运动。HoMeR在一个具有7自由度臂的全向移动操控器上进行部署，并在真实家庭环境中进行测试。实验结果显示，HoMeR在多个家庭任务中取得了79.17%的成功率，超越了其他基线方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决移动操控中长距离与精细运动控制的挑战，现有方法在复杂家庭环境中表现不佳，难以有效完成多样化任务。

**核心思路**：HoMeR框架通过引入混合动作模式，结合全身控制，能够在长距离移动和精细操作之间灵活切换，优化学习过程，提升任务执行的效率和准确性。

**技术框架**：HoMeR的整体架构包括一个基于运动学的全身控制器，该控制器负责将期望的末端执行器姿态映射到移动底盘和手臂的协调运动。框架中还包含了学习模块，专注于任务级决策，降低低级协调的复杂性。

**关键创新**：HoMeR的主要创新在于其混合动作模式的设计，使得系统能够在绝对姿态预测和相对姿态预测之间切换，从而有效应对不同的操控需求。这一设计与传统方法相比，显著提升了在复杂环境中的适应性和灵活性。

**关键设计**：在参数设置上，HoMeR使用了特定的损失函数来平衡长距离和精细运动的学习，同时采用了深度学习网络结构来处理多模态输入，确保系统能够在多样化的场景中进行有效的泛化。

## 📊 实验亮点

HoMeR在三项模拟和三项真实家庭任务中取得了79.17%的成功率，使用仅20次演示即可实现这一结果，平均超越其他基线方法29.17个百分点。这一显著提升展示了HoMeR在复杂任务中的有效性和高效性。

## 🎯 应用场景

HoMeR框架在家庭环境中的应用潜力巨大，能够用于智能家居中的自动化任务，如物品搬运、清洁和整理等。其高效的学习能力和适应性使其在未来的服务机器人和家庭助手中具有广泛的应用前景，能够提升人们的生活质量。

## 📄 摘要（原文）

> We introduce HoMeR, an imitation learning framework for mobile manipulation that combines whole-body control with hybrid action modes that handle both long-range and fine-grained motion, enabling effective performance on realistic in-the-wild tasks. At its core is a fast, kinematics-based whole-body controller that maps desired end-effector poses to coordinated motion across the mobile base and arm. Within this reduced end-effector action space, HoMeR learns to switch between absolute pose predictions for long-range movement and relative pose predictions for fine-grained manipulation, offloading low-level coordination to the controller and focusing learning on task-level decisions. We deploy HoMeR on a holonomic mobile manipulator with a 7-DoF arm in a real home. We compare HoMeR to baselines without hybrid actions or whole-body control across 3 simulated and 3 real household tasks such as opening cabinets, sweeping trash, and rearranging pillows. Across tasks, HoMeR achieves an overall success rate of 79.17% using just 20 demonstrations per task, outperforming the next best baseline by 29.17 on average. HoMeR is also compatible with vision-language models and can leverage their internet-scale priors to better generalize to novel object appearances, layouts, and cluttered scenes. In summary, HoMeR moves beyond tabletop settings and demonstrates a scalable path toward sample-efficient, generalizable manipulation in everyday indoor spaces. Code, videos, and supplementary material are available at: http://homer-manip.github.io


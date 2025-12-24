---
layout: default
title: "VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation"
---

# VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20322" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20322v2</a>
  <a href="https://arxiv.org/pdf/2509.20322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20322v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20322v2', 'VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaofeng Yin, Yanjie Ze, Hong-Xing Yu, C. Karen Liu, Jiajun Wu

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-09-24 (更新: 2025-11-13)

**备注**: Website: https://visualmimic.github.io

---

## 💡 一句话要点

**VisualMimic：基于运动跟踪和生成实现视觉人型机器人Loco-Manipulation**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人型机器人` `Loco-manipulation` `视觉控制` `运动跟踪` `Sim-to-real` `强化学习` `关键点检测`

## 📋 核心要点

1. 现有的人形机器人loco-manipulation方法依赖外部动捕系统或泛化能力不足，难以在非结构化环境中有效工作。
2. VisualMimic通过结合任务无关的低级关键点跟踪器和任务特定的高级策略，实现了视觉和全身控制的统一。
3. 该方法实现了模拟到真实的零样本迁移，并在多种loco-manipulation任务和户外环境中表现出良好的泛化能力。

## 📝 摘要（中文）

本文提出VisualMimic，一个视觉sim-to-real框架，用于统一以自我为中心的视觉感知和人型机器人的全身控制。现有方法依赖外部运动捕捉系统或无法泛化到不同任务。VisualMimic结合了一个任务无关的低级关键点跟踪器（通过teacher-student方案从人类运动数据中训练）和一个任务特定的高级策略，该策略从视觉和本体感觉输入生成关键点命令。为了确保训练的稳定性，我们将噪声注入到低级策略中，并使用人类运动统计数据来裁剪高级动作。VisualMimic实现了在模拟环境中训练的视觉运动策略到真实人型机器人的零样本迁移，从而完成了一系列loco-manipulation任务，例如箱子搬运、推箱子、足球运球和踢球。除了受控的实验室环境外，我们的策略还可以稳健地泛化到户外环境。

## 🔬 方法详解

**问题定义**：现有的人形机器人loco-manipulation方法主要面临两个痛点：一是依赖外部运动捕捉系统，限制了其在真实环境中的应用；二是难以泛化到不同的任务，需要针对每个任务进行单独训练。这使得人形机器人在非结构化环境中的应用受到限制。

**核心思路**：VisualMimic的核心思路是将loco-manipulation任务分解为两个层次：低级的关键点跟踪和高级的策略控制。低级关键点跟踪器负责从视觉输入中提取人体关键点信息，并将其转化为机器人可执行的动作。高级策略则根据视觉和本体感觉输入，生成关键点命令，指导低级跟踪器完成任务。这种分层结构使得系统可以更好地解耦感知和控制，提高泛化能力。

**技术框架**：VisualMimic的整体框架包括三个主要模块：1) 低级关键点跟踪器：使用teacher-student学习方案，从人类运动数据中训练得到，负责将视觉输入转化为关键点动作；2) 高级策略：根据视觉和本体感觉输入，生成关键点命令，指导低级跟踪器完成任务；3) 模拟环境：用于训练高级策略，并通过噪声注入和动作裁剪等技术，提高sim-to-real的迁移能力。

**关键创新**：VisualMimic的关键创新在于其分层控制结构和sim-to-real迁移策略。分层控制结构将loco-manipulation任务分解为低级关键点跟踪和高级策略控制，降低了任务的复杂性，提高了泛化能力。sim-to-real迁移策略通过噪声注入和动作裁剪等技术，减小了模拟环境和真实环境之间的差异，实现了零样本迁移。

**关键设计**：低级关键点跟踪器使用Transformer网络结构，以提高跟踪精度。高级策略使用强化学习算法进行训练，奖励函数的设计考虑了任务目标和运动的自然性。为了提高训练的稳定性，论文还采用了噪声注入和动作裁剪等技术。噪声注入通过在低级策略中添加随机噪声，增加了策略的鲁棒性。动作裁剪则通过限制高级动作的范围，避免了不自然的运动。

## 📊 实验亮点

VisualMimic实现了在模拟环境中训练的视觉运动策略到真实人型机器人的零样本迁移，并在多种loco-manipulation任务（如箱子搬运、推箱子、足球运球和踢球）和户外环境中表现出良好的泛化能力。与现有方法相比，该方法无需外部运动捕捉系统，且能够更好地适应非结构化环境。

## 🎯 应用场景

VisualMimic在人形机器人领域具有广泛的应用前景，例如在物流、仓储、家庭服务等场景中，可以用于完成物品搬运、环境清洁等任务。该研究的实际价值在于降低了人形机器人的开发和部署成本，使其能够更好地适应真实环境。未来，该技术有望应用于更复杂的任务，例如灾难救援、医疗辅助等。

## 📄 摘要（原文）

> Humanoid loco-manipulation in unstructured environments demands tight integration of egocentric perception and whole-body control. However, existing approaches either depend on external motion capture systems or fail to generalize across diverse tasks. We introduce VisualMimic, a visual sim-to-real framework that unifies egocentric vision with hierarchical whole-body control for humanoid robots. VisualMimic combines a task-agnostic low-level keypoint tracker -- trained from human motion data via a teacher-student scheme -- with a task-specific high-level policy that generates keypoint commands from visual and proprioceptive input. To ensure stable training, we inject noise into the low-level policy and clip high-level actions using human motion statistics. VisualMimic enables zero-shot transfer of visuomotor policies trained in simulation to real humanoid robots, accomplishing a wide range of loco-manipulation tasks such as box lifting, pushing, football dribbling, and kicking. Beyond controlled laboratory settings, our policies also generalize robustly to outdoor environments. Videos are available at: https://visualmimic.github.io .


---
layout: default
title: RoboChallenge: Large-scale Real-robot Evaluation of Embodied Policies
---

# RoboChallenge: Large-scale Real-robot Evaluation of Embodied Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17950" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17950v1</a>
  <a href="https://arxiv.org/pdf/2510.17950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17950v1', 'RoboChallenge: Large-scale Real-robot Evaluation of Embodied Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Adina Yakefu, Bin Xie, Chongyang Xu, Enwen Zhang, Erjin Zhou, Fan Jia, Haitao Yang, Haoqiang Fan, Haowei Zhang, Hongyang Peng, Jing Tan, Junwen Huang, Kai Liu, Kaixin Liu, Kefan Gu, Qinglun Zhang, Ruitao Zhang, Saike Huang, Shen Cheng, Shuaicheng Liu, Tiancai Wang, Tiezhen Wang, Wei Sun, Wenbin Tang, Yajun Wei, Yang Chen, Youqiang Gui, Yucheng Zhao, Yunchao Ma, Yunfei Wei, Yunhuan Yang, Yutong Guo, Ze Chen, Zhengyuan Du, Ziheng Zhang, Ziming Liu, Ziwei Yan

**分类**: cs.RO

**发布日期**: 2025-10-20

**备注**: Authors are listed in alphabetical order. The official website is located at https://robochallenge.ai

---

## 💡 一句话要点

**RoboChallenge：大规模真实机器人环境下的具身策略评估系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人控制` `具身智能` `真实机器人` `在线评估` `大规模评估`

## 📋 核心要点

1. 现有机器人控制算法，尤其是基于学习的算法，缺乏大规模、可重复的真实机器人环境评估。
2. 论文提出了RoboChallenge，一个在线评估系统，旨在提供可扩展、可重复的真实机器人控制算法评估平台。
3. 通过RoboChallenge，作者对当前最先进的VLA模型进行了初步的基准测试，为后续研究提供了参考。

## 📝 摘要（中文）

在真实机器人上进行测试对于机器人控制算法至关重要。特别是在基于学习的算法，尤其是VLA模型（未知）的背景下，对大规模评估的需求，即在大量任务上测试大量模型，变得越来越迫切。然而，正确地做到这一点非常重要，尤其是在考虑到可扩展性和可重复性的情况下。本报告描述了我们构建RoboChallenge的方法，这是一个用于测试机器人控制算法的在线评估系统，以及我们使用初始基准Table30对最近最先进的VLA模型进行的调查。

## 🔬 方法详解

**问题定义**：目前，基于学习的机器人控制算法，特别是VLA模型，需要大规模的真实机器人环境评估来验证其性能。然而，构建一个可扩展且可重复的真实机器人评估系统是一项具有挑战性的任务，现有的评估方法难以满足大规模评估的需求。

**核心思路**：RoboChallenge的核心思路是构建一个在线评估系统，该系统能够支持大规模的机器人控制算法评估，并保证评估结果的可重复性。通过提供标准化的任务、评估指标和硬件平台，研究人员可以方便地在真实机器人上测试和比较不同的算法。

**技术框架**：RoboChallenge的整体架构包含以下几个主要模块：任务定义模块、模型部署模块、机器人控制模块、数据采集模块和评估模块。任务定义模块负责定义各种机器人控制任务，例如物体抓取、导航等。模型部署模块负责将待评估的机器人控制算法部署到机器人上。机器人控制模块负责控制机器人的运动。数据采集模块负责采集机器人在执行任务过程中的数据。评估模块负责根据采集到的数据计算评估指标，例如任务完成率、执行时间等。

**关键创新**：RoboChallenge的关键创新在于其可扩展性和可重复性。通过采用模块化的设计，RoboChallenge可以方便地扩展到更多的任务和机器人平台。通过提供标准化的评估流程和数据采集方法，RoboChallenge可以保证评估结果的可重复性。

**关键设计**：RoboChallenge的关键设计包括：1) 标准化的任务定义，使用统一的描述语言来定义机器人控制任务；2) 模块化的软件架构，方便扩展和维护；3) 自动化的评估流程，减少人工干预；4) 详细的数据记录，方便分析和调试。

## 📊 实验亮点

论文使用RoboChallenge对当前最先进的VLA模型进行了初步的基准测试，结果表明，这些模型在Table30基准上表现出一定的性能，但也存在一些局限性。这些结果为后续研究提供了参考，并指出了未来研究的方向。具体的性能数据和对比基线在论文中进行了详细的描述（未知）。

## 🎯 应用场景

RoboChallenge可用于评估各种机器人控制算法，例如强化学习、模仿学习和运动规划算法。该平台可以帮助研究人员快速验证其算法在真实机器人上的性能，并促进机器人控制领域的发展。此外，RoboChallenge还可以用于机器人教育和培训，帮助学生和工程师学习和掌握机器人控制技术。

## 📄 摘要（原文）

> Testing on real machines is indispensable for robotic control algorithms. In the context of learning-based algorithms, especially VLA models, demand for large-scale evaluation, i.e. testing a large number of models on a large number of tasks, is becoming increasingly urgent. However, doing this right is highly non-trivial, especially when scalability and reproducibility is taken into account. In this report, we describe our methodology for constructing RoboChallenge, an online evaluation system to test robotic control algorithms, and our survey of recent state-of-the-art VLA models using our initial benchmark Table30.


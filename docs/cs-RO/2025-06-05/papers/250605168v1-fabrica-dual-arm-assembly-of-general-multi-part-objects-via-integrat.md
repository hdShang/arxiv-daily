---
layout: default
title: "Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning"
---

# Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05168" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05168v1</a>
  <a href="https://arxiv.org/pdf/2506.05168.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05168v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05168v1', 'Fabrica: Dual-Arm Assembly of General Multi-Part Objects via Integrated Planning and Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunsheng Tian, Joshua Jacob, Yijiang Huang, Jialiang Zhao, Edward Gu, Pingchuan Ma, Annan Zhang, Farhad Javid, Branden Romero, Sachin Chitta, Shinjiro Sueda, Hui Li, Wojciech Matusik

**分类**: cs.RO

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出Fabrica以解决多部件物体的双臂组装问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `双臂机器人` `多部件组装` `强化学习` `全局规划` `局部控制` `自动化技术` `智能制造`

## 📋 核心要点

1. 现有的机器人组装方法在处理复杂几何体和长时间操作时面临效率低下和稳定性差的问题。
2. Fabrica通过集成全局规划与局部控制，采用层次化的规划策略和强化学习框架，提升了组装的效率和成功率。
3. 实验结果显示，Fabrica在多部件组装任务中实现了80%的成功步骤，且无需领域知识或人类示范。

## 📝 摘要（中文）

多部件组装对机器人在复杂几何体上执行长时间、接触丰富的操作提出了重大挑战。本文提出了Fabrica，一个双臂机器人系统，能够实现多部件物体的自主组装。通过开发优先级、顺序、抓取和运动规划的层次结构，结合自动夹具生成，Fabrica实现了对任何双臂机器人的多步骤组装规划。为了应对接触丰富的组装步骤，提出了一种轻量级的强化学习框架，训练能够跨物体几何体、组装方向和抓取姿势的通用策略。这些策略在真实世界中实现了零样本迁移，成功率达到80%。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在多部件组装中面临的长时间、接触丰富的操作挑战。现有方法在处理复杂几何体时效率低下，且缺乏通用性。

**核心思路**：Fabrica通过集成全局规划与局部控制，采用层次化的规划策略和轻量级的强化学习框架，来实现对多部件物体的自主组装。这样的设计使得系统能够在复杂环境中高效执行组装任务。

**技术框架**：Fabrica的整体架构包括多个模块：首先是优先级和顺序规划，其次是抓取和运动规划，最后是基于强化学习的策略训练。每个模块都经过优化，以确保高效的全局规划和稳定的局部控制。

**关键创新**：Fabrica的主要创新在于其能够实现零样本迁移的通用策略，这使得机器人能够在真实世界中有效执行多部件组装，而无需依赖领域知识或人类示范。

**关键设计**：在设计中，采用了层次化的规划结构，结合自动夹具生成技术，确保了多步骤组装的可行性。同时，强化学习框架通过引导策略训练，提升了对不同物体几何体和抓取姿势的适应性。

## 📊 实验亮点

Fabrica在多部件组装任务中实现了80%的成功步骤，展示了其在真实世界中的有效性。与传统方法相比，该系统在组装效率和成功率上有显著提升，标志着机器人自主组装技术的一个重要进步。

## 🎯 应用场景

Fabrica的研究成果在工业自动化、智能制造和日常生活中的机器人助手等领域具有广泛的应用潜力。通过提高机器人在复杂组装任务中的自主性和效率，Fabrica能够显著降低人工干预的需求，提升生产效率和灵活性。

## 📄 摘要（原文）

> Multi-part assembly poses significant challenges for robots to execute long-horizon, contact-rich manipulation with generalization across complex geometries. We present Fabrica, a dual-arm robotic system capable of end-to-end planning and control for autonomous assembly of general multi-part objects. For planning over long horizons, we develop hierarchies of precedence, sequence, grasp, and motion planning with automated fixture generation, enabling general multi-step assembly on any dual-arm robots. The planner is made efficient through a parallelizable design and is optimized for downstream control stability. For contact-rich assembly steps, we propose a lightweight reinforcement learning framework that trains generalist policies across object geometries, assembly directions, and grasp poses, guided by equivariance and residual actions obtained from the plan. These policies transfer zero-shot to the real world and achieve 80% successful steps. For systematic evaluation, we propose a benchmark suite of multi-part assemblies resembling industrial and daily objects across diverse categories and geometries. By integrating efficient global planning and robust local control, we showcase the first system to achieve complete and generalizable real-world multi-part assembly without domain knowledge or human demonstrations. Project website: http://fabrica.csail.mit.edu/


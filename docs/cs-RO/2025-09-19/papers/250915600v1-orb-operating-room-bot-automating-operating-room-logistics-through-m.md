---
layout: default
title: "ORB: Operating Room Bot, Automating Operating Room Logistics through Mobile Manipulation"
---

# ORB: Operating Room Bot, Automating Operating Room Logistics through Mobile Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15600" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15600v1</a>
  <a href="https://arxiv.org/pdf/2509.15600.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15600v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15600v1', 'ORB: Operating Room Bot, Automating Operating Room Logistics through Mobile Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinkai Qiu, Yungjun Kim, Gaurav Sethia, Tanmay Agarwal, Siddharth Ghodasara, Zackory Erickson, Jeffrey Ichnowski

**分类**: cs.RO

**发布日期**: 2025-09-19

**备注**: 7 pages, 5 figures, accepted as a regular conference paper in IEEE CASE 2025

---

## 💡 一句话要点

**ORB：提出一种基于移动操作的机器人系统，用于自动化手术室物流。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `手术室机器人` `移动操作` `行为树` `对象识别` `cuRobo`

## 📋 核心要点

1. 现有医院物流机器人主要处理大宗物品运输，无法满足手术室内精细化、无菌环境下的物品级物流需求。
2. ORB通过分层行为树架构整合对象识别、场景理解和GPU加速运动规划，实现手术室物流任务的自动化。
3. 实验结果表明，ORB在手术室供应品检索和补货操作中分别取得了80%和96%的成功率，验证了其可靠性。

## 📝 摘要（中文）

在医院手术室中，高效地向正在进行的手术运送物品至关重要。虽然现有的运送机器人已成功地在房间和楼层之间运输大宗物品，但自动化物品级的手术室物流在感知、效率和保持无菌性方面提出了独特的挑战。本文提出了手术室机器人（ORB），一个用于自动化医院手术室（OR）物流任务的机器人框架。ORB利用鲁棒的分层行为树（BT）架构来整合对象识别、场景理解和GPU加速的运动规划等多种功能。本文的贡献包括：（1）一种模块化软件架构，通过行为树促进鲁棒的移动操作；（2）一种新颖的实时对象识别流程，集成了YOLOv7、Segment Anything Model 2 (SAM2)和Grounded DINO；（3）将cuRobo并行化轨迹优化框架应用于实时、无碰撞的移动操作；（4）经验验证表明，ORB在手术室供应品检索中的成功率为80%，在补货操作中的成功率为96%。这些贡献确立了ORB作为一个可靠且适应性强的自主手术室物流系统。

## 🔬 方法详解

**问题定义**：论文旨在解决手术室环境中物品级物流的自动化问题。现有方法主要依赖人工，效率低且容易出错，同时难以保证无菌环境。现有的移动机器人虽然可以进行物品运输，但缺乏在复杂手术室环境中进行精细操作的能力。

**核心思路**：论文的核心思路是构建一个集成了感知、规划和控制的机器人系统，通过行为树架构协调各个模块，实现自主的物品检索和补货。这种设计旨在提高效率、减少人为错误，并降低感染风险。

**技术框架**：ORB系统的整体架构包括以下几个主要模块：(1) 对象识别模块，用于识别手术室中的物品；(2) 场景理解模块，用于理解手术室环境；(3) 运动规划模块，用于生成无碰撞的机器人运动轨迹；(4) 行为树模块，用于协调各个模块的执行顺序和逻辑。整个流程是，首先通过对象识别和场景理解模块获取环境信息，然后运动规划模块生成轨迹，最后通过行为树控制机器人执行任务。

**关键创新**：论文的关键创新在于以下几个方面：(1) 提出了一种模块化的软件架构，通过行为树实现鲁棒的移动操作；(2) 集成了YOLOv7、SAM2和Grounded DINO，构建了一种新颖的实时对象识别流程；(3) 将cuRobo并行化轨迹优化框架应用于实时、无碰撞的移动操作。与现有方法相比，ORB更加灵活、高效，并且能够更好地适应手术室的复杂环境。

**关键设计**：在对象识别模块中，论文采用了YOLOv7进行初步检测，然后使用SAM2进行分割，最后使用Grounded DINO进行精确定位。在运动规划模块中，论文使用了cuRobo框架，该框架利用GPU加速进行轨迹优化，从而实现实时规划。行为树的设计也至关重要，它需要能够处理各种异常情况，并保证任务的顺利完成。具体的参数设置和网络结构等细节未在摘要中详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，ORB系统在手术室供应品检索任务中取得了80%的成功率，在补货操作中取得了96%的成功率。这些数据表明，ORB系统具有较高的可靠性和实用性，能够有效地完成手术室物流任务。具体的对比基线和提升幅度未在摘要中详细描述，属于未知信息。

## 🎯 应用场景

该研究成果可应用于医院手术室、ICU等对效率和无菌性要求高的场景，实现医疗物资的自动化管理和配送，减少医护人员的工作负担，提高医疗效率，降低院内感染风险。未来，该技术还可扩展到其他需要精细操作的复杂环境，如实验室、工厂等。

## 📄 摘要（原文）

> Efficiently delivering items to an ongoing surgery in a hospital operating room can be a matter of life or death. In modern hospital settings, delivery robots have successfully transported bulk items between rooms and floors. However, automating item-level operating room logistics presents unique challenges in perception, efficiency, and maintaining sterility. We propose the Operating Room Bot (ORB), a robot framework to automate logistics tasks in hospital operating rooms (OR). ORB leverages a robust, hierarchical behavior tree (BT) architecture to integrate diverse functionalities of object recognition, scene interpretation, and GPU-accelerated motion planning. The contributions of this paper include: (1) a modular software architecture facilitating robust mobile manipulation through behavior trees; (2) a novel real-time object recognition pipeline integrating YOLOv7, Segment Anything Model 2 (SAM2), and Grounded DINO; (3) the adaptation of the cuRobo parallelized trajectory optimization framework to real-time, collision-free mobile manipulation; and (4) empirical validation demonstrating an 80% success rate in OR supply retrieval and a 96% success rate in restocking operations. These contributions establish ORB as a reliable and adaptable system for autonomous OR logistics.


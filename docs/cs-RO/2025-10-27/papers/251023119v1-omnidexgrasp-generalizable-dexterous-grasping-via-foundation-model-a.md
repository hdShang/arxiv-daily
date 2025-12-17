---
layout: default
title: OmniDexGrasp: Generalizable Dexterous Grasping via Foundation Model and Force Feedback
---

# OmniDexGrasp: Generalizable Dexterous Grasping via Foundation Model and Force Feedback

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23119" target="_blank" class="toolbar-btn">arXiv: 2510.23119v1</a>
    <a href="https://arxiv.org/pdf/2510.23119.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23119v1" 
            onclick="toggleFavorite(this, '2510.23119v1', 'OmniDexGrasp: Generalizable Dexterous Grasping via Foundation Model and Force Feedback')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yi-Lin Wei, Zhexi Luo, Yuhao Lin, Mu Lin, Zhizhao Liang, Shuoyu Chen, Wei-Shi Zheng

**分类**: cs.RO

**发布日期**: 2025-10-27

**备注**: Project page: https://isee-laboratory.github.io/OmniDexGrasp/

---

## 💡 一句话要点

**OmniDexGrasp：基于Foundation Model和力反馈的通用灵巧抓取框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `灵巧抓取` `Foundation Model` `力反馈` `机器人操作` `通用性` `迁移学习` `自适应控制`

## 📋 核心要点

1. 现有灵巧抓取方法在面对多样化的物体或任务时，由于语义灵巧抓取数据集规模有限，泛化能力不足。
2. OmniDexGrasp框架结合Foundation Model、人类动作迁移策略和力感知自适应抓取，提升了机器人抓取的泛化性和鲁棒性。
3. 实验结果表明，OmniDexGrasp在不同用户指令、抓取任务和灵巧手上均表现出良好的性能，并具备扩展到灵巧操作任务的潜力。

## 📝 摘要（中文）

本文提出OmniDexGrasp，一个通用的灵巧抓取框架，旨在通过结合Foundation Model与迁移和控制策略，实现用户提示、灵巧操作和抓取任务中的全方位能力。OmniDexGrasp集成了三个关键模块：(i) 利用Foundation Model生成支持用户提示和任务全方位能力的人类抓取图像，从而增强泛化性；(ii) 一种人类图像到机器人动作的迁移策略，将人类演示转化为可执行的机器人动作，实现全方位的灵巧操作；(iii) 力感知的自适应抓取策略，确保鲁棒和稳定的抓取执行。在模拟和真实机器人上的实验验证了OmniDexGrasp在各种用户提示、抓取任务和灵巧手上的有效性，进一步的结果表明了其在灵巧操作任务中的可扩展性。

## 🔬 方法详解

**问题定义**：现有灵巧抓取方法难以泛化到各种物体和任务，主要原因是缺乏大规模的语义灵巧抓取数据集。此外，直接利用Foundation Model生成可行的机器人动作具有挑战性，因为抽象的模型知识与物理机器人执行之间存在差距。

**核心思路**：OmniDexGrasp的核心思路是利用Foundation Model的强大泛化能力，结合人类演示学习和力反馈控制，弥合抽象知识与物理执行之间的差距。通过将人类抓取图像转化为机器人动作，并利用力反馈进行自适应调整，实现更鲁棒和通用的灵巧抓取。

**技术框架**：OmniDexGrasp框架包含三个主要模块：1) **Foundation Model模块**：利用Foundation Model生成人类抓取图像，支持多样化的用户提示和任务需求。2) **人类图像到机器人动作迁移模块**：将人类演示图像转化为可执行的机器人动作，实现灵巧操作的迁移。3) **力感知自适应抓取模块**：利用力传感器信息，对抓取动作进行自适应调整，确保抓取的稳定性和鲁棒性。整体流程是从用户指令开始，通过Foundation Model生成抓取图像，然后迁移到机器人动作，最后通过力反馈进行调整和执行。

**关键创新**：OmniDexGrasp的关键创新在于将Foundation Model与机器人灵巧抓取相结合，利用Foundation Model的泛化能力来解决数据集规模有限的问题。此外，该框架还创新性地提出了人类图像到机器人动作的迁移策略，以及力感知的自适应抓取方法，从而提高了抓取的鲁棒性和通用性。

**关键设计**：在人类图像到机器人动作迁移模块中，可能使用了图像匹配、姿态估计等技术，将人类手的姿态映射到机器人手上。力感知自适应抓取模块可能使用了PID控制或强化学习等方法，根据力传感器反馈调整抓取力度和位置。具体的损失函数和网络结构等细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

实验结果表明，OmniDexGrasp在模拟和真实机器人上均表现出良好的性能。该框架能够成功地处理各种用户提示、抓取任务和灵巧手，并且能够扩展到灵巧操作任务。具体的性能数据（例如成功率、抓取时间等）和对比基线（例如传统抓取算法）需要在论文中查找（未知）。

## 🎯 应用场景

OmniDexGrasp具有广泛的应用前景，例如在智能制造中，机器人可以根据人类指令灵活地抓取和操作各种零件。在家庭服务领域，机器人可以帮助人们完成各种家务，如整理物品、烹饪等。此外，该技术还可以应用于医疗康复、灾难救援等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Enabling robots to dexterously grasp and manipulate objects based on human commands is a promising direction in robotics. However, existing approaches are challenging to generalize across diverse objects or tasks due to the limited scale of semantic dexterous grasp datasets. Foundation models offer a new way to enhance generalization, yet directly leveraging them to generate feasible robotic actions remains challenging due to the gap between abstract model knowledge and physical robot execution. To address these challenges, we propose OmniDexGrasp, a generalizable framework that achieves omni-capabilities in user prompting, dexterous embodiment, and grasping tasks by combining foundation models with the transfer and control strategies. OmniDexGrasp integrates three key modules: (i) foundation models are used to enhance generalization by generating human grasp images supporting omni-capability of user prompt and task; (ii) a human-image-to-robot-action transfer strategy converts human demonstrations into executable robot actions, enabling omni dexterous embodiment; (iii) force-aware adaptive grasp strategy ensures robust and stable grasp execution. Experiments in simulation and on real robots validate the effectiveness of OmniDexGrasp on diverse user prompts, grasp task and dexterous hands, and further results show its extensibility to dexterous manipulation tasks.


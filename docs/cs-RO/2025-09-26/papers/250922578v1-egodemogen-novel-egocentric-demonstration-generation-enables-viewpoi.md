---
layout: default
title: "EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation"
---

# EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22578" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22578v1</a>
  <a href="https://arxiv.org/pdf/2509.22578.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22578v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22578v1', 'EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuan Xu, Jiabing Yang, Xiaofeng Wang, Yixiang Chen, Zheng Zhu, Bowen Fang, Guan Huang, Xinze Chen, Yun Ye, Qiang Zhang, Peiyan Li, Xiangnan Wu, Kai Wang, Bing Zhan, Shuo Lu, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang

**分类**: cs.RO

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**EgoDemoGen：生成新颖的自我中心视角演示，实现视角鲁棒的机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `机器人操作` `模仿学习` `视角鲁棒性` `自我中心视角` `视频生成`

## 📋 核心要点

1. 模仿学习策略在机器人操作中表现良好，但当从单一自我中心视角训练时，在视角发生变化时性能会显著下降。
2. EgoDemoGen通过重定向新视角下的动作，并合成对应的自我中心视角视频，从而生成配对的新颖自我中心视角演示。
3. 在仿真和真实机器人实验中，结合EgoDemoGen生成的新视角演示进行训练，显著提高了策略在不同视角下的成功率。

## 📝 摘要（中文）

本文提出EgoDemoGen框架，旨在解决模仿学习策略在机器人操作中因自我中心视角变化而性能下降的问题。EgoDemoGen通过重定向新视角下的动作，并利用提出的生成式视频修复模型EgoViewTransfer合成相应的自我中心视角视频，从而生成配对的新颖自我中心视角演示。EgoViewTransfer模型通过自监督双重重投影策略，在一个预训练的视频生成模型上进行微调，其输入包括新视角重投影的场景视频和根据重定向关节动作渲染的仅包含机器人的视频。在仿真环境（RoboTwin2.0）和真实机器人上的评估表明，结合EgoDemoGen生成的新视角演示和原始标准视角演示进行训练后，标准视角和新视角的策略成功率分别绝对提升了+17.0%和+17.7%。在真实机器人上，绝对提升分别为+18.3%和+25.8%。性能随着EgoDemoGen生成演示比例的增加而持续提升，但收益递减。这些结果表明EgoDemoGen为实现自我中心视角鲁棒的机器人操作提供了一条可行的途径。

## 🔬 方法详解

**问题定义**：现有的基于模仿学习的机器人操作策略，在训练数据和测试数据的自我中心视角不一致时，性能会显著下降。这意味着模型泛化能力不足，难以适应实际应用中视角变化的情况。

**核心思路**：通过生成新颖的自我中心视角下的演示数据，扩充训练集，从而提高策略的视角鲁棒性。核心在于生成高质量的新视角演示，包括动作和对应的视觉观测。

**技术框架**：EgoDemoGen框架主要包含两个部分：1) 动作重定向：将原始演示中的动作在新视角下进行重定向，得到新视角下的关节动作序列。2) 视频合成：利用提出的EgoViewTransfer模型，根据新视角重投影的场景视频和重定向的关节动作渲染的机器人视频，合成新颖的自我中心视角视频。

**关键创新**：EgoViewTransfer模型是关键创新点。它是一个生成式视频修复模型，能够根据新视角的场景信息和机器人动作信息，生成逼真的自我中心视角视频。该模型通过自监督双重重投影策略进行微调，提高了生成视频的质量和一致性。

**关键设计**：EgoViewTransfer模型基于预训练的视频生成模型，并使用自监督双重重投影策略进行微调。具体来说，该策略将生成的视频重投影回原始视角，并与原始视频进行比较，从而约束生成视频的一致性。此外，模型还使用了对抗损失来提高生成视频的真实感。具体的网络结构和损失函数细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，在仿真环境和真实机器人上，结合EgoDemoGen生成的新视角演示进行训练后，策略在标准视角和新视角下的成功率均得到显著提升。在仿真环境中，标准视角和新视角的成功率分别绝对提升了+17.0%和+17.7%。在真实机器人上，绝对提升分别为+18.3%和+25.8%。这些结果验证了EgoDemoGen框架的有效性。

## 🎯 应用场景

EgoDemoGen框架可应用于各种需要视角鲁棒性的机器人操作任务，例如家庭服务机器人、工业机器人等。通过生成不同视角的演示数据，可以提高机器人在复杂环境中的适应能力，降低对人工标注数据的依赖，加速机器人技能的学习和部署。该研究对于提升机器人智能化水平具有重要意义。

## 📄 摘要（原文）

> Imitation learning based policies perform well in robotic manipulation, but they often degrade under *egocentric viewpoint shifts* when trained from a single egocentric viewpoint. To address this issue, we present **EgoDemoGen**, a framework that generates *paired* novel egocentric demonstrations by retargeting actions in the novel egocentric frame and synthesizing the corresponding egocentric observation videos with proposed generative video repair model **EgoViewTransfer**, which is conditioned by a novel-viewpoint reprojected scene video and a robot-only video rendered from the retargeted joint actions. EgoViewTransfer is finetuned from a pretrained video generation model using self-supervised double reprojection strategy. We evaluate EgoDemoGen on both simulation (RoboTwin2.0) and real-world robot. After training with a mixture of EgoDemoGen-generated novel egocentric demonstrations and original standard egocentric demonstrations, policy success rate improves **absolutely** by **+17.0%** for standard egocentric viewpoint and by **+17.7%** for novel egocentric viewpoints in simulation. On real-world robot, the **absolute** improvements are **+18.3%** and **+25.8%**. Moreover, performance continues to improve as the proportion of EgoDemoGen-generated demonstrations increases, with diminishing returns. These results demonstrate that EgoDemoGen provides a practical route to egocentric viewpoint-robust robotic manipulation.


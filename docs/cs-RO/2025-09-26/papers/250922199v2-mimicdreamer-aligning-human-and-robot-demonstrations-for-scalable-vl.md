---
layout: default
title: "MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training"
---

# MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22199" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22199v2</a>
  <a href="https://arxiv.org/pdf/2509.22199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22199v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22199v2', 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyun Li, Ivan Zhang, Runqi Ouyang, Xiaofeng Wang, Zheng Zhu, Zhiqin Yang, Zhentao Zhang, Boyuan Wang, Chaojun Ni, Wenkang Qin, Xinze Chen, Yun Ye, Guan Huang, Zhenbo Song, Xingang Wang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-09-29)

---

## 💡 一句话要点

**MimicDreamer：对齐人类与机器人演示，实现可扩展的VLA模型训练**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人学习` `人类演示` `领域自适应` `视频扩散模型` `逆运动学` `少样本学习`

## 📋 核心要点

1. 现有VLA模型训练依赖昂贵的机器人交互数据，而人类演示视频虽然易得，但存在与机器人视频的领域差异。
2. MimicDreamer框架通过视觉对齐、视角稳定和动作对齐，将人类演示转化为机器人可用的监督信息。
3. 实验表明，仅用合成数据训练的VLA模型即可在真实机器人上实现少样本执行，且性能优于仅用真实数据训练的模型。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型的能力源于多样化的训练数据，但收集具身机器人交互数据成本高昂。相比之下，人类演示视频更易于获取且成本效益更高，并且最近的研究证实了它们在训练VLA模型中的有效性。然而，人类视频和机器人执行的视频之间存在显著的领域差距，包括不稳定的相机视角、人类手部和机械臂之间的视觉差异以及运动动力学的差异。为了弥合这一差距，我们提出了MimicDreamer框架，该框架通过联合对齐视觉、视角和动作，将快速、低成本的人类演示转化为机器人可用的监督信息，从而直接支持策略训练。对于视觉对齐，我们提出了H2R Aligner，这是一种视频扩散模型，通过转移人类操作视频中的运动来生成高保真机器人演示视频。对于视角稳定，我们提出了EgoStabilizer，它通过单应性变换来规范化自我中心视频，并修复由扭曲引起的遮挡和失真。对于动作对齐，我们将人类手部轨迹映射到机器人坐标系，并应用约束逆运动学求解器来生成具有精确姿势跟踪的可行的、低抖动的关节命令。实验表明，仅在我们合成的人类到机器人视频上训练的VLA模型可以在真实机器人上实现少样本执行。此外，与仅在真实机器人数据上训练的模型相比，使用人类数据扩展训练可以显著提高性能；我们的方法在六个代表性的操作任务中平均成功率提高了14.7%。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作（VLA）模型训练中，机器人交互数据获取成本高昂的问题。现有方法依赖于大量的真实机器人数据，限制了VLA模型的泛化能力。虽然人类演示视频易于获取，但与机器人视频存在显著的领域差异，直接使用效果不佳。

**核心思路**：论文的核心思路是将人类演示视频转换为机器人可用的训练数据，从而利用人类数据的可扩展性。通过对齐视觉、视角和动作，弥合人类视频和机器人视频之间的领域差距，使得VLA模型能够从合成数据中学习，并在真实机器人上执行任务。

**技术框架**：MimicDreamer框架包含三个主要模块：H2R Aligner、EgoStabilizer和动作对齐模块。H2R Aligner是一个视频扩散模型，用于将人类操作视频转换为机器人操作视频，实现视觉对齐。EgoStabilizer用于稳定自我中心视角，并修复由视角变换引起的遮挡和失真。动作对齐模块将人类手部轨迹映射到机器人坐标系，并生成可行的机器人关节命令。整体流程是：首先使用H2R Aligner生成机器人视频，然后使用EgoStabilizer稳定视角，最后使用动作对齐模块生成机器人动作指令。

**关键创新**：论文的关键创新在于提出了一个完整的框架，能够将人类演示视频转换为高质量的机器人训练数据。H2R Aligner利用视频扩散模型生成逼真的机器人视频，EgoStabilizer解决了自我中心视角的不稳定性问题，动作对齐模块生成了可行的机器人动作指令。与现有方法相比，该方法能够更有效地利用人类数据，提高VLA模型的泛化能力。

**关键设计**：H2R Aligner使用视频扩散模型，通过学习人类视频和机器人视频之间的映射关系，生成高质量的机器人视频。EgoStabilizer使用单应性变换来稳定视角，并使用图像修复技术来填充遮挡区域。动作对齐模块使用约束逆运动学求解器，生成满足机器人运动学约束的关节命令。损失函数包括视觉相似性损失、视角一致性损失和动作跟踪损失。

## 📊 实验亮点

实验结果表明，仅在MimicDreamer合成数据上训练的VLA模型即可在真实机器人上实现少样本执行。与仅在真实机器人数据上训练的模型相比，使用人类数据扩展训练可以显著提高性能，在六个代表性的操作任务中平均成功率提高了14.7%。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如装配、抓取、放置等。通过利用大量的人类演示视频，可以降低机器人学习的成本，提高机器人的智能化水平。该方法还可以应用于虚拟现实和增强现实等领域，实现人机协作和远程操作。

## 📄 摘要（原文）

> Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.


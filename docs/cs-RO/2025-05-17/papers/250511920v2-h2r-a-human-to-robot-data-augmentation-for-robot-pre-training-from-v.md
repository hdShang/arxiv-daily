---
layout: default
title: "H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos"
---

# H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.11920" class="toolbar-btn" target="_blank">📄 arXiv: 2505.11920v2</a>
  <a href="https://arxiv.org/pdf/2505.11920.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.11920v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.11920v2', 'H2R: A Human-to-Robot Data Augmentation for Robot Pre-training from Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangrun Li, Yaoxu Lyu, Zhuoyang Liu, Chengkai Hou, Jieyu Zhang, Shanghang Zhang

**分类**: cs.RO

**发布日期**: 2025-05-17 (更新: 2025-05-26)

---

## 💡 一句话要点

**提出H2R以解决人机视觉差异问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `数据增强` `机器人学习` `视觉差距` `关键点检测` `动作合成` `自我中心视频` `预训练模型`

## 📋 核心要点

1. 现有方法在机器人学习中存在视觉差距，导致基于人类数据的预训练模型效果不佳。
2. H2R通过检测人类手部关键点和合成机器人动作，生成机器人中心的训练数据，弥合视觉差距。
3. 实验结果表明，H2R在模拟和现实任务中均显著提高了成功率，验证了其有效性。

## 📝 摘要（中文）

大规模视频预训练在机器人学习中已被证明有效。然而，基于人类手部数据预训练的模型在机器人学习中可能表现不佳，因为人类手与不同机器人手之间存在显著的视觉差距。为此，本文提出H2R，一种简单的数据增强技术，通过检测人类手部关键点、在模拟中合成机器人动作，并将渲染的机器人合成到自我中心的视频中，从而在预训练过程中显式地弥合人类与机器人表现之间的视觉差距。我们将H2R应用于增强大规模自我中心人类视频数据集，如Ego4D和SSv2，替换人类手为模拟的机器人手臂，生成以机器人为中心的训练数据。基于此，我们构建并发布了一个覆盖多种机器人表现的100万规模数据集，并通过CLIP基础的图像-文本相似性度量验证增强管道的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人学习中人类手与机器人手之间的视觉差距问题。现有方法在使用人类视频数据进行预训练时，无法有效适应不同机器人的手部表现，导致学习效果不佳。

**核心思路**：H2R的核心思路是通过检测人类手部关键点，合成机器人动作，并将渲染的机器人合成到自我中心的视频中，从而在预训练过程中弥合人类与机器人之间的视觉差距。这样的设计使得生成的数据更符合机器人操作的实际情况。

**技术框架**：H2R的整体架构包括三个主要模块：1) 人类手部关键点检测；2) 机器人动作合成；3) 视频合成与渲染。通过这些模块的协同工作，生成以机器人为中心的训练数据。

**关键创新**：H2R的主要创新在于其数据增强方法，能够有效地将人类视频中的手部动作转化为机器人可用的训练数据。这一方法与传统的直接使用人类数据的方式有本质区别，能够显著提高机器人学习的效果。

**关键设计**：在H2R中，关键设计包括手部关键点的精确检测算法、机器人动作的物理模拟以及视频合成中的渲染技术。这些技术细节确保了生成数据的高质量和真实感，从而提升了模型的学习效果。

## 📊 实验亮点

实验结果显示，H2R在模拟任务中成功率提升5.0%-10.2%，在现实世界任务中提升6.7%-23.3%。这些结果表明，H2R显著改善了机器人策略的泛化能力，验证了其在不同视觉编码器和策略学习方法中的有效性。

## 🎯 应用场景

H2R的研究成果在机器人学习、自动化操作和人机交互等领域具有广泛的应用潜力。通过提供更符合机器人操作需求的训练数据，H2R能够帮助提升机器人在复杂环境中的操作能力，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Large-scale pre-training using videos has proven effective for robot learning. However, the models pre-trained on such data can be suboptimal for robot learning due to the significant visual gap between human hands and those of different robots. To remedy this, we propose H2R, a simple data augmentation technique that detects human hand keypoints, synthesizes robot motions in simulation, and composites rendered robots into egocentric videos. This process explicitly bridges the visual gap between human and robot embodiments during pre-training. We apply H2R to augment large-scale egocentric human video datasets such as Ego4D and SSv2, replacing human hands with simulated robotic arms to generate robot-centric training data. Based on this, we construct and release a family of 1M-scale datasets covering multiple robot embodiments (UR5 with gripper/Leaphand, Franka) and data sources (SSv2, Ego4D). To verify the effectiveness of the augmentation pipeline, we introduce a CLIP-based image-text similarity metric that quantitatively evaluates the semantic fidelity of robot-rendered frames to the original human actions. We validate H2R across three simulation benchmarks: Robomimic, RLBench and PushT and real-world manipulation tasks with a UR5 robot equipped with Gripper and Leaphand end-effectors. H2R consistently improves downstream success rates, yielding gains of 5.0%-10.2% in simulation and 6.7%-23.3% in real-world tasks across various visual encoders and policy learning methods. These results indicate that H2R improves the generalization ability of robotic policies by mitigating the visual discrepancies between human and robot domains.


---
layout: default
title: Learning to Navigate Socially Through Proactive Risk Perception
---

# Learning to Navigate Socially Through Proactive Risk Perception

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07871" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07871v3</a>
  <a href="https://arxiv.org/pdf/2510.07871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07871v3" onclick="toggleFavorite(this, '2510.07871v3', 'Learning to Navigate Socially Through Proactive Risk Perception')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Erjia Xiao, Lingfeng Zhang, Yingbo Tang, Hao Cheng, Renjing Xu, Wenbo Ding, Lei Zhou, Long Chen, Hangjun Ye, Xiaoshuai Hao

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-09 (更新: 2025-11-07)

---

## 💡 一句话要点

**提出基于主动风险感知的社交导航方法，提升动态人群环境下的机器人导航能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `社交导航` `主动风险感知` `机器人导航` `深度学习` `动态环境`

## 📋 核心要点

1. 现有社交导航方法难以准确预测动态环境中潜在的碰撞风险，导致导航安全性不足。
2. 提出主动风险感知模块，学习预测周围人类的碰撞风险，增强智能体的空间感知和避碰能力。
3. 在Social-HM3D基准测试中，该方法显著提升了智能体在动态人群环境下的导航安全性和社交合规性。

## 📝 摘要（中文）

本报告详细描述了我们提交给IROS 2025 RoboSense挑战赛社交导航赛道的方案。该赛道专注于开发基于RGBD的感知和导航系统，使自主智能体能够在动态的人群室内环境中安全、高效且符合社会规范地导航。挑战要求智能体仅使用包括RGB-D观测和里程计在内的板载传感器，从自我中心视角运行，无需访问全局地图或特权信息，同时保持符合社会规范，例如安全距离和避免碰撞。在Falcon模型的基础上，我们引入了一个主动风险感知模块来增强社交导航性能。我们的方法通过碰撞风险理解来增强Falcon，该模块学习预测周围人类的基于距离的碰撞风险评分，这使得智能体能够开发更强大的空间感知和主动避碰行为。在Social-HM3D基准上的评估表明，我们的方法提高了智能体在拥挤的室内场景中与动态人类智能体导航到目标时保持个人空间合规性的能力，在挑战赛的16个参赛队伍中获得第二名。

## 🔬 方法详解

**问题定义**：现有社交导航方法在动态人群环境中，难以准确预测潜在的碰撞风险，导致机器人难以保持安全距离，影响导航效率和社交合规性。尤其是在仅依赖板载传感器和自我中心视角的情况下，风险预测的准确性更具挑战。

**核心思路**：论文的核心思路是通过主动学习预测周围行人的碰撞风险，从而使机器人能够提前规划路径，避免潜在的碰撞。这种主动的风险感知能力能够提升机器人在复杂动态环境中的导航安全性和社交合规性。

**技术框架**：该方法基于Falcon模型，并在此基础上增加了一个主动风险感知模块。整体框架包括：1) RGB-D数据输入；2) Falcon模型进行初步的导航决策；3) 主动风险感知模块预测周围行人的碰撞风险；4) 融合风险信息，调整导航策略，实现更安全的路径规划。

**关键创新**：该方法最重要的创新点在于提出了主动风险感知模块，该模块能够学习预测周围行人的碰撞风险。与传统的基于规则或简单距离阈值的风险评估方法相比，该模块能够更准确地捕捉动态环境中潜在的风险，从而提升导航的安全性。

**关键设计**：主动风险感知模块通过学习预测基于距离的碰撞风险评分来实现风险评估。具体的网络结构和损失函数细节未知，但可以推测可能使用了深度学习模型，并采用回归损失函数来训练风险评分预测器。此外，如何将风险评分有效地融入到Falcon模型的导航决策中也是一个关键设计。

## 📊 实验亮点

该方法在Social-HM3D基准测试中取得了显著的成果，在16支参赛队伍中排名第二，证明了其在动态人群环境中进行社交导航的有效性。实验结果表明，该方法能够有效提升智能体在拥挤室内场景中与动态人类智能体导航到目标时保持个人空间合规性的能力。

## 🎯 应用场景

该研究成果可应用于服务机器人、自动驾驶车辆等领域，尤其是在人群密集的室内环境中，如商场、医院、养老院等。通过提升机器人在动态环境中的导航安全性和社交合规性，可以提高用户体验，降低安全风险，并促进人机协作的效率。

## 📄 摘要（原文）

> In this report, we describe the technical details of our submission to the IROS 2025 RoboSense Challenge Social Navigation Track. This track focuses on developing RGBD-based perception and navigation systems that enable autonomous agents to navigate safely, efficiently, and socially compliantly in dynamic human-populated indoor environments. The challenge requires agents to operate from an egocentric perspective using only onboard sensors including RGB-D observations and odometry, without access to global maps or privileged information, while maintaining social norm compliance such as safe distances and collision avoidance. Building upon the Falcon model, we introduce a Proactive Risk Perception Module to enhance social navigation performance. Our approach augments Falcon with collision risk understanding that learns to predict distance-based collision risk scores for surrounding humans, which enables the agent to develop more robust spatial awareness and proactive collision avoidance behaviors. The evaluation on the Social-HM3D benchmark demonstrates that our method improves the agent's ability to maintain personal space compliance while navigating toward goals in crowded indoor scenes with dynamic human agents, achieving 2nd place among 16 participating teams in the challenge.


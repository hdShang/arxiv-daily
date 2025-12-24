---
layout: default
title: "SocialNav-Map: Dynamic Mapping with Human Trajectory Prediction for Zero-Shot Social Navigation"
---

# SocialNav-Map: Dynamic Mapping with Human Trajectory Prediction for Zero-Shot Social Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12232" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12232v2</a>
  <a href="https://arxiv.org/pdf/2511.12232.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12232v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.12232v2', 'SocialNav-Map: Dynamic Mapping with Human Trajectory Prediction for Zero-Shot Social Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingfeng Zhang, Erjia Xiao, Xiaoshuai Hao, Haoxiang Fu, Zeying Gong, Long Chen, Xiaojun Liang, Renjing Xu, Hangjun Ye, Wenbo Ding

**分类**: cs.RO

**发布日期**: 2025-11-15 (更新: 2025-11-18)

**🔗 代码/项目**: [GITHUB](https://github.com/linglingxiansen/SocialNav-Map)

---

## 💡 一句话要点

**SocialNav-Map：结合动态地图与轨迹预测的零样本社交导航**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `社交导航` `零样本学习` `轨迹预测` `动态地图` `机器人导航`

## 📋 核心要点

1. 现有基于强化学习的社交导航方法需要大量训练，且泛化能力差，难以适应新环境。
2. SocialNav-Map通过结合动态人类轨迹预测和占据栅格地图，实现零样本社交导航。
3. 实验表明，SocialNav-Map无需训练即可显著降低碰撞率，优于现有强化学习方法。

## 📝 摘要（中文）

本文提出了一种名为SocialNav-Map的零样本社交导航框架，旨在解决人群密集动态环境中自主移动机器人的安全导航问题。该框架结合了动态人类轨迹预测和占据栅格地图构建，无需针对特定环境进行训练即可实现安全高效的导航。SocialNav-Map首先将目标位置转换到地图坐标系中，然后创建一个动态占据栅格地图，将预测的人类运动作为动态障碍物纳入其中。该框架采用历史预测和方向预测两种互补方法进行人类轨迹预测。通过将这些预测轨迹整合到占据栅格地图中，机器人能够主动避开与人类的潜在碰撞，同时高效地导航到目的地。在Social-HM3D和Social-MP3D数据集上的大量实验表明，SocialNav-Map显著优于需要2396 GPU小时训练的现有基于强化学习的方法，并且在新的环境中无需任何训练即可将人类碰撞率降低10%以上。

## 🔬 方法详解

**问题定义**：在人群密集的动态环境中，如何使机器人安全、高效地导航到目标位置是一个挑战。现有的基于强化学习的方法需要大量的训练数据，并且在新的环境中泛化能力较差，需要进行额外的微调，这限制了它们在实际场景中的应用。

**核心思路**：SocialNav-Map的核心思路是利用人类轨迹预测来构建动态的占据栅格地图，将预测的人类运动作为动态障碍物，从而使机器人能够提前规划路径，避免碰撞。这种方法避免了对特定环境的训练，实现了零样本的社交导航。

**技术框架**：SocialNav-Map的整体框架包括以下几个主要步骤：1) 将目标位置转换到地图坐标系中；2) 利用历史预测和方向预测两种方法预测人类的未来轨迹；3) 将预测的轨迹整合到占据栅格地图中，生成动态占据栅格地图；4) 利用路径规划算法在动态占据栅格地图上规划出安全、高效的路径。

**关键创新**：SocialNav-Map的关键创新在于将人类轨迹预测与占据栅格地图相结合，构建了动态的导航环境表示。与传统的静态地图相比，动态占据栅格地图能够反映人群的运动趋势，使机器人能够更好地预测潜在的碰撞风险，从而做出更合理的导航决策。此外，该方法实现了零样本学习，无需针对特定环境进行训练。

**关键设计**：在人类轨迹预测方面，SocialNav-Map采用了历史预测和方向预测两种互补的方法。历史预测基于人类过去的运动轨迹来预测未来的位置，而方向预测则基于人类当前的朝向和速度来预测未来的位置。这两种方法可以相互补充，提高轨迹预测的准确性。在动态占据栅格地图的构建方面，SocialNav-Map根据预测轨迹的不确定性，对占据栅格进行加权，从而更好地反映人群的运动风险。

## 📊 实验亮点

SocialNav-Map在Social-HM3D和Social-MP3D数据集上进行了广泛的实验，结果表明，该方法显著优于现有的基于强化学习的方法，后者需要2396 GPU小时的训练。SocialNav-Map在新的环境中无需任何训练即可将人类碰撞率降低10%以上，证明了其优越的泛化能力和实用价值。

## 🎯 应用场景

SocialNav-Map可应用于各种需要与人类进行交互的机器人导航场景，例如商场导览机器人、医院配送机器人、餐厅服务机器人等。该研究成果有助于提升机器人在复杂动态环境中的自主导航能力，降低安全风险，提高服务效率，并为未来人机协作系统的发展奠定基础。

## 📄 摘要（原文）

> Social navigation in densely populated dynamic environments poses a significant challenge for autonomous mobile robots, requiring advanced strategies for safe interaction. Existing reinforcement learning (RL)-based methods require over 2000+ hours of extensive training and often struggle to generalize to unfamiliar environments without additional fine-tuning, limiting their practical application in real-world scenarios. To address these limitations, we propose SocialNav-Map, a novel zero-shot social navigation framework that combines dynamic human trajectory prediction with occupancy mapping, enabling safe and efficient navigation without the need for environment-specific training. Specifically, SocialNav-Map first transforms the task goal position into the constructed map coordinate system. Subsequently, it creates a dynamic occupancy map that incorporates predicted human movements as dynamic obstacles. The framework employs two complementary methods for human trajectory prediction: history prediction and orientation prediction. By integrating these predicted trajectories into the occupancy map, the robot can proactively avoid potential collisions with humans while efficiently navigating to its destination. Extensive experiments on the Social-HM3D and Social-MP3D datasets demonstrate that SocialNav-Map significantly outperforms state-of-the-art (SOTA) RL-based methods, which require 2,396 GPU hours of training. Notably, it reduces human collision rates by over 10% without necessitating any training in novel environments. By eliminating the need for environment-specific training, SocialNav-Map achieves superior navigation performance, paving the way for the deployment of social navigation systems in real-world environments characterized by diverse human behaviors. The code is available at: https://github.com/linglingxiansen/SocialNav-Map.


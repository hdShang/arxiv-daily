---
layout: default
title: "TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning"
---

# TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.11839" class="toolbar-btn" target="_blank">📄 arXiv: 2509.11839v2</a>
  <a href="https://arxiv.org/pdf/2509.11839.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.11839v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.11839v2', 'TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Liu, Pengxiang Ding, Qihang Zhou, Yuxuan Wu, Da Huang, Zimian Peng, Wei Xiao, Weinan Zhang, Lixin Yang, Cewu Lu, Donglin Wang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-15 (更新: 2025-09-17)

**🔗 代码/项目**: [PROJECT_PAGE](https://jiachengliu3.github.io/TrajBooster/)

---

## 💡 一句话要点

**TrajBooster：通过轨迹中心学习提升人形机器人全身操作能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人形机器人` `全身控制` `视觉-语言-动作模型` `跨形态学习` `轨迹优化` `机器人操作` `模仿学习` `强化学习`

## 📋 核心要点

1. 现有VLA模型难以在新机器人上快速对齐动作空间，尤其是在高质量演示数据稀缺的双足人形机器人上。
2. TrajBooster利用轮式人形机器人的末端执行器轨迹作为桥梁，将知识迁移到双足人形机器人上，实现跨形态学习。
3. 通过少量目标机器人数据微调，TrajBooster在Unitree G1上实现了复杂的全身操作，提升了鲁棒性和泛化能力。

## 📝 摘要（中文）

本文提出TrajBooster，一个跨形态框架，利用丰富的轮式人形机器人数据来提升双足VLA（视觉-语言-动作）模型的能力。核心思想是使用末端执行器轨迹作为形态无关的接口。TrajBooster首先从真实世界的轮式人形机器人中提取6D双臂末端执行器轨迹，然后在模拟环境中，通过启发式增强的协调在线DAgger训练的全身控制器，将这些轨迹重定向到Unitree G1机器人，从而将低维轨迹参考转化为可行的高维全身动作。最后，构建异构三元组，将源视觉/语言与目标人形机器人兼容的动作相结合，对VLA模型进行后预训练，并在目标人形机器人领域进行仅10分钟的遥操作数据收集。在Unitree G1上的部署结果表明，该策略能够完成超越桌面级别的家庭任务，实现蹲伏、跨高度操作以及协调的全身运动，显著提高了鲁棒性和泛化能力。结果表明，TrajBooster能够有效地利用现有的轮式人形机器人数据来增强双足人形机器人的VLA性能，减少对昂贵的同形态数据的依赖，同时增强对动作空间的理解和零样本技能迁移能力。

## 🔬 方法详解

**问题定义**：论文旨在解决双足人形机器人视觉-语言-动作（VLA）模型训练中，由于高质量同形态数据稀缺，导致模型难以快速适应新机器人动作空间的问题。现有方法依赖大量同形态数据，成本高昂，且难以实现零样本技能迁移。

**核心思路**：论文的核心思路是利用轮式人形机器人丰富的动作数据，通过末端执行器轨迹作为形态无关的中间表示，将知识迁移到双足人形机器人上。这种方法解耦了形态差异，使得模型能够学习通用的操作技能，并减少对目标机器人数据的依赖。

**技术框架**：TrajBooster框架包含三个主要阶段：(1) **轨迹提取**：从轮式人形机器人数据中提取6D双臂末端执行器轨迹。(2) **轨迹重定向**：在模拟环境中，使用全身控制器将提取的轨迹重定向到Unitree G1双足人形机器人。该控制器通过启发式增强的协调在线DAgger训练，能够将低维轨迹参考转化为可行的高维全身动作。(3) **VLA模型训练**：构建异构三元组，将源视觉/语言信息与目标人形机器人兼容的动作相结合，对VLA模型进行后预训练，并使用少量目标机器人遥操作数据进行微调。

**关键创新**：最重要的技术创新点在于使用末端执行器轨迹作为跨形态学习的桥梁。与直接迁移动作或策略不同，轨迹具有形态无关性，能够更好地泛化到不同结构的机器人上。此外，启发式增强的协调在线DAgger训练方法能够有效地生成高质量的全身控制策略，弥补了双足人形机器人数据稀缺的问题。

**关键设计**：在轨迹重定向阶段，全身控制器的训练采用了启发式增强的协调在线DAgger算法。具体来说，首先使用启发式方法初始化控制器，然后通过在线DAgger迭代优化。协调机制保证了全身运动的协调性，避免了关节冲突和不自然的姿态。在VLA模型训练阶段，异构三元组的设计使得模型能够同时学习视觉、语言和动作之间的关系，并适应目标机器人的动作空间。

## 📊 实验亮点

TrajBooster在Unitree G1双足人形机器人上进行了实验验证，结果表明，该方法能够完成超越桌面级别的家庭任务，例如蹲伏、跨高度操作以及协调的全身运动。与基线方法相比，TrajBooster显著提高了鲁棒性和泛化能力，并且仅需10分钟的目标机器人遥操作数据即可实现良好的性能。

## 🎯 应用场景

该研究成果可应用于家庭服务机器人、工业自动化、医疗康复等领域。通过跨形态学习，可以降低机器人开发的成本和周期，提高机器人的泛化能力和智能化水平。未来，该技术有望实现更复杂、更精细的机器人操作任务，例如在复杂环境中进行物品抓取、装配和维护等。

## 📄 摘要（原文）

> Recent Vision-Language-Action models show potential to generalize across embodiments but struggle to quickly align with a new robot's action space when high-quality demonstrations are scarce, especially for bipedal humanoids. We present TrajBooster, a cross-embodiment framework that leverages abundant wheeled-humanoid data to boost bipedal VLA. Our key idea is to use end-effector trajectories as a morphology-agnostic interface. TrajBooster (i) extracts 6D dual-arm end-effector trajectories from real-world wheeled humanoids, (ii) retargets them in simulation to Unitree G1 with a whole-body controller trained via a heuristic-enhanced harmonized online DAgger to lift low-dimensional trajectory references into feasible high-dimensional whole-body actions, and (iii) forms heterogeneous triplets that couple source vision/language with target humanoid-compatible actions to post-pre-train a VLA, followed by only 10 minutes of teleoperation data collection on the target humanoid domain. Deployed on Unitree G1, our policy achieves beyond-tabletop household tasks, enabling squatting, cross-height manipulation, and coordinated whole-body motion with markedly improved robustness and generalization. Results show that TrajBooster allows existing wheeled-humanoid data to efficiently strengthen bipedal humanoid VLA performance, reducing reliance on costly same-embodiment data while enhancing action space understanding and zero-shot skill transfer capabilities. For more details, For more details, please refer to our \href{https://jiachengliu3.github.io/TrajBooster/}.


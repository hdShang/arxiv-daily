---
layout: default
title: OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
---

# OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13100" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13100v1</a>
  <a href="https://arxiv.org/pdf/2512.13100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13100v1" onclick="toggleFavorite(this, '2512.13100v1', 'OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanhua Ji, Harsha Polavaram, Lawrence Yunliang Chen, Sandeep Bajamahal, Zehan Ma, Simeon Adebola, Chenfeng Xu, Ken Goldberg

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-15

**🔗 代码/项目**: [PROJECT_PAGE](https://OXE-AugE.github.io/)

---

## 💡 一句话要点

**提出OXE-AugE数据集，通过机器人增强扩展OXE，提升跨具身策略学习能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `机器人学习` `跨具身学习` `数据增强` `机器人数据集` `通用机器人策略` `机器人形态` `OXE数据集` `AugE-Toolkit`

## 📋 核心要点

1. 现有机器人数据集（如OXE）存在数据不平衡问题，导致训练的策略容易过拟合到特定的机器人-场景组合。
2. 论文提出AugE-Toolkit和OXE-AugE数据集，通过机器人形态增强来扩展OXE，增加数据多样性，促进跨具身策略学习。
3. 实验表明，在OXE-AugE上微调通用策略，可以显著提高在未见过的机器人-夹爪组合上的成功率，提升幅度达24-45%。

## 📝 摘要（中文）

为了训练能够控制各种机器人形态（机械臂和夹爪组合）的通用机器人策略，需要大规模且多样化的数据集。由于为每个新的硬件平台重新收集演示数据和重新训练成本过高，本文提出可以通过增强现有机器人数据来实现迁移和泛化。Open X-Embodiment (OXE)数据集汇集了来自60多个机器人数据集的演示数据，已被广泛用作训练通用策略的基础。然而，它高度不平衡：前四种机器人类型占据了超过85%的真实数据，这可能导致对机器人-场景组合的过拟合。本文提出了AugE-Toolkit，一个可扩展的机器人增强流水线，以及OXE-AugE，一个高质量的开源数据集，通过9种不同的机器人形态增强了OXE。OXE-AugE提供了超过440万条轨迹，是原始OXE的三倍多。本文系统地研究了扩展机器人增强如何影响跨具身学习。结果表明，使用不同的机械臂和夹爪增强数据集不仅提高了增强机器人的策略性能，而且提高了未见过的机器人甚至原始机器人在分布偏移下的策略性能。在物理实验中，证明了OpenVLA和$π_0$等最先进的通用策略可以通过在OXE-AugE上进行微调来受益，在四个真实世界的操纵任务中，先前未见过的机器人-夹爪组合的成功率提高了24-45%。

## 🔬 方法详解

**问题定义**：现有的大规模机器人数据集，例如OXE，存在严重的数据不平衡问题。少数几种机器人占据了绝大部分数据，导致训练出的策略容易过拟合到这些常见的机器人类型和场景，泛化能力不足。为新的机器人平台重新收集数据和训练模型的成本很高，因此需要一种方法来利用现有数据，并使其能够泛化到不同的机器人形态上。

**核心思路**：论文的核心思路是通过机器人形态增强来扩展现有的机器人数据集。具体来说，就是将现有的机器人轨迹数据，通过替换机器人手臂和夹爪的方式，生成新的轨迹数据。这样可以增加数据集的多样性，减少过拟合的风险，提高策略的泛化能力。这种方法避免了为每种新的机器人重新收集数据的昂贵成本。

**技术框架**：论文提出了AugE-Toolkit，这是一个可扩展的机器人增强流水线。该流水线包含以下几个主要步骤：1) 从原始OXE数据集中提取轨迹数据；2) 使用AugE-Toolkit对轨迹数据进行机器人形态增强，生成新的轨迹数据；3) 将增强后的轨迹数据与原始OXE数据集合并，形成OXE-AugE数据集。该数据集随后被用于训练和微调通用机器人策略。

**关键创新**：论文的关键创新在于提出了一个可扩展的机器人增强流水线，可以有效地增加机器人数据集的多样性。与以往的数据增强方法不同，该方法专注于改变机器人的形态，而不是改变场景或任务。这种方法更适合于解决跨具身策略学习的问题，因为它可以使策略更好地适应不同的机器人硬件。

**关键设计**：AugE-Toolkit的关键设计包括：1) 能够支持多种不同的机器人手臂和夹爪；2) 能够自动生成合理的机器人运动轨迹，避免碰撞和不自然的运动；3) 能够高效地处理大规模的机器人数据集。论文中没有详细说明具体的参数设置、损失函数或网络结构，这些细节可能取决于具体的策略学习算法。

## 📊 实验亮点

实验结果表明，在OXE-AugE数据集上微调的通用策略，在未见过的机器人-夹爪组合上的成功率显著提高。具体来说，OpenVLA和$π_0$等最先进的通用策略，在四个真实世界的操纵任务中，成功率提高了24-45%。这表明，通过机器人增强来扩展数据集，可以有效地提高跨具身策略学习的性能。

## 🎯 应用场景

该研究成果可应用于各种机器人自动化场景，特别是在需要快速部署新机器人或机器人配置的场景中。例如，在柔性制造系统中，可以利用OXE-AugE数据集训练的通用策略，快速适应不同的机器人手臂和夹爪组合，从而提高生产效率和灵活性。此外，该方法还可以用于机器人教育和研究，为学生和研究人员提供一个大规模、多样化的机器人数据集，促进机器人学习算法的开发和改进。

## 📄 摘要（原文）

> Large and diverse datasets are needed for training generalist robot policies that have potential to control a variety of robot embodiments -- robot arm and gripper combinations -- across diverse tasks and environments. As re-collecting demonstrations and retraining for each new hardware platform are prohibitively costly, we show that existing robot data can be augmented for transfer and generalization. The Open X-Embodiment (OXE) dataset, which aggregates demonstrations from over 60 robot datasets, has been widely used as the foundation for training generalist policies. However, it is highly imbalanced: the top four robot types account for over 85\% of its real data, which risks overfitting to robot-scene combinations. We present AugE-Toolkit, a scalable robot augmentation pipeline, and OXE-AugE, a high-quality open-source dataset that augments OXE with 9 different robot embodiments. OXE-AugE provides over 4.4 million trajectories, more than triple the size of the original OXE. We conduct a systematic study of how scaling robot augmentation impacts cross-embodiment learning. Results suggest that augmenting datasets with diverse arms and grippers improves policy performance not only on the augmented robots, but also on unseen robots and even the original robots under distribution shifts. In physical experiments, we demonstrate that state-of-the-art generalist policies such as OpenVLA and $π_0$ benefit from fine-tuning on OXE-AugE, improving success rates by 24-45% on previously unseen robot-gripper combinations across four real-world manipulation tasks. Project website: https://OXE-AugE.github.io/.


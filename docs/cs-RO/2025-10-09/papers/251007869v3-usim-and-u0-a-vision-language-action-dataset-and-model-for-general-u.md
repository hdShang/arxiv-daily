---
layout: default
title: USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots
---

# USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07869" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07869v3</a>
  <a href="https://arxiv.org/pdf/2510.07869.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07869v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.07869v3', 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junwen Gu, Zhiheng Wu, Pengxuan Si, Shuang Qiu, Yukai Feng, Luoyang Sun, Laien Luo, Lianyi Yu, Jian Wang, Zhengxing Wu

**分类**: cs.RO

**发布日期**: 2025-10-09 (更新: 2025-10-15)

**备注**: Project Page: https://vincentgu2000.github.io/u0project/

---

## 💡 一句话要点

**提出USIM和U0以解决水下机器人多任务智能问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水下机器人` `多任务学习` `视觉-语言-动作` `数据集构建` `多模态融合` `卷积注意力机制` `自主智能` `环境监测`

## 📋 核心要点

1. 水下机器人在执行多任务时面临数据稀缺和环境复杂性等挑战，现有方法难以实现高效的自主操作。
2. 本文提出USIM数据集和U0模型，通过多模态融合和感知聚焦增强模块，提升水下机器人在多任务中的智能表现。
3. 实验结果显示，U0在多项任务中成功率达到80%，在移动操作任务中目标距离减少21.2%，验证了其有效性。

## 📝 摘要（中文）

水下环境对机器人操作提出了独特挑战，包括复杂的水动力学、有限的可见性和受限的通信。尽管数据驱动的方法在陆地机器人中取得了进展，但在水下智能的多任务自主执行方面仍然面临困难。为了解决这些问题，本文提出了USIM，一个基于仿真的多任务视觉-语言-动作（VLA）数据集，包含来自1852条轨迹的561K帧数据，涵盖20个任务和9种不同场景。基于此数据集，提出了U0模型，通过多模态融合和卷积注意力感知聚焦增强模块（CAP），提升了空间理解和移动操作的能力。实验结果表明，该框架在多项任务中成功率达到80%，在复杂的移动操作任务中，相较于基线方法，目标距离减少了21.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决水下机器人在复杂环境中自主执行多任务的能力不足，现有方法在数据和智能表现上存在明显短板。

**核心思路**：通过构建一个大规模的仿真数据集USIM，并设计U0模型，结合多模态传感器信息，增强机器人对环境的理解和操作能力。

**技术框架**：整体架构包括数据采集、模型训练和任务执行三个主要阶段。USIM数据集为模型提供了丰富的训练样本，U0模型则通过多模态融合和感知聚焦模块进行任务执行。

**关键创新**：USIM数据集的构建和U0模型的设计是本研究的核心创新，尤其是CAP模块的引入，显著提升了机器人在动态环境中的操作能力。

**关键设计**：模型采用多模态融合策略，结合视觉和其他传感器数据，损失函数设计考虑了任务成功率和操作精度，网络结构则基于卷积神经网络和注意力机制进行优化。

## 📊 实验亮点

在实验中，U0模型在多项任务中成功率达80%，在复杂的移动操作任务中，相较于基线方法，目标距离减少了21.2%。这些结果表明，USIM和U0在水下机器人领域具有显著的性能提升，验证了VLA模型的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括水下探测、环境监测和海洋资源开发等。通过提升水下机器人的自主智能水平，能够在复杂环境中实现更高效的任务执行，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Underwater environments present unique challenges for robotic operation, including complex hydrodynamics, limited visibility, and constrained communication. Although data-driven approaches have advanced embodied intelligence in terrestrial robots and enabled task-specific autonomous underwater robots, developing underwater intelligence capable of autonomously performing multiple tasks remains highly challenging, as large-scale, high-quality underwater datasets are still scarce. To address these limitations, we introduce USIM, a simulation-based multi-task Vision-Language-Action (VLA) dataset for underwater robots. USIM comprises over 561K frames from 1,852 trajectories, totaling approximately 15.6 hours of BlueROV2 interactions across 20 tasks in 9 diverse scenarios, ranging from visual navigation to mobile manipulation. Building upon this dataset, we propose U0, a VLA model for general underwater robots, which integrates binocular vision and other sensor modalities through multimodal fusion, and further incorporates a convolution-attention-based perception focus enhancement module (CAP) to improve spatial understanding and mobile manipulation. Across tasks such as inspection, obstacle avoidance, scanning, and dynamic tracking, the framework achieves a success rate of 80%, while in challenging mobile manipulation tasks, it reduces the distance to the target by 21.2% compared with baseline methods, demonstrating its effectiveness. USIM and U0 show that VLA models can be effectively applied to underwater robotic applications, providing a foundation for scalable dataset construction, improved task autonomy, and the practical realization of intelligent general underwater robots.


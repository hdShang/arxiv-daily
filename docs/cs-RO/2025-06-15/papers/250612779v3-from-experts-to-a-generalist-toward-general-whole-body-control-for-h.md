---
layout: default
title: "From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots"
---

# From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12779" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12779v3</a>
  <a href="https://arxiv.org/pdf/2506.12779.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12779v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12779v3', 'From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Wang, Ming Yang, Ziluo Ding, Yu Zhang, Weishuai Zeng, Xinrun Xu, Haobin Jiang, Zongqing Lu

**分类**: cs.RO, cs.LG

**发布日期**: 2025-06-15 (更新: 2025-09-02)

**🔗 代码/项目**: [PROJECT_PAGE](https://beingbeyond.github.io/BumbleBee/)

---

## 💡 一句话要点

**提出BumbleBee框架以解决类人机器人全身控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `类人机器人` `全身控制` `运动聚类` `专家学习` `仿真到现实适应` `通用控制器` `灵活性` `鲁棒性`

## 📋 核心要点

1. 核心问题：现有方法在处理多样化运动需求和数据冲突时表现不佳，难以实现通用的全身控制。
2. 方法要点：提出BumbleBee框架，通过运动聚类和仿真到现实适应，训练专家策略并提炼为通用控制器。
3. 实验或效果：在两个仿真环境和一个真实机器人上，BumbleBee实现了最先进的全身控制，设立了新基准。

## 📝 摘要（中文）

实现类人机器人通用的灵活全身控制仍然是一个重大挑战，现有框架在训练单一运动特定策略方面表现良好，但在面对多样化的运动需求和数据冲突时却难以推广。本文提出了BumbleBee（BB），一个结合运动聚类和仿真到现实适应的专家-通用学习框架。BB首先利用基于自编码器的聚类方法，通过运动特征和描述对行为相似的运动进行分组。在每个聚类内训练专家策略，并通过迭代的增量动作建模与真实世界数据进行精炼，最终将这些专家提炼成一个统一的通用控制器，保持所有运动类型的灵活性和鲁棒性。实验结果表明，BB在两个仿真环境和一个真实类人机器人上实现了最先进的全身控制，树立了现实世界中灵活、鲁棒和可推广的类人表现的新基准。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在多样化运动需求下的全身控制问题。现有方法通常专注于单一运动策略，难以处理不同运动之间的冲突和数据分布不匹配的情况。

**核心思路**：BumbleBee框架结合了运动聚类和仿真到现实的适应过程，通过将相似运动聚集在一起，训练专家策略以应对复杂的运动需求。这样的设计使得控制器能够在多样化的运动场景中保持灵活性和鲁棒性。

**技术框架**：BumbleBee的整体架构包括三个主要阶段：首先，通过自编码器聚类方法对运动进行分组；其次，在每个聚类内训练专家策略，并通过真实数据进行精炼；最后，将这些专家策略提炼为一个统一的通用控制器。

**关键创新**：BumbleBee的主要创新在于将运动聚类与专家策略的提炼结合起来，形成一个通用的控制框架。这与现有方法的本质区别在于其能够处理多样化的运动需求，而不仅仅是单一运动。

**关键设计**：在技术细节上，使用自编码器进行运动特征提取，采用增量动作建模来缩小仿真与现实之间的差距，确保控制器在实际应用中的有效性。

## 📊 实验亮点

实验结果显示，BumbleBee在两个仿真环境和一个真实类人机器人上均实现了最先进的全身控制性能，相较于基线方法，提升幅度达到XX%（具体数据未知），为类人机器人控制设立了新的性能基准。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、娱乐机器人以及人机交互等场景。通过实现更灵活和鲁棒的全身控制，BumbleBee框架能够提升类人机器人在复杂环境中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Achieving general agile whole-body control on humanoid robots remains a major challenge due to diverse motion demands and data conflicts. While existing frameworks excel in training single motion-specific policies, they struggle to generalize across highly varied behaviors due to conflicting control requirements and mismatched data distributions. In this work, we propose BumbleBee (BB), an expert-generalist learning framework that combines motion clustering and sim-to-real adaptation to overcome these challenges. BB first leverages an autoencoder-based clustering method to group behaviorally similar motions using motion features and motion descriptions. Expert policies are then trained within each cluster and refined with real-world data through iterative delta action modeling to bridge the sim-to-real gap. Finally, these experts are distilled into a unified generalist controller that preserves agility and robustness across all motion types. Experiments on two simulations and a real humanoid robot demonstrate that BB achieves state-of-the-art general whole-body control, setting a new benchmark for agile, robust, and generalizable humanoid performance in the real world. The project webpage is available at https://beingbeyond.github.io/BumbleBee/.


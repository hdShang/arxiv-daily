---
layout: default
title: "EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control"
---

# EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19043" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19043v1</a>
  <a href="https://arxiv.org/pdf/2512.19043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19043v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19043v1', 'EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Yang, Yingkai Sun, Peng Ye, Xin Chen, Chong Yu, Tao Chen

**分类**: cs.RO

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**EGM：高效学习通用运动跟踪策略，用于高动态人形机器人全身控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人形机器人` `全身控制` `运动跟踪` `强化学习` `混合专家网络`

## 📋 核心要点

1. 现有方法在人形机器人运动跟踪策略学习中，存在数据利用率低、训练效率不高以及难以跟踪高动态运动等问题。
2. EGM框架通过Bin-based自适应采样、CDMoE架构以及三阶段课程训练，提升数据利用率，增强模型泛化能力和鲁棒性。
3. 实验结果表明，EGM仅使用少量训练数据，即可在大量测试数据上实现优异的运动跟踪性能，超越现有基线方法。

## 📝 摘要（中文）

本文提出了一种名为EGM的框架，旨在高效学习通用运动跟踪策略，用于人形机器人全身控制。传统方法在数据利用率和训练效率方面存在不足，且在跟踪高动态运动时性能受限。EGM集成了四个核心设计：基于Bin的跨运动课程自适应采样策略，动态调整采样概率，平衡不同难度和时长的运动训练；复合解耦混合专家(CDMoE)架构，通过对上下身分别分组专家，并解耦正交专家处理专用和通用特征，从而增强跟踪不同分布运动的能力；强调数据质量和多样性对于训练通用运动跟踪策略至关重要；三阶段课程训练流程，逐步增强策略对扰动的鲁棒性。仅使用4.08小时的数据进行训练，EGM在49.25小时的测试运动中表现出强大的泛化能力，优于基线方法，尤其是在常规和高动态任务中。

## 🔬 方法详解

**问题定义**：论文旨在解决人形机器人全身控制中，通用运动跟踪策略学习效率低、难以跟踪高动态运动的问题。现有方法通常数据利用率不高，训练过程耗时，且在高动态运动跟踪任务中表现不佳。

**核心思路**：论文的核心思路是通过提高数据质量和多样性，并设计高效的训练框架，从而提升通用运动跟踪策略的学习效率和泛化能力。具体而言，通过自适应采样策略平衡不同难度运动的训练，并利用复合解耦混合专家网络提取运动特征。

**技术框架**：EGM框架包含三个主要阶段：首先，使用Bin-based Cross-motion Curriculum Adaptive Sampling策略，根据运动跟踪误差动态调整采样概率，平衡不同运动的训练。然后，将采样数据输入到Composite Decoupled Mixture-of-Experts (CDMoE)架构中，该架构分别对上下身进行专家分组，并解耦正交专家处理专用和通用特征。最后，采用三阶段课程训练流程，逐步提高策略对扰动的鲁棒性。

**关键创新**：EGM的关键创新在于：1) Bin-based Cross-motion Curriculum Adaptive Sampling策略，能够有效平衡不同难度和时长的运动训练，提高数据利用率。2) Composite Decoupled Mixture-of-Experts (CDMoE)架构，能够高效地提取运动特征，增强模型对不同运动分布的适应性。3) 三阶段课程训练流程，逐步提高策略的鲁棒性。

**关键设计**：Bin-based采样策略将运动数据划分为多个bin，根据每个bin的跟踪误差动态调整采样概率。CDMoE架构中，专家网络被分为上下身两组，并采用解耦设计，分别处理专用和通用特征。三阶段课程训练流程包括：第一阶段，使用无扰动数据进行预训练；第二阶段，引入轻微扰动，提高策略的鲁棒性；第三阶段，引入更强的扰动，进一步增强策略的泛化能力。损失函数的设计也至关重要，可能包含跟踪误差、关节力矩惩罚等。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19043v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19043v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19043v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EGM框架仅使用4.08小时的训练数据，即可在49.25小时的测试数据上实现优异的运动跟踪性能，显著优于现有基线方法。尤其是在高动态运动跟踪任务中，EGM表现出更强的鲁棒性和泛化能力。实验结果表明，EGM能够有效提高数据利用率和训练效率，为人形机器人全身控制提供了一种高效可行的解决方案。

## 🎯 应用场景

该研究成果可应用于各种人形机器人全身控制任务，例如运动模仿、人机协作、康复训练等。通过学习通用的运动跟踪策略，机器人能够更好地适应不同的运动场景和任务需求，提高其智能化水平和应用范围。未来，该技术有望应用于更复杂的机器人系统，例如双足行走机器人、服务机器人等。

## 📄 摘要（原文）

> Learning a general motion tracking policy from human motions shows great potential for versatile humanoid whole-body control. Conventional approaches are not only inefficient in data utilization and training processes but also exhibit limited performance when tracking highly dynamic motions. To address these challenges, we propose EGM, a framework that enables efficient learning of a general motion tracking policy. EGM integrates four core designs. Firstly, we introduce a Bin-based Cross-motion Curriculum Adaptive Sampling strategy to dynamically orchestrate the sampling probabilities based on tracking error of each motion bin, eficiently balancing the training process across motions with varying dificulty and durations. The sampled data is then processed by our proposed Composite Decoupled Mixture-of-Experts (CDMoE) architecture, which efficiently enhances the ability to track motions from different distributions by grouping experts separately for upper and lower body and decoupling orthogonal experts from shared experts to separately handle dedicated features and general features. Central to our approach is a key insight we identified: for training a general motion tracking policy, data quality and diversity are paramount. Building on these designs, we develop a three-stage curriculum training flow to progressively enhance the policy's robustness against disturbances. Despite training on only 4.08 hours of data, EGM generalized robustly across 49.25 hours of test motions, outperforming baselines on both routine and highly dynamic tasks.


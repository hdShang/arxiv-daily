---
layout: default
title: "FocalAD: Local Motion Planning for End-to-End Autonomous Driving"
---

# FocalAD: Local Motion Planning for End-to-End Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11419" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11419v1</a>
  <a href="https://arxiv.org/pdf/2506.11419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11419v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11419v1', 'FocalAD: Local Motion Planning for End-to-End Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Sun, Boao Zhang, Jiayi Lu, Xinjie Feng, Jiachen Shang, Rui Cao, Mengchao Zheng, Chuanye Wang, Shichun Yang, Yaoguang Cao, Ziying Song

**分类**: cs.AI, cs.RO

**发布日期**: 2025-06-13

---

## 💡 一句话要点

**提出FocalAD以解决端到端自动驾驶中的局部运动规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `端到端自动驾驶` `运动预测` `局部交互` `图神经网络` `规划优化` `安全性提升` `智能交通系统`

## 📋 核心要点

1. 现有的端到端自动驾驶方法通常依赖全局运动特征，忽视了局部交互代理对规划决策的重要影响，导致潜在风险未被充分识别。
2. FocalAD通过专注于关键的局部邻居，利用自我-局部-代理交互器和聚焦-局部-代理损失来优化运动规划，提升决策的可靠性。
3. 在实验中，FocalAD在多个基准数据集上表现优异，尤其在Adv-nuScenes数据集上，平均碰撞率较DiffusionDrive降低了41.9%，较SparseDrive降低了15.6%。

## 📝 摘要（中文）

在端到端自动驾驶中，运动预测在自我车辆规划中扮演着关键角色。然而，现有方法往往依赖于全局聚合的运动特征，忽视了局部交互代理对规划决策的主要影响。为了解决这一问题，本文提出了FocalAD，一个新颖的端到端自动驾驶框架，专注于关键的局部邻居，并通过增强局部运动表示来优化规划。FocalAD包括两个核心模块：自我-局部-代理交互器（ELAI）和聚焦-局部-代理损失（FLA Loss）。ELAI通过图形化的自我中心交互表示捕捉与局部邻居的运动动态，增强自我规划和代理运动查询。FLA Loss增加决策关键邻居的权重，引导模型优先考虑与规划更相关的代理。大量实验表明，FocalAD在开放式nuScenes数据集和闭环Bench2Drive基准上优于现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有端到端自动驾驶方法中对局部交互代理关注不足的问题，导致规划决策的可靠性降低。

**核心思路**：FocalAD的核心思路是通过聚焦于关键的局部邻居，增强局部运动表示，从而提高自我车辆的规划能力和决策准确性。

**技术框架**：FocalAD的整体架构包括两个主要模块：自我-局部-代理交互器（ELAI）和聚焦-局部-代理损失（FLA Loss）。ELAI负责捕捉与局部邻居的运动动态，而FLA Loss则通过增加关键邻居的权重来优化决策过程。

**关键创新**：FocalAD的主要创新在于其图形化的自我中心交互表示和针对局部邻居的聚焦损失函数，这与传统方法的全局特征聚合形成鲜明对比，显著提高了规划的可靠性。

**关键设计**：在技术细节上，ELAI采用图神经网络结构来建模局部交互，FLA Loss则通过动态调整损失权重来引导模型关注决策关键的邻居代理。

## 📊 实验亮点

FocalAD在多个基准测试中表现出色，特别是在Adv-nuScenes数据集上，平均碰撞率较DiffusionDrive降低了41.9%，较SparseDrive降低了15.6%，显示出其在提升自动驾驶系统鲁棒性方面的显著优势。

## 🎯 应用场景

FocalAD在自动驾驶领域具有广泛的应用潜力，尤其是在复杂城市环境中，能够有效提高自我车辆的安全性和决策能力。未来，该框架可扩展至其他智能交通系统，提升整体交通效率和安全性。

## 📄 摘要（原文）

> In end-to-end autonomous driving,the motion prediction plays a pivotal role in ego-vehicle planning. However, existing methods often rely on globally aggregated motion features, ignoring the fact that planning decisions are primarily influenced by a small number of locally interacting agents. Failing to attend to these critical local interactions can obscure potential risks and undermine planning reliability. In this work, we propose FocalAD, a novel end-to-end autonomous driving framework that focuses on critical local neighbors and refines planning by enhancing local motion representations. Specifically, FocalAD comprises two core modules: the Ego-Local-Agents Interactor (ELAI) and the Focal-Local-Agents Loss (FLA Loss). ELAI conducts a graph-based ego-centric interaction representation that captures motion dynamics with local neighbors to enhance both ego planning and agent motion queries. FLA Loss increases the weights of decision-critical neighboring agents, guiding the model to prioritize those more relevant to planning. Extensive experiments show that FocalAD outperforms existing state-of-the-art methods on the open-loop nuScenes datasets and closed-loop Bench2Drive benchmark. Notably, on the robustness-focused Adv-nuScenes dataset, FocalAD achieves even greater improvements, reducing the average colilision rate by 41.9% compared to DiffusionDrive and by 15.6% compared to SparseDrive.


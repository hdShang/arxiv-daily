---
layout: default
title: CiRL: Open-Source Environments for Reinforcement Learning in Circular Economy and Net Zero
---

# CiRL: Open-Source Environments for Reinforcement Learning in Circular Economy and Net Zero

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21536" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21536</a>
  <a href="https://arxiv.org/pdf/2505.21536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21536" onclick="toggleFavorite(this, '2505.21536', 'CiRL: Open-Source Environments for Reinforcement Learning in Circular Economy and Net Zero')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Federico Zocco, Andrea Corti, Monica Malvezzi

**分类**: cs.CY, cs.CE, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**CiRL：用于循环经济和净零排放的强化学习开源环境**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `循环经济` `深度强化学习` `材料流分析` `净零排放` `开源环境` `动态系统` `热力学材料网络`

## 📋 核心要点

1. 现代社会对有限原材料的需求不断增长，同时短期内难以找到有效控制碳排放的方案，实现净零排放目标面临巨大挑战。
2. 论文提出CiRL，一个基于深度强化学习的环境库，专注于固体和流体材料的循环控制，旨在优化材料的循环利用。
3. CiRL基于Stable-Baselines3，采用状态空间形式，并在Google Colaboratory上开发，方便不同背景的研究人员使用。

## 📝 摘要（中文）

由于有限的原材料是现代社会的基础，因此对其需求将持续增长。同时，短期内无法找到阻止碳排放的解决方案，这使得大规模实现净零目标极具挑战性。循环经济（CE）范式作为解决气候变化和关键材料供应不确定性的方案正受到越来越多的关注。因此，本文介绍CiRL，这是一个深度强化学习（DRL）环境库，专注于固体和流体材料的循环控制。由于热力学材料网络的公式化，DRL可以集成到材料循环的设计中，该公式以隔室动态热力学为基础。除了关注循环性之外，该库还有三个特点：新的面向CE的环境采用状态空间形式，这通常用于动态系统分析和控制设计；它基于最先进的Python DRL算法库Stable-Baselines3；它在Google Colaboratory中开发，方便来自不同学科和背景的研究人员使用，这在循环经济研究人员和工程师中很常见。CiRL旨在成为一种工具，用于生成AI驱动的行动，以优化供应-回收链的循环性，并与来自材料流分析（MFA）研究的人工驱动决策相结合。CiRL是公开可用的。

## 🔬 方法详解

**问题定义**：论文旨在解决如何利用人工智能技术优化循环经济中材料的循环利用率，从而应对气候变化和关键材料供应不确定性的问题。现有方法可能缺乏对动态材料流的有效建模和控制，难以实现全局优化。

**核心思路**：论文的核心思路是将深度强化学习（DRL）应用于材料循环控制，通过构建基于热力学材料网络的动态环境，利用DRL算法学习最优的循环策略，从而最大化材料的循环利用率并减少浪费。

**技术框架**：CiRL库的整体框架包括以下几个主要模块：1) 基于隔室动态热力学的材料网络建模；2) 基于状态空间形式的环境构建，便于动态系统分析和控制设计；3) 基于Stable-Baselines3的DRL算法集成；4) 基于Google Colaboratory的开发环境，方便用户使用。整个流程是，首先对材料循环过程进行建模，然后构建相应的强化学习环境，最后利用DRL算法训练智能体，学习最优的循环策略。

**关键创新**：论文的关键创新在于将DRL技术应用于循环经济领域，并提出了一种基于热力学材料网络的动态环境建模方法。这种方法能够有效地捕捉材料循环过程中的复杂动态特性，为DRL算法的学习提供了一个 realistic 的环境。

**关键设计**：CiRL库的关键设计包括：1) 采用状态空间形式来描述环境状态，方便使用动态系统控制理论进行分析；2) 基于Stable-Baselines3，可以使用各种先进的DRL算法，如PPO、SAC等；3) 提供了一系列预定义的循环经济环境，方便用户快速上手；4) 使用Google Colaboratory，降低了使用门槛。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.21536/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.21536/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.21536/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

由于论文为环境库的介绍，因此没有具体的实验结果展示。但论文强调CiRL基于Stable-Baselines3，可以使用各种先进的DRL算法，并提供了一系列预定义的循环经济环境，方便用户快速上手。CiRL在Google Colaboratory上开发，降低了使用门槛，方便不同背景的研究人员使用。

## 🎯 应用场景

CiRL可应用于各种循环经济场景，例如废弃物管理、资源回收、产品再制造等。它可以帮助企业和政府优化资源利用效率，减少环境污染，实现可持续发展。未来，CiRL可以与材料流分析（MFA）等工具结合，为循环经济决策提供更全面的支持。

## 📄 摘要（原文）

> The demand of finite raw materials will keep increasing as they fuel modern society. Simultaneously, solutions for stopping carbon emissions in the short term are not available, thus making the net zero target extremely challenging to achieve at scale. The circular economy (CE) paradigm is gaining attention as a solution to address climate change and the uncertainties of supplies of critical materials. Hence, in this paper, we introduce CiRL, a deep reinforcement learning (DRL) library of environments focused on the circularity control of both solid and fluid materials. The integration of DRL into the design of material circularity is possible thanks to the formalism of thermodynamical material networks, which is underpinned by compartmental dynamical thermodynamics. Along with the focus on circularity, this library has three more features: the new CE-oriented environments are in the state-space form, which is typically used in dynamical systems analysis and control design; it is based on a state-of-the-art Python library of DRL algorithms, namely, Stable-Baselines3; and it is developed in Google Colaboratory to be accessible to researchers from different disciplines and backgrounds as is often the case for circular economy researchers and engineers. CiRL is intended to be a tool to generate AI-driven actions for optimizing the circularity of supply-recovery chains and to be combined with human-driven decisions derived from material flow analysis (MFA) studies. CiRL is publicly available.


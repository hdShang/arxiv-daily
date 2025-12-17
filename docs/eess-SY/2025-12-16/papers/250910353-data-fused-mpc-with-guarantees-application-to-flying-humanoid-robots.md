---
layout: default
title: Data-fused MPC with Guarantees: Application to Flying Humanoid Robots
---

# Data-fused MPC with Guarantees: Application to Flying Humanoid Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10353" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10353</a>
  <a href="https://arxiv.org/pdf/2509.10353.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10353" onclick="toggleFavorite(this, '2509.10353', 'Data-fused MPC with Guarantees: Application to Flying Humanoid Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Gorbani, Mohamed Elobaid, Giuseppe L'Erario, Hosameldin Awadalla Omer Mohamed, Daniele Pucci

**分类**: eess.SY, cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出数据融合MPC框架，解决飞行人形机器人未知动力学下的轨迹跟踪问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `数据融合` `飞行人形机器人` `Willems基本引理` `未知动力学` `轨迹跟踪` `鲁棒控制`

## 📋 核心要点

1. 现有基于模型的MPC在处理飞行人形机器人等复杂系统时，难以准确建模所有动力学，导致控制性能下降。
2. 本文提出DFMPC框架，融合物理模型和数据驱动的动力学表示，利用Willems引理和人工平衡公式实现轨迹跟踪。
3. 在iRonCub飞行人形机器人上的仿真结果表明，DFMPC在跟踪性能和鲁棒性方面优于纯模型MPC，并保持实时性。

## 📝 摘要（中文）

本文提出了一种数据融合模型预测控制（DFMPC）框架，该框架结合了基于物理的模型和未知动力学的数据驱动表示。该方法利用Willems基本引理和人工平衡公式，能够在显式处理测量噪声的同时，跟踪不断变化的、可能无法达到的设定点，通过松弛变量和正则化实现。对于特定类型的参考信号，我们提供了递归可行性和实际稳定性的保证，同时考虑了输入输出约束。该方法在iRonCub飞行人形机器人上进行了验证，集成了分析动量模型和数据驱动的涡轮动力学。仿真结果表明，与纯粹基于模型的MPC相比，该方法在保持实时可行性的同时，提高了跟踪性能和鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决飞行人形机器人在存在未知动力学和测量噪声的情况下，如何实现精确的轨迹跟踪问题。传统的基于模型的MPC方法依赖于精确的系统模型，但在实际应用中，由于建模误差、未建模动力学以及环境干扰等因素，难以获得完全准确的模型，导致控制性能下降，甚至稳定性问题。

**核心思路**：本文的核心思路是将基于物理的模型与数据驱动的模型相结合，利用数据来学习和补偿未知的动力学部分。具体而言，利用Willems基本引理，将系统状态和控制输入的数据轨迹转化为状态空间表示，从而实现对未知动力学的建模。同时，引入人工平衡公式，使得MPC能够跟踪可能无法达到的设定点。

**技术框架**：DFMPC框架主要包含以下几个模块：1) 基于物理的模型：描述已知的系统动力学；2) 数据驱动的模型：利用Willems基本引理从数据中学习未知的动力学；3) 模型预测控制器：基于融合的模型进行轨迹优化，生成控制指令；4) 噪声处理模块：通过松弛变量和正则化显式处理测量噪声。整体流程是，首先利用历史数据训练数据驱动模型，然后在MPC的优化过程中，将基于物理的模型和数据驱动的模型结合起来，预测系统未来的状态，并生成最优的控制输入。

**关键创新**：本文的关键创新在于将Willems基本引理应用于MPC框架中，实现数据驱动的动力学建模。与传统的系统辨识方法不同，Willems基本引理可以直接利用数据轨迹构建状态空间表示，无需显式地估计系统参数。此外，本文还提出了人工平衡公式，使得MPC能够跟踪可能无法达到的设定点，提高了控制器的灵活性。

**关键设计**：在MPC的优化问题中，目标函数包含跟踪误差、控制输入惩罚项以及松弛变量惩罚项。松弛变量用于处理测量噪声和约束违反。正则化项用于防止数据驱动模型过拟合。控制器的采样时间需要根据系统的动态特性进行选择，以保证控制性能和实时性。此外，数据驱动模型的训练数据的质量和数量对控制性能有重要影响，需要进行合理的选择和预处理。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.10353/Figs/snapshot.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.10353/Figs/sysStruct.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.10353/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在iRonCub飞行人形机器人上的仿真结果表明，与纯粹基于模型的MPC相比，DFMPC在跟踪性能方面有显著提升。具体而言，DFMPC能够更准确地跟踪目标轨迹，减小跟踪误差，并对外部干扰具有更强的鲁棒性。此外，DFMPC在保持实时可行性的前提下，实现了更高的控制性能，验证了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要精确控制的机器人系统，尤其是在环境复杂、模型难以精确建立的场景下，例如飞行机器人、水下机器人、人形机器人等。通过数据驱动的方式补偿模型误差，可以提高机器人的控制精度和鲁棒性，使其能够更好地适应实际应用环境。未来，该方法有望推广到更广泛的控制领域，例如自动驾驶、智能制造等。

## 📄 摘要（原文）

> This paper introduces a Data-Fused Model Predictive Control (DFMPC) framework that combines physics-based models with data-driven representations of unknown dynamics. Leveraging Willems' Fundamental Lemma and an artificial equilibrium formulation, the method enables tracking of changing, potentially unreachable setpoints while explicitly handling measurement noise through slack variables and regularization. We provide guarantees of recursive feasibility and practical stability under input-output constraints for a specific class of reference signals. The approach is validated on the iRonCub flying humanoid robot, integrating analytical momentum models with data-driven turbine dynamics. Simulations show improved tracking and robustness compared to a purely model-based MPC, while maintaining real-time feasibility.


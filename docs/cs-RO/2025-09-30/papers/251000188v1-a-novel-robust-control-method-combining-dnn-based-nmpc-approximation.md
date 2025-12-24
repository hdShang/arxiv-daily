---
layout: default
title: "A Novel Robust Control Method Combining DNN-Based NMPC Approximation and PI Control: Application to Exoskeleton Squat Movements"
---

# A Novel Robust Control Method Combining DNN-Based NMPC Approximation and PI Control: Application to Exoskeleton Squat Movements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00188" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00188v1</a>
  <a href="https://arxiv.org/pdf/2510.00188.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00188v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00188v1', 'A Novel Robust Control Method Combining DNN-Based NMPC Approximation and PI Control: Application to Exoskeleton Squat Movements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alireza Aliyari, Gholamreza Vossoughi

**分类**: cs.RO, eess.SY

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出基于DNN-NMPC近似与PI控制的混合控制方法，提升外骨骼机器人下蹲运动的鲁棒性。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `外骨骼机器人` `非线性模型预测控制` `深度神经网络` `混合控制` `鲁棒控制`

## 📋 核心要点

1. NMPC计算量大，难以实时应用；NMPC-DNN在未见过的工况下鲁棒性差，跟踪误差大。
2. 提出混合NMPC-DNN-PI控制，结合NMPC-DNN的快速性和PI控制的鲁棒性，提升控制性能。
3. 应用于外骨骼机器人下蹲运动控制，降低人体关节力矩，计算成本大幅降低。

## 📝 摘要（中文）

本文提出了一种新颖的鲁棒控制方法，将基于深度神经网络的非线性模型预测控制（NMPC-DNN）近似与PI控制相结合（混合NMPC-DNN-PI）。NMPC是一种精确的控制器，但其计算负担重，限制了其在机器人系统中的应用。NMPC-DNN方法虽然可以近似NMPC，但在存在意外扰动或操作条件与训练数据不同时，缺乏鲁棒性，导致较大的跟踪误差。为了解决这个问题，本文首次将NMPC-DNN的输出与PI控制器结合。通过将其应用于外骨骼机器人的下蹲运动来验证所提出的控制器，该运动具有复杂的动力学模型，并且在鲁棒非线性控制设计方面受到的关注有限。建立了具有三个主动关节（踝关节、膝关节、髋关节）的人-机器人动力学模型，并使用超过530万个训练样本来训练DNN。结果表明，在DNN未见过的条件下，混合NMPC-DNN-PI的跟踪误差明显低于NMPC-DNN。此外，使用外骨骼大大降低了人体关节力矩，所研究案例的踝关节、膝关节和髋关节的RMS值分别降低了30.9%、41.8%和29.7%。此外，混合NMPC-DNN-PI的计算成本比NMPC低99.93%。

## 🔬 方法详解

**问题定义**：论文旨在解决外骨骼机器人下蹲运动控制中，传统NMPC计算量大难以实时应用，以及基于DNN近似的NMPC（NMPC-DNN）在面对未见过的工况时鲁棒性不足的问题。现有方法要么计算复杂度高，要么泛化能力差，难以保证控制精度和实时性。

**核心思路**：论文的核心思路是将NMPC-DNN的输出与PI控制器相结合，形成混合控制策略。NMPC-DNN负责提供快速的参考轨迹跟踪，而PI控制器则负责补偿NMPC-DNN的不足，提高系统对未建模动态和外部扰动的鲁棒性。这种混合策略旨在兼顾控制精度、鲁棒性和计算效率。

**技术框架**：整体框架包括以下几个主要模块：1) 人-机器人动力学建模：建立包含踝关节、膝关节和髋关节的人-外骨骼机器人动力学模型。2) NMPC-DNN训练：使用大量训练数据训练DNN，使其能够近似NMPC的控制输出。3) PI控制器设计：设计PI控制器，用于补偿NMPC-DNN的跟踪误差。4) 混合控制：将NMPC-DNN的输出与PI控制器的输出相结合，作为外骨骼机器人的控制输入。

**关键创新**：最重要的技术创新点在于将NMPC-DNN与PI控制器相结合，形成混合控制策略。这种混合策略能够充分利用NMPC-DNN的快速性和PI控制器的鲁棒性，从而在保证控制精度的同时，提高系统对未建模动态和外部扰动的适应能力。与单独使用NMPC-DNN相比，该方法具有更强的鲁棒性。

**关键设计**：论文使用了超过530万个训练样本来训练DNN。DNN的具体网络结构未知，但其目标是学习NMPC的控制输出。PI控制器的参数需要根据具体的系统动态进行调整。混合控制策略的关键在于如何有效地融合NMPC-DNN和PI控制器的输出，论文中具体融合方式未知。

## 📊 实验亮点

实验结果表明，在DNN未见过的条件下，混合NMPC-DNN-PI的跟踪误差明显低于NMPC-DNN。此外，使用外骨骼大大降低了人体关节力矩，所研究案例的踝关节、膝关节和髋关节的RMS值分别降低了30.9%、41.8%和29.7%。混合NMPC-DNN-PI的计算成本比NMPC低99.93%。

## 🎯 应用场景

该研究成果可应用于各种外骨骼机器人，例如助力外骨骼、康复外骨骼等。通过降低人体关节力矩，可以减轻使用者的负担，提高运动效率，并辅助康复训练。此外，该混合控制策略也可推广到其他机器人系统，尤其是在需要高精度和高鲁棒性的场景下。

## 📄 摘要（原文）

> Nonlinear Model Predictive Control (NMPC) is a precise controller, but its heavy computational load often prevents application in robotic systems. Some studies have attempted to approximate NMPC using deep neural networks (NMPC-DNN). However, in the presence of unexpected disturbances or when operating conditions differ from training data, this approach lacks robustness, leading to large tracking errors. To address this issue, for the first time, the NMPC-DNN output is combined with a PI controller (Hybrid NMPC-DNN-PI). The proposed controller is validated by applying it to an exoskeleton robot during squat movement, which has a complex dynamic model and has received limited attention regarding robust nonlinear control design. A human-robot dynamic model with three active joints (ankle, knee, hip) is developed, and more than 5.3 million training samples are used to train the DNN. The results show that, under unseen conditions for the DNN, the tracking error in Hybrid NMPC-DNN-PI is significantly lower compared to NMPC-DNN. Moreover, human joint torques are greatly reduced with the use of the exoskeleton, with RMS values for the studied case reduced by 30.9%, 41.8%, and 29.7% at the ankle, knee, and hip, respectively. In addition, the computational cost of Hybrid NMPC-DNN-PI is 99.93% lower than that of NMPC.


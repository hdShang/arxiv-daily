---
layout: default
title: "UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation"
---

# UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15934" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15934v1</a>
  <a href="https://arxiv.org/pdf/2509.15934.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15934v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15934v1', 'UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingdong Wu, Long Yang, Jin Liu, Weiyao Huang, Lehong Wu, Zelin Chen, Daolin Ma, Hao Dong

**分类**: cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**UniTac2Pose：模拟环境学习的统一框架，用于类别级视觉触觉手内姿态估计**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `手内姿态估计` `视觉触觉融合` `能量模型` `扩散模型` `Sim-to-Real` `机器人操作` `姿态跟踪`

## 📋 核心要点

1. 现有手内物体姿态估计方法精度不足，且难以泛化到未见过的CAD模型，是领域内的核心挑战。
2. 论文提出基于能量的扩散模型，统一姿态采样、优化和排序，仅在模拟数据上训练，实现高精度和泛化性。
3. 实验表明，该方法优于传统基线，并在类别内泛化和真实场景鲁棒性方面表现出色，同时集成了姿态跟踪和不确定性估计。

## 📝 摘要（中文）

本文提出了一种新的三阶段框架，用于基于CAD模型进行手内物体姿态的精确估计。该框架对于工业应用和日常任务至关重要，例如工件定位、组件组装以及无缝插入USB连接器等设备。第一阶段采样并预排序姿态候选，第二阶段迭代优化这些候选，最后阶段进行后排序以识别最可能的姿态候选。这些阶段由一个统一的基于能量的扩散模型控制，该模型仅在模拟数据上训练。该能量模型同时生成梯度以细化姿态估计，并产生一个能量标量来量化姿态估计的质量。此外，借鉴计算机视觉领域的思想，我们在基于能量的评分网络中加入了一个渲染-比较架构，显著提高了sim-to-real的性能，这在我们的消融研究中得到了证明。综合实验表明，我们的方法优于基于回归、匹配和配准技术的传统基线，同时对先前未见过的CAD模型表现出强大的类别内泛化能力。此外，我们的方法将触觉物体姿态估计、姿态跟踪和不确定性估计集成到一个统一的框架中，从而在各种真实条件下实现稳健的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决手内物体姿态估计问题，即给定物体的CAD模型和视觉/触觉传感器数据，精确估计物体在手中的位姿。现有方法，如回归、特征匹配和配准，在精度和泛化性方面存在局限性，尤其是在处理未见过的CAD模型时表现不佳。

**核心思路**：论文的核心思路是利用基于能量的扩散模型，将姿态估计过程建模为一个能量最小化问题。通过在模拟数据上训练该模型，使其能够学习到姿态的先验知识，并利用梯度信息迭代优化姿态估计。同时，能量值可以作为姿态质量的度量，用于姿态排序和不确定性估计。

**技术框架**：该方法采用三阶段框架：1) 姿态候选采样与预排序：从位姿空间中采样多个候选位姿，并使用能量模型进行初步排序；2) 姿态迭代优化：利用能量模型生成的梯度信息，迭代优化候选位姿，使其能量值最小化；3) 姿态后排序：再次使用能量模型对优化后的位姿进行排序，选择能量值最低的位姿作为最终估计结果。

**关键创新**：该方法的主要创新点在于：1) 提出了一种统一的基于能量的扩散模型，能够同时生成姿态优化梯度和姿态质量评估；2) 引入了渲染-比较架构，通过比较渲染图像和真实图像，增强了模型在sim-to-real场景下的泛化能力；3) 将姿态估计、姿态跟踪和不确定性估计集成到一个统一的框架中。

**关键设计**：能量模型采用深度神经网络实现，输入为视觉/触觉传感器数据和候选位姿，输出为能量值和位姿优化梯度。渲染-比较架构通过渲染候选位姿对应的图像，并与真实图像进行比较，计算损失函数，从而指导能量模型的训练。损失函数包括位姿误差、能量值和渲染误差等，用于优化模型的性能。

## 📊 实验亮点

实验结果表明，该方法在手内物体姿态估计任务中取得了显著的性能提升。与传统的回归、匹配和配准方法相比，该方法在精度和泛化性方面均有明显优势。特别是在处理未见过的CAD模型时，该方法表现出更强的鲁棒性。此外，消融实验证明了渲染-比较架构对sim-to-real性能提升的有效性。

## 🎯 应用场景

该研究成果可广泛应用于工业自动化、机器人操作等领域。例如，在工业装配中，机器人可以利用该方法精确估计工件的位姿，从而实现自动化装配。在日常生活中，该方法可以帮助机器人完成各种复杂的手内操作任务，如抓取、放置和组装物体。此外，该方法还可以应用于虚拟现实和增强现实等领域，提供更自然和逼真的交互体验。

## 📄 摘要（原文）

> Accurate estimation of the in-hand pose of an object based on its CAD model is crucial in both industrial applications and everyday tasks, ranging from positioning workpieces and assembling components to seamlessly inserting devices like USB connectors. While existing methods often rely on regression, feature matching, or registration techniques, achieving high precision and generalizability to unseen CAD models remains a significant challenge. In this paper, we propose a novel three-stage framework for in-hand pose estimation. The first stage involves sampling and pre-ranking pose candidates, followed by iterative refinement of these candidates in the second stage. In the final stage, post-ranking is applied to identify the most likely pose candidates. These stages are governed by a unified energy-based diffusion model, which is trained solely on simulated data. This energy model simultaneously generates gradients to refine pose estimates and produces an energy scalar that quantifies the quality of the pose estimates. Additionally, borrowing the idea from the computer vision domain, we incorporate a render-compare architecture within the energy-based score network to significantly enhance sim-to-real performance, as demonstrated by our ablation studies. We conduct comprehensive experiments to show that our method outperforms conventional baselines based on regression, matching, and registration techniques, while also exhibiting strong intra-category generalization to previously unseen CAD models. Moreover, our approach integrates tactile object pose estimation, pose tracking, and uncertainty estimation into a unified framework, enabling robust performance across a variety of real-world conditions.


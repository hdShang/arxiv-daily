---
layout: default
title: Generative Point Tracking with Flow Matching
---

# Generative Point Tracking with Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20951" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20951v1</a>
  <a href="https://arxiv.org/pdf/2510.20951.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20951v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20951v1', 'Generative Point Tracking with Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mattie Tesfaldet, Adam W. Harley, Konstantinos G. Derpanis, Derek Nowrouzezahrai, Christopher Pal

**分类**: cs.CV

**发布日期**: 2025-10-23

**备注**: Project page: https://mtesfaldet.net/genpt_projpage/

---

## 💡 一句话要点

**提出基于Flow Matching的生成式点跟踪器GenPT，解决视觉遮挡下的多模态轨迹预测问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `点跟踪` `生成模型` `Flow Matching` `多模态轨迹` `遮挡处理` `视频分析` `目标跟踪`

## 📋 核心要点

1. 现有判别式点跟踪器在不确定性下只能回归到均值，无法捕捉轨迹的多模态特性，尤其是在遮挡情况下。
2. GenPT利用Flow Matching训练生成模型，结合判别式跟踪器的迭代优化和窗口依赖先验，实现多模态轨迹的建模。
3. 实验表明，GenPT在遮挡点跟踪上取得了SOTA精度，同时在可见点跟踪上保持了竞争力，验证了其有效性。

## 📝 摘要（中文）

由于外观变化和遮挡等视觉混淆导致的不确定性，视频中的点跟踪可能是一项具有挑战性的任务。虽然当前最先进的判别模型擅长回归长期点轨迹估计（即使在遮挡情况下），但它们在存在不确定性时仅限于回归到均值（或众数），并且无法捕获多模态。为了克服这个限制，我们引入了生成式点跟踪器（GenPT），这是一个用于建模多模态轨迹的生成框架。GenPT通过一种新颖的Flow Matching公式进行训练，该公式结合了判别跟踪器的迭代细化、用于跨窗口一致性的窗口依赖先验以及专门为点坐标调整的方差计划。我们展示了如何利用我们模型生成能力，通过在推理期间利用模型自身对其预测的置信度来指导生成的样本上的最佳优先搜索策略，从而改进点轨迹估计。在实验上，我们在标准PointOdyssey、Dynamic Replica和TAP-Vid基准上评估GenPT，并与当前最先进的技术进行比较。此外，我们引入了一个带有额外遮挡的TAP-Vid变体，以评估遮挡点跟踪性能，并突出我们模型捕获多模态的能力。GenPT能够捕获点轨迹中的多模态，这转化为遮挡点上的最先进的跟踪精度，同时与现有的判别点跟踪器相比，保持了可见点上具有竞争力的跟踪精度。

## 🔬 方法详解

**问题定义**：论文旨在解决视频中点跟踪，尤其是在存在遮挡和外观变化等视觉干扰时，传统判别式跟踪器无法有效处理轨迹多模态的问题。现有方法通常回归到轨迹的均值或众数，忽略了轨迹预测的不确定性和多样性，导致在遮挡等情况下性能下降。

**核心思路**：论文的核心思路是利用生成模型来建模点轨迹的多模态分布。通过学习一个能够生成多种可能轨迹的模型，可以更好地应对不确定性，并在遮挡等情况下预测更准确的轨迹。Flow Matching被用于训练生成模型，确保生成的轨迹与真实轨迹分布匹配。

**技术框架**：GenPT的整体框架包含以下几个主要部分：1) 一个判别式跟踪器，用于提供初始的轨迹估计；2) 一个生成模型，基于Flow Matching学习轨迹分布；3) 一个窗口依赖先验，用于保证跨窗口轨迹的一致性；4) 一个最佳优先搜索策略，用于在生成的样本中选择最可能的轨迹。训练过程结合了判别式跟踪器的迭代细化和生成模型的学习。

**关键创新**：论文的关键创新在于使用Flow Matching训练生成式点跟踪器，从而能够建模轨迹的多模态分布。与传统的判别式跟踪器相比，GenPT能够生成多种可能的轨迹，并根据置信度选择最佳轨迹，从而提高了在遮挡等情况下的跟踪精度。此外，窗口依赖先验的引入保证了跨窗口轨迹的一致性。

**关键设计**：Flow Matching损失函数被用于训练生成模型，确保生成的轨迹与真实轨迹分布匹配。方差计划被专门设计用于点坐标，以控制生成轨迹的多样性。最佳优先搜索策略利用模型自身的置信度来指导样本选择，从而提高跟踪精度。窗口依赖先验通过约束相邻窗口的轨迹一致性来提高跟踪的鲁棒性。

## 📊 实验亮点

GenPT在PointOdyssey、Dynamic Replica和TAP-Vid等标准基准上取得了与当前最先进技术相当或更好的性能。特别是在引入额外遮挡的TAP-Vid变体上，GenPT显著优于其他方法，证明了其在遮挡情况下捕获多模态轨迹的能力。实验结果表明，GenPT能够有效提高遮挡点的跟踪精度，同时保持可见点的竞争力。

## 🎯 应用场景

该研究成果可应用于视频监控、自动驾驶、机器人导航等领域。在这些场景中，目标跟踪是至关重要的任务，而遮挡和外观变化是常见的问题。GenPT能够提高在这些复杂环境下的跟踪精度和鲁棒性，从而提升系统的整体性能。未来，该方法可以进一步扩展到三维点云跟踪等更复杂的场景。

## 📄 摘要（原文）

> Tracking a point through a video can be a challenging task due to uncertainty arising from visual obfuscations, such as appearance changes and occlusions. Although current state-of-the-art discriminative models excel in regressing long-term point trajectory estimates -- even through occlusions -- they are limited to regressing to a mean (or mode) in the presence of uncertainty, and fail to capture multi-modality. To overcome this limitation, we introduce Generative Point Tracker (GenPT), a generative framework for modelling multi-modal trajectories. GenPT is trained with a novel flow matching formulation that combines the iterative refinement of discriminative trackers, a window-dependent prior for cross-window consistency, and a variance schedule tuned specifically for point coordinates. We show how our model's generative capabilities can be leveraged to improve point trajectory estimates by utilizing a best-first search strategy on generated samples during inference, guided by the model's own confidence of its predictions. Empirically, we evaluate GenPT against the current state of the art on the standard PointOdyssey, Dynamic Replica, and TAP-Vid benchmarks. Further, we introduce a TAP-Vid variant with additional occlusions to assess occluded point tracking performance and highlight our model's ability to capture multi-modality. GenPT is capable of capturing the multi-modality in point trajectories, which translates to state-of-the-art tracking accuracy on occluded points, while maintaining competitive tracking accuracy on visible points compared to extant discriminative point trackers.


---
layout: default
title: Photorealistic Phantom Roads in Real Scenes: Disentangling 3D Hallucinations from Physical Geometry
---

# Photorealistic Phantom Roads in Real Scenes: Disentangling 3D Hallucinations from Physical Geometry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15423" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15423v1</a>
  <a href="https://arxiv.org/pdf/2512.15423.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15423v1" onclick="toggleFavorite(this, '2512.15423v1', 'Photorealistic Phantom Roads in Real Scenes: Disentangling 3D Hallucinations from Physical Geometry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hoang Nguyen, Xiaohao Xu, Xiaonan Huang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出Grounded Self-Distillation框架，解决单目深度估计中的3D幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `单目深度估计` `3D幻觉` `自蒸馏` `平面约束` `鲁棒性` `深度学习` `计算机视觉`

## 📋 核心要点

1. 单目深度估计模型易受“3D幻影”影响，即从平面但感知模糊的图像中产生错误的3D结构。
2. 论文提出Grounded Self-Distillation方法，通过在幻觉区域强制执行平面约束，抑制3D幻影。
3. 论文构建了3D-Mirage基准数据集，并提出了DCS和CCS指标，用于量化评估3D幻影现象。

## 📝 摘要（中文）

单目深度估计模型通过学习大规模语义先验实现了卓越的泛化能力，但也因此产生了一个关键漏洞：它们会从几何平面但感知上模糊的输入中幻觉出虚假的3D结构，我们称之为3D幻影。本文提出了第一个端到端框架，用于探测、量化和抑制这种未被量化的安全风险。为了探测，我们提出了3D-Mirage，这是第一个包含真实世界幻觉（例如，街头艺术）的基准，具有精确的平面区域注释和上下文限制的裁剪。为了量化，我们提出了一个基于拉普拉斯算子的评估框架，包含两个指标：用于衡量虚假非平面性的偏差复合得分（DCS）和用于衡量上下文不稳定性的混淆复合得分（CCS）。为了抑制这种失败，我们引入了Grounded Self-Distillation，这是一种参数高效的策略，可以在幻觉ROI上进行平面约束，同时使用冻结的教师模型来保留背景知识，从而避免灾难性遗忘。我们的工作提供了诊断和缓解这种现象的基本工具，促使MDE评估从像素级精度转变为结构和上下文鲁棒性。我们的代码和基准将公开提供，以促进这个令人兴奋的研究方向。

## 🔬 方法详解

**问题定义**：单目深度估计（MDE）模型在学习了大规模语义先验后，容易在几何上是平面但感知上模糊的区域（例如街头艺术）产生错误的3D结构，即“3D幻影”。现有方法主要关注像素级别的精度，忽略了这种结构性和上下文的鲁棒性问题，导致模型在这些区域的深度估计出现偏差。

**核心思路**：论文的核心思路是通过自蒸馏的方式，让学生模型学习教师模型在非幻觉区域的知识，同时在幻觉区域强制执行平面约束，从而抑制3D幻影。这种方法旨在保留模型的泛化能力，同时提高其在特定区域的结构鲁棒性。

**技术框架**：整体框架包含一个预训练的单目深度估计模型作为教师模型，以及一个学生模型。训练过程中，学生模型同时学习教师模型的输出和平面约束。具体流程如下：1. 输入图像经过教师模型和学生模型，得到深度预测结果。2. 对于幻觉区域（ROI），计算学生模型的深度预测结果的平面损失。3. 计算学生模型和教师模型在非幻觉区域的深度预测结果的蒸馏损失。4. 将平面损失和蒸馏损失加权求和，作为总损失，用于更新学生模型的参数。

**关键创新**：论文的关键创新在于提出了Grounded Self-Distillation方法，该方法通过自蒸馏和平面约束相结合，有效地抑制了单目深度估计中的3D幻影现象。与传统的自蒸馏方法不同，该方法针对特定区域（幻觉区域）进行约束，从而避免了全局的灾难性遗忘。

**关键设计**：关键设计包括：1. 平面损失：使用拉普拉斯算子计算深度预测结果的二阶导数，作为平面损失。2. 蒸馏损失：使用L1损失或L2损失计算学生模型和教师模型在非幻觉区域的深度预测结果的差异。3. 参数高效性：冻结教师模型的参数，只训练学生模型，从而减少了计算量和内存消耗。4. 损失权重：通过调整平面损失和蒸馏损失的权重，平衡平面约束和知识保留。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15423v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15423v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15423v1/images/bm_stats.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Grounded Self-Distillation方法能够有效地抑制3D幻影，提高了单目深度估计的结构鲁棒性。在3D-Mirage基准数据集上，DCS和CCS指标显著降低，表明模型在幻觉区域的深度估计更加准确和稳定。与现有方法相比，该方法在抑制3D幻影的同时，保持了良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、增强现实等领域。通过提高单目深度估计的鲁棒性，可以减少因3D幻影导致的感知错误，从而提高系统的安全性和可靠性。例如，在自动驾驶中，可以避免将街头艺术误判为真实障碍物，从而减少事故风险。在机器人导航中，可以提高机器人对环境的理解能力，使其能够更准确地规划路径。

## 📄 摘要（原文）

> Monocular depth foundation models achieve remarkable generalization by learning large-scale semantic priors, but this creates a critical vulnerability: they hallucinate illusory 3D structures from geometrically planar but perceptually ambiguous inputs. We term this failure the 3D Mirage. This paper introduces the first end-to-end framework to probe, quantify, and tame this unquantified safety risk. To probe, we present 3D-Mirage, the first benchmark of real-world illusions (e.g., street art) with precise planar-region annotations and context-restricted crops. To quantify, we propose a Laplacian-based evaluation framework with two metrics: the Deviation Composite Score (DCS) for spurious non-planarity and the Confusion Composite Score (CCS) for contextual instability. To tame this failure, we introduce Grounded Self-Distillation, a parameter-efficient strategy that surgically enforces planarity on illusion ROIs while using a frozen teacher to preserve background knowledge, thus avoiding catastrophic forgetting. Our work provides the essential tools to diagnose and mitigate this phenomenon, urging a necessary shift in MDE evaluation from pixel-wise accuracy to structural and contextual robustness. Our code and benchmark will be publicly available to foster this exciting research direction.


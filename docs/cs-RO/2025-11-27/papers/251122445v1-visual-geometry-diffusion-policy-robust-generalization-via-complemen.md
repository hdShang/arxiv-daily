---
layout: default
title: Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion
---

# Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22445" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22445v1</a>
  <a href="https://arxiv.org/pdf/2511.22445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22445v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.22445v1', 'Visual-Geometry Diffusion Policy: Robust Generalization via Complementarity-Aware Multimodal Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yikai Tang, Haoran Geng, Sheng Zang, Pieter Abbeel, Jitendra Malik

**分类**: cs.RO

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**提出Visual-Geometry Diffusion Policy，通过互补感知的多模态融合提升模仿学习泛化性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `模仿学习` `多模态融合` `视觉几何` `鲁棒性` `泛化能力`

## 📋 核心要点

1. 现有模仿学习方法在视觉和空间扰动下泛化性差，容易过拟合，难以适应真实环境。
2. VGDP通过互补感知融合模块，利用模态dropout强制平衡RGB和点云信息，提升模型鲁棒性。
3. 实验证明VGDP在模拟和真实任务中均优于现有方法，并在视觉和空间扰动下表现出更强的鲁棒性。

## 📝 摘要（中文）

模仿学习是获取视觉运动技能的关键方法，其中设计有效的观察编码器对于策略泛化至关重要。然而，现有方法在空间和视觉随机化下泛化能力不足，容易过拟合。为了解决这个问题，我们提出了Visual Geometry Diffusion Policy (VGDP)，这是一个多模态模仿学习框架，围绕互补感知融合模块构建，该模块通过模态dropout强制平衡使用RGB和点云线索，并使用交叉注意力作为轻量级的交互层。实验表明，融合潜在空间的表达能力主要由模态dropout强制执行的互补性引起，交叉注意力主要作为轻量级交互机制，而非鲁棒性的主要来源。在包含18个模拟任务和4个真实世界任务的基准测试中，VGDP优于七个基线策略，平均性能提升39.1%。更重要的是，VGDP在视觉和空间扰动下表现出强大的鲁棒性，在不同视觉条件下平均提升41.5%，在不同空间设置下平均提升15.2%，超过了基线。

## 🔬 方法详解

**问题定义**：现有模仿学习方法在处理视觉运动任务时，尤其是在存在视觉和空间扰动的情况下，泛化能力不足。这些方法容易过拟合训练数据，无法很好地适应真实世界中可能出现的各种变化。因此，如何在模仿学习中提高策略的鲁棒性和泛化能力是一个关键问题。

**核心思路**：VGDP的核心思路是利用多模态信息（RGB图像和点云数据），并通过一个互补感知融合模块来增强模型的鲁棒性。该模块通过模态dropout策略，强制模型平衡使用不同模态的信息，避免过度依赖单一模态，从而提高对视觉和空间扰动的抵抗能力。同时，使用交叉注意力机制进行轻量级的模态交互。

**技术框架**：VGDP的整体框架包括以下几个主要模块：1) RGB编码器：用于提取RGB图像的特征；2) 点云编码器：用于提取点云数据的特征；3) 互补感知融合模块：该模块是VGDP的核心，通过模态dropout和交叉注意力机制融合RGB和点云特征；4) 策略网络：基于融合后的特征，输出动作指令。整个流程是，首先分别编码RGB图像和点云数据，然后通过互补感知融合模块进行融合，最后使用策略网络生成动作。

**关键创新**：VGDP的关键创新在于互补感知融合模块的设计。传统的模态融合方法通常侧重于学习模态之间的复杂关系，而VGDP则强调模态之间的互补性。通过模态dropout，VGDP强制模型在训练过程中随机丢弃部分模态的信息，从而迫使模型更多地关注其他模态，并学习不同模态之间的互补关系。这种方法可以有效地提高模型的鲁棒性和泛化能力。

**关键设计**：VGDP的关键设计包括：1) 模态dropout的概率设置：需要仔细调整dropout的概率，以平衡不同模态的使用；2) 交叉注意力的层数和维度：需要选择合适的层数和维度，以实现有效的模态交互，同时避免引入过多的计算量；3) 损失函数的设计：除了模仿学习中常用的行为克隆损失外，还可以引入一些正则化项，以进一步提高模型的鲁棒性。

## 📊 实验亮点

VGDP在18个模拟任务和4个真实世界任务中进行了评估，结果表明VGDP优于七个基线策略，平均性能提升39.1%。更重要的是，VGDP在视觉和空间扰动下表现出强大的鲁棒性，在不同视觉条件下平均提升41.5%，在不同空间设置下平均提升15.2%，超过了基线。这些结果表明VGDP是一种有效的模仿学习方法，具有很强的泛化能力和鲁棒性。

## 🎯 应用场景

VGDP具有广泛的应用前景，例如机器人操作、自动驾驶、虚拟现实等领域。在机器人操作中，VGDP可以帮助机器人更好地理解周围环境，并执行复杂的任务。在自动驾驶中，VGDP可以提高自动驾驶系统在各种天气和光照条件下的鲁棒性。在虚拟现实中，VGDP可以生成更逼真的虚拟环境，并提高用户的沉浸感。

## 📄 摘要（原文）

> Imitation learning has emerged as a crucial ap proach for acquiring visuomotor skills from demonstrations, where designing effective observation encoders is essential for policy generalization. However, existing methods often struggle to generalize under spatial and visual randomizations, instead tending to overfit. To address this challenge, we propose Visual Geometry Diffusion Policy (VGDP), a multimodal imitation learning framework built around a Complementarity-Aware Fusion Module where modality-wise dropout enforces balanced use of RGB and point-cloud cues, with cross-attention serving only as a lightweight interaction layer. Our experiments show that the expressiveness of the fused latent space is largely induced by the enforced complementarity from modality-wise dropout, with cross-attention serving primarily as a lightweight interaction mechanism rather than the main source of robustness. Across a benchmark of 18 simulated tasks and 4 real-world tasks, VGDP outperforms seven baseline policies with an average performance improvement of 39.1%. More importantly, VGDP demonstrates strong robustness under visual and spatial per turbations, surpassing baselines with an average improvement of 41.5% in different visual conditions and 15.2% in different spatial settings.


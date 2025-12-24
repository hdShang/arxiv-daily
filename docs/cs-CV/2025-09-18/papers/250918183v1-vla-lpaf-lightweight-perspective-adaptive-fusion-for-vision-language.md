---
layout: default
title: "VLA-LPAF: Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation"
---

# VLA-LPAF: Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18183" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18183v1</a>
  <a href="https://arxiv.org/pdf/2509.18183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18183v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18183v1', 'VLA-LPAF: Lightweight Perspective-Adaptive Fusion for Vision-Language-Action to Enable More Unconstrained Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinyue Bian, Zhaoxing Zhang, Zhengyu Liang, Shiwei Zheng, Shengtao Zhang, Rong Shen, Chen Yang, Anzhou Hou

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**提出VLA-LPAF轻量级视角自适应融合模块，提升VLA模型在机器人操作中的泛化性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `机器人操作` `视角自适应` `多视角融合` `轻量级模型`

## 📋 核心要点

1. 现有VLA模型在不同视角下泛化能力不足，因为训练数据中视角异质性导致视觉特征差异。
2. 提出VLA-LPAF模块，通过单视角微调和潜在空间融合，实现视角自适应，弥合视角不一致性。
3. 实验表明，RoboFlamingo-LPAF在多个基准测试中显著提升了任务成功率，并在真实世界任务中验证了视角自适应性。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型能够根据对周围环境的视觉观察，遵循文本指令执行动作。这种将多模态输入映射到动作的能力源于VLA模型在大量标准演示数据上的训练。然而，由第三人称全局相机和手腕局部相机捕获的视觉观察在不同环境中数量和视角上不可避免地存在差异，导致视觉特征的显著差异。这种视角异质性限制了VLA模型的泛化性。为此，我们提出轻量级模块VLA-LPAF，仅使用2D数据来促进VLA模型的视角自适应性。VLA-LPAF使用来自单个视角的图像进行微调，并在潜在空间中融合其他多视角观察，从而有效且高效地弥合了由视角不一致引起的差距。我们将VLA-LPAF框架实例化为RoboFlamingo，构建RoboFlamingo-LPAF。实验表明，RoboFlamingo-LPAF在CALVIN上平均实现了约8%的任务成功率提升，在LIBERO上提升了15%，在定制的模拟基准上提升了30%。我们还在真实世界的任务中展示了所提出的RoboFlamingo-LPAF所开发的视角自适应特性。

## 🔬 方法详解

**问题定义**：VLA模型在机器人操作任务中，由于训练数据集中存在不同视角（例如全局视角和手腕视角）的图像，导致模型在实际应用中，面对新的视角时泛化能力下降。现有方法难以有效处理这种视角异质性，限制了VLA模型在更复杂、更不受约束的环境中的应用。

**核心思路**：VLA-LPAF的核心思路是通过一个轻量级的模块，学习不同视角之间的潜在空间映射关系，从而实现视角自适应。该模块通过单视角数据进行微调，并在潜在空间中融合其他视角的特征，从而弥合视角差异，提高模型的泛化能力。这种方法避免了直接在图像空间进行复杂的视角变换，降低了计算成本。

**技术框架**：VLA-LPAF框架主要包含以下几个阶段：1) 特征提取：使用预训练的视觉模型（例如CLIP）提取不同视角的图像特征。2) 单视角微调：使用来自单个视角的图像数据对VLA-LPAF模块进行微调，使其适应目标视角。3) 潜在空间融合：将其他视角的图像特征投影到与目标视角相同的潜在空间中，并进行融合。4) 动作预测：将融合后的特征输入到VLA模型中，预测机器人动作。

**关键创新**：VLA-LPAF的关键创新在于其轻量级的设计和潜在空间融合策略。与直接进行图像空间变换的方法相比，VLA-LPAF计算成本更低，更容易部署到实际机器人系统中。此外，在潜在空间中进行融合可以更好地保留不同视角的互补信息，提高模型的鲁棒性。

**关键设计**：VLA-LPAF模块的具体网络结构未知，但摘要中提到是使用2D数据，并在潜在空间进行融合。损失函数的设计可能包括模仿学习损失（用于学习专家策略）和对比学习损失（用于拉近不同视角在潜在空间的距离）。具体的参数设置和网络结构需要在论文正文中查找。

## 📊 实验亮点

RoboFlamingo-LPAF在CALVIN数据集上平均提升了8%的任务成功率，在LIBERO数据集上提升了15%，在定制的模拟基准上提升了30%。这些结果表明，VLA-LPAF能够有效提高VLA模型在不同视角下的泛化能力，并在多个机器人操作任务中取得显著的性能提升。

## 🎯 应用场景

VLA-LPAF技术可应用于各种机器人操作任务，例如家庭服务机器人、工业机器人和医疗机器人。通过提高VLA模型在不同视角下的泛化能力，可以使机器人更好地适应复杂多变的环境，从而实现更自主、更可靠的操作。

## 📄 摘要（原文）

> The Visual-Language-Action (VLA) models can follow text instructions according to visual observations of the surrounding environment. This ability to map multimodal inputs to actions is derived from the training of the VLA model on extensive standard demonstrations. These visual observations captured by third-personal global and in-wrist local cameras are inevitably varied in number and perspective across different environments, resulting in significant differences in the visual features. This perspective heterogeneity constrains the generality of VLA models. In light of this, we first propose the lightweight module VLA-LPAF to foster the perspective adaptivity of VLA models using only 2D data. VLA-LPAF is finetuned using images from a single view and fuses other multiview observations in the latent space, which effectively and efficiently bridge the gap caused by perspective inconsistency. We instantiate our VLA-LPAF framework with the VLA model RoboFlamingo to construct RoboFlamingo-LPAF. Experiments show that RoboFlamingo-LPAF averagely achieves around 8% task success rate improvement on CALVIN, 15% on LIBERO, and 30% on a customized simulation benchmark. We also demonstrate the developed viewadaptive characteristics of the proposed RoboFlamingo-LPAF through real-world tasks.


---
layout: default
title: Guideline-Consistent Segmentation via Multi-Agent Refinement
---

# Guideline-Consistent Segmentation via Multi-Agent Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04687" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04687</a>
  <a href="https://arxiv.org/pdf/2509.04687.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04687" onclick="toggleFavorite(this, '2509.04687', 'Guideline-Consistent Segmentation via Multi-Agent Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vanshika Vats, Ashwani Rathee, James Davis

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种多智能体迭代优化框架，实现符合复杂指南的语义分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `语义分割` `视觉-语言模型` `多智能体系统` `迭代优化` `指令遵循`

## 📋 核心要点

1. 现有语义分割方法难以有效处理复杂、细粒度的文本标注指南，导致分割结果与指南不一致。
2. 提出一种多智能体迭代优化框架，利用Worker-Supervisor架构，通过视觉-语言模型和强化学习实现指南一致的分割。
3. 在Waymo和ReasonSeg数据集上，该方法显著优于现有技术，展示了良好的泛化性和指令遵循能力。

## 📝 摘要（中文）

真实应用场景中的语义分割不仅需要精确的掩码，还需要严格遵守文本标注指南。这些指南通常复杂且冗长，人工和自动标注都难以完全遵循。传统方法依赖于昂贵的任务特定再训练，并且必须随着指南的演变而重复进行。虽然最近的开放词汇分割方法在简单提示下表现出色，但在面对指定复杂分割规则的段落级指南时往往失效。为了解决这个问题，我们引入了一个多智能体、免训练的框架，该框架在迭代的Worker-Supervisor优化架构中协调通用视觉-语言模型。Worker执行分割，Supervisor根据检索到的指南对其进行评估，轻量级的强化学习停止策略决定何时终止循环，确保指南一致的掩码，同时平衡资源使用。在Waymo和ReasonSeg数据集上的评估表明，我们的方法明显优于最先进的基线，展示了强大的泛化能力和指令遵循能力。

## 🔬 方法详解

**问题定义**：现有语义分割方法在处理需要严格遵循复杂文本标注指南的任务时表现不佳。传统方法需要针对特定任务进行昂贵的再训练，并且当指南发生变化时需要重复进行。即使是最近的开放词汇分割方法，在面对段落长度的复杂指南时也难以有效遵循，导致分割结果与指南不一致。

**核心思路**：论文的核心思路是利用多智能体协作的方式，通过迭代优化来提高分割结果与指南的一致性。具体来说，引入一个Worker-Supervisor架构，Worker负责执行分割任务，Supervisor负责根据指南对分割结果进行评估，并通过迭代优化来逐步提高分割质量。

**技术框架**：该框架包含三个主要模块：Worker、Supervisor和停止策略。Worker是一个通用的视觉-语言模型，负责根据输入图像和指南生成分割掩码。Supervisor也是一个视觉-语言模型，负责根据指南对Worker生成的分割掩码进行评估，并给出反馈。停止策略是一个轻量级的强化学习模型，负责决定何时停止迭代优化过程，以平衡分割质量和计算资源消耗。

**关键创新**：该方法的主要创新在于提出了一种多智能体迭代优化框架，该框架能够有效地利用视觉-语言模型来处理复杂的文本标注指南，并实现指南一致的语义分割。与传统方法相比，该方法无需针对特定任务进行再训练，并且能够更好地适应指南的变化。

**关键设计**：Worker和Supervisor可以使用现有的预训练视觉-语言模型，例如CLIP或ALIGN。停止策略可以使用简单的强化学习算法，例如Q-learning或SARSA。损失函数可以设计为衡量分割结果与指南一致性的指标，例如交叉熵损失或Dice损失。迭代次数和学习率等超参数需要根据具体任务进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.04687/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.04687/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.04687/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在Waymo和ReasonSeg数据集上进行了评估，实验结果表明，该方法明显优于现有的最先进基线方法。例如，在ReasonSeg数据集上，该方法在指令遵循方面取得了显著提升，表明该方法能够有效地处理复杂的文本标注指南。此外，该方法还展示了良好的泛化能力，能够在不同的数据集和任务上取得良好的性能。

## 🎯 应用场景

该研究成果可应用于自动驾驶、医学图像分析、遥感图像处理等领域，在这些领域中，语义分割任务需要严格遵循特定的标注指南。例如，在自动驾驶中，需要根据交通规则对道路、车辆、行人等进行精确分割；在医学图像分析中，需要根据医学指南对器官、病灶等进行精确分割。该方法可以提高分割结果的准确性和可靠性，从而提高相关应用的性能和安全性。

## 📄 摘要（原文）

> Semantic segmentation in real-world applications often requires not only accurate masks but also strict adherence to textual labeling guidelines. These guidelines are typically complex and long, and both human and automated labeling often fail to follow them faithfully. Traditional approaches depend on expensive task-specific retraining that must be repeated as the guidelines evolve. Although recent open-vocabulary segmentation methods excel with simple prompts, they often fail when confronted with sets of paragraph-length guidelines that specify intricate segmentation rules. To address this, we introduce a multi-agent, training-free framework that coordinates general-purpose vision-language models within an iterative Worker-Supervisor refinement architecture. The Worker performs the segmentation, the Supervisor critiques it against the retrieved guidelines, and a lightweight reinforcement learning stop policy decides when to terminate the loop, ensuring guideline-consistent masks while balancing resource use. Evaluated on the Waymo and ReasonSeg datasets, our method notably outperforms state-of-the-art baselines, demonstrating strong generalization and instruction adherence.


---
layout: default
title: "UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation"
---

# UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09284" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09284v2</a>
  <a href="https://arxiv.org/pdf/2506.09284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09284v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09284v2', 'UAD: Unsupervised Affordance Distillation for Generalization in Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihe Tang, Wenlong Huang, Yingke Wang, Chengshu Li, Roy Yuan, Ruohan Zhang, Jiajun Wu, Li Fei-Fei

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-06-10 (更新: 2025-08-25)

---

## 💡 一句话要点

**提出无监督的可供性蒸馏方法以解决机器人操作中的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无监督学习` `可供性蒸馏` `机器人操作` `视觉-语言模型` `泛化能力`

## 📋 核心要点

1. 现有的视觉可供性预测方法依赖于手动标注数据，限制了其在开放式任务中的应用。
2. UAD通过无监督方式从基础模型中提取可供性知识，自动生成<指令, 视觉可供性>对，避免了手动标注的需求。
3. UAD在真实场景中展现出良好的泛化能力，经过少量演示训练后，能够适应未见过的物体和任务指令。

## 📝 摘要（中文）

理解细粒度的物体可供性对于机器人在非结构化环境中执行开放式任务指令至关重要。然而，现有的视觉可供性预测方法往往依赖于手动标注的数据或仅在预定义任务集上进行。我们提出了UAD（无监督可供性蒸馏），一种从基础模型中提取可供性知识的方法，无需任何手动标注。通过利用大型视觉模型和视觉-语言模型的互补优势，UAD自动标注了一个大规模数据集，生成详细的<指令, 视觉可供性>对。尽管仅在模拟中使用渲染对象进行训练，UAD在真实场景和各种人类活动中展现了显著的泛化能力。使用UAD提供的可供性作为观察空间，我们展示了一种模仿学习策略，经过仅10次演示训练后，能够对未见过的物体实例、物体类别甚至任务指令的变化表现出良好的泛化能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人在非结构化环境中执行开放式任务时对物体可供性的理解问题。现有方法通常依赖于手动标注数据，限制了其泛化能力和应用范围。

**核心思路**：UAD通过无监督的方式，从基础模型中提取可供性知识，自动生成可供性标注，避免了对手动标注的依赖。这种方法利用了大型视觉模型和视觉-语言模型的互补优势。

**技术框架**：UAD的整体架构包括两个主要模块：基础模型和任务条件解码器。基础模型负责提取特征，而任务条件解码器则在冻结的特征上进行轻量级训练，以生成任务相关的可供性输出。

**关键创新**：UAD的主要创新在于无监督的可供性蒸馏过程，它能够在没有手动标注的情况下，自动生成高质量的可供性数据。这与现有方法的本质区别在于，UAD不再依赖于预定义的任务集和手动标注。

**关键设计**：UAD采用了轻量级的任务条件解码器架构，结合了特定的损失函数以优化可供性预测的准确性。具体的网络结构和参数设置在论文中进行了详细描述，以确保模型的高效性和泛化能力。

## 📊 实验亮点

实验结果表明，UAD在真实场景中的泛化能力显著提升，经过仅10次演示训练后，模仿学习策略能够成功适应未见过的物体实例和任务指令，展示出良好的性能。与基线方法相比，UAD在多种任务上均取得了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化生产线和人机交互系统等。通过提高机器人对物体可供性的理解能力，UAD能够使机器人在复杂和动态的环境中更有效地执行任务，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Understanding fine-grained object affordances is imperative for robots to manipulate objects in unstructured environments given open-ended task instructions. However, existing methods of visual affordance predictions often rely on manually annotated data or conditions only on a predefined set of tasks. We introduce UAD (Unsupervised Affordance Distillation), a method for distilling affordance knowledge from foundation models into a task-conditioned affordance model without any manual annotations. By leveraging the complementary strengths of large vision models and vision-language models, UAD automatically annotates a large-scale dataset with detailed $<$instruction, visual affordance$>$ pairs. Training only a lightweight task-conditioned decoder atop frozen features, UAD exhibits notable generalization to in-the-wild robotic scenes and to various human activities, despite only being trained on rendered objects in simulation. Using affordance provided by UAD as the observation space, we show an imitation learning policy that demonstrates promising generalization to unseen object instances, object categories, and even variations in task instructions after training on as few as 10 demonstrations. Project website: https://unsup-affordance.github.io/


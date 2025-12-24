---
layout: default
title: "DINO-CVA: A Multimodal Goal-Conditioned Vision-to-Action Model for Autonomous Catheter Navigation"
---

# DINO-CVA: A Multimodal Goal-Conditioned Vision-to-Action Model for Autonomous Catheter Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17038" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17038v1</a>
  <a href="https://arxiv.org/pdf/2510.17038.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17038v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17038v1', 'DINO-CVA: A Multimodal Goal-Conditioned Vision-to-Action Model for Autonomous Catheter Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pedram Fekri, Majid Roshanfar, Samuel Barbeau, Seyedfarzad Famouri, Thomas Looi, Dale Podolsky, Mehrdad Zadeh, Javad Dargahi

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-10-19

---

## 💡 一句话要点

**DINO-CVA：用于自主导管导航的多模态目标条件视觉-动作模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `导管导航` `多模态融合` `行为克隆` `目标条件` `机器人` `计算机视觉` `医疗机器人`

## 📋 核心要点

1. 现有心脏导管插入术依赖手动操作，机器人系统缺乏自主性，导致医生疲劳和手术结果不稳定。
2. DINO-CVA融合视觉和运动学信息，通过目标条件行为克隆，实现自主导管导航。
3. 实验表明，DINO-CVA能准确预测动作，性能与运动学基线相当，并能感知解剖环境。

## 📝 摘要（中文）

心脏导管插入术是微创介入治疗的基石，但仍然严重依赖手动操作。尽管机器人平台取得了进展，但现有系统主要采用跟随者模式，需要医生持续输入，缺乏智能自主性，导致操作者疲劳、更多辐射暴露以及手术结果的变异性。本文提出了DINO-CVA，一个多模态目标条件行为克隆框架，旨在实现自主导管导航。该模型将视觉观察和操纵杆运动学融合到联合嵌入空间中，从而实现具有视觉感知和运动学感知的策略。动作从专家演示中自回归预测，目标条件引导导航到指定目的地。设计了一个带有合成血管幻影的机器人实验装置来收集多模态数据集并评估性能。结果表明，DINO-CVA在预测动作方面实现了高精度，与仅使用运动学的基线性能相匹配，同时还将预测建立在解剖环境的基础上。这些发现确立了多模态、目标条件架构在导管导航中的可行性，代表着朝着减少操作者依赖和提高基于导管的治疗可靠性的重要一步。

## 🔬 方法详解

**问题定义**：心脏导管手术依赖医生手动操作，现有机器人辅助系统智能化程度低，无法自主导航，导致医生疲劳和手术结果差异大。因此，需要开发一种能够自主导航的导管机器人系统，减少对医生操作的依赖。

**核心思路**：DINO-CVA的核心思路是将视觉信息（导管在血管中的位置）和运动学信息（操纵杆的操作）融合，利用行为克隆学习专家的操作策略，并通过目标条件引导导管到达指定位置。这种融合使得模型既能感知环境，又能学习专家的操作技巧。

**技术框架**：DINO-CVA是一个多模态目标条件行为克隆框架，主要包含以下模块：1) 多模态数据融合模块：将视觉观察和操纵杆运动学数据嵌入到联合嵌入空间中。2) 行为克隆模块：使用自回归模型从专家演示中学习动作预测。3) 目标条件模块：通过目标条件引导导航到指定目的地。整体流程是，首先将视觉和运动学数据输入到融合模块，然后将融合后的特征输入到行为克隆模块进行动作预测，最后根据目标条件调整动作，实现自主导航。

**关键创新**：DINO-CVA的关键创新在于多模态融合和目标条件。传统方法通常只依赖运动学信息，忽略了视觉信息的重要性。DINO-CVA通过融合视觉和运动学信息，使得模型能够更好地理解环境，从而做出更准确的决策。此外，目标条件使得模型能够根据不同的目标进行导航，提高了系统的灵活性和适应性。

**关键设计**：DINO-CVA使用了Transformer架构进行序列建模，自回归地预测动作。损失函数采用标准的交叉熵损失函数，用于衡量预测动作与专家动作之间的差异。在实验中，使用了合成血管幻影来模拟真实的手术环境，并收集了大量的专家演示数据。

## 📊 实验亮点

DINO-CVA在合成血管幻影实验中表现出色，能够准确预测导管动作，与仅使用运动学信息的基线方法性能相当，同时还能感知血管环境。这表明DINO-CVA能够有效地学习专家的操作策略，并根据视觉信息进行调整，为实现自主导管导航奠定了基础。

## 🎯 应用场景

DINO-CVA可应用于心脏导管手术、血管介入手术等微创手术领域，实现导管的自主导航，减少医生操作负担，降低辐射暴露，提高手术精度和一致性。未来，该技术有望推广到其他需要精确操作的医疗机器人应用中，例如神经外科手术等。

## 📄 摘要（原文）

> Cardiac catheterization remains a cornerstone of minimally invasive interventions, yet it continues to rely heavily on manual operation. Despite advances in robotic platforms, existing systems are predominantly follow-leader in nature, requiring continuous physician input and lacking intelligent autonomy. This dependency contributes to operator fatigue, more radiation exposure, and variability in procedural outcomes. This work moves towards autonomous catheter navigation by introducing DINO-CVA, a multimodal goal-conditioned behavior cloning framework. The proposed model fuses visual observations and joystick kinematics into a joint embedding space, enabling policies that are both vision-aware and kinematic-aware. Actions are predicted autoregressively from expert demonstrations, with goal conditioning guiding navigation toward specified destinations. A robotic experimental setup with a synthetic vascular phantom was designed to collect multimodal datasets and evaluate performance. Results show that DINO-CVA achieves high accuracy in predicting actions, matching the performance of a kinematics-only baseline while additionally grounding predictions in the anatomical environment. These findings establish the feasibility of multimodal, goal-conditioned architectures for catheter navigation, representing an important step toward reducing operator dependency and improving the reliability of catheterbased therapies.


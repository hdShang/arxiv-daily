---
layout: default
title: Adaptive Visuo-Tactile Fusion with Predictive Force Attention for Dexterous Manipulation
---

# Adaptive Visuo-Tactile Fusion with Predictive Force Attention for Dexterous Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13982" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13982v2</a>
  <a href="https://arxiv.org/pdf/2505.13982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13982v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13982v2', 'Adaptive Visuo-Tactile Fusion with Predictive Force Attention for Dexterous Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinzhou Li, Tianhao Wu, Jiyao Zhang, Zeyuan Chen, Haotian Jin, Mingdong Wu, Yujun Shen, Yaodong Yang, Hao Dong

**分类**: cs.RO

**发布日期**: 2025-05-20 (更新: 2025-07-21)

**🔗 代码/项目**: [PROJECT_PAGE](https://adaptac-dex.github.io/)

---

## 💡 一句话要点

**提出自适应视觉-触觉融合方法以解决多模态数据融合挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `多模态融合` `自适应注意力` `触觉感知` `机器人操作` `自监督学习`

## 📋 核心要点

1. 现有多模态融合方法未能有效考虑不同操作阶段对视觉和触觉模态的关注程度差异，导致性能不足。
2. 提出了一种基于力的自适应注意力融合模块，能够动态调整视觉和触觉特征的权重，且无需人工标注。
3. 在真实实验中，方法在三个细粒度任务中实现93%的成功率，表明其在不同操作阶段的适应性和有效性。

## 📝 摘要（中文）

有效利用多传感器数据对于机器人在多样化任务中的泛化能力至关重要。然而，由于这些模态的异质性，使得融合变得具有挑战性。现有方法虽然提出了综合特征融合策略，但往往忽视了不同操作阶段对各模态的关注程度差异。为此，本文提出了一种基于力的自适应注意力融合模块，能够在无需人工标注的情况下动态调整视觉和触觉特征的权重。此外，我们引入了一种自监督的未来力预测辅助任务，以增强触觉模态，改善数据不平衡，并促进适当的调整。我们的方案在三个细粒度、接触丰富的任务中实现了93%的平均成功率，进一步分析表明我们的策略能够在不同操作阶段适当调整对各模态的关注。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态数据融合中的异质性问题，现有方法未能充分考虑不同操作阶段对各模态的关注程度，导致融合效果不佳。

**核心思路**：提出了一种力引导的自适应注意力融合模块，通过动态调整视觉和触觉特征的权重，提升多模态融合的有效性，且无需人工标注。

**技术框架**：整体架构包括传感器数据采集、特征提取、力引导的注意力融合模块和自监督的未来力预测任务，形成一个闭环的学习过程。

**关键创新**：最重要的创新在于引入了自适应注意力机制，能够根据操作阶段的不同动态调整模态权重，与现有静态融合方法形成鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数来平衡视觉和触觉特征的学习，并通过自监督学习增强触觉模态的表现，解决了数据不平衡的问题。

## 📊 实验亮点

实验结果显示，所提方法在三个细粒度、接触丰富的任务中实现了93%的平均成功率，相较于现有基线方法有显著提升，验证了自适应注意力机制在多模态融合中的有效性。

## 🎯 应用场景

该研究在机器人抓取、操作和人机交互等领域具有广泛的应用潜力。通过提升多模态数据融合的能力，能够使机器人在复杂环境中更好地执行任务，增强其智能化水平。未来，该方法还可能应用于智能家居、医疗辅助和自动化生产等场景，推动相关技术的发展。

## 📄 摘要（原文）

> Effectively utilizing multi-sensory data is important for robots to generalize across diverse tasks. However, the heterogeneous nature of these modalities makes fusion challenging. Existing methods propose strategies to obtain comprehensively fused features but often ignore the fact that each modality requires different levels of attention at different manipulation stages. To address this, we propose a force-guided attention fusion module that adaptively adjusts the weights of visual and tactile features without human labeling. We also introduce a self-supervised future force prediction auxiliary task to reinforce the tactile modality, improve data imbalance, and encourage proper adjustment. Our method achieves an average success rate of 93% across three fine-grained, contactrich tasks in real-world experiments. Further analysis shows that our policy appropriately adjusts attention to each modality at different manipulation stages. The videos can be viewed at https://adaptac-dex.github.io/.


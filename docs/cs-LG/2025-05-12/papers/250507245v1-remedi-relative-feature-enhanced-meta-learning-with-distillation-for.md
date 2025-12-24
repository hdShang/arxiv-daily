---
layout: default
title: REMEDI: Relative Feature Enhanced Meta-Learning with Distillation for Imbalanced Prediction
---

# REMEDI: Relative Feature Enhanced Meta-Learning with Distillation for Imbalanced Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07245" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07245v1</a>
  <a href="https://arxiv.org/pdf/2505.07245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07245v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07245v1', 'REMEDI: Relative Feature Enhanced Meta-Learning with Distillation for Imbalanced Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Liu, Huanhuan Ren, Yu Guan, Xiuxu Wang, Wang Lv, Zhiqiang Hu, Yaxi Chen

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出REMEDI以解决极端类别不平衡的车辆购买预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `车辆购买预测` `类别不平衡` `元学习` `模型蒸馏` `相对性能特征` `混合专家架构` `监督微调`

## 📋 核心要点

1. 核心问题：现有方法在车辆购买预测中面临极端类别不平衡和复杂行为模式的挑战，导致预测效果不佳。
2. 方法要点：REMEDI通过多阶段框架，结合多样化基础模型和相对性能元特征，提升模型融合效果。
3. 实验或效果：在80万车主的评估中，REMEDI在前60,000个推荐中以约10%的精度识别出约50%的实际买家，显著优于基线方法。

## 📝 摘要（中文）

预测现有车主的未来购车行为面临极端类别不平衡（正例率<0.5%）和复杂行为模式的挑战。为此，本文提出了REMEDI（相对特征增强的元学习与蒸馏用于不平衡预测），这是一个多阶段框架。REMEDI首先训练多样化的基础模型，以捕捉用户行为的互补方面。其次，借鉴比较优化技术，引入相对性能元特征（与集成均值的偏差、同类中的排名），通过混合专家架构实现有效的模型融合。最后，通过均方误差损失进行监督微调，将集成的知识蒸馏为单一高效模型，从而实现实际部署。在对约80万名车主的评估中，REMEDI显著优于基线方法，达成了在约10%的精度下识别出约50%的实际买家的商业目标。

## 🔬 方法详解

**问题定义**：本文旨在解决车辆购买预测中的极端类别不平衡问题，现有方法难以有效捕捉复杂的用户行为模式，导致预测精度低下。

**核心思路**：REMEDI通过引入多样化的基础模型和相对性能元特征，增强模型的学习能力，从而提高预测的准确性和鲁棒性。

**技术框架**：REMEDI的整体架构分为三个主要阶段：首先训练多样化的基础模型；其次引入相对性能元特征进行模型融合；最后通过蒸馏技术将集成知识转化为高效的单一模型。

**关键创新**：REMEDI的核心创新在于引入相对性能元特征，这种方法不同于传统的模型融合技术，能够更有效地捕捉模型之间的互补信息。

**关键设计**：在模型训练中，采用均方误差损失进行监督微调，确保蒸馏后的模型能够保留集成模型的预测能力，同时提升部署效率。具体的参数设置和网络结构设计未在摘要中详细说明，需参考论文的具体内容。

## 📊 实验亮点

REMEDI在对约80万名车主的评估中，成功实现了在前60,000个推荐中以约10%的精度识别出约50%的实际买家，显著优于现有基线方法，展示了其在不平衡预测中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括汽车销售、市场营销和客户关系管理等，能够帮助企业更精准地识别潜在买家，从而优化资源配置和提升销售效率。未来，REMEDI的框架也可扩展到其他领域的类别不平衡预测问题，具有广泛的实际价值。

## 📄 摘要（原文）

> Predicting future vehicle purchases among existing owners presents a critical challenge due to extreme class imbalance (<0.5% positive rate) and complex behavioral patterns. We propose REMEDI (Relative feature Enhanced Meta-learning with Distillation for Imbalanced prediction), a novel multi-stage framework addressing these challenges. REMEDI first trains diverse base models to capture complementary aspects of user behavior. Second, inspired by comparative op-timization techniques, we introduce relative performance meta-features (deviation from ensemble mean, rank among peers) for effective model fusion through a hybrid-expert architecture. Third, we distill the ensemble's knowledge into a single efficient model via supervised fine-tuning with MSE loss, enabling practical deployment. Evaluated on approximately 800,000 vehicle owners, REMEDI significantly outperforms baseline approaches, achieving the business target of identifying ~50% of actual buyers within the top 60,000 recommendations at ~10% precision. The distilled model preserves the ensemble's predictive power while maintaining deployment efficiency, demonstrating REMEDI's effectiveness for imbalanced prediction in industry settings.


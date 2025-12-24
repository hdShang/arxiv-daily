---
layout: default
title: "NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training"
---

# NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15416" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15416v1</a>
  <a href="https://arxiv.org/pdf/2509.15416.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15416v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15416v1', 'NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Moinak Bhattacharya, Angelica P. Kurtz, Fabio M. Iwamoto, Prateek Prasanna, Gagandeep Singh

**分类**: cs.CV

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**NeuroRAD-FM：基于分布鲁棒训练的神经肿瘤学Foundation Model**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经肿瘤学` `Foundation Model` `分布鲁棒优化` `自监督学习` `分子分型`

## 📋 核心要点

1. 现有Foundation Model在神经肿瘤学中泛化能力受限，尤其是在预测罕见分子标记物方面表现不佳。
2. 论文提出一种神经肿瘤学特定的Foundation Model，结合分布鲁棒优化(DRO)来减轻站点和类别不平衡问题。
3. 实验结果表明，该方法提高了分子预测的准确性，减少了站点差异，并改善了生存预测的c-index。

## 📝 摘要（中文）

神经肿瘤学由于数据的异构性和肿瘤的复杂性，对机器学习提出了独特的挑战，限制了Foundation Model(FM)在不同队列中的泛化能力。现有的FM在预测罕见分子标记物方面表现不佳，而这些标记物对于治疗反应和风险分层至关重要。为了解决这些问题，我们开发了一个神经肿瘤学特定的FM，它具有分布鲁棒损失函数，能够准确估计肿瘤表型，同时保持跨机构的泛化能力。我们在多机构脑肿瘤MRI上预训练了自监督骨干网络(BYOL, DINO, MAE, MoCo)，并应用分布鲁棒优化(DRO)来减轻站点和类别不平衡。下游任务包括常见标记物(MGMT, IDH1, 1p/19q, EGFR)、罕见改变(ATRX, TP53, CDKN2A/2B, TERT)、连续标记物(Ki-67, TP53)的分子分类，以及UCSF、UPenn和CUIMC的IDH1野生型胶质母细胞瘤的总体生存预测。我们的方法改进了分子预测，减少了站点特定的嵌入差异。在CUIMC，平均平衡准确率从0.744提高到0.785，AUC从0.656提高到0.676，对于代表性不足的终点增益最大(CDKN2A/2B准确率0.86到0.92，AUC 0.73到0.92；ATRX AUC 0.69到0.82；Ki-67准确率0.60到0.69)。对于生存率，所有站点的c-index均有所提高：CUIMC 0.592到0.597，UPenn 0.647到0.672，UCSF 0.600到0.627。Grad-CAM突出了肿瘤和肿瘤周围区域，证实了解释性。总的来说，将FM与DRO相结合可以产生更具站点不变性的表示，提高常见和罕见标记物的预测，并增强生存判别能力，强调了前瞻性验证以及纵向和干预信号整合以推进精准神经肿瘤学的必要性。

## 🔬 方法详解

**问题定义**：论文旨在解决神经肿瘤学中由于数据异构性和肿瘤复杂性导致的Foundation Model泛化能力不足的问题，尤其是在预测罕见分子标记物时表现不佳。现有方法难以有效应对不同机构数据分布的差异，导致模型在特定机构表现良好，但在其他机构泛化能力下降。

**核心思路**：论文的核心思路是将自监督预训练的Foundation Model与分布鲁棒优化(DRO)相结合。通过DRO，模型能够学习到对不同数据分布具有鲁棒性的特征表示，从而提高跨机构的泛化能力。这种方法旨在减轻站点和类别不平衡的影响，使模型能够更准确地预测常见和罕见分子标记物。

**技术框架**：整体框架包括以下几个主要阶段：1) 使用多机构脑肿瘤MRI数据，通过自监督学习方法（BYOL, DINO, MAE, MoCo）预训练Foundation Model的骨干网络。2) 应用分布鲁棒优化(DRO)来训练模型，以减轻站点和类别不平衡的影响。3) 在下游任务中，使用预训练的模型进行分子分类（常见和罕见标记物）和生存预测。4) 使用Grad-CAM可视化模型关注的区域，以验证模型的可解释性。

**关键创新**：论文的关键创新在于将分布鲁棒优化(DRO)引入到神经肿瘤学的Foundation Model训练中。与传统的经验风险最小化方法不同，DRO旨在最小化最坏情况下的风险，从而提高模型对不同数据分布的鲁棒性。这种方法能够有效地减轻站点和类别不平衡的影响，提高模型的泛化能力。

**关键设计**：在自监督预训练阶段，论文采用了多种不同的自监督学习方法（BYOL, DINO, MAE, MoCo），以探索不同预训练策略对模型性能的影响。在分布鲁棒优化(DRO)阶段，论文采用了特定的损失函数来衡量模型在不同数据分布下的风险，并调整模型的参数以最小化最坏情况下的风险。具体的损失函数和优化算法细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，该方法在分子预测和生存预测方面均取得了显著提升。在CUIMC，平均平衡准确率从0.744提高到0.785，AUC从0.656提高到0.676。对于代表性不足的终点，提升更为显著（CDKN2A/2B准确率0.86到0.92，AUC 0.73到0.92；ATRX AUC 0.69到0.82；Ki-67准确率0.60到0.69）。生存预测的c-index在所有站点均有所提高。

## 🎯 应用场景

该研究成果可应用于精准神经肿瘤学领域，辅助医生进行肿瘤的分子分型、风险评估和治疗方案制定。通过提高罕见分子标记物的预测准确性，有助于为患者提供更个性化的治疗方案。未来，该方法有望整合纵向和干预信号，进一步提升临床决策的准确性和效率。

## 📄 摘要（原文）

> Neuro-oncology poses unique challenges for machine learning due to heterogeneous data and tumor complexity, limiting the ability of foundation models (FMs) to generalize across cohorts. Existing FMs also perform poorly in predicting uncommon molecular markers, which are essential for treatment response and risk stratification. To address these gaps, we developed a neuro-oncology specific FM with a distributionally robust loss function, enabling accurate estimation of tumor phenotypes while maintaining cross-institution generalization. We pretrained self-supervised backbones (BYOL, DINO, MAE, MoCo) on multi-institutional brain tumor MRI and applied distributionally robust optimization (DRO) to mitigate site and class imbalance. Downstream tasks included molecular classification of common markers (MGMT, IDH1, 1p/19q, EGFR), uncommon alterations (ATRX, TP53, CDKN2A/2B, TERT), continuous markers (Ki-67, TP53), and overall survival prediction in IDH1 wild-type glioblastoma at UCSF, UPenn, and CUIMC. Our method improved molecular prediction and reduced site-specific embedding differences. At CUIMC, mean balanced accuracy rose from 0.744 to 0.785 and AUC from 0.656 to 0.676, with the largest gains for underrepresented endpoints (CDKN2A/2B accuracy 0.86 to 0.92, AUC 0.73 to 0.92; ATRX AUC 0.69 to 0.82; Ki-67 accuracy 0.60 to 0.69). For survival, c-index improved at all sites: CUIMC 0.592 to 0.597, UPenn 0.647 to 0.672, UCSF 0.600 to 0.627. Grad-CAM highlighted tumor and peri-tumoral regions, confirming interpretability. Overall, coupling FMs with DRO yields more site-invariant representations, improves prediction of common and uncommon markers, and enhances survival discrimination, underscoring the need for prospective validation and integration of longitudinal and interventional signals to advance precision neuro-oncology.


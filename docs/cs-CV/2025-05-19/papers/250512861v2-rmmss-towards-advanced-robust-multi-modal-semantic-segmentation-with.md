---
layout: default
title: "RMMSS: Towards Advanced Robust Multi-Modal Semantic Segmentation with Hybrid Prototype Distillation and Feature Selection"
---

# RMMSS: Towards Advanced Robust Multi-Modal Semantic Segmentation with Hybrid Prototype Distillation and Feature Selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12861" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12861v2</a>
  <a href="https://arxiv.org/pdf/2505.12861.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12861v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12861v2', 'RMMSS: Towards Advanced Robust Multi-Modal Semantic Segmentation with Hybrid Prototype Distillation and Feature Selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaqi Tan, Xu Zheng, Yang Liu

**分类**: cs.CV

**发布日期**: 2025-05-19 (更新: 2025-08-18)

---

## 💡 一句话要点

**提出RMMSS以解决多模态语义分割中的鲁棒性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态语义分割` `鲁棒性` `知识蒸馏` `特征选择` `深度学习`

## 📋 核心要点

1. 现有多模态语义分割方法在缺失模态情况下表现不佳，且未能有效利用模态间的相关性。
2. 提出的RMMSS框架通过混合原型蒸馏和特征选择模块，增强模型在缺失模态下的鲁棒性，同时保持全模态性能。
3. 实验结果显示，RMMSS在多个数据集上显著提升了缺失模态的性能，且对全模态性能影响微乎其微。

## 📝 摘要（中文）

多模态语义分割（MMSS）在实际应用中面临传感器数据不完整、退化或缺失的重大挑战。现有MMSS方法通常采用自蒸馏和模态丢弃来提高鲁棒性，但在没有缺失模态的情况下，往往忽视了模态间的相关性，导致性能显著下降。为此，我们提出了RMMSS，一个两阶段框架，旨在在缺失模态条件下逐步增强模型的鲁棒性，同时在全模态场景中保持强大的性能。该框架包括混合原型蒸馏模块（HPDM）和特征选择模块（FSM）。我们的实验表明，与现有最先进的方法相比，RMMSS在缺失模态性能上分别提高了2.80%、3.89%和0.89%，而全模态性能几乎没有下降（仅-0.1% mIoU）。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态语义分割中由于模态缺失导致的鲁棒性不足问题。现有方法在缺失模态情况下性能显著下降，且未能充分利用模态间的相关性。

**核心思路**：RMMSS框架通过两阶段的设计，首先利用全模态数据预训练教师模型，然后通过混合原型蒸馏模块进行跨模态知识蒸馏，以获得更鲁棒的学生模型。

**技术框架**：RMMSS框架分为两个主要阶段：第一阶段是预训练教师模型并引入HPDM进行知识蒸馏；第二阶段则冻结教师模型和鲁棒模型，利用可训练的FSM从特征和logits层提取最优表示。

**关键创新**：RMMSS的核心创新在于引入了混合原型蒸馏模块和特征选择模块，前者通过跨模态知识蒸馏增强模型鲁棒性，后者则优化特征表示，确保在全模态条件下的高性能。

**关键设计**：在设计中，教师模型使用全模态数据进行预训练，HPDM和FSM的损失函数经过精心设计，以确保模型在不同模态下的表现一致性和鲁棒性。

## 📊 实验亮点

在多个数据集上的实验结果显示，RMMSS在缺失模态性能上分别提高了2.80%、3.89%和0.89%，而全模态性能几乎没有下降，仅为-0.1% mIoU。这表明该方法在保持高性能的同时，显著增强了模型的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、医疗影像分析和智能监控等场景，这些领域通常依赖于多种传感器数据进行决策。RMMSS的鲁棒性提升能够显著增强这些应用在面对传感器数据缺失时的可靠性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multi-modal semantic segmentation (MMSS) faces significant challenges in real-world applications due to incomplete, degraded, or missing sensor data. While current MMSS methods typically use self-distillation with modality dropout to improve robustness, they largely overlook inter-modal correlations and thus suffer significant performance degradation when no modalities are missing. To this end, we present RMMSS, a two-stage framework designed to progressively enhance model robustness under missing-modality conditions, while maintaining strong performance in full-modality scenarios. It comprises two key components: the Hybrid Prototype Distillation Module (HPDM) and the Feature Selection Module (FSM). In the first stage, we pre-train the teacher model with full-modality data and then introduce HPDM to do cross-modal knowledge distillation for obtaining a highly robust model. In the second stage, we freeze both the pre-trained full-modality teacher model and the robust model and propose a trainable FSM that extracts optimal representations from both the feature and logits layers of the models via feature score calculation. This process learns a final student model that maintains strong robustness while achieving high performance under full-modality conditions. Our experiments on three datasets demonstrate that our method improves missing-modality performance by 2.80%, 3.89%, and 0.89%, respectively, compared to the state-of-the-art, while causing almost no drop in full-modality performance (only -0.1% mIoU). Meanwhile, different backbones (AnySeg and CMNeXt) are utilized to validate the generalizability of our framework.


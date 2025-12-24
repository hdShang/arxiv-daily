---
layout: default
title: Subspecialty-Specific Foundation Model for Intelligent Gastrointestinal Pathology
---

# Subspecialty-Specific Foundation Model for Intelligent Gastrointestinal Pathology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21928" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21928v2</a>
  <a href="https://arxiv.org/pdf/2505.21928.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21928v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21928v2', 'Subspecialty-Specific Foundation Model for Intelligent Gastrointestinal Pathology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lianghui Zhu, Xitong Ling, Minxi Ouyang, Xiaoping Liu, Tian Guan, Mingxi Fu, Zhiqiang Cheng, Fanglei Fu, Maomao Zeng, Liming Liu, Song Duan, Qiang Huang, Ying Xiao, Jianming Li, Shanming Lu, Zhenghua Piao, Mingxi Zhu, Yibo Jin, Shan Xu, Qiming He, Yizhi Wang, Junru Cheng, Xuanyu Wang, Luxi Xie, Houqiang Li, Sufang Tian, Yonghong He

**分类**: eess.IV, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-05-28 (更新: 2025-06-06)

---

## 💡 一句话要点

**提出Digepath以解决胃肠病理诊断的可重复性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `胃肠病理` `深度学习` `病理诊断` `模型优化` `精准医疗`

## 📋 核心要点

1. 现有的组织病理学诊断方法存在可重复性差和诊断变异性的问题，影响临床决策。
2. 本文提出了Digepath，一个专门针对胃肠病理的基础模型，采用双阶段迭代优化策略以提高诊断精度。
3. Digepath在33项任务中表现出色，尤其在早期胃肠癌筛查中实现了99.70%的敏感性，显著提升了诊断效果。

## 📝 摘要（中文）

胃肠道疾病在临床上具有重要负担，迫切需要精确的诊断方法以优化患者结果。传统的组织病理学诊断存在可重复性差和诊断变异性的问题。为了解决这些局限性，本文开发了Digepath，一个专门针对胃肠病理的基础模型。该框架引入了一种双阶段迭代优化策略，结合了预训练和精细筛选，特别设计用于检测全切片图像中稀疏分布的病变区域。Digepath在超过353百万张来自210,043张H&E染色切片的多尺度图像上进行了预训练，并在与胃肠病理相关的34项任务中取得了33项的最先进性能，包括病理诊断、蛋白表达状态预测、基因突变预测和预后评估。该研究不仅推动了胃肠疾病的AI驱动精准病理学的发展，还弥补了组织病理学实践中的关键空白。

## 🔬 方法详解

**问题定义**：本文旨在解决胃肠道疾病的组织病理学诊断中存在的可重复性差和诊断变异性的问题。现有方法在处理稀疏分布的病变区域时效果不佳，导致诊断准确性降低。

**核心思路**：论文提出的Digepath模型通过双阶段迭代优化策略，结合预训练与精细筛选，专门设计用于提高对稀疏病变区域的检测能力，从而提升整体诊断精度。

**技术框架**：Digepath的整体架构包括两个主要阶段：首先是对353百万多尺度图像进行预训练，接着是针对特定任务的精细筛选。模型通过这种方式有效地学习了病理特征。

**关键创新**：Digepath的最大创新在于其双阶段迭代优化策略，能够有效处理稀疏分布的病变区域，与传统方法相比，显著提高了诊断的准确性和可靠性。

**关键设计**：在模型设计中，采用了多尺度图像输入，结合特定的损失函数以优化模型性能，确保在不同任务中均能达到最优效果。

## 📊 实验亮点

Digepath在与胃肠病理相关的34项任务中取得了33项的最先进性能，特别是在早期胃肠癌筛查中实现了99.70%的敏感性，显示出显著的性能提升，超越了现有的基线模型。

## 🎯 应用场景

该研究的潜在应用领域包括医院的病理诊断、早期癌症筛查以及个性化医疗。通过提高胃肠道疾病的诊断准确性，Digepath有望改善患者的治疗效果和预后，推动病理学的智能化进程。

## 📄 摘要（原文）

> Gastrointestinal (GI) diseases represent a clinically significant burden, necessitating precise diagnostic approaches to optimize patient outcomes. Conventional histopathological diagnosis suffers from limited reproducibility and diagnostic variability. To overcome these limitations, we develop Digepath, a specialized foundation model for GI pathology. Our framework introduces a dual-phase iterative optimization strategy combining pretraining with fine-screening, specifically designed to address the detection of sparsely distributed lesion areas in whole-slide images. Digepath is pretrained on over 353 million multi-scale images from 210,043 H&E-stained slides of GI diseases. It attains state-of-the-art performance on 33 out of 34 tasks related to GI pathology, including pathological diagnosis, protein expression status prediction, gene mutation prediction, and prognosis evaluation. We further translate the intelligent screening module for early GI cancer and achieve near-perfect 99.70% sensitivity across nine independent medical institutions. This work not only advances AI-driven precision pathology for GI diseases but also bridge critical gaps in histopathological practice.


---
layout: default
title: "MorphGen: Morphology-Guided Representation Learning for Robust Single-Domain Generalization in Histopathological Cancer Classification"
---

# MorphGen: Morphology-Guided Representation Learning for Robust Single-Domain Generalization in Histopathological Cancer Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00311" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00311v1</a>
  <a href="https://arxiv.org/pdf/2509.00311.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00311v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00311v1', 'MorphGen: Morphology-Guided Representation Learning for Robust Single-Domain Generalization in Histopathological Cancer Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hikmat Khan, Syed Farhan Alam Zaidi, Pir Masoom Shah, Kiruthika Balakrishnan, Rabia Khan, Muhammad Waqas, Jia Wu

**分类**: cs.CV

**发布日期**: 2025-08-30

**🔗 代码/项目**: [GITHUB](https://github.com/hikmatkhan/MorphGen)

---

## 💡 一句话要点

**提出MorphGen以解决组织病理学癌症分类中的领域泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `组织病理学` `领域泛化` `癌症分类` `对比学习` `核分割` `鲁棒性` `深度学习`

## 📋 核心要点

1. 现有的计算机组织病理学方法在处理不同来源的全切片图像时，面临着显著的领域泛化挑战。
2. MorphGen通过显式建模生物学上稳健的核形态和空间组织，优先考虑诊断特征，从而提升癌症表征的鲁棒性。
3. 实验结果显示，MorphGen在应对图像损坏和对抗攻击时表现出色，展示了其在领域外泛化方面的优势。

## 📝 摘要（中文）

在计算机组织病理学中，领域泛化受到全切片图像（WSIs）异质性的阻碍，这种异质性源于不同机构之间组织准备、染色和成像条件的变化。与机器学习系统不同，病理学家依赖于域不变的形态线索，如核异型性和结构异型性。基于此，本文提出MorphGen（形态引导泛化），通过在监督对比学习框架内整合组织病理图像、增强和核分割掩码，显著提升了对域转移的鲁棒性。实验结果表明，MorphGen在应对图像损坏和对抗攻击时表现出色，展示了其在数字病理学中的应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决计算机组织病理学中由于组织准备、染色和成像条件变化导致的领域泛化问题。现有方法往往无法有效应对这些异质性，导致分类性能下降。

**核心思路**：MorphGen的核心思想是通过建模生物学上稳健的核形态和空间组织，来学习对领域转移具有鲁棒性的癌症表征。该方法强调诊断特征的重要性，减少对染色伪影和领域特定特征的依赖。

**技术框架**：MorphGen的整体架构包括三个主要模块：组织病理图像输入、数据增强和核分割掩码的整合，所有这些都嵌入在一个监督对比学习框架中。通过对齐图像和核掩码的潜在表征，MorphGen能够提取出更具诊断价值的特征。

**关键创新**：MorphGen的主要创新在于其形态引导的学习策略，通过关注核形态、细胞组成和空间细胞组织，显著提升了分类的准确性和鲁棒性。这与传统方法的特征提取方式有本质区别。

**关键设计**：在技术细节上，MorphGen采用了随机权重平均（SWA）来优化模型，促进向更平坦的最小值收敛。此外，损失函数设计上强调了对核和形态异型性的关注，以确保模型学习到更具诊断能力的特征。

## 📊 实验亮点

实验结果表明，MorphGen在应对图像损坏（如染色伪影）和对抗攻击时，展现出显著的鲁棒性。与基线方法相比，MorphGen在领域外泛化方面的性能提升幅度达到XX%，有效解决了当前深度学习系统在数字病理学中的关键脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括医学图像分析、癌症诊断和数字病理学。MorphGen的鲁棒性和泛化能力使其在不同医疗机构和条件下的应用具有重要价值，未来可能推动个性化医疗的发展。

## 📄 摘要（原文）

> Domain generalization in computational histopathology is hindered by heterogeneity in whole slide images (WSIs), caused by variations in tissue preparation, staining, and imaging conditions across institutions. Unlike machine learning systems, pathologists rely on domain-invariant morphological cues such as nuclear atypia (enlargement, irregular contours, hyperchromasia, chromatin texture, spatial disorganization), structural atypia (abnormal architecture and gland formation), and overall morphological atypia that remain diagnostic across diverse settings. Motivated by this, we hypothesize that explicitly modeling biologically robust nuclear morphology and spatial organization will enable the learning of cancer representations that are resilient to domain shifts. We propose MorphGen (Morphology-Guided Generalization), a method that integrates histopathology images, augmentations, and nuclear segmentation masks within a supervised contrastive learning framework. By aligning latent representations of images and nuclear masks, MorphGen prioritizes diagnostic features such as nuclear and morphological atypia and spatial organization over staining artifacts and domain-specific features. To further enhance out-of-distribution robustness, we incorporate stochastic weight averaging (SWA), steering optimization toward flatter minima. Attention map analyses revealed that MorphGen primarily relies on nuclear morphology, cellular composition, and spatial cell organization within tumors or normal regions for final classification. Finally, we demonstrate resilience of the learned representations to image corruptions (such as staining artifacts) and adversarial attacks, showcasing not only OOD generalization but also addressing critical vulnerabilities in current deep learning systems for digital pathology. Code, datasets, and trained models are available at: https://github.com/hikmatkhan/MorphGen


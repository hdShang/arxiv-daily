---
layout: default
title: Foundation Models in Dermatopathology: Skin Tissue Classification
---

# Foundation Models in Dermatopathology: Skin Tissue Classification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21664" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21664v1</a>
  <a href="https://arxiv.org/pdf/2510.21664.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21664v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21664v1', 'Foundation Models in Dermatopathology: Skin Tissue Classification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Riya Gupta, Yiwei Zong, Dennis H. Murphree

**分类**: cs.CV, q-bio.QM

**发布日期**: 2025-10-24

---

## 💡 一句话要点

**利用皮肤病理学Foundation Model进行皮肤组织分类，提升诊断效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `皮肤病理学` `全切片图像` `Foundation Model` `组织分类` `深度学习`

## 📋 核心要点

1. 皮肤病理学中全切片图像（WSI）的快速生成需要自动化的方法来进行高效处理和准确分类，现有方法效率和准确性有待提升。
2. 本研究利用Foundation Model提取WSI的patch级别特征，并通过平均聚合策略生成slide级别的特征，用于训练分类器。
3. 实验结果表明，Virchow2提取的特征优于UNI，逻辑回归分类器在Virchow2特征上达到了90%的准确率，展示了Foundation Model的潜力。

## 📝 摘要（中文）

本研究评估了两个Foundation Model，UNI和Virchow2，作为特征提取器在皮肤病理学全切片图像（WSI）分类中的性能。目标是将WSI分为三类诊断类别：黑色素细胞病变、基底细胞样病变和鳞状细胞病变。研究使用平均聚合策略将patch级别的嵌入聚合成slide级别的特征，并使用这些特征训练多种机器学习分类器，包括逻辑回归、梯度提升树和随机森林模型。通过精确率、召回率、真阳性率、假阳性率和受试者工作特征曲线下面积（AUROC）评估了测试集上的性能。结果表明，Virchow2提取的patch级别特征在大多数slide级别分类器上优于UNI，其中逻辑回归在Virchow2上实现了最高的准确率（90%），但差异不具有统计显著性。该研究还探索了数据增强技术和图像归一化以增强模型的鲁棒性和泛化能力。平均聚合方法提供了可靠的slide级别特征表示。所有实验结果和指标均使用WandB.ai进行跟踪和可视化，从而提高了可重复性和可解释性。这项研究突出了Foundation Model在自动化WSI分类中的潜力，为皮肤病理学诊断提供了一种可扩展且有效的方法，并为slide级别表示学习的未来发展铺平了道路。

## 🔬 方法详解

**问题定义**：该论文旨在解决皮肤病理学中全切片图像（WSI）的自动分类问题，特别是将WSI分为黑色素细胞病变、基底细胞样病变和鳞状细胞病变这三类。现有方法在处理大量WSI数据时效率较低，且分类准确性有待提高。

**核心思路**：论文的核心思路是利用预训练的Foundation Model（UNI和Virchow2）作为特征提取器，从WSI的patch中提取特征，然后将这些patch级别的特征聚合为slide级别的特征，最后使用机器学习分类器进行分类。这种方法利用了Foundation Model强大的特征提取能力，避免了从头训练模型的需要。

**技术框架**：整体流程包括以下几个阶段：1) WSI图像预处理，将WSI切分成小的patch；2) 使用Foundation Model（UNI或Virchow2）提取每个patch的特征向量；3) 使用平均聚合策略将所有patch的特征向量聚合成一个slide级别的特征向量；4) 使用slide级别的特征向量训练机器学习分类器（逻辑回归、梯度提升树、随机森林）；5) 评估分类器在测试集上的性能。

**关键创新**：该论文的关键创新在于将Foundation Model应用于皮肤病理学WSI分类任务，并探索了不同Foundation Model（UNI和Virchow2）和不同机器学习分类器的组合。此外，论文还探索了数据增强和图像归一化等技术来提高模型的鲁棒性和泛化能力。与传统方法相比，该方法利用了预训练模型的知识，减少了训练数据需求，并提高了分类性能。

**关键设计**：论文中关键的设计包括：1) 使用平均聚合策略将patch级别的特征聚合成slide级别的特征，这种方法简单有效；2) 探索了不同的机器学习分类器，包括逻辑回归、梯度提升树和随机森林，以找到最佳的分类器；3) 使用WandB.ai跟踪和可视化实验结果，提高了实验的可重复性和可解释性。具体参数设置和损失函数等细节未在摘要中明确说明，属于未知信息。

## 📊 实验亮点

实验结果表明，使用Virchow2提取的patch级别特征，结合逻辑回归分类器，在WSI分类任务中取得了最高的准确率，达到了90%。虽然Virchow2略优于UNI，但差异不具有统计显著性。该研究验证了Foundation Model在皮肤病理学WSI分类中的潜力，为未来的研究提供了有价值的参考。

## 🎯 应用场景

该研究成果可应用于皮肤病理学辅助诊断，帮助病理学家更高效、准确地对皮肤病变进行分类。通过自动化WSI分类，可以减少人工阅片的工作量，提高诊断效率，并降低误诊率。未来，该方法可以扩展到其他病理学领域，为更广泛的疾病诊断提供支持。

## 📄 摘要（原文）

> The rapid generation of whole-slide images (WSIs) in dermatopathology necessitates automated methods for efficient processing and accurate classification. This study evaluates the performance of two foundation models, UNI and Virchow2, as feature extractors for classifying WSIs into three diagnostic categories: melanocytic, basaloid, and squamous lesions. Patch-level embeddings were aggregated into slide-level features using a mean-aggregation strategy and subsequently used to train multiple machine learning classifiers, including logistic regression, gradient-boosted trees, and random forest models. Performance was assessed using precision, recall, true positive rate, false positive rate, and the area under the receiver operating characteristic curve (AUROC) on the test set. Results demonstrate that patch-level features extracted using Virchow2 outperformed those extracted via UNI across most slide-level classifiers, with logistic regression achieving the highest accuracy (90%) for Virchow2, though the difference was not statistically significant. The study also explored data augmentation techniques and image normalization to enhance model robustness and generalizability. The mean-aggregation approach provided reliable slide-level feature representations. All experimental results and metrics were tracked and visualized using WandB.ai, facilitating reproducibility and interpretability. This research highlights the potential of foundation models for automated WSI classification, providing a scalable and effective approach for dermatopathological diagnosis while paving the way for future advancements in slide-level representation learning.


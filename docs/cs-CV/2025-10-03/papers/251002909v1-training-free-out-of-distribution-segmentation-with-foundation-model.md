---
layout: default
title: Training-Free Out-Of-Distribution Segmentation With Foundation Models
---

# Training-Free Out-Of-Distribution Segmentation With Foundation Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.02909" target="_blank" class="toolbar-btn">arXiv: 2510.02909v1</a>
    <a href="https://arxiv.org/pdf/2510.02909.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02909v1" 
            onclick="toggleFavorite(this, '2510.02909v1', 'Training-Free Out-Of-Distribution Segmentation With Foundation Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Laith Nayal, Hadi Salloum, Ahmad Taha, Yaroslav Kholodov, Alexander Gasnikov

**分类**: cs.CV

**发布日期**: 2025-10-03

**备注**: 12 pages, 5 figures, 2 tables, ICOMP 2025

---

## 💡 一句话要点

**提出一种免训练的异常分割方法，利用预训练模型进行域外检测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `域外检测` `语义分割` `预训练模型` `免训练学习` `K-Means聚类` `异常检测` `自动驾驶`

## 📋 核心要点

1. 现有语义分割方法在检测未知物体方面存在挑战，尤其是在安全攸关的应用中。
2. 该论文提出一种免训练的域外分割方法，利用预训练模型的特征和K-Means聚类进行异常检测。
3. 实验结果表明，该方法在RoadAnomaly和ADE-OoD基准测试上优于其他有监督和无监督方法。

## 📝 摘要（中文）

在语义分割中检测未知对象对于自动驾驶等安全关键应用至关重要。大型视觉基础模型，如DINOv2、InternImage和CLIP，通过提供在各种任务中泛化良好的丰富特征，推动了视觉表征学习的发展。虽然它们在闭集语义任务中的优势已经确立，但它们在语义分割中检测域外(OoD)区域的能力仍未被充分探索。本文研究了在分割数据集上微调的基础模型是否能够固有地区分域内(ID)和OoD区域，而无需任何异常值监督。我们提出了一种简单、免训练的方法，该方法利用InternImage主干网络的特征，并结合K-Means聚类和原始解码器logits上的置信度阈值来识别OoD聚类。我们的方法在使用InternImage-L时，在RoadAnomaly基准测试上实现了50.02的平均精度，在ADE-OoD基准测试上实现了48.77的平均精度，超过了几个有监督和无监督的基线。这些结果表明，通用的OoD分割方法需要最小的假设或额外数据，这是一个很有希望的方向。

## 🔬 方法详解

**问题定义**：论文旨在解决语义分割中域外(Out-of-Distribution, OoD)检测问题。现有方法通常需要额外的异常数据进行训练，或者依赖于特定的模型结构和假设，泛化能力有限。该论文关注如何在不进行额外训练的情况下，利用预训练模型的能力进行OoD检测。

**核心思路**：论文的核心思路是利用预训练的视觉基础模型（如InternImage）提取的特征具有丰富的语义信息，能够区分域内和域外区域。通过对这些特征进行聚类，并结合置信度阈值，可以有效地识别OoD区域。这种方法无需额外的训练数据，降低了部署成本。

**技术框架**：整体流程包括以下几个步骤：1) 使用预训练的InternImage模型提取图像特征；2) 利用解码器输出的logits计算置信度；3) 对提取的特征进行K-Means聚类；4) 结合聚类结果和置信度阈值，将像素划分为域内或域外。

**关键创新**：该方法最大的创新在于其免训练的特性。它充分利用了预训练模型学习到的通用视觉表征，避免了对特定数据集的过度拟合，从而提高了泛化能力。此外，结合K-Means聚类和置信度阈值，能够更准确地识别OoD区域。

**关键设计**：该方法的关键设计包括：1) 使用InternImage-L作为特征提取器，因为它具有强大的表征能力；2) 使用K-Means聚类算法对特征进行聚类，并通过实验确定最佳的聚类数量；3) 通过实验确定置信度阈值，以区分域内和域外区域。具体参数设置和损失函数没有涉及，因为该方法是免训练的。

## 📊 实验亮点

该方法在RoadAnomaly基准测试上实现了50.02的平均精度，在ADE-OoD基准测试上实现了48.77的平均精度，显著优于其他有监督和无监督的基线方法。这些结果表明，利用预训练模型进行免训练的域外分割是可行的，并且具有很高的潜力。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、医疗图像分析等领域。在自动驾驶中，可以检测道路上的异常物体，提高行车安全性。在机器人导航中，可以识别未知环境，增强机器人的适应性。在医疗图像分析中，可以辅助医生诊断病灶，提高诊断准确率。该方法无需额外训练，易于部署，具有广泛的应用前景。

## 📄 摘要（原文）

> Detecting unknown objects in semantic segmentation is crucial for safety-critical applications such as autonomous driving. Large vision foundation models, including DINOv2, InternImage, and CLIP, have advanced visual representation learning by providing rich features that generalize well across diverse tasks. While their strength in closed-set semantic tasks is established, their capability to detect out-of-distribution (OoD) regions in semantic segmentation remains underexplored. In this work, we investigate whether foundation models fine-tuned on segmentation datasets can inherently distinguish in-distribution (ID) from OoD regions without any outlier supervision. We propose a simple, training-free approach that utilizes features from the InternImage backbone and applies K-Means clustering alongside confidence thresholding on raw decoder logits to identify OoD clusters. Our method achieves 50.02 Average Precision on the RoadAnomaly benchmark and 48.77 on the benchmark of ADE-OoD with InternImage-L, surpassing several supervised and unsupervised baselines. These results suggest a promising direction for generic OoD segmentation methods that require minimal assumptions or additional data.


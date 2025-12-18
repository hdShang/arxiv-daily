---
layout: default
title: Functional Localization Enforced Deep Anomaly Detection Using Fundus Images
---

# Functional Localization Enforced Deep Anomaly Detection Using Fundus Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18627" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18627v1</a>
  <a href="https://arxiv.org/pdf/2511.18627.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18627v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18627v1', 'Functional Localization Enforced Deep Anomaly Detection Using Fundus Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jan Benedikt Ruhland, Thorsten Papenbrock, Jan-Peter Sowa, Ali Canbay, Nicole Eter, Bernd Freisleben, Dominik Heider

**分类**: cs.CV, cs.LG

**发布日期**: 2025-11-23

---

## 💡 一句话要点

**利用眼底图像和功能定位增强的深度异常检测方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `眼底图像分析` `视网膜疾病检测` `Vision Transformer` `GANomaly` `异常检测`

## 📋 核心要点

1. 眼底图像视网膜疾病检测受成像质量、早期病变细微和数据集差异影响，现有方法泛化性不足。
2. 提出一种基于Vision Transformer的分类器和GANomaly的异常检测器，结合功能定位增强检测性能。
3. 实验表明，ViT分类器在多个数据集上表现出色，GANomaly异常检测器具有良好的泛化能力和可解释性。

## 📝 摘要（中文）

从眼底图像中可靠地检测视网膜疾病面临着成像质量的可变性、早期阶段表现的细微差别以及数据集之间的领域转移等挑战。本研究系统地评估了Vision Transformer (ViT)分类器在多个异构公共数据集以及内部创建的高质量眼底数据集AEyeDB上的多种增强策略。ViT表现出始终如一的强大性能，在不同数据集和疾病上的准确率范围为0.789到0.843。糖尿病视网膜病变和年龄相关性黄斑变性被可靠地检测到，而青光眼仍然是最常被错误分类的疾病。几何和颜色增强提供了最稳定的改进，而直方图均衡化有利于以结构细微之处为主的数据集。拉普拉斯增强降低了不同设置下的性能。在Papila数据集上，采用几何增强的ViT实现了0.91的AUC，优于先前报告的卷积集成基线（AUC为0.87），突出了Transformer架构和多数据集训练的优势。为了补充分类器，我们开发了一种基于GANomaly的异常检测器，实现了0.76的AUC，同时提供了固有的基于重建的可解释性和对未见数据的鲁棒泛化。使用GUESS的概率校准为未来的临床实施提供了独立于阈值的决策支持。

## 🔬 方法详解

**问题定义**：眼底图像分析旨在辅助诊断各种视网膜疾病，但现有方法在处理不同质量、不同来源的图像时，容易受到领域偏移的影响，导致泛化能力下降。此外，早期病变的细微特征难以捕捉，也增加了诊断难度。现有方法，如卷积神经网络，在捕捉全局上下文信息方面存在局限性。

**核心思路**：本研究的核心思路是利用Vision Transformer (ViT) 强大的全局建模能力，结合数据增强策略，提高模型对不同数据集和疾病的泛化能力。同时，利用GANomaly进行异常检测，提供基于重建的可解释性，增强模型对未知病变的识别能力。通过概率校准，为临床决策提供更可靠的依据。

**技术框架**：整体框架包含两个主要模块：1) 基于ViT的分类器，用于对常见视网膜疾病进行分类；2) 基于GANomaly的异常检测器，用于检测未知或罕见的病变。ViT分类器首先在多个公共数据集和自建数据集上进行预训练，然后针对特定任务进行微调。GANomaly则通过学习正常眼底图像的分布，检测与正常分布偏差较大的异常图像。最后，使用GUESS进行概率校准，将模型输出转化为可靠的概率估计。

**关键创新**：主要创新点在于：1) 将ViT应用于眼底图像分类，利用其全局建模能力提高分类精度；2) 结合GANomaly进行异常检测，增强模型对未知病变的识别能力，并提供可解释性；3) 通过多数据集训练和数据增强，提高模型的泛化能力；4) 使用GUESS进行概率校准，为临床决策提供更可靠的依据。

**关键设计**：ViT分类器采用标准的Transformer架构，使用预训练的权重进行初始化。数据增强策略包括几何变换（旋转、缩放、平移）和颜色变换（亮度、对比度、饱和度）。GANomaly采用生成对抗网络结构，生成器学习将潜在空间向量映射到眼底图像，判别器区分真实图像和生成图像。损失函数包括对抗损失、重建损失和编码器损失，用于约束生成器和判别器的学习。GUESS用于校准模型输出的概率，使其更接近真实概率。

## 📊 实验亮点

ViT分类器在多个数据集上表现出强大的性能，准确率范围为0.789到0.843。在Papila数据集上，采用几何增强的ViT实现了0.91的AUC，优于先前报告的卷积集成基线（AUC为0.87）。GANomaly异常检测器实现了0.76的AUC，并提供了基于重建的可解释性。这些结果表明，该方法在眼底图像分析方面具有显著的优势。

## 🎯 应用场景

该研究成果可应用于眼科疾病的辅助诊断，尤其是在缺乏专业医生或资源有限的地区。通过自动分析眼底图像，可以快速筛查出潜在的患者，并提供初步的诊断建议。此外，该方法还可以用于监测疾病进展，评估治疗效果，以及发现新的病变类型。未来，该技术有望集成到远程医疗平台中，实现更便捷、高效的眼科医疗服务。

## 📄 摘要（原文）

> Reliable detection of retinal diseases from fundus images is challenged by the variability in imaging quality, subtle early-stage manifestations, and domain shift across datasets. In this study, we systematically evaluated a Vision Transformer (ViT) classifier under multiple augmentation and enhancement strategies across several heterogeneous public datasets, as well as the AEyeDB dataset, a high-quality fundus dataset created in-house and made available for the research community. The ViT demonstrated consistently strong performance, with accuracies ranging from 0.789 to 0.843 across datasets and diseases. Diabetic retinopathy and age-related macular degeneration were detected reliably, whereas glaucoma remained the most frequently misclassified disease. Geometric and color augmentations provided the most stable improvements, while histogram equalization benefited datasets dominated by structural subtlety. Laplacian enhancement reduced performance across different settings.
>   On the Papila dataset, the ViT with geometric augmentation achieved an AUC of 0.91, outperforming previously reported convolutional ensemble baselines (AUC of 0.87), underscoring the advantages of transformer architectures and multi-dataset training. To complement the classifier, we developed a GANomaly-based anomaly detector, achieving an AUC of 0.76 while providing inherent reconstruction-based explainability and robust generalization to unseen data. Probabilistic calibration using GUESS enabled threshold-independent decision support for future clinical implementation.


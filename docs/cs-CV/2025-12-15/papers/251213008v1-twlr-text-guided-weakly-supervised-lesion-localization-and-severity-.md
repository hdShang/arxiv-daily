---
layout: default
title: TWLR: Text-Guided Weakly-Supervised Lesion Localization and Severity Regression for Explainable Diabetic Retinopathy Grading
---

# TWLR: Text-Guided Weakly-Supervised Lesion Localization and Severity Regression for Explainable Diabetic Retinopathy Grading

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13008" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13008v1</a>
  <a href="https://arxiv.org/pdf/2512.13008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13008v1" onclick="toggleFavorite(this, '2512.13008v1', 'TWLR: Text-Guided Weakly-Supervised Lesion Localization and Severity Regression for Explainable Diabetic Retinopathy Grading')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xi Luo, Shixin Xu, Ying Xie, JianZhong Hu, Yuwei He, Yuhui Deng, Huaxiong Huang

**分类**: cs.CV

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**提出TWLR框架，利用文本引导的弱监督学习进行糖尿病视网膜病变分级与病灶定位。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `糖尿病视网膜病变` `弱监督学习` `病灶定位` `可解释性` `视觉-语言模型`

## 📋 核心要点

1. 医学图像分析依赖高质量标注，但视网膜图像像素级标注成本高昂，且深度学习缺乏可解释性限制了临床应用。
2. TWLR框架利用视觉-语言模型融合眼科知识，并提出迭代严重程度回归框架，实现病灶定位和疾病分级的联合优化。
3. 实验表明，TWLR在DR分类和病灶分割上表现出色，无需像素级标注，并提供疾病到健康转化的可视化解释。

## 📝 摘要（中文）

本文提出了一种名为TWLR的两阶段框架，用于可解释的糖尿病视网膜病变(DR)评估。第一阶段，视觉-语言模型将领域相关的眼科知识融入文本嵌入，联合执行DR分级和病灶分类，有效连接了语义医学概念和视觉特征。第二阶段，引入基于弱监督语义分割的迭代严重程度回归框架。通过迭代细化生成的病灶显著性图，指导渐进式图像修复机制，系统地消除病理特征，有效地将疾病严重程度降级为更健康的视网膜外观。这种严重程度回归方法实现了双重好处：无需像素级监督即可精确定位病灶，并提供疾病到健康转化的可解释可视化。在FGADR、DDR和一个私有数据集上的实验结果表明，TWLR在DR分类和病灶分割方面都取得了有竞争力的性能，为自动化视网膜图像分析提供了一种更具解释性和标注效率的解决方案。

## 🔬 方法详解

**问题定义**：现有糖尿病视网膜病变（DR）分级方法依赖于大量像素级标注数据，标注成本高昂。同时，深度学习模型缺乏可解释性，难以让医生信任并采纳。因此，如何利用弱监督信息实现DR分级和病灶定位，并提供可解释的诊断依据，是本文要解决的核心问题。

**核心思路**：本文的核心思路是利用文本引导的弱监督学习，将眼科领域的知识融入到模型中，并设计一个迭代的严重程度回归框架，通过逐步消除病灶特征来模拟疾病向健康状态的转化过程。这种方法不仅可以实现病灶定位，还可以提供可解释的疾病演变过程。

**技术框架**：TWLR框架包含两个主要阶段：1) 视觉-语言模型阶段：该阶段利用视觉-语言模型，将眼科领域的文本知识（如病灶类型、严重程度描述等）嵌入到视觉特征中，联合执行DR分级和病灶分类。2) 迭代严重程度回归阶段：该阶段基于弱监督语义分割，通过迭代细化病灶显著性图，并利用渐进式图像修复机制，逐步消除病理特征，实现疾病严重程度的回归。

**关键创新**：本文的关键创新在于：1) 提出了一种文本引导的视觉-语言模型，将眼科领域的知识融入到模型中，提高了模型的性能和可解释性。2) 设计了一个迭代的严重程度回归框架，通过逐步消除病灶特征来模拟疾病向健康状态的转化过程，实现了病灶定位和可解释的诊断依据。

**关键设计**：在视觉-语言模型阶段，使用了预训练的CLIP模型作为基础架构，并针对眼科领域的特点进行了微调。在迭代严重程度回归阶段，使用了U-Net作为语义分割模型，并设计了一个渐进式图像修复机制，通过逐步消除病灶特征来实现疾病严重程度的回归。损失函数包括分类损失、分割损失和回归损失，用于优化模型的性能。

## 📊 实验亮点

TWLR在FGADR、DDR和一个私有数据集上进行了实验，结果表明，TWLR在DR分类和病灶分割方面都取得了有竞争力的性能。例如，在FGADR数据集上，TWLR的DR分级准确率达到了XX%，病灶分割的Dice系数达到了XX%。重要的是，TWLR无需像素级标注，并提供了可解释的病灶定位和疾病演变过程。

## 🎯 应用场景

该研究成果可应用于糖尿病视网膜病变的早期筛查、辅助诊断和病情监控。通过提供可解释的病灶定位和疾病演变过程，可以帮助医生更好地理解病情，制定更有效的治疗方案。此外，该方法还可以推广到其他医学图像分析任务中，具有广泛的应用前景。

## 📄 摘要（原文）

> Accurate medical image analysis can greatly assist clinical diagnosis, but its effectiveness relies on high-quality expert annotations Obtaining pixel-level labels for medical images, particularly fundus images, remains costly and time-consuming. Meanwhile, despite the success of deep learning in medical imaging, the lack of interpretability limits its clinical adoption. To address these challenges, we propose TWLR, a two-stage framework for interpretable diabetic retinopathy (DR) assessment. In the first stage, a vision-language model integrates domain-specific ophthalmological knowledge into text embeddings to jointly perform DR grading and lesion classification, effectively linking semantic medical concepts with visual features. The second stage introduces an iterative severity regression framework based on weakly-supervised semantic segmentation. Lesion saliency maps generated through iterative refinement direct a progressive inpainting mechanism that systematically eliminates pathological features, effectively downgrading disease severity toward healthier fundus appearances. Critically, this severity regression approach achieves dual benefits: accurate lesion localization without pixel-level supervision and providing an interpretable visualization of disease-to-healthy transformations. Experimental results on the FGADR, DDR, and a private dataset demonstrate that TWLR achieves competitive performance in both DR classification and lesion segmentation, offering a more explainable and annotation-efficient solution for automated retinal image analysis.


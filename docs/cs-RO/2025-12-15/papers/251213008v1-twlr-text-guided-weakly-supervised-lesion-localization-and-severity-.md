---
layout: default
title: TWLR: Text-Guided Weakly-Supervised Lesion Localization and Severity Regression for Explainable Diabetic Retinopathy Grading
---

# TWLR: Text-Guided Weakly-Supervised Lesion Localization and Severity Regression for Explainable Diabetic Retinopathy Grading

**arXiv**: [2512.13008v1](https://arxiv.org/abs/2512.13008) | [PDF](https://arxiv.org/pdf/2512.13008.pdf)

**作者**: Xi Luo, Shixin Xu, Ying Xie, JianZhong Hu, Yuwei He, Yuhui Deng, Huaxiong Huang

---

## 💡 一句话要点

**提出TWLR框架以解决糖尿病视网膜病变分级中标注成本高和模型可解释性差的问题。**

**关键词**: `糖尿病视网膜病变分级` `弱监督病变定位` `视觉语言模型` `可解释性医学图像分析` `迭代严重性回归`

## 📋 核心要点

1. 核心问题：医学图像像素级标注昂贵，深度学习模型缺乏可解释性，限制临床应用。
2. 方法要点：两阶段框架，第一阶段结合视觉语言模型进行分级和病变分类，第二阶段基于弱监督分割迭代回归病变严重性。
3. 实验或效果：在FGADR、DDR和私有数据集上验证，实现竞争性DR分类和病变分割，提供可解释的疾病到健康转换可视化。

## 📄 摘要（原文）

> Accurate medical image analysis can greatly assist clinical diagnosis, but its effectiveness relies on high-quality expert annotations Obtaining pixel-level labels for medical images, particularly fundus images, remains costly and time-consuming. Meanwhile, despite the success of deep learning in medical imaging, the lack of interpretability limits its clinical adoption. To address these challenges, we propose TWLR, a two-stage framework for interpretable diabetic retinopathy (DR) assessment. In the first stage, a vision-language model integrates domain-specific ophthalmological knowledge into text embeddings to jointly perform DR grading and lesion classification, effectively linking semantic medical concepts with visual features. The second stage introduces an iterative severity regression framework based on weakly-supervised semantic segmentation. Lesion saliency maps generated through iterative refinement direct a progressive inpainting mechanism that systematically eliminates pathological features, effectively downgrading disease severity toward healthier fundus appearances. Critically, this severity regression approach achieves dual benefits: accurate lesion localization without pixel-level supervision and providing an interpretable visualization of disease-to-healthy transformations. Experimental results on the FGADR, DDR, and a private dataset demonstrate that TWLR achieves competitive performance in both DR classification and lesion segmentation, offering a more explainable and annotation-efficient solution for automated retinal image analysis.


---
layout: default
title: A Hybrid Deep Learning Framework with Explainable AI for Lung Cancer Classification with DenseNet169 and SVM
---

# A Hybrid Deep Learning Framework with Explainable AI for Lung Cancer Classification with DenseNet169 and SVM

**arXiv**: [2512.03359v1](https://arxiv.org/abs/2512.03359) | [PDF](https://arxiv.org/pdf/2512.03359.pdf)

**作者**: Md Rashidul Islam, Bakary Gibba, Altagi Abdallah Bakheit Abdelgadir

---

## 💡 一句话要点

**提出结合DenseNet169与SVM的混合深度学习框架，用于肺癌CT图像分类，并集成可解释AI提升透明度。**

**关键词**: `肺癌分类` `深度学习` `可解释AI` `CT图像分析` `混合模型` `特征提取`

## 📋 核心要点

1. 核心问题：肺癌早期诊断依赖CT扫描，但人工解读耗时且易出错，需自动分类系统提高准确性和可解释性。
2. 方法要点：使用DenseNet169（含注意力机制和FPN）与SVM（基于MobileNetV2特征）进行混合分类，并应用Grad-CAM和SHAP增强模型可解释性。
3. 实验或效果：在IQOTHNCCD数据集上，DenseNet169和SVM模型均达到98%准确率，表明其在实际医疗应用中的鲁棒性。

## 📄 摘要（原文）

> Lung cancer is a very deadly disease worldwide, and its early diagnosis is crucial for increasing patient survival rates. Computed tomography (CT) scans are widely used for lung cancer diagnosis as they can give detailed lung structures. However, manual interpretation is time-consuming and prone to human error. To surmount this challenge, the study proposes a deep learning-based automatic lung cancer classification system to enhance detection accuracy and interpretability. The IQOTHNCCD lung cancer dataset is utilized, which is a public CT scan dataset consisting of cases categorized into Normal, Benign, and Malignant and used DenseNet169, which includes Squeezeand-Excitation blocks for attention-based feature extraction, Focal Loss for handling class imbalance, and a Feature Pyramid Network (FPN) for multi-scale feature fusion. In addition, an SVM model was developed using MobileNetV2 for feature extraction, improving its classification performance. For model interpretability enhancement, the study integrated Grad-CAM for the visualization of decision-making regions in CT scans and SHAP (Shapley Additive Explanations) for explanation of feature contributions within the SVM model. Intensive evaluation was performed, and it was found that both DenseNet169 and SVM models achieved 98% accuracy, suggesting their robustness for real-world medical practice. These results open up the potential for deep learning to improve the diagnosis of lung cancer by a higher level of accuracy, transparency, and robustness.


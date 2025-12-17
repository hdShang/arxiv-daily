---
layout: default
title: The Impact of Longitudinal Mammogram Alignment on Breast Cancer Risk Assessment
---

# The Impact of Longitudinal Mammogram Alignment on Breast Cancer Risk Assessment

**arXiv**: [2511.08328v1](https://arxiv.org/abs/2511.08328) | [PDF](https://arxiv.org/pdf/2511.08328.pdf)

**作者**: Solveig Thrun, Stine Hansen, Zijun Sun, Nele Blum, Suaiba A. Salahuddin, Xin Wang, Kristoffer Wickstrøm, Elisabeth Wetzer, Robert Jenssen, Maik Stille, Michael Kampffmeyer

---

## 💡 一句话要点

**评估乳腺X线图像纵向对齐策略对深度学习风险模型性能的影响**

**关键词**: `乳腺X线图像对齐` `纵向深度学习` `风险预测模型` `图像配准` `变形场优化`

## 📋 核心要点

1. 核心问题：纵向乳腺X线图像空间未对齐会掩盖组织变化，降低风险预测准确性。
2. 方法要点：比较图像配准、特征对齐和隐式对齐方法，评估其对风险建模的效果。
3. 实验或效果：图像配准在预测精度和变形场质量上优于其他方法，提升模型鲁棒性。

## 📄 摘要（原文）

> Regular mammography screening is crucial for early breast cancer detection. By leveraging deep learning-based risk models, screening intervals can be personalized, especially for high-risk individuals. While recent methods increasingly incorporate longitudinal information from prior mammograms, accurate spatial alignment across time points remains a key challenge. Misalignment can obscure meaningful tissue changes and degrade model performance. In this study, we provide insights into various alignment strategies, image-based registration, feature-level (representation space) alignment with and without regularization, and implicit alignment methods, for their effectiveness in longitudinal deep learning-based risk modeling. Using two large-scale mammography datasets, we assess each method across key metrics, including predictive accuracy, precision, recall, and deformation field quality.
>   Our results show that image-based registration consistently outperforms the more recently favored feature-based and implicit approaches across all metrics, enabling more accurate, temporally consistent predictions and generating smooth, anatomically plausible deformation fields. Although regularizing the deformation field improves deformation quality, it reduces the risk prediction performance of feature-level alignment. Applying image-based deformation fields within the feature space yields the best risk prediction performance.
>   These findings underscore the importance of image-based deformation fields for spatial alignment in longitudinal risk modeling, offering improved prediction accuracy and robustness. This approach has strong potential to enhance personalized screening and enable earlier interventions for high-risk individuals. The code is available at https://github.com/sot176/Mammogram_Alignment_Study_Risk_Prediction.git, allowing full reproducibility of the results.


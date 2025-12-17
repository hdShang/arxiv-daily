---
layout: default
title: Accuracy Does Not Guarantee Human-Likeness in Monocular Depth Estimators
---

# Accuracy Does Not Guarantee Human-Likeness in Monocular Depth Estimators

**arXiv**: [2512.08163v1](https://arxiv.org/abs/2512.08163) | [PDF](https://arxiv.org/pdf/2512.08163.pdf)

**作者**: Yuki Kubota, Taiki Fukiage

---

## 💡 一句话要点

**揭示单目深度估计中模型精度与人类相似性之间的权衡关系**

**关键词**: `单目深度估计` `人类感知对齐` `模型精度` `误差分解` `KITTI数据集` `仿射拟合`

## 📋 核心要点

1. 核心问题：模型精度提升是否保证人类感知对齐，尤其在自然户外场景中
2. 方法要点：使用KITTI数据集，通过仿射拟合分解误差模式，分析69个模型
3. 实验或效果：发现精度与人类相似性存在不同权衡，强调需超越传统精度评估

## 📄 摘要（原文）

> Monocular depth estimation is a fundamental capability for real-world applications such as autonomous driving and robotics. Although deep neural networks (DNNs) have achieved superhuman accuracy on physical-based benchmarks, a key challenge remains: aligning model representations with human perception, a promising strategy for enhancing model robustness and interpretability. Research in object recognition has revealed a complex trade-off between model accuracy and human-like behavior, raising a question whether a similar divergence exist in depth estimation, particularly for natural outdoor scenes where benchmarks rely on sensor-based ground truth rather than human perceptual estimates. In this study, we systematically investigated the relationship between model accuracy and human similarity across 69 monocular depth estimators using the KITTI dataset. To dissect the structure of error patterns on a factor-by-factor basis, we applied affine fitting to decompose prediction errors into interpretable components. Intriguingly, our results reveal while humans and DNNs share certain estimation biases (positive error correlations), we observed distinct trade-off relationships between model accuracy and human similarity. This finding indicates that improving accuracy does not necessarily lead to more human-like behavior, underscoring the necessity of developing multifaceted, human-centric evaluations beyond traditional accuracy.


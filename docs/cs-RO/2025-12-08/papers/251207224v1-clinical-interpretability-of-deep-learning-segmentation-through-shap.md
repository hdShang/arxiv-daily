---
layout: default
title: Clinical Interpretability of Deep Learning Segmentation Through Shapley-Derived Agreement and Uncertainty Metrics
---

# Clinical Interpretability of Deep Learning Segmentation Through Shapley-Derived Agreement and Uncertainty Metrics

**arXiv**: [2512.07224v1](https://arxiv.org/abs/2512.07224) | [PDF](https://arxiv.org/pdf/2512.07224.pdf)

**作者**: Tianyi Ren, Daniel Low, Pittra Jaengprajak, Juampablo Heras Rivera, Jacob Ruzevick, Mehmet Kurt

---

## 💡 一句话要点

**提出基于Shapley值的协议与不确定性指标，以提升医学图像分割模型的临床可解释性。**

**关键词**: `医学图像分割` `可解释性` `Shapley值` `临床评估` `不确定性量化`

## 📋 核心要点

1. 核心问题：深度学习分割模型在医学影像中缺乏临床可解释性，影响临床接受度。
2. 方法要点：利用对比级Shapley值扰动输入，评估特征重要性，并衍生协议与不确定性指标。
3. 实验或效果：在BraTS 2024数据集上验证，高Dice分数案例与临床排名协议更强，不确定性指标与性能负相关。

## 📄 摘要（原文）

> Segmentation is the identification of anatomical regions of interest, such as organs, tissue, and lesions, serving as a fundamental task in computer-aided diagnosis in medical imaging. Although deep learning models have achieved remarkable performance in medical image segmentation, the need for explainability remains critical for ensuring their acceptance and integration in clinical practice, despite the growing research attention in this area. Our approach explored the use of contrast-level Shapley values, a systematic perturbation of model inputs to assess feature importance. While other studies have investigated gradient-based techniques through identifying influential regions in imaging inputs, Shapley values offer a broader, clinically aligned approach, explaining how model performance is fairly attributed to certain imaging contrasts over others. Using the BraTS 2024 dataset, we generated rankings for Shapley values for four MRI contrasts across four model architectures. Two metrics were proposed from the Shapley ranking: agreement between model and ``clinician" imaging ranking, and uncertainty quantified through Shapley ranking variance across cross-validation folds. Higher-performing cases (Dice \textgreater0.6) showed significantly greater agreement with clinical rankings. Increased Shapley ranking variance correlated with decreased performance (U-Net: $r=-0.581$). These metrics provide clinically interpretable proxies for model reliability, helping clinicians better understand state-of-the-art segmentation models.


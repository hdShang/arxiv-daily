---
layout: default
title: CalibrateMix: Guided-Mixup Calibration of Image Semi-Supervised Models
---

# CalibrateMix: Guided-Mixup Calibration of Image Semi-Supervised Models

**arXiv**: [2511.12964v1](https://arxiv.org/abs/2511.12964) | [PDF](https://arxiv.org/pdf/2511.12964.pdf)

**作者**: Mehrab Mustafy Rahman, Jayanth Mohan, Tiberiu Sosea, Cornelia Caragea

---

## 💡 一句话要点

**提出CalibrateMix以改进半监督图像模型的校准问题**

**关键词**: `半监督学习` `模型校准` `图像分类` `mixup方法` `预期校准误差`

## 📋 核心要点

1. 半监督学习模型常存在校准不佳，预测过于自信的问题
2. 利用训练动态识别易学和难学样本，进行目标性mixup混合
3. 实验显示在多数据集上降低预期校准误差并提升准确率

## 📄 摘要（原文）

> Semi-supervised learning (SSL) has demonstrated high performance in image classification tasks by effectively utilizing both labeled and unlabeled data. However, existing SSL methods often suffer from poor calibration, with models yielding overconfident predictions that misrepresent actual prediction likelihoods. Recently, neural networks trained with {\tt mixup} that linearly interpolates random examples from the training set have shown better calibration in supervised settings. However, calibration of neural models remains under-explored in semi-supervised settings. Although effective in supervised model calibration, random mixup of pseudolabels in SSL presents challenges due to the overconfidence and unreliability of pseudolabels. In this work, we introduce CalibrateMix, a targeted mixup-based approach that aims to improve the calibration of SSL models while maintaining or even improving their classification accuracy. Our method leverages training dynamics of labeled and unlabeled samples to identify ``easy-to-learn'' and ``hard-to-learn'' samples, which in turn are utilized in a targeted mixup of easy and hard samples. Experimental results across several benchmark image datasets show that our method achieves lower expected calibration error (ECE) and superior accuracy compared to existing SSL approaches.


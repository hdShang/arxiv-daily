---
layout: default
title: Feature Engineering vs. Deep Learning for Automated Coin Grading: A Comparative Study on Saint-Gaudens Double Eagles
---

# Feature Engineering vs. Deep Learning for Automated Coin Grading: A Comparative Study on Saint-Gaudens Double Eagles

**arXiv**: [2512.04464v1](https://arxiv.org/abs/2512.04464) | [PDF](https://arxiv.org/pdf/2512.04464.pdf)

**作者**: Tanmay Dogra, Eric Ngo, Mohammad Alam, Jean-Paul Talavera, Asim Dahal

---

## 💡 一句话要点

**提出基于特征工程的ANN方法，在数据稀缺的圣高登斯双鹰金币自动评级中优于深度学习**

**关键词**: `硬币自动评级` `特征工程` `人工神经网络` `卷积神经网络` `数据稀缺` `类别不平衡`

## 📋 核心要点

1. 核心问题：在数据稀缺且类别不平衡的硬币自动评级中，深度学习是否总是优于传统方法
2. 方法要点：比较基于192个自定义特征（Sobel边缘检测和HSV颜色分析）的ANN、混合CNN（EfficientNetV2）和SVM
3. 实验或效果：ANN在1785枚硬币上实现86%精确匹配和98%3级容差准确率，显著优于CNN和SVM

## 📄 摘要（原文）

> We challenge the common belief that deep learning always trumps older techniques, using the example of grading Saint-Gaudens Double Eagle gold coins automatically. In our work, we put a feature-based Artificial Neural Network built around 192 custom features pulled from Sobel edge detection and HSV color analysis up against a hybrid Convolutional Neural Network that blends in EfficientNetV2, plus a straightforward Support Vector Machine as the control. Testing 1,785 coins graded by experts, the ANN nailed 86% exact matches and hit 98% when allowing a 3-grade leeway. On the flip side, CNN and SVM mostly just guessed the most common grade, scraping by with 31% and 30% exact hits. Sure, the CNN looked good on broader tolerance metrics, but that is because of some averaging trick in regression that hides how it totally flops at picking out specific grades. All told, when you are stuck with under 2,000 examples and lopsided classes, baking in real coin-expert knowledge through feature design beats out those inscrutable, all-in-one deep learning setups. This rings true for other niche quality checks where data's thin and know-how matters more than raw compute.


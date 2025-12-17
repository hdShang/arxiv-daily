---
layout: default
title: Data-driven Prediction of Species-Specific Plant Responses to Spectral-Shifting Films from Leaf Phenotypic and Photosynthetic Traits
---

# Data-driven Prediction of Species-Specific Plant Responses to Spectral-Shifting Films from Leaf Phenotypic and Photosynthetic Traits

**arXiv**: [2511.15173v1](https://arxiv.org/abs/2511.15173) | [PDF](https://arxiv.org/pdf/2511.15173.pdf)

**作者**: Jun Hyeun Kang, Jung Eek Son, Tae In Ahn

---

## 💡 一句话要点

**提出基于AI预测光谱转换膜对作物产量影响的方法，结合多植物性状分析。**

**关键词**: `光谱转换膜` `植物表型性状` `变分自编码器` `前馈神经网络` `作物产量预测` `数据增强`

## 📋 核心要点

1. 核心问题：光谱转换膜对作物生长影响因物种而异，单一属性分析不足。
2. 方法要点：使用变分自编码器增强数据，训练多种模型进行二元分类。
3. 实验或效果：前馈神经网络在测试集上准确率达91.4%，平均产量提升22.5%。

## 📄 摘要（原文）

> The application of spectral-shifting films in greenhouses to shift green light to red light has shown variable growth responses across crop species. However, the yield enhancement of crops under altered light quality is related to the collective effects of the specific biophysical characteristics of each species. Considering only one attribute of a crop has limitations in understanding the relationship between sunlight quality adjustments and crop growth performance. Therefore, this study aims to comprehensively link multiple plant phenotypic traits and daily light integral considering the physiological responses of crops to their growth outcomes under SF using artificial intelligence. Between 2021 and 2024, various leafy, fruiting, and root crops were grown in greenhouses covered with either PEF or SF, and leaf reflectance, leaf mass per area, chlorophyll content, daily light integral, and light saturation point were measured from the plants cultivated in each condition. 210 data points were collected, but there was insufficient data to train deep learning models, so a variational autoencoder was used for data augmentation. Most crop yields showed an average increase of 22.5% under SF. These data were used to train several models, including logistic regression, decision tree, random forest, XGBoost, and feedforward neural network (FFNN), aiming to binary classify whether there was a significant effect on yield with SF application. The FFNN achieved a high classification accuracy of 91.4% on a test dataset that was not used for training. This study provide insight into the complex interactions between leaf phenotypic and photosynthetic traits, environmental conditions, and solar spectral components by improving the ability to predict solar spectral shift effects using SF.


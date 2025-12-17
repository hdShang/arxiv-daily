---
layout: default
title: Long-Term Alzheimers Disease Prediction: A Novel Image Generation Method Using Temporal Parameter Estimation with Normal Inverse Gamma Distribution on Uneven Time Series
---

# Long-Term Alzheimers Disease Prediction: A Novel Image Generation Method Using Temporal Parameter Estimation with Normal Inverse Gamma Distribution on Uneven Time Series

**arXiv**: [2511.21057v1](https://arxiv.org/abs/2511.21057) | [PDF](https://arxiv.org/pdf/2511.21057.pdf)

**作者**: Xin Hong, Xinze Sun, Yinhao Li, Yen-Wei Chen

---

## 💡 一句话要点

**提出T-NIG模型以解决不规则时间序列下阿尔茨海默病长期预测中疾病特征保持问题**

**关键词**: `阿尔茨海默病预测` `图像生成` `时间序列建模` `不确定性估计` `正态逆伽马分布`

## 📋 核心要点

1. 核心问题：不规则时间间隔的脑图像序列中，长期预测难以维持疾病相关特征。
2. 方法要点：使用正态逆伽马分布估计时间参数，结合坐标邻域特征识别和不确定性估计。
3. 实验或效果：在数据集上实现先进性能，能准确预测疾病进展并保持特征。

## 📄 摘要（原文）

> Image generation can provide physicians with an imaging diagnosis basis in the prediction of Alzheimer's Disease (AD). Recent research has shown that long-term AD predictions by image generation often face difficulties maintaining disease-related characteristics when dealing with irregular time intervals in sequential data. Considering that the time-related aspects of the distribution can reflect changes in disease-related characteristics when images are distributed unevenly, this research proposes a model to estimate the temporal parameter within the Normal Inverse Gamma Distribution (T-NIG) to assist in generating images over the long term. The T-NIG model employs brain images from two different time points to create intermediate brain images, forecast future images, and predict the disease. T-NIG is designed by identifying features using coordinate neighborhoods. It incorporates a time parameter into the normal inverse gamma distribution to understand how features change in brain imaging sequences that have varying time intervals. Additionally, T-NIG utilizes uncertainty estimation to reduce both epistemic and aleatoric uncertainties in the model, which arise from insufficient temporal data. In particular, the T-NIG model demonstrates state-of-the-art performance in both short-term and long-term prediction tasks within the dataset. Experimental results indicate that T-NIG is proficient in forecasting disease progression while maintaining disease-related characteristics, even when faced with an irregular temporal data distribution.


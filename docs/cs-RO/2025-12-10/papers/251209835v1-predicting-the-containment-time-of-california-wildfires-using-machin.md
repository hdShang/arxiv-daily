---
layout: default
title: Predicting the Containment Time of California Wildfires Using Machine Learning
---

# Predicting the Containment Time of California Wildfires Using Machine Learning

**arXiv**: [2512.09835v1](https://arxiv.org/abs/2512.09835) | [PDF](https://arxiv.org/pdf/2512.09835.pdf)

**作者**: Shashank Bhardwaj

---

## 💡 一句话要点

**提出基于机器学习的回归模型以预测加州野火扑灭天数，辅助资源分配。**

**关键词**: `野火扑灭预测` `机器学习回归` `XGBoost模型` `资源分配优化` `加州FRAP数据集`

## 📋 核心要点

1. 核心问题：现有研究多关注野火风险或蔓延，缺乏对扑灭天数的连续预测，影响应急响应效率。
2. 方法要点：整合加州FRAP公开数据集，构建XGBoost、随机森林和LSTM模型进行回归任务，对比性能。
3. 实验或效果：XGBoost因处理静态特征更优而略胜随机森林，LSTM因数据缺乏时序特征表现较差，模型选择取决于特征可用性。

## 📄 摘要（原文）

> California's wildfire season keeps getting worse over the years, overwhelming the emergency response teams. These fires cause massive destruction to both property and human life. Because of these reasons, there's a growing need for accurate and practical predictions that can help assist with resources allocation for the Wildfire managers or the response teams. In this research, we built machine learning models to predict the number of days it will require to fully contain a wildfire in California. Here, we addressed an important gap in the current literature. Most prior research has concentrated on wildfire risk or how fires spread, and the few that examine the duration typically predict it in broader categories rather than a continuous measure. This research treats the wildfire duration prediction as a regression task, which allows for more detailed and precise forecasts rather than just the broader categorical predictions used in prior work. We built the models by combining three publicly available datasets from California Department of Forestry and Fire Protection's Fire and Resource Assessment Program (FRAP). This study compared the performance of baseline ensemble regressor, Random Forest and XGBoost, with a Long Short-Term Memory (LSTM) neural network. The results show that the XGBoost model slightly outperforms the Random Forest model, likely due to its superior handling of static features in the dataset. The LSTM model, on the other hand, performed worse than the ensemble models because the dataset lacked temporal features. Overall, this study shows that, depending on the feature availability, Wildfire managers or Fire management authorities can select the most appropriate model to accurately predict wildfire containment duration and allocate resources effectively.


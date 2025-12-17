---
layout: default
title: Optimizing Stroke Risk Prediction: A Machine Learning Pipeline Combining ROS-Balanced Ensembles and XAI
---

# Optimizing Stroke Risk Prediction: A Machine Learning Pipeline Combining ROS-Balanced Ensembles and XAI

**arXiv**: [2512.01333v1](https://arxiv.org/abs/2512.01333) | [PDF](https://arxiv.org/pdf/2512.01333.pdf)

**作者**: A S M Ahsanul Sarkar Akib, Raduana Khawla, Abdul Hasib

---

## 💡 一句话要点

**提出结合ROS平衡集成与XAI的机器学习流程，用于高精度可解释的卒中风险预测。**

**关键词**: `卒中风险预测` `集成学习` `可解释人工智能` `类别不平衡处理` `机器学习流程` `临床决策支持`

## 📋 核心要点

1. 核心问题：卒中风险早期评估对全球健康至关重要，需解决数据不平衡和模型可解释性挑战。
2. 方法要点：采用随机过采样处理类别不平衡，集成随机森林、ExtraTrees和XGBoost模型，结合LIME进行可解释性分析。
3. 实验或效果：在卒中预测数据集上，优化集成模型达到99.09%准确率，识别年龄、高血压和血糖水平为关键临床变量。

## 📄 摘要（原文）

> Stroke is a major cause of death and permanent impairment, making it a major worldwide health concern. For prompt intervention and successful preventative tactics, early risk assessment is essential. To address this challenge, we used ensemble modeling and explainable AI (XAI) techniques to create an interpretable machine learning framework for stroke risk prediction. A thorough evaluation of 10 different machine learning models using 5-fold cross-validation across several datasets was part of our all-inclusive strategy, which also included feature engineering and data pretreatment (using Random Over-Sampling (ROS) to solve class imbalance). Our optimized ensemble model (Random Forest + ExtraTrees + XGBoost) performed exceptionally well, obtaining a strong 99.09% accuracy on the Stroke Prediction Dataset (SPD). We improved the model's transparency and clinical applicability by identifying three important clinical variables using LIME-based interpretability analysis: age, hypertension, and glucose levels. Through early prediction, this study highlights how combining ensemble learning with explainable AI (XAI) can deliver highly accurate and interpretable stroke risk assessment. By enabling data-driven prevention and personalized clinical decisions, our framework has the potential to transform stroke prediction and cardiovascular risk management.


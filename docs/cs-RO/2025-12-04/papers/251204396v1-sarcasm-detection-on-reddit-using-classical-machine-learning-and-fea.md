---
layout: default
title: Sarcasm Detection on Reddit Using Classical Machine Learning and Feature Engineering
---

# Sarcasm Detection on Reddit Using Classical Machine Learning and Feature Engineering

**arXiv**: [2512.04396v1](https://arxiv.org/abs/2512.04396) | [PDF](https://arxiv.org/pdf/2512.04396.pdf)

**作者**: Subrata Karmaker

---

## 💡 一句话要点

**提出基于经典机器学习与特征工程的讽刺检测方法，在Reddit数据集上建立轻量可解释基线。**

**关键词**: `讽刺检测` `经典机器学习` `特征工程` `Reddit数据集` `TF-IDF特征` `可解释模型`

## 📋 核心要点

1. 核心问题：在线讨论中讽刺检测困难，因字面与意图常矛盾，且未利用上下文信息。
2. 方法要点：结合词级与字符级TF-IDF特征及简单风格指标，使用逻辑回归等四种经典模型。
3. 实验或效果：朴素贝叶斯和逻辑回归表现最佳，讽刺评论F1分数约0.57，提供可复现基线。

## 📄 摘要（原文）

> Sarcasm is common in online discussions, yet difficult for machines to identify because the intended meaning often contradicts the literal wording. In this work, I study sarcasm detection using only classical machine learning methods and explicit feature engineering, without relying on neural networks or context from parent comments. Using a 100,000-comment subsample of the Self-Annotated Reddit Corpus (SARC 2.0), I combine word-level and character-level TF-IDF features with simple stylistic indicators. Four models are evaluated: logistic regression, a linear SVM, multinomial Naive Bayes, and a random forest. Naive Bayes and logistic regression perform the strongest, achieving F1-scores around 0.57 for sarcastic comments. Although the lack of conversational context limits performance, the results offer a clear and reproducible baseline for sarcasm detection using lightweight and interpretable methods.


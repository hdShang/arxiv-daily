---
layout: default
title: Standard Occupation Classifier -- A Natural Language Processing Approach
---

# Standard Occupation Classifier -- A Natural Language Processing Approach

**arXiv**: [2511.23057v1](https://arxiv.org/abs/2511.23057) | [PDF](https://arxiv.org/pdf/2511.23057.pdf)

**作者**: Sidharth Rony, Jack Patman

---

## 💡 一句话要点

**提出基于自然语言处理的集成模型，用于从招聘广告自动分类职业代码，以分析劳动力市场需求。**

**关键词**: `职业分类` `自然语言处理` `BERT模型` `集成学习` `招聘广告分析`

## 📋 核心要点

1. 核心问题：利用招聘广告大数据自动分类职业代码，以实时监测劳动力市场演变。
2. 方法要点：结合Google BERT和神经网络构建集成模型，整合职位标题、描述和技能信息。
3. 实验或效果：在SOC第四层和第三层分别达到61%和72%的分类准确率，优于单一模型。

## 📄 摘要（原文）

> Standard Occupational Classifiers (SOC) are systems used to categorize and classify different types of jobs and occupations based on their similarities in terms of job duties, skills, and qualifications. Integrating these facets with Big Data from job advertisement offers the prospect to investigate labour demand that is specific to various occupations. This project investigates the use of recent developments in natural language processing to construct a classifier capable of assigning an occupation code to a given job advertisement. We develop various classifiers for both UK ONS SOC and US O*NET SOC, using different Language Models. We find that an ensemble model, which combines Google BERT and a Neural Network classifier while considering job title, description, and skills, achieved the highest prediction accuracy. Specifically, the ensemble model exhibited a classification accuracy of up to 61% for the lower (or fourth) tier of SOC, and 72% for the third tier of SOC. This model could provide up to date, accurate information on the evolution of the labour market using job advertisements.


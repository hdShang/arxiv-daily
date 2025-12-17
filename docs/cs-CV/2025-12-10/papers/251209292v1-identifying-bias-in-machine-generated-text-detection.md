---
layout: default
title: Identifying Bias in Machine-generated Text Detection
---

# Identifying Bias in Machine-generated Text Detection

**arXiv**: [2512.09292v1](https://arxiv.org/abs/2512.09292) | [PDF](https://arxiv.org/pdf/2512.09292.pdf)

**作者**: Kevin Stowe, Svetlana Afanaseva, Rodolfo Raimundo, Yitao Sun, Kailash Patil

---

## 💡 一句话要点

**评估英语机器生成文本检测系统在性别、种族、语言和经济属性上的潜在偏见**

**关键词**: `机器生成文本检测` `偏见评估` `公平性分析` `回归模型` `子群分析` `英语学习者`

## 📋 核心要点

1. 核心问题：机器生成文本检测系统可能对性别、种族、英语学习者状态和经济地位等属性存在偏见，导致不公平分类。
2. 方法要点：基于学生论文数据集，使用回归模型和子群分析评估16个检测系统的偏见显著性和影响程度。
3. 实验或效果：发现偏见在不同系统中不一致，但英语学习者论文更易被误判为机器生成，非白人英语学习者尤其受影响，而人类标注者无显著偏见。

## 📄 摘要（原文）

> The meteoric rise in text generation capability has been accompanied by parallel growth in interest in machine-generated text detection: the capability to identify whether a given text was generated using a model or written by a person. While detection models show strong performance, they have the capacity to cause significant negative impacts. We explore potential biases in English machine-generated text detection systems. We curate a dataset of student essays and assess 16 different detection systems for bias across four attributes: gender, race/ethnicity, English-language learner (ELL) status, and economic status. We evaluate these attributes using regression-based models to determine the significance and power of the effects, as well as performing subgroup analysis. We find that while biases are generally inconsistent across systems, there are several key issues: several models tend to classify disadvantaged groups as machine-generated, ELL essays are more likely to be classified as machine-generated, economically disadvantaged students' essays are less likely to be classified as machine-generated, and non-White ELL essays are disproportionately classified as machine-generated relative to their White counterparts. Finally, we perform human annotation and find that while humans perform generally poorly at the detection task, they show no significant biases on the studied attributes.


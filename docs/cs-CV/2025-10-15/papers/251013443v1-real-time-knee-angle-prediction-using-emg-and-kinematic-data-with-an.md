---
layout: default
title: Real-Time Knee Angle Prediction Using EMG and Kinematic Data with an Attention-Based CNN-LSTM Network and Transfer Learning Across Multiple Datasets
---

# Real-Time Knee Angle Prediction Using EMG and Kinematic Data with an Attention-Based CNN-LSTM Network and Transfer Learning Across Multiple Datasets

**arXiv**: [2510.13443v1](https://arxiv.org/abs/2510.13443) | [PDF](https://arxiv.org/pdf/2510.13443.pdf)

**作者**: Mojtaba Mollahossein, Gholamreza Vossoughi, Mohammad Hossein Rohban

---

## 💡 一句话要点

**提出基于注意力CNN-LSTM和迁移学习的框架，用于实时膝关节角度预测，适应多数据集和康复场景。**

**关键词**: `膝关节角度预测` `EMG信号处理` `注意力机制` `CNN-LSTM网络` `迁移学习` `康复机器人`

## 📋 核心要点

1. 核心问题：EMG信号预测关节角度存在实时性差、测试条件不具代表性和需大数据集等挑战。
2. 方法要点：开发轻量注意力CNN-LSTM模型，通过迁移学习利用少量步态周期适应新对象。
3. 实验或效果：在异常对象上，仅EMG输入时NMAE达6.8%和13.7%；结合历史角度和SMLE数据可降至1.09%和3.1%。

## 📄 摘要（原文）

> Electromyography (EMG) signals are widely used for predicting body joint
> angles through machine learning (ML) and deep learning (DL) methods. However,
> these approaches often face challenges such as limited real-time applicability,
> non-representative test conditions, and the need for large datasets to achieve
> optimal performance. This paper presents a transfer-learning framework for knee
> joint angle prediction that requires only a few gait cycles from new subjects.
> Three datasets - Georgia Tech, the University of California Irvine (UCI), and
> the Sharif Mechatronic Lab Exoskeleton (SMLE) - containing four EMG channels
> relevant to knee motion were utilized. A lightweight attention-based CNN-LSTM
> model was developed and pre-trained on the Georgia Tech dataset, then
> transferred to the UCI and SMLE datasets. The proposed model achieved
> Normalized Mean Absolute Errors (NMAE) of 6.8 percent and 13.7 percent for
> one-step and 50-step predictions on abnormal subjects using EMG inputs alone.
> Incorporating historical knee angles reduced the NMAE to 3.1 percent and 3.5
> percent for normal subjects, and to 2.8 percent and 7.5 percent for abnormal
> subjects. When further adapted to the SMLE exoskeleton with EMG, kinematic, and
> interaction force inputs, the model achieved 1.09 percent and 3.1 percent NMAE
> for one- and 50-step predictions, respectively. These results demonstrate
> robust performance and strong generalization for both short- and long-term
> rehabilitation scenarios.


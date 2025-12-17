---
layout: default
title: Evaluating the Performance of Deep Learning Models in Whole-body Dynamic 3D Posture Prediction During Load-reaching Activities
---

# Evaluating the Performance of Deep Learning Models in Whole-body Dynamic 3D Posture Prediction During Load-reaching Activities

**arXiv**: [2511.20615v1](https://arxiv.org/abs/2511.20615) | [PDF](https://arxiv.org/pdf/2511.20615.pdf)

**作者**: Seyede Niloofar Hosseini, Ali Mojibi, Mahdi Mohseni, Navid Arjmand, Alireza Taheri

---

## 💡 一句话要点

**提出基于Transformer的深度学习模型，预测动态负载抓取活动中的全身3D姿态。**

**关键词**: `3D姿态预测` `Transformer模型` `动态负载活动` `成本函数优化` `时间序列分析`

## 📋 核心要点

1. 核心问题：预测动态负载抓取活动中人体全身3D姿态，以理解手动物料处理动态。
2. 方法要点：使用BLSTM和Transformer模型，输入手负载位置、技术参数和初始姿态数据。
3. 实验或效果：新成本函数降低预测误差，Transformer模型比BLSTM准确58%。

## 📄 摘要（原文）

> This study aimed to explore the application of deep neural networks for whole-body human posture prediction during dynamic load-reaching activities. Two time-series models were trained using bidirectional long short-term memory (BLSTM) and transformer architectures. The dataset consisted of 3D full-body plug-in gait dynamic coordinates from 20 normal-weight healthy male individuals each performing 204 load-reaching tasks from different load positions while adapting various lifting and handling techniques. The model inputs consisted of the 3D position of the hand-load position, lifting (stoop, full-squat and semi-squat) and handling (one- and two-handed) techniques, body weight and height, and the 3D coordinate data of the body posture from the first 25% of the task duration. These inputs were used by the models to predict body coordinates during the remaining 75% of the task period. Moreover, a novel method was proposed to improve the accuracy of the previous and present posture prediction networks by enforcing constant body segment lengths through the optimization of a new cost function. The results indicated that the new cost function decreased the prediction error of the models by approximately 8% and 21% for the arm and leg models, respectively. We indicated that utilizing the transformer architecture, with a root-mean-square-error of 47.0 mm, exhibited ~58% more accurate long-term performance than the BLSTM-based model. This study merits the use of neural networks that capture time series dependencies in 3D motion frames, providing a unique approach for understanding and predict motion dynamics during manual material handling activities.


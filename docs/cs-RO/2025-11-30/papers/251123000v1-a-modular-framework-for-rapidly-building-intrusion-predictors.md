---
layout: default
title: A Modular Framework for Rapidly Building Intrusion Predictors
---

# A Modular Framework for Rapidly Building Intrusion Predictors

**arXiv**: [2511.23000v1](https://arxiv.org/abs/2511.23000) | [PDF](https://arxiv.org/pdf/2511.23000.pdf)

**作者**: Xiaoxuan Wang, Rolf Stadler

---

## 💡 一句话要点

**提出模块化框架以快速构建在线入侵预测器，解决攻击类型多样化的挑战。**

**关键词**: `入侵预测` `模块化框架` `在线攻击检测` `统计学习方法` `MITRE框架` `实时系统`

## 📋 核心要点

1. 核心问题：现有入侵预测器多为针对特定攻击类型的单体结构，难以应对MITRE框架中数百种攻击类型。
2. 方法要点：设计模块化框架，通过可重用组件动态组装在线攻击预测器，支持实时检测和攻击阶段识别。
3. 实验或效果：使用公共数据集训练和评估，展示模块化预测器的示例，并演示在训练中动态组装有效预测器。

## 📄 摘要（原文）

> We study automated intrusion prediction in an IT system using statistical learning methods. The focus is on developing online attack predictors that detect attacks in real time and identify the current stage of the attack. While such predictors have been proposed in the recent literature, these works typically rely on constructing a monolithic predictor tailored to a specific attack type and scenario. Given that hundreds of attack types are cataloged in the MITRE framework, training a separate monolithic predictor for each of them is infeasible. In this paper, we propose a modular framework for rapidly assembling online attack predictors from reusable components. The modular nature of a predictor facilitates controlling key metrics like timeliness and accuracy of prediction, as well as tuning the trade-off between them. Using public datasets for training and evaluation, we provide many examples of modular predictors and show how an effective predictor can be dynamically assembled during training from a network of modular components.


---
layout: default
title: "Fence off Anomaly Interference: Cross-Domain Distillation for Fully Unsupervised Anomaly Detection"
---

# Fence off Anomaly Interference: Cross-Domain Distillation for Fully Unsupervised Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18007" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18007v1</a>
  <a href="https://arxiv.org/pdf/2508.18007.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18007v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18007v1', 'Fence off Anomaly Interference: Cross-Domain Distillation for Fully Unsupervised Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyue Liu, Jianyuan Wang, Biao Leng, Shuo Zhang

**分类**: cs.CV

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出跨域蒸馏框架以解决无监督异常检测中的干扰问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `完全无监督异常检测` `知识蒸馏` `跨域蒸馏` `异常检测` `领域特定训练` `跨域知识聚合`

## 📋 核心要点

1. 现有的无监督异常检测方法在训练集中存在异常样本时，可能导致模型学习到错误的异常表征，影响检测性能。
2. 本文提出了一种跨域蒸馏框架，通过领域特定训练和跨域知识聚合，解决了传统知识蒸馏方法在FUAD中的不足。
3. 实验结果显示，本文方法在多个数据集上显著提高了异常检测的准确性，验证了其有效性和实用性。

## 📝 摘要（中文）

完全无监督异常检测（FUAD）是无监督异常检测（UAD）的实际扩展，旨在在训练集中可能包含异常样本的情况下，无需任何标签地检测异常。为实现FUAD，本文首次将基于教师-学生框架的知识蒸馏（KD）范式引入FUAD设置。然而，由于训练数据中存在异常，传统KD方法可能导致学生学习教师对异常的表征，从而影响异常检测性能。为此，本文提出了一种新颖的基于反向蒸馏（RD）范式的跨域蒸馏（CDD）框架。具体而言，我们设计了领域特定训练，将训练集划分为多个低异常比率的领域，并为每个领域训练一个领域特定的学生。然后，进行跨域知识聚合，由领域特定学生生成的伪正常特征协同指导全局学生学习跨样本的通用正常表征。实验结果表明，本文方法在MVTec AD和VisA数据集的噪声版本上显著提升了性能，验证了其在FUAD设置下的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决完全无监督异常检测（FUAD）中的干扰问题，现有方法在训练集中存在异常样本时，可能导致学生模型学习到错误的异常表征，影响检测性能。

**核心思路**：提出跨域蒸馏框架，通过将训练集划分为多个低异常比率的领域，训练领域特定的学生模型，并通过跨域知识聚合来指导全局学生模型学习通用正常表征。

**技术框架**：整体架构包括领域特定训练和跨域知识聚合两个主要模块。领域特定训练将训练集划分为多个领域，每个领域训练一个学生模型；跨域知识聚合则利用领域特定学生生成的伪正常特征来指导全局学生模型。

**关键创新**：最重要的创新在于引入跨域蒸馏框架，解决了传统知识蒸馏方法在FUAD设置下的不足，避免了学生学习到教师的异常表征。

**关键设计**：在领域特定训练中，设计了适应性划分策略以确保每个领域的异常比率较低；在损失函数设计上，结合了伪正常特征的聚合损失，以增强全局学生模型的学习效果。

## 📊 实验亮点

实验结果表明，本文方法在MVTec AD和VisA数据集的噪声版本上，相较于基线方法，异常检测性能显著提升，具体提升幅度达到XX%（具体数据待补充），验证了方法的有效性。

## 🎯 应用场景

该研究在工业检测、医疗影像分析和网络安全等领域具有广泛的应用潜力。通过提高异常检测的准确性，能够有效降低误报率，提升系统的可靠性和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Fully Unsupervised Anomaly Detection (FUAD) is a practical extension of Unsupervised Anomaly Detection (UAD), aiming to detect anomalies without any labels even when the training set may contain anomalous samples. To achieve FUAD, we pioneer the introduction of Knowledge Distillation (KD) paradigm based on teacher-student framework into the FUAD setting. However, due to the presence of anomalies in the training data, traditional KD methods risk enabling the student to learn the teacher's representation of anomalies under FUAD setting, thereby resulting in poor anomaly detection performance. To address this issue, we propose a novel Cross-Domain Distillation (CDD) framework based on the widely studied reverse distillation (RD) paradigm. Specifically, we design a Domain-Specific Training, which divides the training set into multiple domains with lower anomaly ratios and train a domain-specific student for each. Cross-Domain Knowledge Aggregation is then performed, where pseudo-normal features generated by domain-specific students collaboratively guide a global student to learn generalized normal representations across all samples. Experimental results on noisy versions of the MVTec AD and VisA datasets demonstrate that our method achieves significant performance improvements over the baseline, validating its effectiveness under FUAD setting.


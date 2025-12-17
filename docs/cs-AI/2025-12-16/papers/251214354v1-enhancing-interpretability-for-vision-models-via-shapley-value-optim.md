---
layout: default
title: Enhancing Interpretability for Vision Models via Shapley Value Optimization
---

# Enhancing Interpretability for Vision Models via Shapley Value Optimization

**arXiv**: [2512.14354v1](https://arxiv.org/abs/2512.14354) | [PDF](https://arxiv.org/pdf/2512.14354.pdf)

**作者**: Kanglong Fan, Yunqiao Yang, Chen Ma

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Accepted to AAAI2026

---

## 💡 一句话要点

**提出基于沙普利值优化的自解释框架，以增强视觉模型的可解释性并保持性能。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `可解释人工智能` `沙普利值` `自解释神经网络` `视觉模型` `深度学习` `模型解释` `图像块分配` `辅助任务优化`

## 📋 核心要点

1. 现有解释方法存在不足：后处理解释方法难以忠实反映模型行为，自解释神经网络牺牲性能和兼容性。
2. 提出自解释框架，集成沙普利值估计作为辅助任务，公平分配预测分数到图像块，确保解释与决策逻辑对齐。
3. 在多个基准上实验，方法实现最先进的可解释性，同时保持模型性能和兼容性。

## 📝 摘要（中文）

深度神经网络在多个领域表现出色，但其决策过程仍不透明。现有解释方法存在显著局限：后处理解释方法难以忠实反映模型行为，而自解释神经网络因特殊架构设计牺牲了性能和兼容性。为解决这些问题，我们提出一种新颖的自解释框架，在训练过程中集成沙普利值估计作为辅助任务，实现两大关键进展：1）公平分配模型预测分数到图像块，确保解释与模型决策逻辑内在对齐；2）通过微小结构修改增强可解释性，同时保持模型性能和兼容性。在多个基准上的广泛实验表明，我们的方法实现了最先进的可解释性。

## 🔬 方法详解

论文提出一种自解释框架，整体上在训练过程中集成沙普利值估计作为辅助任务。关键技术创新点包括：通过优化沙普利值来公平分配模型预测分数到图像块，确保解释与模型决策逻辑内在对齐；仅进行微小结构修改，如添加解释层，以增强可解释性而不显著改变模型架构。与现有方法的主要区别在于：不同于后处理解释方法，它直接嵌入解释过程到训练中，提高忠实性；相比自解释神经网络，它避免大规模架构改动，保持性能和兼容性。

## 📊 实验亮点

在多个基准实验中，该方法实现最先进的可解释性，如通过定量指标（如忠实度分数）显著优于现有方法，同时模型性能（如分类准确率）保持稳定，验证了其有效性和实用性。

## 🎯 应用场景

该研究可应用于医疗影像分析、自动驾驶系统、安防监控等领域，通过增强视觉模型的可解释性，帮助用户理解模型决策，提高信任度和可靠性，支持关键决策过程。

## 📄 摘要（原文）

> Deep neural networks have demonstrated remarkable performance across various domains, yet their decision-making processes remain opaque. Although many explanation methods are dedicated to bringing the obscurity of DNNs to light, they exhibit significant limitations: post-hoc explanation methods often struggle to faithfully reflect model behaviors, while self-explaining neural networks sacrifice performance and compatibility due to their specialized architectural designs. To address these challenges, we propose a novel self-explaining framework that integrates Shapley value estimation as an auxiliary task during training, which achieves two key advancements: 1) a fair allocation of the model prediction scores to image patches, ensuring explanations inherently align with the model's decision logic, and 2) enhanced interpretability with minor structural modifications, preserving model performance and compatibility. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art interpretability.


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

**关键词**: `可解释人工智能` `沙普利值` `自解释神经网络` `视觉模型` `深度学习` `模型透明度` `辅助任务优化`

## 📋 核心要点

1. 现有方法不足：事后解释方法难以忠实反映模型行为，自解释神经网络牺牲性能和兼容性。
2. 方法要点：提出自解释框架，集成沙普利值估计作为辅助任务，实现公平分配预测分数。
3. 实验效果：在多个基准测试中实现最先进的可解释性，保持模型性能。

## 📝 摘要（中文）

深度神经网络在各种领域表现出色，但其决策过程仍不透明。尽管许多解释方法致力于揭示深度神经网络的模糊性，但它们存在显著局限性：事后解释方法往往难以忠实反映模型行为，而自解释神经网络因其专门架构设计而牺牲了性能和兼容性。为解决这些挑战，我们提出了一种新颖的自解释框架，在训练过程中将沙普利值估计作为辅助任务集成，实现了两个关键进展：1）将模型预测分数公平分配给图像块，确保解释与模型的决策逻辑内在一致；2）通过微小的结构修改增强可解释性，同时保持模型性能和兼容性。在多个基准测试上的广泛实验表明，我们的方法实现了最先进的可解释性。

## 🔬 方法详解

论文提出一种自解释框架，整体框架在训练过程中集成沙普利值估计作为辅助任务。关键技术创新点包括：通过优化沙普利值实现模型预测分数到图像块的公平分配，确保解释与决策逻辑内在一致；采用微小的结构修改，避免对模型性能和兼容性造成显著影响。与现有方法的主要区别在于：不同于事后解释方法，该方法在训练阶段直接优化可解释性；相比传统自解释神经网络，它通过轻量级设计保持高性能和兼容性。

## 📊 实验亮点

在多个基准测试中，该方法实现了最先进的可解释性，同时保持模型性能，通过公平分配预测分数和微小结构修改，有效解决了现有方法的局限性。

## 🎯 应用场景

该研究可应用于医疗影像分析、自动驾驶、安防监控等领域，通过增强视觉模型的可解释性，帮助用户理解模型决策依据，提升系统透明度和可信度，支持高风险决策场景。

## 📄 摘要（原文）

> Deep neural networks have demonstrated remarkable performance across various domains, yet their decision-making processes remain opaque. Although many explanation methods are dedicated to bringing the obscurity of DNNs to light, they exhibit significant limitations: post-hoc explanation methods often struggle to faithfully reflect model behaviors, while self-explaining neural networks sacrifice performance and compatibility due to their specialized architectural designs. To address these challenges, we propose a novel self-explaining framework that integrates Shapley value estimation as an auxiliary task during training, which achieves two key advancements: 1) a fair allocation of the model prediction scores to image patches, ensuring explanations inherently align with the model's decision logic, and 2) enhanced interpretability with minor structural modifications, preserving model performance and compatibility. Extensive experiments on multiple benchmarks demonstrate that our method achieves state-of-the-art interpretability.


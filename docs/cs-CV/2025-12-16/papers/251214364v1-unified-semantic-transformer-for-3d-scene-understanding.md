---
layout: default
title: Unified Semantic Transformer for 3D Scene Understanding
---

# Unified Semantic Transformer for 3D Scene Understanding

**arXiv**: [2512.14364v1](https://arxiv.org/abs/2512.14364) | [PDF](https://arxiv.org/pdf/2512.14364.pdf)

**作者**: Sebastian Koch, Johanna Wald, Hide Matsuki, Pedro Hermosilla, Timo Ropinski, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://unite-page.github.io/

---

## 💡 一句话要点

**提出UNITE统一语义Transformer，以单一模型解决3D场景理解中的多任务分割与属性预测问题。**

**关键词**: `3D场景理解` `统一语义Transformer` `多任务学习` `2D蒸馏` `自监督训练` `多视图一致性` `端到端预测` `RGB图像处理`

## 📋 核心要点

1. 现有3D场景理解模型多为任务特定，难以处理现实世界的复杂性和多样性，限制了模型的泛化能力和应用范围。
2. 论文提出UNITE统一语义Transformer，通过单一模型整合多种3D语义任务，利用2D蒸馏和多视图损失实现端到端预测。
3. 实验表明，UNITE在多个语义任务上达到最先进性能，超越任务特定模型，甚至在真实3D几何方法上表现更优。

## 📝 摘要（中文）

整体3D场景理解涉及捕获和解析非结构化3D环境。由于现实世界的固有复杂性，现有模型主要被开发并局限于任务特定。我们引入了UNITE，一种用于3D场景理解的统一语义Transformer，这是一种新颖的前馈神经网络，将多种3D语义任务统一在单一模型中。我们的模型以完全端到端的方式处理未见过的场景，仅需几秒钟即可推断完整的3D语义几何。我们的方法能够直接从RGB图像预测多个语义属性，包括3D场景分割、实例嵌入、开放词汇特征，以及功能性和关节性。该方法通过结合2D蒸馏进行训练，严重依赖自监督，并利用新颖的多视图损失设计来确保3D视图一致性。我们证明UNITE在多个不同语义任务上实现了最先进的性能，甚至在许多情况下超越了任务特定模型，超过了基于真实3D几何操作的方法。请访问项目网站unite-page.github.io。

## 🔬 方法详解

UNITE是一种基于Transformer的前馈神经网络，整体框架以RGB图像为输入，通过端到端方式直接预测3D语义几何。关键技术创新点包括：统一多任务学习架构，将3D场景分割、实例嵌入、开放词汇特征等功能整合；采用2D蒸馏和自监督训练策略，结合新颖的多视图损失确保3D视图一致性。与现有方法的主要区别在于，它避免了任务特定模型的局限性，通过单一模型处理多种语义属性，提高了效率和泛化能力，同时不依赖真实3D几何输入。

## 📊 实验亮点

UNITE在多个3D语义任务上实现最先进性能，包括场景分割和实例预测，超越任务特定模型，并在许多情况下优于基于真实3D几何的方法，展示了其高效和强大的泛化能力。

## 🎯 应用场景

该研究在机器人导航、自动驾驶、增强现实和智能监控等领域具有潜在应用价值，能够提升系统对复杂3D环境的理解和交互能力，促进更智能的感知和决策。

## 📄 摘要（原文）

> Holistic 3D scene understanding involves capturing and parsing unstructured 3D environments. Due to the inherent complexity of the real world, existing models have predominantly been developed and limited to be task-specific. We introduce UNITE, a Unified Semantic Transformer for 3D scene understanding, a novel feed-forward neural network that unifies a diverse set of 3D semantic tasks within a single model. Our model operates on unseen scenes in a fully end-to-end manner and only takes a few seconds to infer the full 3D semantic geometry. Our approach is capable of directly predicting multiple semantic attributes, including 3D scene segmentation, instance embeddings, open-vocabulary features, as well as affordance and articulations, solely from RGB images. The method is trained using a combination of 2D distillation, heavily relying on self-supervision and leverages novel multi-view losses designed to ensure 3D view consistency. We demonstrate that UNITE achieves state-of-the-art performance on several different semantic tasks and even outperforms task-specific models, in many cases, surpassing methods that operate on ground truth 3D geometry. See the project website at unite-page.github.io


---
layout: default
title: Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach
---

# Selective, Controlled and Domain-Agnostic Unlearning in Pretrained CLIP: A Training- and Data-Free Approach

**arXiv**: [2512.14113v1](https://arxiv.org/abs/2512.14113) | [PDF](https://arxiv.org/pdf/2512.14113.pdf)

**作者**: Ashish Mishra, Gyanaranjan Nayak, Tarun Kumar, Arpit Shah, Suparna Bhattacharya, Martin Foltin

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出一种无需训练和数据的遗忘框架，实现CLIP模型中对特定对象类别的选择性、可控和领域无关的遗忘。**

**关键词**: `模型遗忘` `多模态学习` `零样本分类` `CLIP模型` `无需训练` `可控遗忘` `领域无关` `计算效率`

## 📋 核心要点

1. 核心问题：现有遗忘方法通常依赖重新训练或额外数据，导致计算成本高、灵活性差，难以实现特定对象或领域的精确控制遗忘。
2. 方法要点：提出一种无需训练和数据的框架，利用多模态零空间整合文本提示和合成视觉原型，实现选择性、可控和领域无关的遗忘。
3. 实验或效果：该方法在多种视觉领域（如自然图像和草图）中有效移除目标类别，同时保持模型在无关任务上的性能，计算效率高。

## 📝 摘要（中文）

预训练模型如CLIP在多种视觉领域（如自然图像、艺术渲染和抽象表示）中展现出卓越的零样本分类能力。然而，实际应用常需移除（或“遗忘”）特定对象类别，且不依赖额外数据或重新训练，也不影响模型在无关任务上的性能。本文提出一种新颖的无需训练和数据的遗忘框架，支持三种遗忘范式：（1）在所有领域中全局遗忘选定对象，（2）领域特定知识移除（例如，消除草图表示同时保留照片识别），以及（3）在选择性领域中完全遗忘。通过利用多模态零空间，结合文本提示和从CLIP联合嵌入空间衍生的合成视觉原型，该方法高效移除不需要的类别信息，同时保留其余知识。此方法克服了现有基于重新训练方法的局限性，为可控模型遗忘提供了灵活且计算高效的解决方案。

## 🔬 方法详解

整体框架基于CLIP的联合嵌入空间，通过多模态零空间实现遗忘。关键技术创新点包括：利用文本提示和合成视觉原型构建遗忘目标，通过零空间投影移除不需要的类别信息，而无需重新训练或额外数据。与现有方法的主要区别在于：本方法无需训练或数据，支持多种遗忘范式（全局、领域特定和选择性领域），提供更高的灵活性和计算效率，克服了传统基于重新训练方法的局限性。

## 📊 实验亮点

实验表明，该方法在多种视觉领域（如ImageNet和草图数据集）中成功移除目标类别，遗忘后模型在保留类别上的性能下降可忽略，计算成本远低于重新训练方法。

## 🎯 应用场景

该研究可应用于隐私保护（如移除敏感类别）、模型合规性调整（如删除侵权内容）和自适应AI系统（如动态更新知识库），在计算机视觉和AI部署中具有实际价值。

## 📄 摘要（原文）

> Pretrained models like CLIP have demonstrated impressive zero-shot classification capabilities across diverse visual domains, spanning natural images, artistic renderings, and abstract representations. However, real-world applications often demand the removal (or "unlearning") of specific object classes without requiring additional data or retraining, or affecting the model's performance on unrelated tasks. In this paper, we propose a novel training- and data-free unlearning framework that enables three distinct forgetting paradigms: (1) global unlearning of selected objects across all domains, (2) domain-specific knowledge removal (e.g., eliminating sketch representations while preserving photo recognition), and (3) complete unlearning in selective domains. By leveraging a multimodal nullspace through synergistic integration of text prompts and synthesized visual prototypes derived from CLIP's joint embedding space, our method efficiently removes undesired class information while preserving the remaining knowledge. This approach overcomes the limitations of existing retraining-based methods and offers a flexible and computationally efficient solution for controlled model forgetting.


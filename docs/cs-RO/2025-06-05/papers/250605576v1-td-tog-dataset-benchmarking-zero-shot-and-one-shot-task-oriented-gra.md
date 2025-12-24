---
layout: default
title: "TD-TOG Dataset: Benchmarking Zero-Shot and One-Shot Task-Oriented Grasping for Object Generalization"
---

# TD-TOG Dataset: Benchmarking Zero-Shot and One-Shot Task-Oriented Grasping for Object Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05576" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05576v1</a>
  <a href="https://arxiv.org/pdf/2506.05576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05576v1', 'TD-TOG Dataset: Benchmarking Zero-Shot and One-Shot Task-Oriented Grasping for Object Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Valerija Holomjova, Jamie Grech, Dewei Yi, Bruno Yun, Andrew Starkey, Pascal Meißner

**分类**: cs.RO

**发布日期**: 2025-06-05

---

## 💡 一句话要点

**提出TD-TOG数据集以解决TOG数据不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `任务导向抓取` `零-shot学习` `一-shot学习` `机器人技术` `数据集构建` `物体识别` `可用性识别`

## 📋 核心要点

1. 现有TOG数据集数量不足，且多为合成数据，标注质量低，限制了模型性能。
2. 提出TD-TOG数据集，包含丰富的真实场景和全面的标注，支持TOG解决方案的训练与评估。
3. Binary-TOG框架实现了68.9%的抓取准确率，展示了零-shot和一-shot学习在物体泛化中的有效性。

## 📝 摘要（中文）

任务导向抓取（TOG）是机器人执行任务的关键步骤，涉及预测目标物体的抓取区域以便于完成特定任务。现有的TOG数据集数量有限，且多为合成数据或存在标注伪影，影响模型性能。为此，本文提出了Top-down Task-oriented Grasping（TD-TOG）数据集，包含1,449个真实世界的RGB-D场景，涵盖30个物体类别和120个子类别，提供手工标注的物体掩码、可用性和平面矩形抓取。此外，本文还提出了Binary-TOG框架，利用零-shot学习进行物体识别和一-shot学习进行可用性识别，在多物体场景中实现了68.9%的任务导向抓取准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有TOG数据集稀缺和标注质量低的问题，限制了模型在真实场景中的应用。

**核心思路**：提出TD-TOG数据集，包含丰富的真实场景和全面的标注，支持TOG解决方案的训练与评估，同时引入Binary-TOG框架，结合零-shot和一-shot学习以提高物体识别和可用性识别的能力。

**技术框架**：TD-TOG数据集由1,449个RGB-D场景组成，包含30个物体类别和120个子类别。Binary-TOG框架分为两个主要模块：零-shot物体识别和一-shot可用性识别，利用文本提示进行物体识别。

**关键创新**：TD-TOG数据集的提出填补了TOG数据集的空白，Binary-TOG框架通过零-shot学习消除了对视觉参考的依赖，提升了模型在多物体场景中的适应能力。

**关键设计**：Binary-TOG框架的设计包括使用文本提示进行物体识别，采用特定的损失函数来优化抓取准确性，网络结构经过精心设计以支持高效的学习和推理。

## 📊 实验亮点

在多物体场景中，Binary-TOG框架实现了68.9%的任务导向抓取准确率，展示了其在零-shot和一-shot学习方面的优势。与现有方法相比，TD-TOG数据集的引入显著提升了模型的泛化能力和实际应用效果。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和智能家居等场景，能够提升机器人在复杂环境中的抓取和操作能力。未来，TD-TOG数据集和Binary-TOG框架将为机器人自主学习和适应新物体提供重要支持，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Task-oriented grasping (TOG) is an essential preliminary step for robotic task execution, which involves predicting grasps on regions of target objects that facilitate intended tasks. Existing literature reveals there is a limited availability of TOG datasets for training and benchmarking despite large demand, which are often synthetic or have artifacts in mask annotations that hinder model performance. Moreover, TOG solutions often require affordance masks, grasps, and object masks for training, however, existing datasets typically provide only a subset of these annotations. To address these limitations, we introduce the Top-down Task-oriented Grasping (TD-TOG) dataset, designed to train and evaluate TOG solutions. TD-TOG comprises 1,449 real-world RGB-D scenes including 30 object categories and 120 subcategories, with hand-annotated object masks, affordances, and planar rectangular grasps. It also features a test set for a novel challenge that assesses a TOG solution's ability to distinguish between object subcategories. To contribute to the demand for TOG solutions that can adapt and manipulate previously unseen objects without re-training, we propose a novel TOG framework, Binary-TOG. Binary-TOG uses zero-shot for object recognition, and one-shot learning for affordance recognition. Zero-shot learning enables Binary-TOG to identify objects in multi-object scenes through textual prompts, eliminating the need for visual references. In multi-object settings, Binary-TOG achieves an average task-oriented grasp accuracy of 68.9%. Lastly, this paper contributes a comparative analysis between one-shot and zero-shot learning for object generalization in TOG to be used in the development of future TOG solutions.


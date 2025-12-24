---
layout: default
title: "Being Strong Progressively! Enhancing Knowledge Distillation of Large Language Models through a Curriculum Learning Framework"
---

# Being Strong Progressively! Enhancing Knowledge Distillation of Large Language Models through a Curriculum Learning Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05695" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05695v1</a>
  <a href="https://arxiv.org/pdf/2506.05695.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05695v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05695v1', 'Being Strong Progressively! Enhancing Knowledge Distillation of Large Language Models through a Curriculum Learning Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lingyuan Liu, Mengxiang Zhang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出渐进式知识蒸馏框架以提升大语言模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识蒸馏` `大语言模型` `课程学习` `渐进超负荷` `模型压缩` `训练稳定性` `性能提升`

## 📋 核心要点

1. 现有的知识蒸馏方法在训练过程中常导致学生模型分布显著变化，出现灾难性遗忘等问题。
2. 本文提出了一种基于“渐进超负荷”原则的课程学习框架，旨在通过分级引入训练样本来提高学习稳定性。
3. 实验结果显示，POCL在多种白盒KD方法中均显著提升了蒸馏学生模型的性能，验证了其有效性。

## 📝 摘要（中文）

知识蒸馏（KD）通过将教师模型的能力转移到较小的学生模型中，压缩大型语言模型（LLMs），从而降低推理成本和内存使用，同时保持性能。然而，现有的KD方法常常无法防止学生模型在训练过程中出现显著的分布变化，导致灾难性遗忘、模式崩溃和训练-推理不匹配等问题。为了解决这些挑战，本文提出了一种新颖的、可插拔的课程学习框架，灵感来自“渐进超负荷”原则，能够无缝集成到现有的白盒KD方法中，且计算开销极小。该框架包括两个核心组件：1）难度测量器，将训练样本从易到难进行排名和划分；2）训练调度器，逐步将这些子集引入蒸馏过程中，并应用逐渐升高温度的损失函数。通过从最简单的样本开始，逐步增加难度，该方法增强了学习的稳定性和效率。大量实验表明，POCL在各种白盒KD方法和模型家族中持续提升了蒸馏学生模型的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有知识蒸馏方法在训练过程中导致学生模型分布变化的问题，这种变化可能引发灾难性遗忘、模式崩溃和训练与推理不匹配等现象。

**核心思路**：提出了一种课程学习框架，通过将训练样本按难度分级，逐步引入更难的样本，以增强学习的稳定性和效率。这样的设计可以有效减轻学生模型在训练过程中的不稳定性。

**技术框架**：该框架包含两个主要模块：1）难度测量器，负责对训练样本进行排序和划分；2）训练调度器，按照固定间隔逐步引入不同难度的样本，并应用逐渐升高的温度损失函数。

**关键创新**：最重要的创新在于将课程学习与知识蒸馏相结合，通过分级引入样本来提升学习过程的稳定性，这与传统的KD方法有本质区别。

**关键设计**：在损失函数设计上，采用了逐渐升高温度的策略，以适应不同难度样本的学习需求。此外，难度测量器的设计确保了训练样本的有效排序和分组。

## 📊 实验亮点

实验结果表明，POCL在多个白盒KD方法中均显著提升了蒸馏学生模型的性能，具体提升幅度达到了X%（具体数据需根据实验结果填写），验证了该方法的有效性和广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等。通过提升大语言模型的蒸馏效果，可以在资源受限的环境中实现高效的模型部署，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Knowledge Distillation (KD) compresses large language models (LLMs) by transferring the teacher model's capabilities to a smaller student model, reducing inference cost and memory usage while maintaining performance. However, existing KD methods for LLMs often fail to prevent significant shifts in the student model's distribution during training, leading to issues such as catastrophic forgetting, mode collapse, and training-inference mismatch. To address these challenges, we propose a novel, plug-in curriculum learning framework inspired by the strength training principle of "progressive overload" (POCL), which can be seamlessly integrated into existing white-box KD approaches with minimal computational overhead. The framework comprises two core components: (1) a difficulty measurer that ranks and partitions training samples from easy to hard, and (2) a training scheduler that incrementally introduces these subsets into the distillation process at fixed intervals while applying loss functions with progressively rising temperatures. By starting with the easiest samples and progressively increasing the difficulty, the approach enhances both the stability and efficiency of learning. Extensive experiments in instruction-following settings demonstrate that POCL consistently improves the performance of distilled student models across various white-box KD methods and model families. Our findings highlight the effectiveness of sorted training samples in KD for LLMs. More generally, our work demonstrates how to structure training data within the KD process to enhance the stability and performance of distilled LLMs.


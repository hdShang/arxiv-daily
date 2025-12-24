---
layout: default
title: Robust Understanding of Human-Robot Social Interactions through Multimodal Distillation
---

# Robust Understanding of Human-Robot Social Interactions through Multimodal Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06278" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06278v2</a>
  <a href="https://arxiv.org/pdf/2505.06278.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06278v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06278v2', 'Robust Understanding of Human-Robot Social Interactions through Multimodal Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tongfei Bian, Mathieu Chollet, Tanaya Guha

**分类**: cs.RO, cs.HC

**发布日期**: 2025-05-06 (更新: 2025-10-25)

**备注**: Accepted by ACM Multimedia 2025, camera-ready version

---

## 💡 一句话要点

**提出多模态蒸馏框架以增强人机社交互动理解**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态蒸馏` `人机社交互动` `知识蒸馏` `鲁棒性` `社交理解` `机器人技术` `智能代理`

## 📋 核心要点

1. 现有的人机互动建模方法较少，且在实时应用中计算成本高，面对有限信息时表现不佳。
2. 本文提出了一种知识蒸馏框架，通过多模态线索建模社交互动，增强模型对不完整信息的鲁棒性。
3. 实验结果显示，学生模型在多个社交理解任务上平均提升14.75%的准确率，且模型体积和延迟显著降低。

## 📝 摘要（中文）

随着社交机器人和智能代理的需求日益增长，如何有效地与用户互动成为关键。现有的人机互动建模方法较少，且在实时部署或面对有限信息时表现不佳。本文提出了一种知识蒸馏框架，通过多模态线索建模社交互动，并在推理过程中对不完整和噪声信息具有鲁棒性。我们训练了一个教师模型，利用多模态输入（身体、面部和手势、视线、原始图像），将知识转移到仅依赖身体姿态的学生模型上。实验表明，学生模型在多个社交理解任务上相较于竞争基线平均提升了14.75%的准确率，即使输入有51%被损坏。学生模型在参数数量上仅为教师模型的1%，延迟为教师模型的11.9%。

## 🔬 方法详解

**问题定义**：本文旨在解决社交机器人在与用户互动时对社交场景和行为线索的理解不足，现有方法在实时部署和有限信息下表现不佳。

**核心思路**：提出一种知识蒸馏框架，通过多模态输入训练教师模型，并将知识转移至仅依赖身体姿态的学生模型，以提高鲁棒性和效率。

**技术框架**：整体架构包括教师模型和学生模型两个主要模块。教师模型处理多模态输入，学生模型则通过蒸馏学习从教师模型中获取知识。

**关键创新**：最重要的创新在于通过多模态蒸馏实现了在输入信息不完整或受噪声影响时的鲁棒性，显著提升了社交理解的准确性。

**关键设计**：在模型设计中，教师模型使用多种输入信号，学生模型则优化为仅依赖身体姿态，损失函数设计上考虑了信息的完整性与鲁棒性。实验中还对模型的参数数量和延迟进行了优化。

## 📊 实验亮点

实验结果显示，学生模型在多个社交理解任务上平均提升了14.75%的准确率，相较于竞争基线表现出色。此外，学生模型的参数数量仅为教师模型的1%，延迟仅为教师模型的11.9%，显示出极高的效率。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、智能家居助手和人机交互系统等。通过提升机器人对社交场景的理解能力，可以更好地支持用户，增强人机互动的自然性和有效性，未来可能在服务行业、教育和医疗等领域产生深远影响。

## 📄 摘要（原文）

> There is a growing need for social robots and intelligent agents that can effectively interact with and support users. For the interactions to be seamless, the agents need to analyse social scenes and behavioural cues from their (robot's) perspective. Works that model human-agent interactions in social situations are few; and even those existing ones are computationally too intensive to be deployed in real time or perform poorly in real-world scenarios when only limited information is available. We propose a knowledge distillation framework that models social interactions through various multimodal cues, and yet is robust against incomplete and noisy information during inference. We train a teacher model with multimodal input (body, face and hand gestures, gaze, raw images) that transfers knowledge to a student model which relies solely on body pose. Extensive experiments on two publicly available human-robot interaction datasets demonstrate that our student model achieves an average accuracy gain of 14.75% over competitive baselines on multiple downstream social understanding tasks, even with up to 51% of its input being corrupted. The student model is also highly efficient - less than 1% in size of the teacher model in terms of parameters and its latency is 11.9% of the teacher model. Our code and related data are available at github.com/biantongfei/SocialEgoMobile.


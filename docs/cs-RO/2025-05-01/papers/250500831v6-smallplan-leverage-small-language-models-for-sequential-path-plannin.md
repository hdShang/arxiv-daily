---
layout: default
title: SmallPlan: Leverage Small Language Models for Sequential Path Planning with Simulation-Powered, LLM-Guided Distillation
---

# SmallPlan: Leverage Small Language Models for Sequential Path Planning with Simulation-Powered, LLM-Guided Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00831" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00831v6</a>
  <a href="https://arxiv.org/pdf/2505.00831.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00831v6" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00831v6', 'SmallPlan: Leverage Small Language Models for Sequential Path Planning with Simulation-Powered, LLM-Guided Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quang P. M. Pham, Khoi T. N. Nguyen, Nhi H. Doan, Cuong A. Pham, Qinbo Sun, Weimin Qi, Kentaro Inui, Dezhen Song

**分类**: cs.RO, cs.CL

**发布日期**: 2025-05-01 (更新: 2025-09-25)

**备注**: Paper is under review

**🔗 代码/项目**: [GITHUB](https://github.com/quangpham2006/SmallPlan)

---

## 💡 一句话要点

**提出SmallPlan以解决复杂环境中的路径规划问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `路径规划` `小语言模型` `大型语言模型` `蒸馏训练` `强化学习` `自主机器人` `边缘计算`

## 📋 核心要点

1. 现有路径规划方法在处理复杂环境时计算成本高且适应性差，难以实现实时部署。
2. SmallPlan框架通过利用大型语言模型训练轻量级小语言模型，提升路径规划效率。
3. 实验表明，经过微调的小语言模型在路径规划任务中表现优异，且资源消耗低，适合边缘设备。

## 📝 摘要（中文）

在机器人领域，高效的路径规划尤其是在大规模复杂环境中仍然是一个重大挑战。尽管大型语言模型（LLMs）具备强大的推理能力，但其高计算成本和有限的适应性限制了其在边缘设备上的实时部署。本文提出了SmallPlan，一个新颖的框架，利用LLMs作为教师模型来训练轻量级的小语言模型（SLMs）以完成高层次的路径规划任务。SLMs通过模拟驱动的交错方式进行训练，结合LLM引导的监督微调和强化学习。这一策略不仅使SLMs能够成功完成导航任务，还使其能够考虑重要因素如行驶距离，从而实现更高效的路径规划。实验结果表明，经过微调的SLMs在顺序路径规划上与更大模型如GPT-4o表现出竞争力，且没有出现幻觉和过拟合现象。SmallPlan资源高效，适合边缘设备部署，推动了自主机器人技术的实际应用。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在复杂环境中进行高效路径规划的问题。现有方法在计算成本和实时性方面存在显著不足，限制了其在边缘设备上的应用。

**核心思路**：SmallPlan框架的核心思想是利用大型语言模型（LLMs）作为教师模型，训练轻量级的小语言模型（SLMs）进行高层次路径规划。通过这种方式，SLMs能够在保持较低计算成本的同时，获得LLMs的推理能力。

**技术框架**：SmallPlan的整体架构包括两个主要阶段：首先是通过模拟环境进行SLMs的训练，其次是结合LLM引导的监督微调和强化学习。这种交错的训练方式使得SLMs能够在复杂场景中有效导航。

**关键创新**：SmallPlan的主要创新在于将LLMs与SLMs结合，通过教师-学生模型的蒸馏过程，使得SLMs在路径规划中能够有效学习重要的环境特征，避免了传统方法中的幻觉和过拟合问题。

**关键设计**：在模型设计上，SLMs的训练采用了强化学习策略，并结合了距离等重要因素的考虑，优化了路径规划的效率和准确性。

## 📊 实验亮点

实验结果显示，经过微调的小语言模型在顺序路径规划任务中表现出色，性能与大型模型如GPT-4o相当，且在计算资源消耗上更具优势，未出现幻觉和过拟合现象，证明了其在边缘设备上的可行性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、无人驾驶汽车和智能物流系统等。通过提高路径规划的效率和准确性，SmallPlan能够在实际应用中显著提升机器人在复杂环境中的导航能力，推动智能设备的普及和应用。

## 📄 摘要（原文）

> Efficient path planning in robotics, particularly within large-scale, complex environments, remains a significant hurdle. While Large Language Models (LLMs) offer strong reasoning capabilities, their high computational cost and limited adaptability hinder real-time deployment on edge devices. We present SmallPlan - a novel framework leveraging LLMs as teacher models to train lightweight Small Language Models (SLMs) for high-level path planning tasks. In SmallPlan, the SLMs provide optimal action sequences to navigate across scene graphs that compactly represent full-scaled 3D scenes. The SLMs are trained in a simulation-powered, interleaved manner with LLM-guided supervised fine-tuning (SFT) and reinforcement learning (RL). This strategy not only enables SLMs to successfully complete navigation tasks but also makes them aware of important factors like distance travel, providing more efficient path planning. Through experiments, we demonstrate that the fine-tuned SLMs perform competitively with larger models like GPT-4o on sequential path planning, without suffering from hallucination and overfitting. SmallPlan is resource-efficient, making it well-suited for edge-device deployment and advancing practical autonomous robotics. Our source code is available here: https://github.com/quangpham2006/SmallPlan


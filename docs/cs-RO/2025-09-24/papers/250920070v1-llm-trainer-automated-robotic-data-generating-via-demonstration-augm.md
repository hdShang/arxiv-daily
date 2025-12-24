---
layout: default
title: "LLM Trainer: Automated Robotic Data Generating via Demonstration Augmentation using LLMs"
---

# LLM Trainer: Automated Robotic Data Generating via Demonstration Augmentation using LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20070" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20070v1</a>
  <a href="https://arxiv.org/pdf/2509.20070.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20070v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20070v1', 'LLM Trainer: Automated Robotic Data Generating via Demonstration Augmentation using LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abraham George, Amir Barati Farimani

**分类**: cs.RO

**发布日期**: 2025-09-24

**备注**: 9 pages, 5 figures, 4 tables. Submitted to ICRA 2026

---

## 💡 一句话要点

**提出LLM Trainer以解决机器人模仿学习数据生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人模仿学习` `数据生成` `大型语言模型` `自动化` `示范学习` `汤普森采样` `关键帧提取`

## 📋 核心要点

1. 现有方法在机器人模仿学习中依赖大量人类示范，导致数据生成效率低下。
2. 论文提出的LLM Trainer通过少量示范生成大量数据，采用离线注释和在线重定向的双步骤方法。
3. 实验结果表明，LLM Trainer在多项任务中表现优于传统的专家设计基线，成功率显著提升。

## 📝 摘要（中文）

我们提出了LLM Trainer，这是一个完全自动化的管道，利用大型语言模型（LLMs）的世界知识，将少量人类示范（少至一个）转化为大量机器人模仿学习数据集。我们的方法将示范生成分为两个步骤：离线示范注释，提取关键帧、显著对象和姿态-对象关系；在线关键姿态重定向，根据初始观察将这些关键帧适应到新场景。利用这些修改后的关键点，我们的系统扭曲原始示范以生成新轨迹，并在成功执行后保存结果。由于注释可在不同场景间重用，我们使用汤普森采样优化注释，显著提高生成成功率。我们在多项任务上评估了该方法，发现其数据注释方法始终优于专家设计的基线。最后，我们在Franka Emika Panda机器人上展示了硬件可行性。

## 🔬 方法详解

**问题定义**：本论文旨在解决机器人模仿学习中数据生成的低效率问题。现有方法通常需要大量人类示范，限制了其应用范围和灵活性。

**核心思路**：LLM Trainer通过利用大型语言模型的知识，将少量人类示范转化为丰富的机器人数据集。该方法的设计旨在提高数据生成的效率和成功率。

**技术框架**：整体架构分为两个主要阶段：第一阶段是离线示范注释，提取关键帧、显著对象和姿态-对象关系；第二阶段是在线关键姿态重定向，将关键帧适应到新场景。

**关键创新**：最重要的创新在于将示范生成过程分为注释和重定向两个步骤，并且注释可以在不同场景中重用，显著提高了生成效率。

**关键设计**：采用汤普森采样优化注释过程，确保生成的示范在多种场景下都能有效应用。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

实验结果显示，LLM Trainer的注释方法在多项任务中始终优于专家设计的基线，生成成功率显著提高。具体性能数据和对比基线的详细信息可在原文中查阅。

## 🎯 应用场景

该研究的潜在应用领域包括机器人自动化、智能制造和人机交互等。通过提高模仿学习的数据生成效率，LLM Trainer能够加速机器人学习过程，降低对人类示范的依赖，进而推动机器人技术的普及和应用。

## 📄 摘要（原文）

> We present LLM Trainer, a fully automated pipeline that leverages the world knowledge of Large Language Models (LLMs) to transform a small number of human demonstrations (as few as one) into a large robot dataset for imitation learning. Our approach decomposes demonstration generation into two steps: (1) offline demonstration annotation that extracts keyframes, salient objects, and pose-object relations; and (2) online keypose retargeting that adapts those keyframes to a new scene, given an initial observation. Using these modified keypoints, our system warps the original demonstration to generate a new trajectory, which is then executed, and the resulting demo, if successful, is saved. Because the annotation is reusable across scenes, we use Thompson sampling to optimize the annotation, significantly improving generation success rate. We evaluate our method on a range of tasks, and find that our data annotation method consistently outperforms expert-engineered baselines. We further show an ensemble policy that combines the optimized LLM feed-forward plan with a learned feedback imitation learning controller. Finally, we demonstrate hardware feasibility on a Franka Emika Panda robot. For additional materials and demonstration videos, please see the project website: https://sites.google.com/andrew.cmu.edu/llm-trainer


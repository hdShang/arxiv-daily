---
layout: default
title: Active-O3: Empowering Multimodal Large Language Models with Active Perception via GRPO
---

# Active-O3: Empowering Multimodal Large Language Models with Active Perception via GRPO

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21457" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21457v1</a>
  <a href="https://arxiv.org/pdf/2505.21457.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21457v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21457v1', 'Active-O3: Empowering Multimodal Large Language Models with Active Perception via GRPO')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muzhi Zhu, Hao Zhong, Canyu Zhao, Zongze Du, Zheng Huang, Mingyu Liu, Hao Chen, Cheng Zou, Jingdong Chen, Ming Yang, Chunhua Shen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-27

**备注**: Project Page: https://aim-uofa.github.io/ACTIVE-o3

---

## 💡 一句话要点

**提出ACTIVE-O3以解决多模态大语言模型的主动感知问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `主动感知` `多模态大语言模型` `强化学习` `机器人导航` `自动驾驶` `遥感图像分析` `信息获取`

## 📋 核心要点

1. 现有方法在主动感知能力上探索不足，导致多模态大语言模型在任务相关信息获取上效率低下。
2. 提出ACTIVE-O3，通过强化学习框架GRPO，赋予多模态大语言模型主动感知能力，提升信息获取效率。
3. ACTIVE-O3在多个基准测试中表现出色，尤其在零-shot推理能力上，未依赖任何显式推理数据。

## 📝 摘要（中文）

主动视觉，也称为主动感知，指的是主动选择观察位置和方式以获取与任务相关的信息。它是人类和先进的具身智能体高效感知与决策的关键组成部分。近年来，多模态大语言模型（MLLMs）作为机器人系统中的中央规划和决策模块受到广泛关注。然而，尽管主动感知在具身智能中的重要性，关于如何为MLLMs赋予或学习主动感知能力的探索仍然较少。本文首先系统定义了基于MLLM的主动感知任务，并指出最近提出的GPT-o3模型的放大搜索策略可以视为主动感知的特例，但仍存在搜索效率低和区域选择不准确的问题。为了解决这些问题，本文提出了ACTIVE-O3，一个基于强化学习的训练框架，旨在为MLLMs赋予主动感知能力。我们还建立了一个全面的基准套件，以评估ACTIVE-O3在一般开放世界任务和特定领域场景中的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在主动感知能力上的不足，现有方法如GPT-o3在搜索效率和区域选择上存在痛点。

**核心思路**：ACTIVE-O3通过强化学习框架GRPO，设计了一种新的训练方法，使得MLLMs能够主动选择观察区域，从而提高信息获取的效率和准确性。

**技术框架**：ACTIVE-O3的整体架构包括任务定义、模型训练和评估三个主要模块。首先定义主动感知任务，然后通过GRPO进行模型训练，最后在多个基准上进行评估。

**关键创新**：ACTIVE-O3的主要创新在于其基于强化学习的训练框架，显著提升了MLLMs在主动感知任务中的表现，与传统方法相比，能够更有效地选择观察区域。

**关键设计**：在参数设置上，ACTIVE-O3采用了特定的损失函数以优化区域选择的准确性，并设计了适应性网络结构以支持多模态输入的处理。通过这些设计，模型在复杂场景下的表现得到了提升。

## 📊 实验亮点

ACTIVE-O3在多个基准测试中表现出色，尤其在V*基准上展现出强大的零-shot推理能力，未依赖任何显式推理数据。与基线模型相比，ACTIVE-O3在小物体检测和密集物体定位任务中显著提升了性能，验证了其有效性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、自动驾驶、遥感图像分析等。通过提升多模态大语言模型的主动感知能力，能够在复杂环境中更有效地进行信息获取和决策，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Active vision, also known as active perception, refers to the process of actively selecting where and how to look in order to gather task-relevant information. It is a critical component of efficient perception and decision-making in humans and advanced embodied agents. Recently, the use of Multimodal Large Language Models (MLLMs) as central planning and decision-making modules in robotic systems has gained extensive attention. However, despite the importance of active perception in embodied intelligence, there is little to no exploration of how MLLMs can be equipped with or learn active perception capabilities. In this paper, we first provide a systematic definition of MLLM-based active perception tasks. We point out that the recently proposed GPT-o3 model's zoom-in search strategy can be regarded as a special case of active perception; however, it still suffers from low search efficiency and inaccurate region selection. To address these issues, we propose ACTIVE-O3, a purely reinforcement learning based training framework built on top of GRPO, designed to equip MLLMs with active perception capabilities. We further establish a comprehensive benchmark suite to evaluate ACTIVE-O3 across both general open-world tasks, such as small-object and dense object grounding, and domain-specific scenarios, including small object detection in remote sensing and autonomous driving, as well as fine-grained interactive segmentation. In addition, ACTIVE-O3 also demonstrates strong zero-shot reasoning abilities on the V* Benchmark, without relying on any explicit reasoning data. We hope that our work can provide a simple codebase and evaluation protocol to facilitate future research on active perception in MLLMs.


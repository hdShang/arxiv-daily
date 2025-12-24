---
layout: default
title: "Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation"
---

# Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13998" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13998v1</a>
  <a href="https://arxiv.org/pdf/2508.13998.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13998v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13998v1', 'Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifu Yuan, Haiqin Cui, Yaoting Huang, Yibin Chen, Fei Ni, Zibin Dong, Pengyi Li, Yan Zheng, Jianye Hao

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-08-19

**备注**: Embodied-R1 technical report

---

## 💡 一句话要点

**提出Embodied-R1以解决机器人操作中的感知-行动差距问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身人工智能` `视觉-语言模型` `强化学习` `指向能力` `机器人操作` `数据集构建` `零-shot泛化` `多任务学习`

## 📋 核心要点

1. 核心问题：现有的具身人工智能方法在通用化方面受到数据稀缺和具身性异质性的限制，导致感知与行动之间存在显著差距。
2. 方法要点：本文提出“指向”作为中间表示，并设计了Embodied-R1模型，通过强化学习微调来提升具身推理能力。
3. 实验或效果：Embodied-R1在11个基准测试中表现出色，尤其在SIMPLEREnv中实现了56.2%的成功率，较强基线提升62%。

## 📝 摘要（中文）

在具身人工智能领域，通用化受到“看与做之间的差距”的制约，这主要源于数据稀缺和具身性异质性。为了解决这一问题，本文首次提出“指向”作为统一的、与具身性无关的中间表示，定义了四种核心的具身指向能力，连接高层次的视觉-语言理解与低层次的动作原语。我们引入了Embodied-R1，一个专为具身推理和指向设计的3B视觉-语言模型（VLM）。通过构建大规模数据集Embodied-Points-200K，并采用两阶段强化微调（RFT）课程进行训练，Embodied-R1在11个具身空间和指向基准上取得了最先进的性能，展示了在多种视觉干扰下的高鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决具身人工智能中的“看与做之间的差距”问题，现有方法在数据稀缺和具身性异质性方面存在显著不足，限制了模型的通用性和鲁棒性。

**核心思路**：提出“指向”作为统一的中间表示，定义四种核心的具身指向能力，以此连接高层次的视觉-语言理解与低层次的动作原语，从而实现更有效的具身推理。

**技术框架**：Embodied-R1模型采用两阶段强化微调（RFT）课程进行训练，结合多任务奖励设计，利用大规模数据集Embodied-Points-200K作为训练基础，支持关键的具身指向能力。

**关键创新**：最重要的创新在于引入“指向”作为中间表示，突破了传统方法的局限，使得模型在多种任务中具备更强的零-shot泛化能力。

**关键设计**：在训练过程中，采用了专门设计的多任务奖励机制，并通过强化学习微调来优化模型性能，确保在不同视觉干扰下的鲁棒性。具体的网络结构和损失函数设计未详细披露，标记为未知。

## 📊 实验亮点

Embodied-R1在11个具身空间和指向基准上取得了最先进的性能，特别是在SIMPLEREnv中实现了56.2%的成功率，并在8个真实世界XArm任务中达到87.5%的成功率，较强基线提升62%。此外，该模型在多种视觉干扰下表现出高鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化制造、家庭服务机器人等。通过提升机器人在复杂环境中的操作能力，Embodied-R1有望在实际应用中实现更高的效率和灵活性，推动具身人工智能的发展。

## 📄 摘要（原文）

> Generalization in embodied AI is hindered by the "seeing-to-doing gap," which stems from data scarcity and embodiment heterogeneity. To address this, we pioneer "pointing" as a unified, embodiment-agnostic intermediate representation, defining four core embodied pointing abilities that bridge high-level vision-language comprehension with low-level action primitives. We introduce Embodied-R1, a 3B Vision-Language Model (VLM) specifically designed for embodied reasoning and pointing. We use a wide range of embodied and general visual reasoning datasets as sources to construct a large-scale dataset, Embodied-Points-200K, which supports key embodied pointing capabilities. We then train Embodied-R1 using a two-stage Reinforced Fine-tuning (RFT) curriculum with a specialized multi-task reward design. Embodied-R1 achieves state-of-the-art performance on 11 embodied spatial and pointing benchmarks. Critically, it demonstrates robust zero-shot generalization by achieving a 56.2% success rate in the SIMPLEREnv and 87.5% across 8 real-world XArm tasks without any task-specific fine-tuning, representing a 62% improvement over strong baselines. Furthermore, the model exhibits high robustness against diverse visual disturbances. Our work shows that a pointing-centric representation, combined with an RFT training paradigm, offers an effective and generalizable pathway to closing the perception-action gap in robotics.


---
layout: default
title: "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning"
---

# SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08989" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08989v1</a>
  <a href="https://arxiv.org/pdf/2506.08989.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08989v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08989v1', 'SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Liang, Zhong-Zhi Li, Yeyun Gong, Yang Wang, Hengyuan Zhang, Yelong Shen, Ying Nian Wu, Weizhu Chen

**分类**: cs.LG, cs.CL

**发布日期**: 2025-06-10

**备注**: Reinforcement Learning; Large Language Models; LLM Reasoning

---

## 💡 一句话要点

**提出自我意识弱点驱动的问题合成框架以提升强化学习效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `问题合成` `自我意识` `模型增强` `数学推理` `智能教育` `性能提升`

## 📋 核心要点

1. 现有的强化学习方法在生成高质量数学问题时面临人类标注问题稀缺和答案验证有限的挑战。
2. 本文提出的SwS框架通过识别模型的弱点，系统性地合成新问题以增强模型的学习能力。
3. 实验表明，SwS框架在多个推理基准上显著提升了模型性能，7B和32B模型的平均性能分别提高了10.0%和7.7%。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）在复杂推理任务中表现出色，但高质量问题集的缺乏限制了其扩展性。现有合成数据集中的人类标注数学问题稀缺，且验证答案有限，导致生成有效问题的效率低下。为此，本文提出了自我意识弱点驱动的问题合成框架（SwS），通过识别模型的不足并利用这些弱点进行问题增强。具体而言，弱点被定义为模型在RL训练中反复未能学习的问题。通过提取这些失败案例的核心概念，合成新问题以加强模型的薄弱领域，从而提升其推理能力。实验结果显示，在七个主流推理基准上，7B和32B模型的平均性能分别提升了10.0%和7.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在生成高质量数学问题时的不足，尤其是人类标注问题稀缺和验证答案有限的问题。现有合成策略往往不考虑模型能力，导致生成问题的效率低下。

**核心思路**：SwS框架的核心思想是通过识别模型在训练过程中反复未能解决的问题（即弱点），并利用这些弱点进行问题合成，从而增强模型的学习能力。

**技术框架**：该框架包括几个主要模块：首先，识别模型的弱点；其次，从失败案例中提取核心概念；最后，合成新问题以针对性地增强模型的薄弱领域。

**关键创新**：SwS框架的创新之处在于其自我意识能力，能够让模型识别并解决自身的弱点，而不依赖外部知识蒸馏。这一设计使得模型在强化学习中具备更强的泛化能力。

**关键设计**：在实现过程中，框架中涉及的关键参数设置和损失函数设计旨在优化模型对合成问题的学习效率，具体细节在论文中有详细阐述。通过迭代训练，模型能够逐步克服其弱点。

## 📊 实验亮点

实验结果显示，SwS框架在七个主流推理基准上显著提升了模型性能，其中7B模型的平均性能提升了10.0%，32B模型的平均性能提升了7.7%。这些结果表明，SwS框架在问题合成和模型训练中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和自动化问题生成等。通过提升模型在复杂推理任务中的表现，SwS框架能够为教育领域提供更高效的学习工具，帮助学生更好地掌握数学问题解决能力，未来可能对个性化学习和智能教育产生深远影响。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective for training large language models (LLMs) on complex reasoning tasks, such as mathematical problem solving. A prerequisite for the scalability of RLVR is a high-quality problem set with precise and verifiable answers. However, the scarcity of well-crafted human-labeled math problems and limited-verification answers in existing distillation-oriented synthetic datasets limit their effectiveness in RL. Additionally, most problem synthesis strategies indiscriminately expand the problem set without considering the model's capabilities, leading to low efficiency in generating useful questions. To mitigate this issue, we introduce a Self-aware Weakness-driven problem Synthesis framework (SwS) that systematically identifies model deficiencies and leverages them for problem augmentation. Specifically, we define weaknesses as questions that the model consistently fails to learn through its iterative sampling during RL training. We then extract the core concepts from these failure cases and synthesize new problems to strengthen the model's weak areas in subsequent augmented training, enabling it to focus on and gradually overcome its weaknesses. Without relying on external knowledge distillation, our framework enables robust generalization byempowering the model to self-identify and address its weaknesses in RL, yielding average performance gains of 10.0% and 7.7% on 7B and 32B models across eight mainstream reasoning benchmarks.


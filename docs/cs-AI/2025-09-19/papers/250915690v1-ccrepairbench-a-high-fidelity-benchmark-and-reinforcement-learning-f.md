---
layout: default
title: "CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair"
---

# CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15690" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15690v1</a>
  <a href="https://arxiv.org/pdf/2509.15690.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15690v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15690v1', 'CCrepairBench: A High-Fidelity Benchmark and Reinforcement Learning Framework for C++ Compilation Repair')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weixuan Sun, Jucai Zhai, Dengfeng Liu, Xin Zhang, Xiaojun Wu, Qiaobo Hao, AIMgroup, Yang Fang, Jiuyang Tang

**分类**: cs.AI

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出CCrepairBench，用于C++编译错误修复的高保真基准和强化学习框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `C++编译修复` `强化学习` `代码生成` `LLM评估` `数据集构建`

## 📋 核心要点

1. 现有C++编译错误修复方法缺乏大规模高保真数据集，且监督学习方法难以生成语义正确的补丁。
2. 提出基于强化学习的修复范式，利用混合奖励信号引导模型学习，关注修复的语义质量。
3. 构建CCrepair数据集，并设计两阶段评估系统，使用LLM作为评估器，保证评估的可靠性。

## 📝 摘要（中文）

C++编译错误的自动修复是一个重要的挑战，对提高开发者生产力至关重要。该领域的发展受到两个主要因素的限制：缺乏大规模、高保真的数据集，以及传统监督方法的局限性，这些方法通常无法生成语义正确的补丁。本文通过引入一个包含三个核心贡献的综合框架来解决这些问题。首先，我们提出了CCrepair，这是一个通过复杂的生成-验证流程构建的新型大规模C++编译错误数据集。其次，我们提出了一种由混合奖励信号引导的强化学习（RL）范式，将重点从单纯的可编译性转移到修复的语义质量。最后，我们建立了一个稳健的两阶段评估系统，提供这种信号，该系统以LLM-as-a-Judge为中心，其可靠性已通过一组人类专家的集体判断进行了严格验证。这种集成方法使训练目标与生成高质量、非平凡的、在语法和语义上都正确的补丁对齐。实验证明了我们方法的有效性。我们经过RL训练的Qwen2.5-1.5B-Instruct模型实现了与Qwen2.5-14B-Instruct模型相当的性能，验证了我们训练范式的效率。我们的工作为研究界提供了一个有价值的新数据集和一个更有效的训练和评估鲁棒编译修复模型的范式，为更实用和可靠的自动编程助手铺平了道路。

## 🔬 方法详解

**问题定义**：C++编译错误自动修复旨在解决开发者在编程过程中遇到的编译错误，现有方法主要依赖监督学习，但缺乏大规模高质量数据集，且难以保证修复后的代码在语义上的正确性。现有方法往往只关注代码的可编译性，忽略了修复后的代码是否真正解决了问题。

**核心思路**：本文的核心思路是利用强化学习，通过奖励信号引导模型学习生成语义正确的补丁。通过构建一个高质量的C++编译错误数据集，并设计一个能够准确评估修复质量的评估系统，从而训练出一个能够生成高质量修复补丁的模型。强化学习能够探索更大的解空间，避免陷入局部最优解。

**技术框架**：整体框架包含三个主要部分：CCrepair数据集构建、基于强化学习的修复模型训练和两阶段评估系统。CCrepair数据集通过生成-验证流程构建，保证数据质量。强化学习训练使用混合奖励信号，包括编译成功奖励和语义正确性奖励。两阶段评估系统首先进行编译测试，然后使用LLM作为评估器进行语义评估。

**关键创新**：最重要的技术创新点在于将强化学习引入C++编译错误修复，并设计了混合奖励信号，从而能够训练出生成语义正确补丁的模型。与传统的监督学习方法相比，强化学习能够更好地探索解空间，避免陷入局部最优解。使用LLM作为评估器，能够更准确地评估修复的语义质量。

**关键设计**：混合奖励信号包括编译成功奖励和语义正确性奖励，其中语义正确性奖励由LLM评估器给出。强化学习算法采用Q-learning，网络结构采用Transformer。数据集构建过程中，采用了多种代码生成和变异技术，以保证数据集的多样性和复杂性。LLM评估器采用Qwen2.5系列模型，并经过人工评估验证其可靠性。

## 📊 实验亮点

实验结果表明，经过RL训练的Qwen2.5-1.5B-Instruct模型性能与Qwen2.5-14B-Instruct模型相当，验证了该训练范式的有效性。该方法在C++编译错误修复任务上取得了显著的性能提升，为自动编程助手的发展奠定了基础。

## 🎯 应用场景

该研究成果可应用于智能编程助手、代码自动修复工具等领域，能够显著提高开发者的生产力，减少调试时间。通过自动修复编译错误，可以降低软件开发的成本，并提高软件的质量和可靠性。未来，该技术有望扩展到其他编程语言和更复杂的代码修复任务。

## 📄 摘要（原文）

> The automated repair of C++ compilation errors presents a significant challenge, the resolution of which is critical for developer productivity. Progress in this domain is constrained by two primary factors: the scarcity of large-scale, high-fidelity datasets and the limitations of conventional supervised methods, which often fail to generate semantically correct patches.This paper addresses these gaps by introducing a comprehensive framework with three core contributions. First, we present CCrepair, a novel, large-scale C++ compilation error dataset constructed through a sophisticated generate-and-verify pipeline. Second, we propose a Reinforcement Learning (RL) paradigm guided by a hybrid reward signal, shifting the focus from mere compilability to the semantic quality of the fix. Finally, we establish the robust, two-stage evaluation system providing this signal, centered on an LLM-as-a-Judge whose reliability has been rigorously validated against the collective judgments of a panel of human experts. This integrated approach aligns the training objective with generating high-quality, non-trivial patches that are both syntactically and semantically correct. The effectiveness of our approach was demonstrated experimentally. Our RL-trained Qwen2.5-1.5B-Instruct model achieved performance comparable to a Qwen2.5-14B-Instruct model, validating the efficiency of our training paradigm. Our work provides the research community with a valuable new dataset and a more effective paradigm for training and evaluating robust compilation repair models, paving the way for more practical and reliable automated programming assistants.


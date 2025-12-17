---
layout: default
title: RoboGPT-R1: Enhancing Robot Planning with Reinforcement Learning
---

# RoboGPT-R1: Enhancing Robot Planning with Reinforcement Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14828" target="_blank" class="toolbar-btn">arXiv: 2510.14828v2</a>
    <a href="https://arxiv.org/pdf/2510.14828.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14828v2" 
            onclick="toggleFavorite(this, '2510.14828v2', 'RoboGPT-R1: Enhancing Robot Planning with Reinforcement Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jinrui Liu, Bingyan Nie, Boyu Li, Yaran Chen, Yuze Wang, Shunsen He, Haoran Li

**分类**: cs.AI, cs.RO

**发布日期**: 2025-10-16 (更新: 2025-10-22)

---

## 💡 一句话要点

**RoboGPT-R1：强化学习增强机器人规划能力，提升长时程操作任务性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人规划` `强化学习` `具身智能` `视觉语言模型` `长时程操作` `监督微调` `奖励函数`

## 📋 核心要点

1. 现有基于监督微调的大语言模型和视觉语言模型在复杂环境中执行长时程操作任务时，由于常识和推理能力的限制，面临挑战。
2. RoboGPT-R1采用两阶段微调框架，先通过监督学习获取知识，再利用强化学习提升视觉空间理解和推理能力，弥补监督学习的不足。
3. 实验表明，在Qwen2.5-VL-3B上训练的RoboGPT-R1，在EmbodiedBench上显著优于GPT-4o-mini和基于Qwen2.5-VL-7B训练的模型。

## 📝 摘要（中文）

为了提高具身智能体在长时程操作任务中完成复杂人类指令的推理能力，本文提出了RoboGPT-R1，一个用于具身规划的两阶段微调框架。该框架首先通过监督训练从专家序列中获取基础知识，然后利用强化学习解决模型在视觉空间理解和推理方面的不足。为了在多步推理任务中实现物理理解和动作序列一致性，设计了一种基于规则的奖励函数，同时考虑了长时程性能和环境中的动作约束。在Qwen2.5-VL-3B上训练的推理模型，在EmbodiedBench基准测试中，显著优于更大规模的模型GPT-4o-mini 21.33%，并且超过了在Qwen2.5-VL-7B上训练的其他工作 20.33%。

## 🔬 方法详解

**问题定义**：现有方法在具身智能体的长时程操作任务中，由于缺乏足够的常识和推理能力，难以很好地理解环境并规划出合理的动作序列，导致任务完成效果不佳。监督微调虽然可以学习到一些知识，但泛化能力和物理理解能力不足。

**核心思路**：RoboGPT-R1的核心思路是结合监督学习和强化学习的优势。首先通过监督学习让模型学习到基础知识，然后利用强化学习来弥补模型在视觉空间理解和推理方面的不足，从而提高模型在复杂环境中的规划能力。

**技术框架**：RoboGPT-R1是一个两阶段的微调框架。第一阶段是监督学习，使用专家序列对模型进行微调，使其学习到基础知识。第二阶段是强化学习，使用基于规则的奖励函数来训练模型，使其能够更好地理解环境并规划出合理的动作序列。奖励函数同时考虑了长时程性能和环境中的动作约束。

**关键创新**：RoboGPT-R1的关键创新在于结合了监督学习和强化学习，并设计了一种基于规则的奖励函数。这种结合可以有效地提高模型在复杂环境中的规划能力。基于规则的奖励函数能够同时考虑长时程性能和环境中的动作约束，从而保证了动作序列的合理性和有效性。

**关键设计**：奖励函数的设计是关键。它由两部分组成：一部分是长时程性能奖励，用于鼓励模型完成任务；另一部分是动作约束奖励，用于惩罚违反环境约束的动作。具体规则和权重设置未知，但目标是引导模型学习到既能完成任务又能遵守环境规则的动作序列。

## 📊 实验亮点

RoboGPT-R1在EmbodiedBench基准测试中取得了显著的性能提升。具体来说，它比GPT-4o-mini的性能高出21.33%，并且比在Qwen2.5-VL-7B上训练的其他工作高出20.33%。这些结果表明，RoboGPT-R1能够有效地提高机器人在复杂环境中的规划能力。

## 🎯 应用场景

RoboGPT-R1可应用于各种需要机器人进行长时程操作任务的场景，例如家庭服务、工业自动化、医疗辅助等。通过提升机器人的推理和规划能力，使其能够更好地理解人类指令，并在复杂环境中完成任务，从而提高工作效率和生活质量。未来，该研究可以进一步扩展到更复杂的环境和任务中。

## 📄 摘要（原文）

> Improving the reasoning capabilities of embodied agents is crucial for robots to complete complex human instructions in long-view manipulation tasks successfully. Despite the success of large language models and vision language models based on Supervised Fine-Tuning (SFT) in planning tasks, they continue facing challenges in performing long-horizon manipulation tasks in complex real-world environments, owing to their restricted common sense and reasoning capabilities. Considering that aligning general-purpose vision language models to robotic planning tasks via supervised fine-tuning suffers from poor generalization and insufficient physical understanding, we propose RoboGPT-R1, a two-stage fine-tuning framework for embodied planning. In this framework, supervised training acquires foundational knowledge through expert sequences, followed by RL to address the model's shortcomings in visual-spatial understanding and reasoning. To achieve physical understanding and action sequence consistency in multi-step reasoning tasks, we design a rule-based reward function that simultaneously considers long-horizon performance and action constraint in the environment. The reasoning model, trained on Qwen2.5-VL-3B, significantly outperforms the larger-scale model, GPT-4o-mini, by 21.33% and surpasses other work trained on Qwen2.5-VL-7B by 20.33% on the EmbodiedBench benchmark.


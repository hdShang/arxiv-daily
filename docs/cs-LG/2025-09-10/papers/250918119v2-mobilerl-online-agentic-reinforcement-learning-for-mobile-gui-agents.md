---
layout: default
title: "MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents"
---

# MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18119" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18119v2</a>
  <a href="https://arxiv.org/pdf/2509.18119.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18119v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18119v2', 'MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Xu, Xiao Liu, Xinghan Liu, Jiaqi Fu, Hanchen Zhang, Bohao Jing, Shudan Zhang, Yuting Wang, Wenyi Zhao, Yuxiao Dong

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-10 (更新: 2025-10-24)

**🔗 代码/项目**: [GITHUB](https://github.com/THUDM/MobileRL)

---

## 💡 一句话要点

**提出MobileRL框架，通过在线强化学习提升移动GUI智能体的任务完成能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `移动GUI智能体` `强化学习` `在线学习` `难度自适应` `奖励重塑`

## 📋 核心要点

1. 现有移动GUI智能体面临任务难度差异大和环境采样效率低下的挑战，导致强化学习训练困难。
2. MobileRL框架通过难度自适应的正向回放、失败课程过滤和最短路径奖励调整来解决上述问题。
3. 实验结果表明，MobileRL在AndroidWorld和AndroidLab上取得了SOTA性能，显著提升了任务成功率。

## 📝 摘要（中文）

本文提出了一种在线智能体强化学习框架MobileRL，旨在提升移动GUI智能体的性能。由于任务难度呈现重尾分布以及大规模环境采样效率低下，利用强化学习开发有效的移动GUI智能体仍然具有挑战性。MobileRL的核心是难度自适应GRPO（ADAGRPO）算法。在ADAGRPO中，我们设计了难度自适应的正向回放和失败课程过滤，使模型能够适应不同的任务难度。此外，我们引入了最短路径奖励调整策略，以重塑多轮智能体任务中与任务长度相关的奖励。这些策略共同稳定了强化学习训练，提高了样本效率，并在各种移动应用和任务中产生了强大的性能。我们将MOBILERL应用于两个开源模型（Qwen2.5-VL-7B-Instruct和GLM-4.1V-9B-Base）。由此产生的MOBILERL-9B模型在AndroidWorld（80.2%）和AndroidLab（53.6%）上的成功率方面均达到了最先进水平。MOBILERL框架已开源。

## 🔬 方法详解

**问题定义**：现有基于强化学习的移动GUI智能体在训练过程中面临两个主要问题：一是任务难度分布不均匀，存在大量的简单任务和少量困难任务，导致模型难以有效学习；二是环境采样效率低下，需要大量的交互才能获得有效的训练样本，训练成本高昂。

**核心思路**：MobileRL的核心思路是通过难度自适应的策略来解决上述问题。具体来说，它通过难度自适应的正向回放来增加困难样本的利用率，通过失败课程过滤来避免简单样本的干扰，并通过最短路径奖励调整来优化奖励信号，从而提高训练效率和模型性能。

**技术框架**：MobileRL框架主要包含以下几个模块：1) 环境交互模块，负责与移动GUI环境进行交互，收集训练样本；2) 难度评估模块，负责评估当前任务的难度；3) ADAGRPO算法模块，包含难度自适应的正向回放、失败课程过滤和最短路径奖励调整策略，用于优化智能体的策略；4) 模型更新模块，负责根据收集到的训练样本更新智能体的模型参数。

**关键创新**：MobileRL的关键创新在于ADAGRPO算法，它通过难度自适应的正向回放和失败课程过滤来解决任务难度分布不均匀的问题，并通过最短路径奖励调整来优化奖励信号。与现有方法相比，MobileRL能够更有效地利用训练样本，提高训练效率和模型性能。

**关键设计**：难度自适应正向回放：根据任务难度动态调整正向回放的概率，增加困难样本的利用率。失败课程过滤：过滤掉简单的失败样本，避免其对模型训练产生负面影响。最短路径奖励调整：根据任务的最短路径长度调整奖励信号，避免奖励稀疏的问题。具体参数设置和网络结构细节未在论文中详细描述，属于未知信息。

## 📊 实验亮点

MobileRL在AndroidWorld和AndroidLab两个基准测试集上取得了显著的性能提升。具体而言，使用MOBILERL-9B模型在AndroidWorld上的成功率达到了80.2%，在AndroidLab上的成功率达到了53.6%，均超过了现有最先进的模型。

## 🎯 应用场景

MobileRL框架可应用于各种移动GUI自动化任务，例如自动化测试、智能助手、辅助功能等。它可以帮助用户更高效地完成移动设备上的各种操作，提高用户体验。未来，该技术有望扩展到其他类型的GUI环境，例如桌面应用和网页应用。

## 📄 摘要（原文）

> Building general-purpose graphical user interface (GUI) agents has become increasingly promising with the progress in vision language models. However, developing effective mobile GUI agents with reinforcement learning (RL) remains challenging due to the heavy-tailed distribution of task difficulty and the inefficiency of large-scale environment sampling. We present an online agentic reinforcement learning framework MobileRL to enhance GUI agents in mobile environments. Its core component is the Difficulty-ADAptive GRPO (ADAGRPO) algorithm. In ADAGRPO, we design difficulty-adaptive positive replay and failure curriculum filtering to adapt the model to different task difficulties. We introduce the shortest-path reward adjustment strategy to reshape rewards concerning the task length in multi-turn agentic tasks. Those strategies jointly stabilize RL training, improve sample efficiency, and generate strong performance across diverse mobile apps and tasks. We apply MOBILERL to two open models (Qwen2.5-VL-7B-Instruct and GLM-4.1V-9B-Base). The resultant MOBILERL-9B model achieves state-of-the-art results in terms of success rates on both AndroidWorld (80.2%) and AndroidLab (53.6%). The MOBILERL framework is open-sourced at: https://github.com/THUDM/MobileRL.


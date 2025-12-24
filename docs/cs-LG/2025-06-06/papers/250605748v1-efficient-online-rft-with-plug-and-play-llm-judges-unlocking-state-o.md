---
layout: default
title: "Efficient Online RFT with Plug-and-Play LLM Judges: Unlocking State-of-the-Art Performance"
---

# Efficient Online RFT with Plug-and-Play LLM Judges: Unlocking State-of-the-Art Performance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05748" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05748v1</a>
  <a href="https://arxiv.org/pdf/2506.05748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05748v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05748v1', 'Efficient Online RFT with Plug-and-Play LLM Judges: Unlocking State-of-the-Art Performance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rudransh Agnihotri, Ananya Pandey

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出高效在线RFT方法以解决RLHF中的奖励模型训练瓶颈**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `人类反馈` `奖励模型` `在线评估` `LoRA适配器` `自然语言处理` `模型压缩`

## 📋 核心要点

1. 现有的奖励模型训练方法通常需要大量参数和复杂的离线调整，导致成本高昂且效率低下。
2. 本文提出了一种通过简单的JSON规则和LoRA适配器来增强LLM的方法，旨在降低成本并提高评估效率。
3. 实验结果表明，该方法在多个基准上表现优异，尤其是在RewardBench和GSM-8K上显著超越了传统模型。

## 📝 摘要（中文）

奖励模型训练是现代强化学习人类反馈（RLHF）管道中的成本瓶颈，通常需要数十亿参数和离线偏好调整阶段。本文提出的方法通过仅使用一行JSON规则和一个影响模型参数0.8%的rank-16 LoRA适配器，增强了一个冻结的、经过指令调优的7B LLM，使其能够完全替代之前使用的重型评估模型。该插件式评估者在RewardBench上达到了96.2%的准确率，超越了参数范围从27B到70B的专用奖励网络。此外，它使得7B的演员在在线PPO上实现92%的精确匹配准确率，超越了得分为61.8%的70B DPO基线。

## 🔬 方法详解

**问题定义**：本文旨在解决现代RLHF管道中奖励模型训练的高成本和低效率问题，现有方法通常依赖于庞大的模型和复杂的离线训练过程。

**核心思路**：通过引入一个冻结的7B LLM，并结合简单的JSON规则和LoRA适配器，本文实现了高效的在线奖励评估，避免了传统方法的复杂性。

**技术框架**：整体架构包括一个指令调优的LLM作为基础模型，LoRA适配器用于增强模型的评估能力，结合在线PPO算法进行训练和评估。

**关键创新**：最重要的创新在于使用小型LoRA适配器替代大型评估模型，显著降低了参数需求，同时保持了高准确率。

**关键设计**：模型使用了仅影响0.8%参数的rank-16 LoRA适配器，结合六个上下文示例以提升零到少量样本的表现，并在安全性和对抗性场景中优化了评估效果。

## 📊 实验亮点

实验结果显示，所提出的LoRA评估者在RewardBench上达到了96.2%的准确率，超越了27B至70B参数的专用奖励网络。此外，7B的演员在GSM-8K上实现了92%的精确匹配准确率，显著高于70B DPO基线的61.8%。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和自动化评估等。通过降低奖励模型的训练成本和复杂性，该方法可以促进RLHF在实际应用中的广泛推广，提升智能系统的学习效率和效果。

## 📄 摘要（原文）

> Reward-model training is the cost bottleneck in modern Reinforcement Learning Human Feedback (RLHF) pipelines, often requiring tens of billions of parameters and an offline preference-tuning phase. In the proposed method, a frozen, instruction-tuned 7B LLM is augmented with only a one line JSON rubric and a rank-16 LoRA adapter (affecting just 0.8% of the model's parameters), enabling it to serve as a complete substitute for the previously used heavyweight evaluation models. The plug-and-play judge achieves 96.2% accuracy on RewardBench, outperforming specialized reward networks ranging from 27B to 70B parameters. Additionally, it allows a 7B actor to outperform the top 70B DPO baseline, which scores 61.8%, by achieving 92% exact match accuracy on GSM-8K utilizing online PPO. Thorough ablations indicate that (i) six in context demonstrations deliver the majority of the zero-to-few-shot improvements (+2pp), and (ii) the LoRA effectively addresses the remaining disparity, particularly in the safety and adversarial Chat-Hard segments. The proposed model introduces HH-Rationales, a subset of 10,000 pairs from Anthropic HH-RLHF, to examine interpretability, accompanied by human generated justifications. GPT-4 scoring indicates that our LoRA judge attains approximately = 9/10 in similarity to human explanations, while zero-shot judges score around =5/10. These results indicate that the combination of prompt engineering and tiny LoRA produces a cost effective, transparent, and easily adjustable reward function, removing the offline phase while achieving new state-of-the-art outcomes for both static evaluation and online RLHF.


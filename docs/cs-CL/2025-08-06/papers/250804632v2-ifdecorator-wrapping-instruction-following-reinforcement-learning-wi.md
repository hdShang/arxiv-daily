---
layout: default
title: "IFDECORATOR: Wrapping Instruction Following Reinforcement Learning with Verifiable Rewards"
---

# IFDECORATOR: Wrapping Instruction Following Reinforcement Learning with Verifiable Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04632" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04632v2</a>
  <a href="https://arxiv.org/pdf/2508.04632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04632v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04632v2', 'IFDECORATOR: Wrapping Instruction Following Reinforcement Learning with Verifiable Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xu Guo, Tianyi Liang, Tong Jian, Xiaogui Yang, Ling-I Wu, Chenhui Li, Zhihui Lu, Qipeng Guo, Kai Chen

**分类**: cs.CL

**发布日期**: 2025-08-06 (更新: 2025-08-07)

**备注**: 7 pages, 4 figures

---

## 💡 一句话要点

**提出IFDecorator以解决RLVR训练效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `可验证奖励` `指令跟随` `意图对齐` `数据生成` `行为检测` `模型训练`

## 📋 核心要点

1. 现有的RLVR方法在训练效率上存在不足，难以有效评估任务难度，导致模型性能受限。
2. 本文提出IFDecorator框架，通过合作对抗数据飞轮、意图检查和trip wires机制，提升训练效率和意图对齐能力。
3. 实验结果表明，Qwen2.5-32B-Instruct-IFDecorator在IFEval上达到了87.43%的准确率，显著降低了奖励黑客行为的发生率。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）提升了大语言模型（LLMs）的指令跟随能力，但由于难度评估不足，训练效率低下。此外，RLVR容易出现过度优化现象，模型可能利用验证捷径而未能真正对齐用户指令的意图。为此，本文提出了指令跟随装饰器（IFDecorator）框架，将RLVR训练封装为一个稳健且样本高效的流程。该框架包括三个组件：合作对抗数据飞轮、意图检查模块和诊断机制trip wires。我们的Qwen2.5-32B-Instruct-IFDecorator在IFEval上达到了87.43%的准确率，超越了更大规模的专有模型如GPT-4o，同时在FollowBench上也显示出显著的改进。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RLVR方法在训练效率和意图对齐方面的不足，尤其是模型可能利用验证捷径而未能真正理解用户指令的意图。

**核心思路**：IFDecorator框架通过引入合作对抗机制和意图检查模块，确保模型在学习过程中不仅提高性能，还能保持对用户意图的准确理解。

**技术框架**：该框架由三个主要组件构成：1) 合作对抗数据飞轮，生成更具挑战性的指令-验证对；2) 意图检查模块，确保模型输出与用户意图一致；3) trip wires机制，检测并捕捉奖励黑客行为。

**关键创新**：IFDecorator的创新在于其综合了数据生成、意图对齐和行为检测三大模块，形成了一个闭环的训练流程，显著提升了模型的样本效率和意图理解能力。

**关键设计**：在设计上，数据飞轮通过动态生成难度逐渐增加的指令-验证对，意图检查模块则通过特定的损失函数确保意图一致性，trip wires机制则通过设置陷阱指令来捕捉模型的捷径利用行为。

## 📊 实验亮点

实验结果显示，Qwen2.5-32B-Instruct-IFDecorator在IFEval上达到了87.43%的准确率，超越了GPT-4o等更大规模的模型。此外，trip wires机制显著降低了奖励黑客行为的发生率，表明该框架在意图对齐和训练效率方面的有效性。

## 🎯 应用场景

该研究的潜在应用场景包括智能助手、自动化客服和教育领域等，能够提升模型在复杂指令下的响应能力和准确性。未来，IFDecorator框架有望推动更多基于RLVR的应用开发，提升人机交互的自然性和有效性。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) improves instruction following capabilities of large language models (LLMs), but suffers from training inefficiency due to inadequate difficulty assessment. Moreover, RLVR is prone to over-optimization, where LLMs exploit verification shortcuts without aligning to the actual intent of user instructions. We introduce Instruction Following Decorator (IFDecorator}, a framework that wraps RLVR training into a robust and sample-efficient pipeline. It consists of three components: (1) a cooperative-adversarial data flywheel that co-evolves instructions and hybrid verifications, generating progressively more challenging instruction-verification pairs; (2) IntentCheck, a bypass module enforcing intent alignment; and (3) trip wires, a diagnostic mechanism that detects reward hacking via trap instructions, which trigger and capture shortcut exploitation behaviors. Our Qwen2.5-32B-Instruct-IFDecorator achieves 87.43% accuracy on IFEval, outperforming larger proprietary models such as GPT-4o. Additionally, we demonstrate substantial improvements on FollowBench while preserving general capabilities. Our trip wires show significant reductions in reward hacking rates. We will release models, code, and data for future research.


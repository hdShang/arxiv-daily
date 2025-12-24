---
layout: default
title: "Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models"
---

# Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05850" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05850v2</a>
  <a href="https://arxiv.org/pdf/2506.05850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05850v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05850v2', 'Cross-lingual Collapse: How Language-Centric Foundation Models Shape Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheonbok Park, Jeonghoon Kim, Joosung Lee, Sanghwan Bae, Jaegul Choo, Kang Min Yoo

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-06-09)

**备注**: Preprint

---

## 💡 一句话要点

**提出跨语言崩溃现象以揭示多语言模型推理的局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨语言推理` `多语言模型` `逻辑推理` `强化学习` `奖励设计` `低资源语言` `模型微调`

## 📋 核心要点

1. 现有多语言模型在推理时存在语言崩溃现象，导致低资源语言的推理能力迅速下降。
2. 论文通过对多语言大型推理模型进行微调，提出了使用群体相对策略优化的方法来解决这一问题。
3. 实验结果表明，语言一致性奖励可以缓解崩溃现象，但会导致准确率显著下降，且崩溃现象大部分不可逆。

## 📝 摘要（中文）

本文识别了跨语言崩溃现象，即多语言模型的推理链在使用不同语言提示时，仍然回归到其主导的预训练语言。尽管通过可验证奖励的强化学习，大型语言模型在逻辑推理方面表现出色，但多语言推理的机制尚未得到充分探讨。我们通过对多语言大型推理模型进行微调，发现预训练语言的不平衡会迅速加剧，导致低资源语言的推理能力下降。此外，尽管语言一致性奖励可以缓解这一现象，但会导致准确率下降5-10个百分点。最终的语言崩溃现象是严重且大部分不可逆的，后续微调难以恢复模型的目标语言推理能力。

## 🔬 方法详解

**问题定义**：本文旨在解决多语言模型在推理过程中出现的跨语言崩溃现象，现有方法未能有效处理低资源语言的推理能力下降问题。

**核心思路**：我们提出通过群体相对策略优化（GRPO）对多语言大型推理模型进行微调，以改善多语言推理的平衡性和一致性。

**技术框架**：研究中使用了翻译后的GSM8K和SimpleRL-Zoo数据集，分别在中文、韩文和乌克兰文上进行训练，监测任务准确性和推理链的一致性。

**关键创新**：最重要的创新在于识别并分析了跨语言崩溃现象，揭示了不同语言在推理能力训练上的不平等，强调了奖励设计和数据难度对多语言推理的影响。

**关键设计**：在微调过程中，设置了语言一致性奖励机制，并监控了模型在不同语言下的推理表现，发现其对准确率的影响显著。

## 📊 实验亮点

实验结果显示，使用GRPO方法后，低资源语言的推理能力在仅几百次更新内显著下降，且语言一致性奖励虽然能够缓解崩溃现象，但导致准确率下降5-10个百分点。这些发现强调了多语言模型训练中的不平等性。

## 🎯 应用场景

该研究的潜在应用领域包括多语言自然语言处理、跨语言信息检索和多语言对话系统等。通过改善多语言模型的推理能力，能够提升低资源语言的应用效果，推动全球范围内的语言技术发展，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> We identify \textbf{Cross-lingual Collapse}, a systematic drift in which the chain-of-thought (CoT) of a multilingual language model reverts to its dominant pre-training language even when the prompt is expressed in a different language. Recent large language models (LLMs) with reinforcement learning with verifiable reward (RLVR) have achieved strong logical reasoning performances by exposing their intermediate reasoning traces, giving rise to large reasoning models (LRMs). However, the mechanism behind multilingual reasoning in LRMs is not yet fully explored. To investigate the issue, we fine-tune multilingual LRMs with Group-Relative Policy Optimization (GRPO) on translated versions of the GSM$8$K and SimpleRL-Zoo datasets in three different languages: Chinese, Korean, and Ukrainian. During training, we monitor both task accuracy and language consistency of the reasoning chains. Our experiments reveal three key findings: (i) GRPO rapidly amplifies pre-training language imbalances, leading to the erosion of low-resource languages within just a few hundred updates; (ii) language consistency reward mitigates this drift but does so at the expense of an almost 5 - 10 pp drop in accuracy. and (iii) the resulting language collapse is severely damaging and largely irreversible, as subsequent fine-tuning struggles to steer the model back toward its original target-language reasoning capabilities. Together, these findings point to a remarkable conclusion: \textit{not all languages are trained equally for reasoning}. Furthermore, our paper sheds light on the roles of reward shaping, data difficulty, and pre-training priors in eliciting multilingual reasoning.


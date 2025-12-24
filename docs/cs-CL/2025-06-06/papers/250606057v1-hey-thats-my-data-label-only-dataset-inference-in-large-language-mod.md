---
layout: default
title: "Hey, That's My Data! Label-Only Dataset Inference in Large Language Models"
---

# Hey, That's My Data! Label-Only Dataset Inference in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06057" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06057v1</a>
  <a href="https://arxiv.org/pdf/2506.06057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06057v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06057v1', 'Hey, That\'s My Data! Label-Only Dataset Inference in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Xiong, Zihao Wang, Rui Zhu, Tsung-Yi Ho, Pin-Yu Chen, Jingwei Xiong, Haixu Tang, Lucila Ohno-Machado

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出CatShift以解决大语言模型数据推断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `数据集推断` `灾难性遗忘` `版权保护` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有的数据集推断方法依赖于模型内部的日志概率，导致在许多情况下无法有效检测可疑数据集。
2. CatShift框架利用灾难性遗忘的特性，通过比较模型输出的变化来判断数据集的成员资格，避免了对内部信号的依赖。
3. 实验结果表明，CatShift在开放源代码和API基础的LLMs上均表现出色，能够有效识别数据集成员资格。

## 📝 摘要（中文）

大语言模型（LLMs）在自然语言处理领域取得了显著进展，但其对大规模、常常是专有数据集的依赖带来了版权侵犯和财务损失的风险。现有的数据集推断方法通常依赖于日志概率来检测可疑的训练材料，但许多领先的LLMs已开始隐瞒这些信号。为了解决这一问题，本文提出了CatShift，一个基于标签的数据集推断框架，利用灾难性遗忘的特性来识别数据集成员资格。通过比较模型在可疑数据集上的输出变化与已知非成员验证集的变化，CatShift能够有效判断可疑数据集是否可能是模型原始训练数据的一部分。大量实验验证了CatShift在无法访问日志的环境下的有效性，为保护专有数据提供了可靠的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在数据集推断中面临的版权风险，现有方法依赖于日志概率，无法有效识别可疑数据集。

**核心思路**：CatShift框架利用灾难性遗忘的特性，通过对模型在可疑数据集上的输出变化进行分析，判断其是否为模型原始训练数据的一部分。

**技术框架**：CatShift的整体架构包括数据集输入、模型输出监测和统计分析三个主要模块。首先，模型在可疑数据集上进行微调，然后比较输出变化与已知非成员集的变化。

**关键创新**：CatShift的创新在于其不依赖于内部模型日志，而是通过输出变化来进行推断，这一方法在现有技术中尚属首次。

**关键设计**：在关键设计方面，CatShift采用了特定的微调策略和输出比较方法，确保能够有效捕捉到模型在接触可疑数据集后的输出变化。

## 📊 实验亮点

实验结果显示，CatShift在多种开放源代码和API基础的LLMs上均表现优异，能够在无法访问日志的情况下有效识别数据集成员资格，提升了数据保护的可靠性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括保护专有数据集的版权、增强数据隐私安全性以及为法律合规提供技术支持。随着大语言模型的广泛应用，CatShift能够为企业和研究机构提供有效的工具，以防止数据泄露和版权侵犯。

## 📄 摘要（原文）

> Large Language Models (LLMs) have revolutionized Natural Language Processing by excelling at interpreting, reasoning about, and generating human language. However, their reliance on large-scale, often proprietary datasets poses a critical challenge: unauthorized usage of such data can lead to copyright infringement and significant financial harm. Existing dataset-inference methods typically depend on log probabilities to detect suspicious training material, yet many leading LLMs have begun withholding or obfuscating these signals. This reality underscores the pressing need for label-only approaches capable of identifying dataset membership without relying on internal model logits.
>   We address this gap by introducing CatShift, a label-only dataset-inference framework that capitalizes on catastrophic forgetting: the tendency of an LLM to overwrite previously learned knowledge when exposed to new data. If a suspicious dataset was previously seen by the model, fine-tuning on a portion of it triggers a pronounced post-tuning shift in the model's outputs; conversely, truly novel data elicits more modest changes. By comparing the model's output shifts for a suspicious dataset against those for a known non-member validation set, we statistically determine whether the suspicious set is likely to have been part of the model's original training corpus. Extensive experiments on both open-source and API-based LLMs validate CatShift's effectiveness in logit-inaccessible settings, offering a robust and practical solution for safeguarding proprietary data.


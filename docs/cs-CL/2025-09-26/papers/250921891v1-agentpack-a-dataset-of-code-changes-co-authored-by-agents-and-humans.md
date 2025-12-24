---
layout: default
title: "AgentPack: A Dataset of Code Changes, Co-Authored by Agents and Humans"
---

# AgentPack: A Dataset of Code Changes, Co-Authored by Agents and Humans

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21891" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21891v1</a>
  <a href="https://arxiv.org/pdf/2509.21891.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21891v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21891v1', 'AgentPack: A Dataset of Code Changes, Co-Authored by Agents and Humans')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yangtian Zi, Zixuan Wu, Aleksander Boruch-Gruszecki, Jonathan Bell, Arjun Guha

**分类**: cs.SE, cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**AgentPack：一个由智能体与人类共同编写的代码变更数据集，用于提升代码编辑模型性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码编辑` `数据集` `软件工程智能体` `代码生成` `大型语言模型`

## 📋 核心要点

1. 现有代码编辑模型依赖挖掘提交记录和拉取请求，但这些数据通常包含噪声，例如提交信息简短、提交内容混杂等。
2. AgentPack数据集利用人类与智能体共同编写的代码变更，这些变更范围更窄、目标更明确，且提交信息由LLM生成，包含更详细的意图和原理。
3. 实验表明，在AgentPack上微调的模型性能优于在传统人类提交数据集上训练的模型，验证了该数据集的有效性。

## 📝 摘要（中文）

本文提出了AgentPack，一个包含130万个代码编辑的数据集，这些编辑由Claude Code、OpenAI Codex和Cursor Agent等智能体与人类共同完成，涵盖了截至2025年8月中旬的公共GitHub项目。论文描述了数据集的识别和管理流程，量化了这些智能体的采用趋势，并分析了编辑的结构属性。实验结果表明，在AgentPack上微调的模型优于在先前仅包含人类提交的数据集上训练的模型，突显了利用软件工程智能体的公开数据来训练未来代码编辑模型的潜力。

## 🔬 方法详解

**问题定义**：现有代码编辑模型的训练依赖于从GitHub等平台挖掘的提交记录和拉取请求。然而，这些数据存在诸多问题，例如提交信息过于简短难以理解，单个提交可能包含多个不相关的修改，以及大量提交来自简单的、基于规则的机器人，导致训练数据质量不高。这些问题限制了代码编辑模型的性能提升。

**核心思路**：论文的核心思路是利用软件工程智能体（如Claude Code、OpenAI Codex等）与人类共同编写的代码变更来构建高质量的训练数据集。这些智能体生成的代码变更通常范围更小、目标更明确，并且由LLM生成的提交信息能够更清晰地表达意图和原理。此外，这些变更经过人类维护者的审查，进一步保证了数据质量。

**技术框架**：AgentPack数据集的构建流程主要包括以下几个步骤：1) 从GitHub等公共代码仓库中识别由软件工程智能体参与的代码提交；2) 过滤和清洗数据，去除低质量的提交；3) 提取代码变更和对应的提交信息，构建训练样本；4) 对数据集进行统计分析，例如智能体的采用趋势、编辑的结构属性等。

**关键创新**：AgentPack数据集的关键创新在于其数据来源。与以往依赖人类提交的数据集不同，AgentPack包含了大量由智能体与人类共同编写的代码变更。这种数据来源能够提供更清晰、更结构化的训练样本，从而提升代码编辑模型的性能。此外，数据集构建过程中的人工审查也保证了数据质量。

**关键设计**：论文中并未详细描述具体的参数设置、损失函数或网络结构等技术细节。重点在于数据集的构建和分析，以及利用该数据集训练代码编辑模型并验证其有效性。数据集的规模为130万个代码编辑，涵盖了多种编程语言和项目。

## 📊 实验亮点

实验结果表明，在AgentPack数据集上微调的代码编辑模型优于在传统人类提交数据集上训练的模型。这表明利用软件工程智能体的公开数据能够有效提升代码编辑模型的性能。具体的性能提升幅度未知，论文重点在于验证数据集的有效性。

## 🎯 应用场景

AgentPack数据集可用于训练和评估各种代码编辑模型，例如代码补全、代码修复、代码重构等。该数据集能够提升代码编辑模型的性能和泛化能力，从而提高软件开发的效率和质量。此外，该数据集还可以用于研究软件工程智能体的行为和影响。

## 📄 摘要（原文）

> Fine-tuning large language models for code editing has typically relied on mining commits and pull requests. The working hypothesis has been that commit messages describe human intent in natural language, and patches to code describe the changes that implement that intent. However, much of the previously collected data is noisy: commit messages are terse, human-written commits commingle several unrelated edits, and many commits come from simple, rule-based bots.
>   The recent adoption of software engineering agents changes this landscape. Code changes co-authored by humans and agents tend to be more narrowly scoped and focused on clearer goals. Their commit messages, generated by LLMs, articulate intent and rationale in much greater detail. Moreover, when these changes land in public repositories, they are implicitly filtered by humans: maintainers discard low-quality commits to their projects.
>   We present AgentPack, a corpus of 1.3M code edits co-authored by Claude Code, OpenAI Codex, and Cursor Agent across public GitHub projects up to mid-August 2025. We describe the identification and curation pipeline, quantify adoption trends of these agents, and analyze the structural properties of the edits. Finally, we show that models fine-tuned on AgentPack can outperform models trained on prior human-only commit corpora, highlighting the potential of using public data from software engineering agents to train future code-editing models.


---
layout: default
title: Large Language Models as Autonomous Spacecraft Operators in Kerbal Space Program
---

# Large Language Models as Autonomous Spacecraft Operators in Kerbal Space Program

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19896" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19896v1</a>
  <a href="https://arxiv.org/pdf/2505.19896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19896v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19896v1', 'Large Language Models as Autonomous Spacecraft Operators in Kerbal Space Program')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alejandro Carrasco, Victor Rodriguez-Fernandez, Richard Linares

**分类**: cs.AI, astro-ph.IM, cs.CL

**发布日期**: 2025-05-26

**备注**: Non revised version for paper going to be published in Journal of Advances in Space Research

**DOI**: [10.1016/j.asr.2025.06.034](https://doi.org/10.1016/j.asr.2025.06.034)

**🔗 代码/项目**: [GITHUB](https://github.com/ARCLab-MIT/kspdg) | [HUGGINGFACE](https://huggingface.co/OhhTuRnz)

---

## 💡 一句话要点

**提出基于大语言模型的自主航天器操作方案以解决卫星自主决策问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `自主卫星操作` `航天控制` `决策支持` `机器学习`

## 📋 核心要点

1. 现有方法在自主卫星操作中缺乏有效的决策支持，尤其是在非合作环境下的复杂任务中。
2. 本文提出了一种基于大语言模型的自主代理，通过提示工程和微调技术来提升决策能力。
3. 我们的LLM代理在KSPDG挑战赛中表现优异，获得第二名，展示了其在航天控制中的潜力。

## 📝 摘要（中文）

近年来，大语言模型（LLMs）作为自主代理的应用趋势逐渐显现，能够根据用户文本提示采取行动。本文旨在将这一概念应用于航天控制领域，使LLMs在自主卫星操作的决策过程中发挥重要作用。作为这一目标的第一步，我们开发了一种基于LLM的解决方案，参与了Kerbal Space Program Differential Games（KSPDG）挑战赛。这是一项公开的软件设计竞赛，参与者需创建自主代理以操控参与非合作空间操作的卫星。我们的方法利用了提示工程、少量示例提示和微调技术，成功开发出一款有效的LLM代理，并在比赛中获得第二名。根据我们的了解，这项工作开创性地将LLM代理整合到航天研究中。项目包含多个开放的代码库，以促进复制和进一步研究，代码库可在GitHub上访问，训练模型和数据集可在Hugging Face上获取。

## 🔬 方法详解

**问题定义**：本文旨在解决自主卫星操作中的决策支持问题，现有方法在非合作环境下的复杂任务中表现不足，缺乏灵活性和适应性。

**核心思路**：我们提出利用大语言模型（LLMs）作为自主代理，通过精心设计的提示和少量示例来引导模型进行有效决策，提升其在复杂航天任务中的表现。

**技术框架**：整体架构包括数据收集、模型训练和评估三个主要阶段。首先，收集与航天操作相关的数据，然后对LLM进行微调，最后在KSP游戏引擎中进行测试和评估。

**关键创新**：本研究的创新点在于将LLM应用于航天领域，尤其是在非合作卫星操作中，开创性地将自然语言处理技术与航天控制相结合，提升了决策的智能化水平。

**关键设计**：在模型训练中，我们采用了特定的损失函数和网络结构，结合少量示例提示技术，确保模型能够在有限的信息下做出准确的决策。

## 📊 实验亮点

在KSPDG挑战赛中，我们的LLM代理获得了第二名的优异成绩，展示了其在复杂航天操作中的有效性。与其他参赛者相比，我们的方法在决策准确性和灵活性上有显著提升，证明了大语言模型在航天领域的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自主卫星操作、航天任务规划和智能决策支持系统。通过将大语言模型应用于航天控制，可以显著提高卫星在复杂环境下的自主决策能力，未来可能推动航天探索和卫星网络的智能化发展。

## 📄 摘要（原文）

> Recent trends are emerging in the use of Large Language Models (LLMs) as autonomous agents that take actions based on the content of the user text prompts. We intend to apply these concepts to the field of Control in space, enabling LLMs to play a significant role in the decision-making process for autonomous satellite operations. As a first step towards this goal, we have developed a pure LLM-based solution for the Kerbal Space Program Differential Games (KSPDG) challenge, a public software design competition where participants create autonomous agents for maneuvering satellites involved in non-cooperative space operations, running on the KSP game engine. Our approach leverages prompt engineering, few-shot prompting, and fine-tuning techniques to create an effective LLM-based agent that ranked 2nd in the competition. To the best of our knowledge, this work pioneers the integration of LLM agents into space research. The project comprises several open repositories to facilitate replication and further research. The codebase is accessible on \href{https://github.com/ARCLab-MIT/kspdg}{GitHub}, while the trained models and datasets are available on \href{https://huggingface.co/OhhTuRnz}{Hugging Face}. Additionally, experiment tracking and detailed results can be reviewed on \href{https://wandb.ai/carrusk/huggingface}{Weights \& Biases


---
layout: default
title: "RepoDebug: Repository-Level Multi-Task and Multi-Language Debugging Evaluation of Large Language Models"
---

# RepoDebug: Repository-Level Multi-Task and Multi-Language Debugging Evaluation of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04078" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04078v2</a>
  <a href="https://arxiv.org/pdf/2509.04078.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04078v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04078v2', 'RepoDebug: Repository-Level Multi-Task and Multi-Language Debugging Evaluation of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingjing Liu, Zeming Liu, Zihao Cheng, Mengliang He, Xiaoming Shi, Yuhang Guo, Xiangrong Zhu, Yuanfang Guo, Yunhong Wang, Haifeng Wang

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-04 (更新: 2025-09-08)

**备注**: 30 pages, 12 figures, EMNLP 2025 Findings

---

## 💡 一句话要点

**RepoDebug：用于评估大型语言模型在仓库级多任务多语言调试能力的数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码调试` `大型语言模型` `仓库级调试` `多任务学习` `多语言支持`

## 📋 核心要点

1. 现有代码调试数据集主要关注函数级别，忽略了实际应用中更复杂的仓库级别场景，导致对LLM调试能力的评估不完整。
2. RepoDebug数据集旨在提供一个更全面、更真实的仓库级代码调试评估平台，支持多任务、多语言和多种错误类型。
3. 实验结果表明，即使是当前表现最佳的LLM，在RepoDebug数据集上的仓库级调试能力仍然有待提高，揭示了该领域的挑战。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码调试方面表现出显著的熟练度，尤其是在自动程序修复方面，这可以大大减少开发人员的时间消耗并提高他们的效率。为了促进代码调试的发展，调试数据集取得了显著的进步。然而，这些数据集主要侧重于评估LLM的函数级代码修复能力，而忽略了更复杂和真实的仓库级场景，这导致对LLM在仓库级调试中面临的挑战的理解不完整。虽然已经提出了一些仓库级数据集，但它们通常受到任务、语言和错误类型多样性有限等限制。为了缓解这一挑战，本文介绍RepoDebug，一个多任务和多语言仓库级代码调试数据集，包含22种错误亚型，支持8种常用的编程语言和3种调试任务。此外，我们对10个LLM进行了评估实验，其中表现最佳的模型Claude 3.5 Sonnect在仓库级调试中仍然表现不佳。

## 🔬 方法详解

**问题定义**：现有代码调试数据集主要集中在函数级别，缺乏对仓库级别复杂场景的覆盖。这些数据集在任务类型、支持语言和错误类型方面存在局限性，无法全面评估LLM在实际软件开发中的调试能力。因此，需要一个更全面、更真实的仓库级调试数据集，以推动LLM在该领域的进一步发展。

**核心思路**：RepoDebug的核心思路是构建一个多任务、多语言的仓库级代码调试数据集，包含多种错误类型，以模拟真实的软件开发场景。通过在该数据集上评估LLM的调试能力，可以更准确地了解LLM在实际应用中的表现，并为未来的研究提供基准。

**技术框架**：RepoDebug数据集包含以下几个关键组成部分：1) 多种编程语言的支持（8种常用语言）；2) 多种调试任务的支持（3种调试任务）；3) 丰富的错误类型（22种错误亚型）；4) 仓库级别的代码结构。该数据集的设计旨在模拟真实的软件开发环境，并提供多样化的调试场景。

**关键创新**：RepoDebug的主要创新在于其全面性和真实性。与现有的代码调试数据集相比，RepoDebug更关注仓库级别的调试，支持多种编程语言、调试任务和错误类型。这使得RepoDebug能够更准确地评估LLM在实际软件开发中的调试能力。

**关键设计**：RepoDebug数据集的构建过程中，关键的设计包括：1) 错误类型的选择，涵盖了常见的软件缺陷；2) 编程语言的选择，覆盖了广泛使用的编程语言；3) 调试任务的设计，模拟了真实的调试流程；4) 数据集的规模，保证了评估的可靠性。此外，RepoDebug还提供了详细的文档和评估工具，方便研究人员使用。

## 📊 实验亮点

对10个LLM在RepoDebug数据集上进行了评估，结果表明，即使是表现最佳的Claude 3.5 Sonnect模型，在仓库级调试任务中仍然表现不佳。这表明当前LLM在处理复杂的仓库级代码调试问题时仍然面临挑战，为未来的研究提供了明确的方向。

## 🎯 应用场景

RepoDebug数据集可用于评估和比较不同LLM在仓库级代码调试方面的能力，推动自动程序修复技术的发展。该数据集还可以用于训练和优化LLM，提高其在实际软件开发中的调试效率。此外，RepoDebug可以帮助开发人员更好地了解LLM的优势和局限性，从而更有效地利用LLM来辅助软件开发。

## 📄 摘要（原文）

> Large Language Models (LLMs) have exhibited significant proficiency in code debugging, especially in automatic program repair, which may substantially reduce the time consumption of developers and enhance their efficiency. Significant advancements in debugging datasets have been made to promote the development of code debugging. However, these datasets primarily focus on assessing the LLM's function-level code repair capabilities, neglecting the more complex and realistic repository-level scenarios, which leads to an incomplete understanding of the LLM's challenges in repository-level debugging. While several repository-level datasets have been proposed, they often suffer from limitations such as limited diversity of tasks, languages, and error types. To mitigate this challenge, this paper introduces RepoDebug, a multi-task and multi-language repository-level code debugging dataset with 22 subtypes of errors that supports 8 commonly used programming languages and 3 debugging tasks. Furthermore, we conduct evaluation experiments on 10 LLMs, where Claude 3.5 Sonnect, the best-performing model, still cannot perform well in repository-level debugging.


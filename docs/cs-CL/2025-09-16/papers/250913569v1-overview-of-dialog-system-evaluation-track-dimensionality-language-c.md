---
layout: default
title: "Overview of Dialog System Evaluation Track: Dimensionality, Language, Culture and Safety at DSTC 12"
---

# Overview of Dialog System Evaluation Track: Dimensionality, Language, Culture and Safety at DSTC 12

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13569" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13569v1</a>
  <a href="https://arxiv.org/pdf/2509.13569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13569v1', 'Overview of Dialog System Evaluation Track: Dimensionality, Language, Culture and Safety at DSTC 12')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: John Mendonça, Lining Zhang, Rahul Mallidi, Alon Lavie, Isabel Trancoso, Luis Fernando D'Haro, João Sedoc

**分类**: cs.CL

**发布日期**: 2025-09-16

**备注**: DSTC12 Track 1 Overview Paper. https://chateval.org/dstc12

---

## 💡 一句话要点

**DSTC12对话系统评测：关注维度、语言、文化和安全**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话系统评估` `多维评估` `多语言安全` `文化安全` `大型语言模型` `DSTC12` `自然语言处理`

## 📋 核心要点

1. 现有对话系统评估方法在维度、语言、文化和安全方面存在不足，传统指标难以全面评估LLM。
2. DSTC12 Track 1旨在通过多维评估和多语言文化安全检测，填补对话系统评估中的关键差距。
3. 实验结果表明，现有模型在多维评估和文化安全方面仍有提升空间，尤其是在文化敏感性方面。

## 📝 摘要（中文）

大型语言模型（LLM）的快速发展加剧了对鲁棒对话系统评估的需求，但全面的评估仍然具有挑战性。传统的指标通常不足，并且安全考虑因素经常被狭隘地定义或存在文化偏见。DSTC12 Track 1“对话系统评估：维度、语言、文化和安全”是解决这些关键差距的持续努力的一部分。该track包含两个子任务：（1）对话级别、多维自动评估指标，以及（2）多语言和多文化安全检测。对于任务1，专注于10个对话维度，Llama-3-8B基线实现了最高的平均Spearman相关性（0.1681），表明有很大的改进空间。在任务2中，虽然参与团队在多语言安全子集上显著优于Llama-Guard-3-1B基线（最高ROC-AUC 0.9648），但基线在文化子集上表现更好（0.5126 ROC-AUC），突出了文化意识安全方面的关键需求。本文介绍了提供给参与者的数据集和基线，以及每个提出的两个子任务的提交评估结果。

## 🔬 方法详解

**问题定义**：论文旨在解决对话系统评估中维度单一、缺乏多语言文化考量以及安全定义狭隘的问题。现有评估方法难以捕捉对话的复杂性，并且在跨文化场景下的安全性评估不足。

**核心思路**：论文的核心思路是通过构建包含多维度评估指标和多语言文化安全检测的数据集和评测任务，促进对话系统评估方法的发展，特别是提升其在文化敏感性和安全性方面的能力。

**技术框架**：DSTC12 Track 1包含两个子任务：一是对话级别、多维自动评估指标，评估模型在10个对话维度上的表现；二是多语言和多文化安全检测，旨在检测模型在不同语言和文化背景下的安全性。组织方提供了数据集和基线模型，供参赛者进行模型训练和评估。

**关键创新**：该论文的关键创新在于其对对话系统评估维度的扩展，以及对多语言和多文化安全问题的关注。它不仅考虑了对话的质量，还强调了对话系统在不同文化背景下的安全性，这在以往的研究中往往被忽视。

**关键设计**：在任务1中，使用了Spearman相关性来评估模型预测的评估指标与人工评估指标之间的相关性。在任务2中，使用了ROC-AUC来评估模型在安全检测任务中的性能。基线模型包括Llama-3-8B和Llama-Guard-3-1B，为参赛者提供了一个起点。

## 📊 实验亮点

在对话维度评估任务中，Llama-3-8B基线取得了0.1681的平均Spearman相关性，表明仍有较大提升空间。在多语言安全检测任务中，参赛团队显著优于Llama-Guard-3-1B基线，ROC-AUC达到0.9648，但在文化安全检测任务中，基线表现更好（ROC-AUC 0.5126），突显了文化敏感性方面的挑战。

## 🎯 应用场景

该研究成果可应用于开发更鲁棒、更安全、更具文化敏感性的对话系统。例如，可以用于评估和改进聊天机器人、虚拟助手等应用，确保它们在不同文化背景下都能提供高质量和安全的服务。未来的研究可以进一步探索更细粒度的文化差异，并开发更有效的文化安全检测方法。

## 📄 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has intensified the need for robust dialogue system evaluation, yet comprehensive assessment remains challenging. Traditional metrics often prove insufficient, and safety considerations are frequently narrowly defined or culturally biased. The DSTC12 Track 1, "Dialog System Evaluation: Dimensionality, Language, Culture and Safety," is part of the ongoing effort to address these critical gaps. The track comprised two subtasks: (1) Dialogue-level, Multi-dimensional Automatic Evaluation Metrics, and (2) Multilingual and Multicultural Safety Detection. For Task 1, focused on 10 dialogue dimensions, a Llama-3-8B baseline achieved the highest average Spearman's correlation (0.1681), indicating substantial room for improvement. In Task 2, while participating teams significantly outperformed a Llama-Guard-3-1B baseline on the multilingual safety subset (top ROC-AUC 0.9648), the baseline proved superior on the cultural subset (0.5126 ROC-AUC), highlighting critical needs in culturally-aware safety. This paper describes the datasets and baselines provided to participants, as well as submission evaluation results for each of the two proposed subtasks.


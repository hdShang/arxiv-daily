---
layout: default
title: An Empirical Study of Many-to-Many Summarization with Large Language Models
---

# An Empirical Study of Many-to-Many Summarization with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12983" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12983v1</a>
  <a href="https://arxiv.org/pdf/2505.12983.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12983v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12983v1', 'An Empirical Study of Many-to-Many Summarization with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaan Wang, Fandong Meng, Zengkui Sun, Yunlong Liang, Yuxuan Cao, Jiarong Xu, Haoxiang Shi, Jie Zhou

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-19

**备注**: Accepted to ACL 2025 main conference

---

## 💡 一句话要点

**提出多对多摘要生成方法以提升多语言处理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多对多摘要生成` `大型语言模型` `指令微调` `多语言处理` `事实性问题`

## 📋 核心要点

1. 现有方法在多语言摘要生成中面临事实性问题，且零-shot模型的性能不足以满足实际应用需求。
2. 本研究通过重新组织数据集并评估18种LLMs，探索其在多对多摘要生成中的能力，提出了指令微调的方法。
3. 实验结果显示，经过指令微调的开源LLMs在自动评估中显著优于零-shot LLMs，且与传统模型的性能相当。

## 📝 摘要（中文）

多对多摘要生成（M2MS）旨在处理任何语言的文档并生成相应语言的摘要。近年来，大型语言模型（LLMs）展现出强大的多语言能力，具备在实际应用中执行M2MS的潜力。本研究系统性地探讨了LLMs在M2MS任务中的能力。我们重新组织了基于八个领域特定数据集的M2MS数据，包含47.8K样本，涵盖五个领域和六种语言，用于训练和评估LLMs。实验表明，零-shot LLMs在结果上与微调的传统模型相当，而经过指令微调后，开源LLMs的M2MS能力显著提升，超越了零-shot LLMs（包括GPT-4）。然而，人类评估显示LLMs仍面临事实性问题，指令微调可能加剧该问题，因此控制事实错误成为构建LLM摘要生成器的关键。

## 🔬 方法详解

**问题定义**：本研究旨在解决多对多摘要生成（M2MS）中的事实性问题和零-shot模型性能不足的挑战。现有方法在多语言处理时，常常无法保证生成摘要的准确性和可靠性。

**核心思路**：论文提出通过重新组织数据集并对LLMs进行指令微调，以提升其在多对多摘要生成任务中的表现。这样的设计旨在充分利用LLMs的多语言能力，同时增强其在特定任务上的适应性。

**技术框架**：整体架构包括数据集的重新组织、LLMs的零-shot和指令微调评估。研究使用了47.8K样本的多语言数据集，并对18种LLMs进行了基准测试。

**关键创新**：最重要的创新在于通过指令微调显著提升LLMs的M2MS能力，并且在自动评估中超越了包括GPT-4在内的零-shot模型。这一方法展示了LLMs在特定任务上的可调性和适应性。

**关键设计**：在实验中，采用了多种LLMs进行比较，包括微调的传统模型（如mBART），并通过自动评估和人类评估来验证模型的性能。关键参数和损失函数的设置经过精心设计，以确保模型在多语言摘要生成中的有效性。

## 📊 实验亮点

实验结果显示，经过指令微调的开源LLMs在多对多摘要生成任务中，自动评估得分显著高于零-shot LLMs（包括GPT-4），并且与微调的传统模型相当。这表明指令微调能够有效提升LLMs的任务特定能力。

## 🎯 应用场景

该研究的潜在应用领域包括多语言信息检索、跨语言文档摘要生成以及国际化内容的自动化处理。随着全球信息交流的加速，M2MS技术将为多语言用户提供更高效的信息获取方式，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Many-to-many summarization (M2MS) aims to process documents in any language and generate the corresponding summaries also in any language. Recently, large language models (LLMs) have shown strong multi-lingual abilities, giving them the potential to perform M2MS in real applications. This work presents a systematic empirical study on LLMs' M2MS ability. Specifically, we first reorganize M2MS data based on eight previous domain-specific datasets. The reorganized data contains 47.8K samples spanning five domains and six languages, which could be used to train and evaluate LLMs. Then, we benchmark 18 LLMs in a zero-shot manner and an instruction-tuning manner. Fine-tuned traditional models (e.g., mBART) are also conducted for comparisons. Our experiments reveal that, zero-shot LLMs achieve competitive results with fine-tuned traditional models. After instruct-tuning, open-source LLMs can significantly improve their M2MS ability, and outperform zero-shot LLMs (including GPT-4) in terms of automatic evaluations. In addition, we demonstrate that this task-specific improvement does not sacrifice the LLMs' general task-solving abilities. However, as revealed by our human evaluation, LLMs still face the factuality issue, and the instruction tuning might intensify the issue. Thus, how to control factual errors becomes the key when building LLM summarizers in real applications, and is worth noting in future research.


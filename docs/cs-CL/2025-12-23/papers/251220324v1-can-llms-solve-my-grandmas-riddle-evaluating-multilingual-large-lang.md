---
layout: default
title: Can LLMs Solve My Grandma's Riddle? Evaluating Multilingual Large Language Models on Reasoning Traditional Bangla Tricky Riddles
---

# Can LLMs Solve My Grandma's Riddle? Evaluating Multilingual Large Language Models on Reasoning Traditional Bangla Tricky Riddles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20324" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20324v1</a>
  <a href="https://arxiv.org/pdf/2512.20324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20324v1', 'Can LLMs Solve My Grandma\'s Riddle? Evaluating Multilingual Large Language Models on Reasoning Traditional Bangla Tricky Riddles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nurul Labib Sayeedi, Md. Faiyaz Abdullah Sayeedi, Khushnur Binte Jahangir, Swakkhar Shatabda, Sarah Masud Preum

**分类**: cs.CL

**发布日期**: 2025-12-23

**🔗 代码/项目**: [GITHUB](https://github.com/Labib1610/BanglaRiddleEval)

---

## 💡 一句话要点

**BanglaRiddleEval：评估多语言大模型在孟加拉语谜语推理上的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `孟加拉语` `谜语推理` `低资源语言` `基准测试`

## 📋 核心要点

1. 现有LLM在形象化、文化背景和低资源语言环境下的推理能力有待提升，尤其是在孟加拉语等低资源语言中。
2. 论文构建了BanglaRiddleEval基准，包含孟加拉语传统谜语，用于评估LLM在推理、歧义消解等方面的能力。
3. 实验结果表明，现有LLM在孟加拉语谜语推理方面与人类水平存在差距，为未来研究提供了挑战。

## 📝 摘要（中文）

大型语言模型（LLMs）在许多NLP基准测试中表现出令人印象深刻的性能，但它们在形象化、具有文化基础和低资源环境中的推理能力仍未得到充分探索。本文通过引入BanglaRiddleEval来解决孟加拉语的这一差距，BanglaRiddleEval是一个包含1,244个传统孟加拉语谜语的基准，这些谜语被实例化为四个任务（总共4,976个谜语-任务组合）。使用基于LLM的pipeline，我们生成了思维链解释、语义连贯的干扰项和细粒度的歧义注释，并在不同的prompt策略下评估了一系列开源和闭源模型。模型在生成式问答中实现了适度的语义重叠，但正确率较低；多项选择题的准确率峰值仅为约56%，而人类基线为83%；歧义消解的范围从大约26%到68%，高质量的解释仅限于最强的模型。这些结果表明，当前的LLM捕获了一些孟加拉语谜语推理所需的线索，但与人类水平的性能相差甚远，从而将BanglaRiddleEval确立为一个具有挑战性的低资源形象推理新基准。所有数据、代码和评估脚本都可以在GitHub上找到：https://github.com/Labib1610/BanglaRiddleEval。

## 🔬 方法详解

**问题定义**：论文旨在评估大型语言模型（LLMs）在理解和解决传统孟加拉语谜语方面的能力。现有方法在低资源、文化相关的语言推理方面存在不足，无法充分捕捉谜语中的隐喻、歧义和文化背景。这导致LLMs在处理此类任务时表现不佳，缺乏有效的评估基准。

**核心思路**：论文的核心思路是构建一个专门针对孟加拉语谜语的评估基准（BanglaRiddleEval），并利用该基准来系统地评估各种LLMs的推理能力。通过分析LLMs在不同任务上的表现，揭示其在处理低资源、形象化语言推理方面的局限性，并为未来的研究提供方向。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据集构建：收集并整理1244个传统孟加拉语谜语，并将其转化为四个不同的任务（如生成式问答、多项选择题、歧义消解等）。2) 数据增强：利用LLM生成思维链解释、语义连贯的干扰项和细粒度的歧义注释，以扩充数据集。3) 模型评估：选择一系列开源和闭源LLMs，并在BanglaRiddleEval基准上进行评估，采用不同的prompt策略。4) 结果分析：分析LLMs在不同任务上的表现，并与人类基线进行比较，以评估其推理能力。

**关键创新**：该论文的关键创新在于：1) 提出了BanglaRiddleEval，这是一个专门针对孟加拉语谜语推理的基准，填补了低资源语言推理评估的空白。2) 利用LLM生成思维链解释和歧义注释，为谜语推理提供了更丰富的上下文信息。3) 系统地评估了各种LLMs在孟加拉语谜语推理上的表现，揭示了其在处理低资源、形象化语言推理方面的局限性。

**关键设计**：在数据集构建方面，论文将每个谜语转化为四个任务：生成式问答（Generative QA）、多项选择题（MCQ）、歧义消解（Ambiguity Resolution）和解释生成（Explanation Generation）。在模型评估方面，采用了不同的prompt策略，例如zero-shot、few-shot和chain-of-thought prompting。评估指标包括生成式问答的语义重叠度、多项选择题的准确率和歧义消解的准确率。

## 📊 实验亮点

实验结果表明，现有LLM在BanglaRiddleEval基准上的表现远低于人类水平。多项选择题的准确率峰值仅为56%，而人类基线为83%。歧义消解的准确率范围为26%至68%。这些结果表明，LLM虽然能捕捉到一些线索，但在孟加拉语谜语推理方面仍有很大的提升空间。

## 🎯 应用场景

该研究成果可应用于提升LLM在低资源语言和文化背景下的推理能力，例如：开发更智能的孟加拉语聊天机器人、教育辅助工具和文化遗产保护应用。此外，BanglaRiddleEval基准可以促进对LLM在形象化语言理解方面的研究，并推动相关技术的进步。

## 📄 摘要（原文）

> Large Language Models (LLMs) show impressive performance on many NLP benchmarks, yet their ability to reason in figurative, culturally grounded, and low-resource settings remains underexplored. We address this gap for Bangla by introducing BanglaRiddleEval, a benchmark of 1,244 traditional Bangla riddles instantiated across four tasks (4,976 riddle-task artifacts in total). Using an LLM-based pipeline, we generate Chain-of-Thought explanations, semantically coherent distractors, and fine-grained ambiguity annotations, and evaluate a diverse suite of open-source and closed-source models under different prompting strategies. Models achieve moderate semantic overlap on generative QA but low correctness, MCQ accuracy peaks at only about 56% versus an 83% human baseline, and ambiguity resolution ranges from roughly 26% to 68%, with high-quality explanations confined to the strongest models. These results show that current LLMs capture some cues needed for Bangla riddle reasoning but remain far from human-level performance, establishing BanglaRiddleEval as a challenging new benchmark for low-resource figurative reasoning. All data, code, and evaluation scripts are available on GitHub: https://github.com/Labib1610/BanglaRiddleEval.


---
layout: default
title: "LLMs and their Limited Theory of Mind: Evaluating Mental State Annotations in Situated Dialogue"
---

# LLMs and their Limited Theory of Mind: Evaluating Mental State Annotations in Situated Dialogue

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02292" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02292v1</a>
  <a href="https://arxiv.org/pdf/2509.02292.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02292v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02292v1', 'LLMs and their Limited Theory of Mind: Evaluating Mental State Annotations in Situated Dialogue')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Katharine Kowalyshyn, Matthias Scheutz

**分类**: cs.CL

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**提出基于LLM的两步框架，评估团队对话中共享心智模型的偏差。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `共享心智模型` `团队对话` `偏差检测` `自然语言理解`

## 📋 核心要点

1. 现有方法难以有效评估团队对话中共享心智模型的偏差，阻碍了团队协作效率的提升。
2. 利用LLM作为标注者和偏差检测器，构建两步框架，自动识别和评估团队成员间心理状态的差异。
3. 实验结果表明，LLM在自然语言注释任务中表现良好，但在空间推理和歧义消除方面存在系统性误差。

## 📝 摘要（中文）

本文提出了一种新颖的两步框架，利用大型语言模型（LLM）作为人类风格的标注者，分析团队对话以追踪团队的共享心智模型（SMM），并作为自动偏差检测器，识别个体心理状态之间的差异。第一步，LLM通过识别来自合作远程搜索任务（CReST）语料库中面向任务的对话中的SMM元素来生成注释。然后，第二个LLM将这些LLM衍生的注释和人工注释与金标准标签进行比较，以检测和表征差异。本文为该用例定义了一个SMM一致性评估框架，并将其应用于六个CReST对话，最终生成：（1）人类和LLM注释的数据集；（2）SMM一致性的可重复评估框架；（3）基于LLM的差异检测的实证评估。结果表明，尽管LLM在简单的自然语言注释任务中表现出明显的一致性，但在需要空间推理或消除韵律线索歧义的场景中，它们会系统性地出错。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效评估团队对话中共享心智模型（SMM）的一致性问题。现有方法依赖人工标注，成本高昂且效率低下，难以大规模应用。此外，现有方法在处理需要复杂推理（如空间推理和韵律消歧）的对话时表现不佳。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的强大自然语言理解和生成能力，模拟人类标注者的行为，自动识别和评估团队对话中的SMM元素。通过比较LLM和人类标注的结果，可以发现LLM在理解SMM方面的局限性，并为改进LLM的推理能力提供指导。

**技术框架**：该框架包含两个主要步骤：1) LLM标注：使用一个LLM对CReST语料库中的团队对话进行标注，识别对话中与SMM相关的元素。2) 偏差检测：使用另一个LLM比较LLM生成的标注和人工标注，与金标准标签进行对比，以检测和表征差异。该框架还定义了一个SMM一致性评估框架，用于评估LLM标注的质量。

**关键创新**：该论文的关键创新在于提出了一种基于LLM的两步框架，用于自动评估团队对话中SMM的一致性。与传统的人工标注方法相比，该框架具有成本低、效率高的优点。此外，该框架还可以用于识别LLM在理解SMM方面的局限性，为改进LLM的推理能力提供指导。

**关键设计**：论文使用了CReST语料库，该语料库包含面向任务的团队对话。在LLM标注阶段，使用了提示工程（prompt engineering）技术，引导LLM识别对话中与SMM相关的元素。在偏差检测阶段，使用了多种评估指标，如准确率、召回率和F1值，评估LLM标注的质量。具体的参数设置、损失函数、网络结构等技术细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，LLM在简单的自然语言注释任务中表现出较高的一致性，但在需要空间推理或消除韵律线索歧义的场景中，LLM会系统性地出错。该研究揭示了LLM在理解复杂心理状态方面的局限性，为未来的研究方向提供了重要启示。具体的性能数据和提升幅度未在摘要中详细说明，属于未知信息。

## 🎯 应用场景

该研究成果可应用于提升团队协作效率、改进人机协作系统、以及开发更智能的对话代理。通过自动评估团队成员间的共享心智模型，可以及时发现和纠正沟通偏差，从而提高团队的整体表现。此外，该研究还可以用于训练更强大的LLM，使其能够更好地理解人类的心理状态。

## 📄 摘要（原文）

> What if large language models could not only infer human mindsets but also expose every blind spot in team dialogue such as discrepancies in the team members' joint understanding? We present a novel, two-step framework that leverages large language models (LLMs) both as human-style annotators of team dialogues to track the team's shared mental models (SMMs) and as automated discrepancy detectors among individuals' mental states. In the first step, an LLM generates annotations by identifying SMM elements within task-oriented dialogues from the Cooperative Remote Search Task (CReST) corpus. Then, a secondary LLM compares these LLM-derived annotations and human annotations against gold-standard labels to detect and characterize divergences. We define an SMM coherence evaluation framework for this use case and apply it to six CReST dialogues, ultimately producing: (1) a dataset of human and LLM annotations; (2) a reproducible evaluation framework for SMM coherence; and (3) an empirical assessment of LLM-based discrepancy detection. Our results reveal that, although LLMs exhibit apparent coherence on straightforward natural-language annotation tasks, they systematically err in scenarios requiring spatial reasoning or disambiguation of prosodic cues.


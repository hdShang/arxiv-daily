---
layout: default
title: Semi-structured LLM Reasoners Can Be Rigorously Audited
---

# Semi-structured LLM Reasoners Can Be Rigorously Audited

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24217" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24217v2</a>
  <a href="https://arxiv.org/pdf/2505.24217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24217v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24217v2', 'Semi-structured LLM Reasoners Can Be Rigorously Audited')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jixuan Leng, Cassandra A. Cohen, Zhixian Zhang, Chenyan Xiong, William W. Cohen

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出半结构化推理模型以解决大型语言模型的可审计性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理模型` `可审计性` `半结构化表示` `自动审计` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在推理过程中存在错误和遗漏，导致可信度不足，难以审计和识别偏见。
2. 本文提出的半结构化推理模型（SSRMs）生成可审计的推理轨迹，采用Python语法标记推理步骤。
3. 实验结果显示，SSRMs在十二个基准测试中表现优异，且审计能力未影响整体准确性。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）已具备推理能力，但其推理结果的可信度仍然存在问题，可能包含难以发现的错误和遗漏，进而掩盖模型输出中的偏见。为了解决这一问题，本文提出了半结构化推理模型（SSRMs），该模型能够生成半结构化的推理表示，采用非可执行的Python语法，标记每个推理步骤及其输入和输出。这种结构使得SSRMs的推理过程可以被自动审计，以识别推理缺陷。我们评估了三种审计方法，结果表明这些方法能够有效标记推理错误，同时SSRMs在多个基准测试中表现出强大的性能和良好的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型推理过程中的可信度和审计性问题。现有方法难以识别推理中的错误和偏见，导致结果不可靠。

**核心思路**：提出半结构化推理模型（SSRMs），通过生成半结构化的推理轨迹，标记推理步骤及其输入输出，从而实现自动审计。

**技术框架**：SSRMs的整体架构包括推理生成模块和审计模块。推理生成模块负责生成推理轨迹，审计模块则对这些轨迹进行分析，识别潜在的推理错误。

**关键创新**：SSRMs的主要创新在于其生成的推理轨迹采用非可执行的Python语法，使得审计过程更加系统化和自动化。这一设计与传统的推理模型有本质区别。

**关键设计**：在模型训练中，采用特定的损失函数来优化推理轨迹的生成质量，并通过多种审计方法（如手工审计、LLM生成审计和学习的典型性审计）来验证推理的准确性。

## 📊 实验亮点

实验结果表明，SSRMs在十二个基准测试中表现出色，与其他同类模型相比，准确性未受影响，且能够有效标记推理错误。具体而言，所有三种审计方法均能有效识别推理缺陷，显示出SSRMs的强大审计能力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动化决策支持等。通过提高大型语言模型的审计能力，可以增强其在敏感领域（如医疗、法律等）的应用可信度，进而推动其在实际场景中的广泛应用。

## 📄 摘要（原文）

> Although Large Language Models (LLMs) have become capable reasoners, the problem of faithfulness persists: their reasoning can contain errors and omissions that are difficult to detect and that may obscure biases in model outputs. To address this issue, we introduce Semi-Structured Reasoning Models (SSRMs), which are trained to produce semi-structured representations of reasoning. SSRMs generate reasoning traces in a non-executable Pythonic syntax that names each reasoning step and marks its inputs and outputs. This structure allows SSRM traces to be automatically audited to identify reasoning flaws. We evaluate three types of audits: hand-crafted structured reasoning audits, written in a domain-specific language (DSL) implemented in Python; LLM-generated structured reasoning audits; and learned typicality audits, which apply probabilistic models over reasoning traces. We show that all of these methods can be used to effectively flag probable reasoning errors. Importantly, the auditability of SSRMs does not appear to compromise overall accuracy: in evaluation on twelve benchmarks and two model families, SSRMs demonstrate strong performance and generalizability relative to other models of comparable size.


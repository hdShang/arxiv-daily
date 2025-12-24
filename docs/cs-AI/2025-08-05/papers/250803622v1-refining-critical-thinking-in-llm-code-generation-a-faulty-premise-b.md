---
layout: default
title: "Refining Critical Thinking in LLM Code Generation: A Faulty Premise-based Evaluation Framework"
---

# Refining Critical Thinking in LLM Code Generation: A Faulty Premise-based Evaluation Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03622" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03622v1</a>
  <a href="https://arxiv.org/pdf/2508.03622.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03622v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03622v1', 'Refining Critical Thinking in LLM Code Generation: A Faulty Premise-based Evaluation Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialin Li, Jinzhe Li, Gengxu Li, Yi Chang, Yuan Wu

**分类**: cs.AI

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出FPBench框架以解决LLM代码生成中的错误前提问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `错误前提` `评估框架` `推理能力` `自我审查` `多维评估`

## 📋 核心要点

1. 现有的代码生成模型在处理错误前提时表现不佳，导致生成代码的准确性和可靠性下降。
2. 论文提出FPBench框架，通过构建三类错误前提并引入多维评估指标，系统性地评估LLM的代码生成能力。
3. 实验结果显示，大多数模型在错误前提下的推理能力较差，且自我审查能力有限，强调了改进的必要性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在代码生成能力上的进步，它们对输入前提的依赖性加剧。当用户提供包含错误前提的输入时，代码生成的幻觉概率显著上升，暴露出其自我审查能力的不足。本文提出了FPBench，这是第一个针对错误前提的代码生成评估框架。通过系统构建三类错误前提并整合多维评估指标，对15个代表性LLM进行了深入评估。主要发现包括：大多数模型在错误前提下表现出较差的推理能力和次优的代码生成性能，严重依赖显式提示进行错误检测，自我审查能力有限；错误前提导致资源投资的收益递减，盲目增加长度无法提升质量；三类错误前提分别激活模型中的不同缺陷模式，揭示了代码生成模型认知机制的三重分离。该研究强调了LLMs在代码生成中主动验证前提的迫切需求，并通过FPBench框架和多维评估系统，为开发可靠的人本代码生成模型提供了理论基础和实践路径。

## 🔬 方法详解

**问题定义**：本文解决的问题是大型语言模型在处理错误前提时的代码生成能力不足，现有方法未能有效识别和处理这些错误前提，导致生成代码的质量下降。

**核心思路**：论文的核心思路是构建FPBench框架，系统性地评估LLM在面对错误前提时的表现，通过多维度的评估指标来揭示模型的缺陷和不足。

**技术框架**：FPBench框架包括三个主要模块：错误前提构建模块、评估指标整合模块和模型性能评估模块。错误前提构建模块负责生成不同类型的错误前提，评估指标整合模块则将多维评估指标结合起来，最后模型性能评估模块对15个LLM进行全面评估。

**关键创新**：FPBench框架是第一个专注于错误前提的代码生成评估工具，创新性地通过系统构建错误前提和多维评估指标，揭示了LLM在处理错误前提时的认知机制差异。

**关键设计**：在评估过程中，论文设计了三类错误前提，并针对每类错误前提设置了特定的评估指标，以便更准确地反映模型的性能和缺陷。

## 📊 实验亮点

实验结果表明，大多数LLM在面对错误前提时的推理能力较差，且自我审查能力有限。通过FPBench框架的评估，发现模型在错误前提下的性能显著低于预期，强调了改进的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化测试和智能编程助手等。FPBench框架为开发更可靠的代码生成模型提供了理论基础，未来可用于提升代码生成工具的准确性和用户体验。

## 📄 摘要（原文）

> With the advancement of code generation capabilities in large language models (LLMs), their reliance on input premises has intensified. When users provide inputs containing faulty premises, the probability of code generation hallucinations rises significantly, exposing deficiencies in their self-scrutiny capabilities. This paper proposes Faulty Premises Bench (FPBench), the first code generation evaluation framework targeting faulty premises. By systematically constructing three categories of faulty premises and integrating multi-dimensional evaluation metrics, it conducts in-depth assessments of 15 representative LLMs. The key findings are as follows: (1) Most models exhibit poor reasoning abilities and suboptimal code generation performance under faulty premises, heavily relying on explicit prompts for error detection, with limited self-scrutiny capabilities; (2) Faulty premises trigger a point of diminishing returns in resource investment, leading to blindly increasing length fails to enhance quality; (3) The three types of faulty premises respectively activate distinct defect patterns in models, revealing a triple dissociation in the cognitive mechanisms of code generation models. This study not only highlights the urgent need for LLMs to proactively verify premises in code generation but also, through the proposed FPBench framework and multi-dimensional evaluation system, provides a theoretical foundation and practical pathway for developing reliable, human-centric code generation models.


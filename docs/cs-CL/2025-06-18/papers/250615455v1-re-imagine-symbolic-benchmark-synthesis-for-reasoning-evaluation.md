---
layout: default
title: "RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation"
---

# RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15455" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15455v1</a>
  <a href="https://arxiv.org/pdf/2506.15455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15455v1', 'RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinnuo Xu, Rachel Lawrence, Kshitij Dubey, Atharva Pandey, Risa Ueno, Fabian Falck, Aditya V. Nori, Rahul Sharma, Amit Sharma, Javier Gonzalez

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-18

**备注**: ICML 2025

---

## 💡 一句话要点

**提出RE-IMAGINE框架以评估大型语言模型的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理能力` `大型语言模型` `因果推理` `问题生成` `性能评估` `统计回忆` `机器学习` `人工智能`

## 📋 核心要点

1. 现有大型语言模型在推理基准测试中的高准确率可能源于统计回忆，而非真实推理能力。
2. RE-IMAGINE框架通过生成不同层次的问题变体，评估LLMs的推理能力，克服了记忆依赖的局限性。
3. 实验结果显示，模型在面对问题变体时性能显著下降，揭示了其对统计回忆的依赖程度。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在推理基准测试中表现出高准确率。然而，尚不清楚这些结果是否源于真实的推理能力，还是仅仅是对训练集的统计回忆。受因果层次理论的启发，本文提出了RE-IMAGINE框架，旨在对LLMs的推理能力进行分层表征，并自动生成不同层次问题变体。通过改变中间符号表示，RE-IMAGINE能够生成大量无法仅通过记忆解决的问题。此外，该框架具有通用性，适用于数学、代码和逻辑等多个推理领域。我们在四个广泛使用的基准上展示了该框架，并观察到在模型查询问题变体时性能下降，表明模型在过去表现中对统计回忆的依赖程度，进而为未来针对推理层次的技能研究开辟了新方向。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理基准测试中表现高准确率的真实性问题，现有方法未能有效区分真实推理与统计回忆的影响。

**核心思路**：RE-IMAGINE框架通过引入因果层次理论，生成不同层次的推理问题变体，以评估模型的推理能力，避免仅依赖记忆的解决方案。

**技术框架**：该框架包括问题生成模块、推理能力评估模块和结果分析模块。问题生成模块通过中间符号表示改变问题，评估模块则对模型的推理能力进行量化分析。

**关键创新**：RE-IMAGINE的创新在于其能够生成大量无法通过记忆解决的问题变体，并且适用于多种推理领域，突破了传统方法的局限。

**关键设计**：框架中的问题生成采用符号表示，确保生成的问题具有多样性和复杂性，评估模块则使用标准化的性能指标来量化模型的推理能力。

## 📊 实验亮点

实验结果表明，当模型面对RE-IMAGINE生成的问题变体时，性能显著下降，部分模型的准确率降低了20%以上。这一发现强调了模型在推理任务中对统计回忆的依赖，提示了未来研究的方向。

## 🎯 应用场景

RE-IMAGINE框架具有广泛的应用潜力，能够用于评估和提升大型语言模型在数学、编程和逻辑推理等领域的能力。其设计可以为教育、智能问答系统和自动化推理工具等领域提供支持，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Recent Large Language Models (LLMs) have reported high accuracy on reasoning benchmarks. However, it is still unclear whether the observed results arise from true reasoning or from statistical recall of the training set. Inspired by the ladder of causation (Pearl, 2009) and its three levels (associations, interventions and counterfactuals), this paper introduces RE-IMAGINE, a framework to characterize a hierarchy of reasoning ability in LLMs, alongside an automated pipeline to generate problem variations at different levels of the hierarchy. By altering problems in an intermediate symbolic representation, RE-IMAGINE generates arbitrarily many problems that are not solvable using memorization alone. Moreover, the framework is general and can work across reasoning domains, including math, code, and logic. We demonstrate our framework on four widely-used benchmarks to evaluate several families of LLMs, and observe reductions in performance when the models are queried with problem variations. These assessments indicate a degree of reliance on statistical recall for past performance, and open the door to further research targeting skills across the reasoning hierarchy.


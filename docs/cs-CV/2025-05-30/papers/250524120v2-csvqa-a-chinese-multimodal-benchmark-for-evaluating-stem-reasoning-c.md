---
layout: default
title: "CSVQA: A Chinese Multimodal Benchmark for Evaluating STEM Reasoning Capabilities of VLMs"
---

# CSVQA: A Chinese Multimodal Benchmark for Evaluating STEM Reasoning Capabilities of VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24120" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24120v2</a>
  <a href="https://arxiv.org/pdf/2505.24120.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24120v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24120v2', 'CSVQA: A Chinese Multimodal Benchmark for Evaluating STEM Reasoning Capabilities of VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ai Jian, Weijie Qiu, Xiaokun Wang, Peiyu Wang, Yunzhuo Hao, Jiangbo Pei, Yichen Wei, Yi Peng, Xuchen Song

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-06-17)

**备注**: 36 pages

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/Skywork)

---

## 💡 一句话要点

**提出CSVQA以评估视觉语言模型的科学推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `科学推理` `多模态基准` `领域知识` `视觉问答` `STEM教育` `推理能力`

## 📋 核心要点

1. 现有多模态基准主要集中于通用图像理解和文本推理，缺乏科学领域的真实背景评估。
2. 本文提出CSVQA基准，专注于通过领域基础的视觉问答评估科学推理能力，包含1,378个问题-答案对。
3. 对15个VLMs的评估结果显示，最高模型仅有49.6%的准确率，表明科学推理能力亟待提升。

## 📝 摘要（中文）

视觉语言模型（VLMs）在多模态理解方面取得了显著进展，但其科学推理能力仍未得到充分评估。现有的多模态基准主要评估通用图像理解或文本驱动的推理，缺乏真实的科学背景，无法有效整合领域特定知识与视觉证据分析。为填补这一空白，本文提出了CSVQA，一个专门设计用于通过领域基础的视觉问答评估科学推理的诊断性多模态基准。该基准包含1,378对精心构建的问题-答案对，涵盖多个STEM学科，要求领域知识、视觉证据整合和高阶推理。与以往的多模态基准相比，CSVQA更强调真实的科学内容和复杂推理。我们还提出了严格的评估协议，以系统性地评估模型预测是否基于有效的中间推理步骤。对15个VLMs的综合评估显示出显著的性能差异，即使是排名最高的专有模型也仅达到49.6%的准确率。这一实证结果强调了提升VLMs科学推理能力的迫切需求。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态基准在科学推理评估中的不足，尤其是缺乏真实科学背景和领域知识的整合。

**核心思路**：CSVQA基准通过构建领域基础的视觉问答任务，要求模型在回答问题时整合视觉证据与领域知识，从而更好地评估其科学推理能力。

**技术框架**：该基准包含1,378个问题-答案对，覆盖多个STEM学科。评估流程包括问题生成、答案验证和推理步骤的审查，确保模型的推理过程是合理的。

**关键创新**：CSVQA的主要创新在于其专注于科学推理的多模态评估，强调真实世界的科学内容和复杂推理，与现有基准相比具有显著的区别。

**关键设计**：在设计过程中，问题和答案对的构建遵循严格的领域知识标准，评估协议要求模型提供有效的中间推理步骤，确保预测的合理性和准确性。

## 📊 实验亮点

在对15个视觉语言模型的评估中，最高模型的准确率仅为49.6%，显示出显著的性能差异。这一结果强调了当前模型在科学推理方面的不足，表明需要进一步提升其能力以满足实际应用需求。

## 🎯 应用场景

CSVQA基准的提出为科学推理能力的评估提供了新的工具，具有广泛的应用潜力。它可以用于教育领域，帮助学生和研究人员理解科学推理过程，也可为VLMs的进一步研究和开发提供指导，推动人工智能在科学研究中的应用。未来，该基准可能会影响科学教育和研究方法的发展。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated remarkable progress in multimodal understanding, yet their capabilities for scientific reasoning remain inadequately assessed. Current multimodal benchmarks predominantly evaluate generic image comprehension or text-driven reasoning, lacking authentic scientific contexts that require domain-specific knowledge integration with visual evidence analysis. To fill this gap, we present CSVQA, a diagnostic multimodal benchmark specifically designed for evaluating scientific reasoning through domain-grounded visual question answering. Our benchmark features 1,378 carefully constructed question-answer pairs spanning diverse STEM disciplines, each demanding domain knowledge, integration of visual evidence, and higher-order reasoning. Compared to prior multimodal benchmarks, CSVQA places greater emphasis on real-world scientific content and complex reasoning. We additionally propose a rigorous evaluation protocol to systematically assess whether model predictions are substantiated by valid intermediate reasoning steps based on curated explanations. Our comprehensive evaluation of 15 VLMs on this benchmark reveals notable performance disparities, as even the top-ranked proprietary model attains only 49.6% accuracy. This empirical evidence underscores the pressing need for advancing scientific reasoning capabilities in VLMs. Our CSVQA is released at https://huggingface.co/datasets/Skywork/CSVQA


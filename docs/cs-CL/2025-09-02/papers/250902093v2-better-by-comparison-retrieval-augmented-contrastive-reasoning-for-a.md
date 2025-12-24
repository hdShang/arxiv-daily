---
layout: default
title: "Better by Comparison: Retrieval-Augmented Contrastive Reasoning for Automatic Prompt Optimization"
---

# Better by Comparison: Retrieval-Augmented Contrastive Reasoning for Automatic Prompt Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02093" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02093v2</a>
  <a href="https://arxiv.org/pdf/2509.02093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02093v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02093v2', 'Better by Comparison: Retrieval-Augmented Contrastive Reasoning for Automatic Prompt Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juhyeon Lee, Wonduk Seo, Hyunjin An, Seunghyun Lee, Yi Bu

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-09-02 (更新: 2025-10-03)

**备注**: Preprint

---

## 💡 一句话要点

**提出对比推理提示优化（CRPO），通过检索增强对比学习提升LLM提示质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `提示优化` `对比学习` `检索增强` `大型语言模型` `自动提示工程`

## 📋 核心要点

1. 现有自动提示优化方法侧重于直接改进或微调，忽略了LLM从对比示例中学习推理的能力。
2. CRPO框架将提示优化视为检索增强的推理过程，通过对比不同质量的提示-响应对进行学习。
3. 实验表明，CRPO在HelpSteer2基准测试中显著优于现有方法，提升了提示优化的效果。

## 📝 摘要（中文）

自动提示优化已成为提升大型语言模型（LLM）提示质量的有效策略，旨在生成更准确和有用的响应。然而，现有工作主要集中于直接提示改进或模型微调，忽略了利用LLM内在推理能力从对比示例中学习的潜力。本文提出了对比推理提示优化（CRPO），这是一个将提示优化形式化为检索增强推理过程的新框架。该方法从HelpSteer2数据集中检索前k个参考提示-响应对，该数据集是一个开源集合，其中每个响应都标注了helpfulness、correctness、coherence、complexity和verbosity。CRPO构建了两种互补的优化范式：（1）分层对比推理，LLM比较高质量、中等质量和低质量的示例（包括提示和响应），通过反思性推理来改进其自身的生成；（2）多指标对比推理，LLM分析每个评估维度上的最佳示例，并将它们的优势整合到优化的提示中。通过显式对比高质量和低质量的示例，CRPO使模型能够推断出为什么某些提示成功而另一些提示失败，从而实现更鲁棒和可解释的优化。在HelpSteer2基准上的实验结果表明，CRPO显著优于基线方法。研究结果突出了对比的、检索增强的推理在推进自动提示优化方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决如何更有效地进行自动提示优化的问题。现有方法主要依赖于直接的提示修改或模型微调，缺乏利用LLM自身推理能力从对比示例中学习的机制。这些方法难以解释优化过程，且可能不够鲁棒。

**核心思路**：论文的核心思路是利用LLM的对比推理能力，通过检索并对比高质量和低质量的提示-响应对，让LLM学习到成功提示的要素和失败提示的不足。这种对比学习的方式能够帮助LLM更好地理解提示的有效性，从而生成更优的提示。

**技术框架**：CRPO框架主要包含两个阶段：检索阶段和对比推理阶段。在检索阶段，从HelpSteer2数据集中检索与当前任务相关的top-k个提示-响应对。在对比推理阶段，CRPO构建了两种对比推理范式：分层对比推理和多指标对比推理。分层对比推理比较高质量、中等质量和低质量的示例，而多指标对比推理则分析每个评估维度上的最佳示例。LLM通过对这些示例进行反思性推理，从而优化提示。

**关键创新**：CRPO的关键创新在于将对比学习和检索增强相结合，用于自动提示优化。与现有方法不同，CRPO不是直接修改提示，而是通过对比学习让LLM理解提示的有效性。此外，CRPO还提出了分层对比推理和多指标对比推理两种新的对比推理范式。

**关键设计**：CRPO的关键设计包括：1) 使用HelpSteer2数据集作为检索的知识库；2) 设计了分层对比推理和多指标对比推理两种对比推理范式；3) 使用LLM（具体模型未知）作为推理引擎，通过prompting的方式引导LLM进行对比分析和提示优化。具体的损失函数和网络结构等细节未在论文中详细描述。

## 📊 实验亮点

CRPO在HelpSteer2基准测试中显著优于基线方法，证明了对比推理和检索增强在提示优化中的有效性。具体的性能数据和提升幅度在摘要中提到，但未给出具体数值。实验结果表明，CRPO能够生成更鲁棒和可解释的优化提示。

## 🎯 应用场景

CRPO可应用于各种需要提示工程的LLM应用场景，例如问答系统、文本生成、代码生成等。通过自动优化提示，可以提升LLM的性能和用户体验，降低人工设计提示的成本。该研究对于提升LLM的可用性和可解释性具有重要意义。

## 📄 摘要（原文）

> Automatic prompt optimization has recently emerged as a strategy for improving the quality of prompts used in Large Language Models (LLMs), with the goal of generating more accurate and useful responses. However, most prior work focuses on direct prompt refinement or model fine-tuning, overlooking the potential of leveraging LLMs' inherent reasoning capability to learn from contrasting examples. In this paper, we present Contrastive Reasoning Prompt Optimization (CRPO), a novel framework that formulates prompt optimization as a retrieval-augmented reasoning process. Our approach retrieves top k reference prompt-response pairs from the HelpSteer2 dataset, an open source collection where each response is annotated for helpfulness, correctness, coherence, complexity, and verbosity, and constructs two complementary optimization paradigms: (1) tiered contrastive reasoning, where the LLM compares high-, medium-, and low-quality exemplars (both prompts and responses) to refine its own generation through reflective reasoning, and (2) multi-metric contrastive reasoning, where the LLM analyzes the best exemplars along each evaluation dimension and integrates their strengths into an optimized prompt. By explicitly contrasting high and low quality exemplars, CRPO enables the model to deduce why certain prompts succeed while others fail, thereby achieving more robust and interpretable optimization. Experimental results on the HelpSteer2 benchmark demonstrate that CRPO significantly outperforms baselines. Our findings highlight the promise of contrastive, retrieval-augmented reasoning for advancing automatic prompt optimization.


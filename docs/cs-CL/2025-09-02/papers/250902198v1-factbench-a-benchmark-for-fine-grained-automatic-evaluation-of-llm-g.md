---
layout: default
title: "FActBench: A Benchmark for Fine-grained Automatic Evaluation of LLM-Generated Text in the Medical Domain"
---

# FActBench: A Benchmark for Fine-grained Automatic Evaluation of LLM-Generated Text in the Medical Domain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02198" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02198v1</a>
  <a href="https://arxiv.org/pdf/2509.02198.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02198v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02198v1', 'FActBench: A Benchmark for Fine-grained Automatic Evaluation of LLM-Generated Text in the Medical Domain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anum Afzal, Juraj Vladika, Florian Matthes

**分类**: cs.CL

**发布日期**: 2025-09-02

---

## 💡 一句话要点

**构建医学领域LLM生成文本自动评估基准FActBench，提升事实性评估准确度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `事实核查` `医学领域` `自然语言推理` `思维链` `自动评估` `基准测试`

## 📋 核心要点

1. 大型语言模型在医学等专业领域面临事实性挑战，现有评估方法不够精细。
2. 构建FActBench基准，结合CoT提示和NLI技术，实现更准确的事实核查。
3. 实验表明，CoT和NLI一致投票的事实核查分数与领域专家评估结果高度相关。

## 📝 摘要（中文）

大型语言模型(LLMs)在处理专业领域知识时表现不佳，其中事实性是最关键的评估指标。同时，可靠的事实核查工具和数据源对于缓解幻觉至关重要。本文提出了一个全面的事实核查基准FActBench，涵盖医学领域的四个生成任务和六个最先进的LLMs。使用了两种最先进的事实核查技术：思维链(CoT)提示和自然语言推理(NLI)。实验表明，通过这两种技术的一致投票获得的事实核查分数与领域专家评估的相关性最佳。

## 🔬 方法详解

**问题定义**：大型语言模型在医学等专业领域生成文本时，容易出现事实性错误（hallucination），现有的评估方法不够精细，难以准确衡量模型生成内容的真实性和可靠性。缺乏高质量的医学领域事实核查基准，阻碍了相关技术的发展。

**核心思路**：论文的核心思路是构建一个专门针对医学领域的、细粒度的、自动化的事实核查基准FActBench。通过结合多种事实核查技术，并与领域专家评估进行对比，从而更准确地评估LLM生成文本的事实性。

**技术框架**：FActBench基准包含四个医学领域的文本生成任务，并评估了六个最先进的LLMs。该基准使用两种事实核查技术：1) Chain-of-Thought (CoT) Prompting：通过引导模型逐步推理，提高事实核查的准确性。2) Natural Language Inference (NLI)：使用NLI模型判断生成文本与已知事实之间的关系（支持、矛盾、中立）。最终，采用Unanimous Voting策略，即只有当CoT和NLI都认为生成文本是正确的，才将其判定为事实正确的。

**关键创新**：该论文的关键创新在于构建了一个专门针对医学领域的细粒度事实核查基准FActBench。与通用的事实核查基准相比，FActBench更关注医学领域的专业知识和术语，能够更准确地评估LLM在医学领域的表现。此外，结合CoT和NLI两种技术，并采用Unanimous Voting策略，提高了事实核查的可靠性。

**关键设计**：在CoT Prompting中，设计了合适的prompt模板，引导模型进行逐步推理。在NLI中，选择了合适的预训练NLI模型，并针对医学领域进行了微调。Unanimous Voting策略要求CoT和NLI的结果一致，从而降低了误判的概率。具体参数设置和模型选择在论文中有详细描述。

## 📊 实验亮点

实验结果表明，FActBench基准能够有效评估LLM在医学领域的事实性。通过CoT和NLI一致投票获得的事实核查分数与领域专家评估的相关性最高，表明该方法能够更准确地反映LLM的真实表现。该基准为医学领域LLM的开发和评估提供了重要的工具。

## 🎯 应用场景

该研究成果可应用于医学领域的智能问答、电子病历生成、医学知识库构建等场景。通过提高LLM生成文本的事实性，可以提升医疗服务的质量和效率，辅助医生进行诊断和治疗，并为患者提供更可靠的医疗信息。未来，该基准可以扩展到其他专业领域，促进LLM在各行业的应用。

## 📄 摘要（原文）

> Large Language Models tend to struggle when dealing with specialized domains. While all aspects of evaluation hold importance, factuality is the most critical one. Similarly, reliable fact-checking tools and data sources are essential for hallucination mitigation. We address these issues by providing a comprehensive Fact-checking Benchmark FActBench covering four generation tasks and six state-of-the-art Large Language Models (LLMs) for the Medical domain. We use two state-of-the-art Fact-checking techniques: Chain-of-Thought (CoT) Prompting and Natural Language Inference (NLI). Our experiments show that the fact-checking scores acquired through the Unanimous Voting of both techniques correlate best with Domain Expert Evaluation.


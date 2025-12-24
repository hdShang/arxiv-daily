---
layout: default
title: "From Retrieval to Reasoning: A Framework for Cyber Threat Intelligence NER with Explicit and Adaptive Instructions"
---

# From Retrieval to Reasoning: A Framework for Cyber Threat Intelligence NER with Explicit and Adaptive Instructions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19414" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19414v1</a>
  <a href="https://arxiv.org/pdf/2512.19414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19414v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19414v1', 'From Retrieval to Reasoning: A Framework for Cyber Threat Intelligence NER with Explicit and Adaptive Instructions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaren Peng, Hongda Sun, Xuan Tian, Cheng Huang, Zeqing Li, Rui Yan

**分类**: cs.CR, cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**提出TTPrompt框架，通过显式指令提升网络威胁情报命名实体识别性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `网络威胁情报` `命名实体识别` `大型语言模型` `上下文学习` `指令学习`

## 📋 核心要点

1. 现有基于检索的上下文学习方法在CTI NER任务中依赖实体类型重叠，缺乏可靠的语义泛化能力。
2. TTPrompt框架通过将CTI知识显式编码为分层指令，指导LLM进行更精确的实体识别。
3. 反馈驱动的指令细化(FIR)使模型能从少量数据中学习并适应不同的标注风格，提升泛化性。

## 📝 摘要（中文）

网络威胁情报(CTI)的自动化严重依赖于命名实体识别(NER)从非结构化文本中提取关键实体。目前，大型语言模型(LLM)主要通过基于检索的上下文学习(ICL)来解决此任务。本文分析了这种主流范式，揭示了一个根本缺陷：其成功并非源于全局语义相似性，而主要源于检索到的示例中实体类型的偶然重叠。这暴露了依赖不可靠的隐式归纳的局限性。为了解决这个问题，我们提出了TTPrompt，一个从隐式归纳转向显式指令的框架。TTPrompt将CTI的战术、技术和程序(TTP)的核心概念映射到一个指令层次结构：将任务定义制定为战术，将指导策略制定为技术，并将注释指南制定为程序。此外，为了处理静态指南的适应性挑战，我们引入了反馈驱动的指令细化(FIR)。FIR使LLM能够通过从少量标记数据上的错误中学习来自动细化指南，从而适应不同的注释方言。在五个CTI NER基准上的实验表明，TTPrompt始终优于基于检索的基线。值得注意的是，仅使用1%的训练数据进行细化，它就能与在完整数据集上微调的模型相媲美。例如，在LADDER上，其71.96%的Micro F1接近微调基线，而在复杂的CTINexus上，其Macro F1超过了微调的ACLM模型10.91%。

## 🔬 方法详解

**问题定义**：论文旨在解决网络威胁情报(CTI)领域中命名实体识别(NER)任务的自动化问题。现有方法，特别是基于检索的上下文学习(ICL)，在CTI NER任务中表现出对检索示例中实体类型重叠的过度依赖，而非真正的语义理解。这种依赖导致模型在面对新的、未见过的实体类型或标注风格时泛化能力不足。

**核心思路**：论文的核心思路是将CTI领域的知识显式地编码到LLM的指令中，从而引导模型进行更准确和可靠的实体识别。通过将CTI的战术、技术和程序(TTP)概念映射到指令层次结构，模型能够更好地理解任务目标和约束，从而减少对隐式归纳的依赖。

**技术框架**：TTPrompt框架包含两个主要组成部分：指令层次结构和反馈驱动的指令细化(FIR)。指令层次结构将CTI知识组织为三个层次：战术(Tactics)定义任务目标，技术(Techniques)提供指导策略，程序(Procedures)提供注释指南。FIR模块允许LLM通过分析预测错误并从少量标记数据中学习，从而自动细化指令，适应不同的标注风格。整体流程包括：1)构建初始指令集；2)使用指令集指导LLM进行NER；3)分析预测结果并识别错误；4)使用FIR模块细化指令；5)重复步骤2-4，直到性能收敛。

**关键创新**：最重要的技术创新点在于将隐式归纳转变为显式指令。与依赖检索到的示例进行隐式学习的方法不同，TTPrompt通过明确的指令来指导模型，从而提高了模型的可解释性和泛化能力。此外，FIR模块的引入使得模型能够自适应地学习和调整指令，从而更好地适应不同的数据分布和标注风格。

**关键设计**：指令层次结构的设计是关键。战术层定义了NER任务的总体目标，例如识别特定类型的威胁行为者。技术层提供了指导策略，例如使用特定的命名约定或上下文信息。程序层提供了详细的注释指南，例如如何处理嵌套实体或不明确的边界。FIR模块使用一个小的验证集来评估模型的性能，并使用错误分析来识别需要改进的指令。细化过程可以使用不同的技术，例如基于规则的修改或基于LLM的生成。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19414v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19414v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19414v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，TTPrompt在五个CTI NER基准测试中始终优于基于检索的基线方法。特别是在LADDER数据集上，TTPrompt的Micro F1值达到71.96%，接近于在完整数据集上微调的模型。在更复杂的CTINexus数据集上，TTPrompt的Macro F1值超过了微调的ACLM模型10.91%。更重要的是，TTPrompt仅使用1%的训练数据进行细化，就能达到与全量数据微调模型相近的性能，显著降低了标注成本。

## 🎯 应用场景

该研究成果可应用于自动化网络威胁情报分析，提升威胁检测和响应效率。通过更准确地识别和提取威胁情报中的关键实体，可以帮助安全分析师更快地理解威胁态势，制定有效的防御策略，并减少人工分析的工作量。未来，该方法可以扩展到其他安全领域的文本分析任务，例如漏洞报告分析和恶意软件分析。

## 📄 摘要（原文）

> The automation of Cyber Threat Intelligence (CTI) relies heavily on Named Entity Recognition (NER) to extract critical entities from unstructured text. Currently, Large Language Models (LLMs) primarily address this task through retrieval-based In-Context Learning (ICL). This paper analyzes this mainstream paradigm, revealing a fundamental flaw: its success stems not from global semantic similarity but largely from the incidental overlap of entity types within retrieved examples. This exposes the limitations of relying on unreliable implicit induction. To address this, we propose TTPrompt, a framework shifting from implicit induction to explicit instruction. TTPrompt maps the core concepts of CTI's Tactics, Techniques, and Procedures (TTPs) into an instruction hierarchy: formulating task definitions as Tactics, guiding strategies as Techniques, and annotation guidelines as Procedures. Furthermore, to handle the adaptability challenge of static guidelines, we introduce Feedback-driven Instruction Refinement (FIR). FIR enables LLMs to self-refine guidelines by learning from errors on minimal labeled data, adapting to distinct annotation dialects. Experiments on five CTI NER benchmarks demonstrate that TTPrompt consistently surpasses retrieval-based baselines. Notably, with refinement on just 1% of training data, it rivals models fine-tuned on the full dataset. For instance, on LADDER, its Micro F1 of 71.96% approaches the fine-tuned baseline, and on the complex CTINexus, its Macro F1 exceeds the fine-tuned ACLM model by 10.91%.


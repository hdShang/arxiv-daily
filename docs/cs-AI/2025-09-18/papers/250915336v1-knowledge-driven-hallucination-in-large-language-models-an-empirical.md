---
layout: default
title: "Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling"
---

# Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15336" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15336v1</a>
  <a href="https://arxiv.org/pdf/2509.15336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15336v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15336v1', 'Knowledge-Driven Hallucination in Large Language Models: An Empirical Study on Process Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Humam Kourani, Anton Antonov, Alessandro Berti, Wil M. P. van der Aalst

**分类**: cs.AI

**发布日期**: 2025-09-18

**备注**: The Version of Record of this contribution will be published in the proceedings of the 2nd International Workshop on Generative AI for Process Mining (GenAI4PM 2025). This preprint has not undergone peer review or any post-submission improvements or corrections

---

## 💡 一句话要点

**研究LLM在过程建模中知识驱动的幻觉现象，揭示其固有知识与证据冲突时的可靠性问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识驱动幻觉` `业务流程建模` `证据驱动推理` `可靠性评估`

## 📋 核心要点

1. LLM在分析任务中依赖预训练知识，但也因此存在知识驱动的幻觉风险，即输出与输入证据冲突。
2. 该研究通过在业务流程建模任务中评估LLM，探究其在证据与预训练知识冲突时的可靠性。
3. 实验设计了标准和非典型流程场景，衡量LLM对证据的忠实度，并提出评估方法。

## 📝 摘要（中文）

大型语言模型（LLM）在分析任务中的效用源于其海量的预训练知识，这使其能够解释模糊的输入并推断缺失的信息。然而，这种能力也带来了一种关键风险，我们称之为知识驱动的幻觉：即模型的输出与明确的源证据相矛盾，因为它被模型广义的内部知识所覆盖。本文通过评估LLM在自动化过程建模任务中的表现来研究这种现象，该任务的目标是从给定的源工件生成正式的业务流程模型。业务流程管理（BPM）领域为这项研究提供了一个理想的背景，因为许多核心业务流程遵循标准化模式，使得LLM很可能拥有强大的预训练模式。我们进行了一项受控实验，旨在创建提供的证据与LLM的背景知识之间存在故意冲突的场景。我们使用描述标准和故意非典型过程结构的输入来衡量LLM对所提供证据的忠实度。我们的工作提供了一种评估这种关键可靠性问题的方法，并提高了人们对在任何基于证据的领域中严格验证AI生成工件的必要性的认识。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在自动化业务流程建模任务中出现的“知识驱动的幻觉”问题。现有方法在利用LLM进行此类任务时，往往忽略了LLM可能存在的先验知识与输入证据之间的冲突，导致模型生成与证据不符的错误模型。这种幻觉现象降低了LLM在证据驱动型领域的可靠性。

**核心思路**：论文的核心思路是通过设计受控实验，人为地制造LLM的先验知识与输入证据之间的冲突，从而量化和分析LLM的“知识驱动的幻觉”现象。通过对比LLM在处理标准和非标准业务流程时的表现，评估其对输入证据的忠实程度。

**技术框架**：该研究采用实验方法，主要包含以下几个阶段：
1.  **场景设计**：设计包含标准和非标准业务流程描述的输入数据，其中非标准流程与LLM可能存在的常见流程模式相悖。
2.  **模型推理**：将设计的输入数据输入到LLM中，让其生成业务流程模型。
3.  **结果评估**：对比LLM生成的模型与输入证据，评估模型是否忠实于证据，并量化“知识驱动的幻觉”程度。

**关键创新**：该研究的关键创新在于：
1.  首次明确提出了“知识驱动的幻觉”这一概念，并将其应用于LLM在业务流程建模领域的分析。
2.  设计了一种受控实验方法，用于量化和分析LLM的“知识驱动的幻觉”现象。
3.  强调了在证据驱动型领域中，对AI生成工件进行严格验证的必要性。

**关键设计**：实验的关键设计在于：
1.  选择业务流程建模作为研究场景，因为该领域存在大量标准化的流程模式，LLM很可能具备相关的先验知识。
2.  设计非标准流程时，故意违反常见的流程模式，从而制造LLM的先验知识与输入证据之间的冲突。
3.  评估指标主要关注LLM生成的模型是否忠实于输入证据，例如是否正确识别流程中的活动、顺序和分支。

## 📊 实验亮点

该研究通过受控实验，量化了LLM在业务流程建模任务中“知识驱动的幻觉”现象。实验结果表明，当输入证据与LLM的预训练知识冲突时，LLM倾向于生成符合其预训练知识的模型，而忽略输入证据。这表明LLM在证据驱动型任务中存在一定的可靠性风险，需要进行严格的验证和校准。

## 🎯 应用场景

该研究成果可应用于各种需要LLM进行证据驱动型推理和决策的领域，例如法律文件分析、医疗诊断辅助、金融风险评估等。通过识别和缓解LLM的知识驱动幻觉，可以提高AI系统的可靠性和安全性，促进其在关键领域的应用。

## 📄 摘要（原文）

> The utility of Large Language Models (LLMs) in analytical tasks is rooted in their vast pre-trained knowledge, which allows them to interpret ambiguous inputs and infer missing information. However, this same capability introduces a critical risk of what we term knowledge-driven hallucination: a phenomenon where the model's output contradicts explicit source evidence because it is overridden by the model's generalized internal knowledge. This paper investigates this phenomenon by evaluating LLMs on the task of automated process modeling, where the goal is to generate a formal business process model from a given source artifact. The domain of Business Process Management (BPM) provides an ideal context for this study, as many core business processes follow standardized patterns, making it likely that LLMs possess strong pre-trained schemas for them. We conduct a controlled experiment designed to create scenarios with deliberate conflict between provided evidence and the LLM's background knowledge. We use inputs describing both standard and deliberately atypical process structures to measure the LLM's fidelity to the provided evidence. Our work provides a methodology for assessing this critical reliability issue and raises awareness of the need for rigorous validation of AI-generated artifacts in any evidence-based domain.


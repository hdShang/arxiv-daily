---
layout: default
title: "PerHalluEval: Persian Hallucination Evaluation Benchmark for Large Language Models"
---

# PerHalluEval: Persian Hallucination Evaluation Benchmark for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21104" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21104v1</a>
  <a href="https://arxiv.org/pdf/2509.21104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21104v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21104v1', 'PerHalluEval: Persian Hallucination Evaluation Benchmark for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Hosseini, Kimia Hosseini, Shayan Bali, Zahra Zanjani, Saeedeh Momtazi

**分类**: cs.CL

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**提出PerHalluEval，首个波斯语LLM幻觉评估基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `波斯语` `大型语言模型` `幻觉评估` `低资源语言` `自然语言处理`

## 📋 核心要点

1. 现有LLM在波斯语等低资源语言中存在严重的幻觉问题，缺乏有效的评估基准。
2. 构建一个三阶段LLM驱动的评估流程，结合人工验证和token概率选择，检测幻觉实例。
3. 评估结果表明，现有LLM在检测波斯语幻觉文本方面表现不佳，提供外部知识可部分缓解幻觉。

## 📝 摘要（中文）

幻觉是所有大型语言模型（LLM）都面临的一个持续性问题，尤其是在波斯语等低资源语言中。PerHalluEval（波斯语幻觉评估）是首个为波斯语量身定制的动态幻觉评估基准。该基准利用一个三阶段的LLM驱动流程，并结合人工验证，生成关于问答和摘要任务的合理答案和摘要，重点在于检测外在和内在幻觉。此外，我们使用生成token的对数概率来选择最可信的幻觉实例。另外，我们还邀请人工标注员突出问答数据集中特定于波斯语的上下文，以评估LLM在与波斯文化相关的内容上的表现。我们使用PerHalluEval评估了12个LLM，包括开源和闭源模型，结果表明这些模型在检测波斯语幻觉文本方面普遍存在困难。我们表明，提供外部知识（即摘要任务的原始文档）可以在一定程度上缓解幻觉。此外，在幻觉方面，专门为波斯语训练的LLM与其他LLM相比没有显著差异。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在波斯语中产生幻觉的问题，并缺乏针对波斯语的幻觉评估基准。现有方法无法有效评估LLM在波斯语环境下的幻觉生成情况，尤其是在处理特定于波斯文化的知识时。

**核心思路**：论文的核心思路是构建一个动态的、基于LLM驱动的评估流程，该流程能够自动生成合理的答案和摘要，并结合人工验证来检测幻觉。通过使用token的对数概率来选择更可信的幻觉实例，从而提高评估的准确性。

**技术框架**：PerHalluEval基准的整体框架包含三个主要阶段：1) 使用LLM生成问答和摘要数据，包括真实数据和幻觉数据；2) 使用token的对数概率对生成的幻觉数据进行筛选，选择置信度较高的幻觉实例；3) 邀请人工标注员对数据进行验证，并突出显示特定于波斯文化的上下文。

**关键创新**：该论文的关键创新在于构建了首个针对波斯语的幻觉评估基准，并提出了一种结合LLM生成和人工验证的动态评估流程。此外，论文还关注了特定于波斯文化的知识，并评估了LLM在处理这些知识时的幻觉情况。

**关键设计**：在数据生成阶段，使用了多种LLM来生成问答和摘要数据，以保证数据的多样性。在幻觉检测阶段，使用了token的对数概率作为筛选幻觉实例的指标。在人工验证阶段，邀请了多位标注员进行标注，并对标注结果进行一致性分析。

## 📊 实验亮点

PerHalluEval评估了12个LLM，结果表明这些模型在检测波斯语幻觉文本方面普遍存在困难。提供外部知识可以在一定程度上缓解摘要任务中的幻觉。专门为波斯语训练的LLM与其他LLM相比，在幻觉方面没有显著差异。

## 🎯 应用场景

该研究成果可应用于提升波斯语LLM的可靠性和可信度，尤其是在需要准确信息的场景中，如智能客服、信息检索和机器翻译。该基准的构建方法也可推广到其他低资源语言的幻觉评估中，促进多语言LLM的发展。

## 📄 摘要（原文）

> Hallucination is a persistent issue affecting all large language Models (LLMs), particularly within low-resource languages such as Persian. PerHalluEval (Persian Hallucination Evaluation) is the first dynamic hallucination evaluation benchmark tailored for the Persian language. Our benchmark leverages a three-stage LLM-driven pipeline, augmented with human validation, to generate plausible answers and summaries regarding QA and summarization tasks, focusing on detecting extrinsic and intrinsic hallucinations. Moreover, we used the log probabilities of generated tokens to select the most believable hallucinated instances. In addition, we engaged human annotators to highlight Persian-specific contexts in the QA dataset in order to evaluate LLMs' performance on content specifically related to Persian culture. Our evaluation of 12 LLMs, including open- and closed-source models using PerHalluEval, revealed that the models generally struggle in detecting hallucinated Persian text. We showed that providing external knowledge, i.e., the original document for the summarization task, could mitigate hallucination partially. Furthermore, there was no significant difference in terms of hallucination when comparing LLMs specifically trained for Persian with others.


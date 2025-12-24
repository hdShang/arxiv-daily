---
layout: default
title: "SciVer: Evaluating Foundation Models for Multimodal Scientific Claim Verification"
---

# SciVer: Evaluating Foundation Models for Multimodal Scientific Claim Verification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15569" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15569v1</a>
  <a href="https://arxiv.org/pdf/2506.15569.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15569v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15569v1', 'SciVer: Evaluating Foundation Models for Multimodal Scientific Claim Verification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengye Wang, Yifei Shen, Zexi Kuang, Arman Cohan, Yilun Zhao

**分类**: cs.CL

**发布日期**: 2025-06-18

---

## 💡 一句话要点

**提出SciVer以评估多模态科学声明验证中的基础模型能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `科学声明验证` `基础模型` `评估基准` `机器学习`

## 📋 核心要点

1. 现有方法在多模态科学声明验证中缺乏有效的评估基准，导致模型性能难以量化和比较。
2. 论文提出SciVer基准，通过3000个专家注释的示例，系统性评估基础模型在科学声明验证中的能力。
3. 实验表明，21个多模态基础模型的表现与人类专家相比存在显著差距，揭示了当前模型的局限性。

## 📝 摘要（中文）

我们介绍了SciVer，这是第一个专门设计用于评估基础模型在多模态科学背景下验证声明能力的基准。SciVer包含3000个专家注释的示例，涵盖1113篇科学论文，分为四个子集，代表多模态科学声明验证中的常见推理类型。为了实现细粒度评估，每个示例都包括专家注释的支持证据。我们评估了21个最先进的多模态基础模型的性能，包括o4-mini、Gemini-2.5-Flash、Llama-3.2-Vision和Qwen2.5-VL。实验结果显示，这些模型与人类专家在SciVer上的表现存在显著差距。通过对检索增强生成（RAG）和人类错误评估的深入分析，我们识别了当前开源模型的关键局限性，为提升模型在多模态科学文献任务中的理解和推理能力提供了重要见解。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何有效评估基础模型在多模态科学声明验证中的能力。现有方法缺乏系统性评估，导致模型性能难以量化和比较。

**核心思路**：论文的核心解决思路是构建SciVer基准，提供3000个专家注释的示例，涵盖多种推理类型，以便对模型进行细粒度评估。

**技术框架**：整体架构包括数据收集、专家注释、模型评估和结果分析四个主要模块。数据收集阶段从1113篇科学论文中提取信息，专家注释阶段确保数据的准确性，模型评估阶段使用21个基础模型进行性能测试，结果分析阶段则深入探讨模型的局限性。

**关键创新**：最重要的技术创新点在于创建了一个专门针对多模态科学声明验证的评估基准，填补了现有研究的空白，使得模型性能的比较更加科学和系统。

**关键设计**：在设计中，采用了专家注释的支持证据作为评估标准，确保了数据的高质量。此外，模型评估中使用了多种最先进的多模态基础模型，确保了结果的代表性和可靠性。

## 📊 实验亮点

实验结果显示，21个多模态基础模型在SciVer基准上的表现与人类专家相比存在显著差距，具体而言，模型的准确率普遍低于人类专家，揭示了当前模型在理解和推理方面的关键局限性。这一发现为未来模型的改进提供了重要方向。

## 🎯 应用场景

该研究的潜在应用领域包括科学研究、学术出版和教育等。通过提升基础模型在科学声明验证中的能力，SciVer可以帮助研究人员更有效地验证科学信息的准确性，促进科学知识的传播与应用，未来可能对科学研究的透明度和可信度产生深远影响。

## 📄 摘要（原文）

> We introduce SciVer, the first benchmark specifically designed to evaluate the ability of foundation models to verify claims within a multimodal scientific context. SciVer consists of 3,000 expert-annotated examples over 1,113 scientific papers, covering four subsets, each representing a common reasoning type in multimodal scientific claim verification. To enable fine-grained evaluation, each example includes expert-annotated supporting evidence. We assess the performance of 21 state-of-the-art multimodal foundation models, including o4-mini, Gemini-2.5-Flash, Llama-3.2-Vision, and Qwen2.5-VL. Our experiment reveals a substantial performance gap between these models and human experts on SciVer. Through an in-depth analysis of retrieval-augmented generation (RAG), and human-conducted error evaluations, we identify critical limitations in current open-source models, offering key insights to advance models' comprehension and reasoning in multimodal scientific literature tasks.


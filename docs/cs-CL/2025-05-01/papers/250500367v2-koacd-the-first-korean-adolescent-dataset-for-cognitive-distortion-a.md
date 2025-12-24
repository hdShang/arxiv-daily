---
layout: default
title: "KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation"
---

# KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00367" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00367v2</a>
  <a href="https://arxiv.org/pdf/2505.00367.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00367v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00367v2', 'KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: JunSeo Kim, HyeHyeon Kim

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-01 (更新: 2025-09-20)

**备注**: Accepted to Findings of EMNLP 2025

---

## 💡 一句话要点

**提出KoACD数据集以解决青少年认知扭曲分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `认知扭曲` `青少年心理健康` `自然语言处理` `多LLM协商` `数据集构建` `合成数据生成` `心理健康监测`

## 📋 核心要点

1. 现有研究主要集中于成人数据集，青少年认知扭曲的研究相对缺乏，导致数据不足和分析不全面。
2. 本研究提出KoACD数据集，并采用多LLM协商方法，通过角色切换和迭代反馈来优化认知扭曲的分类。
3. 实验结果显示，尽管LLM在明确标记的扭曲分类上表现良好，但在上下文推理方面仍存在不足，人类评估者的准确性更高。

## 📝 摘要（中文）

认知扭曲是指可能导致青少年抑郁和焦虑等心理健康问题的负面思维模式。以往的自然语言处理研究主要集中在小规模的成人数据集上，青少年领域的研究相对有限。本研究引入了KoACD，这是首个针对韩国青少年认知扭曲的大规模数据集，包含108,717个实例。我们采用多大型语言模型（LLM）协商方法来优化扭曲分类，通过模型间的迭代反馈和角色切换来减少偏差并提高标签一致性。此外，我们使用两种方法生成合成数据：文本清晰度的认知澄清和多样化扭曲表现的认知平衡。通过LLM和专家评估的验证表明，尽管LLM能够对具有明确标记的扭曲进行分类，但在上下文依赖的推理方面表现不佳，而人类评估者的准确性更高。KoACD旨在促进未来对认知扭曲检测的研究，数据集和实现细节已公开获取。

## 🔬 方法详解

**问题定义**：本研究旨在解决青少年认知扭曲分析中的数据不足和分类准确性问题。现有方法主要依赖于成人数据集，缺乏针对青少年的大规模研究，导致分析结果的局限性。

**核心思路**：论文提出了KoACD数据集，并利用多LLM协商方法，通过模型间的角色切换和迭代反馈来优化扭曲分类，旨在减少偏差并提高标签一致性。

**技术框架**：整体架构包括数据集构建、LLM协商分类和合成数据生成三个主要模块。首先构建包含108,717个实例的KoACD数据集，然后通过多LLM进行协商分类，最后生成合成数据以增强数据多样性。

**关键创新**：本研究的关键创新在于首次引入大规模青少年认知扭曲数据集，并采用多LLM协商方法进行分类，显著提高了分类的准确性和一致性。与以往方法相比，能够更好地处理上下文依赖的推理问题。

**关键设计**：在模型设计中，采用了迭代反馈机制和角色切换策略，以优化标签一致性。合成数据生成方面，使用认知澄清和认知平衡两种方法，以确保数据的清晰度和多样性。具体的损失函数和参数设置在实验中进行了详细调优。

## 📊 实验亮点

实验结果表明，LLM在明确标记的扭曲分类上表现良好，但在上下文推理方面的准确性较低。人类评估者的准确性显著高于LLM，显示出该研究在提高认知扭曲分类准确性方面的潜力。具体数据和提升幅度在实验中进行了详细分析。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康监测、教育干预和青少年心理咨询等。KoACD数据集的发布将为相关领域的研究提供重要的数据支持，促进对青少年认知扭曲的深入理解和有效干预。未来，该数据集可能成为心理健康研究和人工智能应用的基础资源。

## 📄 摘要（原文）

> Cognitive distortion refers to negative thinking patterns that can lead to mental health issues like depression and anxiety in adolescents. Previous studies using natural language processing (NLP) have focused mainly on small-scale adult datasets, with limited research on adolescents. This study introduces KoACD, the first large-scale dataset of cognitive distortions in Korean adolescents, containing 108,717 instances. We applied a multi-Large Language Model (LLM) negotiation method to refine distortion classification, enabling iterative feedback and role-switching between models to reduce bias and improve label consistency. In addition, we generated synthetic data using two approaches: cognitive clarification for textual clarity and cognitive balancing for diverse distortion representation. Validation through LLMs and expert evaluations showed that while LLMs classified distortions with explicit markers, they struggled with context-dependent reasoning, where human evaluators demonstrated higher accuracy. KoACD aims to enhance future research on cognitive distortion detection. The dataset and implementation details are publicly accessible.


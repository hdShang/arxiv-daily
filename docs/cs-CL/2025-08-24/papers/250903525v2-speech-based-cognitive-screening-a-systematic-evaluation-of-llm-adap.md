---
layout: default
title: "Speech-Based Cognitive Screening: A Systematic Evaluation of LLM Adaptation Strategies"
---

# Speech-Based Cognitive Screening: A Systematic Evaluation of LLM Adaptation Strategies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03525" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03525v2</a>
  <a href="https://arxiv.org/pdf/2509.03525.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03525v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03525v2', 'Speech-Based Cognitive Screening: A Systematic Evaluation of LLM Adaptation Strategies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fatemeh Taherinezhad, Mohamad Javad Momeni Nezhad, Sepehr Karimi, Sina Rashidi, Ali Zolnour, Maryam Dadkhah, Yasaman Haghbin, Hossein AzadMaleki, Maryam Zolnoori

**分类**: cs.CL, cs.AI, eess.AS

**发布日期**: 2025-08-24 (更新: 2025-10-07)

---

## 💡 一句话要点

**提出多种模型适应策略以提升认知筛查的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `痴呆症筛查` `大型语言模型` `多模态学习` `上下文学习` `推理增强` `模型适应` `音频-文本融合`

## 📋 核心要点

1. 现有的痴呆症筛查方法存在未诊断率高的问题，尤其是在使用传统检测手段时。
2. 论文提出了多种大型语言模型的适应策略，包括上下文学习、推理增强提示和多模态集成等，以提高检测效果。
3. 实验结果表明，类中心演示和token级微调显著提升了模型性能，尤其是在分类任务中表现突出。

## 📝 摘要（中文）

在美国，超过一半的阿尔茨海默病及相关痴呆症患者未被诊断，基于语音的筛查提供了一种可扩展的检测方法。本文比较了多种大型语言模型（LLM）适应策略在痴呆检测中的效果，使用DementiaBank语音语料库评估了九种文本模型和三种多模态音频-文本模型。研究发现，类中心演示在上下文学习中表现最佳，推理增强对小型模型有改善作用，而基于token的微调通常产生最佳结果。添加分类头显著提升了表现不佳的模型。多模态模型中，微调的音频-文本系统表现良好，但未超越顶级文本模型。这些发现强调了模型适应策略对基于语音的痴呆检测的重要性，适当调整的开放权重模型可以匹敌或超越商业系统。

## 🔬 方法详解

**问题定义**：本文旨在解决当前痴呆症筛查中存在的高未诊断率问题，尤其是传统方法的局限性，如依赖于专业人员进行评估。

**核心思路**：通过比较多种大型语言模型的适应策略，探索如何利用语音数据提高痴呆症的检测准确性，特别是通过上下文学习和推理增强来优化模型性能。

**技术框架**：研究采用DementiaBank语音语料库，评估了九种文本模型和三种多模态音频-文本模型，主要模块包括数据预处理、模型训练、性能评估等。

**关键创新**：最重要的创新在于提出了类中心演示和token级微调策略，这些方法在上下文学习和模型适应方面显著提升了检测效果，与传统方法相比具有更高的灵活性和准确性。

**关键设计**：在模型训练中，采用了不同的演示选择策略和推理设计，参数设置上注重效率，损失函数和网络结构经过优化以适应多模态输入。实验中添加分类头以提升模型表现。

## 📊 实验亮点

实验结果显示，类中心演示在上下文学习中表现最佳，推理增强对小型模型的性能提升显著，而token级微调通常产生最佳得分。添加分类头后，表现不佳的模型得到了显著改善，微调的音频-文本系统虽然表现良好，但未超越顶级文本模型。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、老年护理和智能诊断系统。通过基于语音的痴呆筛查，能够在早期阶段识别出高风险患者，从而为后续的干预和治疗提供支持，具有重要的社会价值和临床意义。

## 📄 摘要（原文）

> Over half of US adults with Alzheimer disease and related dementias remain undiagnosed, and speech-based screening offers a scalable detection approach. We compared large language model adaptation strategies for dementia detection using the DementiaBank speech corpus, evaluating nine text-only models and three multimodal audio-text models on recordings from DementiaBank speech corpus. Adaptations included in-context learning with different demonstration selection policies, reasoning-augmented prompting, parameter-efficient fine-tuning, and multimodal integration. Results showed that class-centroid demonstrations achieved the highest in-context learning performance, reasoning improved smaller models, and token-level fine-tuning generally produced the best scores. Adding a classification head substantially improved underperforming models. Among multimodal models, fine-tuned audio-text systems performed well but did not surpass the top text-only models. These findings highlight that model adaptation strategies, including demonstration selection, reasoning design, and tuning method, critically influence speech-based dementia detection, and that properly adapted open-weight models can match or exceed commercial systems.


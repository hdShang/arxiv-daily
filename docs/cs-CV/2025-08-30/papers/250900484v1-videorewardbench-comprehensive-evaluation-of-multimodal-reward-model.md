---
layout: default
title: "VideoRewardBench: Comprehensive Evaluation of Multimodal Reward Models for Video Understanding"
---

# VideoRewardBench: Comprehensive Evaluation of Multimodal Reward Models for Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00484" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00484v1</a>
  <a href="https://arxiv.org/pdf/2509.00484.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00484v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00484v1', 'VideoRewardBench: Comprehensive Evaluation of Multimodal Reward Models for Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihong Zhang, Xiaojian Huang, Jin Xu, Zhuodong Luo, Xinzhi Wang, Jiansheng Wei, Xuejin Chen

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-30

**备注**: https://videorewardbench.github.io/

---

## 💡 一句话要点

**提出VideoRewardBench以解决视频理解中多模态奖励模型评估不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频理解` `多模态奖励模型` `评估基准` `AI辅助数据管道` `模型性能对比`

## 📋 核心要点

1. 现有的视频领域多模态奖励模型评估基准在问题数量和多样性、评估维度及MRMs类型的评估上存在显著不足。
2. 本文提出VideoRewardBench，涵盖视频理解的感知、知识、推理和安全四个核心方面，提供了更全面的评估框架。
3. 实验结果显示，顶级模型的准确率仍然较低，且不同类型的MRMs在推理时的表现受输入视频帧数影响显著。

## 📝 摘要（中文）

多模态奖励模型（MRMs）在大型视觉语言模型（LVLMs）的训练、推理和评估中起着关键作用，主要通过评估响应质量。然而，现有的视频领域MRMs评估基准存在问题，包括问题数量和多样性不足、评估维度不全面以及对不同类型MRMs评估不充分。为了解决这些问题，本文提出了VideoRewardBench，这是第一个涵盖视频理解四个核心方面的综合基准：感知、知识、推理和安全。通过AI辅助的数据管道，我们整理了一个包含1,563个标注样本的高质量偏好数据集，样本数量是现有基准的15倍。我们对28种MRMs进行了全面评估，结果显示即使是表现最好的模型GPT-4o的总体准确率也仅为57.0%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频领域多模态奖励模型评估基准在问题数量、评估维度及MRMs类型评估上的不足，导致评估结果不够全面和准确。

**核心思路**：通过引入VideoRewardBench，提供一个涵盖视频理解四个核心方面的综合评估框架，以提升对MRMs的评估质量和多样性。

**技术框架**：整体架构包括数据收集、样本标注和模型评估三个主要模块。数据收集通过AI辅助管道进行，样本标注确保数据的高质量，模型评估则涵盖28种MRMs的性能对比。

**关键创新**：VideoRewardBench是第一个全面评估视频理解的多模态奖励模型的基准，显著提升了问题的数量和多样性，提供了更丰富的评估维度。

**关键设计**：数据集中包含1,563个标注样本，样本为视频-文本提示、选择的响应和拒绝的响应的三元组，确保了评估的全面性和准确性。

## 📊 实验亮点

实验结果表明，尽管GPT-4o是表现最好的模型，其总体准确率仅为57.0%，而开源模型Qwen2.5-VL-72B的准确率为53.3%。这些结果揭示了当前MRMs在视频理解任务中的局限性，强调了进一步研究的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括视频内容分析、智能监控、自动视频摘要生成等。通过提供更全面的评估基准，VideoRewardBench将推动多模态奖励模型在视频理解领域的发展，提升相关技术的实际应用价值。

## 📄 摘要（原文）

> Multimodal reward models (MRMs) play a crucial role in the training, inference, and evaluation of Large Vision Language Models (LVLMs) by assessing response quality. However, existing benchmarks for evaluating MRMs in the video domain suffer from a limited number and diversity of questions, a lack of comprehensive evaluation dimensions, and inadequate evaluation of diverse types of MRMs. To address these gaps, we introduce VideoRewardBench, the first comprehensive benchmark covering four core aspects of video understanding: perception, knowledge, reasoning, and safety. Through our AI-assisted data pipeline, we curate a high-quality preference dataset of 1,563 annotated samples, including 1,482 unique videos and 1,559 distinct questions--15 times the number found in the most question-rich prior benchmark. Each sample is a triplet consisting of a video-text prompt, a chosen response, and a rejected response. We also conduct a comprehensive evaluation across 28 multimodal reward models spanning three categories: generative, discriminative, and semi-scalar. Results show that even the top-performing model GPT-4o achieves only 57.0% overall accuracy, and the state-of-the-art open-source model Qwen2.5-VL-72B reaches merely 53.3%. Our analysis further reveals three key insights: (i) MRMs trained with reinforcement learning (RL) do not necessarily exhibit stronger cross-modal generalization than those trained without RL; (ii) except for discriminative MRMs, other types of MRMs across varying model capacities can benefit from inference-time scaling; and (iii) variations in input video frame count have different effects on different types of MRMs. We believe VideoRewardBench offers a challenging and valuable benchmark for advancing the evaluation and development of MRMs in the video domain.


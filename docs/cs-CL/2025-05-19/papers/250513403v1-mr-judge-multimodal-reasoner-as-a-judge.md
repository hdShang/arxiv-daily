---
layout: default
title: "MR. Judge: Multimodal Reasoner as a Judge"
---

# MR. Judge: Multimodal Reasoner as a Judge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13403" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13403v1</a>
  <a href="https://arxiv.org/pdf/2505.13403.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13403v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13403v1', 'MR. Judge: Multimodal Reasoner as a Judge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Renjie Pi, Felix Bai, Qibin Chen, Simon Wang, Jiulong Shan, Kieran Liu, Meng Cao

**分类**: cs.CL

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出MR. Judge以提升多模态语言模型的评判能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `语言模型` `评判机制` `自动注释` `推理能力`

## 📋 核心要点

1. 现有方法在评判响应时缺乏有效的推理机制，导致评判结果的可解释性和准确性不足。
2. 本文提出的MR. Judge通过将评判过程视为推理驱动的多选问题，增强了MLLM的推理能力和评判效果。
3. 实验结果显示，MR. Judge-7B在多个基准测试中表现优异，尤其在VL-RewardBench上超越了GPT-4o，提升幅度显著。

## 📝 摘要（中文）

随着使用大型语言模型（LLMs）和多模态大型语言模型（MLLMs）作为评判者的范式逐渐成熟，本文提出了多模态推理者作为评判者（MR. Judge），旨在赋予通用MLLMs更强的推理能力。与直接为每个响应打分不同，我们将评判过程构建为一种基于推理的多选问题。评判模型首先进行全面的推理，涵盖响应的不同方面，最终选择最佳响应。这一推理过程不仅提高了评判的可解释性，还显著增强了MLLM评判者的性能。为了解决缺乏带评分响应的问题，我们提出了自动注释策略，包括反向响应候选合成和基于文本的推理提取。实验表明，MR. Judge在多项任务中表现出色，MR. Judge-7B在VL-RewardBench上超越GPT-4o 9.9%，在推理时间扩展中提升MM-Vet性能达7.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态语言模型在评判响应时缺乏有效推理能力的问题，导致评判结果的可解释性和准确性不足。

**核心思路**：MR. Judge通过将评判过程转化为推理驱动的多选问题，使模型在评判时能够进行全面的推理，最终选择最佳响应。这种设计旨在提高评判的可解释性和准确性。

**技术框架**：MR. Judge的整体架构包括两个主要模块：反向响应候选合成和基于文本的推理提取。反向合成模块从监督微调数据集中生成负面候选响应，而推理提取模块则通过数据合成管道提取推理能力。

**关键创新**：最重要的创新点在于将评判过程视为推理问题，利用多模态模型的推理能力进行响应选择。这一方法与传统的直接评分方式本质上不同，强调了推理过程的重要性。

**关键设计**：在关键设计方面，模型采用了精心设计的损失函数和网络结构，以确保推理能力的有效提取和应用，同时在训练过程中进行了适当的超参数调整，以优化模型性能。

## 📊 实验亮点

实验结果显示，MR. Judge-7B在VL-RewardBench上超越了GPT-4o 9.9%，并在推理时间扩展中提升MM-Vet性能达7.7%。这些结果表明，MR. Judge在多项任务中均表现出色，验证了其有效性和优越性。

## 🎯 应用场景

MR. Judge的研究成果具有广泛的应用潜力，尤其在需要高质量评判和反馈的领域，如教育、内容审核和人机交互等。通过提升多模态语言模型的推理能力，该方法能够为用户提供更准确和可解释的评判结果，进而推动相关领域的智能化发展。

## 📄 摘要（原文）

> The paradigm of using Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) as evaluative judges has emerged as an effective approach in RLHF and inference-time scaling. In this work, we propose Multimodal Reasoner as a Judge (MR. Judge), a paradigm for empowering general-purpose MLLMs judges with strong reasoning capabilities. Instead of directly assigning scores for each response, we formulate the judgement process as a reasoning-inspired multiple-choice problem. Specifically, the judge model first conducts deliberate reasoning covering different aspects of the responses and eventually selects the best response from them. This reasoning process not only improves the interpretibility of the judgement, but also greatly enhances the performance of MLLM judges. To cope with the lack of questions with scored responses, we propose the following strategy to achieve automatic annotation: 1) Reverse Response Candidates Synthesis: starting from a supervised fine-tuning (SFT) dataset, we treat the original response as the best candidate and prompt the MLLM to generate plausible but flawed negative candidates. 2) Text-based reasoning extraction: we carefully design a data synthesis pipeline for distilling the reasoning capability from a text-based reasoning model, which is adopted to enable the MLLM judges to regain complex reasoning ability via warm up supervised fine-tuning. Experiments demonstrate that our MR. Judge is effective across a wide range of tasks. Specifically, our MR. Judge-7B surpasses GPT-4o by 9.9% on VL-RewardBench, and improves performance on MM-Vet during inference-time scaling by up to 7.7%.


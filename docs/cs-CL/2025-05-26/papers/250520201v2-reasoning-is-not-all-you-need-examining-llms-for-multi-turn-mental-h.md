---
layout: default
title: Reasoning Is Not All You Need: Examining LLMs for Multi-Turn Mental Health Conversations
---

# Reasoning Is Not All You Need: Examining LLMs for Multi-Turn Mental Health Conversations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20201" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20201v2</a>
  <a href="https://arxiv.org/pdf/2505.20201.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20201v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20201v2', 'Reasoning Is Not All You Need: Examining LLMs for Multi-Turn Mental Health Conversations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohit Chandra, Siddharth Sriraman, Harneet Singh Khanuja, Yiqiao Jin, Munmun De Choudhury

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-05-28)

**备注**: 34 pages, 5 figures, 30 tables

---

## 💡 一句话要点

**提出MedAgent框架以解决多轮心理健康对话评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理健康对话` `大型语言模型` `多轮对话` `数据生成` `评估框架` `患者中心` `对话系统`

## 📋 核心要点

1. 现有方法主要关注诊断准确性，忽视了患者特定目标和个性，导致多轮对话效果不佳。
2. 论文提出MedAgent框架，通过合成生成多轮心理健康对话，创建MHSD数据集以支持评估。
3. 实验结果显示，前沿模型在患者沟通中的表现低于预期，且随着对话轮次增加，性能下降明显。

## 📝 摘要（中文）

由于心理健康服务的有限获取和大型语言模型（LLMs）能力的提升，越来越多的人开始依赖LLMs来满足心理健康需求。然而，LLMs在多轮心理健康对话中的能力尚未得到充分探讨。现有评估框架通常关注诊断准确性和胜率，忽视了与患者特定目标、价值观和个性的一致性。为此，本文提出了MedAgent，一个用于合成生成现实的多轮心理健康对话的框架，并利用该框架创建了包含2200多个患者-LLM对话的心理健康理解对话（MHSD）数据集。此外，我们还提出了MultiSenseEval，一个全面评估LLMs在医疗环境中多轮对话能力的框架。研究发现，前沿推理模型在以患者为中心的沟通中表现不佳，且在高级诊断能力方面的平均得分仅为31%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多轮心理健康对话中的评估不足，现有方法未能充分考虑患者的个性和目标，导致对话效果不理想。

**核心思路**：提出MedAgent框架，通过合成生成真实的多轮心理健康对话，创建MHSD数据集，以便于全面评估LLMs在此领域的表现。

**技术框架**：该框架包括数据生成模块、对话评估模块和模型性能分析模块，旨在通过合成数据和人本标准来评估LLMs的对话能力。

**关键创新**：MedAgent框架及MHSD数据集的创建是本研究的核心创新，提供了一个新的评估标准，超越了传统的诊断准确性和胜率评估。

**关键设计**：在数据生成过程中，采用了特定的对话策略和情感分析技术，确保生成的对话符合心理健康领域的实际需求。

## 📊 实验亮点

实验结果表明，前沿推理模型在患者沟通中的平均得分仅为31%，显示出其在多轮对话中的不足。此外，随着对话轮次的增加，模型性能出现明显下降，强调了对话设计的重要性和复杂性。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康咨询、在线心理治疗和智能客服等。通过提供更符合患者需求的对话能力，LLMs可以在心理健康领域发挥更大的作用，改善患者的体验和结果。未来，随着技术的进步，该框架可能会推动更广泛的心理健康服务的自动化和个性化。

## 📄 摘要（原文）

> Limited access to mental healthcare, extended wait times, and increasing capabilities of Large Language Models (LLMs) has led individuals to turn to LLMs for fulfilling their mental health needs. However, examining the multi-turn mental health conversation capabilities of LLMs remains under-explored. Existing evaluation frameworks typically focus on diagnostic accuracy and win-rates and often overlook alignment with patient-specific goals, values, and personalities required for meaningful conversations. To address this, we introduce MedAgent, a novel framework for synthetically generating realistic, multi-turn mental health sensemaking conversations and use it to create the Mental Health Sensemaking Dialogue (MHSD) dataset, comprising over 2,200 patient-LLM conversations. Additionally, we present MultiSenseEval, a holistic framework to evaluate the multi-turn conversation abilities of LLMs in healthcare settings using human-centric criteria. Our findings reveal that frontier reasoning models yield below-par performance for patient-centric communication and struggle at advanced diagnostic capabilities with average score of 31%. Additionally, we observed variation in model performance based on patient's persona and performance drop with increasing turns in the conversation. Our work provides a comprehensive synthetic data generation framework, a dataset and evaluation framework for assessing LLMs in multi-turn mental health conversations.


---
layout: default
title: Advancing Conversational Diagnostic AI with Multimodal Reasoning
---

# Advancing Conversational Diagnostic AI with Multimodal Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04653" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04653v1</a>
  <a href="https://arxiv.org/pdf/2505.04653.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04653v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04653v1', 'Advancing Conversational Diagnostic AI with Multimodal Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khaled Saab, Jan Freyberg, Chunjong Park, Tim Strother, Yong Cheng, Wei-Hung Weng, David G. T. Barrett, David Stutz, Nenad Tomasev, Anil Palepu, Valentin Liévin, Yash Sharma, Roma Ruparel, Abdullah Ahmed, Elahe Vedadi, Kimberly Kanada, Cian Hughes, Yun Liu, Geoff Brown, Yang Gao, Sean Li, S. Sara Mahdavi, James Manyika, Katherine Chou, Yossi Matias, Avinatan Hassidim, Dale R. Webster, Pushmeet Kohli, S. M. Ali Eslami, Joëlle Barral, Adam Rodman, Vivek Natarajan, Mike Schaekermann, Tao Tu, Alan Karthikesalingam, Ryutaro Tanno

**分类**: cs.CL, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出多模态推理以提升对话式诊断AI的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `对话式AI` `诊断系统` `远程医疗` `智能医疗`

## 📋 核心要点

1. 现有方法主要依赖语言交互，无法有效处理多模态医疗数据，限制了远程医疗的应用。
2. 本文提出AMIE系统，具备收集和推理多模态数据的能力，能够动态控制对话流程，模拟经验丰富的临床医生。
3. 实验结果显示AMIE在7/9多模态和29/32非多模态评估维度上优于初级保健医生，展示了显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLMs）在进行诊断对话方面展现了巨大潜力，但评估主要局限于语言交互，未能满足远程医疗的实际需求。本文提出了一种新能力，能够收集和解释多模态数据，并在咨询过程中进行精确推理，从而提升Articulate Medical Intelligence Explorer（AMIE）的对话诊断和管理性能。通过与初级保健医生的随机盲测比较，AMIE在多模态和非多模态评估中均表现出色，显示出多模态对话诊断AI的明显进展，但实际应用仍需进一步研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有对话式诊断AI在多模态数据处理上的不足，现有方法无法有效整合和推理来自不同医疗来源的信息。

**核心思路**：提出AMIE系统，通过动态对话框架，结合多模态数据推理，提升诊断对话的准确性和流畅性，模拟临床医生的思维过程。

**技术框架**：系统基于Gemini 2.0 Flash，采用状态感知对话框架，主要模块包括数据收集、状态推理、对话管理和反馈生成，确保对话流的动态控制。

**关键创新**：AMIE的核心创新在于其多模态推理能力，能够在对话中实时整合和分析多种医疗数据，显著提升了诊断的准确性和历史采集的结构化程度。

**关键设计**：系统设计中采用了状态感知机制，结合不确定性引导后续问题，确保对话的针对性和有效性，同时在损失函数和网络结构上进行了优化，以适应多模态数据的特性。

## 📊 实验亮点

实验结果表明，AMIE在7/9多模态和29/32非多模态评估维度上优于初级保健医生，特别是在诊断准确性方面，显示出显著的性能提升。这一成果为多模态对话诊断AI的发展奠定了基础。

## 🎯 应用场景

该研究的潜在应用领域包括远程医疗、智能诊断助手和医疗咨询平台。通过提升对话式诊断AI的多模态处理能力，能够更好地满足临床医生和患者的需求，提高医疗服务的效率和准确性，未来可能在实际医疗场景中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated great potential for conducting diagnostic conversations but evaluation has been largely limited to language-only interactions, deviating from the real-world requirements of remote care delivery. Instant messaging platforms permit clinicians and patients to upload and discuss multimodal medical artifacts seamlessly in medical consultation, but the ability of LLMs to reason over such data while preserving other attributes of competent diagnostic conversation remains unknown. Here we advance the conversational diagnosis and management performance of the Articulate Medical Intelligence Explorer (AMIE) through a new capability to gather and interpret multimodal data, and reason about this precisely during consultations. Leveraging Gemini 2.0 Flash, our system implements a state-aware dialogue framework, where conversation flow is dynamically controlled by intermediate model outputs reflecting patient states and evolving diagnoses. Follow-up questions are strategically directed by uncertainty in such patient states, leading to a more structured multimodal history-taking process that emulates experienced clinicians. We compared AMIE to primary care physicians (PCPs) in a randomized, blinded, OSCE-style study of chat-based consultations with patient actors. We constructed 105 evaluation scenarios using artifacts like smartphone skin photos, ECGs, and PDFs of clinical documents across diverse conditions and demographics. Our rubric assessed multimodal capabilities and other clinically meaningful axes like history-taking, diagnostic accuracy, management reasoning, communication, and empathy. Specialist evaluation showed AMIE to be superior to PCPs on 7/9 multimodal and 29/32 non-multimodal axes (including diagnostic accuracy). The results show clear progress in multimodal conversational diagnostic AI, but real-world translation needs further research.


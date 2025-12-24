---
layout: default
title: "CaughtCheating: Is Your MLLM a Good Cheating Detective? Exploring the Boundary of Visual Perception and Reasoning"
---

# CaughtCheating: Is Your MLLM a Good Cheating Detective? Exploring the Boundary of Visual Perception and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.00045" class="toolbar-btn" target="_blank">📄 arXiv: 2507.00045v1</a>
  <a href="https://arxiv.org/pdf/2507.00045.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.00045v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.00045v1', 'CaughtCheating: Is Your MLLM a Good Cheating Detective? Exploring the Boundary of Visual Perception and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ming Li, Chenguang Wang, Yijun Liang, Xiyao Wang, Yuhang Zhou, Xiyang Wu, Yuqing Zhang, Ruiyi Zhang, Tianyi Zhou

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-23

---

## 💡 一句话要点

**提出CaughtCheating以解决多模态大语言模型的视觉推理挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉推理` `社交媒体` `复杂任务` `模型评估` `侦探能力` `视觉感知` `实验分析`

## 📋 核心要点

1. 现有的多模态大语言模型在处理复杂视觉推理任务时表现不佳，尤其是在需要识别细微线索的场景中。
2. 本文提出了CaughtCheating任务，旨在评估MLLMs在视觉感知与推理方面的能力，特别是在社交媒体场景中的应用。
3. 通过系统的实验与分析，发现GPT-o3在CaughtCheating任务中的表现显著下降，为未来的研究提供了新的方向。

## 📝 摘要（中文）

近年来，代理型多模态大语言模型（MLLMs）如GPT-o3在各种基准测试中表现优异，促使对更具挑战性的测试任务的需求。本文探讨了MLLMs在处理复杂视觉线索时的能力，尤其是其在“CaughtCheating”场景中的表现，该场景模拟社交媒体上用户请求他人识别伴侣照片中的可疑线索的情境。通过大量实验，分析了现有MLLMs在此类任务中表现不佳的原因，并提出了一类具有重要价值的视觉感知与推理任务，为MLLMs实现人类级别的侦探感知与推理能力铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在复杂视觉推理任务中的不足，尤其是在识别社交媒体照片中的可疑线索时的能力缺失。现有方法在此类任务中表现不佳，无法有效处理细微的视觉信息。

**核心思路**：论文提出了CaughtCheating任务，通过设计一系列具有挑战性的视觉感知与推理场景，评估MLLMs的侦探能力。该设计旨在揭示模型在处理复杂线索时的局限性，并为改进提供依据。

**技术框架**：研究采用了多阶段实验流程，首先定义任务场景，然后设计实验以评估模型在不同条件下的表现，最后进行数据分析以识别模型的弱点。主要模块包括任务设计、模型评估和结果分析。

**关键创新**：CaughtCheating任务是本文的核心创新，提供了一种新的评估标准，强调了视觉推理在多模态大语言模型中的重要性。这一任务与现有的标准测试方法有本质区别，聚焦于社交媒体环境中的实际应用。

**关键设计**：在实验中，设置了多种参数以确保任务的挑战性，包括视觉线索的复杂性和模糊性。此外，采用了特定的损失函数来优化模型在视觉推理任务中的表现。

## 📊 实验亮点

实验结果显示，GPT-o3在CaughtCheating任务中的表现显著下降，准确率接近零，表明其在复杂视觉推理场景中的局限性。这一发现为未来的模型改进提供了重要的实验依据，并强调了在视觉推理任务中提升模型能力的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、在线欺诈检测以及智能助手等。通过提升多模态大语言模型在视觉推理方面的能力，可以更好地识别和处理用户上传的可疑内容，从而提高平台的安全性和用户体验。未来，该研究可能推动更智能的视觉分析工具的发展，促进人机协作的进步。

## 📄 摘要（原文）

> Recent agentic Multi-Modal Large Language Models (MLLMs) such as GPT-o3 have achieved near-ceiling scores on various existing benchmarks, motivating a demand for more challenging test tasks. These MLLMs have been reported to excel in a few expert-level tasks for humans, e.g., GeoGuesser, reflecting their potential as a detective who can notice minuscule cues in an image and weave them into coherent, situational explanations, leading to a reliable answer. But can they match the performance of excellent human detectives? To answer this question, we investigate some hard scenarios where GPT-o3 can still handle, and find a common scenario where o3's performance drops to nearly zero, which we name CaughtCheating. It is inspired by the social media requests that ask others to detect suspicious clues from photos shared by the poster's partner. We conduct extensive experiments and analysis to understand why existing MLLMs lack sufficient capability to solve this kind of task. CaughtCheating provides a class of challenging visual perception and reasoning tasks with great value and practical usage. Success in these tasks paves the way for MLLMs to acquire human-level detective perception and reasoning capabilities.


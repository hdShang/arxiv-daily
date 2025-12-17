---
layout: default
title: Echo-CoPilot: A Multi-View, Multi-Task Agent for Echocardiography Interpretation and Reporting
---

# Echo-CoPilot: A Multi-View, Multi-Task Agent for Echocardiography Interpretation and Reporting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09944" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09944</a>
  <a href="https://arxiv.org/pdf/2512.09944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09944" onclick="toggleFavorite(this, '2512.09944', 'Echo-CoPilot: A Multi-View, Multi-Task Agent for Echocardiography Interpretation and Reporting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Moein Heidari, Mohammad Amin Roohi, Ilker Hacihaliloglu

**分类**: cs.AI, cs.CV, cs.LG, eess.IV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Echo-CoPilot：用于心动超声解读和报告的多视角多任务智能体**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心动超声` `大型语言模型` `多任务学习` `医学影像` `报告生成`

## 📋 核心要点

1. 传统心动超声解读依赖手动，耗时且易出错，现有模型缺乏统一的临床评估能力。
2. Echo-CoPilot利用大型语言模型协调多种工具，实现多视角、多任务的心动超声自动解读。
3. 在MIMIC-EchoQA基准测试中，Echo-CoPilot的准确率达到50.8%，优于其他视觉语言模型。

## 📝 摘要（中文）

心动超声检查是现代心血管护理的核心，但完整的研究解读仍然是一项认知需求高、多视角的任务，目前仍以手动方式进行。虽然最近的心动超声基础模型可以在诸如视图分类、分割或疾病预测等单个感知子任务上实现强大的性能，但它们通常孤立地运行，无法提供统一的、临床上连贯的评估。本文介绍了Echo-CoPilot，一个多视角、多任务智能体，它使用大型语言模型来协调一套专门的心动超声工具。在ReAct风格的循环中，该智能体分解临床医生的查询，调用工具进行视图识别、心脏结构分割、测量和疾病预测以及报告合成，并将它们的输出集成到符合指南的答案和叙述性摘要中。我们在公共MIMIC-EchoQA基准上评估了Echo-CoPilot，其准确率达到了50.8％，优于通用和生物医学视频视觉语言模型。定性分析进一步表明，该智能体利用定量测量和生理背景来解决临床决策阈值附近的具有挑战性的病例，例如临界左心室肥厚或心包积液严重程度。

## 🔬 方法详解

**问题定义**：心动超声检查在心血管疾病诊断中至关重要，但人工解读耗时且主观性强。现有方法通常针对单一任务（如视图分类、分割），缺乏对整个超声报告的综合理解和生成能力。因此，如何构建一个能够自动、准确地解读心动超声并生成报告的系统是亟待解决的问题。

**核心思路**：Echo-CoPilot的核心思路是利用大型语言模型（LLM）作为协调者，将多个专业的心动超声分析工具整合起来，形成一个多视角、多任务的智能体。通过ReAct循环，LLM能够根据临床医生的查询，动态地调用不同的工具，并将结果整合，最终生成符合临床指南的报告。这种方法模仿了医生解读超声的过程，即先识别视图，然后进行测量和疾病预测，最后综合所有信息得出结论。

**技术框架**：Echo-CoPilot的技术框架主要包含以下几个模块：1) 查询分解模块：将临床医生的查询分解为多个子任务。2) 工具调用模块：根据子任务，调用相应的专业工具，如视图识别、心脏结构分割、测量和疾病预测工具。3) 结果整合模块：将各个工具的输出结果整合起来，形成一个统一的表示。4) 报告生成模块：利用LLM生成符合临床指南的报告。整个流程采用ReAct循环，LLM根据当前状态和工具的反馈，不断调整策略，直到生成最终报告。

**关键创新**：Echo-CoPilot的关键创新在于将大型语言模型应用于心动超声解读领域，并将其作为智能体的核心协调者。与以往的单任务模型不同，Echo-CoPilot能够处理多视角、多任务的复杂场景，并生成完整的超声报告。此外，ReAct循环的设计使得智能体能够动态地调整策略，更好地适应不同的临床查询。

**关键设计**：Echo-CoPilot的关键设计包括：1) 使用预训练的视觉模型进行视图识别、心脏结构分割和疾病预测。2) 利用大型语言模型进行查询分解、结果整合和报告生成。3) 设计ReAct循环，使得智能体能够动态地调整策略。4) 使用临床指南作为约束，确保生成的报告符合医学规范。具体的参数设置、损失函数和网络结构等细节未在论文中详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.09944/figures/Echo-CoPilot.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.09944/examples2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.09944/fig3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Echo-CoPilot在MIMIC-EchoQA基准测试中取得了50.8%的准确率，显著优于通用的和生物医学的视频视觉语言模型。定性分析表明，该智能体能够利用定量测量和生理背景信息，解决临床决策阈值附近的复杂病例，例如临界左心室肥厚或心包积液严重程度的判断。

## 🎯 应用场景

Echo-CoPilot可应用于临床心动超声报告的自动生成，减轻医生的工作负担，提高诊断效率和准确性。它还可以作为教学工具，帮助医学生学习心动超声的解读。未来，该技术有望扩展到其他医学影像领域，实现更广泛的临床应用。

## 📄 摘要（原文）

> Echocardiography is central to contemporary cardiovascular care, but full-study interpretation remains a cognitively demanding, multi-view task that is still performed manually. While recent foundation models for echocardiography can achieve strong performance on individual perceptual subtasks such as view classification, segmentation, or disease prediction, they typically operate in isolation and do not provide a unified, clinically coherent assessment. In this work, we introduce Echo-CoPilot, a multi-view, multi-task agent that uses a large language model to orchestrate a suite of specialized echocardiography tools. Within a ReAct-style loop, the agent decomposes clinician queries, invokes tools for view recognition, cardiac structure segmentation, measurement and disease prediction, and report synthesis, and integrates their outputs into guideline-aware answers and narrative summaries. We evaluate Echo-CoPilot on the public MIMIC-EchoQA benchmark, where it achieves an accuracy of 50.8\%, outperforming both general-purpose and biomedical video vision-language models. Qualitative analyses further show that the agent leverages quantitative measurements and physiologic context to resolve challenging cases near clinical decision thresholds, such as borderline left ventricular hypertrophy or pericardial effusion severity. The code will be released upon acceptance of the paper.


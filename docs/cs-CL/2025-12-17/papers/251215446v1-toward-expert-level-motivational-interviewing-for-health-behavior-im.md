---
layout: default
title: Toward expert-level motivational interviewing for health behavior improvement with LLMs
---

# Toward expert-level motivational interviewing for health behavior improvement with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15446" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15446v1</a>
  <a href="https://arxiv.org/pdf/2512.15446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15446v1" onclick="toggleFavorite(this, '2512.15446v1', 'Toward expert-level motivational interviewing for health behavior improvement with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Run-ze Hu, Yang Yang, Yi-hang Yang, Jing-qi Kong, Jia-hui Luo, Wen-yu Yang, Jing Chen, Jing-yao Liu, Hui-qun Zeng, Lei Zhang, Zheng Liu

**分类**: cs.CL

**发布日期**: 2025-12-17

**备注**: 26 pages, 3 figures

---

## 💡 一句话要点

**利用大型语言模型实现专家级动机访谈，促进健康行为改善**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动机访谈` `大型语言模型` `健康行为改变` `心理咨询` `AI辅助` `自然语言处理` `微调` `中文LLM`

## 📋 核心要点

1. 动机访谈(MI)在促进健康行为改变方面有效，但依赖于高水平的人工咨询师，成本高昂且难以规模化。
2. 本研究通过在MI风格的对话数据上微调开源LLM，构建了MI-LLMs，旨在提供一种可扩展的AI辅助方案。
3. 实验结果表明，微调后的MI-LLMs在技术和关系层面上的表现接近真实MI对话，展现了AI在健康咨询领域的潜力。

## 📝 摘要（中文）

背景：动机访谈(MI)是一种有效的咨询方法，可以促进健康行为的改变，但其影响受到训练有素的人工咨询师需求的限制。目的：本研究旨在通过开发和评估用于动机访谈的大型语言模型(MI-LLMs)来探索一种可扩展的替代方案。方法：我们首先整理了五个中文心理咨询语料库，并使用带有MI提示的GPT-4将来自两个最高质量数据集(CPsyCounD和PsyDTCorpus)的多轮对话转录为2040个MI风格的咨询对话，其中2000个用于训练，40个用于测试。三个具有中文能力的开源LLM(Baichuan2-7B-Chat, ChatGLM-4-9B-Chat和Llama-3-8B-Chinese-Chat-v2)在此语料库上进行了微调，并命名为MI-LLMs。我们使用基于回合的自动指标和专家手动编码(使用动机访谈治疗完整性(MITI)编码手册4.2.1)评估了MI-LLMs。结果：在所有三个模型中，与基础模型相比，微调显著提高了BLEU-4和ROUGE分数，手动编码表明MI-LLMs实现了接近真实MI对话的技术和关系全局分数以及MI一致性比率，尽管复杂反思和反思-问题比率仍然较低。结论：这些发现提供了初步证据，表明面向MI的微调可以赋予通用LLM核心的MI一致咨询行为，这表明了一种可扩展的AI辅助健康行为改变支持途径，同时也强调了需要在数据规模、复杂MI技能和真实干预试验方面做进一步的工作。

## 🔬 方法详解

**问题定义**：本研究旨在解决健康行为改变咨询中人工咨询师资源有限的问题。现有方法依赖于训练有素的咨询师，成本高昂且难以大规模推广。因此，需要一种可扩展的、低成本的解决方案，以满足日益增长的健康咨询需求。

**核心思路**：本研究的核心思路是利用大型语言模型(LLM)的强大生成能力和理解能力，通过在MI风格的对话数据上进行微调，使LLM能够模拟专家级咨询师的行为，从而提供AI辅助的动机访谈服务。这种方法旨在降低咨询成本，提高可及性，并实现个性化的健康行为干预。

**技术框架**：整体框架包括以下几个主要阶段：1) 数据收集与整理：收集并整理中文心理咨询语料库，并使用GPT-4将其转录为MI风格的对话。2) 模型选择与微调：选择具有中文能力的开源LLM（Baichuan2-7B-Chat, ChatGLM-4-9B-Chat和Llama-3-8B-Chinese-Chat-v2），并在MI风格的对话数据上进行微调。3) 模型评估：使用自动指标（BLEU-4, ROUGE）和专家手动编码（MITI）对微调后的模型进行评估。

**关键创新**：本研究的关键创新在于：1) 构建了MI-LLMs，首次探索了利用LLM进行动机访谈的可能性。2) 提出了基于MI风格对话数据的微调方法，使LLM能够学习并模拟专家级咨询师的行为。3) 使用MITI编码手册对MI-LLMs进行了全面评估，验证了其在技术和关系层面上的有效性。

**关键设计**：在数据方面，使用了高质量的中文心理咨询语料库，并使用GPT-4将其转录为MI风格的对话，保证了数据的质量和多样性。在模型方面，选择了具有中文能力的开源LLM，并进行了充分的微调，使其能够更好地适应MI任务。在评估方面，使用了自动指标和专家手动编码相结合的方法，全面评估了MI-LLMs的性能。

## 📊 实验亮点

实验结果表明，经过MI风格对话数据微调后，Baichuan2-7B-Chat, ChatGLM-4-9B-Chat和Llama-3-8B-Chinese-Chat-v2三个模型在BLEU-4和ROUGE等指标上均有显著提升。专家手动编码结果显示，MI-LLMs在技术和关系全局得分以及MI一致性比率上接近真实MI对话水平，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于在线健康咨询平台、智能健康助手、慢性病管理系统等领域，为用户提供个性化的健康行为干预服务。通过AI辅助的动机访谈，可以有效提高用户对健康行为改变的积极性，促进健康生活方式的养成，从而改善整体健康水平。

## 📄 摘要（原文）

> Background: Motivational interviewing (MI) is an effective counseling approach for promoting health behavior change, but its impact is constrained by the need for highly trained human counselors. Objective: This study aimed to explore a scalable alternative by developing and evaluating Large Language Models for Motivational Interviewing (MI-LLMs). Methods: We first curated five Chinese psychological counseling corpora and, using GPT-4 with an MI-informed prompt, transcribed multi-turn dialogues from the two highest-quality datasets (CPsyCounD and PsyDTCorpus) into 2,040 MI-style counseling conversations, of which 2,000 were used for training and 40 for testing. Three Chinese-capable open-source LLMs (Baichuan2-7B-Chat, ChatGLM-4-9B-Chat and Llama-3-8B-Chinese-Chat-v2) were fine-tuned on this corpus and were named as MI-LLMs. We evaluated MI-LLMs using round-based automatic metrics and expert manual coding with the Motivational Interviewing Treatment Integrity (MITI) Coding Manual 4.2.1. Results: Across all three models, fine-tuning substantially improved BLEU-4 and ROUGE scores compared with the base models, and manual coding showed that MI-LLMs achieved technical and relational global scores, and MI-adherent ratios that approached those of real MI dialogues, although complex reflections and reflection-to-question ratios remained less frequent. Conclusions: These findings provide initial evidence that MI-oriented fine-tuning can endow general-purpose LLMs with core MI-consistent counseling behaviors, suggesting a scalable pathway toward AI-assisted health behavior change support while underscoring the need for further work on data scale, complex MI skills and real-world intervention trials.


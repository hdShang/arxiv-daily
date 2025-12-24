---
layout: default
title: "Radiology's Last Exam (RadLE): Benchmarking Frontier Multimodal AI Against Human Experts and a Taxonomy of Visual Reasoning Errors in Radiology"
---

# Radiology's Last Exam (RadLE): Benchmarking Frontier Multimodal AI Against Human Experts and a Taxonomy of Visual Reasoning Errors in Radiology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25559" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25559v1</a>
  <a href="https://arxiv.org/pdf/2509.25559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25559v1', 'Radiology\'s Last Exam (RadLE): Benchmarking Frontier Multimodal AI Against Human Experts and a Taxonomy of Visual Reasoning Errors in Radiology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Suvrankar Datta, Divya Buchireddygari, Lakshmi Vennela Chowdary Kaza, Mrudula Bhalke, Kautik Singh, Ayush Pandey, Sonit Sai Vasipalli, Upasana Karnwal, Hakikat Bir Singh Bhatti, Bhavya Ratan Maroo, Sanjana Hebbar, Rahul Joseph, Gurkawal Kaur, Devyani Singh, Akhil V, Dheeksha Devasya Shama Prasad, Nishtha Mahajan, Ayinaparthi Arisha, Rajesh Vanagundi, Reet Nandy, Kartik Vuthoo, Snigdhaa Rajvanshi, Nikhileswar Kondaveeti, Suyash Gunjal, Rishabh Jain, Rajat Jain, Anurag Agrawal

**分类**: cs.AI, cs.LG

**发布日期**: 2025-09-29

**备注**: 29 pages, 7 figures, 7 tables, includes Annexure (1). Part of the work accepted at RSNA 2025 (Cutting Edge Oral Presentation)

---

## 💡 一句话要点

**RadLE：放射学专家级诊断基准，评估多模态AI并分析视觉推理错误**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `放射学` `多模态AI` `视觉推理` `诊断基准` `医学影像` `大型语言模型` `专家系统`

## 📋 核心要点

1. 现有AI医学影像评估多集中于常见病理的公共数据集，缺乏对困难诊断案例的严格评估。
2. 构建RadLE基准，通过模拟真实使用场景，对比前沿AI模型与放射科医生在专家级诊断中的表现。
3. 实验表明，前沿AI模型在复杂诊断中远逊于放射科医生，并分析了AI视觉推理的错误类型。

## 📝 摘要（中文）

本研究开发了一个包含50个专家级“即时诊断”案例的放射学基准(RadLE)，涵盖多种影像模态，旨在评估前沿AI模型与认证放射科医生和放射学学员的诊断能力。通过原生Web界面测试了五种流行的前沿AI模型（OpenAI o3、OpenAI GPT-5、Gemini 2.5 Pro、Grok-4和Claude Opus 4.1）的推理模式，模拟真实世界的使用场景。由盲法专家对准确性进行评分，并通过三次独立运行评估可重复性。GPT-5还接受了各种推理模式的评估。研究定义了视觉推理错误的分类，并评估了推理质量。结果表明，认证放射科医生的诊断准确率最高（83%），优于学员（45%）和所有AI模型（GPT-5的最佳性能为30%）。GPT-5和o3的可靠性较高，Gemini 2.5 Pro和Grok-4的可靠性中等，Claude Opus 4.1的可靠性较差。研究结果表明，在具有挑战性的诊断案例中，先进的前沿模型与放射科医生相比仍有很大差距。该基准突出了通用AI在医学影像方面的局限性，并警告不要在无监督的情况下进行临床使用。此外，还对推理轨迹进行了定性分析，并提出了AI模型视觉推理错误的实用分类，以便更好地理解其失效模式，为评估标准提供信息，并指导更强大的模型开发。

## 🔬 方法详解

**问题定义**：论文旨在解决通用多模态AI模型在复杂放射学诊断任务中表现不足的问题。现有方法主要依赖于公共数据集，这些数据集通常包含常见病理，无法充分评估模型在处理罕见或复杂病例时的能力。此外，现有评估方法缺乏对AI模型推理过程的深入分析，难以了解其失效模式。

**核心思路**：论文的核心思路是构建一个更具挑战性的放射学诊断基准(RadLE)，该基准包含专家级的“即时诊断”案例，涵盖多种影像模态。通过将前沿AI模型与放射科医生和学员的诊断结果进行对比，可以更准确地评估AI模型在实际临床应用中的潜力。此外，论文还对AI模型的推理过程进行了定性分析，并提出了一个视觉推理错误的分类，以便更好地理解其失效模式。

**技术框架**：该研究的技术框架主要包括以下几个部分：1)构建RadLE基准：收集50个专家级的“即时诊断”案例，涵盖多种影像模态。2)选择前沿AI模型：选择五种流行的前沿AI模型（OpenAI o3、OpenAI GPT-5、Gemini 2.5 Pro、Grok-4和Claude Opus 4.1）进行评估。3)评估诊断准确性：由盲法专家对AI模型和人类专家的诊断结果进行评分。4)评估可靠性：通过三次独立运行评估AI模型诊断结果的可重复性。5)分析推理过程：对AI模型的推理轨迹进行定性分析，并提出一个视觉推理错误的分类。

**关键创新**：该论文的关键创新点在于：1)构建了一个更具挑战性的放射学诊断基准(RadLE)，该基准包含专家级的“即时诊断”案例，涵盖多种影像模态。2)对AI模型的推理过程进行了定性分析，并提出了一个视觉推理错误的分类，以便更好地理解其失效模式。3)通过模拟真实世界的使用场景，更准确地评估了前沿AI模型在实际临床应用中的潜力。

**关键设计**：在实验设计方面，论文采用了以下关键设计：1)盲法评估：由盲法专家对AI模型和人类专家的诊断结果进行评分，以避免主观偏差。2)独立运行：通过三次独立运行评估AI模型诊断结果的可重复性，以确保结果的可靠性。3)推理模式测试：通过原生Web界面测试AI模型的推理模式，以模拟真实世界的使用场景。4)错误分类：提出了一个视觉推理错误的分类，包括幻觉、忽略相关信息、不正确的空间推理等。

## 📊 实验亮点

实验结果表明，认证放射科医生的诊断准确率最高（83%），显著优于放射学学员（45%）和所有AI模型（GPT-5的最佳性能为30%）。GPT-5和o3的可靠性较高，Gemini 2.5 Pro和Grok-4的可靠性中等，Claude Opus 4.1的可靠性较差。这些数据清晰地展示了当前前沿AI模型在复杂放射学诊断任务中与人类专家之间的差距。

## 🎯 应用场景

该研究成果可应用于医学影像AI模型的评估和改进，指导更可靠的临床辅助诊断工具的开发。通过分析AI的视觉推理错误，可以针对性地改进模型，提高诊断准确率，减少误诊漏诊，最终提升医疗服务质量。

## 📄 摘要（原文）

> Generalist multimodal AI systems such as large language models (LLMs) and vision language models (VLMs) are increasingly accessed by clinicians and patients alike for medical image interpretation through widely available consumer-facing chatbots. Most evaluations claiming expert level performance are on public datasets containing common pathologies. Rigorous evaluation of frontier models on difficult diagnostic cases remains limited. We developed a pilot benchmark of 50 expert-level "spot diagnosis" cases across multiple imaging modalities to evaluate the performance of frontier AI models against board-certified radiologists and radiology trainees. To mirror real-world usage, the reasoning modes of five popular frontier AI models were tested through their native web interfaces, viz. OpenAI o3, OpenAI GPT-5, Gemini 2.5 Pro, Grok-4, and Claude Opus 4.1. Accuracy was scored by blinded experts, and reproducibility was assessed across three independent runs. GPT-5 was additionally evaluated across various reasoning modes. Reasoning quality errors were assessed and a taxonomy of visual reasoning errors was defined. Board-certified radiologists achieved the highest diagnostic accuracy (83%), outperforming trainees (45%) and all AI models (best performance shown by GPT-5: 30%). Reliability was substantial for GPT-5 and o3, moderate for Gemini 2.5 Pro and Grok-4, and poor for Claude Opus 4.1. These findings demonstrate that advanced frontier models fall far short of radiologists in challenging diagnostic cases. Our benchmark highlights the present limitations of generalist AI in medical imaging and cautions against unsupervised clinical use. We also provide a qualitative analysis of reasoning traces and propose a practical taxonomy of visual reasoning errors by AI models for better understanding their failure modes, informing evaluation standards and guiding more robust model development.


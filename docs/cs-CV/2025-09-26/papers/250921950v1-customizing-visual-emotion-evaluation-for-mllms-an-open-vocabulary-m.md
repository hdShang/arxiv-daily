---
layout: default
title: "Customizing Visual Emotion Evaluation for MLLMs: An Open-vocabulary, Multifaceted, and Scalable Approach"
---

# Customizing Visual Emotion Evaluation for MLLMs: An Open-vocabulary, Multifaceted, and Scalable Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21950" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21950v1</a>
  <a href="https://arxiv.org/pdf/2509.21950.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21950v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21950v1', 'Customizing Visual Emotion Evaluation for MLLMs: An Open-vocabulary, Multifaceted, and Scalable Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daiqing Wu, Dongbao Yang, Sicheng Zhao, Can Ma, Yu Zhou

**分类**: cs.CV

**发布日期**: 2025-09-26

**🔗 代码/项目**: [GITHUB](https://github.com/wdqqdw/MVEI)

---

## 💡 一句话要点

**提出一种开放词汇、多方面、可扩展的视觉情感评估方法，用于评估多模态大语言模型的情感理解能力。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉情感评估` `情感陈述判断` `开放词汇` `自动化数据生成`

## 📋 核心要点

1. 现有视觉情感评估方法存在不足，包括忽略合理响应、情感分类体系有限、忽视上下文因素和标注成本高昂。
2. 提出情感陈述判断任务和自动化流程，以开放词汇、多方面、可扩展的方式构建情感评估数据集。
3. 实验表明，MLLM在情感解释和上下文情感判断方面表现较好，但在理解感知主观性方面存在局限，与人类存在差距。

## 📝 摘要（中文）

近年来，多模态大语言模型（MLLMs）在各种任务中表现出色，其能力不断超出预期。然而，它们从图像中感知情感的能力仍然存在争议，在零样本场景下的研究结果各不相同。我们认为这种不一致部分源于现有评估方法的局限性，包括忽略了合理的响应、情感分类体系有限、忽视了上下文因素以及标注工作量大。为了促进MLLM的定制化视觉情感评估，我们提出了一种情感陈述判断任务，以克服这些限制。作为对该任务的补充，我们设计了一个自动化的流程，以最小的人工成本高效地构建以情感为中心的陈述。通过系统地评估主流MLLM，我们的研究展示了它们在情感解释和基于上下文的情感判断方面的更强性能，同时也揭示了在理解感知主观性方面的相对局限性。与人类相比，即使是像GPT4o这样的顶级MLLM也表现出显著的性能差距，突出了未来改进的关键领域。通过开发一个基础的评估框架并进行全面的MLLM评估，我们希望这项工作有助于提高MLLM的情感智能。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型（MLLMs）在视觉情感理解方面评估不一致的问题。现有评估方法的痛点在于：1) 忽略了模型可能产生的合理情感反应；2) 使用的情感分类体系过于有限，无法捕捉情感的细微差别；3) 忽视了图像的上下文信息对情感理解的影响；4) 需要大量的人工标注，成本高昂。这些问题导致现有评估结果无法准确反映MLLMs的真实情感理解能力。

**核心思路**：论文的核心思路是通过设计一种新的评估任务——情感陈述判断（Emotion Statement Judgment），并结合自动化数据生成流程，来克服现有评估方法的局限性。该方法允许使用开放词汇来描述情感，考虑了情感的多方面性，并能高效地生成大规模的评估数据集。通过让MLLMs判断给定的图像和情感陈述是否匹配，从而更全面地评估其视觉情感理解能力。

**技术框架**：整体框架包含两个主要部分：1) 情感陈述判断任务的设计：给定一张图像和一个情感陈述，MLLM需要判断该陈述是否准确描述了图像所表达的情感。2) 自动化数据生成流程：该流程利用算法自动生成大量以情感为中心的陈述，减少人工标注的需求。具体流程细节未知。

**关键创新**：论文的关键创新在于：1) 提出了一种新的视觉情感评估任务，该任务更全面地考虑了情感的复杂性和多样性；2) 设计了一种自动化的数据生成流程，大大降低了评估数据集的构建成本，使其更具可扩展性；3) 采用开放词汇进行情感描述，避免了传统情感分类体系的局限性。

**关键设计**：论文中关于情感陈述判断任务的关键设计在于允许开放词汇的情感描述，这使得评估能够捕捉到更细微和多样的情感表达。自动化数据生成流程的具体参数设置、损失函数和网络结构等技术细节未知。

## 📊 实验亮点

研究表明，主流MLLM在情感解释和基于上下文的情感判断方面表现出较强的性能。然而，在理解感知主观性方面存在局限性，与人类的表现存在显著差距，即使是GPT4o这样的顶级MLLM也未能达到人类水平。这突出了未来研究需要重点关注的方向，即提升MLLM对情感主观性的理解能力。

## 🎯 应用场景

该研究成果可应用于提升多模态大语言模型在情感计算、人机交互、智能客服、情感分析等领域的性能。更准确的情感理解能力有助于开发更具同理心和人性化的AI系统，例如，在心理健康咨询、情感陪伴机器人等场景中具有重要价值。此外，该评估框架可以作为MLLM情感智能发展的重要基准。

## 📄 摘要（原文）

> Recently, Multimodal Large Language Models (MLLMs) have achieved exceptional performance across diverse tasks, continually surpassing previous expectations regarding their capabilities. Nevertheless, their proficiency in perceiving emotions from images remains debated, with studies yielding divergent results in zero-shot scenarios. We argue that this inconsistency stems partly from constraints in existing evaluation methods, including the oversight of plausible responses, limited emotional taxonomies, neglect of contextual factors, and labor-intensive annotations. To facilitate customized visual emotion evaluation for MLLMs, we propose an Emotion Statement Judgment task that overcomes these constraints. Complementing this task, we devise an automated pipeline that efficiently constructs emotion-centric statements with minimal human effort. Through systematically evaluating prevailing MLLMs, our study showcases their stronger performance in emotion interpretation and context-based emotion judgment, while revealing relative limitations in comprehending perception subjectivity. When compared to humans, even top-performing MLLMs like GPT4o demonstrate remarkable performance gaps, underscoring key areas for future improvement. By developing a fundamental evaluation framework and conducting a comprehensive MLLM assessment, we hope this work contributes to advancing emotional intelligence in MLLMs. Project page: https://github.com/wdqqdw/MVEI.


---
layout: default
title: Seeing the Big Picture: Evaluating Multimodal LLMs' Ability to Interpret and Grade Handwritten Student Work
---

# Seeing the Big Picture: Evaluating Multimodal LLMs' Ability to Interpret and Grade Handwritten Student Work

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.05538" target="_blank" class="toolbar-btn">arXiv: 2510.05538v1</a>
    <a href="https://arxiv.org/pdf/2510.05538.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05538v1" 
            onclick="toggleFavorite(this, '2510.05538v1', 'Seeing the Big Picture: Evaluating Multimodal LLMs\' Ability to Interpret and Grade Handwritten Student Work')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Owen Henkel, Bill Roberts, Doug Jaffe, Laurence Holt

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-07

---

## 💡 一句话要点

**评估多模态LLM在手写学生作业判阅中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `大型语言模型` `手写识别` `教育应用` `自动评分`

## 📋 核心要点

1. 手写数学作业批改耗时，但能提供学生学习过程的宝贵信息，现有方法难以兼顾效率与洞察。
2. 利用多模态LLM直接判阅手写作业，并结合人工描述辅助模型理解，分离视觉与教学能力。
3. 实验表明，MLLM在算术题上表现接近人类，但在理解数学插图方面仍有提升空间。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)的最新进展引发了它们在批改、分析和提供手写学生作业反馈方面的潜力问题。这种能力在中小学数学教育中尤其有益，因为大多数作业仍然是手写的，看到学生解决问题的完整过程可以为了解他们的学习过程提供有价值的见解，但批改非常耗时。我们提出了两个实验，研究MLLM在手写学生数学作业上的表现。实验A检查了来自加纳中学生的288份手写答卷，这些学生解决的是有客观答案的算术题。在这种情况下，模型达到了接近人类的准确率(95%，k = 0.90)，但偶尔会出现人类教育工作者不太可能犯的错误。实验B评估了来自美国小学生的150幅数学插图，这些图画是问题的答案。这些任务缺乏单一的客观答案，需要复杂的视觉解释以及教学判断才能进行分析和评估。我们试图将MLLM的视觉能力与它们的教学能力分开，首先要求它们直接给学生的插图打分，然后用对插图的详细人工描述来增强图像。我们发现，当模型必须直接分析学生的插图时，它们表现不佳，与真实分数的kappa系数仅为0.20，但当给出人工描述时，它们的一致性水平显著提高到0.47，这与人与人之间的一致性水平一致。这一差距表明，MLLM可以相对较好地“看到”和解释算术作业，但在“看到”学生的数学插图方面仍然存在困难。

## 🔬 方法详解

**问题定义**：论文旨在评估多模态大型语言模型（MLLM）在理解和评分手写学生作业方面的能力。现有方法，特别是传统的人工批改，在处理大量手写作业时效率低下，且难以保证评分的一致性。此外，对于非客观题，如何准确理解学生的解题思路和创造性表达是一个挑战。

**核心思路**：论文的核心思路是利用MLLM的视觉理解能力和语言处理能力，直接对手写作业进行分析和评分。为了区分MLLM的视觉能力和教学能力，论文设计了实验，分别评估模型在直接分析图像和在人工描述辅助下的表现。通过对比两种情况下的评分结果，可以了解模型在视觉理解方面的局限性。

**技术框架**：该研究主要通过实验评估现有MLLM的能力，并没有提出新的模型架构。实验流程包括：1）收集手写学生作业数据，包括算术题和数学插图；2）使用MLLM直接对作业进行评分；3）对于数学插图，提供人工描述作为辅助信息，再次使用MLLM进行评分；4）将MLLM的评分结果与人工评分结果进行比较，计算一致性指标（Kappa系数）。

**关键创新**：该研究的创新点在于：1）首次系统性地评估了MLLM在手写学生作业判阅中的潜力；2）通过对比直接图像分析和人工描述辅助两种情况，分离了MLLM的视觉理解能力和教学能力；3）揭示了MLLM在处理不同类型手写作业（算术题 vs. 数学插图）时的性能差异。

**关键设计**：实验A使用了来自加纳中学生的288份算术题答卷，实验B使用了来自美国小学生的150幅数学插图。评分标准由人工制定，并作为ground truth。一致性评估采用Kappa系数，衡量MLLM评分与人工评分之间的一致性程度。对于人工描述，论文没有提供具体的设计细节，但强调了描述的详细程度。

## 📊 实验亮点

实验A表明，MLLM在算术题上的评分准确率达到95%，Kappa系数为0.90，接近人类水平。实验B发现，MLLM直接分析数学插图的Kappa系数仅为0.20，但在人工描述辅助下，Kappa系数提升至0.47，与人与人之间的一致性水平相当。这表明MLLM在视觉理解方面仍有提升空间。

## 🎯 应用场景

该研究成果可应用于智能教育领域，例如自动批改手写作业、提供个性化学习反馈、辅助教师进行教学评估等。尤其是在资源匮乏的地区，MLLM可以减轻教师的负担，提高教学效率。未来，结合更先进的MLLM和更精细的人工描述，有望实现更准确、更智能的作业批改和学习辅导。

## 📄 摘要（原文）

> Recent advances in multimodal large language models (MLLMs) raise the question of their potential for grading, analyzing, and offering feedback on handwritten student classwork. This capability would be particularly beneficial in elementary and middle-school mathematics education, where most work remains handwritten, because seeing students' full working of a problem provides valuable insights into their learning processes, but is extremely time-consuming to grade. We present two experiments investigating MLLM performance on handwritten student mathematics classwork. Experiment A examines 288 handwritten responses from Ghanaian middle school students solving arithmetic problems with objective answers. In this context, models achieved near-human accuracy (95%, k = 0.90) but exhibited occasional errors that human educators would be unlikely to make. Experiment B evaluates 150 mathematical illustrations from American elementary students, where the drawings are the answer to the question. These tasks lack single objective answers and require sophisticated visual interpretation as well as pedagogical judgment in order to analyze and evaluate them. We attempted to separate MLLMs' visual capabilities from their pedagogical abilities by first asking them to grade the student illustrations directly, and then by augmenting the image with a detailed human description of the illustration. We found that when the models had to analyze the student illustrations directly, they struggled, achieving only k = 0.20 with ground truth scores, but when given human descriptions, their agreement levels improved dramatically to k = 0.47, which was in line with human-to-human agreement levels. This gap suggests MLLMs can "see" and interpret arithmetic work relatively well, but still struggle to "see" student mathematical illustrations.


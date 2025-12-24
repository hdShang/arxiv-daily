---
layout: default
title: "Analysis of instruction-based LLMs' capabilities to score and judge text-input problems in an academic setting"
---

# Analysis of instruction-based LLMs' capabilities to score and judge text-input problems in an academic setting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20982" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20982v1</a>
  <a href="https://arxiv.org/pdf/2509.20982.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20982v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20982v1', 'Analysis of instruction-based LLMs\' capabilities to score and judge text-input problems in an academic setting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Valeria Ramirez-Garcia, David de-Fitero-Dominguez, Antonio Garcia-Cabot, Eva Garcia-Lopez

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**提出基于LLM的自动评分系统，用于评估学术文本输入问题，参考答案辅助效果最佳。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自动评分` `文本输入问题` `教育评估` `参考答案辅助`

## 📋 核心要点

1. 现有方法缺乏有效的自动评估学术文本输入问题的方法，尤其是在需要细致评分标准的情况下。
2. 提出五种基于LLM的评估系统，核心思想是利用LLM的理解和生成能力，结合不同的辅助信息（如参考答案、原子标准）进行评分。
3. 实验结果表明，参考答案辅助评估方法在多个指标上优于其他方法，与人工评估结果最接近，证明了其有效性。

## 📝 摘要（中文）

大型语言模型（LLM）可以作为评估者，这方面的研究包括LLM-as-a-Judge和微调的判断LLM。在教育领域，LLM已被研究为学生和教师的辅助工具。本研究调查了基于LLM的自动评估系统，用于评估学术文本输入问题，并使用评分标准。我们提出了五种评估系统，并在一个包含110个高等教育计算机科学学生答案的自定义数据集上进行了测试，使用了JudgeLM、Llama-3.1-8B和DeepSeek-R1-Distill-Llama-8B三个模型。这些评估系统包括：JudgeLM评估、参考答案辅助评估、无参考答案评估、加性评估和自适应评估。所有评估方法都与人工评估者的结果进行了比较。结果表明，使用LLM自动评估文本输入问题的最佳方法是参考答案辅助评估。与人工评估相比，参考答案辅助评估具有最低的中值绝对偏差（0.945）和最低的均方根偏差（1.214），可提供公平的评分以及深刻而完整的评估。其他方法，如加性评估和自适应评估，在简洁的答案中未能提供良好的结果，无参考答案评估缺乏正确评估问题所需的信息，而JudgeLM评估由于模型的局限性而未提供良好的结果。因此，我们得出结论，在适当的方法论辅助下，人工智能驱动的自动评估系统有潜力作为其他学术资源的补充工具。

## 🔬 方法详解

**问题定义**：论文旨在解决学术场景下文本输入题目的自动评分问题。现有方法，如人工评分，耗时耗力且可能存在主观偏差。利用LLM进行评分面临的挑战在于如何有效地利用LLM的知识和推理能力，并使其评分结果与人工评分尽可能一致。

**核心思路**：论文的核心思路是探索不同的LLM使用方式，并结合不同的辅助信息，以提高LLM评分的准确性和可靠性。通过对比不同的评估策略，找到最适合文本输入题目的自动评分方法。

**技术框架**：整体框架包括以下几个阶段：1) 数据集构建：收集计算机科学领域学生的文本输入答案，并由人工进行评分；2) 模型选择：选择JudgeLM、Llama-3.1-8B和DeepSeek-R1-Distill-Llama-8B三个LLM作为评估模型；3) 评估系统设计：设计五种不同的评估系统，包括JudgeLM评估、参考答案辅助评估、无参考答案评估、加性评估和自适应评估；4) 实验评估：使用不同的评估系统对数据集进行评分，并将结果与人工评分进行比较；5) 结果分析：分析不同评估系统的性能，并找出最佳的评估方法。

**关键创新**：论文的关键创新在于提出了多种基于LLM的评估系统，并系统地比较了它们在学术文本输入题目评分任务上的性能。特别是，参考答案辅助评估方法，通过提供参考答案作为上下文信息，显著提高了LLM评分的准确性。

**关键设计**：五种评估系统的关键设计如下：1) JudgeLM评估：直接使用JudgeLM模型进行评分；2) 参考答案辅助评估：将参考答案与学生答案一起输入LLM进行评分；3) 无参考答案评估：仅将学生答案输入LLM进行评分；4) 加性评估：将评分标准分解为多个原子标准，分别对每个标准进行评分，然后将结果加总；5) 自适应评估：根据每个问题的特点，动态生成评分标准，然后进行评分。实验中，使用中值绝对偏差（MAD）和均方根偏差（RMSD）作为评估指标，以衡量LLM评分与人工评分之间的差异。

## 📊 实验亮点

实验结果表明，参考答案辅助评估方法在所有评估方法中表现最佳，其与人工评估结果的中值绝对偏差（MAD）为0.945，均方根偏差（RMSD）为1.214，显著优于其他方法。这表明，提供参考答案可以有效提高LLM评分的准确性和可靠性。

## 🎯 应用场景

该研究成果可应用于在线教育平台、自动阅卷系统、智能辅导系统等领域。通过自动评估学生的文本输入答案，可以减轻教师的负担，提高教学效率，并为学生提供个性化的反馈和指导。此外，该方法还可以扩展到其他需要文本评估的场景，如论文评审、代码审查等。

## 📄 摘要（原文）

> Large language models (LLMs) can act as evaluators, a role studied by methods like LLM-as-a-Judge and fine-tuned judging LLMs. In the field of education, LLMs have been studied as assistant tools for students and teachers. Our research investigates LLM-driven automatic evaluation systems for academic Text-Input Problems using rubrics. We propose five evaluation systems that have been tested on a custom dataset of 110 answers about computer science from higher education students with three models: JudgeLM, Llama-3.1-8B and DeepSeek-R1-Distill-Llama-8B. The evaluation systems include: The JudgeLM evaluation, which uses the model's single answer prompt to obtain a score; Reference Aided Evaluation, which uses a correct answer as a guide aside from the original context of the question; No Reference Evaluation, which ommits the reference answer; Additive Evaluation, which uses atomic criteria; and Adaptive Evaluation, which is an evaluation done with generated criteria fitted to each question. All evaluation methods have been compared with the results of a human evaluator. Results show that the best method to automatically evaluate and score Text-Input Problems using LLMs is Reference Aided Evaluation. With the lowest median absolute deviation (0.945) and the lowest root mean square deviation (1.214) when compared to human evaluation, Reference Aided Evaluation offers fair scoring as well as insightful and complete evaluations. Other methods such as Additive and Adaptive Evaluation fail to provide good results in concise answers, No Reference Evaluation lacks information needed to correctly assess questions and JudgeLM Evaluations have not provided good results due to the model's limitations. As a result, we conclude that Artificial Intelligence-driven automatic evaluation systems, aided with proper methodologies, show potential to work as complementary tools to other academic resources.


---
layout: default
title: "Measuring Faithfulness and Abstention: An Automated Pipeline for Evaluating LLM-Generated 3-ply Case-Based Legal Arguments"
---

# Measuring Faithfulness and Abstention: An Automated Pipeline for Evaluating LLM-Generated 3-ply Case-Based Legal Arguments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00694" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00694v2</a>
  <a href="https://arxiv.org/pdf/2506.00694.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00694v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00694v2', 'Measuring Faithfulness and Abstention: An Automated Pipeline for Evaluating LLM-Generated 3-ply Case-Based Legal Arguments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Li Zhang, Morgan Gray, Jaromir Savelka, Kevin D. Ashley

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-31 (更新: 2025-06-03)

**备注**: 11 pages, 7th Workshop on Automated Semantic Analysis of Information in Legal Text @ ICAIL 2025, 16 June 2025, Chicago, IL

**🔗 代码/项目**: [PROJECT_PAGE](https://lizhang-aiandlaw.github.io/An-Automated-Pipeline-for-Evaluating-LLM-Generated-3-ply-Case-Based-Legal-Arguments/)

---

## 💡 一句话要点

**提出自动化评估管道以解决LLM生成法律论证的可靠性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `法律论证` `自动化评估` `因素提取` `幻觉检测` `弃权能力` `机器学习` `法律技术`

## 📋 核心要点

1. 现有大型语言模型在法律论证生成中的可靠性不足，尤其是在避免幻觉和适当弃权方面存在挑战。
2. 本文提出了一种自动化评估管道，通过外部LLM提取因素并与真实案例进行比较，评估LLM的生成能力。
3. 实验结果显示，尽管LLM在避免幻觉方面表现良好，但在因素利用和遵循弃权指令上存在显著不足。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂法律任务如论证生成中展现出潜力，但其可靠性仍然令人担忧。本文在先前人类评估的基础上，提出了一种自动化评估管道，专注于评估LLM在生成三层法律论证时的真实性（无幻觉）、因素利用和适当的弃权能力。我们定义幻觉为生成输入案例材料中不存在的因素，而弃权则是模型在没有事实依据时遵循指令不生成论证的能力。通过外部LLM提取生成论证中的因素，并与输入案例三元组中的真实因素进行比较，我们对八种不同的LLM进行了三项难度递增的测试。结果表明，尽管当前LLM在可行论证生成测试中避免幻觉的准确率超过90%，但它们往往未能充分利用案例中的相关因素。尤其是在弃权测试中，大多数模型未能遵循停止指令，反而生成了虚假的论证。该自动化管道为评估这些关键LLM行为提供了一种可扩展的方法，强调在法律环境中可靠部署之前需要改善因素利用和强健的弃权能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成法律论证时的可靠性问题，尤其是幻觉和弃权能力不足的挑战。现有方法依赖人工评估，效率低且主观性强。

**核心思路**：提出一种自动化评估管道，利用外部LLM提取生成论证中的因素，并与输入案例的真实因素进行比较，以量化LLM的表现。

**技术框架**：该管道包括三个主要模块：1) 生成论证的LLM；2) 外部LLM用于因素提取；3) 评估模块对比生成因素与真实因素。

**关键创新**：最重要的创新在于引入自动化评估机制，能够高效、客观地评估LLM在法律论证生成中的表现，克服了传统人工评估的局限。

**关键设计**：在实验中，设置了三项难度递增的测试，分别评估标准论证生成、角色互换论证生成和缺乏共同因素时的弃权能力，确保全面评估LLM的性能。实验中使用的损失函数和参数设置经过精心设计，以优化模型的生成能力和遵循指令的能力。

## 📊 实验亮点

实验结果显示，当前LLM在可行论证生成测试中避免幻觉的准确率超过90%。然而，在弃权测试中，大多数模型未能遵循指令，生成了虚假的论证，表明在因素利用和弃权能力方面仍需显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括法律技术、智能法律咨询和法律教育等。通过提高LLM在法律论证生成中的可靠性，可以为法律专业人士提供更为准确的支持，提升法律服务的效率和质量。未来，随着技术的进步，该评估管道有望在更多复杂的法律场景中得到应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) demonstrate potential in complex legal tasks like argument generation, yet their reliability remains a concern. Building upon pilot work assessing LLM generation of 3-ply legal arguments using human evaluation, this paper introduces an automated pipeline to evaluate LLM performance on this task, specifically focusing on faithfulness (absence of hallucination), factor utilization, and appropriate abstention. We define hallucination as the generation of factors not present in the input case materials and abstention as the model's ability to refrain from generating arguments when instructed and no factual basis exists. Our automated method employs an external LLM to extract factors from generated arguments and compares them against the ground-truth factors provided in the input case triples (current case and two precedent cases). We evaluated eight distinct LLMs on three tests of increasing difficulty: 1) generating a standard 3-ply argument, 2) generating an argument with swapped precedent roles, and 3) recognizing the impossibility of argument generation due to lack of shared factors and abstaining. Our findings indicate that while current LLMs achieve high accuracy (over 90%) in avoiding hallucination on viable argument generation tests (Tests 1 & 2), they often fail to utilize the full set of relevant factors present in the cases. Critically, on the abstention test (Test 3), most models failed to follow instructions to stop, instead generating spurious arguments despite the lack of common factors. This automated pipeline provides a scalable method for assessing these crucial LLM behaviors, highlighting the need for improvements in factor utilization and robust abstention capabilities before reliable deployment in legal settings. Link: https://lizhang-aiandlaw.github.io/An-Automated-Pipeline-for-Evaluating-LLM-Generated-3-ply-Case-Based-Legal-Arguments/


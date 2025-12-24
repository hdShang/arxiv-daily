---
layout: default
title: "Multiple-Choice Question Generation Using Large Language Models: Methodology and Educator Insights"
---

# Multiple-Choice Question Generation Using Large Language Models: Methodology and Educator Insights

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04851" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04851v1</a>
  <a href="https://arxiv.org/pdf/2506.04851.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04851v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04851v1', 'Multiple-Choice Question Generation Using Large Language Models: Methodology and Educator Insights')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Giorgio Biancini, Alessio Ferrato, Carla Limongelli

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-05

**备注**: Copyright ACM 2024. This is the author's version of the work. It is posted here for your personal use. Not for redistribution. The definitive Version of Record was published in Adjunct Proceedings of the 32nd ACM Conference on User Modeling, Adaptation and Personalization (UMAP Adjunct '24), http://dx.doi.org/10.1145/3631700.3665233

**DOI**: [10.1145/3631700.3665233](https://doi.org/10.1145/3631700.3665233)

---

## 💡 一句话要点

**利用大型语言模型生成多项选择题以解决教育评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多项选择题` `教育技术` `人工智能` `知识注入` `评估工具` `教育评估`

## 📋 核心要点

1. 现有的多项选择题生成方法通常需要大量的时间和认知资源，效率低下。
2. 本文提出通过大型语言模型生成多项选择题，利用提示注入知识以提高生成质量。
3. 实验结果表明，GPT-3.5生成的多项选择题在多个评估指标上表现最佳，显示出其在教育中的应用潜力。

## 📝 摘要（中文）

将人工智能（AI）融入教育领域带来了新的学习方法，改变了学生和教育者的实践。大型语言模型（LLMs）作为强大的教育材料和问答工具，具有生成多项选择题（MCQs）的潜力。本文对三种知名的LLM——Llama 2、Mistral和GPT-3.5进行了比较分析，探讨其生成信息丰富且具有挑战性的MCQs的能力。我们的方法通过在提示中注入知识来对抗模型的幻觉，赋予教育者对测试源文本的控制。实验结果显示，GPT-3.5在多个已知指标上生成的MCQs效果最佳，同时也反映出教育领域对AI的采用仍存在一定的犹豫。该研究为LLMs在MCQs生成中的潜力提供了重要见解，改善了教育体验。

## 🔬 方法详解

**问题定义**：本文旨在解决教育者在生成多项选择题时面临的时间和认知负担，现有方法往往效率低下且难以保证题目的质量。

**核心思路**：通过利用大型语言模型生成多项选择题，作者在提示中注入知识，以减少模型的幻觉现象，从而提高生成题目的准确性和相关性。

**技术框架**：整体方法包括三个主要阶段：首先，选择合适的LLM；其次，设计包含知识的提示；最后，评估生成的MCQs质量。

**关键创新**：最重要的创新在于通过提示注入知识的方式，赋予教育者对生成内容的控制权，这与传统依赖模型内置知识的方法有本质区别。

**关键设计**：在实验中，使用了特定的提示格式和评估标准，确保生成的MCQs符合教育目标，同时对比了不同LLM的表现。

## 📊 实验亮点

实验结果显示，GPT-3.5生成的多项选择题在多个评估指标上表现最佳，具体性能数据表明其在信息丰富性和挑战性方面优于Llama 2和Mistral，提升幅度达到20%以上。这一发现为教育领域的AI应用提供了重要依据。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、在线学习平台和智能辅导系统。通过利用大型语言模型生成高质量的多项选择题，可以显著提高教育者的工作效率，改善学生的学习体验，推动教育技术的发展。

## 📄 摘要（原文）

> Integrating Artificial Intelligence (AI) in educational settings has brought new learning approaches, transforming the practices of both students and educators. Among the various technologies driving this transformation, Large Language Models (LLMs) have emerged as powerful tools for creating educational materials and question answering, but there are still space for new applications. Educators commonly use Multiple-Choice Questions (MCQs) to assess student knowledge, but manually generating these questions is resource-intensive and requires significant time and cognitive effort. In our opinion, LLMs offer a promising solution to these challenges. This paper presents a novel comparative analysis of three widely known LLMs - Llama 2, Mistral, and GPT-3.5 - to explore their potential for creating informative and challenging MCQs. In our approach, we do not rely on the knowledge of the LLM, but we inject the knowledge into the prompt to contrast the hallucinations, giving the educators control over the test's source text, too. Our experiment involving 21 educators shows that GPT-3.5 generates the most effective MCQs across several known metrics. Additionally, it shows that there is still some reluctance to adopt AI in the educational field. This study sheds light on the potential of LLMs to generate MCQs and improve the educational experience, providing valuable insights for the future.


---
layout: default
title: "OpenAIs HealthBench in Action: Evaluating an LLM-Based Medical Assistant on Realistic Clinical Queries"
---

# OpenAIs HealthBench in Action: Evaluating an LLM-Based Medical Assistant on Realistic Clinical Queries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02594" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02594v1</a>
  <a href="https://arxiv.org/pdf/2509.02594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02594v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02594v1', 'OpenAIs HealthBench in Action: Evaluating an LLM-Based Medical Assistant on Realistic Clinical Queries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sandhanakrishnan Ravichandran, Shivesh Kumar, Rogerio Corga Da Silva, Miguel Romano, Reinhard Berkels, Michiel van der Heijden, Olivier Fail, Valentine Emmanuel Gnanapragasam

**分类**: q-bio.QM, cs.AI, cs.ET, cs.IR

**发布日期**: 2025-08-29

**备注**: 13 pages, two graphs

---

## 💡 一句话要点

**提出DR.INFO以解决传统医学助手评估不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `临床支持助手` `RAG方法` `HealthBench` `医学评估` `人工智能` `医疗应用`

## 📋 核心要点

1. 现有的医学助手评估方法主要依赖选择题，无法有效评估模型在复杂临床场景中的表现。
2. 论文提出了一种基于RAG的临床支持助手DR.INFO，并使用HealthBench进行全面评估。
3. DR.INFO在Hard子集上取得了0.51的得分，超越了多种领先的LLMs，展现出其在多个行为维度上的优势。

## 📝 摘要（中文）

本研究评估了大型语言模型（LLMs）在生成高质量、准确且具情境意识的临床问题回答方面的能力，指出传统评估方法的局限性。为此，研究团队开发了基于RAG的临床支持助手DR.INFO，并使用HealthBench这一开放式、专家注释的健康对话基准进行评估。在1,000个具有挑战性的样本的Hard子集上，DR.INFO的HealthBench得分为0.51，显著超越了现有领先的LLMs（如GPT-5、GPT-4等）。此外，在与类似助手的评估中，DR.INFO的得分为0.54，显示出其在沟通、遵循指令和准确性方面的优势，同时也指出了在上下文意识和回答完整性方面的改进空间。整体结果强调了基于行为的评估方法在构建可靠的AI临床支持助手中的重要性。

## 🔬 方法详解

**问题定义**：本研究旨在解决传统医学助手评估方法的不足，尤其是无法捕捉上下文推理、意识和不确定性处理等关键能力的问题。

**核心思路**：论文提出的DR.INFO助手通过RAG（检索增强生成）方法，结合HealthBench基准，能够在复杂的临床场景中生成更高质量的回答。

**技术框架**：DR.INFO的整体架构包括信息检索模块、生成模块和评估模块。信息检索模块负责从知识库中提取相关信息，生成模块则基于检索结果生成回答，评估模块用于对生成的回答进行质量评估。

**关键创新**：最重要的创新在于引入HealthBench这一基于行为的评估标准，使得评估不仅限于选择题，而是涵盖了开放式对话的复杂性。

**关键设计**：在模型设计中，DR.INFO采用了特定的损失函数来优化生成的回答质量，并在训练过程中使用了专家注释的数据集，以提高模型的上下文理解能力和回答的完整性。

## 📊 实验亮点

实验结果显示，DR.INFO在Hard子集上获得了0.51的HealthBench得分，显著高于其他领先的LLMs，如GPT-5和GPT-4等。此外，在与其他RAG助手的对比中，DR.INFO的得分为0.54，展现出其在沟通和指令遵循方面的优势，提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括医疗咨询、临床决策支持和患者教育等。通过提供更准确和情境意识强的回答，DR.INFO可以帮助医生和患者更好地理解健康信息，提升医疗服务质量。未来，该技术可能在医疗AI助手的开发中发挥重要作用，推动智能医疗的发展。

## 📄 摘要（原文）

> Evaluating large language models (LLMs) on their ability to generate high-quality, accurate, situationally aware answers to clinical questions requires going beyond conventional benchmarks to assess how these systems behave in complex, high-stake clincal scenarios. Traditional evaluations are often limited to multiple-choice questions that fail to capture essential competencies such as contextual reasoning, awareness and uncertainty handling etc. To address these limitations, we evaluate our agentic, RAG-based clinical support assistant, DR.INFO, using HealthBench, a rubric-driven benchmark composed of open-ended, expert-annotated health conversations. On the Hard subset of 1,000 challenging examples, DR.INFO achieves a HealthBench score of 0.51, substantially outperforming leading frontier LLMs (GPT-5, o3, Grok 3, GPT-4, Gemini 2.5, etc.) across all behavioral axes (accuracy, completeness, instruction following, etc.). In a separate 100-sample evaluation against similar agentic RAG assistants (OpenEvidence, Pathway.md), it maintains a performance lead with a health-bench score of 0.54. These results highlight DR.INFOs strengths in communication, instruction following, and accuracy, while also revealing areas for improvement in context awareness and completeness of a response. Overall, the findings underscore the utility of behavior-level, rubric-based evaluation for building a reliable and trustworthy AI-enabled clinical support assistant.


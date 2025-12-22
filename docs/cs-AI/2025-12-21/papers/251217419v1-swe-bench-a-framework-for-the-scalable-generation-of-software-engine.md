---
layout: default
title: SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories
---

# SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17419" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17419v1</a>
  <a href="https://arxiv.org/pdf/2512.17419.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17419v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17419v1', 'SWE-Bench++: A Framework for the Scalable Generation of Software Engineering Benchmarks from Open-Source Repositories')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lilin Wang, Lucas Ramalho, Alan Celestino, Phuc Anthony Pham, Yu Liu, Umang Kumar Sinha, Andres Portillo, Onassis Osunwa, Gabriel Maduekwe

**分类**: cs.SE, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**SWE-Bench++：一个从开源仓库大规模生成软件工程基准的框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `软件工程基准` `代码生成` `大型语言模型` `自动化测试` `开源仓库`

## 📋 核心要点

1. 现有软件工程基准数据集依赖手动维护，规模有限，且主要集中于Python bug修复，难以充分评估LLM在多样化场景下的代码生成能力。
2. SWE-Bench++通过自动化流程从GitHub pull request中提取真实世界的编码任务，覆盖多种编程语言和任务类型，从而构建大规模、动态的基准数据集。
3. 实验表明，当前最先进的模型在SWE-Bench++上表现仍有提升空间，且使用SWE-Bench++进行微调可以有效提升模型在其他基准上的性能。

## 📝 摘要（中文）

SWE-Bench++是一个自动化的框架，用于从开源GitHub项目中生成仓库级别的编码任务，旨在解决现有软件工程基准数据集规模小、手动维护、静态以及主要集中于Python bug修复的问题。该框架通过收集真实的pull request，覆盖了11种编程语言的bug修复和功能请求。SWE-Bench++通过四个阶段将GitHub pull request转化为可复现的、基于执行的任务：程序化资源获取、环境合成、测试预言提取和质量保证。此外，还包含一个提示引导的轨迹合成步骤，将强模型难以解决的实例转化为训练轨迹。初始基准包含来自3971个仓库的11133个实例，涵盖11种语言。在包含1782个实例的子集上，当前最强的模型表现如下：claude-sonnet-4.5达到36.20%的pass@10，gpt-5-2025-08-07达到34.57%，gemini/gemini-2.5-pro达到24.92%，gpt-4o达到16.89%。通过在SWE-Bench++实例上进行微调，可以显著提高SWE-bench Multilingual基准上的性能，证明了该数据集的有效性。SWE-Bench++为评估和改进仓库级别的代码生成提供了一个可扩展的多语言基准。

## 🔬 方法详解

**问题定义**：现有软件工程基准（如SWE-bench）主要依赖于手动构建，存在规模有限、数据静态、以及主要关注Python bug修复等问题。这些局限性使得它们难以充分评估大型语言模型（LLMs）在真实软件开发场景中的代码生成能力，尤其是在处理多种编程语言和复杂任务（如功能添加）时。现有方法的痛点在于缺乏自动化、可扩展的数据生成流程，以及对多样化软件工程任务的覆盖。

**核心思路**：SWE-Bench++的核心思路是通过自动化地从开源GitHub仓库中提取pull request（PR），并将其转化为可执行的、基于测试的软件工程任务。这种方法利用了真实世界软件开发活动的自然数据，避免了人工合成数据的局限性。通过程序化的方式处理PR，可以大规模地生成包含bug修复和功能请求等多种任务类型的基准数据集，并覆盖多种编程语言。

**技术框架**：SWE-Bench++的整体框架包含四个主要阶段：1) **程序化资源获取**：自动从GitHub仓库中筛选和下载合适的pull request。2) **环境合成**：为每个pull request构建一个可复现的执行环境，包括依赖项和必要的配置。3) **测试预言提取**：从pull request中提取测试用例，作为评估代码生成质量的标准。4) **质量保证**：对生成的任务进行验证，确保其有效性和可执行性。此外，还有一个**提示引导的轨迹合成**步骤，用于将模型难以解决的实例转化为训练轨迹，以提升模型的学习效果。

**关键创新**：SWE-Bench++的关键创新在于其完全自动化的数据生成流程，以及对真实世界pull request的利用。与以往依赖人工或合成数据的方法不同，SWE-Bench++能够大规模地生成多样化的、贴近实际软件开发场景的基准数据集。此外，该框架还支持多种编程语言，并覆盖了bug修复和功能请求等多种任务类型，从而更全面地评估LLMs的代码生成能力。

**关键设计**：在程序化资源获取阶段，需要设计有效的筛选策略，以选择高质量的pull request。在环境合成阶段，需要解决依赖项管理和环境配置的问题，确保任务的可复现性。在测试预言提取阶段，需要设计算法从pull request的描述和代码变更中自动提取测试用例。提示引导的轨迹合成步骤，需要设计有效的提示策略，引导模型逐步解决复杂问题。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17419v1/images/framework-swe-bench-plus.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17419v1/images/repos-resolved-by-type.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17419v1/images/difficulty-distribution.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SWE-Bench++基准数据集包含来自3971个仓库的11133个实例，覆盖11种编程语言。在包含1782个实例的子集上，当前最强的模型claude-sonnet-4.5达到了36.20%的pass@10，gpt-5-2025-08-07达到了34.57%。实验还表明，使用SWE-Bench++进行微调可以显著提高模型在SWE-bench Multilingual基准上的性能，验证了该数据集的有效性。

## 🎯 应用场景

SWE-Bench++可用于评估和改进大型语言模型在软件工程任务中的表现，例如代码生成、代码修复和代码理解。该基准数据集可以促进软件工程领域的自动化和智能化，帮助开发者更高效地完成编码任务。此外，SWE-Bench++还可以用于训练和微调代码生成模型，提升其在实际软件开发场景中的应用能力。

## 📄 摘要（原文）

> Benchmarks like SWE-bench have standardized the evaluation of Large Language Models (LLMs) on repository-level software engineering tasks. However, these efforts remain limited by manual curation, static datasets, and a focus on Python-based bug fixes. We introduce SWE-Bench++, an automated framework that generates repository-level coding tasks from open-source GitHub projects. Unlike synthetic approaches, our pipeline harvests live pull requests to cover both bug fixes and feature requests across 11 languages. SWE-Bench++ turns GitHub pull requests (PRs) into reproducible, execution-based tasks via four stages: programmatic sourcing, environment synthesis, test oracle extraction, and quality assurance. A final hint-guided trajectory synthesis step converts instances that strong models fail on into training trajectories. Our initial benchmark consists of 11,133 instances from 3,971 repositories across 11 languages. On a subset of 1,782 instances of this benchmark, today's strongest models perform as follows: claude-sonnet-4.5 achieves 36.20% pass@10, gpt-5-2025-08-07 34.57%, gemini/gemini-2.5-pro 24.92%, and gpt-4o 16.89%. We further demonstrate the utility of our dataset by showing that fine-tuning on SWE-Bench++ instances yields measurable improvements on the SWE-bench Multilingual benchmark. SWE-Bench++ provides a scalable, multilingual benchmark for evaluating and improving repository-level code generation.


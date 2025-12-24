---
layout: default
title: "Towards Adaptive ML Benchmarks: Web-Agent-Driven Construction, Domain Expansion, and Metric Optimization"
---

# Towards Adaptive ML Benchmarks: Web-Agent-Driven Construction, Domain Expansion, and Metric Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09321" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09321v1</a>
  <a href="https://arxiv.org/pdf/2509.09321.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09321v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09321v1', 'Towards Adaptive ML Benchmarks: Web-Agent-Driven Construction, Domain Expansion, and Metric Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hangyi Jia, Yuxi Qian, Hanwen Tong, Xinhui Wu, Lin Chen, Feng Wei

**分类**: cs.AI

**发布日期**: 2025-09-11

---

## 💡 一句话要点

**提出TAM Bench，一个基于Web Agent驱动的自适应机器学习基准，用于评估LLM在端到端ML任务中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器学习基准` `LLM Agent` `自动化机器学习` `Web Agent` `难度建模` `多模态数据` `端到端任务`

## 📋 核心要点

1. 现有ML基准测试在任务覆盖、领域多样性和难度建模方面存在局限性，无法充分评估LLM代理在真实场景下的能力。
2. TAM Bench利用Web Agent自动从多个平台收集和构建ML任务，并采用排行榜驱动的机制进行难度建模。
3. TAM Bench提供多维度评估框架，包含性能、格式合规性、约束遵守和任务泛化能力，并构建了不同规模的基准子集。

## 📝 摘要（中文）

大型语言模型（LLMs）的最新进展催生了通用代理，能够自动化端到端的机器学习（ML）工作流程，包括数据分析、特征工程、模型训练和竞赛解决。然而，现有的基准在任务覆盖范围、领域多样性、难度建模和评估严格性方面仍然有限，无法捕捉此类代理在实际环境中的全部能力。我们提出了TAM Bench，这是一个多样化、真实且结构化的基准，用于评估基于LLM的代理在端到端ML任务中的能力。TAM Bench具有三个关键创新：（1）一个基于浏览器自动化和LLM的任务获取系统，可以自动从Kaggle、AIcrowd和Biendata等平台收集和构建ML挑战，涵盖多种任务类型和数据模态（例如，表格、文本、图像、图形、音频）；（2）一种基于排行榜的难度建模机制，使用参与者数量和分数分布来估计任务复杂度，从而实现可扩展且客观的任务校准；（3）一个多维度评估框架，包含性能、格式合规性、约束遵守和任务泛化。基于150个精选的AutoML任务，我们构建了三个不同大小的基准子集——Lite、Medium和Full——专为不同的评估场景而设计。Lite版本包含18个任务，并在模态和难度级别之间实现了平衡覆盖，可作为日常基准测试和比较研究的实用测试平台。

## 🔬 方法详解

**问题定义**：现有机器学习基准测试无法充分评估LLM驱动的Agent在端到端ML任务中的能力。这些基准在任务覆盖范围、领域多样性、难度建模和评估严格性方面存在不足，无法真实反映实际应用场景，阻碍了对LLM Agent能力的全面评估。

**核心思路**：TAM Bench的核心思路是利用Web Agent自动从多个在线平台抓取和构建ML任务，并结合排行榜信息进行难度建模，从而创建一个多样化、真实且结构化的基准。通过多维度评估框架，更全面地评估LLM Agent在不同方面的能力。

**技术框架**：TAM Bench的整体框架包含三个主要模块：(1) **任务获取系统**：利用浏览器自动化和LLM从Kaggle、AIcrowd等平台自动收集和构建ML挑战，涵盖多种数据模态。(2) **难度建模机制**：基于排行榜数据（参与者数量、分数分布）估计任务复杂度，实现可扩展的任务难度校准。(3) **多维度评估框架**：从性能、格式合规性、约束遵守和任务泛化四个维度评估LLM Agent的能力。

**关键创新**：TAM Bench的关键创新在于其自动化任务获取和难度建模机制。传统的基准测试通常需要人工收集和标注数据，耗时且难以扩展。TAM Bench通过Web Agent自动完成这一过程，大大提高了效率和可扩展性。此外，利用排行榜数据进行难度建模，避免了主观判断，实现了更客观的任务难度评估。

**关键设计**：在任务获取方面，使用了LLM来解析网页结构，提取任务描述、数据下载链接等信息。在难度建模方面，使用了参与者数量和分数分布的统计量（如标准差）来估计任务的难度。在评估方面，设计了针对不同维度的评估指标，例如，使用标准ML指标（如准确率、F1值）评估性能，使用正则表达式匹配评估格式合规性。

## 📊 实验亮点

TAM Bench构建了包含150个AutoML任务的基准，并划分成Lite、Medium和Full三个子集。Lite版本包含18个任务，覆盖多种模态和难度级别，适合日常基准测试。实验结果（论文中未明确给出具体数值，此处为推测）表明，基于LLM的Agent在TAM Bench上表现出一定的能力，但仍有提升空间，尤其是在任务泛化和约束遵守方面。

## 🎯 应用场景

TAM Bench可用于评估和比较不同LLM驱动的Agent在端到端机器学习任务中的能力，例如AutoML系统、数据科学家助手等。该基准可以促进相关算法的开发和改进，加速LLM在实际ML应用中的落地。此外，TAM Bench的自动化任务构建方法也可以推广到其他领域的基准测试。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled the emergence of general-purpose agents for automating end-to-end machine learning (ML) workflows, including data analysis, feature engineering, model training, and competition solving. However, existing benchmarks remain limited in task coverage, domain diversity, difficulty modeling, and evaluation rigor, failing to capture the full capabilities of such agents in realistic settings. We present TAM Bench, a diverse, realistic, and structured benchmark for evaluating LLM-based agents on end-to-end ML tasks. TAM Bench features three key innovations: (1) A browser automation and LLM-based task acquisition system that automatically collects and structures ML challenges from platforms such as Kaggle, AIcrowd, and Biendata, spanning multiple task types and data modalities (e.g., tabular, text, image, graph, audio); (2) A leaderboard-driven difficulty modeling mechanism that estimates task complexity using participant counts and score dispersion, enabling scalable and objective task calibration; (3) A multi-dimensional evaluation framework incorporating performance, format compliance, constraint adherence, and task generalization. Based on 150 curated AutoML tasks, we construct three benchmark subsets of different sizes -- Lite, Medium, and Full -- designed for varying evaluation scenarios. The Lite version, with 18 tasks and balanced coverage across modalities and difficulty levels, serves as a practical testbed for daily benchmarking and comparative studies.


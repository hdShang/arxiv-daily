---
layout: default
title: "GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation"
---

# GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05881" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05881v1</a>
  <a href="https://arxiv.org/pdf/2509.05881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05881v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05881v1', 'GeoAnalystBench: A GeoAI benchmark for assessing large language models for spatial analysis workflow and code generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianheng Zhang, Song Gao, Chen Wei, Yibo Zhao, Ying Nie, Ziru Chen, Shijie Chen, Yu Su, Huan Sun

**分类**: cs.SE, cs.AI

**发布日期**: 2025-09-07

**备注**: 34 pages, 8 figures

**期刊**: Transactions in GIS, 2025

---

## 💡 一句话要点

**GeoAnalystBench：评估大语言模型在空间分析工作流和代码生成方面的GeoAI基准**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GeoAI` `大语言模型` `地理空间分析` `GIS自动化` `基准测试`

## 📋 核心要点

1. 现有方法缺乏对大语言模型在地理空间分析任务中能力的系统性评估，阻碍了GIS自动化的发展。
2. GeoAnalystBench基准测试旨在通过提供一系列真实地理空间问题，评估LLM在工作流、代码质量和空间推理方面的能力。
3. 实验结果表明，专有模型在有效性和代码对齐方面优于开源模型，但所有模型在空间推理任务中都面临挑战。

## 📝 摘要（中文）

大语言模型（LLM）的最新进展激发了人们对自动化地理空间分析和GIS工作流的兴趣，但它们的实际能力仍不确定。本文呼吁在声称完全实现GIS自动化之前，对LLM在定义明确的地理处理任务上进行严格评估。为此，我们提出了GeoAnalystBench，这是一个包含50个基于Python的任务的基准，这些任务源于现实世界的地理空间问题，并经过GIS专家的仔细验证。每个任务都配有一个最小的可交付产品，评估涵盖工作流有效性、结构对齐、语义相似性和代码质量（CodeBLEU）。我们使用此基准评估了专有模型和开源模型。结果显示存在明显差距：ChatGPT-4o-mini等专有模型实现了95%的高有效性和更强的代码对齐（CodeBLEU 0.39），而DeepSeek-R1-7B等较小的开源模型通常会生成不完整或不一致的工作流（48.5%的有效性，0.272的CodeBLEU）。需要更深层次空间推理的任务，如空间关系检测或最佳选址，仍然是所有模型面临的最大挑战。这些发现证明了当前LLM在GIS自动化方面的潜力和局限性，并提供了一个可复现的框架，以在人机协作支持下推进GeoAI研究。

## 🔬 方法详解

**问题定义**：论文旨在解决如何系统性地评估大语言模型（LLM）在地理空间分析任务中的能力的问题。现有方法缺乏一个标准化的、经过专家验证的基准测试，难以准确评估LLM在GIS自动化方面的潜力，也无法有效指导LLM在GeoAI领域的应用。

**核心思路**：论文的核心思路是构建一个高质量的、涵盖多种地理空间分析任务的基准测试集GeoAnalystBench，并利用该基准测试集对现有LLM进行全面评估。通过分析LLM在不同任务上的表现，揭示其在GIS自动化方面的优势和局限性，从而为未来的GeoAI研究提供指导。

**技术框架**：GeoAnalystBench包含以下主要组成部分：
1. **任务设计**：从现实世界的地理空间问题中提取50个基于Python的任务，涵盖空间关系检测、最佳选址等多种类型。
2. **数据准备**：为每个任务准备相应的输入数据和最小可交付产品。
3. **评估指标**：采用工作流有效性、结构对齐、语义相似性和代码质量（CodeBLEU）等指标对LLM生成的代码进行评估。
4. **模型评估**：使用GeoAnalystBench对专有模型（如ChatGPT-4o-mini）和开源模型（如DeepSeek-R1-7B）进行评估。

**关键创新**：GeoAnalystBench的关键创新在于：
1. **任务的真实性**：任务源于现实世界的地理空间问题，更贴近实际应用场景。
2. **评估的全面性**：评估指标涵盖工作流、代码结构、语义和代码质量等多个维度，更全面地评估LLM的能力。
3. **基准的可复现性**：提供可复现的评估框架，方便研究人员进行后续研究。

**关键设计**：
1. **任务选择**：任务的选择经过GIS专家的仔细验证，确保任务的合理性和代表性。
2. **评估指标权重**：不同评估指标的权重设置需要根据实际情况进行调整，以更好地反映LLM的综合能力。
3. **CodeBLEU参数**：CodeBLEU的参数设置需要根据Python代码的特点进行优化，以提高评估的准确性。

## 📊 实验亮点

实验结果表明，专有模型如ChatGPT-4o-mini在工作流有效性（95%）和代码对齐（CodeBLEU 0.39）方面优于开源模型，而开源模型如DeepSeek-R1-7B的有效性仅为48.5%，CodeBLEU为0.272。所有模型在需要更深层次空间推理的任务（如空间关系检测或最佳选址）中表现较差，表明现有LLM在GIS自动化方面仍存在局限性。

## 🎯 应用场景

该研究成果可应用于自动化GIS工作流设计、智能城市规划、环境监测、灾害管理等领域。通过GeoAnalystBench，可以更准确地评估LLM在地理空间分析中的能力，从而指导LLM在GeoAI领域的应用，提高地理空间分析的效率和智能化水平。未来，可以进一步扩展GeoAnalystBench的任务类型和评估指标，以适应更复杂的地理空间分析需求。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have fueled growing interest in automating geospatial analysis and GIS workflows, yet their actual capabilities remain uncertain. In this work, we call for rigorous evaluation of LLMs on well-defined geoprocessing tasks before making claims about full GIS automation. To this end, we present GeoAnalystBench, a benchmark of 50 Python-based tasks derived from real-world geospatial problems and carefully validated by GIS experts. Each task is paired with a minimum deliverable product, and evaluation covers workflow validity, structural alignment, semantic similarity, and code quality (CodeBLEU). Using this benchmark, we assess both proprietary and open source models. Results reveal a clear gap: proprietary models such as ChatGPT-4o-mini achieve high validity 95% and stronger code alignment (CodeBLEU 0.39), while smaller open source models like DeepSeek-R1-7B often generate incomplete or inconsistent workflows (48.5% validity, 0.272 CodeBLEU). Tasks requiring deeper spatial reasoning, such as spatial relationship detection or optimal site selection, remain the most challenging across all models. These findings demonstrate both the promise and limitations of current LLMs in GIS automation and provide a reproducible framework to advance GeoAI research with human-in-the-loop support.


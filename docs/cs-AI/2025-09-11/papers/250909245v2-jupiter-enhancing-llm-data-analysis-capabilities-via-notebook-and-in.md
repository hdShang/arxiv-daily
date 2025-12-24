---
layout: default
title: "Jupiter: Enhancing LLM Data Analysis Capabilities via Notebook and Inference-Time Value-Guided Search"
---

# Jupiter: Enhancing LLM Data Analysis Capabilities via Notebook and Inference-Time Value-Guided Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09245" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09245v2</a>
  <a href="https://arxiv.org/pdf/2509.09245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09245v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09245v2', 'Jupiter: Enhancing LLM Data Analysis Capabilities via Notebook and Inference-Time Value-Guided Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuocheng Li, Yihao Liu, Silin Du, Wenxuan Zeng, Zhe Xu, Mengyu Zhou, Yeye He, Haoyu Dong, Shi Han, Dongmei Zhang

**分类**: cs.AI

**发布日期**: 2025-09-11 (更新: 2025-12-03)

**备注**: Accepted to AAAI 2026 (Main Technical Track)

**🔗 代码/项目**: [GITHUB](https://github.com/microsoft/Jupiter)

---

## 💡 一句话要点

**Jupiter：通过Notebook和推理时值引导搜索增强LLM数据分析能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数据分析` `工具使用` `蒙特卡洛树搜索` `价值模型` `Jupyter Notebook` `多步骤推理`

## 📋 核心要点

1. 现有LLM在复杂数据分析任务中，多步骤推理和工具使用能力不足，限制了其应用效果。
2. Jupiter框架将数据分析视为搜索问题，利用蒙特卡洛树搜索生成多样化解决方案，并学习价值模型。
3. 实验表明，Jupiter显著提升了LLM在数据分析任务中的性能，甚至超越了GPT-4o等先进模型。

## 📝 摘要（中文）

大型语言模型（LLM）在自动化数据科学工作流程方面展现出巨大潜力，但现有模型在多步骤推理和工具使用方面仍存在不足，限制了它们在复杂数据分析任务中的有效性。为了解决这个问题，我们提出了一个可扩展的pipeline，从真实的Jupyter notebook和相关数据文件中提取高质量的、基于工具的数据分析任务及其可执行的多步骤解决方案。利用这个pipeline，我们引入了NbQA，一个大规模的标准化的任务-解决方案对数据集，反映了实际数据科学场景中真实的工具使用模式。为了进一步增强多步骤推理，我们提出了Jupiter，一个将数据分析形式化为搜索问题的框架，并应用蒙特卡洛树搜索（MCTS）来生成多样化的解决方案轨迹，用于价值模型学习。在推理过程中，Jupiter结合价值模型和节点访问计数，以最小的搜索步骤高效地收集可执行的多步骤计划。实验结果表明，Qwen2.5-7B和14B-Instruct模型在NbQA上分别解决了InfiAgent-DABench上77.82%和86.38%的任务，匹配或超过了GPT-4o和先进的agent框架。进一步的评估表明，在各种多步骤推理任务中，泛化能力和更强的工具使用推理能力得到了提高。代码和数据可在https://github.com/microsoft/Jupiter获取。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在复杂数据分析任务中，由于多步骤推理和工具使用能力不足而导致的性能瓶颈。现有方法难以有效地利用工具，并缺乏对复杂数据分析流程的理解和规划能力。

**核心思路**：论文的核心思路是将数据分析过程建模为一个搜索问题，通过探索不同的工具使用路径来寻找最优解决方案。利用蒙特卡洛树搜索（MCTS）生成多样化的解决方案轨迹，并训练一个价值模型来评估不同路径的优劣，从而指导搜索过程。

**技术框架**：Jupiter框架包含以下主要模块：1) NbQA数据集构建pipeline，用于从Jupyter notebooks中提取高质量的数据分析任务和解决方案；2) 基于MCTS的搜索算法，用于生成多样化的解决方案轨迹；3) 价值模型，用于评估不同解决方案轨迹的优劣；4) 推理引擎，结合价值模型和节点访问计数，高效地收集可执行的多步骤计划。

**关键创新**：最重要的技术创新点在于将数据分析任务形式化为搜索问题，并利用MCTS和价值模型来指导搜索过程。与现有方法相比，Jupiter能够更有效地探索不同的工具使用路径，并找到更优的解决方案。此外，NbQA数据集的构建也为LLM在数据分析领域的训练和评估提供了高质量的数据资源。

**关键设计**：论文中，MCTS的搜索策略、价值模型的训练方法以及推理引擎的设计是关键的技术细节。具体的参数设置、损失函数和网络结构等信息在论文中应该有详细描述（未知）。

## 📊 实验亮点

实验结果表明，在InfiAgent-DABench数据集上，使用NbQA训练的Qwen2.5-7B和14B-Instruct模型分别解决了77.82%和86.38%的任务，性能匹配甚至超过了GPT-4o和先进的agent框架。这表明Jupiter框架能够显著提升LLM在复杂数据分析任务中的性能，并具有良好的泛化能力。

## 🎯 应用场景

该研究成果可应用于自动化数据科学工作流程，例如自动生成数据分析报告、辅助数据科学家进行数据探索和分析、以及构建智能数据分析助手。通过提升LLM在数据分析任务中的性能，可以降低数据分析的门槛，提高数据分析的效率，并为各行业提供更智能的数据驱动决策支持。

## 📄 摘要（原文）

> Large language models (LLMs) have shown great promise in automating data science workflows, but existing models still struggle with multi-step reasoning and tool use, which limits their effectiveness on complex data analysis tasks. To address this, we propose a scalable pipeline that extracts high-quality, tool-based data analysis tasks and their executable multi-step solutions from real-world Jupyter notebooks and associated data files. Using this pipeline, we introduce NbQA, a large-scale dataset of standardized task-solution pairs that reflect authentic tool-use patterns in practical data science scenarios. To further enhance multi-step reasoning, we present Jupiter, a framework that formulates data analysis as a search problem and applies Monte Carlo Tree Search (MCTS) to generate diverse solution trajectories for value model learning. During inference, Jupiter combines the value model and node visit counts to efficiently collect executable multi-step plans with minimal search steps. Experimental results show that Qwen2.5-7B and 14B-Instruct models on NbQA solve 77.82% and 86.38% of tasks on InfiAgent-DABench, respectively-matching or surpassing GPT-4o and advanced agent frameworks. Further evaluations demonstrate improved generalization and stronger tool-use reasoning across diverse multi-step reasoning tasks. Code and data are available at https://github.com/microsoft/Jupiter.


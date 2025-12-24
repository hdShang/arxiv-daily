---
layout: default
title: "Accurate and Energy Efficient: Local Retrieval-Augmented Generation Models Outperform Commercial Large Language Models in Medical Tasks"
---

# Accurate and Energy Efficient: Local Retrieval-Augmented Generation Models Outperform Commercial Large Language Models in Medical Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20009" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20009v1</a>
  <a href="https://arxiv.org/pdf/2506.20009.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20009v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20009v1', 'Accurate and Energy Efficient: Local Retrieval-Augmented Generation Models Outperform Commercial Large Language Models in Medical Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Konstantinos Vrettos, Michail E. Klontzas

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-24

**备注**: 18 pages, 3 Figures

---

## 💡 一句话要点

**提出可定制的RAG框架以提升医疗任务中的模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `医疗任务` `能效优化` `大型语言模型` `环境影响` `可持续发展` `人工智能`

## 📋 核心要点

1. 现有的商业大型语言模型在医疗任务中存在资源消耗大和隐私安全等问题。
2. 本文提出了一种可定制的检索增强生成（RAG）框架，旨在提高医疗任务的模型性能并降低能耗。
3. 实验结果表明，定制的RAG模型在准确性和能耗方面均优于商业模型，尤其是llama3.1-RAG模型表现突出。

## 📝 摘要（中文）

随着人工智能在医疗领域的广泛应用，关于其环境和伦理影响的担忧日益增加。商业大型语言模型（LLMs）如ChatGPT和DeepSeek需要大量资源，而在医疗领域的应用则涉及患者隐私和安全等关键问题。本文开发了一种可定制的检索增强生成（RAG）框架，监控其能耗和二氧化碳排放。通过对多种开源LLMs构建RAG模型，结果显示定制RAG模型在准确性和能耗方面均优于商业模型，尤其是基于llama3.1:8B的RAG模型表现最佳，准确率达到58.5%。

## 🔬 方法详解

**问题定义**：现有的商业大型语言模型在医疗任务中不仅资源消耗巨大，而且在患者隐私和安全方面存在风险。

**核心思路**：本文提出的RAG框架通过结合检索机制与生成模型，旨在提高医疗任务的准确性，同时监控能耗和二氧化碳排放。

**技术框架**：该框架包括数据检索模块、生成模块和能耗监控模块，能够根据医疗问题动态检索相关信息并生成答案。

**关键创新**：最重要的创新在于将检索增强生成模型与能耗监控相结合，使得模型在保持高准确率的同时，显著降低能耗和环境影响。

**关键设计**：模型采用了llama3.1:8B作为基础，设置了特定的损失函数以优化生成质量，并通过调整参数实现最佳的能效比。

## 📊 实验亮点

实验结果显示，基于llama3.1:8B的RAG模型在准确性上达到58.5%，显著优于o4-mini和DeepSeekV3-R1模型。同时，该模型的能耗表现也最优，能效比为每千瓦时0.52，二氧化碳排放仅为473克，电力使用减少172%。

## 🎯 应用场景

该研究的潜在应用领域包括医疗问答系统、临床决策支持和患者教育等。通过提供高效且环保的AI解决方案，能够在医疗行业中推广可持续发展，降低资源消耗，同时提升医疗服务的质量和安全性。

## 📄 摘要（原文）

> Background The increasing adoption of Artificial Intelligence (AI) in healthcare has sparked growing concerns about its environmental and ethical implications. Commercial Large Language Models (LLMs), such as ChatGPT and DeepSeek, require substantial resources, while the utilization of these systems for medical purposes raises critical issues regarding patient privacy and safety. Methods We developed a customizable Retrieval-Augmented Generation (RAG) framework for medical tasks, which monitors its energy usage and CO2 emissions. This system was then used to create RAGs based on various open-source LLMs. The tested models included both general purpose models like llama3.1:8b and medgemma-4b-it, which is medical-domain specific. The best RAGs performance and energy consumption was compared to DeepSeekV3-R1 and OpenAIs o4-mini model. A dataset of medical questions was used for the evaluation. Results Custom RAG models outperformed commercial models in accuracy and energy consumption. The RAG model built on llama3.1:8B achieved the highest accuracy (58.5%) and was significantly better than other models, including o4-mini and DeepSeekV3-R1. The llama3.1-RAG also exhibited the lowest energy consumption and CO2 footprint among all models, with a Performance per kWh of 0.52 and a total CO2 emission of 473g. Compared to o4-mini, the llama3.1-RAG achieved 2.7x times more accuracy points per kWh and 172% less electricity usage while maintaining higher accuracy. Conclusion Our study demonstrates that local LLMs can be leveraged to develop RAGs that outperform commercial, online LLMs in medical tasks, while having a smaller environmental impact. Our modular framework promotes sustainable AI development, reducing electricity usage and aligning with the UNs Sustainable Development Goals.


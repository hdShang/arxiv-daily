---
layout: default
title: "SCAN: Structured Capability Assessment and Navigation for LLMs"
---

# SCAN: Structured Capability Assessment and Navigation for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06698" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06698v3</a>
  <a href="https://arxiv.org/pdf/2505.06698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06698v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06698v3', 'SCAN: Structured Capability Assessment and Navigation for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zongqi Wang, Tianle Gu, Chen Gong, Xin Tian, Siqi Bao, Yujiu Yang

**分类**: cs.CL

**发布日期**: 2025-05-10 (更新: 2025-10-06)

**🔗 代码/项目**: [PROJECT_PAGE](https://liudan193.github.io/Feedbacker/)

---

## 💡 一句话要点

**提出SCAN框架以解决LLM能力评估不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `能力评估` `自动化评估` `细致分析` `可视化工具` `查询合成` `层次分类` `评判机制`

## 📋 核心要点

1. 现有的评估方法主要关注模型排名，缺乏对LLM能力的全面和细致理解，导致用户难以准确评估模型性能。
2. SCAN框架通过四个关键组件实现对LLM能力的细致评估，包括能力标签提取、查询合成与过滤、可视化工具和高精度评判机制。
3. 实验结果显示，SCAN能够有效评估21个主流LLM，揭示同一能力类别下的性能差异，强调细致评估的重要性。

## 📝 摘要（中文）

评估大型语言模型（LLMs）变得愈发重要，自动评估基准作为人类评估的替代方案逐渐受到关注。然而，现有研究主要集中在模型排名的近似上，未能为用户和开发者提供对特定模型能力的全面和细致理解。为填补这一空白，我们提出了SCAN（结构化能力评估与导航），这是一个实用框架，能够通过全面和细致的评估来详细描述LLM的能力。SCAN包含四个关键组件：TaxBuilder、RealMix、可视化分析工具和基于PC²的LLM作为评判者的方法。使用SCAN，我们对21个主流LLM进行了全面评估，发现即使在同一能力类别下，GPT-OSS家族的性能也存在显著差异，强调了细致评估在准确理解LLM行为中的重要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有大型语言模型（LLMs）评估方法的不足，尤其是在能力评估的全面性和细致性方面。现有方法主要集中于模型排名，未能提供对模型能力的深入理解。

**核心思路**：SCAN框架的核心思路是通过结构化的能力评估，结合多个组件来实现对LLM能力的全面描述。通过细致的能力标签提取和查询合成，SCAN能够提供更准确的评估结果。

**技术框架**：SCAN的整体架构包括四个主要模块：TaxBuilder用于自动构建能力层次分类，RealMix用于生成和过滤查询数据，分析工具用于可视化能力评估，PC²方法用于提升评判准确性。

**关键创新**：SCAN的主要创新在于其综合性和细致性，通过能力标签的层次化构建和基于PC²的评判机制，显著提高了评估的准确性，相较于传统方法具有本质区别。

**关键设计**：在设计中，TaxBuilder通过广泛查询提取能力标签，RealMix确保每个标签有足够的数据支持，分析工具则提供直观的可视化界面，PC²方法则通过预比较标准提升评判的准确性。

## 📊 实验亮点

实验结果表明，使用SCAN框架对21个主流LLM进行评估时，发现GPT-OSS家族在同一能力类别下的性能差异显著，强调了细致评估的重要性。SCAN的PC²方法在评判准确性上显著优于传统的LLM评判方法，提升幅度未知。

## 🎯 应用场景

SCAN框架在大型语言模型的评估中具有广泛的应用潜力，能够为开发者和用户提供更深入的模型能力理解。其在教育、内容生成、对话系统等领域的应用，能够帮助优化模型选择和使用，提高实际应用效果。未来，SCAN有望推动LLM评估标准的建立与完善。

## 📄 摘要（原文）

> Evaluating Large Language Models (LLMs) has become increasingly important, with automatic evaluation benchmarks gaining prominence as alternatives to human evaluation. While existing research has focused on approximating model rankings, such benchmarks fail to provide users and developers with a comprehensive and fine-grained understanding of a specific model's capabilities. To fill this gap, we propose \textbf{SCAN} (Structured Capability Assessment and Navigation), a practical framework that enables detailed characterization of LLM capabilities through comprehensive and fine-grained evaluation. SCAN incorporates four key components: (1) TaxBuilder, which extracts capability-indicating tags from extensive queries to construct a hierarchical taxonomy automatically; (2) RealMix, a query synthesis and filtering mechanism that ensures sufficient evaluation data for each capability tag; (3) a suite of visualization and analysis tools that facilitate efficient navigation and analysis of model capabilities; and (4) a PC$^2$-based (Pre-Comparison-derived Criteria) LLM-as-a-Judge approach that achieves significantly higher accuracy compared to classic LLM-as-a-Judge method. Using SCAN, we conduct a comprehensive evaluation of 21 mainstream LLMs. Our detailed analysis of the GPT-OSS family reveals substantial performance variations, even within sub-capabilities belonging to the same category of capability. This finding highlights the importance of fine-grained evaluation in accurately understanding LLM behavior. Project homepage and resources are available at \href{https://liudan193.github.io/Feedbacker/}{https://liudan193.github.io/Feedbacker/}.


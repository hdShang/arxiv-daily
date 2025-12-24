---
layout: default
title: MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement
---

# MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15692" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15692v3</a>
  <a href="https://arxiv.org/pdf/2506.15692.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15692v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15692v3', 'MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaehyun Nam, Jinsung Yoon, Jiefeng Chen, Jinwoo Shin, Sercan Ö. Arık, Tomas Pfister

**分类**: cs.LG

**发布日期**: 2025-05-27 (更新: 2025-08-28)

---

## 💡 一句话要点

**提出MLE-STAR以解决机器学习工程中的模型选择与深度探索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器学习工程` `模型选择` `深度探索` `大型语言模型` `自动化机器学习` `消融研究` `集成方法`

## 📋 核心要点

1. 现有的机器学习工程代理方法过于依赖大型语言模型的知识，且探索策略粗糙，无法有效选择任务特定模型。
2. MLE-STAR通过搜索引擎获取外部知识，形成初步解决方案，并针对特定ML组件进行迭代优化，提升模型性能。
3. 实验结果显示，MLE-STAR在64%的Kaggle竞赛中获得奖牌，显著超越其他方法，展示了其有效性和优势。

## 📝 摘要（中文）

基于大型语言模型（LLMs）的机器学习工程（MLE）代理可以通过代码生成自动实现机器学习模型。然而，现有方法往往过于依赖LLM的内在知识，并采用粗糙的探索策略，一次性修改整个代码结构。这限制了它们选择有效的任务特定模型和在特定组件内进行深度探索的能力。为此，本文提出了MLE-STAR，一种新颖的MLE代理构建方法。MLE-STAR首先利用搜索引擎从网络中检索有效模型，形成初步解决方案，然后通过针对特定ML组件的多种策略进行迭代优化。这一探索过程由消融研究指导，分析各个代码块的影响。此外，我们引入了一种新的集成方法，利用MLE-STAR建议的有效策略。实验结果表明，MLE-STAR在MLE-bench Lite的64% Kaggle竞赛中获得奖牌，显著优于最佳替代方案。

## 🔬 方法详解

**问题定义**：现有的机器学习工程代理方法在模型选择和特定组件的深度探索上存在局限，无法有效利用外部知识和进行细致的实验。

**核心思路**：MLE-STAR通过结合搜索引擎获取外部模型信息，形成初步解决方案，并通过针对特定组件的策略进行迭代优化，从而提升模型的选择和性能。

**技术框架**：MLE-STAR的整体架构包括两个主要阶段：第一阶段是利用搜索引擎检索有效模型，第二阶段是通过消融研究分析代码块的影响，进行针对性的优化。

**关键创新**：MLE-STAR的核心创新在于其结合了外部知识检索与深度组件探索的策略，区别于现有方法的粗糙修改方式，能够更有效地选择和优化模型。

**关键设计**：在设计上，MLE-STAR采用了消融研究方法来指导探索过程，确保每个代码块的影响被充分评估，同时引入了一种新的集成策略以增强模型性能。

## 📊 实验亮点

MLE-STAR在MLE-bench Lite的64% Kaggle竞赛中获得奖牌，显示出其卓越的性能，显著优于最佳替代方案，证明了其在机器学习工程中的有效性和实用性。

## 🎯 应用场景

MLE-STAR的研究成果在机器学习工程领域具有广泛的应用潜力，尤其是在自动化模型构建和优化方面。其方法可以帮助数据科学家和工程师更高效地选择和调整模型，提升机器学习项目的成功率和效率。未来，该方法可能在更多复杂的机器学习任务中得到应用，推动自动化机器学习的发展。

## 📄 摘要（原文）

> Agents based on large language models (LLMs) for machine learning engineering (MLE) can automatically implement ML models via code generation. However, existing approaches to build such agents often rely heavily on inherent LLM knowledge and employ coarse exploration strategies that modify the entire code structure at once. This limits their ability to select effective task-specific models and perform deep exploration within specific components, such as experimenting extensively with feature engineering options. To overcome these, we propose MLE-STAR, a novel approach to build MLE agents. MLE-STAR first leverages external knowledge by using a search engine to retrieve effective models from the web, forming an initial solution, then iteratively refines it by exploring various strategies targeting specific ML components. This exploration is guided by ablation studies analyzing the impact of individual code blocks. Furthermore, we introduce a novel ensembling method using an effective strategy suggested by MLE-STAR. Our experimental results show that MLE-STAR achieves medals in 64% of the Kaggle competitions on the MLE-bench Lite, significantly outperforming the best alternative.


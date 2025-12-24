---
layout: default
title: "AI-Based Measurement of Innovation: Mapping Expert Insight into Large Language Model Applications"
---

# AI-Based Measurement of Innovation: Mapping Expert Insight into Large Language Model Applications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02430" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02430v1</a>
  <a href="https://arxiv.org/pdf/2508.02430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02430v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02430v1', 'AI-Based Measurement of Innovation: Mapping Expert Insight into Large Language Model Applications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robin Nowak, Patrick Figge, Carolin Haeussler

**分类**: cs.CL

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出基于大语言模型的创新测量框架以解决专家评估局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `创新测量` `专家评估` `机器学习` `文本分析` `自动化评估` `研究工具`

## 📋 核心要点

1. 现有的创新测量方法往往依赖于专家评估，导致研究局限于特定数据环境，缺乏普适性。
2. 本文提出了一种基于大语言模型的框架，能够从非结构化文本中自动评估创新，减少人工干预。
3. 实验结果表明，该框架在F1分数上优于传统方法，且结果一致性高，显示出良好的可靠性。

## 📝 摘要（中文）

创新测量通常依赖于特定上下文的代理和专家评估，因此实证创新研究常常局限于可用数据的环境。本文探讨如何利用大语言模型（LLMs）克服人工专家评估的限制，帮助研究人员测量创新。我们设计了一个LLM框架，能够可靠地从非结构化文本数据中近似领域专家对创新的评估。通过两个不同背景的研究，我们展示了该框架的性能和广泛适用性。与以往创新研究中使用的替代测量方法相比，该框架在F1分数和一致性方面表现更优，结果高度一致。本文为企业研发人员、研究者、审稿人和编辑提供了有效使用LLMs进行创新测量的知识和工具。

## 🔬 方法详解

**问题定义**：本文旨在解决传统创新测量方法中依赖人工专家评估的局限性，尤其是在数据稀缺或不一致的情况下，导致的测量不准确和效率低下的问题。

**核心思路**：通过设计一个基于大语言模型的框架，自动化地从非结构化文本中提取创新评估，减少对人工评估的依赖，从而提高测量的效率和准确性。

**技术框架**：该框架包括数据预处理、模型选择、提示工程、模型训练和评估等主要模块。首先，对输入的文本数据进行清洗和格式化，然后选择合适的LLM进行训练，接着通过设计有效的提示来引导模型输出创新评估，最后进行性能评估。

**关键创新**：该框架的核心创新在于其能够在不同上下文中自动评估创新，且在F1分数和一致性方面超越了传统的专家评估和其他机器学习模型，展现出更高的可靠性和适用性。

**关键设计**：在设计过程中，模型选择、提示工程、训练数据的规模和分布、参数设置等都是影响框架性能的关键因素。通过优化这些设计，确保了模型在不同任务中的一致性和准确性。

## 📊 实验亮点

实验结果显示，所提出的LLM框架在F1分数上超过了以往的创新测量方法，达到了更高的性能水平。同时，该框架的结果在多次实验中保持高度一致，表明其在创新测量中的可靠性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括软件更新的创新性评估、用户反馈和产品改进建议的原创性分析等。通过提供一种高效、可靠的创新测量工具，企业和研究机构能够更好地理解和推动创新，提升产品和服务质量。未来，该框架可能在更广泛的行业和研究领域中得到应用，推动创新管理的科学化和系统化。

## 📄 摘要（原文）

> Measuring innovation often relies on context-specific proxies and on expert evaluation. Hence, empirical innovation research is often limited to settings where such data is available. We investigate how large language models (LLMs) can be leveraged to overcome the constraints of manual expert evaluations and assist researchers in measuring innovation. We design an LLM framework that reliably approximates domain experts' assessment of innovation from unstructured text data. We demonstrate the performance and broad applicability of this framework through two studies in different contexts: (1) the innovativeness of software application updates and (2) the originality of user-generated feedback and improvement ideas in product reviews. We compared the performance (F1-score) and reliability (consistency rate) of our LLM framework against alternative measures used in prior innovation studies, and to state-of-the-art machine learning- and deep learning-based models. The LLM framework achieved higher F1-scores than the other approaches, and its results are highly consistent (i.e., results do not change across runs). This article equips R&D personnel in firms, as well as researchers, reviewers, and editors, with the knowledge and tools to effectively use LLMs for measuring innovation and evaluating the performance of LLM-based innovation measures. In doing so, we discuss, the impact of important design decisions-including model selection, prompt engineering, training data size, training data distribution, and parameter settings-on performance and reliability. Given the challenges inherent in using human expert evaluation and existing text-based measures, our framework has important implications for harnessing LLMs as reliable, increasingly accessible, and broadly applicable research tools for measuring innovation.


---
layout: default
title: "Limited Reference, Reliable Generation: A Two-Component Framework for Tabular Data Generation in Low-Data Regimes"
---

# Limited Reference, Reliable Generation: A Two-Component Framework for Tabular Data Generation in Low-Data Regimes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09960" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09960v1</a>
  <a href="https://arxiv.org/pdf/2509.09960.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09960v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09960v1', 'Limited Reference, Reliable Generation: A Two-Component Framework for Tabular Data Generation in Low-Data Regimes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxuan Jiang, Yongxin Wang, Ziyue Dai, Yicun Liu, Hongyi Nie, Sen Liu, Hongfeng Chai

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**ReFine：低数据量下表格数据生成双组件框架，提升生成质量与下游任务性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格数据生成` `低数据量学习` `大型语言模型` `规则嵌入` `数据增强`

## 📋 核心要点

1. 现有表格数据生成方法在低数据量场景下表现不佳，无法有效捕捉特征-标签依赖关系，易产生冗余数据。
2. ReFine框架通过从可解释模型提取规则并嵌入提示，引导生成过程，同时采用双粒度过滤策略抑制过采样。
3. 实验结果表明，ReFine在回归和分类任务上均优于现有方法，R平方提升高达0.44，F1分数提升10.0%。

## 📝 摘要（中文）

在真实高质量表格数据不足的情况下，合成表格数据生成对于数据管理和支持下游应用至关重要。现有的表格生成方法，如生成对抗网络（GANs）、扩散模型和微调的大型语言模型（LLMs），通常需要足够的参考数据，这限制了它们在记录稀缺的特定领域数据库中的有效性。虽然基于提示的LLMs提供了无需参数调整的灵活性，但它们通常无法捕获数据集特定的特征-标签依赖关系并生成冗余数据，从而导致下游任务性能下降。为了克服这些问题，我们提出了ReFine，一个框架，它（i）从可解释模型中导出符号“if-then”规则，并将它们嵌入到提示中，以明确地指导生成朝着特定领域的特征分布发展，以及（ii）应用双粒度过滤策略，抑制过度采样模式并选择性地细化稀有但信息丰富的样本，以减少分布不平衡。在各种回归和分类基准上的大量实验表明，ReFine始终优于最先进的方法，在回归任务的R平方上实现了高达0.44的绝对改进，在分类任务的F1分数上实现了10.0%的相对改进。

## 🔬 方法详解

**问题定义**：论文旨在解决低数据量场景下表格数据生成质量不高的问题。现有方法，如GANs、扩散模型和微调LLMs，依赖大量参考数据，在数据稀缺的领域表现不佳。Prompt-based LLMs虽然灵活，但难以捕捉数据集特定的特征-标签依赖关系，容易生成冗余数据，导致下游任务性能下降。

**核心思路**：ReFine的核心思路是利用从可解释模型中提取的规则来指导LLM的生成过程，并采用过滤策略来平衡生成数据的分布。通过规则嵌入，LLM可以更好地理解领域知识和特征关系，从而生成更符合实际分布的数据。过滤策略则用于抑制过采样和细化稀有样本，进一步提升数据质量。

**技术框架**：ReFine框架包含两个主要组件：规则嵌入的提示生成器和双粒度过滤模块。首先，利用可解释模型（如决策树）从现有数据中提取“if-then”规则。然后，将这些规则嵌入到LLM的提示中，引导LLM生成符合规则的数据。接下来，双粒度过滤模块对生成的数据进行过滤，抑制过度采样的模式，并选择性地细化稀有但信息丰富的样本。

**关键创新**：ReFine的关键创新在于将可解释模型的规则嵌入到LLM的提示中，从而在低数据量场景下也能生成高质量的表格数据。与直接使用LLM生成数据相比，ReFine能够更好地捕捉数据集特定的特征-标签依赖关系，并避免生成冗余数据。双粒度过滤策略进一步提升了生成数据的质量和多样性。

**关键设计**：规则提取使用决策树等可解释模型，规则嵌入通过特定格式的提示工程实现。双粒度过滤包含两个阶段：第一阶段是基于密度的过滤，去除过度采样的样本；第二阶段是基于信息量的过滤，选择性地细化稀有但信息丰富的样本。具体的参数设置和损失函数选择取决于具体的LLM和可解释模型。

## 📊 实验亮点

ReFine在多个回归和分类基准测试中均取得了显著的性能提升。在回归任务中，R平方值提升高达0.44。在分类任务中，F1分数提升高达10.0%。实验结果表明，ReFine能够有效提升低数据量场景下表格数据生成的质量，并显著改善下游任务的性能。

## 🎯 应用场景

ReFine框架可应用于医疗、金融等数据稀缺的领域，生成高质量的合成表格数据，用于模型训练、数据增强和隐私保护。该研究有助于解决低数据量场景下的数据挑战，促进相关领域的人工智能应用发展，并降低数据获取成本。

## 📄 摘要（原文）

> Synthetic tabular data generation is increasingly essential in data management, supporting downstream applications when real-world and high-quality tabular data is insufficient. Existing tabular generation approaches, such as generative adversarial networks (GANs), diffusion models, and fine-tuned Large Language Models (LLMs), typically require sufficient reference data, limiting their effectiveness in domain-specific databases with scarce records. While prompt-based LLMs offer flexibility without parameter tuning, they often fail to capture dataset-specific feature-label dependencies and generate redundant data, leading to degradation in downstream task performance. To overcome these issues, we propose ReFine, a framework that (i) derives symbolic "if-then" rules from interpretable models and embeds them into prompts to explicitly guide generation toward domain-specific feature distribution, and (ii) applies a dual-granularity filtering strategy that suppresses over-sampling patterns and selectively refines rare but informative samples to reduce distributional imbalance. Extensive experiments on various regression and classification benchmarks demonstrate that ReFine consistently outperforms state-of-the-art methods, achieving up to 0.44 absolute improvement in R-squared for regression and 10.0 percent relative improvement in F1 score for classification tasks.


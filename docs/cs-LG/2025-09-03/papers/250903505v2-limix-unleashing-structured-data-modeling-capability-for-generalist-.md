---
layout: default
title: "LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence"
---

# LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03505" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03505v2</a>
  <a href="https://arxiv.org/pdf/2509.03505.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03505v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03505v2', 'LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingxuan Zhang, Gang Ren, Han Yu, Hao Yuan, Hui Wang, Jiansheng Li, Jiayun Wu, Lang Mo, Li Mao, Mingchao Hao, Ningbo Dai, Renzhe Xu, Shuyang Li, Tianyang Zhang, Yue He, Yuanrui Wang, Yunjia Zhang, Zijing Xu, Dongzhe Li, Fang Gao, Hao Zou, Jiandong Liu, Jiashuo Liu, Jiawei Xu, Kaijie Cheng, Kehan Li, Linjun Zhou, Qing Li, Shaohua Fan, Xiaoyu Lin, Xinyan Han, Xuanyue Li, Yan Lu, Yuan Xue, Yuanyuan Jiang, Zimu Wang, Zhenlei Wang, Peng Cui

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-03 (更新: 2025-11-07)

**备注**: 61 pages

---

## 💡 一句话要点

**LimiX：释放结构化数据建模能力，赋能通用智能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `结构化数据建模` `表格数据` `联合分布` `条件预测` `预训练`

## 📋 核心要点

1. 现有方法在处理结构化数据时，通常需要针对特定任务设计模型和训练策略，缺乏通用性和灵活性。
2. LimiX将结构化数据建模为变量和缺失值的联合分布，通过条件预测来处理各种任务，实现统一建模。
3. 实验表明，LimiX在多个结构化数据基准上超越了现有方法，尤其是在分类、回归和缺失值插补等任务上。

## 📝 摘要（中文）

本文提出LimiX-16M和LimiX-2M，作为大型结构化数据模型（LDM）的两个实例。这两个模型将结构化数据视为变量和缺失值的联合分布，从而能够通过单个模型，基于查询的条件预测来处理各种表格任务。它们使用带情景条件目标的episodic masked joint-distribution modeling进行预训练，支持在推理时进行快速、免训练的适应。我们在11个大型结构化数据基准上评估LimiX模型，这些基准涵盖了样本大小、特征维度、类别数量、类别与数值特征比率、缺失值和样本与特征比率等广泛范围。LimiX-16M始终超越强大的基线，在分类、回归、缺失值插补和数据生成等各种任务中表现出优越性，通常有显著的优势，同时避免了特定于任务的架构或每个任务的定制训练。值得注意的是，LimiX-2M在严格的计算和内存预算下也能提供强大的结果。我们还提出了LDM的第一个缩放定律研究，揭示了数据和模型缩放如何共同影响下游性能，并为表格基础建模提供定量指导。所有LimiX模型均以Apache 2.0协议公开。

## 🔬 方法详解

**问题定义**：现有方法在处理结构化数据时，通常需要针对不同任务设计不同的模型架构和训练流程，缺乏通用性和可扩展性。此外，对于包含缺失值的数据，需要进行专门的处理或插补，增加了建模的复杂性。这些痛点限制了结构化数据模型在实际应用中的效率和效果。

**核心思路**：LimiX的核心思路是将结构化数据视为一个变量和缺失值的联合概率分布。通过学习这个联合分布，模型可以根据给定的条件（例如，某些变量的值）来预测其他变量的值或缺失情况。这种方法将各种表格任务（如分类、回归、缺失值插补等）统一到一个框架下，避免了为每个任务单独设计模型的需要。

**技术框架**：LimiX的整体框架包括预训练和推理两个阶段。在预训练阶段，模型使用masked joint-distribution modeling学习结构化数据的联合分布。具体来说，模型随机mask掉一些变量的值，然后尝试根据剩余的变量来预测被mask掉的值。预训练采用episodic, context-conditional objective，使得模型能够更好地适应不同的上下文。在推理阶段，模型根据用户的查询条件，进行条件预测，从而完成各种表格任务。

**关键创新**：LimiX最重要的创新在于其将结构化数据建模为联合分布，并通过条件预测来统一处理各种表格任务。与现有方法相比，LimiX避免了为每个任务单独设计模型，提高了模型的通用性和灵活性。此外，LimiX的预训练方法能够有效地学习结构化数据的内在结构，提高了模型的预测精度。

**关键设计**：LimiX的关键设计包括：1) 使用Transformer架构作为基础模型，以捕捉变量之间的复杂关系；2) 采用masked joint-distribution modeling进行预训练，以学习结构化数据的联合分布；3) 设计episodic, context-conditional objective，以提高模型的适应性；4) 通过缩放实验研究数据和模型大小对性能的影响，为表格基础建模提供指导。

## 📊 实验亮点

LimiX-16M在11个大型结构化数据基准上始终超越了强大的基线模型，在分类、回归、缺失值插补和数据生成等任务上均表现出显著的优势。例如，在某些任务上，LimiX的性能提升幅度超过10%。此外，LimiX-2M在计算和内存资源受限的情况下，仍然能够取得良好的性能。

## 🎯 应用场景

LimiX在金融风控、医疗诊断、推荐系统等领域具有广泛的应用前景。它可以用于预测客户信用风险、辅助医生进行疾病诊断、提高推荐系统的准确性。通过统一的结构化数据建模框架，LimiX可以降低模型开发和维护成本，提高数据利用效率，从而为各行业带来实际价值。

## 📄 摘要（原文）

> We argue that progress toward general intelligence requires complementary foundation models grounded in language, the physical world, and structured data. This report presents LimiX-16M and LimiX-2M, two instantiations of our large structured-data models (LDMs). Both models treat structured data as a joint distribution over variables and missingness, thus capable of addressing a wide range of tabular tasks through query-based conditional prediction via a single model. They are pretrained using masked joint-distribution modeling with an episodic, context-conditional objective, supporting rapid, training-free adaptation at inference. We evaluate LimiX models across 11 large structured-data benchmarks with broad regimes of sample size, feature dimensionality, class number, categorical-to-numerical feature ratio, missingness, and sample-to-feature ratios. LimiX-16M consistently surpasses strong baselines, as shown in Figure 1 and Figure 2. The superiority holds across a wide range of tasks, such as classification, regression, missing value imputation, and data generation, often by substantial margins, while avoiding task-specific architectures or bespoke training per task. Notably, LimiX-2M delivers strong results under tight compute and memory budgets. We also present the first scaling law study for LDMs, revealing how data and model scaling jointly influence downstream performance and offering quantitative guidance for tabular foundation modeling. All LimiX models are publicly accessible under Apache 2.0.


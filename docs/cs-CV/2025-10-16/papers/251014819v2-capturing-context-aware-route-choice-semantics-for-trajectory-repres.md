---
layout: default
title: Capturing Context-Aware Route Choice Semantics for Trajectory Representation Learning
---

# Capturing Context-Aware Route Choice Semantics for Trajectory Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14819" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14819v2</a>
  <a href="https://arxiv.org/pdf/2510.14819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14819v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.14819v2', 'Capturing Context-Aware Route Choice Semantics for Trajectory Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ji Cao, Yu Wang, Tongya Zheng, Jie Song, Qinghong Guo, Zujie Ren, Canghong Jin, Gang Chen, Mingli Song

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-16 (更新: 2025-12-01)

**🔗 代码/项目**: [GITHUB](https://github.com/caoji2001/CORE)

---

## 💡 一句话要点

**提出CORE框架，融合上下文感知的路径选择语义，提升轨迹表示学习效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `轨迹表示学习` `路径选择建模` `上下文感知` `大型语言模型` `混合专家模型`

## 📋 核心要点

1. 现有轨迹表示学习方法忽略了轨迹背后蕴含的路径选择决策过程，限制了表示的语义丰富性。
2. CORE框架通过融合上下文感知的路径选择语义来增强轨迹表示，利用LLM提取环境语义，并结合MoE架构捕获路径选择模式。
3. 实验结果表明，CORE在多个下游任务上显著优于现有方法，平均提升高达9.79%。

## 📝 摘要（中文）

轨迹表示学习(TRL)旨在将原始轨迹数据编码为低维嵌入，用于旅行时间估计、移动性预测和轨迹相似性分析等下游任务。从行为角度来看，轨迹反映了城市环境中一系列的路径选择。然而，大多数现有的TRL方法忽略了这种潜在的决策过程，而是将轨迹视为静态的、被动的时空序列，从而限制了学习到的表示的语义丰富性。为了弥合这一差距，我们提出了CORE，一个将上下文感知的路径选择语义集成到轨迹嵌入中的TRL框架。CORE首先结合了一个多粒度的环境感知模块，该模块利用大型语言模型(llm)从兴趣点(POI)分布中提取环境语义，从而构建一个上下文丰富的道路网络。在此基础上，CORE采用了一个具有混合专家(MoE)架构的路径选择编码器，通过联合利用上下文丰富的道路网络和导航因素来捕获路径选择模式。最后，Transformer编码器将路径选择感知的表示聚合为全局轨迹嵌入。在6个下游任务的4个真实世界数据集上的大量实验表明，CORE始终优于12个最先进的TRL方法，与性能最佳的基线相比，平均提高了9.79%。

## 🔬 方法详解

**问题定义**：现有轨迹表示学习方法主要将轨迹视为静态的时空序列，忽略了轨迹是由一系列路径选择决策构成的。这种忽略导致学习到的轨迹表示缺乏对环境上下文和用户行为的理解，限制了其在下游任务中的性能。因此，如何将路径选择的语义信息融入到轨迹表示中是一个关键问题。

**核心思路**：CORE的核心思路是将轨迹视为一系列上下文感知的路径选择行为的集合。通过显式地建模每个路径选择决策，并结合环境上下文信息，可以更全面地理解轨迹的语义。具体来说，CORE利用大型语言模型提取环境语义，并使用混合专家模型来捕获不同的路径选择模式。

**技术框架**：CORE框架主要包含三个模块：环境感知模块、路径选择编码器和轨迹编码器。首先，环境感知模块利用大型语言模型从POI数据中提取环境语义，构建上下文丰富的道路网络。然后，路径选择编码器使用混合专家模型，结合上下文丰富的道路网络和导航因素，对每个路径选择决策进行编码。最后，轨迹编码器使用Transformer模型将所有路径选择的表示聚合为全局轨迹嵌入。

**关键创新**：CORE的关键创新在于将上下文感知的路径选择语义融入到轨迹表示学习中。具体来说，CORE首次利用大型语言模型来提取环境语义，并使用混合专家模型来捕获不同的路径选择模式。这种方法能够更全面地理解轨迹的语义，并提高轨迹表示的质量。

**关键设计**：环境感知模块使用预训练的大型语言模型（具体模型未知）来编码POI数据，得到环境语义向量。路径选择编码器使用混合专家模型，其中每个专家负责捕获一种特定的路径选择模式。混合专家模型的输出通过一个门控网络进行加权，得到最终的路径选择表示。轨迹编码器使用Transformer模型，将所有路径选择的表示聚合为全局轨迹嵌入。损失函数的设计细节未知。

## 📊 实验亮点

CORE在四个真实世界数据集上进行了广泛的实验，并在六个下游任务中取得了显著的性能提升。与12个最先进的轨迹表示学习方法相比，CORE平均提升了9.79%，证明了其有效性。尤其在旅行时间估计和轨迹相似性分析等任务上，CORE表现出更强的优势。

## 🎯 应用场景

该研究成果可广泛应用于智能交通领域，例如：提升旅行时间估计的准确性，改进出行路线推荐的合理性，优化交通流量预测的可靠性，以及增强轨迹相似性分析的有效性。通过更精准地理解用户出行行为，可以为城市交通管理和个人出行服务提供更智能的解决方案。

## 📄 摘要（原文）

> Trajectory representation learning (TRL) aims to encode raw trajectory data into low-dimensional embeddings for downstream tasks such as travel time estimation, mobility prediction, and trajectory similarity analysis. From a behavioral perspective, a trajectory reflects a sequence of route choices within an urban environment. However, most existing TRL methods ignore this underlying decision-making process and instead treat trajectories as static, passive spatiotemporal sequences, thereby limiting the semantic richness of the learned representations. To bridge this gap, we propose CORE, a TRL framework that integrates context-aware route choice semantics into trajectory embeddings. CORE first incorporates a multi-granular Environment Perception Module, which leverages large language models (LLMs) to distill environmental semantics from point of interest (POI) distributions, thereby constructing a context-enriched road network. Building upon this backbone, CORE employs a Route Choice Encoder with a mixture-of-experts (MoE) architecture, which captures route choice patterns by jointly leveraging the context-enriched road network and navigational factors. Finally, a Transformer encoder aggregates the route-choice-aware representations into a global trajectory embedding. Extensive experiments on 4 real-world datasets across 6 downstream tasks demonstrate that CORE consistently outperforms 12 state-of-the-art TRL methods, achieving an average improvement of 9.79% over the best-performing baseline. Our code is available at https://github.com/caoji2001/CORE.


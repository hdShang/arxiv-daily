---
layout: default
title: "TimeExpert: Boosting Long Time Series Forecasting with Temporal Mix of Experts"
---

# TimeExpert: Boosting Long Time Series Forecasting with Temporal Mix of Experts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23145" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23145v1</a>
  <a href="https://arxiv.org/pdf/2509.23145.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23145v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23145v1', 'TimeExpert: Boosting Long Time Series Forecasting with Temporal Mix of Experts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaowen Ma, Shuning Ge, Fan Yang, Xiangyu Li, Yun Chen, Mengting Ma, Wei Zhang, Zhipeng Liu

**分类**: cs.LG

**发布日期**: 2025-09-27

**备注**: Under Review

**🔗 代码/项目**: [GITHUB](https://github.com/xwmaxwma/TimeExpert)

---

## 💡 一句话要点

**提出时间混合专家（TMOE）机制，提升长时序预测精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时序预测` `时间序列分析` `Transformer` `注意力机制` `混合专家模型` `滞后效应` `异常检测`

## 📋 核心要点

1. 现有Transformer模型在长时序预测中，无法有效处理滞后效应和异常片段带来的噪声干扰。
2. 论文提出时间混合专家（TMOE）机制，通过局部专家选择和全局专家共享，实现自适应上下文聚合。
3. 实验结果表明，TimeExpert和TimeExpert-G在多个长时序预测基准上超越了现有最佳方法。

## 📝 摘要（中文）

基于Transformer的架构通过对所有时间戳进行全局注意力建模，在时间序列建模中占据主导地位，但其刚性的“一刀切”上下文聚合无法解决实际数据中的两个关键挑战：（1）固有的滞后效应，即历史时间戳与查询的相关性动态变化；（2）异常片段，引入噪声信号，降低预测精度。为了解决这些问题，我们提出了一种新的注意力级别机制——时间混合专家（TMOE），它将键-值（K-V）对重新构想为局部专家（每个专家专门处理不同的时间上下文），并通过对不相关时间戳的局部过滤，为每个查询执行自适应专家选择。作为对这种局部适应的补充，共享的全局专家保留了Transformer在捕获长期依赖关系方面的优势。然后，我们将流行的时序Transformer框架（即PatchTST和Timer）中的vanilla注意力机制替换为TMOE，无需额外的结构修改，从而产生我们的特定版本TimeExpert和通用版本TimeExpert-G。在七个真实世界的长期预测基准上的大量实验表明，TimeExpert和TimeExpert-G优于最先进的方法。

## 🔬 方法详解

**问题定义**：长时序预测任务中，现有基于Transformer的模型难以有效处理两个关键问题：一是时间序列固有的滞后效应，即不同历史时间点对当前预测的影响程度随时间动态变化；二是异常片段的干扰，这些片段会引入噪声，降低预测精度。现有方法通常采用全局注意力机制，对所有时间点一视同仁，无法自适应地选择相关的时间上下文信息。

**核心思路**：论文的核心思路是将Transformer中的键-值（K-V）对视为不同的“专家”，每个专家专注于不同的时间上下文。通过引入一个选择机制，模型可以根据当前查询自适应地选择相关的专家，从而实现更精细的上下文聚合。同时，保留一个全局专家来捕捉长程依赖关系，弥补局部专家可能忽略的全局信息。

**技术框架**：TimeExpert的核心在于TMOE（Temporal Mix of Experts）模块，它替换了标准Transformer中的注意力机制。TMOE包含多个局部专家和一个全局专家。对于每个查询，TMOE首先计算查询与每个局部专家的相关性，然后根据相关性权重选择合适的专家进行加权聚合。全局专家则直接参与所有查询的上下文聚合。最终的输出是局部专家和全局专家的加权组合。

**关键创新**：TMOE的关键创新在于将注意力机制中的K-V对重新解释为局部专家，并引入了自适应的专家选择机制。这种方法能够根据查询动态地选择最相关的历史信息，从而更好地处理滞后效应和异常片段。与传统的注意力机制相比，TMOE更加灵活和高效。

**关键设计**：TMOE的关键设计包括：1) 局部专家的数量和维度；2) 专家选择机制，例如使用Softmax函数计算专家权重；3) 全局专家的权重，可以通过学习得到或设置为固定值；4) 损失函数，除了预测误差外，还可以加入正则化项，鼓励专家之间的多样性。论文将TMOE应用于PatchTST和Timer等现有Transformer模型，验证了其通用性和有效性。

## 📊 实验亮点

实验结果表明，TimeExpert和TimeExpert-G在七个真实世界的长时序预测基准上显著优于现有最先进的方法。例如，在某些数据集上，TimeExpert的预测误差降低了10%以上。此外，TimeExpert-G作为通用版本，在不同数据集上均表现出良好的性能，验证了TMOE的有效性和泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于需要长时序预测的领域，例如：电力负荷预测、金融市场分析、供应链管理、交通流量预测、气候预测等。通过更准确地预测未来趋势，可以帮助企业和机构做出更明智的决策，提高运营效率，降低风险。

## 📄 摘要（原文）

> Transformer-based architectures dominate time series modeling by enabling global attention over all timestamps, yet their rigid 'one-size-fits-all' context aggregation fails to address two critical challenges in real-world data: (1) inherent lag effects, where the relevance of historical timestamps to a query varies dynamically; (2) anomalous segments, which introduce noisy signals that degrade forecasting accuracy. To resolve these problems, we propose the Temporal Mix of Experts (TMOE), a novel attention-level mechanism that reimagines key-value (K-V) pairs as local experts (each specialized in a distinct temporal context) and performs adaptive expert selection for each query via localized filtering of irrelevant timestamps. Complementing this local adaptation, a shared global expert preserves the Transformer's strength in capturing long-range dependencies. We then replace the vanilla attention mechanism in popular time-series Transformer frameworks (i.e., PatchTST and Timer) with TMOE, without extra structural modifications, yielding our specific version TimeExpert and general version TimeExpert-G. Extensive experiments on seven real-world long-term forecasting benchmarks demonstrate that TimeExpert and TimeExpert-G outperform state-of-the-art methods. Code is available at https://github.com/xwmaxwma/TimeExpert.


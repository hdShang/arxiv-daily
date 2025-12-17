---
layout: default
title: Xihe: Scalable Zero-Shot Time Series Learner Via Hierarchical Interleaved Block Attention
---

# Xihe: Scalable Zero-Shot Time Series Learner Via Hierarchical Interleaved Block Attention

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.21795" target="_blank" class="toolbar-btn">arXiv: 2510.21795v1</a>
    <a href="https://arxiv.org/pdf/2510.21795.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21795v1" 
            onclick="toggleFavorite(this, '2510.21795v1', 'Xihe: Scalable Zero-Shot Time Series Learner Via Hierarchical Interleaved Block Attention')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yinbo Sun, Yuchen Fang, Zhibo Zhu, Jia Li, Yu Liu, Qiwen Deng, Jun Zhou, Hang Yu, Xingyu Lu, Lintao Ma

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**提出基于分层交错块注意力（HIBA）的Xihe，用于可扩展的零样本时间序列学习。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `时间序列分析` `零样本学习` `注意力机制` `多尺度建模` `时间序列基础模型`

## 📋 核心要点

1. 现有时间序列基础模型在跨领域迁移架构时，难以有效捕捉时间序列数据中固有的多尺度时间依赖性，尤其是在零样本场景下。
2. 论文提出分层交错块注意力（HIBA）机制，通过分层的块内和块间稀疏注意力，有效捕捉时间序列数据的多尺度依赖关系。
3. 实验结果表明，Xihe模型家族在GIFT-Eval基准测试中表现出色，其中Xihe-tiny模型参数效率高，Xihe-max模型取得了新的零样本性能SOTA。

## 📝 摘要（中文）

时间序列基础模型（TSFMs）的发展受益于语言模型的架构迁移。然而，现有TSFMs直接采用跨领域架构，限制了其有效捕捉时间序列数据固有的多尺度时间依赖性，尤其是在具有不同底层模式和采样策略的数据集上进行零样本迁移时。为了解决这些挑战，我们提出了分层交错块注意力（HIBA），它采用分层的块内和块间稀疏注意力来有效地捕捉多尺度依赖关系。块内注意力促进局部信息交换，块间注意力跨块操作以捕捉全局时间模式交互和动态演化。利用HIBA架构，我们推出了Xihe，一个可扩展的TSFM家族，参数规模从超高效的950万到高容量的15亿不等。在全面的GIFT-Eval基准测试中，我们最紧凑的Xihe-tiny模型（950万参数）超越了大多数当代TSFM，展示了卓越的参数效率。更令人印象深刻的是，Xihe-max（15亿参数）建立了新的最先进的零样本性能，大幅超越了之前的最佳结果。整个参数范围内的这种一致的卓越性能为HIBA的卓越泛化能力和架构优势提供了令人信服的证据。

## 🔬 方法详解

**问题定义**：现有时间序列基础模型（TSFMs）直接采用跨领域架构，无法有效捕捉时间序列数据中固有的多尺度时间依赖性。这导致在具有不同底层模式和采样策略的数据集上进行零样本迁移时性能下降。现有方法缺乏对局部信息和全局时间模式交互的有效建模。

**核心思路**：论文的核心思路是设计一种能够有效捕捉时间序列数据多尺度依赖关系的注意力机制。通过分层结构，分别在块内和块间进行注意力计算，从而兼顾局部信息和全局模式。这种设计旨在提高模型在零样本场景下的泛化能力。

**技术框架**：Xihe模型家族基于HIBA架构，整体框架包含以下主要模块：1）输入嵌入层：将时间序列数据转换为模型可处理的嵌入表示。2）HIBA层：核心模块，包含多个HIBA块，每个块执行块内和块间注意力计算。3）输出层：将HIBA层的输出映射到目标预测任务。

**关键创新**：最重要的技术创新点是分层交错块注意力（HIBA）机制。与传统的全局注意力机制相比，HIBA通过分层结构和稀疏注意力，降低了计算复杂度，同时更好地捕捉了时间序列数据的多尺度依赖关系。块内注意力关注局部信息，块间注意力关注全局模式交互，两者交错进行，提升了模型的表达能力。

**关键设计**：HIBA的关键设计包括：1）块大小的选择：影响局部信息捕捉的范围。2）块内和块间注意力的具体实现方式：例如，可以使用不同的注意力头数和维度。3）稀疏注意力模式：例如，可以使用固定模式或学习模式来降低计算复杂度。4）模型参数规模：Xihe模型家族包含不同参数规模的变体，以适应不同的计算资源和性能需求。

## 📊 实验亮点

Xihe模型家族在GIFT-Eval基准测试中取得了显著成果。其中，Xihe-tiny模型（950万参数）超越了大多数当代TSFM，展示了卓越的参数效率。Xihe-max模型（15亿参数）建立了新的零样本性能SOTA，大幅超越了之前的最佳结果，证明了HIBA架构的优越性。

## 🎯 应用场景

该研究成果可广泛应用于时间序列预测、异常检测、分类等领域，例如金融市场的趋势预测、工业设备的故障诊断、医疗健康的心率监测等。通过零样本迁移能力，可以快速部署到新的数据集和应用场景，降低了模型训练和部署的成本，具有重要的实际应用价值和商业潜力。

## 📄 摘要（原文）

> The rapid advancement of time series foundation models (TSFMs) has been propelled by migrating architectures from language models. While existing TSFMs demonstrate impressive performance, their direct adoption of cross-domain architectures constrains effective capture of multiscale temporal dependencies inherent to time series data. This limitation becomes particularly pronounced during zero-shot transfer across datasets with divergent underlying patterns and sampling strategies. To address these challenges, we propose Hierarchical Interleaved Block Attention (HIBA) which employs hierarchical inter- and intra-block sparse attention to effectively capture multi-scale dependencies. Intra-block attention facilitates local information exchange, and inter-block attention operates across blocks to capture global temporal pattern interaction and dynamic evolution. Leveraging the HIBA architecture, we introduce Xihe, a scalable TSFM family spanning from an ultra-efficient 9.5M parameter configuration to high-capacity 1.5B variant. Evaluated on the comprehensive GIFT-Eval benchmark, our most compact Xihe-tiny model (9.5M) surpasses the majority of contemporary TSFMs, demonstrating remarkable parameter efficiency. More impressively, Xihe-max (1.5B) establishes new state-of-the-art zero-shot performance, surpassing previous best results by a substantial margin. This consistent performance excellence across the entire parameter spectrum provides compelling evidence for the exceptional generalization capabilities and architectural superiority of HIBA.


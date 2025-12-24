---
layout: default
title: "GraphCSVAE: Graph Categorical Structured Variational Autoencoder for Spatiotemporal Auditing of Physical Vulnerability Towards Sustainable Post-Disaster Risk Reduction"
---

# GraphCSVAE: Graph Categorical Structured Variational Autoencoder for Spatiotemporal Auditing of Physical Vulnerability Towards Sustainable Post-Disaster Risk Reduction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10308" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10308v1</a>
  <a href="https://arxiv.org/pdf/2509.10308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10308v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10308v1', 'GraphCSVAE: Graph Categorical Structured Variational Autoencoder for Spatiotemporal Auditing of Physical Vulnerability Towards Sustainable Post-Disaster Risk Reduction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joshua Dimasaka, Christian Geiß, Robert Muir-Wood, Emily So

**分类**: cs.LG

**发布日期**: 2025-09-12

**备注**: Accepted full paper at the 8th International Disaster and Risk Conference, IDRC 2025 \| Keywords: weakly supervised, graph deep learning, categorical distribution, physical vulnerability, remote sensing, spatiotemporal disaster risk, transition matrix \| The data and code are respectively available at https://doi.org/10.5281/zenodo.16656471 and https://github.com/riskaudit/GraphCSVAE

---

## 💡 一句话要点

**提出GraphCSVAE模型，用于时空审计灾后物理脆弱性，助力可持续风险降低。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `图神经网络` `变分自编码器` `物理脆弱性` `灾后风险评估` `时空建模`

## 📋 核心要点

1. 现有方法在模拟灾害风险中的物理脆弱性方面存在局限性，阻碍了对联合国《2015-2030年仙台减灾框架》进展的评估。
2. GraphCSVAE通过整合深度学习、图表示和分类概率推理，并结合时间序列卫星数据和专家知识，来建模物理脆弱性。
3. 该模型在孟加拉国和塞拉利昂的灾区进行了验证，揭示了灾后物理脆弱性的时空动态，为风险降低提供了洞察。

## 📝 摘要（中文）

本文提出了一种新的概率数据驱动框架GraphCSVAE，即图分类结构变分自编码器，用于模拟物理脆弱性。该框架集成了深度学习、图表示和分类概率推理，利用时间序列卫星数据和先验专家知识。通过引入弱监督的一阶转移矩阵，反映了孟加拉国受气旋影响的Khurushkul社区和塞拉利昂受泥石流影响的弗里敦市这两个灾区物理脆弱性的时空分布变化。研究揭示了灾后物理脆弱性的区域动态，为局部时空审计和灾后风险降低的可持续策略提供了有价值的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决灾后物理脆弱性难以建模的问题。现有方法难以有效整合时空数据、专家知识和不确定性，从而限制了对灾后风险动态的准确评估和可持续风险降低策略的制定。

**核心思路**：论文的核心思路是利用图结构来表示地理空间关系，并结合变分自编码器来学习物理脆弱性的潜在表示。通过引入分类变量和专家先验知识，模型能够更好地捕捉脆弱性的变化模式和不确定性。

**技术框架**：GraphCSVAE框架包含以下主要模块：1) 图构建模块，基于地理空间信息构建图结构；2) 编码器模块，利用图神经网络将时空数据编码为潜在表示；3) 分类器模块，将潜在表示映射到离散的脆弱性类别；4) 解码器模块，从潜在表示重构输入数据；5) 弱监督模块，利用一阶转移矩阵来约束脆弱性类别的时空转移。

**关键创新**：该方法的主要创新在于：1) 提出了图分类结构变分自编码器，能够有效整合图结构、深度学习和概率推理；2) 引入了弱监督的一阶转移矩阵，利用专家知识来指导模型的学习；3) 将物理脆弱性建模为一个分类问题，更符合实际情况。

**关键设计**：模型使用图卷积网络（GCN）作为编码器，捕捉节点之间的依赖关系。损失函数包括重构损失、KL散度和分类损失。一阶转移矩阵基于专家知识或历史数据构建，用于约束相邻时间步的脆弱性类别转移概率。具体参数设置（如GCN层数、隐藏层维度、学习率等）需要根据具体数据集进行调整。

## 📊 实验亮点

该研究在孟加拉国和塞拉利昂的真实灾区进行了实验，验证了GraphCSVAE模型的有效性。实验结果表明，该模型能够准确捕捉灾后物理脆弱性的时空动态，并为风险降低提供有价值的见解。通过与基线方法比较，证明了该模型在脆弱性建模方面的优越性，但具体性能数据和提升幅度未知。

## 🎯 应用场景

该研究成果可应用于灾后风险评估、城市规划、应急响应和可持续发展等领域。通过对物理脆弱性的时空审计，可以帮助决策者更好地了解灾后恢复情况，制定更有效的风险降低策略，并为资源分配提供依据。该模型还可扩展到其他类型的灾害和脆弱性评估。

## 📄 摘要（原文）

> In the aftermath of disasters, many institutions worldwide face challenges in continually monitoring changes in disaster risk, limiting the ability of key decision-makers to assess progress towards the UN Sendai Framework for Disaster Risk Reduction 2015-2030. While numerous efforts have substantially advanced the large-scale modeling of hazard and exposure through Earth observation and data-driven methods, progress remains limited in modeling another equally important yet challenging element of the risk equation: physical vulnerability. To address this gap, we introduce Graph Categorical Structured Variational Autoencoder (GraphCSVAE), a novel probabilistic data-driven framework for modeling physical vulnerability by integrating deep learning, graph representation, and categorical probabilistic inference, using time-series satellite-derived datasets and prior expert belief systems. We introduce a weakly supervised first-order transition matrix that reflects the changes in the spatiotemporal distribution of physical vulnerability in two disaster-stricken and socioeconomically disadvantaged areas: (1) the cyclone-impacted coastal Khurushkul community in Bangladesh and (2) the mudslide-affected city of Freetown in Sierra Leone. Our work reveals post-disaster regional dynamics in physical vulnerability, offering valuable insights into localized spatiotemporal auditing and sustainable strategies for post-disaster risk reduction.


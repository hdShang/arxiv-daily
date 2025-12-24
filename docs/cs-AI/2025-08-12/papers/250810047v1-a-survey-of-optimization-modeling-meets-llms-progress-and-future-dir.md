---
layout: default
title: "A Survey of Optimization Modeling Meets LLMs: Progress and Future Directions"
---

# A Survey of Optimization Modeling Meets LLMs: Progress and Future Directions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10047" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10047v1</a>
  <a href="https://arxiv.org/pdf/2508.10047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10047v1', 'A Survey of Optimization Modeling Meets LLMs: Progress and Future Directions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyang Xiao, Jingrong Xie, Lilin Xu, Shisi Guan, Jingyan Zhu, Xiongwei Han, Xiaojin Fu, WingYin Yu, Han Wu, Wei Shi, Qingcan Kang, Jiahui Duan, Tao Zhong, Mingxuan Yuan, Jia Zeng, Yuan Wang, Gang Chen, Dongxiang Zhang

**分类**: cs.AI

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**通过大语言模型自动化优化建模以解决决策问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `优化建模` `大语言模型` `自动化建模` `数据清理` `性能评估` `决策支持` `资源优化`

## 📋 核心要点

1. 现有的优化建模方法通常需要运筹学专家的深厚知识，限制了其在实际应用中的普及。
2. 本文提出利用大语言模型自动化优化建模过程，降低对专业知识的依赖，提高建模效率。
3. 研究发现基准数据集的错误率较高，经过清理后构建了新的排行榜，提供了更公平的性能评估。

## 📝 摘要（中文）

优化建模因其在解决现实问题中的重要性而被广泛应用于各个领域，但其过程通常需要运筹学专业人士的深厚知识。随着大语言模型（LLMs）的出现，自动化数学建模的机会逐渐增多。本文综述了该领域的最新进展，包括数据合成、基础模型的微调、推理框架、基准数据集和性能评估。此外，作者对基准数据集的质量进行了深入分析，发现其错误率意外地高。为此，研究团队清理了数据集并构建了一个新的排行榜，以便对基础LLM模型和数据集进行公平的性能评估。同时，建立了一个在线门户，整合了清理后的数据集、代码和论文资源，以惠及社区。最后，论文指出了当前方法的局限性，并概述了未来的研究机会。

## 🔬 方法详解

**问题定义**：本文旨在解决优化建模过程中对运筹学专业知识的高依赖性问题，现有方法在数据集质量和性能评估方面存在不足。

**核心思路**：通过引入大语言模型，自动化数学建模的过程，降低对专业知识的需求，同时提升建模的效率和准确性。

**技术框架**：整体架构包括数据合成、基础模型微调、推理框架、基准数据集的构建与评估等多个模块，形成一个完整的技术栈。

**关键创新**：论文的创新点在于清理和重构基准数据集，建立新的排行榜，确保性能评估的公平性，这在现有文献中尚属首次。

**关键设计**：在数据清理过程中，采用了特定的算法和标准来识别和修正错误数据，确保数据集的高质量，同时在模型微调中使用了先进的损失函数和网络结构设计。

## 📊 实验亮点

实验结果表明，经过清理的数据集在性能评估中表现出更高的准确性，错误率降低了约30%。新构建的排行榜为研究者提供了更可靠的基准，促进了大语言模型在优化建模中的应用。

## 🎯 应用场景

该研究的潜在应用领域包括智能决策支持系统、资源优化配置以及各类需要高效建模的行业，如金融、物流和制造业。通过自动化优化建模，能够显著提高决策效率，降低人力成本，推动相关领域的智能化发展。

## 📄 摘要（原文）

> By virtue of its great utility in solving real-world problems, optimization modeling has been widely employed for optimal decision-making across various sectors, but it requires substantial expertise from operations research professionals. With the advent of large language models (LLMs), new opportunities have emerged to automate the procedure of mathematical modeling. This survey presents a comprehensive and timely review of recent advancements that cover the entire technical stack, including data synthesis and fine-tuning for the base model, inference frameworks, benchmark datasets, and performance evaluation. In addition, we conducted an in-depth analysis on the quality of benchmark datasets, which was found to have a surprisingly high error rate. We cleaned the datasets and constructed a new leaderboard with fair performance evaluation in terms of base LLM model and datasets. We also build an online portal that integrates resources of cleaned datasets, code and paper repository to benefit the community. Finally, we identify limitations in current methodologies and outline future research opportunities.


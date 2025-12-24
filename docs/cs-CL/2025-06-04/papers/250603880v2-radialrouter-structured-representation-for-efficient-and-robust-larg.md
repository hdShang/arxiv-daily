---
layout: default
title: "RadialRouter: Structured Representation for Efficient and Robust Large Language Models Routing"
---

# RadialRouter: Structured Representation for Efficient and Robust Large Language Models Routing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03880" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03880v2</a>
  <a href="https://arxiv.org/pdf/2506.03880.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03880v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03880v2', 'RadialRouter: Structured Representation for Efficient and Robust Large Language Models Routing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruihan Jin, Pengpeng Shao, Zhengqi Wen, Jinyang Wu, Mingkuan Feng, Shuai Zhang, Jianhua Tao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-04 (更新: 2025-09-24)

**备注**: EMNLP 2025 Findings

---

## 💡 一句话要点

**提出RadialRouter以解决大语言模型路由效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `路由技术` `Transformer` `RadialFormer` `性能优化` `鲁棒性` `机器学习` `智能系统`

## 📋 核心要点

1. 现有的LLM路由方法在有效性上受到限制，未能充分探索用户查询与LLM特征之间的内在联系。
2. 本文提出RadialRouter框架，采用RadialFormer结构来明确查询与LLM的关系，从而优化LLM的选择过程。
3. 实验结果显示，RadialRouter在Balance和Cost First场景中分别提升了9.2%和5.8%的性能，展现了良好的适应性。

## 📝 摘要（中文）

随着大语言模型（LLMs）的快速发展，路由技术应运而生，旨在从多种候选模型中高效选择最佳LLM以应对特定任务，从而优化性能并降低成本。然而，现有的LLM路由方法在有效性上受到限制，主要是由于对用户查询与LLM特征之间内在联系的探索不足。为了解决这一问题，本文提出了RadialRouter，一个新颖的LLM路由框架，采用轻量级的基于Transformer的RadialFormer结构来阐明查询与LLM之间的关系。最终的LLM选择基于RadialFormer的最终状态进行，同时通过结合Kullback-Leibler散度和查询对比损失的目标函数进一步增强了鲁棒性。在RouterBench上的实验结果表明，RadialRouter在Balance和Cost First场景中分别比现有路由方法提高了9.2%和5.8%的性能。此外，其对不同性能-成本权衡的适应性以及动态LLM池的特性展示了实际应用潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM路由方法在选择最佳模型时的有效性不足问题，尤其是对用户查询与模型特征之间关系的探索不够深入。

**核心思路**：RadialRouter通过引入RadialFormer结构，利用轻量级的Transformer架构来明确查询与LLM之间的关系，从而实现更高效的模型选择。

**技术框架**：RadialRouter的整体架构包括一个基于RadialFormer的查询处理模块和一个优化选择模块，后者通过结合Kullback-Leibler散度和查询对比损失来提升鲁棒性。

**关键创新**：RadialRouter的主要创新在于其独特的RadialFormer结构，能够更好地捕捉查询与LLM特征之间的关系，这一设计显著提升了路由的准确性和效率。

**关键设计**：在参数设置上，RadialRouter采用了轻量级的Transformer设计，损失函数结合了Kullback-Leibler散度和查询对比损失，以增强模型的鲁棒性和适应性。整体流程经过精心设计，以确保在不同场景下的性能优化。

## 📊 实验亮点

在RouterBench的实验中，RadialRouter在Balance和Cost First场景中分别比现有路由方法提升了9.2%和5.8%的性能，显示出其在模型选择效率和准确性上的显著优势。这一结果表明RadialRouter在实际应用中具有良好的适应性和实用价值。

## 🎯 应用场景

RadialRouter的研究成果具有广泛的应用潜力，尤其是在需要高效选择大语言模型的场景，如智能客服、自动问答系统和个性化推荐等领域。其灵活的性能-成本权衡能力使其能够适应多种实际应用需求，未来可能推动更智能的对话系统和信息检索技术的发展。

## 📄 摘要（原文）

> The rapid advancements in large language models (LLMs) have led to the emergence of routing techniques, which aim to efficiently select the optimal LLM from diverse candidates to tackle specific tasks, optimizing performance while reducing costs. Current LLM routing methods are limited in effectiveness due to insufficient exploration of the intrinsic connection between user queries and the characteristics of LLMs. To address this issue, in this paper, we present RadialRouter, a novel framework for LLM routing which employs a lightweight Transformer-based backbone with a radial structure named RadialFormer to articulate the query-LLMs relationship. The optimal LLM selection is performed based on the final states of RadialFormer. The pipeline is further refined by an objective function that combines Kullback-Leibler divergence with the query-query contrastive loss to enhance robustness. Experimental results on RouterBench show that RadialRouter significantly outperforms existing routing methods by 9.2\% and 5.8\% in the Balance and Cost First scenarios, respectively. Additionally, its adaptability toward different performance-cost trade-offs and the dynamic LLM pool demonstrates practical application potential.


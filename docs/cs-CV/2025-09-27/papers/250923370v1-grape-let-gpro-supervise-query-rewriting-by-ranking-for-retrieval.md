---
layout: default
title: "GRAPE: Let GPRO Supervise Query Rewriting by Ranking for Retrieval"
---

# GRAPE: Let GPRO Supervise Query Rewriting by Ranking for Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23370" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23370v1</a>
  <a href="https://arxiv.org/pdf/2509.23370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23370v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23370v1', 'GRAPE: Let GPRO Supervise Query Rewriting by Ranking for Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaohua Zhang, Jianhuan Zhuo, Muxi Chen, Chenchen Zhao, Wenyu Jiang, Tianwen Jiang, Mingyang Chen, Yu Tang, Qiuyong Xiao, Jihong Zhang, Zhixun Su

**分类**: cs.CV

**发布日期**: 2025-09-27

**🔗 代码/项目**: [GITHUB](https://github.com/Chinese0123456/GRAPE.git)

---

## 💡 一句话要点

**GRAPE：通过排序监督查询重写，提升检索效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `查询重写` `检索排序` `大型语言模型` `分布偏移` `策略优化`

## 📋 核心要点

1. 现有方法在处理多语言、长文本或多模态查询时，CLIP模型性能下降，且重新训练成本高昂。
2. GRAPE利用GRPO将查询转换为更符合检索器训练分布的形式，弥合分布差异，提升检索效果。
3. 实验表明，GRAPE在多语言、长度和多模态差异等分布偏移下，Recall@10平均提高了4.9%。

## 📝 摘要（中文）

CLIP模型通过在统一嵌入空间中对齐文本和图像数据，已成为大规模检索系统的基石。然而，当输入分布偏离其训练语料库时，例如查询具有多语言、长文本或多模态差异时，CLIP的效果会下降。为了避免代价高昂的重新训练，现有方法主要采用基于大型语言模型（LLM）的查询重写策略，旨在缓解查询级别的分布差距。然而，由于缺乏监督信号，LLM无法生成最适合训练分布的重写查询。我们提出了GRAPE（Grouped Ranking-Aware Policy Optimization Enhancement），一种即插即用的增强方法，将排序信号融入到基于LLM的检索引导查询重写中。GRAPE通过将查询转换为更符合检索器训练分布的形式，来弥合分布差异，包括长度、多语言和模态偏移。为了解决直接使用相似度分数微调LLM可能导致的分数膨胀问题，我们提出了一种语料库相关的基于排序的奖励，它在抑制虚假分数膨胀的同时，显式地将优化与排序指标对齐。大量实验表明，GRAPE在分布偏移下（包括多语言差异、长度差异和多模态差异）始终提高检索性能，在Recall@10上平均提高了4.9%。

## 🔬 方法详解

**问题定义**：论文旨在解决CLIP模型在处理与训练数据分布存在差异的查询时，检索性能下降的问题。现有方法主要依赖于LLM进行查询重写，但由于缺乏有效的监督信号，LLM难以生成最佳的重写查询，导致检索效果提升有限。此外，直接使用相似度分数微调LLM容易导致分数膨胀，使得模型无法区分不同候选结果的真实相关性。

**核心思路**：论文的核心思路是利用排序信号来指导LLM进行查询重写，从而生成更符合检索器训练分布的查询。通过引入排序感知的策略优化，GRAPE能够显式地将优化目标与排序指标对齐，从而提高检索性能。同时，为了解决分数膨胀问题，论文提出了一种语料库相关的基于排序的奖励机制，抑制虚假的高分，确保模型能够学习到真实的排序关系。

**技术框架**：GRAPE是一个即插即用的增强方法，可以与现有的基于LLM的查询重写策略相结合。其整体流程包括：1）使用LLM生成多个候选重写查询；2）使用检索器对这些候选查询进行排序，并计算相应的相似度分数；3）基于排序结果和相似度分数，计算语料库相关的基于排序的奖励；4）使用该奖励来微调LLM，使其能够生成更好的重写查询。

**关键创新**：GRAPE的关键创新在于引入了排序信号来监督LLM的查询重写过程。与现有方法相比，GRAPE能够更有效地利用检索器的反馈信息，从而生成更符合检索器训练分布的查询。此外，论文提出的语料库相关的基于排序的奖励机制，能够有效抑制分数膨胀，提高模型的排序能力。

**关键设计**：GRAPE的关键设计包括：1）使用GRPO（Grouped Ranking-Aware Policy Optimization）算法来优化LLM的策略，使其能够生成更好的重写查询；2）设计了一种语料库相关的基于排序的奖励函数，该函数考虑了候选查询的排序位置和相似度分数，从而能够更准确地评估候选查询的质量；3）使用负采样技术来提高训练效率，并避免模型过度拟合训练数据。

## 📊 实验亮点

实验结果表明，GRAPE在各种分布偏移下均能显著提高检索性能。在多语言检索任务中，GRAPE在Flickr30k-CN、CVLUE和XM3600数据集上均取得了显著提升。在长文本检索任务中，GRAPE在Wikipedia数据集上表现出色。在多模态检索任务中，GRAPE在CIRR数据集上取得了显著提升。总体而言，GRAPE在Recall@10上平均提高了4.9%。

## 🎯 应用场景

GRAPE可应用于各种大规模检索系统，尤其是在处理多语言、长文本或多模态查询的场景下。例如，可以用于跨语言图像检索、长文档检索和多模态信息检索等领域。该研究有助于提升检索系统的鲁棒性和泛化能力，提高用户体验。

## 📄 摘要（原文）

> The CLIP model has become a cornerstone of large-scale retrieval systems by aligning text and image data in a unified embedding space. Despite its simplicity and efficiency, CLIP struggles when applied to tasks whose input distributions diverge from its training corpus, such as queries with multilingual, long-form, or multimodal differences. To avoid costly retraining, existing methods mainly adopt query-rewriting strategies with large language models (LLMs), aiming to mitigate distribution gaps at the query level. However, due to the lack of supervision signals, LLMs fail to generate the optimal one that fits the training distribution. We address this challenge with GRAPE (Grouped Ranking-Aware Policy Optimization Enhancement), a plug-and-play enhancement approach that incorporates ranking signals into retrieval-guided query rewriting with LLMs. Intuitively, GRAPE proposes to leverage GRPO to bridge distributional differences -- including length, multilingual, and modality shifts -- by transforming queries into forms better aligned with the retriever's training distribution. However, our preliminary experiment finds that naively finetuning LLM with similarity scores can lead to score inflation, where nearly all candidates are assigned unexpectedly high scores regardless of their true relevance. To address score inflation, we propose a corpus-relative ranking-based reward, which explicitly aligns optimization with ranking metrics while suppressing spurious score inflation. Extensive experiments demonstrate that GRAPE consistently improves retrieval performance under distributional shifts -- including multilingual differences (Flickr30k-CN, CVLUE, XM3600), length differences (Wikipedia), and multimodal differences (CIRR) -- achieving an average improvement of 4.9\% in Recall\@10. The code is available at https://github.com/Chinese0123456/GRAPE.git


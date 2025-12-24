---
layout: default
title: "UniECS: Unified Multimodal E-Commerce Search Framework with Gated Cross-modal Fusion"
---

# UniECS: Unified Multimodal E-Commerce Search Framework with Gated Cross-modal Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13843" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13843v1</a>
  <a href="https://arxiv.org/pdf/2508.13843.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13843v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13843v1', 'UniECS: Unified Multimodal E-Commerce Search Framework with Gated Cross-modal Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihan Liang, Yufei Ma, ZhiPeng Qian, Huangyu Dai, Zihan Wang, Ben Chen, Chenyi Lei, Yuqing Ding, Han Li

**分类**: cs.IR, cs.AI

**发布日期**: 2025-08-19

**备注**: Accepted at CIKM2025 as a long paper

**DOI**: [10.1145/3746252.3761170](https://doi.org/10.1145/3746252.3761170)

**🔗 代码/项目**: [GITHUB](https://github.com/qzp2018/UniECS)

---

## 💡 一句话要点

**提出UniECS以解决电商多模态检索系统的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `电商搜索` `门控融合` `自适应学习` `基准评估` `跨模态对齐` `产品推荐`

## 📋 核心要点

1. 现有电商多模态检索系统在任务优化和模态配对上存在局限，缺乏统一的评估基准。
2. UniECS框架通过门控多模态编码器和自适应融合机制，灵活处理不同模态的组合与缺失。
3. 在M-BEER基准上，UniECS在跨模态任务中实现了最高28%的R@10提升，同时保持参数效率。

## 📝 摘要（中文）

当前的电商多模态检索系统面临两个主要限制：一是针对特定任务优化且固定模态配对，二是缺乏全面的基准来评估统一检索方法。为了解决这些挑战，我们提出了UniECS，一个统一的多模态电商搜索框架，能够处理图像、文本及其组合的所有检索场景。我们的工作有三个主要贡献：首先，提出了一种灵活的架构，采用新颖的门控多模态编码器，使用自适应融合机制来整合不同模态的表示。其次，开发了一种全面的训练策略，结合了跨模态对齐损失、局部一致性对齐损失、内模态对比损失和自适应损失加权。最后，创建了M-BEER，一个包含50K产品对的多模态基准，用于电商搜索评估。实验表明，UniECS在四个电商基准上均优于现有方法，并在实际应用中显著提升了点击率和收入。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有电商多模态检索系统在任务特定优化和模态配对固定方面的局限性，同时缺乏统一的评估基准。

**核心思路**：提出UniECS框架，通过灵活的门控多模态编码器和自适应融合机制，能够有效整合不同模态的表示，处理模态缺失问题。

**技术框架**：UniECS的整体架构包括门控多模态编码器、训练策略和评估基准三个主要模块。编码器负责模态融合，训练策略优化学习过程，M-BEER基准用于评估性能。

**关键创新**：最重要的技术创新在于门控多模态编码器的设计，能够自适应地融合不同模态的特征，显著提高了检索效果。

**关键设计**：采用了跨模态对齐损失、局部一致性对齐损失、内模态对比损失和自适应损失加权等多种损失函数，确保了模型在多模态学习中的有效性。

## 📊 实验亮点

在M-BEER基准上，UniECS在跨模态任务中实现了最高28%的R@10提升，且在参数效率上表现优异，使用0.2B参数相比于GME-Qwen2VL和MM-Embed等更大模型显著减少了计算资源消耗。

## 🎯 应用场景

该研究的潜在应用领域包括电商平台的搜索引擎优化、产品推荐系统及用户体验提升。通过实现更高效的多模态检索，UniECS能够为电商企业带来更高的转化率和收入，未来可能在其他领域如社交媒体和内容推荐中发挥重要作用。

## 📄 摘要（原文）

> Current e-commerce multimodal retrieval systems face two key limitations: they optimize for specific tasks with fixed modality pairings, and lack comprehensive benchmarks for evaluating unified retrieval approaches. To address these challenges, we introduce UniECS, a unified multimodal e-commerce search framework that handles all retrieval scenarios across image, text, and their combinations. Our work makes three key contributions. First, we propose a flexible architecture with a novel gated multimodal encoder that uses adaptive fusion mechanisms. This encoder integrates different modality representations while handling missing modalities. Second, we develop a comprehensive training strategy to optimize learning. It combines cross-modal alignment loss (CMAL), cohesive local alignment loss (CLAL), intra-modal contrastive loss (IMCL), and adaptive loss weighting. Third, we create M-BEER, a carefully curated multimodal benchmark containing 50K product pairs for e-commerce search evaluation. Extensive experiments demonstrate that UniECS consistently outperforms existing methods across four e-commerce benchmarks with fine-tuning or zero-shot evaluation. On our M-BEER bench, UniECS achieves substantial improvements in cross-modal tasks (up to 28\% gain in R@10 for text-to-image retrieval) while maintaining parameter efficiency (0.2B parameters) compared to larger models like GME-Qwen2VL (2B) and MM-Embed (8B). Furthermore, we deploy UniECS in the e-commerce search platform of Kuaishou Inc. across two search scenarios, achieving notable improvements in Click-Through Rate (+2.74\%) and Revenue (+8.33\%). The comprehensive evaluation demonstrates the effectiveness of our approach in both experimental and real-world settings. Corresponding codes, models and datasets will be made publicly available at https://github.com/qzp2018/UniECS.


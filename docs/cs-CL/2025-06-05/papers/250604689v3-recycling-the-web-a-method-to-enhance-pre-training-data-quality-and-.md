---
layout: default
title: "Recycling the Web: A Method to Enhance Pre-training Data Quality and Quantity for Language Models"
---

# Recycling the Web: A Method to Enhance Pre-training Data Quality and Quantity for Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04689" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04689v3</a>
  <a href="https://arxiv.org/pdf/2506.04689.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04689v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04689v3', 'Recycling the Web: A Method to Enhance Pre-training Data Quality and Quantity for Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thao Nguyen, Yang Li, Olga Golovneva, Luke Zettlemoyer, Sewoong Oh, Ludwig Schmidt, Xian Li

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-05 (更新: 2025-09-15)

**备注**: Accepted to COLM 2025

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/facebook)

---

## 💡 一句话要点

**提出REWIRE方法以解决预训练数据质量和数量不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `预训练` `数据增强` `文本改写` `合成数据` `自然语言处理`

## 📋 核心要点

1. 现有的预训练方法依赖于大规模网络爬取，但高质量文本的获取受到限制，导致数据质量不足。
2. 本文提出REWIRE方法，通过改写被过滤掉的低质量文本，增强数据集的多样性和质量，以提高模型性能。
3. 实验结果显示，在多个任务上，使用混合数据集相比仅使用过滤后的网络数据，性能提升达1.0至2.5个百分点。

## 📝 摘要（中文）

随着大规模语言模型的发展，模型性能与数据规模呈正相关。然而，现有的网络数据爬取并未以相同速度增长，且高质量文本的可用性有限。为了解决预训练中的数据瓶颈，本文提出了REWIRE（REcycling the Web with guIded REwrite）方法，通过改写低质量文档来丰富训练数据。实验表明，结合高质量原始文本与改写文本的混合数据集，在多个任务上显著提升了模型性能。我们还公开了高质量合成数据，供研究者使用。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模语言模型预训练中的数据质量和数量不足问题。现有方法依赖于网络爬取的数据，但高质量文本的比例极低，导致有效训练数据稀缺。

**核心思路**：REWIRE方法通过对低质量文档进行改写，使其能够被有效利用，从而增加合成数据在最终训练集中的比例。这种方法旨在提升数据集的整体质量和多样性。

**技术框架**：REWIRE的整体架构包括数据收集、低质量文本筛选、文本改写和最终数据集构建四个主要模块。首先收集网络数据，然后筛选出低质量文本，接着通过改写技术提升其质量，最后与高质量文本混合形成新的训练数据集。

**关键创新**：REWIRE的创新在于其通过改写低质量文本来生成高质量合成数据，这一方法与传统的仅依赖高质量数据的方式有本质区别。它有效地利用了被过滤掉的数据，提升了数据的利用率。

**关键设计**：在技术细节上，REWIRE使用了特定的改写算法，确保生成的文本在语义上与原文相似，同时具备更高的质量。此外，设计了相应的损失函数，以优化改写过程中的文本质量。

## 📊 实验亮点

实验结果显示，在DCLM基准测试中，使用REWIRE方法的混合数据集在22个不同任务上分别提升了1.0、1.3和2.5个百分点的性能，相比于仅使用过滤后的网络数据，表现更为优越。此外，使用混合数据集的效果优于简单增加2倍的网络数据。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过提升预训练数据的质量和数量，REWIRE方法能够显著改善模型的性能，推动相关技术的发展。未来，该方法可能会在更广泛的AI应用中发挥重要作用，尤其是在数据稀缺的领域。

## 📄 摘要（原文）

> Scaling laws predict that the performance of large language models improves with increasing model size and data size. In practice, pre-training has been relying on massive web crawls, using almost all data sources publicly available on the internet so far. However, this pool of natural data does not grow at the same rate as the compute supply. Furthermore, the availability of high-quality texts is even more limited: data filtering pipelines often remove up to 99% of the initial web scrapes to achieve state-of-the-art. To address the "data wall" of pre-training scaling, our work explores ways to transform and recycle data discarded in existing filtering processes. We propose REWIRE, REcycling the Web with guIded REwrite, a method to enrich low-quality documents so that they could become useful for training. This in turn allows us to increase the representation of synthetic data in the final pre-training set. Experiments at 1B, 3B and 7B scales of the DCLM benchmark show that mixing high-quality raw texts and our rewritten texts lead to 1.0, 1.3 and 2.5 percentage points improvement respectively across 22 diverse tasks, compared to training on only filtered web data. Training on the raw-synthetic data mix is also more effective than having access to 2x web data. Through further analysis, we demonstrate that about 82% of the mixed in texts come from transforming lower-quality documents that would otherwise be discarded. REWIRE also outperforms related approaches of generating synthetic data, including Wikipedia-style paraphrasing, question-answer synthesizing and knowledge extraction. These results suggest that recycling web texts holds the potential for being a simple and effective approach for scaling pre-training data. We make our high-quality synthetic data publicly available at https://huggingface.co/datasets/facebook/recycling_the_web.


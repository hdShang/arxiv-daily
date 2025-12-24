---
layout: default
title: Cross-Lingual Optimization for Language Transfer in Large Language Models
---

# Cross-Lingual Optimization for Language Transfer in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14297" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14297v1</a>
  <a href="https://arxiv.org/pdf/2505.14297.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14297v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14297v1', 'Cross-Lingual Optimization for Language Transfer in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jungseob Lee, Seongtae Hong, Hyeonseok Moon, Heuiseok Lim

**分类**: cs.CL

**发布日期**: 2025-05-20

**备注**: Accepted for publication at ACL 2025. Jungseob Lee and Seongtae Hong contributed equally to this work

---

## 💡 一句话要点

**提出跨语言优化方法以解决大语言模型语言迁移问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨语言优化` `语言迁移` `大语言模型` `监督微调` `低资源语言` `机器翻译` `自然语言处理`

## 📋 核心要点

1. 现有的监督微调方法在低资源语言环境中表现不佳，过于依赖英语数据，导致目标语言能力不足。
2. 提出的跨语言优化（CLO）方法通过利用英语SFT数据和翻译模型，实现了高效的语言迁移，保持了英语能力。
3. 实验结果显示，CLO在多种语言上均优于SFT，特别是在低资源语言中，数据需求显著降低，性能提升明显。

## 📝 摘要（中文）

在将大型语言模型适应其他语言时，通常采用监督微调（SFT）作为标准方法。然而，这种方法往往过于强调英语性能，尤其在数据受限的环境中更为明显。为了解决这些挑战，本文提出了跨语言优化（CLO），该方法能够高效地将以英语为中心的语言模型迁移到目标语言，同时保持其英语能力。CLO利用公开的英语SFT数据和翻译模型实现跨语言迁移。实验结果表明，CLO在获取目标语言能力和保持英语性能方面均优于SFT，尤其在低资源语言中，CLO仅使用3200个样本便超越了使用6400个样本的SFT，显示出CLO在数据利用上的优势。

## 🔬 方法详解

**问题定义**：本文旨在解决在低资源语言环境中，现有监督微调方法（SFT）对英语性能的过度依赖，导致目标语言能力不足的问题。

**核心思路**：提出跨语言优化（CLO）方法，通过结合英语SFT数据和翻译模型，促进英语与目标语言之间的有效迁移，同时保持英语能力。

**技术框架**：CLO的整体架构包括数据准备阶段（利用公开的英语SFT数据）、翻译模型的构建和训练阶段，以及跨语言迁移的实施阶段，确保目标语言的学习与英语能力的保留。

**关键创新**：CLO的主要创新在于其能够在低资源语言中以较少的数据实现更好的性能，克服了SFT对数据量的敏感性，展现出更强的鲁棒性。

**关键设计**：在CLO中，关键参数设置包括样本数量的优化，损失函数的设计以平衡英语和目标语言的学习，以及网络结构的选择以适应不同语言的特性。

## 📊 实验亮点

实验结果表明，CLO在六种语言上均优于传统的SFT方法。在低资源语言中，CLO仅使用3200个样本便超越了使用6400个样本的SFT，显示出在数据利用效率上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括多语言自然语言处理、机器翻译和跨语言信息检索等。通过提高低资源语言的处理能力，CLO方法能够促进全球范围内的信息获取与交流，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Adapting large language models to other languages typically employs supervised fine-tuning (SFT) as a standard approach. However, it often suffers from an overemphasis on English performance, a phenomenon that is especially pronounced in data-constrained environments. To overcome these challenges, we propose \textbf{Cross-Lingual Optimization (CLO)} that efficiently transfers an English-centric LLM to a target language while preserving its English capabilities. CLO utilizes publicly available English SFT data and a translation model to enable cross-lingual transfer. We conduct experiments using five models on six languages, each possessing varying levels of resource. Our results show that CLO consistently outperforms SFT in both acquiring target language proficiency and maintaining English performance. Remarkably, in low-resource languages, CLO with only 3,200 samples surpasses SFT with 6,400 samples, demonstrating that CLO can achieve better performance with less data. Furthermore, we find that SFT is particularly sensitive to data quantity in medium and low-resource languages, whereas CLO remains robust. Our comprehensive analysis emphasizes the limitations of SFT and incorporates additional training strategies in CLO to enhance efficiency.


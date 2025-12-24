---
layout: default
title: Dual Debiasing for Noisy In-Context Learning for Text Generation
---

# Dual Debiasing for Noisy In-Context Learning for Text Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00418" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00418v2</a>
  <a href="https://arxiv.org/pdf/2506.00418.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00418v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00418v2', 'Dual Debiasing for Noisy In-Context Learning for Text Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siqi Liang, Sumyeong Ahn, Paramveer S. Dhillon, Jiayu Zhou

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-31 (更新: 2025-06-21)

**备注**: Accepted by 2025 ACL Findings

---

## 💡 一句话要点

**提出双重去偏差框架以解决噪声注释下的文本生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本生成` `上下文学习` `噪声检测` `去偏差` `合成邻居` `样本清洁度评分`

## 📋 核心要点

1. 现有的噪声检测方法假设噪声样本的困惑度高于干净样本，但在高噪声比例下这一假设失效，导致检测不准确。
2. 本文提出了一种双重去偏差框架，通过合成邻居来修正困惑度估计，从而生成稳健的样本清洁度评分。
3. 实验结果显示，该方法在噪声检测能力上显著优于现有方法，最终的ICL性能与完全干净的示例语料相当。

## 📝 摘要（中文）

在上下文学习（ICL）中，高质量的示例依赖于大量标注语料库。然而，现有方法通过局部困惑度来检测噪声注释，假设噪声样本的困惑度高于干净样本。当噪声比例较高时，这一假设失效。本文重新审视了在噪声注释下的困惑度基础范式，指出困惑度中存在来自注释和大型语言模型（LLMs）固有的领域知识的两种偏差。为克服这些偏差，提出了一种双重去偏差框架，利用合成邻居显式修正困惑度估计，生成稳健的样本清洁度评分。实验表明，该方法在噪声检测能力上优于现有方法，其最终ICL性能可与完全干净的示例语料相媲美，且在极高噪声比例下仍保持稳健性。

## 🔬 方法详解

**问题定义**：本文旨在解决在高噪声注释下的文本生成困惑度估计不准确的问题。现有方法假设噪声样本的困惑度高于干净样本，但在噪声比例较高的情况下，这一假设往往不成立，导致噪声检测能力不足。

**核心思路**：论文提出的双重去偏差框架通过引入合成邻居来显式修正困惑度估计，从而减轻注释和领域知识带来的偏差。这种设计旨在提高样本清洁度评分的准确性，使其不受整体语料噪声水平的影响。

**技术框架**：该方法的整体架构包括两个主要模块：首先，通过合成邻居生成样本的困惑度估计；其次，利用这些估计来计算样本清洁度评分。整个流程强调了对困惑度的修正和评估。

**关键创新**：最重要的技术创新在于双重去偏差框架的提出，它通过合成邻居的方式显式修正困惑度估计，与传统方法相比，能够更准确地评估样本的清洁度。

**关键设计**：在参数设置上，合成邻居的生成过程需要考虑邻居的多样性和代表性；损失函数的设计则需确保困惑度估计的准确性。此外，网络结构的选择也需兼顾计算效率与准确性。

## 📊 实验亮点

实验结果显示，提出的方法在噪声检测能力上显著优于现有方法，最终的ICL性能与完全干净的示例语料相当。在极高噪声比例下，该方法仍保持稳健性，展现出良好的应用前景。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的文本生成、对话系统以及机器翻译等。通过提高噪声样本的检测能力，能够显著提升模型在真实世界应用中的表现，尤其是在数据质量不均的情况下。未来，该方法有望推动更高效的文本生成技术的发展。

## 📄 摘要（原文）

> In context learning (ICL) relies heavily on high quality demonstrations drawn from large annotated corpora. Existing approaches detect noisy annotations by ranking local perplexities, presuming that noisy samples yield higher perplexities than their clean counterparts. However, this assumption breaks down when the noise ratio is high and many demonstrations are flawed. We reexamine the perplexity based paradigm for text generation under noisy annotations, highlighting two sources of bias in perplexity: the annotation itself and the domain specific knowledge inherent in large language models (LLMs). To overcome these biases, we introduce a dual debiasing framework that uses synthesized neighbors to explicitly correct perplexity estimates, yielding a robust Sample Cleanliness Score. This metric uncovers absolute sample cleanliness regardless of the overall corpus noise level. Extensive experiments demonstrate our method's superior noise detection capabilities and show that its final ICL performance is comparable to that of a fully clean demonstration corpus. Moreover, our approach remains robust even when noise ratios are extremely high.


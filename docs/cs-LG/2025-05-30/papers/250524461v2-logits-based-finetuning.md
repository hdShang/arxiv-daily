---
layout: default
title: Logits-Based Finetuning
---

# Logits-Based Finetuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24461" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24461v2</a>
  <a href="https://arxiv.org/pdf/2505.24461.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24461v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24461v2', 'Logits-Based Finetuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyao Li, Senqiao Yang, Sitong Wu, Han Shi, Chuanyang Zheng, Hong Xu, Jiaya Jia

**分类**: cs.LG

**发布日期**: 2025-05-30 (更新: 2025-06-11)

**🔗 代码/项目**: [GITHUB](https://github.com/dvlab-research/Logits-Based-Finetuning)

---

## 💡 一句话要点

**提出基于logits的微调方法以解决传统SFT的局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `监督微调` `知识蒸馏` `logits` `模型训练` `自然语言处理` `数学基准测试`

## 📋 核心要点

1. 现有的监督微调方法无法有效捕捉token级别的依赖和语言多样性，导致模型性能受限。
2. 本文提出的基于logits的微调框架，通过结合教师logits与真实标签，增强训练目标的多样性和准确性。
3. 实验表明，该方法在多个数学基准测试中均表现优异，平均提升达到7.28%，并在特定任务上提升显著。

## 📝 摘要（中文）

近年来，开发紧凑高效的大型语言模型（LLMs）成为研究热点。传统的监督微调（SFT）依赖单一的真实标签，往往无法捕捉到token级别的依赖关系和语言多样性。为了解决这些局限性，本文提出了一种基于logits的微调框架，结合了监督学习和知识蒸馏的优势。该方法通过将教师logits与真实标签结合，构建丰富的训练目标，从而确保训练的可靠性和有效性。实验结果表明，该方法在多个数学基准测试中显著优于以往的SFT模型，准确率提升达到18%和22.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决传统监督微调（SFT）方法在捕捉token级别依赖和语言多样性方面的不足，导致模型在复杂任务中的表现不佳。

**核心思路**：提出基于logits的微调框架，通过结合教师模型的logits与真实标签，构建更丰富的训练目标，以增强模型的学习能力和泛化能力。

**技术框架**：该框架主要包括数据准备、logits生成、训练目标构建和模型训练四个阶段。首先，构建1.2M的logits数据集，然后利用教师模型生成logits，最后结合真实标签进行训练。

**关键创新**：最重要的创新在于通过结合教师logits与真实标签，形成了新的训练目标，这一方法显著提升了模型的准确性和语言多样性，区别于传统的单一标签训练。

**关键设计**：在损失函数设计上，采用了结合logits和真实标签的复合损失函数，以确保模型在训练过程中既保持准确性又增强多样性。

## 📊 实验亮点

实验结果显示，基于logits的微调方法在Mawps和TabMWP任务上分别提升了18%和22.7%的准确率。在九个广泛使用的数学基准测试中，该方法平均提升达7.28%，显著优于以往的SFT模型。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、教育技术和科学计算等。通过提升大型语言模型的性能，可以更好地支持复杂的语言理解任务，推动智能教育和自动化科学研究的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In recent years, developing compact and efficient large language models (LLMs) has emerged as a thriving area of research. Traditional Supervised Fine-Tuning (SFT), which relies on singular ground truth labels, often fails to capture token-level dependencies and linguistic diversity. To address these limitations, we propose a logits-based fine-tuning framework that integrates the strengths of supervised learning and knowledge distillation. Our approach constructs enriched training targets by combining teacher logits with ground truth labels, preserving both correctness and linguistic diversity. This ensures more reliable and effective training. We constructed a large-scale 1.2M logits dataset and trained a series of science-focused models. Experimental results demonstrate that our method achieves significant improvements, with accuracy gains of 18% on Mawps and 22.7% on TabMWP. Across nine widely used mathematical benchmarks, our method consistently outperforms prior SFT models, achieving an average improvement of 7.28%. Codes are available at https://github.com/dvlab-research/Logits-Based-Finetuning.


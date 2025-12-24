---
layout: default
title: Towards Better Instruction Following Retrieval Models
---

# Towards Better Instruction Following Retrieval Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21439" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21439v1</a>
  <a href="https://arxiv.org/pdf/2505.21439.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21439v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21439v1', 'Towards Better Instruction Following Retrieval Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchen Zhuang, Aaron Trinh, Rushi Qiang, Haotian Sun, Chao Zhang, Hanjun Dai, Bo Dai

**分类**: cs.CL, cs.IR

**发布日期**: 2025-05-27

**备注**: Retrieval Models, Embedding, Retrieval with Instructions

---

## 💡 一句话要点

**提出InF-IR以解决指令跟随信息检索模型的不足**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信息检索` `指令跟随` `对比学习` `语料库构建` `模型优化`

## 📋 核心要点

1. 现有的信息检索模型主要依赖标准的<查询, 段落>对，难以有效处理用户的指令，导致检索效果不佳。
2. 本文提出InF-IR语料库，通过生成<指令, 查询, 段落>三元组，增强模型对用户意图的理解和跟随能力。
3. 实验表明，使用InF-Embed模型在五个基准测试中，指令跟随能力提升了8.1%的p-MRR，显示出显著的效果改进。

## 📝 摘要（中文）

现代信息检索模型在处理标准的<查询, 段落>对时，难以有效理解和遵循用户的明确指令。为此，本文引入了InF-IR，一个大规模、高质量的训练语料库，旨在增强指令跟随信息检索模型的能力。InF-IR将传统的训练对扩展为超过38,000个富有表现力的<指令, 查询, 段落>三元组作为正样本，并为每个正样本生成两个附加的困难负样本。通过对比学习和指令-查询注意力机制优化的InF-Embed模型，实验结果表明，该模型在五个基准测试中显著超越竞争基线，提升了8.1%的p-MRR。

## 🔬 方法详解

**问题定义**：本文旨在解决现代信息检索模型在处理用户指令时的不足，现有方法主要依赖标准的<查询, 段落>对，缺乏对用户意图的有效理解。

**核心思路**：提出InF-IR语料库，通过生成丰富的<指令, 查询, 段落>三元组，增强模型在指令跟随任务中的表现。该方法通过对比学习和指令-查询注意力机制，优化检索结果与用户意图的对齐。

**技术框架**：整体架构包括数据生成、模型训练和评估三个主要阶段。数据生成阶段使用先进的推理模型生成正负样本，模型训练阶段则采用对比学习方法优化InF-Embed模型，最后通过多个基准测试评估模型性能。

**关键创新**：最重要的创新在于构建了InF-IR语料库，提供了大量的对比性正负样本，支持更高效的表示学习，与现有方法相比，显著提升了小型编码器模型的检索能力。

**关键设计**：在模型设计中，采用了对比损失函数和指令-查询注意力机制，确保模型能够有效捕捉用户意图，并通过精细的参数设置提升模型的整体性能。

## 📊 实验亮点

在五个指令基础的检索基准测试中，InF-Embed模型的表现显著优于竞争基线，p-MRR提升了8.1%。这一结果表明，模型在指令跟随能力上取得了显著进展，展示了InF-IR语料库的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、搜索引擎和客户服务等场景，能够显著提升用户与系统之间的交互体验。通过更好地理解用户指令，未来可实现更智能的信息检索和个性化推荐，推动人机交互的进一步发展。

## 📄 摘要（原文）

> Modern information retrieval (IR) models, trained exclusively on standard <query, passage> pairs, struggle to effectively interpret and follow explicit user instructions. We introduce InF-IR, a large-scale, high-quality training corpus tailored for enhancing retrieval models in Instruction-Following IR. InF-IR expands traditional training pairs into over 38,000 expressive <instruction, query, passage> triplets as positive samples. In particular, for each positive triplet, we generate two additional hard negative examples by poisoning both instructions and queries, then rigorously validated by an advanced reasoning model (o3-mini) to ensure semantic plausibility while maintaining instructional incorrectness. Unlike existing corpora that primarily support computationally intensive reranking tasks for decoder-only language models, the highly contrastive positive-negative triplets in InF-IR further enable efficient representation learning for smaller encoder-only models, facilitating direct embedding-based retrieval. Using this corpus, we train InF-Embed, an instruction-aware Embedding model optimized through contrastive learning and instruction-query attention mechanisms to align retrieval outcomes precisely with user intents. Extensive experiments across five instruction-based retrieval benchmarks demonstrate that InF-Embed significantly surpasses competitive baselines by 8.1% in p-MRR, measuring the instruction-following capabilities.


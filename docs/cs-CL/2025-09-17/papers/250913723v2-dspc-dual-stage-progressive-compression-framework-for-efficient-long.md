---
layout: default
title: "DSPC: Dual-Stage Progressive Compression Framework for Efficient Long-Context Reasoning"
---

# DSPC: Dual-Stage Progressive Compression Framework for Efficient Long-Context Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13723" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13723v2</a>
  <a href="https://arxiv.org/pdf/2509.13723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13723v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13723v2', 'DSPC: Dual-Stage Progressive Compression Framework for Efficient Long-Context Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaxin Gao, Yao Lu, Zongfei Zhang, Jiaqi Nie, Shanqing Yu, Qi Xuan

**分类**: cs.CL

**发布日期**: 2025-09-17 (更新: 2025-09-18)

---

## 💡 一句话要点

**提出DSPC双阶段渐进压缩框架，无需训练即可高效压缩长文本上下文，提升LLM推理效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本压缩` `提示压缩` `双阶段压缩` `免训练方法` `大型语言模型`

## 📋 核心要点

1. 现有长文本压缩方法通常需要训练额外的辅助模型，增加了计算负担，限制了实际应用。
2. DSPC框架通过粗粒度的句子过滤和细粒度的token修剪，在不进行模型训练的情况下实现高效的提示压缩。
3. 实验表明，DSPC在长文本基准测试中，显著优于现有压缩方法，同时降低了计算成本。

## 📝 摘要（中文）

大型语言模型(LLMs)在许多自然语言处理(NLP)任务中取得了显著成功。为了获得更准确的输出，驱动LLMs的提示变得越来越长，这导致了更高的计算成本。为了解决这个提示膨胀问题，已经提出了提示压缩。然而，大多数现有方法需要训练一个小的辅助模型进行压缩，从而导致大量的额外计算。为了避免这种情况，我们提出了一种两阶段、免训练的方法，称为双阶段渐进压缩(DSPC)。在粗粒度阶段，语义相关的句子过滤基于TF-IDF删除语义价值低的句子。在细粒度阶段，使用注意力贡献、跨模型损失差异和位置重要性来评估token重要性，从而能够在保留语义的同时修剪低效用的token。我们在LLaMA-3.1-8B-Instruct和GPT-3.5-Turbo上，在受限的token预算下验证了DSPC，并观察到了一致的改进。例如，在Longbench数据集的FewShot任务中，DSPC仅使用3倍少的token就实现了49.17的性能，优于最佳的state-of-the-art基线LongLLMLingua 7.76。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）中由于长上下文提示导致的计算成本高昂问题。现有的提示压缩方法通常需要训练额外的辅助模型，这增加了计算负担，并且可能引入额外的复杂性。因此，需要一种无需训练且高效的提示压缩方法，以降低LLMs的推理成本。

**核心思路**：论文的核心思路是采用一种双阶段渐进压缩策略，即DSPC，该策略分为粗粒度的句子过滤和细粒度的token修剪。通过这种方式，可以在保留关键语义信息的同时，逐步减少提示的长度，从而降低计算成本。这种设计避免了训练额外模型的需求，提高了效率。

**技术框架**：DSPC框架包含两个主要阶段：
1. **粗粒度句子过滤**：使用TF-IDF算法评估句子级别的语义重要性，并移除语义价值较低的句子，从而减少提示的长度。
2. **细粒度token修剪**：通过综合考虑注意力贡献、跨模型损失差异和位置重要性等因素，评估token级别的重要性，并修剪低效用的token，进一步压缩提示。

**关键创新**：DSPC的关键创新在于其免训练的设计和双阶段渐进压缩策略。与需要训练辅助模型的现有方法不同，DSPC完全依赖于现有的LLM和简单的统计方法（如TF-IDF）进行压缩，从而避免了额外的计算负担。双阶段策略能够更精细地控制压缩过程，在保证语义完整性的前提下，实现更高的压缩率。

**关键设计**：
* **TF-IDF句子过滤**：使用TF-IDF值作为句子语义重要性的度量，设定阈值来决定哪些句子被保留。
* **Token重要性评估**：综合考虑以下三个因素：
    * 注意力贡献：基于LLM的注意力权重来评估token的重要性。
    * 跨模型损失差异：通过比较原始模型和压缩后模型在验证集上的损失差异来评估token的重要性。
    * 位置重要性：根据token在提示中的位置（例如，开头或结尾）来赋予不同的重要性权重。
* **Token修剪策略**：根据token的重要性得分，设定阈值来决定哪些token被修剪。

## 📊 实验亮点

DSPC在Longbench数据集的FewShot任务中，仅使用3倍少的token就实现了49.17的性能，超越了当前最佳的基线方法LongLLMLingua 7.76个百分点。实验结果表明，DSPC能够在显著降低计算成本的同时，保持甚至提升LLM的性能，验证了其有效性和优越性。

## 🎯 应用场景

DSPC框架可广泛应用于各种需要处理长文本输入的LLM应用场景，例如：文档摘要、问答系统、代码生成等。通过降低LLM的计算成本，DSPC能够提高推理速度，降低部署成本，并使得在资源受限的设备上运行LLM成为可能。未来，DSPC可以进一步扩展到多模态场景，例如压缩图像或音频等输入。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable success in many natural language processing (NLP) tasks. To achieve more accurate output, the prompts used to drive LLMs have become increasingly longer, which incurs higher computational costs. To address this prompt inflation problem, prompt compression has been proposed. However, most existing methods require training a small auxiliary model for compression, incurring a significant amount of additional computation. To avoid this, we propose a two-stage, training-free approach, called Dual-Stage Progressive Compression (DSPC). In the coarse-grained stage, semantic-related sentence filtering removes sentences with low semantic value based on TF-IDF. In the fine-grained stage, token importance is assessed using attention contribution, cross-model loss difference, and positional importance, enabling the pruning of low-utility tokens while preserving semantics. We validate DSPC on LLaMA-3.1-8B-Instruct and GPT-3.5-Turbo under a constrained token budget and observe consistent improvements. For instance, in the FewShot task of the Longbench dataset, DSPC achieves a performance of 49.17 by using only 3x fewer tokens, outperforming the best state-of-the-art baseline LongLLMLingua by 7.76.


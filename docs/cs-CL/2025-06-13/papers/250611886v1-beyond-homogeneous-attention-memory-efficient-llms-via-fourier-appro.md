---
layout: default
title: "Beyond Homogeneous Attention: Memory-Efficient LLMs via Fourier-Approximated KV Cache"
---

# Beyond Homogeneous Attention: Memory-Efficient LLMs via Fourier-Approximated KV Cache

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11886" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11886v1</a>
  <a href="https://arxiv.org/pdf/2506.11886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11886v1', 'Beyond Homogeneous Attention: Memory-Efficient LLMs via Fourier-Approximated KV Cache')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoran Liu, Siyang He, Qiqi Wang, Ruixiao Li, Yuerong Song, Zhigeng Liu, Linlin Li, Qun Liu, Zengfeng Huang, Qipeng Guo, Ziwei He, Xipeng Qiu

**分类**: cs.CL

**发布日期**: 2025-06-13

**备注**: 10 pages, 7 figures, work in progress

---

## 💡 一句话要点

**提出FourierAttention以解决大语言模型的内存效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `内存效率` `傅里叶变换` `长上下文处理` `自定义内核` `变换器架构` `模型压缩`

## 📋 核心要点

1. 现有方法在处理长上下文时，KV缓存的内存需求不断增加，导致准确性和计算效率的折中。
2. FourierAttention利用变换器头部维度的异质性，通过傅里叶基投影来优化长上下文的处理，避免了训练过程中的复杂性。
3. 在LLaMA模型的实验中，FourierAttention在长上下文任务上表现优异，显著提升了准确性，并且内存使用效率得到了优化。

## 📝 摘要（中文）

大语言模型在上下文长度增加时面临日益增长的键值（KV）缓存内存需求。现有的压缩方法通常会均化头部维度或依赖于注意力引导的令牌剪枝，往往牺牲准确性或引入计算开销。我们提出了FourierAttention，这是一种无训练框架，利用变换器头部维度的异质角色：低维度优先考虑局部上下文，而高维度则捕捉长程依赖。通过将长上下文不敏感的维度投影到正交傅里叶基上，FourierAttention用固定长度的谱系数近似其时间演变。对LLaMA模型的评估表明，FourierAttention在LongBench和Needle-In-A-Haystack（NIAH）上实现了最佳的长上下文准确性。此外，设计了一个自定义的Triton内核FlashFourierAttention，通过简化读写操作优化内存，实现高效部署而不影响性能。

## 🔬 方法详解

**问题定义**：论文要解决的是大语言模型在长上下文处理中的内存效率问题。现有方法通过均化头部维度或剪枝策略，往往导致准确性下降或计算开销增加。

**核心思路**：论文提出的FourierAttention框架利用变换器头部维度的异质性，低维度关注局部上下文，高维度捕捉长程依赖，通过傅里叶基的投影来近似长上下文的处理。

**技术框架**：FourierAttention的整体架构包括两个主要模块：一是对长上下文不敏感的维度进行傅里叶基投影，二是使用固定长度的谱系数来近似其时间演变，确保内存使用的高效性。

**关键创新**：FourierAttention的核心创新在于其无训练的特性和对头部维度异质性的利用，与现有方法相比，它避免了训练过程中的复杂性，同时保持了长上下文的处理能力。

**关键设计**：在设计中，采用了正交傅里叶基的投影方法，确保了维度的有效利用，并通过自定义的Triton内核FlashFourierAttention优化了内存读写操作，提升了整体性能。

## 📊 实验亮点

实验结果显示，FourierAttention在LongBench和NIAH任务上实现了最佳的长上下文准确性，相较于传统方法，显著提升了内存使用效率，确保了性能的同时降低了计算开销。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等场景，能够有效提升大语言模型在长文本处理中的效率和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models struggle with memory demands from the growing Key-Value (KV) cache as context lengths increase. Existing compression methods homogenize head dimensions or rely on attention-guided token pruning, often sacrificing accuracy or introducing computational overhead. We propose FourierAttention, a training-free framework that exploits the heterogeneous roles of transformer head dimensions: lower dimensions prioritize local context, while upper ones capture long-range dependencies. By projecting the long-context-insensitive dimensions onto orthogonal Fourier bases, FourierAttention approximates their temporal evolution with fixed-length spectral coefficients. Evaluations on LLaMA models show that FourierAttention achieves the best long-context accuracy on LongBench and Needle-In-A-Haystack (NIAH). Besides, a custom Triton kernel, FlashFourierAttention, is designed to optimize memory via streamlined read-write operations, enabling efficient deployment without performance compromise.


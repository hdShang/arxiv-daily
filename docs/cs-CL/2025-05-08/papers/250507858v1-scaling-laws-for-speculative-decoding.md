---
layout: default
title: Scaling Laws for Speculative Decoding
---

# Scaling Laws for Speculative Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07858" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07858v1</a>
  <a href="https://arxiv.org/pdf/2505.07858.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07858v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07858v1', 'Scaling Laws for Speculative Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyuan Yan, Mo Zhu, Guo-qing Jiang, Jianfei Wang, Jiaxing Chen, Wentai Zhang, Xiang Liao, Xiao Cui, Chen Zhang, Zhuoran Song, Ran Zhu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-08

**备注**: 17 pages, 8 figures

---

## 💡 一句话要点

**提出规范解码技术以提升大语言模型推理效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `规范解码` `大语言模型` `推理效率` `对数线性扩展` `草稿模型` `自然语言处理` `自动摘要` `问答系统`

## 📋 核心要点

1. 现有的解码方法在推理效率上存在不足，尤其是在处理复杂推理任务时表现不佳。
2. 本文提出了规范解码技术，通过建立对数线性扩展规律，优化草稿模型的接受率和解码速度。
3. 实验结果表明，Scylla在解码吞吐量上较EAGLE2提升了2倍，并在摘要和问答任务上表现出显著的性能提升。

## 📝 摘要（中文）

随着对大语言模型（LLMs）高效解码的需求不断上升，尤其是在依赖扩展链式推理的架构中，如OpenAI-o3和DeepSeek-R1，本文研究了通过密集LLM架构的规范解码技术，以加速推理任务。尽管利用并行草稿验证周期的规范解码方法已显示出加速潜力，但与传统的LLM训练方法相比，解码效率的扩展规律仍未得到充分探索。本文发现了控制草稿模型接受率（或解码速度）的对数线性扩展规律，并在此基础上实现了Scylla，显著提升了多种LLM的解码效率。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在推理任务中解码效率不足的问题，现有方法在处理复杂推理时的性能未能满足需求。

**核心思路**：通过探索规范解码技术，建立对数线性扩展规律，优化草稿模型的接受率和解码速度，从而提升推理效率。

**技术框架**：整体架构包括三个主要模块：预训练阶段、草稿模型构建和解码过程。预训练阶段负责生成初始模型，草稿模型构建则通过并行草稿验证提高解码效率，最后在解码过程中应用扩展规律。

**关键创新**：本文的主要创新在于发现了控制草稿模型接受率的对数线性扩展规律，这一理论为解码效率的提升提供了新的视角，与传统方法相比具有本质的区别。

**关键设计**：在参数设置上，本文对预训练的token数量、草稿模型的容量和解码批量大小进行了系统的调整，以实现最佳的解码性能。

## 📊 实验亮点

实验结果显示，Scylla在温度T=0时的接受率比EAGLE2高出1.5-2.2倍，比EAGLE3高出0.3，尤其在摘要和问答任务上表现出显著的性能提升。此外，工业推理引擎的部署实现了2倍的解码吞吐量提升，验证了系统扩展的变革潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的复杂推理任务，如自动摘要生成和问答系统。通过提升解码效率，能够显著改善用户体验，并推动大语言模型在工业界的广泛应用，未来可能影响多个行业的智能化进程。

## 📄 摘要（原文）

> The escalating demand for efficient decoding in large language models (LLMs) is particularly critical for reasoning-intensive architectures like OpenAI-o3 and DeepSeek-R1, which depend on extended chain-of-thought reasoning. This study investigates speculative decoding techniques through dense LLM architectures to establish foundational insights for accelerating reasoning tasks. While speculative decoding methods leveraging parallel draft-verification cycles have emerged as promising acceleration techniques, the scaling laws governing decoding efficiency remain under-explored compared to conventional backbone LLMs developed through Pretraining->SFT->RLHF training paradigms. In this work, we discover Log-linear Scaling Laws (Theorem 1.1, 1.2 and 1.3) governing draft model acceptance rate (or decoding speed) across three dimensions: pretraining token volume, draft model capacity, and decoding batch size. Building on these laws, we achieve Scylla, which coordinates multi-dimensional scaling for popular LLMs (Llama2/3, Qwen2.5). Empirical validation shows Scylla achieves 1.5-2.2 higher acceptance rate than EAGLE2 and 0.3 higher than EAGLE3 at temperature T = 0, with peak performance gains on summarization and QA tasks (Figure 2). Industrial inference engine deployments demonstrate 2X decoding throughput improvements over EAGLE2 (Table 5), validating the transformative potential of systematic scaling for efficient LLM inference. Code will be released later.


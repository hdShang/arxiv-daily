---
layout: default
title: Enhancing Learned Knowledge in LoRA Adapters Through Efficient Contrastive Decoding on Ascend NPUs
---

# Enhancing Learned Knowledge in LoRA Adapters Through Efficient Contrastive Decoding on Ascend NPUs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14620" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14620v1</a>
  <a href="https://arxiv.org/pdf/2505.14620.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14620v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14620v1', 'Enhancing Learned Knowledge in LoRA Adapters Through Efficient Contrastive Decoding on Ascend NPUs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Morgan Lindsay Heisler, Linzi Xing, Ge Shi, Hanieh Sadri, Gursimran Singh, Weiwei Zhang, Tao Ye, Ying Xiong, Yong Zhang, Zhenan Fan

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-20

**备注**: Accepted at ACM KDD 2025

**DOI**: [10.1145/3711896.3737215](https://doi.org/10.1145/3711896.3737215)

---

## 💡 一句话要点

**提出对比LoRA解码以提升大语言模型的任务性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对比解码` `LoRA适配` `大语言模型` `任务特定知识` `华为Ascend NPU` `计算效率` `微调技术`

## 📋 核心要点

1. 现有的解码方法如贪婪搜索和束搜索在处理复杂推理任务时，常受到基模型偏见的影响，导致生成的响应不够特定和准确。
2. 本文提出的对比LoRA解码（CoLD）框架，通过对比解码技术，优化了LoRA适配模型的任务特定知识利用，提升了模型的下游性能。
3. 实验结果表明，CoLD在任务准确率上提高了5.54%，同时将端到端延迟降低了28%，显示出其在资源受限环境中的实用性。

## 📝 摘要（中文）

华为云用户利用LoRA（低秩适配）作为一种高效且可扩展的方法，针对特定应用需求微调和定制大型语言模型（LLMs）。然而，复杂推理或深度上下文理解的任务常常受到基模型偏见或干扰的影响，导致生成的响应过于通用。本文提出了一种新颖的对比LoRA解码（CoLD）框架，旨在最大化利用LoRA适配模型中的任务特定知识，从而提升下游性能。CoLD通过对候选标记进行对比解码，基于LoRA适配专家模型与基模型的概率分布差异进行评分，优先选择与LoRA学习表示更一致的标记。尽管有效，但CoLD的简单实现计算开销较大，因此我们为华为Ascend NPU开发了优化内核。与贪婪解码相比，CoLD在任务准确率上提高了5.54%，并将端到端延迟降低了28%。

## 🔬 方法详解

**问题定义**：现有的解码方法在处理复杂推理任务时，常常受到基模型的偏见影响，导致生成的响应过于通用，无法充分利用LoRA适配模型的特定知识。

**核心思路**：本文提出的对比LoRA解码（CoLD）通过对比解码技术，基于LoRA适配专家模型与基模型的概率分布差异，优先选择与LoRA学习表示一致的候选标记，从而提升任务特定性能。

**技术框架**：CoLD的整体架构包括候选标记评分模块和优化解码模块。评分模块评估每个候选标记的适应性，优化解码模块则负责高效生成最终输出。

**关键创新**：CoLD的主要创新在于其对比解码策略，通过对比不同模型的概率分布，显著提升了任务特定知识的利用效率，与传统的贪婪解码方法相比，能够生成更具针对性的响应。

**关键设计**：在实现CoLD时，采用了优化的内核设计以适应华为Ascend NPU，确保在计算效率和解码性能之间取得平衡，同时设置了适当的损失函数以引导模型学习更有效的表示。

## 📊 实验亮点

实验结果显示，CoLD在任务准确率上提高了5.54%，同时将端到端延迟降低了28%。与传统的贪婪解码方法相比，CoLD显著提升了模型在特定任务上的表现，展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括云计算环境中的大语言模型微调，特别是在需要高效解码和快速响应的场景，如智能客服、内容生成和数据分析等。其优化的解码策略能够在资源受限的环境中提供更好的性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Huawei Cloud users leverage LoRA (Low-Rank Adaptation) as an efficient and scalable method to fine-tune and customize large language models (LLMs) for application-specific needs. However, tasks that require complex reasoning or deep contextual understanding are often hindered by biases or interference from the base model when using typical decoding methods like greedy or beam search. These biases can lead to generic or task-agnostic responses from the base model instead of leveraging the LoRA-specific adaptations. In this paper, we introduce Contrastive LoRA Decoding (CoLD), a novel decoding framework designed to maximize the use of task-specific knowledge in LoRA-adapted models, resulting in better downstream performance. CoLD uses contrastive decoding by scoring candidate tokens based on the divergence between the probability distributions of a LoRA-adapted expert model and the corresponding base model. This approach prioritizes tokens that better align with the LoRA's learned representations, enhancing performance for specialized tasks. While effective, a naive implementation of CoLD is computationally expensive because each decoding step requires evaluating multiple token candidates across both models. To address this, we developed an optimized kernel for Huawei's Ascend NPU. CoLD achieves up to a 5.54% increase in task accuracy while reducing end-to-end latency by 28% compared to greedy decoding. This work provides practical and efficient decoding strategies for fine-tuned LLMs in resource-constrained environments and has broad implications for applied data science in both cloud and on-premises settings.


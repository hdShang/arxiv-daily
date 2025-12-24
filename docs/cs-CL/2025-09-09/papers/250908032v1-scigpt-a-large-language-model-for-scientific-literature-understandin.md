---
layout: default
title: "SciGPT: A Large Language Model for Scientific Literature Understanding and Knowledge Discovery"
---

# SciGPT: A Large Language Model for Scientific Literature Understanding and Knowledge Discovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08032" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08032v1</a>
  <a href="https://arxiv.org/pdf/2509.08032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08032v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08032v1', 'SciGPT: A Large Language Model for Scientific Literature Understanding and Knowledge Discovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fengyu She, Nan Wang, Hongfei Wu, Ziyi Wan, Jingmian Wang, Chang Wang

**分类**: cs.CL

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**SciGPT：面向科学文献理解和知识发现的大语言模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `科学文献理解` `知识发现` `领域自适应` `稀疏混合专家` `领域蒸馏` `知识图谱`

## 📋 核心要点

1. 现有通用大语言模型难以捕捉科学领域的专业术语和方法论严谨性，限制了其在跨学科研究中的应用。
2. SciGPT通过低成本的领域蒸馏、稀疏混合专家注意力机制和知识感知适配，提升了模型在科学领域的性能。
3. 在ScienceBench上的实验结果表明，SciGPT在序列标注、生成和推理等核心科学任务上优于GPT-4o，并展现出强大的鲁棒性。

## 📝 摘要（中文）

科学文献呈指数级增长，这给研究人员高效地综合知识带来了瓶颈。通用大语言模型(LLMs)在文本处理方面显示出潜力，但它们常常无法捕捉科学领域特有的细微差别(例如，技术术语、方法论的严谨性)，并且难以处理复杂的科学任务，限制了它们在跨学科研究中的应用。为了解决这些差距，本文提出了SciGPT，一个为科学文献理解而设计的领域自适应基础模型，以及ScienceBench，一个为评估科学LLMs量身定制的开源基准。

## 🔬 方法详解

**问题定义**：当前科学文献数量爆炸式增长，研究人员难以高效地从中提取和综合知识。通用大语言模型虽然具备一定的文本处理能力，但在理解科学领域的专业术语、方法论以及处理复杂科学任务方面存在不足，无法很好地支持跨学科研究。

**核心思路**：SciGPT的核心思路是构建一个领域自适应的大语言模型，使其能够更好地理解和处理科学文献。通过领域蒸馏、稀疏混合专家注意力机制和知识感知适配等技术，提升模型在科学领域的性能和鲁棒性。

**技术框架**：SciGPT构建于Qwen3架构之上，主要包含三个关键模块：1) 低成本领域蒸馏模块，用于将通用语言模型的知识迁移到科学领域；2) 稀疏混合专家(SMoE)注意力机制，用于处理长文档并降低内存消耗；3) 知识感知适配模块，用于整合领域本体知识，弥合跨学科知识的差距。

**关键创新**：SciGPT的关键创新在于其领域自适应策略，具体包括：1) 采用两阶段蒸馏流程，在性能和效率之间取得平衡；2) 引入SMoE注意力机制，显著降低长文档处理的内存消耗；3) 通过知识感知适配，将领域本体知识融入模型，提升跨学科理解能力。

**关键设计**：SciGPT的领域蒸馏采用两阶段策略，第一阶段使用大规模科学文本进行预训练，第二阶段使用高质量的标注数据进行微调。SMoE注意力机制通过稀疏激活不同的专家网络，降低计算复杂度。知识感知适配模块利用领域本体构建知识图谱，并将知识图谱的信息融入到模型的表示学习中。

## 📊 实验亮点

SciGPT在ScienceBench基准测试中表现出色，在序列标注、生成和推理等核心科学任务上优于GPT-4o。此外，SciGPT在未见过的科学任务中也表现出强大的鲁棒性，证明了其在AI辅助科学发现方面的潜力。SMoE注意力机制能够将处理32000 token长文档的内存消耗降低55%。

## 🎯 应用场景

SciGPT可应用于多个科学领域，例如生物医学、化学、材料科学等，帮助研究人员快速理解和综合文献知识，加速科学发现过程。它还可以用于构建智能科研助手，辅助科研人员进行文献检索、知识抽取、假设生成等任务，提升科研效率。

## 📄 摘要（原文）

> Scientific literature is growing exponentially, creating a critical bottleneck for researchers to efficiently synthesize knowledge. While general-purpose Large Language Models (LLMs) show potential in text processing, they often fail to capture scientific domain-specific nuances (e.g., technical jargon, methodological rigor) and struggle with complex scientific tasks, limiting their utility for interdisciplinary research. To address these gaps, this paper presents SciGPT, a domain-adapted foundation model for scientific literature understanding and ScienceBench, an open source benchmark tailored to evaluate scientific LLMs.
>   Built on the Qwen3 architecture, SciGPT incorporates three key innovations: (1) low-cost domain distillation via a two-stage pipeline to balance performance and efficiency; (2) a Sparse Mixture-of-Experts (SMoE) attention mechanism that cuts memory consumption by 55\% for 32,000-token long-document reasoning; and (3) knowledge-aware adaptation integrating domain ontologies to bridge interdisciplinary knowledge gaps.
>   Experimental results on ScienceBench show that SciGPT outperforms GPT-4o in core scientific tasks including sequence labeling, generation, and inference. It also exhibits strong robustness in unseen scientific tasks, validating its potential to facilitate AI-augmented scientific discovery.


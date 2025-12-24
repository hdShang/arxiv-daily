---
layout: default
title: "SLiNT: Structure-aware Language Model with Injection and Contrastive Training for Knowledge Graph Completion"
---

# SLiNT: Structure-aware Language Model with Injection and Contrastive Training for Knowledge Graph Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.06531" class="toolbar-btn" target="_blank">📄 arXiv: 2509.06531v1</a>
  <a href="https://arxiv.org/pdf/2509.06531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.06531v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.06531v1', 'SLiNT: Structure-aware Language Model with Injection and Contrastive Training for Knowledge Graph Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mengxue Yang, Chun Yang, Jiaqi Zhu, Jiafan Li, Jingqi Zhang, Yuyang Li, Ying Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-08

**备注**: Accepted by EMNLP Findings 2025

---

## 💡 一句话要点

**SLiNT：通过注入和对比训练的结构感知语言模型，用于知识图谱补全**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱补全` `链接预测` `结构感知学习` `对比学习` `大型语言模型`

## 📋 核心要点

1. 现有知识图谱补全方法在利用结构信息方面存在不足，导致结构稀疏和语义模糊，尤其是在数据不完整或零样本场景下。
2. SLiNT通过结构引导的邻域增强、动态硬对比学习和梯度解耦双重注入，将结构信息注入到冻结的LLM中，提升链接预测性能。
3. 实验结果表明，SLiNT在WN18RR和FB15k-237数据集上优于或媲美现有方法，验证了结构感知表示学习的有效性。

## 📝 摘要（中文）

知识图谱中的链接预测需要整合结构信息和语义上下文，以推断缺失的实体。大型语言模型虽然具有强大的生成推理能力，但它们对结构信号的利用有限，常常导致结构稀疏和语义模糊，尤其是在不完整或零样本设置下。为了应对这些挑战，我们提出了SLiNT（Structure-aware Language model with Injection and coNtrastive Training），这是一个模块化框架，它将知识图谱导出的结构上下文注入到冻结的LLM骨干中，并通过基于LoRA的轻量级适配进行鲁棒的链接预测。具体来说，结构引导的邻域增强（SGNE）检索伪邻居以丰富稀疏实体并缓解缺失的上下文；动态硬对比学习（DHCL）通过插值硬正样本和负样本来引入细粒度的监督，以解决实体级别的模糊性；梯度解耦双重注入（GDDI）执行token级别的结构感知干预，同时保留核心LLM参数。在WN18RR和FB15k-237上的实验表明，与基于嵌入和基于生成的基线相比，SLiNT实现了优越或具有竞争力的性能，证明了结构感知表示学习对于可扩展知识图谱补全的有效性。

## 🔬 方法详解

**问题定义**：知识图谱补全任务旨在预测知识图谱中缺失的实体或关系。现有方法，特别是基于大型语言模型的方法，虽然具备强大的语义理解能力，但在利用知识图谱的结构信息方面存在不足，导致模型在处理结构稀疏或零样本场景时表现不佳。这些方法难以有效区分语义相似但结构不同的实体，造成语义模糊。

**核心思路**：SLiNT的核心思路是将知识图谱的结构信息有效地注入到预训练语言模型中，从而增强模型对结构信息的感知能力，缓解结构稀疏和语义模糊问题。通过结构信息增强，模型可以更好地理解实体之间的关系，从而提高链接预测的准确性。同时，采用对比学习的方式，进一步区分相似实体，提升模型的判别能力。

**技术框架**：SLiNT是一个模块化的框架，主要包含三个模块：结构引导的邻域增强（SGNE）、动态硬对比学习（DHCL）和梯度解耦双重注入（GDDI）。首先，SGNE通过检索伪邻居来丰富稀疏实体的上下文信息。然后，DHCL通过引入硬正样本和负样本进行对比学习，解决实体级别的模糊性。最后，GDDI在token级别进行结构感知干预，同时冻结LLM的大部分参数，只对少量参数进行微调。

**关键创新**：SLiNT的关键创新在于其结构感知注入和对比训练机制。与以往方法不同，SLiNT不是简单地将结构信息作为额外的输入，而是通过SGNE、DHCL和GDDI三个模块，将结构信息深度融合到语言模型的表示学习过程中。这种方法能够更有效地利用结构信息，提高模型在复杂场景下的泛化能力。梯度解耦双重注入（GDDI）的设计保证了在注入结构信息的同时，不会破坏预训练语言模型的原有知识。

**关键设计**：SGNE模块使用基于嵌入相似度的邻居检索方法，选择与目标实体最相关的伪邻居。DHCL模块通过插值生成硬正样本和负样本，并使用InfoNCE损失函数进行对比学习。GDDI模块使用LoRA进行参数高效微调，并设计了梯度解耦机制，防止结构信息更新影响LLM的固有知识。具体损失函数的设计和超参数的选择需要根据实际数据集进行调整。

## 📊 实验亮点

SLiNT在WN18RR和FB15k-237数据集上进行了实验，结果表明SLiNT取得了优越或具有竞争力的性能。例如，在WN18RR数据集上，SLiNT的MRR指标超过了现有最佳基线模型，证明了其结构感知表示学习的有效性。实验结果还表明，SLiNT在处理结构稀疏和零样本场景时表现出色，具有良好的泛化能力。

## 🎯 应用场景

SLiNT在知识图谱补全方面具有广泛的应用前景，例如智能问答、推荐系统、信息检索等。通过补全知识图谱，可以提高这些应用在处理复杂查询和推理任务时的准确性和可靠性。此外，SLiNT的结构感知学习方法也可以应用于其他图结构数据，例如社交网络分析、生物信息学等领域，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Link prediction in knowledge graphs requires integrating structural information and semantic context to infer missing entities. While large language models offer strong generative reasoning capabilities, their limited exploitation of structural signals often results in structural sparsity and semantic ambiguity, especially under incomplete or zero-shot settings. To address these challenges, we propose SLiNT (Structure-aware Language model with Injection and coNtrastive Training), a modular framework that injects knowledge-graph-derived structural context into a frozen LLM backbone with lightweight LoRA-based adaptation for robust link prediction. Specifically, Structure-Guided Neighborhood Enhancement (SGNE) retrieves pseudo-neighbors to enrich sparse entities and mitigate missing context; Dynamic Hard Contrastive Learning (DHCL) introduces fine-grained supervision by interpolating hard positives and negatives to resolve entity-level ambiguity; and Gradient-Decoupled Dual Injection (GDDI) performs token-level structure-aware intervention while preserving the core LLM parameters. Experiments on WN18RR and FB15k-237 show that SLiNT achieves superior or competitive performance compared with both embedding-based and generation-based baselines, demonstrating the effectiveness of structure-aware representation learning for scalable knowledge graph completion.


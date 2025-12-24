---
layout: default
title: InfiGFusion: Graph-on-Logits Distillation via Efficient Gromov-Wasserstein for Model Fusion
---

# InfiGFusion: Graph-on-Logits Distillation via Efficient Gromov-Wasserstein for Model Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13893" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13893v1</a>
  <a href="https://arxiv.org/pdf/2505.13893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13893v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13893v1', 'InfiGFusion: Graph-on-Logits Distillation via Efficient Gromov-Wasserstein for Model Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanyi Wang, Zhaoyi Yan, Yiming Zhang, Qi Zhou, Yanggan Gu, Fei Wu, Hongxia Yang

**分类**: cs.CL

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出InfiGFusion以解决异构模型融合中的语义依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模型融合` `语义依赖` `图模型` `Gromov-Wasserstein` `深度学习` `自然语言处理` `推理任务`

## 📋 核心要点

1. 现有的logit融合方法未能有效处理词汇维度之间的语义依赖，导致模型融合效果不佳。
2. 本文提出InfiGFusion，通过Graph-on-Logits Distillation显式建模词汇通道间的交互，提升模型融合的质量与稳定性。
3. 实验结果显示，InfiGFusion在11个基准测试中超越了现有最优模型，尤其在复杂推理任务中表现出色，提升幅度显著。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展推动了将异构开源模型融合为统一系统的努力，以继承其互补优势。现有的基于logit的融合方法虽然保持了推理效率，但独立处理词汇维度，忽视了跨维度交互所编码的语义依赖。为明确建模这些依赖，本文提出了InfiGFusion，这是第一个具有结构感知的融合框架，采用了新颖的Graph-on-Logits Distillation（GLD）损失。通过保留每个输出的前k个logits并聚合其外积，形成全球共激活图，确保了可扩展性和效率。实验表明，GLD在多个融合设置中一致性提升了融合质量和稳定性，InfiGFusion在11个基准测试中超越了现有最优模型，尤其在复杂推理任务中表现突出。

## 🔬 方法详解

**问题定义**：本文旨在解决异构模型融合中词汇维度独立处理所导致的语义依赖缺失问题。现有方法未能有效捕捉模型内部推理过程中的交互关系，影响了融合效果。

**核心思路**：提出InfiGFusion框架，通过Graph-on-Logits Distillation（GLD）损失，显式建模词汇通道之间的交互，利用全局共激活图来增强模型融合的语义理解。

**技术框架**：整体架构包括三个主要模块：1) 保留每个输出的前k个logits；2) 聚合这些logits的外积以构建共激活图；3) 采用排序基础的闭式近似来计算Gromov-Wasserstein距离，确保计算效率。

**关键创新**：GLD损失是本文的核心创新，首次引入结构感知的图模型来处理logits之间的关系，显著提升了融合质量，与传统方法相比，能够更好地捕捉语义依赖。

**关键设计**：设计了排序基础的闭式近似算法，将Gromov-Wasserstein距离的计算复杂度从O(n^4)降低到O(n log n)，并提供了可证明的近似保证，确保了方法的可扩展性和效率。

## 📊 实验亮点

实验结果表明，InfiGFusion在11个基准测试中超越了现有最优模型，尤其在复杂推理任务中表现突出。在Multistep Arithmetic任务上提升了35.6分，在Causal Judgement任务上提升了37.06分，显示出显著的多步和关系推理能力。

## 🎯 应用场景

InfiGFusion的研究成果可广泛应用于自然语言处理、机器翻译、对话系统等领域，尤其在需要融合多种模型以提升性能的场景中具有重要价值。未来，该方法可能推动更高效的模型集成技术的发展，促进智能系统的多样化和智能化。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have intensified efforts to fuse heterogeneous open-source models into a unified system that inherits their complementary strengths. Existing logit-based fusion methods maintain inference efficiency but treat vocabulary dimensions independently, overlooking semantic dependencies encoded by cross-dimension interactions. These dependencies reflect how token types interact under a model's internal reasoning and are essential for aligning models with diverse generation behaviors. To explicitly model these dependencies, we propose \textbf{InfiGFusion}, the first structure-aware fusion framework with a novel \textit{Graph-on-Logits Distillation} (GLD) loss. Specifically, we retain the top-$k$ logits per output and aggregate their outer products across sequence positions to form a global co-activation graph, where nodes represent vocabulary channels and edges quantify their joint activations. To ensure scalability and efficiency, we design a sorting-based closed-form approximation that reduces the original $O(n^4)$ cost of Gromov-Wasserstein distance to $O(n \log n)$, with provable approximation guarantees. Experiments across multiple fusion settings show that GLD consistently improves fusion quality and stability. InfiGFusion outperforms SOTA models and fusion baselines across 11 benchmarks spanning reasoning, coding, and mathematics. It shows particular strength in complex reasoning tasks, with +35.6 improvement on Multistep Arithmetic and +37.06 on Causal Judgement over SFT, demonstrating superior multi-step and relational inference.


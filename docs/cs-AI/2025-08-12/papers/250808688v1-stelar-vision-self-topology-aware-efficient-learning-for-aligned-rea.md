---
layout: default
title: "STELAR-VISION: Self-Topology-Aware Efficient Learning for Aligned Reasoning in Vision"
---

# STELAR-VISION: Self-Topology-Aware Efficient Learning for Aligned Reasoning in Vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08688" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08688v1</a>
  <a href="https://arxiv.org/pdf/2508.08688.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08688v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08688v1', 'STELAR-VISION: Self-Topology-Aware Efficient Learning for Aligned Reasoning in Vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Li, Han Zhang, Zhantao Yang, Fangyi Chen, Zihan Wang, Anudeepsekhar Bolimera, Marios Savvides

**分类**: cs.AI, cs.CV

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出STELAR-VISION以解决多模态推理中的拓扑依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多模态推理` `拓扑感知` `合成数据` `强化学习` `准确性提升` `输出优化`

## 📋 核心要点

1. 现有视觉语言模型在处理复杂多模态任务时，常常生成冗长的输出，且依赖链式推理，限制了其表现。
2. STELAR-Vision通过引入拓扑感知的训练框架和合成数据管道TopoAug，增强了模型的推理能力。
3. 在MATH-V和VLM-S2H上，STELAR-Vision相比基础模型提高了9.7%的准确率，并在多个基准测试中表现优异。

## 📝 摘要（中文）

视觉语言模型（VLMs）在推理方面取得了显著进展，但在复杂的多模态任务中仍面临挑战，尤其是生成冗长输出的问题。现有方法主要依赖链式推理（CoT），而许多任务更适合使用树或图等替代拓扑。为此，本文提出了STELAR-Vision，一个拓扑感知的推理训练框架。其核心是TopoAug，一个合成数据管道，通过多样的拓扑结构丰富训练过程。通过监督微调和强化学习，我们对Qwen2VL模型进行了后训练，兼顾准确性和效率。此外，我们提出了Frugal Learning，旨在以最小的准确性损失减少输出长度。实验结果表明，STELAR-Vision在多个基准测试中显著提升了模型的准确性和泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在复杂多模态任务中生成冗长输出和推理能力不足的问题。现有方法主要依赖链式推理，未能充分利用其他拓扑结构的优势。

**核心思路**：STELAR-Vision通过引入拓扑感知的训练框架，利用多样的拓扑结构来增强模型的推理能力，从而提高准确性和效率。

**技术框架**：该框架包括TopoAug合成数据管道、监督微调和强化学习三个主要模块。TopoAug负责生成多样的拓扑结构数据，监督微调和强化学习则用于优化模型性能。

**关键创新**：STELAR-Vision的核心创新在于其拓扑感知的训练方法，区别于传统的链式推理，能够更好地适应多模态任务的需求。

**关键设计**：在训练过程中，采用了Frugal Learning策略以减少输出长度，同时保持较高的准确性。此外，模型的参数设置和损失函数设计也经过精心调整，以确保最佳的训练效果。

## 📊 实验亮点

STELAR-VISION在MATH-V和VLM-S2H上分别提高了9.7%和7.3%的准确率，且在五个超出分布的基准测试中，表现优于Phi-4-Multimodal-Instruct高达28.4%，显示出强大的泛化能力。此外，相比于仅使用链式训练，整体准确率提升了4.3%。

## 🎯 应用场景

STELAR-VISION的研究成果可广泛应用于多模态推理任务，如图像描述生成、视觉问答和人机交互等领域。其拓扑感知的训练方法能够提升模型在复杂场景下的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Vision-language models (VLMs) have made significant strides in reasoning, yet they often struggle with complex multimodal tasks and tend to generate overly verbose outputs. A key limitation is their reliance on chain-of-thought (CoT) reasoning, despite many tasks benefiting from alternative topologies like trees or graphs. To address this, we introduce STELAR-Vision, a training framework for topology-aware reasoning. At its core is TopoAug, a synthetic data pipeline that enriches training with diverse topological structures. Using supervised fine-tuning and reinforcement learning, we post-train Qwen2VL models with both accuracy and efficiency in mind. Additionally, we propose Frugal Learning, which reduces output length with minimal accuracy loss. On MATH-V and VLM-S2H, STELAR-Vision improves accuracy by 9.7% over its base model and surpasses the larger Qwen2VL-72B-Instruct by 7.3%. On five out-of-distribution benchmarks, it outperforms Phi-4-Multimodal-Instruct by up to 28.4% and LLaMA-3.2-11B-Vision-Instruct by up to 13.2%, demonstrating strong generalization. Compared to Chain-Only training, our approach achieves 4.3% higher overall accuracy on in-distribution datasets and consistently outperforms across all OOD benchmarks. We have released datasets, and code will be available.


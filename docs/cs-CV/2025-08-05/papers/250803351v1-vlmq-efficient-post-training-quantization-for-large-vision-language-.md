---
layout: default
title: "VLMQ: Efficient Post-Training Quantization for Large Vision-Language Models via Hessian Augmentation"
---

# VLMQ: Efficient Post-Training Quantization for Large Vision-Language Models via Hessian Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03351" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03351v1</a>
  <a href="https://arxiv.org/pdf/2508.03351.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03351v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03351v1', 'VLMQ: Efficient Post-Training Quantization for Large Vision-Language Models via Hessian Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yufei Xue, Yushi Huang, Jiawei Shao, Jun Zhang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-08-05

**备注**: 13 pages, 5 figures

---

## 💡 一句话要点

**提出VLMQ以解决视觉语言模型的后训练量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后训练量化` `视觉语言模型` `Hessian优化` `重要性感知` `多模态学习` `模型压缩` `推理加速`

## 📋 核心要点

1. 现有的后训练量化方法在视觉语言模型中应用时，因模态差异导致性能显著下降。
2. 本文提出VLMQ框架，通过优化重要性感知目标和轻量级计算方法，解决视觉标记冗余问题。
3. 在8个基准测试中，VLMQ在低比特量化下表现优异，特别是在MME-RealWorld上提升了16.45%。

## 📝 摘要（中文）

后训练量化（PTQ）已成为压缩大型模型和加速推理的有效方法，但其在视觉语言模型（VLMs）中的应用尚未得到充分探索。本文识别了VLMs中的模态差异，即文本标记有限与视觉标记冗余。现有的基于Hessian的PTQ方法在量化过程中对所有标记一视同仁，导致在VLMs中应用时性能显著下降。为此，本文提出了一种针对VLMs的重视重要性的PTQ框架VLMQ，优化了带有标记级重要性因子的Hessian，并通过轻量级的块级反向传播计算这些因子，确保了效率和有效性。实验证明，VLMQ在多个基准测试中表现出色，尤其是在低比特设置下，取得了16.45%的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型（VLMs）在后训练量化（PTQ）中的性能下降问题，现有Hessian基方法未考虑模态差异，导致量化效果不佳。

**核心思路**：提出VLMQ框架，针对VLMs的特性，优化重要性感知目标，计算标记级重要性因子，以提高量化效果并保持高效性。

**技术框架**：VLMQ包括两个主要模块：1) 重要性感知目标优化，2) 轻量级块级反向传播计算重要性因子，确保与并行权重更新兼容。

**关键创新**：VLMQ通过引入标记级重要性因子，显著改善了Hessian的计算方式，与传统方法相比，能够更有效地处理视觉标记的冗余性。

**关键设计**：在损失函数中引入了重要性因子，采用轻量级的块级反向传播策略，确保计算效率，并通过理论联系指导标记级扰动的计算。

## 📊 实验亮点

VLMQ在8个基准测试中表现出色，特别是在低比特量化设置下，MME-RealWorld任务上实现了16.45%的性能提升，展示了其在视觉语言模型后训练量化中的优越性，超越了现有的主流方法。

## 🎯 应用场景

该研究的潜在应用领域包括视觉问答、图像描述生成和多模态检索等。通过提高视觉语言模型的推理效率和准确性，VLMQ能够在实际应用中显著提升用户体验，推动智能助手和自动化系统的发展。未来，随着模型规模的不断扩大，VLMQ的技术框架可能会在更多领域得到应用，促进多模态AI的进步。

## 📄 摘要（原文）

> Post-training quantization (PTQ) has emerged as an effective approach for compressing large models and accelerating their inference without retraining. While PTQ has been extensively studied in the context of large language models (LLMs), its applicability to vision-language models (VLMs) remains underexplored. In this paper, we identify a modality discrepancy (\emph{i.e.}, limited text tokens \emph{vs.} excessive and redundant vision tokens) of VLMs. However, existing Hessian-based LLM PTQ methods treat all tokens equally during quantization, resulting in severe performance drops when applied to VLMs. Motivated by this observation, we propose a novel importance-aware PTQ framework tailored for VLMs, dubbed VLMQ. Specifically, to address vision token redundancy, VLMQ 1) optimizes an importance-aware objective that yields an enhanced Hessian with token-level importance factors, while retaining compatibility with parallelized weight updates, and 2) ensures efficiency and effectiveness by computing these factors via a single lightweight block-wise backward pass, guided by a theoretical connection to token-level perturbations. Extensive evaluations on 8 benchmarks across 0.5B$\sim$32B VLMs demonstrate the state-of-the-art (SOTA) performance of our VLMQ, particularly under low-bit settings. For example, it achieves a substantial \textbf{16.45\%} improvement on MME-RealWorld under 2-bit quantization.


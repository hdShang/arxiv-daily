---
layout: default
title: AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints
---

# AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16245" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16245v1</a>
  <a href="https://arxiv.org/pdf/2512.16245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16245v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16245v1', 'AlignMerge - Alignment-Preserving Large Language Model Merging via Fisher-Guided Geometric Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aniruddha Roy, Jyoti Patel, Aman Chadha, Vinija Jain, Amitava Das

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**AlignMerge：通过Fisher引导的几何约束实现对齐保持的大语言模型合并**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型合并` `模型对齐` `Fisher信息几何` `安全性` `几何约束`

## 📋 核心要点

1. 现有LLM合并方法在保持模型性能的同时，容易破坏模型的对齐性，导致安全性下降。
2. AlignMerge通过在Fisher-Rao几何空间中施加约束，显式地将对齐作为合并过程中的不变性条件。
3. 实验表明，AlignMerge在多个模型上提高了对齐指标，同时保持或超过了最佳专家的指令遵循和推理能力。

## 📝 摘要（中文）

合并大型语言模型(LLMs)是一种实用的方法，可以在不重新训练的情况下组合来自多个微调检查点的能力。然而，标准方案（线性权重平均、任务向量和Fisher加权平均）可能会在保持损失的同时悄然破坏对齐。我们认为合并不是一种数值技巧，而是一种围绕已对齐锚点的几何约束操作：必须引导融合以尊重安全性几何，而不是事后验证。我们引入AlignMerge，一个几何感知合并框架，它使对齐成为显式不变性。在指令调整基础周围的局部Fisher图中，我们使用投影算子P_A估计对齐子空间并优化：L_AlignMerge = L_geo + lambda_align * L_align + lambda_bud * L_bud，其中L_geo使合并结果在Fisher-Rao几何中接近其专家，L_align惩罚沿对齐敏感方向的运动，L_bud强制执行软对齐预算。作为对齐函数，我们使用解码不变的对齐质量指数(AQI)，这是一个潜在空间标准，可以捕获对齐和未对齐行为在表示空间中分离的清晰程度。在五个模型系列（LLaMA-3 8B、Mistral 7B、Qwen 2、Phi-3.5、Gemma 2）中，将安全锚点与任务专家合并，AlignMerge提高了对齐指标（AQI、毒性、LLM-judge对齐），同时在指令遵循、推理和帮助性方面匹配或超过了最佳专家。与Fisher soups、TIES、SafeMerge和MergeAlign相比，它还表现出更小的对齐子空间漂移和更少的预算违规。这些结果使保持对齐的合并成为首要的设计目标，并为未来基础模型的几何感知组合提供了一条途径。

## 🔬 方法详解

**问题定义**：现有的大语言模型合并方法，如线性权重平均、任务向量等，虽然能够保持模型的性能指标，但往往忽略了模型对齐性，导致合并后的模型可能产生不安全或有害的输出。这些方法缺乏对模型几何结构的考虑，无法保证合并后的模型仍然保持良好的对齐特性。

**核心思路**：AlignMerge的核心思路是将模型合并视为一个在几何空间中受约束的优化问题。它围绕一个已经对齐的“锚点”模型，通过施加几何约束，确保合并后的模型在保持性能的同时，也保持良好的对齐性。这种方法显式地将对齐作为合并过程中的一个不变性条件，避免了事后验证对齐性的不足。

**技术框架**：AlignMerge框架包含以下主要步骤：1. 选择一个已经对齐的“锚点”模型。2. 在锚点模型周围的Fisher图中，估计一个对齐子空间，并计算投影算子P_A。3. 定义一个包含几何约束、对齐约束和预算约束的损失函数L_AlignMerge。4. 通过优化L_AlignMerge，得到合并后的模型。

**关键创新**：AlignMerge的关键创新在于：1. 显式地将对齐作为合并过程中的不变性条件。2. 利用Fisher-Rao几何来约束合并过程，确保合并后的模型在几何空间中接近其专家模型。3. 使用解码不变的对齐质量指数(AQI)作为对齐函数，能够更好地捕捉模型对齐和未对齐行为在表示空间中的分离程度。

**关键设计**：L_AlignMerge损失函数包含三个部分：L_geo用于保持合并结果在Fisher-Rao几何中接近其专家模型；L_align用于惩罚沿对齐敏感方向的运动，防止模型偏离对齐子空间；L_bud用于强制执行软对齐预算，限制模型在未对齐方向上的偏移。lambda_align和lambda_bud是超参数，用于控制对齐约束和预算约束的强度。AQI的计算涉及到在潜在空间中区分对齐和未对齐行为，需要选择合适的正负样本。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16245v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16245v1/figures/mechanistic.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16245v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，AlignMerge在LLaMA-3 8B、Mistral 7B、Qwen 2、Phi-3.5、Gemma 2等多个模型系列上，显著提高了对齐指标（AQI、毒性、LLM-judge对齐），同时在指令遵循、推理和帮助性方面匹配或超过了最佳专家。与Fisher soups、TIES、SafeMerge和MergeAlign等基线方法相比，AlignMerge表现出更小的对齐子空间漂移和更少的预算违规。

## 🎯 应用场景

AlignMerge技术可应用于安全敏感的大语言模型部署场景，例如医疗、金融等领域。通过合并多个具有不同专长的模型，同时保证模型的安全性和可靠性，可以构建更强大、更可信赖的AI系统。该技术还有助于构建更具适应性和可扩展性的模型组合，应对不断变化的任务需求。

## 📄 摘要（原文）

> Merging large language models (LLMs) is a practical way to compose capabilities from multiple fine-tuned checkpoints without retraining. Yet standard schemes (linear weight soups, task vectors, and Fisher-weighted averaging) can preserve loss while quietly destroying alignment. We argue that merging is not a numerical trick but a geometry-constrained operation around an already-aligned anchor: fusion must be steered to respect safety geometry, not validated post hoc.
>   We introduce AlignMerge, a geometry-aware merging framework that makes alignment an explicit invariant. In a local Fisher chart around an instruction-tuned base, we estimate an alignment subspace with projector P_A and optimize:
>   L_AlignMerge = L_geo + lambda_align * L_align + lambda_bud * L_bud,
>   where L_geo keeps the merge close to its experts in Fisher-Rao geometry, L_align penalizes motion along alignment-sensitive directions, and L_bud enforces a soft alignment budget. As the alignment functional we use the decoding-invariant Alignment Quality Index (AQI), a latent-space criterion that captures how cleanly aligned and misaligned behaviors separate in representation space.
>   Across five model families (LLaMA-3 8B, Mistral 7B, Qwen 2, Phi-3.5, Gemma 2), merging safety anchors with task experts, AlignMerge improves alignment metrics (AQI, toxicity, LLM-judge alignment) while matching or exceeding the best expert on instruction-following, reasoning, and helpfulness. It also exhibits smaller alignment-subspace drift and fewer budget violations than Fisher soups, TIES, SafeMerge, and MergeAlign. These results make alignment-preserving merging a first-class design goal and suggest a path to geometry-aware composition of future foundation models.


---
layout: default
title: "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning"
---

# SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05614" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05614v1</a>
  <a href="https://arxiv.org/pdf/2509.05614.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05614v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05614v1', 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanzhen Wang, Jiaming Xu, Jiayi Pan, Yongkang Zhou, Guohao Dai

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-09-06

**备注**: 8pages, 10 figures,

---

## 💡 一句话要点

**SpecPrune-VLA：通过动作感知自适应推测剪枝加速视觉-语言-动作模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `模型剪枝` `动作感知` `模型加速` `机器人` `推理优化`

## 📋 核心要点

1. 现有VLA模型剪枝方法仅依赖当前动作的局部信息，忽略了全局上下文，导致性能下降和加速效果不佳。
2. SpecPrune-VLA利用全局历史和局部上下文进行token选择，通过两级剪枝和动作感知控制实现更智能的剪枝。
3. 实验表明，SpecPrune-VLA在保持成功率的同时，显著提升了VLA模型的推理速度，在A800和3090上分别加速1.46倍和1.57倍。

## 📝 摘要（中文）

本文提出SpecPrune-VLA，一种用于加速视觉-语言-动作(VLA)模型的训练无关方法。现有剪枝方法仅利用当前动作的局部信息进行token剪枝，忽略了来自先前动作的全局上下文，导致成功率显著下降和加速效果受限。SpecPrune-VLA利用局部和全局信息进行更智能的token选择，包含两级剪枝和启发式控制：（1）动作级别的静态剪枝：使用全局历史和局部上下文减少每个动作的视觉token；（2）层级别的动态剪枝：基于层特定的重要性剪枝每层的token；（3）轻量级的动作感知控制器：将动作分类为粗粒度/细粒度，并调整剪枝强度，因为细粒度动作对剪枝更敏感。在LIBERO上的实验表明，SpecPrune-VLA在NVIDIA A800上实现了1.46倍的加速，在NVIDIA GeForce RTX 3090上实现了1.57倍的加速，与OpenVLA-OFT相比，成功率损失可忽略不计。

## 🔬 方法详解

**问题定义**：VLA模型计算量大，推理速度慢。现有剪枝方法在VLA模型上应用时，仅考虑当前动作的局部信息，忽略了历史动作的全局上下文，导致剪枝后模型性能显著下降，无法有效加速。

**核心思路**：利用连续动作之间的高度相似性，结合当前动作的局部信息和历史动作的全局上下文，进行更智能的token选择和剪枝，从而在保证模型性能的同时，提高推理速度。核心在于动作感知的剪枝策略，根据动作的粒度调整剪枝的激进程度。

**技术框架**：SpecPrune-VLA包含三个主要组成部分：动作级别的静态剪枝、层级别的动态剪枝和轻量级的动作感知控制器。静态剪枝在动作层面减少视觉token数量，动态剪枝在层层面根据重要性剪枝token，动作感知控制器根据动作粒度调整剪枝强度。

**关键创新**：SpecPrune-VLA的关键创新在于：1) 结合全局历史和局部上下文进行剪枝；2) 提出两级剪枝策略，分别在动作级别和层级别进行剪枝；3) 设计轻量级的动作感知控制器，根据动作粒度动态调整剪枝强度。与现有方法相比，SpecPrune-VLA能够更有效地平衡模型性能和推理速度。

**关键设计**：动作感知控制器将动作分为粗粒度和细粒度，细粒度动作对剪枝更敏感，因此降低剪枝比例。静态剪枝和动态剪枝的具体比例通过实验确定。损失函数保持不变，因为SpecPrune-VLA是一种训练无关的方法。

## 📊 实验亮点

SpecPrune-VLA在LIBERO数据集上取得了显著的加速效果，在NVIDIA A800上实现了1.46倍的加速，在NVIDIA GeForce RTX 3090上实现了1.57倍的加速，与OpenVLA-OFT相比，成功率损失可忽略不计。这表明SpecPrune-VLA能够在保持模型性能的同时，有效提高VLA模型的推理速度。

## 🎯 应用场景

SpecPrune-VLA可应用于各种需要实时响应的机器人任务，例如自动驾驶、智能制造和家庭服务机器人。通过加速VLA模型的推理速度，可以提高机器人的决策效率和交互能力，使其能够更好地适应复杂多变的环境。

## 📄 摘要（原文）

> Pruning accelerates compute-bound models by reducing computation. Recently applied to Vision-Language-Action (VLA) models, existing methods prune tokens using only local info from current action, ignoring global context from prior actions, causing >20% success rate drop and limited speedup. We observe high similarity across consecutive actions and propose leveraging both local (current) and global (past) info for smarter token selection. We introduce SpecPrune-VLA, a training-free method with two-level pruning and heuristic control: (1) Static pruning at action level: uses global history and local context to reduce visual tokens per action; (2) Dynamic pruning at layer level: prunes tokens per layer based on layer-specific importance; (3) Lightweight action-aware controller: classifies actions as coarse/fine-grained (by speed), adjusting pruning aggressiveness since fine-grained actions are pruning-sensitive. Experiments on LIBERO show SpecPrune-VLA achieves 1.46 times speedup on NVIDIA A800 and 1.57 times on NVIDIA GeForce RTX 3090 vs. OpenVLA-OFT, with negligible success rate loss.


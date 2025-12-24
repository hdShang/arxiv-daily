---
layout: default
title: "AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video"
---

# AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03100" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03100v3</a>
  <a href="https://arxiv.org/pdf/2508.03100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03100v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03100v3', 'AVATAR: Reinforcement Learning to See, Hear, and Reason Over Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yogesh Kulkarni, Pooyan Fazli

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-11-24)

---

## 💡 一句话要点

**提出AVATAR以解决多模态视频推理中的数据效率和信用分配问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态视频推理` `离线训练` `时间优势塑造` `信用分配` `样本效率`

## 📋 核心要点

1. 现有方法在多模态视频推理中存在数据效率低、消失优势和信用分配不均等问题，限制了其性能。
2. AVATAR通过离线训练架构提高样本效率，并引入时间优势塑造策略，优化关键推理阶段的信用分配。
3. AVATAR在MMVU、OmniBench和Video-Holmes等基准测试中超越了Qwen2.5-Omni基线，样本效率提升达到5倍。

## 📝 摘要（中文）

多模态视频的长时间推理面临着时空融合和对齐的挑战。尽管现有方法如群体相对策略优化（GRPO）在此领域表现出一定潜力，但存在数据效率低、消失优势问题以及统一信用分配等三大局限。本文提出了AVATAR（音频-视频对齐与推理代理），通过离线训练架构和时间优势塑造（TAS）策略，显著提高了样本效率和推理步骤的信用分配。AVATAR在多个基准测试中表现优异，超越Qwen2.5-Omni基线，样本效率提升达到5倍，所需生成的完成数量减少80%。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态视频推理中的数据效率低、消失优势和信用分配不均等问题。现有方法如GRPO在这些方面表现不佳，导致学习信号不足。

**核心思路**：AVATAR的核心思路是通过离线训练架构重用过去的经验来提高样本效率，并通过时间优势塑造策略来强调关键推理阶段，从而解决现有方法的局限。

**技术框架**：AVATAR的整体架构包括两个主要模块：离线训练架构和时间优势塑造。离线训练架构通过重用历史经验来提高样本效率，而时间优势塑造则在学习过程中对关键推理阶段进行加权。

**关键创新**：AVATAR的主要创新在于其离线训练架构和时间优势塑造策略，这与现有方法的在线训练和统一信用分配形成鲜明对比，显著提升了学习效率和推理质量。

**关键设计**：在设计上，AVATAR采用了多样化的奖励机制以解决消失优势问题，并在损失函数中引入了对关键推理阶段的加权，以确保模型在学习过程中关注重要的推理步骤。

## 📊 实验亮点

AVATAR在多个基准测试中表现出色，相较于Qwen2.5-Omni基线，MMVU提升5.4分，OmniBench提升4.9分，Video-Holmes提升4.5分。同时，AVATAR展示了5倍的样本效率，达到目标性能所需的生成完成数量减少80%。

## 🎯 应用场景

AVATAR的研究成果在多模态视频理解、智能监控、自动驾驶和人机交互等领域具有广泛的应用潜力。通过提高视频推理的效率和准确性，AVATAR能够为这些领域提供更智能的解决方案，推动相关技术的发展与应用。未来，AVATAR的框架也可能扩展到其他类型的多模态数据分析中。

## 📄 摘要（原文）

> Multimodal reasoning over long-horizon video is challenging due to the need for precise spatiotemporal fusion and alignment across modalities. While recent methods such as Group Relative Policy Optimization (GRPO) have shown promise in this domain, they suffer from three key limitations: (1) data inefficiency from their on-policy design, (2) a vanishing advantage problem, where identical or near-identical rewards within a group eliminate the learning signal by producing zero-valued advantages, and (3) uniform credit assignment that fails to emphasize critical reasoning steps. We introduce $\textbf{AVATAR}$ ($\textbf{A}$udio-$\textbf{V}$ideo $\textbf{A}$gen$\textbf{t}$ for $\textbf{A}$lignment and $\textbf{R}$easoning), a framework that addresses these limitations through two core components: (1) an off-policy training architecture that improves sample efficiency and resolves vanishing advantages by reusing past experiences with greater reward diversity, and (2) Temporal Advantage Shaping (TAS), a novel credit assignment strategy that upweights key reasoning phases during learning. $\textbf{AVATAR}$ achieves strong performance across various benchmarks, outperforming the Qwen2.5-Omni baseline by $\mathbf{+5.4}$ on MMVU, $\mathbf{+4.9}$ on OmniBench, and $\mathbf{+4.5}$ on Video-Holmes, while demonstrating $\textbf{$5$$\times$ sample efficiency}$, requiring $80\%$ fewer generated completions to reach target performance.


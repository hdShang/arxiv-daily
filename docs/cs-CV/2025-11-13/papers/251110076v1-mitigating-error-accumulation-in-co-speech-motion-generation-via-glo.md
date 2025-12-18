---
layout: default
title: Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints
---

# Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10076" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10076v1</a>
  <a href="https://arxiv.org/pdf/2511.10076.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10076v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10076v1', 'Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangyue Zhang, Jianfang Li, Jianqiang Ren, Jiaxu Zhang

**分类**: cs.CV

**发布日期**: 2025-11-13

**备注**: AAAI 2026

**期刊**: AAAI 2026

---

## 💡 一句话要点

**提出GlobalDiff，通过全局旋转扩散和多级约束缓解共语运动生成中的误差累积**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `共语运动生成` `扩散模型` `全局旋转` `多级约束` `误差累积`

## 📋 核心要点

1. 现有共语运动生成方法基于局部关节旋转，存在误差累积，导致末端执行器运动不稳定。
2. GlobalDiff直接在全局关节旋转空间进行扩散，解耦关节依赖，并引入多级约束弥补结构先验缺失。
3. 实验表明，GlobalDiff生成更平滑准确的运动，性能较当前最佳方法提升46.0%。

## 📝 摘要（中文）

可靠的共语运动生成需要精确的运动表示和所有关节之间一致的结构先验。现有的生成方法通常在局部关节旋转上操作，这些旋转是基于骨骼结构分层定义的。这导致生成过程中出现累积误差，表现为末端执行器处的不稳定和不合理的运动。本文提出了GlobalDiff，这是一个基于扩散的框架，首次直接在全局关节旋转空间中操作，从根本上将每个关节的预测与上游依赖关系解耦，并减轻分层误差累积。为了弥补全局旋转空间中结构先验的缺失，我们引入了一种多级约束方案。具体来说，关节结构约束在每个关节周围引入虚拟锚点，以更好地捕捉细粒度的方向。骨骼结构约束强制骨骼之间的角度一致性，以保持结构完整性。时间结构约束利用多尺度变分编码器将生成的运动与真实的时间模式对齐。这些约束共同规范全局扩散过程并加强结构感知。在标准共语基准上的大量评估表明，GlobalDiff生成平滑而准确的运动，在多个说话人身份下，与当前SOTA相比，性能提高了46.0%。

## 🔬 方法详解

**问题定义**：现有共语运动生成方法依赖于局部关节旋转，这些旋转是分层定义的，导致误差在骨骼链上传播和累积，最终使得末端执行器的运动不自然、不稳定。这种分层依赖关系使得下游关节的运动预测严重依赖于上游关节的准确性，任何微小的误差都会被放大。

**核心思路**：GlobalDiff的核心思路是直接在全局关节旋转空间中进行运动生成，从而消除关节之间的分层依赖关系。通过将每个关节的运动预测与其他关节解耦，可以避免误差累积。为了弥补全局旋转空间中结构信息的缺失，引入多级约束来保证生成运动的合理性和结构完整性。

**技术框架**：GlobalDiff是一个基于扩散模型的框架，包含以下主要模块：1) 全局旋转扩散模块：直接在全局关节旋转空间中进行扩散和反向扩散过程，生成运动序列。2) 关节结构约束：在每个关节周围引入虚拟锚点，通过约束关节与锚点之间的关系来捕捉细粒度的方向信息。3) 骨骼结构约束：强制骨骼之间的角度一致性，保证骨骼结构的合理性。4) 时间结构约束：使用多尺度变分编码器学习真实运动的时间模式，并将其作为约束来引导生成过程。

**关键创新**：GlobalDiff最重要的技术创新在于首次将扩散模型应用于全局关节旋转空间，从而解决了传统方法中存在的误差累积问题。此外，多级约束方案有效地弥补了全局旋转空间中结构信息的缺失，保证了生成运动的质量。

**关键设计**：关节结构约束通过在每个关节周围均匀分布若干个虚拟锚点，并计算关节旋转矩阵与锚点之间的距离损失来实现。骨骼结构约束通过计算相邻骨骼之间的角度，并约束其与真实运动的角度一致来实现。时间结构约束使用一个多尺度变分编码器来学习真实运动的时间模式，并使用KL散度损失来约束生成运动的时间分布。

## 📊 实验亮点

GlobalDiff在标准共语基准测试中取得了显著的性能提升，与当前最先进的方法相比，性能提高了46.0%。实验结果表明，GlobalDiff能够生成更平滑、更准确的共语运动，有效地解决了误差累积问题。此外，消融实验验证了多级约束方案的有效性，表明每个约束都对最终性能有贡献。

## 🎯 应用场景

该研究成果可应用于虚拟人动画、游戏角色控制、人机交互等领域。通过生成更自然、流畅的共语运动，可以提升用户体验，增强虚拟角色的表现力。未来，该技术有望应用于更复杂的场景，例如虚拟会议、远程协作等，实现更逼真的人机交互。

## 📄 摘要（原文）

> Reliable co-speech motion generation requires precise motion representation and consistent structural priors across all joints. Existing generative methods typically operate on local joint rotations, which are defined hierarchically based on the skeleton structure. This leads to cumulative errors during generation, manifesting as unstable and implausible motions at end-effectors. In this work, we propose GlobalDiff, a diffusion-based framework that operates directly in the space of global joint rotations for the first time, fundamentally decoupling each joint's prediction from upstream dependencies and alleviating hierarchical error accumulation. To compensate for the absence of structural priors in global rotation space, we introduce a multi-level constraint scheme. Specifically, a joint structure constraint introduces virtual anchor points around each joint to better capture fine-grained orientation. A skeleton structure constraint enforces angular consistency across bones to maintain structural integrity. A temporal structure constraint utilizes a multi-scale variational encoder to align the generated motion with ground-truth temporal patterns. These constraints jointly regularize the global diffusion process and reinforce structural awareness. Extensive evaluations on standard co-speech benchmarks show that GlobalDiff generates smooth and accurate motions, improving the performance by 46.0 % compared to the current SOTA under multiple speaker identities.


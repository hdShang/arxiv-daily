---
layout: default
title: "TaoCache: Structure-Maintained Video Generation Acceleration"
---

# TaoCache: Structure-Maintained Video Generation Acceleration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08978" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08978v1</a>
  <a href="https://arxiv.org/pdf/2508.08978.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08978v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08978v1', 'TaoCache: Structure-Maintained Video Generation Acceleration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhentao Fan, Zongzuo Wang, Weiwei Zhang

**分类**: cs.CV

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出TaoCache以解决视频生成加速中的结构一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `缓存加速` `去噪模型` `结构一致性` `深度学习`

## 📋 核心要点

1. 现有的缓存加速方法在视频生成中跳过早期或中期去噪步骤，导致结构不一致性，影响生成质量。
2. TaoCache采用固定点视角预测噪声输出，通过校准噪声增量的余弦相似度和范数比，保持高分辨率结构。
3. 在多个数据集上，TaoCache在相同加速条件下显著提高了视觉质量，超越了以往的缓存方法。

## 📝 摘要（中文）

现有基于缓存的视频扩散模型加速方法主要跳过早期或中期去噪步骤，这常常导致生成结果与完整时间步之间存在结构差异，影响指令遵循和角色一致性。本文提出了TaoCache，这是一种无需训练的即插即用缓存策略，采用固定点视角预测模型的噪声输出，特别有效于后期去噪阶段。通过校准连续噪声增量的余弦相似度和范数比，TaoCache在实现激进跳过的同时保持高分辨率结构。该方法与Pyramid Attention Broadcast (PAB)和TeaCache等补充加速方法是正交的，并能无缝集成到基于DiT的框架中。在Latte-1、OpenSora-Plan v110和Wan2.1上，TaoCache在相同加速条件下显著提高了视觉质量（LPIPS、SSIM、PSNR）。

## 🔬 方法详解

**问题定义**：现有的缓存加速方法在视频生成过程中常常跳过早期或中期的去噪步骤，导致生成结果与完整时间步之间存在结构差异。这种差异不仅影响了生成的视觉质量，还可能妨碍指令遵循和角色一致性，限制了模型的实际应用。

**核心思路**：TaoCache提出了一种新的缓存策略，采用固定点视角来预测模型的噪声输出，而不是依赖于残差缓存。这种方法特别关注后期去噪阶段，通过校准连续噪声增量的余弦相似度和范数比，能够在保持高分辨率结构的同时实现激进的跳过。

**技术框架**：TaoCache的整体架构包括噪声预测模块和结构保持模块。噪声预测模块负责生成噪声输出，而结构保持模块则通过校准噪声增量的相似度和范数比来确保生成结果的结构一致性。该方法可以无缝集成到基于DiT的框架中，增强其加速能力。

**关键创新**：TaoCache的主要创新在于其固定点视角的噪声预测方法，这与传统的残差缓存方法有本质区别。通过这种新颖的设计，TaoCache能够在加速生成的同时保持高质量的视觉结构，解决了以往方法的不足。

**关键设计**：在TaoCache中，关键的参数设置包括噪声增量的余弦相似度和范数比的校准。这些设计细节确保了在加速生成的同时，能够有效保持生成结果的高分辨率和结构一致性。

## 📊 实验亮点

在Latte-1、OpenSora-Plan v110和Wan2.1数据集上，TaoCache在相同加速条件下显著提高了视觉质量，具体表现为LPIPS、SSIM和PSNR等指标均优于以往的缓存方法，展示了其在视频生成领域的强大性能。

## 🎯 应用场景

TaoCache的研究成果在视频生成、动画制作和虚拟现实等领域具有广泛的应用潜力。通过提高视频生成的效率和质量，该方法能够为实时视频处理和高质量内容创作提供支持，推动相关技术的发展和应用。未来，TaoCache可能会在更复杂的生成任务中展现出更大的价值。

## 📄 摘要（原文）

> Existing cache-based acceleration methods for video diffusion models primarily skip early or mid denoising steps, which often leads to structural discrepancies relative to full-timestep generation and can hinder instruction following and character consistency. We present TaoCache, a training-free, plug-and-play caching strategy that, instead of residual-based caching, adopts a fixed-point perspective to predict the model's noise output and is specifically effective in late denoising stages. By calibrating cosine similarities and norm ratios of consecutive noise deltas, TaoCache preserves high-resolution structure while enabling aggressive skipping. The approach is orthogonal to complementary accelerations such as Pyramid Attention Broadcast (PAB) and TeaCache, and it integrates seamlessly into DiT-based frameworks. Across Latte-1, OpenSora-Plan v110, and Wan2.1, TaoCache attains substantially higher visual quality (LPIPS, SSIM, PSNR) than prior caching methods under the same speedups.


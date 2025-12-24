---
layout: default
title: "Revisit What You See: Disclose Language Prior in Vision Tokens for LVLM Decoding"
---

# Revisit What You See: Disclose Language Prior in Vision Tokens for LVLM Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09522" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09522v2</a>
  <a href="https://arxiv.org/pdf/2506.09522.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09522v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09522v2', 'Revisit What You See: Disclose Language Prior in Vision Tokens for LVLM Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Beomsik Cho, Jaehyung Kim

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-11 (更新: 2025-10-11)

**备注**: Code available at https://github.com/bscho333/ReVisiT

---

## 💡 一句话要点

**提出ReVisiT以解决视觉信息在LVLM解码中的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多模态任务` `文本生成` `视觉信息` `解码优化`

## 📋 核心要点

1. 现有大型视觉语言模型在解码过程中对视觉信息的利用不足，导致频繁的幻觉现象。
2. 本文提出ReVisiT方法，通过参考视觉标记来引导文本生成，优化解码过程。
3. 在五个基准测试中，ReVisiT显著提升了视觉定位效果，并将计算成本降低了多达2倍。

## 📝 摘要（中文）

大型视觉语言模型（LVLM）通过整合视觉感知与语言理解，在多模态任务中表现出色。然而，视觉信息在模型解码过程中的贡献仍未得到充分探讨，导致频繁的幻觉现象。通过一系列分析，研究发现视觉标记在幻觉发生时仍提供有意义的视觉信息，并且其语义在适当的词汇约束下可以在文本空间中显现。基于这些观察，本文提出了一种简单的无训练解码方法ReVisiT，该方法参考视觉标记来指导文本生成。ReVisiT通过上下文感知的约束散度最小化动态选择最相关的视觉标记，并利用其约束投影来优化输出分布，从而更好地融入视觉语义。实验结果表明，ReVisiT在五个基准测试中持续提升视觉定位，且计算开销最小，性能与最先进的解码基线相当或更优，同时计算成本降低了多达2倍。

## 🔬 方法详解

**问题定义**：本文旨在解决大型视觉语言模型在解码过程中对视觉信息利用不足的问题，现有方法在幻觉现象频繁出现时，未能有效利用视觉信息。

**核心思路**：ReVisiT方法通过动态选择与当前解码上下文最相关的视觉标记，利用其语义信息来优化文本生成过程，从而提升视觉语义的融入效果。

**技术框架**：ReVisiT的整体架构包括视觉标记的选择模块和文本生成优化模块。选择模块通过上下文感知的约束散度最小化来动态选择视觉标记，而生成优化模块则利用选择的视觉标记对文本输出分布进行约束投影。

**关键创新**：ReVisiT的主要创新在于其无训练的解码方法，通过视觉标记的语义信息来指导文本生成，显著改善了现有方法在视觉信息利用上的不足。

**关键设计**：在设计中，ReVisiT采用了上下文感知的约束散度最小化策略，确保选择的视觉标记与当前解码上下文高度相关，同时通过约束投影优化输出分布，以更好地融入视觉语义。

## 📊 实验亮点

实验结果显示，ReVisiT在五个基准测试中均显著提升了视觉定位效果，相较于最先进的解码基线，性能相当或更优，同时计算成本降低了多达2倍，展示了其在效率和效果上的双重优势。

## 🎯 应用场景

该研究的潜在应用领域包括多模态内容生成、视觉问答系统以及智能助手等。通过提升视觉信息的利用效率，ReVisiT能够在实际应用中提供更准确的文本生成和更好的用户体验，未来可能对人机交互和自动化内容创作产生深远影响。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) achieve strong performance across multimodal tasks by integrating visual perception with language understanding. However, how vision information contributes to the model's decoding process remains under-explored, as reflected in frequent hallucinations. Through a series of analyses, we found that (i) vision tokens provide meaningful visual information even when hallucinations occur, and (ii) their semantics are encoded in the textual space and become explicit under appropriate vocabulary constraints. Building on these observations, we propose ReVisiT, a simple training-free decoding method that references vision tokens to guide text generation. Our approach leverages the semantic information embedded within vision tokens by projecting them into the text token distribution. Specifically, ReVisiT dynamically selects the most relevant vision token at each decoding step via context-aware constrained divergence minimization, and using its constrained projection to refine the output distribution to better incorporate visual semantics. Across five benchmarks on recent LVLMs, ReVisiT consistently enhances visual grounding with minimal computational overhead, and achieves competitive or superior results to state-of-the-art decoding baselines while reducing computational cost by up to $2\times$.


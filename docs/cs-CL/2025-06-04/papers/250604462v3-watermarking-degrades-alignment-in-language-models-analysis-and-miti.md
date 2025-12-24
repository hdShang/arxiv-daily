---
layout: default
title: "Watermarking Degrades Alignment in Language Models: Analysis and Mitigation"
---

# Watermarking Degrades Alignment in Language Models: Analysis and Mitigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04462" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04462v3</a>
  <a href="https://arxiv.org/pdf/2506.04462.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04462v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04462v3', 'Watermarking Degrades Alignment in Language Models: Analysis and Mitigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Apurv Verma, NhatHai Phan, Shubhendu Trivedi

**分类**: cs.CL, cs.CR, cs.LG

**发布日期**: 2025-06-04 (更新: 2025-07-12)

**备注**: Published at the 1st Workshop on GenAI Watermarking (ICLR 2025). Code: https://github.com/dapurv5/alignmark

**期刊**: 1st Workshop on GenAI Watermarking, ICLR 2025

---

## 💡 一句话要点

**提出对抗水印影响的对齐恢复方法以提升语言模型性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水印技术` `语言模型` `对齐恢复` `奖励模型` `自然语言处理` `模型安全性` `输出质量` `实验分析`

## 📋 核心要点

1. 现有水印技术对语言模型的输出质量造成负面影响，尤其在真实度和安全性方面的影响尚未被充分探讨。
2. 提出对齐重采样（AR）方法，通过外部奖励模型在推理时恢复模型的对齐性能，解决水印带来的降级问题。
3. 实验结果表明，使用AR方法能够在水印情况下有效恢复或超越基线对齐分数，且保持水印的可检测性。

## 📝 摘要（中文）

水印技术对大型语言模型（LLMs）的输出质量有显著影响，但其对真实度、安全性和有用性的影响尚未得到充分研究。本文系统分析了两种流行的水印方法——Gumbel和KGW——如何影响四个对齐LLMs的核心对齐属性。实验揭示了两种不同的降级模式：保护衰减和保护增强。为缓解这些降级，提出了对齐重采样（AR）方法，通过外部奖励模型在推理时恢复对齐。实验表明，采样2-4个水印生成的结果能够有效恢复或超越基线对齐分数，确保水印的可检测性。此研究揭示了水印强度与模型对齐之间的关键平衡，为负责任地部署水印LLMs提供了简单的推理时解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决水印技术对大型语言模型对齐性能的负面影响，现有方法在提升有用性与保持安全性之间存在矛盾。

**核心思路**：提出对齐重采样（AR）方法，通过在推理阶段引入外部奖励模型，恢复模型的对齐性能，缓解水印带来的负面影响。

**技术框架**：AR方法在推理时对水印生成的结果进行重采样，结合外部奖励模型评估生成结果的对齐程度，确保生成结果的多样性与可检测性。

**关键创新**：AR方法的核心创新在于通过外部奖励模型的引入，解决了水印技术导致的对齐性能下降问题，与传统水印方法相比，提供了更为灵活的解决方案。

**关键设计**：在AR方法中，采样的水印生成数量设置为2-4个，以确保有效恢复对齐分数，同时在设计中牺牲了一定的失真自由度，以保持水印的强检测性。

## 📊 实验亮点

实验结果显示，使用对齐重采样（AR）方法能够在水印情况下有效恢复或超越基线对齐分数，具体而言，采样2-4个水印生成结果时，能够显著提升对齐性能，确保水印的可检测性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和内容生成等。通过有效地恢复水印LLMs的对齐性能，研究为负责任地使用水印技术提供了理论基础和实践指导，促进了安全和可靠的AI应用发展。

## 📄 摘要（原文）

> Watermarking techniques for large language models (LLMs) can significantly impact output quality, yet their effects on truthfulness, safety, and helpfulness remain critically underexamined. This paper presents a systematic analysis of how two popular watermarking approaches-Gumbel and KGW-affect these core alignment properties across four aligned LLMs. Our experiments reveal two distinct degradation patterns: guard attenuation, where enhanced helpfulness undermines model safety, and guard amplification, where excessive caution reduces model helpfulness. These patterns emerge from watermark-induced shifts in token distribution, surfacing the fundamental tension that exists between alignment objectives.
>   To mitigate these degradations, we propose Alignment Resampling (AR), an inference-time sampling method that uses an external reward model to restore alignment. We establish a theoretical lower bound on the improvement in expected reward score as the sample size is increased and empirically demonstrate that sampling just 2-4 watermarked generations effectively recovers or surpasses baseline (unwatermarked) alignment scores. To overcome the limited response diversity of standard Gumbel watermarking, our modified implementation sacrifices strict distortion-freeness while maintaining robust detectability, ensuring compatibility with AR. Experimental results confirm that AR successfully recovers baseline alignment in both watermarking approaches, while maintaining strong watermark detectability. This work reveals the critical balance between watermark strength and model alignment, providing a simple inference-time solution to responsibly deploy watermarked LLMs in practice.


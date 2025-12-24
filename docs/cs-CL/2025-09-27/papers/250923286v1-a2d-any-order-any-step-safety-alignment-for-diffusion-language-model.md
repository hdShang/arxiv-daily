---
layout: default
title: "A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models"
---

# A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23286" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23286v1</a>
  <a href="https://arxiv.org/pdf/2509.23286.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23286v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23286v1', 'A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wonje Jeung, Sangyeon Yoon, Yoonjun Cho, Dongjae Jeon, Sangwoo Shin, Hyesoo Hong, Albert No

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

**备注**: Code and models are available at https://ai-isl.github.io/A2D

---

## 💡 一句话要点

**提出A2D以解决扩散语言模型的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `安全性对齐` `令牌级防御` `实时监控` `有害内容检测` `生成模型` `自动回复系统`

## 📋 核心要点

1. 现有的扩散大型语言模型在生成内容时灵活性高，但也因此容易受到各种攻击，尤其是有害内容的生成。
2. A2D通过令牌级对齐机制，确保在生成过程中一旦检测到有害内容就发出拒绝信号，从而增强模型的安全性。
3. 实验结果表明，A2D显著降低了DIJA攻击的成功率，并提高了安全终止的速度，展现出良好的实用性和有效性。

## 📝 摘要（中文）

扩散大型语言模型（dLLMs）允许任意顺序生成，但这种灵活性扩大了攻击面：有害内容可能出现在任意位置，基于模板的预填充攻击如DIJA能够绕过响应级拒绝。本文提出A2D（任意顺序、任意步骤防御），一种令牌级对齐方法，确保dLLMs在出现有害内容时发出[EOS]拒绝信号。通过在随机掩蔽下直接对齐安全性，A2D对任意解码顺序和任意步骤的预填充攻击表现出鲁棒性，并支持实时监控：dLLMs可以开始响应，但在出现不安全的延续时自动终止。在安全基准测试中，A2D始终防止有害输出的生成，将DIJA的成功率从80%以上降低到接近零（LLaDA-8B-Instruct为1.3%，Dream-v0-Instruct-7B为0.0%），阈值化的[EOS]概率允许早期拒绝，实现高达19.3倍的安全终止速度提升。

## 🔬 方法详解

**问题定义**：本文旨在解决扩散大型语言模型在生成过程中可能出现的有害内容问题。现有方法在面对任意顺序和任意步骤的攻击时，缺乏有效的防御机制，导致安全性不足。

**核心思路**：A2D的核心思路是通过令牌级的对齐方法，确保模型在生成有害内容时能够及时发出拒绝信号。通过随机掩蔽的方式，A2D能够在多种攻击条件下保持鲁棒性。

**技术框架**：A2D的整体架构包括令牌级对齐模块和实时监控模块。令牌级对齐模块负责检测和对齐有害内容，而实时监控模块则在生成过程中监控内容的安全性，一旦发现不安全的延续，立即终止生成。

**关键创新**：A2D的主要创新在于其令牌级对齐机制，使得模型能够在生成的每一步都进行安全性检查。这一设计与现有的响应级拒绝机制有本质区别，后者只能在生成结束后进行判断。

**关键设计**：在A2D中，采用了随机掩蔽技术来增强模型的鲁棒性，并通过阈值化的[EOS]概率实现早期拒绝。此外，模型的损失函数设计也考虑了安全性与生成质量的平衡。

## 📊 实验亮点

实验结果显示，A2D在安全基准测试中表现优异，将DIJA攻击的成功率从80%以上降低至接近零（LLaDA-8B-Instruct为1.3%，Dream-v0-Instruct-7B为0.0%）。此外，A2D的阈值化[EOS]概率设计使得安全终止速度提升高达19.3倍，显著提高了模型的实用性和响应效率。

## 🎯 应用场景

A2D的研究成果在多个领域具有广泛的应用潜力，尤其是在需要生成安全内容的场景，如自动回复系统、内容生成平台和社交媒体监控等。通过增强模型的安全性，A2D能够有效防止有害内容的传播，提升用户体验和信任度。未来，A2D的技术也可能被进一步推广到其他类型的生成模型中，推动更安全的人工智能应用发展。

## 📄 摘要（原文）

> Diffusion large language models (dLLMs) enable any-order generation, but this flexibility enlarges the attack surface: harmful spans may appear at arbitrary positions, and template-based prefilling attacks such as DIJA bypass response-level refusals. We introduce A2D (Any-Order, Any-Step Defense), a token-level alignment method that aligns dLLMs to emit an [EOS] refusal signal whenever harmful content arises. By aligning safety directly at the token-level under randomized masking, A2D achieves robustness to both any-decoding-order and any-step prefilling attacks under various conditions. It also enables real-time monitoring: dLLMs may begin a response but automatically terminate if unsafe continuation emerges. On safety benchmarks, A2D consistently prevents the generation of harmful outputs, slashing DIJA success rates from over 80% to near-zero (1.3% on LLaDA-8B-Instruct, 0.0% on Dream-v0-Instruct-7B), and thresholded [EOS] probabilities allow early rejection, yielding up to 19.3x faster safe termination.


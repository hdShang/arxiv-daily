---
layout: default
title: "FLASH: Latent-Aware Semi-Autoregressive Speculative Decoding for Multimodal Tasks"
---

# FLASH: Latent-Aware Semi-Autoregressive Speculative Decoding for Multimodal Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12728" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12728v2</a>
  <a href="https://arxiv.org/pdf/2505.12728.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12728v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12728v2', 'FLASH: Latent-Aware Semi-Autoregressive Speculative Decoding for Multimodal Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihua Wang, Ruibo Li, Haozhe Du, Joey Tianyi Zhou, Yu Zhang, Xu Yang

**分类**: cs.CV, cs.MM

**发布日期**: 2025-05-19 (更新: 2025-05-25)

**备注**: This preprint is under review

**🔗 代码/项目**: [GITHUB](https://github.com/ZihuaEvan/FlashSD/)

---

## 💡 一句话要点

**提出FLASH以解决多模态任务中的解码速度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `投机解码` `潜在感知` `半自回归` `视觉输入` `解码速度` `视频理解`

## 📋 核心要点

1. 现有的投机解码方法在多模态模型中未能充分利用视觉输入的特性，导致解码速度慢。
2. 本文提出FLASH框架，通过潜在感知标记压缩和半自回归解码策略，优化多模态数据的解码过程。
3. 实验结果显示，FLASH在多模态任务中显著优于现有方法，实现了高达2.68倍的速度提升。

## 📝 摘要（中文）

大型语言模型（LLMs）和多模态模型（LMMs）在推理能力上表现出色，但解码速度较慢的问题依然存在。尤其在LMMs中，视觉输入通常包含更多的标记且信息密度较低。现有的投机解码方法虽然能加速LLM推理，但在LMMs中未能充分考虑视觉输入的独特特性。本文提出FLASH（快速潜在感知半自回归启发式），专为LMMs设计的投机解码框架，通过轻量级的潜在感知标记压缩机制和半自回归解码策略，显著提高了解码速度，同时保持高接受率。实验表明，FLASH在视频字幕生成和视觉指令调优任务中，分别实现了2.68倍和2.55倍的速度提升。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态模型（LMMs）在解码速度上的瓶颈，现有方法主要依赖文本模型，未能充分考虑视觉输入的特点，导致效率低下。

**核心思路**：FLASH框架通过引入潜在感知标记压缩机制，减少视觉标记的冗余，同时采用半自回归解码策略，在一次前向传播中生成多个标记，从而加速解码过程。

**技术框架**：FLASH的整体架构包括两个主要模块：潜在感知标记压缩模块和半自回归解码模块。前者负责优化视觉输入的标记表示，后者则通过生成多个候选标记来提高解码效率。

**关键创新**：FLASH的创新之处在于其专为多模态任务设计的投机解码策略，充分利用了视觉数据的特性，与传统方法相比，显著提升了解码速度和效率。

**关键设计**：在设计中，采用了轻量级的潜在感知标记压缩算法，以降低视觉标记的冗余，同时在半自回归解码中，设置了合理的生成策略，以确保生成标记的质量和速度。通过这些设计，FLASH实现了高效的解码过程。

## 📊 实验亮点

实验结果表明，FLASH在视频字幕生成任务中实现了2.68倍的速度提升，在视觉指令调优任务中实现了2.55倍的速度提升，显著优于现有的投机解码方法，展示了其在多模态任务中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括视频理解、图像描述生成和视觉指令执行等多模态任务。通过提高解码速度，FLASH能够在实时系统中发挥重要作用，提升用户体验和系统效率，未来可能在智能助手、自动驾驶等领域产生深远影响。

## 📄 摘要（原文）

> Large language and multimodal models (LLMs and LMMs) exhibit strong inference capabilities but are often limited by slow decoding speeds. This challenge is especially acute in LMMs, where visual inputs typically comprise more tokens with lower information density than text -- an issue exacerbated by recent trends toward finer-grained visual tokenizations to boost performance. Speculative decoding has been effective in accelerating LLM inference by using a smaller draft model to generate candidate tokens, which are then selectively verified by the target model, improving speed without sacrificing output quality. While this strategy has been extended to LMMs, existing methods largely overlook the unique properties of visual inputs and depend solely on text-based draft models. In this work, we propose \textbf{FLASH} (Fast Latent-Aware Semi-Autoregressive Heuristics), a speculative decoding framework designed specifically for LMMs, which leverages two key properties of multimodal data to design the draft model. First, to address redundancy in visual tokens, we propose a lightweight latent-aware token compression mechanism. Second, recognizing that visual objects often co-occur within a scene, we employ a semi-autoregressive decoding strategy to generate multiple tokens per forward pass. These innovations accelerate draft decoding while maintaining high acceptance rates, resulting in faster overall inference. Experiments show that FLASH significantly outperforms prior speculative decoding approaches in both unimodal and multimodal settings, achieving up to \textbf{2.68$\times$} speed-up on video captioning and \textbf{2.55$\times$} on visual instruction tuning tasks compared to the original LMM. Our code is available \href{https://github.com/ZihuaEvan/FlashSD/}{[here]}.


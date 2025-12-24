---
layout: default
title: HDGlyph: A Hierarchical Disentangled Glyph-Based Framework for Long-Tail Text Rendering in Diffusion Models
---

# HDGlyph: A Hierarchical Disentangled Glyph-Based Framework for Long-Tail Text Rendering in Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06543" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06543v1</a>
  <a href="https://arxiv.org/pdf/2505.06543.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06543v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06543v1', 'HDGlyph: A Hierarchical Disentangled Glyph-Based Framework for Long-Tail Text Rendering in Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhan Zhuang, Mengqi Huang, Fengyi Fu, Nan Chen, Bohan Lei, Zhendong Mao

**分类**: cs.CV

**发布日期**: 2025-05-10

---

## 💡 一句话要点

**提出HDGlyph框架以解决长尾文本渲染问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `长尾文本渲染` `字形框架` `视觉合成` `文本生成` `深度学习`

## 📋 核心要点

1. 现有方法在处理长尾文本时表现不佳，尤其是未见或小尺寸文本的渲染效果较差。
2. HDGlyph框架通过分层解耦文本生成与视觉合成，联合优化常见和长尾文本的渲染效果。
3. 实验结果显示，HDGlyph在英语和中文文本渲染中分别提高了5.08%和11.7%的准确率，且在长尾场景中表现优异。

## 📝 摘要（中文）

视觉文本渲染旨在将指定的文本内容准确整合到生成的图像中，这在商业设计等多个应用中至关重要。尽管近期取得了一些进展，但现有方法在处理长尾文本时，尤其是未见或小尺寸文本时仍面临挑战。本文提出了一种新颖的分层解耦字形框架HDGlyph，该框架将文本生成与非文本视觉合成进行分层解耦，从而实现对常见文本和长尾文本渲染的联合优化。在训练阶段，HDGlyph通过多语言字形网络和字形感知感知损失解耦像素级表示，确保即使对于未见字符也能实现稳健渲染。在推理阶段，HDGlyph应用噪声解耦无分类引导和潜在解耦两阶段渲染方案，精细化背景和小尺寸文本。广泛评估表明，该模型在英语和中文文本渲染中分别提高了5.08%和11.7%的准确率，同时保持高图像质量，并在长尾场景中表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉文本渲染方法在长尾文本处理中的不足，尤其是未见字符和小尺寸文本的渲染效果差。

**核心思路**：HDGlyph框架通过分层解耦的方式，将文本生成与非文本视觉合成分开处理，从而实现对不同类型文本的优化。这样的设计使得模型能够更好地处理长尾文本和未见字符。

**技术框架**：HDGlyph的整体架构包括训练阶段的多语言字形网络和字形感知损失，以及推理阶段的噪声解耦无分类引导和潜在解耦两阶段渲染方案。

**关键创新**：HDGlyph的主要创新在于其分层解耦的设计，使得文本生成与视觉合成可以独立优化，这与现有方法的单一处理方式有本质区别。

**关键设计**：在训练中，使用了多语言字形网络来解耦像素级表示，并引入字形感知损失以增强模型对未见字符的鲁棒性。推理阶段则采用了噪声解耦的引导策略和两阶段渲染方案，以提升小尺寸文本的渲染质量。

## 📊 实验亮点

实验结果表明，HDGlyph在英语和中文文本渲染中分别提高了5.08%和11.7%的准确率，显著优于其他方法。同时，该模型在长尾场景中表现出色，展现了强大的准确性和视觉效果。

## 🎯 应用场景

HDGlyph框架在商业设计、广告创作以及任何需要高质量文本渲染的视觉内容生成领域具有广泛的应用潜力。其创新的解耦设计不仅提升了文本渲染的准确性，还为未来的文本生成模型提供了新的思路，可能推动相关领域的进一步研究与发展。

## 📄 摘要（原文）

> Visual text rendering, which aims to accurately integrate specified textual content within generated images, is critical for various applications such as commercial design. Despite recent advances, current methods struggle with long-tail text cases, particularly when handling unseen or small-sized text. In this work, we propose a novel Hierarchical Disentangled Glyph-Based framework (HDGlyph) that hierarchically decouples text generation from non-text visual synthesis, enabling joint optimization of both common and long-tail text rendering. At the training stage, HDGlyph disentangles pixel-level representations via the Multi-Linguistic GlyphNet and the Glyph-Aware Perceptual Loss, ensuring robust rendering even for unseen characters. At inference time, HDGlyph applies Noise-Disentangled Classifier-Free Guidance and Latent-Disentangled Two-Stage Rendering (LD-TSR) scheme, which refines both background and small-sized text. Extensive evaluations show our model consistently outperforms others, with 5.08% and 11.7% accuracy gains in English and Chinese text rendering while maintaining high image quality. It also excels in long-tail scenarios with strong accuracy and visual performance.


---
layout: default
title: "LexiMark: Robust Watermarking via Lexical Substitutions to Enhance Membership Verification of an LLM's Textual Training Data"
---

# LexiMark: Robust Watermarking via Lexical Substitutions to Enhance Membership Verification of an LLM's Textual Training Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14474" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14474v2</a>
  <a href="https://arxiv.org/pdf/2506.14474.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14474v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14474v2', 'LexiMark: Robust Watermarking via Lexical Substitutions to Enhance Membership Verification of an LLM\'s Textual Training Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eyal German, Sagiv Antebi, Edan Habler, Asaf Shabtai, Yuval Elovici

**分类**: cs.CL, cs.CR

**发布日期**: 2025-06-17 (更新: 2025-10-05)

---

## 💡 一句话要点

**提出LexiMark以增强LLM训练数据的水印验证**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水印技术` `大型语言模型` `数据验证` `同义词替换` `知识产权保护` `模型训练` `隐蔽性技术`

## 📋 核心要点

1. 现有的数据集水印方法缺乏隐蔽性，容易被检测和移除，导致验证LLM训练数据的困难。
2. LexiMark通过对高熵词进行同义词替换，增强了LLM对水印文本的记忆能力，同时保持文本的语义完整性。
3. 实验结果表明，LexiMark在多个训练设置下的AUROC评分显著提高，验证了其在水印数据使用检测中的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）可能在未经所有者同意的情况下使用数据进行训练或微调。验证特定LLM是否在特定数据实例或整个数据集上训练极具挑战性。数据集水印通过在训练数据中嵌入可识别的修改来解决这一问题，以检测未经授权的使用。然而，现有方法往往缺乏隐蔽性，容易被检测和移除。为此，本文提出了一种新颖的水印技术LexiMark，旨在通过对精心选择的高熵词进行同义词替换来增强LLM对水印文本的记忆能力，而不改变文本的语义完整性。实验结果显示，与现有方法相比，AUROC评分显著提高，证明了该方法在可靠验证未经授权的水印数据是否用于LLM训练中的有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型训练数据的水印验证问题，现有方法由于缺乏隐蔽性，容易被检测和移除，导致验证过程的复杂性和不可靠性。

**核心思路**：LexiMark的核心思路是通过对高熵词进行同义词替换，嵌入水印，从而增强LLM对水印文本的记忆能力，而不改变文本的语义。这种设计使得水印难以被检测和移除。

**技术框架**：LexiMark的整体架构包括数据预处理、同义词替换模块和水印嵌入模块。首先，对训练数据进行分析，识别高熵词；然后，通过同义词替换生成水印文本，最后将水印文本用于LLM的训练。

**关键创新**：LexiMark的主要创新在于其隐蔽性和鲁棒性，通过上下文适当的同义词替换，使得水印难以被自动或手动检测，与现有方法相比，显著提高了水印的隐蔽性和抗移除能力。

**关键设计**：在关键设计上，LexiMark选择高熵词进行替换，并通过特定的损失函数来优化水印的嵌入效果，确保文本的语义完整性和流畅性。

## 📊 实验亮点

实验结果显示，LexiMark在多个训练设置下的AUROC评分显著提高，超过了现有水印方法的表现，证明了其在验证未经授权使用水印数据方面的有效性。具体而言，LexiMark在七个开源模型上的表现均优于基线，显示出其广泛的适用性和鲁棒性。

## 🎯 应用场景

LexiMark的研究成果在多个领域具有潜在应用价值，包括保护知识产权、确保数据使用合规性以及增强模型训练的透明度。随着LLM的广泛应用，确保训练数据的合法性和可追溯性将变得愈发重要，LexiMark为此提供了一种有效的解决方案。

## 📄 摘要（原文）

> Large language models (LLMs) can be trained or fine-tuned on data obtained without the owner's consent. Verifying whether a specific LLM was trained on particular data instances or an entire dataset is extremely challenging. Dataset watermarking addresses this by embedding identifiable modifications in training data to detect unauthorized use. However, existing methods often lack stealth, making them relatively easy to detect and remove. In light of these limitations, we propose LexiMark, a novel watermarking technique designed for text and documents, which embeds synonym substitutions for carefully selected high-entropy words. Our method aims to enhance an LLM's memorization capabilities on the watermarked text without altering the semantic integrity of the text. As a result, the watermark is difficult to detect, blending seamlessly into the text with no visible markers, and is resistant to removal due to its subtle, contextually appropriate substitutions that evade automated and manual detection. We evaluated our method using baseline datasets from recent studies and seven open-source models: LLaMA-1 7B, LLaMA-3 8B, Mistral 7B, Pythia 6.9B, as well as three smaller variants from the Pythia family (160M, 410M, and 1B). Our evaluation spans multiple training settings, including continued pretraining and fine-tuning scenarios. The results demonstrate significant improvements in AUROC scores compared to existing methods, underscoring our method's effectiveness in reliably verifying whether unauthorized watermarked data was used in LLM training.


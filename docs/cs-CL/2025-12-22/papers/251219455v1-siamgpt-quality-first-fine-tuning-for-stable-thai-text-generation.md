---
layout: default
title: "SiamGPT: Quality-First Fine-Tuning for Stable Thai Text Generation"
---

# SiamGPT: Quality-First Fine-Tuning for Stable Thai Text Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19455" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19455v1</a>
  <a href="https://arxiv.org/pdf/2512.19455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19455v1', 'SiamGPT: Quality-First Fine-Tuning for Stable Thai Text Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thittipat Pairatsuppawat, Abhibhu Tachaapornchai, Paweekorn Kusolsomboon, Chutikan Chaiwong, Thodsaporn Chay-intr, Kobkrit Viriyayudhakorn, Nongnuch Ketui, Aslan B. Wong

**分类**: cs.CL

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**SiamGPT：面向稳定泰语文本生成的质量优先微调方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `泰语NLP` `大型语言模型` `指令微调` `质量优先` `多轮对话`

## 📋 核心要点

1. 现有开源大语言模型在泰语环境下，复杂指令下的生成结果不稳定，难以有效部署。
2. SiamGPT采用质量优先的微调策略，结合翻译后的高质量英语指令数据和泰语适配的AutoIF框架。
3. 实验表明，SiamGPT在指令遵循、多轮对话和语言稳定性方面均有提升，并在SEA-HELM基准测试中表现最佳。

## 📝 摘要（中文）

由于在复杂指令下生成不稳定，即使在英语方面表现出色，开源大型语言模型在泰语部署方面仍然面临困难。为了缓解这些限制，我们提出了SiamGPT-32B，一个基于Qwen3-32B的开源模型，采用质量优先策略进行微调，强调精心策划的监督而非数据规模。该微调流程结合了翻译的高复杂度英语指令数据和泰语改编的AutoIF框架，用于指令和语言约束。仅使用监督微调，无需持续预训练或语料库扩展，SiamGPT-32B提高了指令遵循、多轮对话鲁棒性和语言稳定性。在SEA-HELM基准上的评估表明，SiamGPT-32B在类似规模的开源泰语模型中实现了最强的整体性能，在指令遵循、多轮对话和自然语言理解方面均取得了持续的提升。

## 🔬 方法详解

**问题定义**：论文旨在解决开源大型语言模型在泰语文本生成中，面对复杂指令时生成结果不稳定的问题。现有方法通常依赖于大规模数据进行训练，但忽略了数据的质量，导致模型在泰语环境下的指令遵循能力较弱，多轮对话鲁棒性不足，且语言表达不够稳定。

**核心思路**：论文的核心思路是采用“质量优先”的微调策略，即更加注重训练数据的质量而非数量。通过精心挑选和处理高质量的指令数据，并结合泰语环境的特点进行适配，从而提升模型在泰语文本生成方面的性能。这种策略避免了盲目扩大数据规模可能带来的噪声和偏差，更加有效地利用了有限的资源。

**技术框架**：SiamGPT的整体框架包括以下几个主要阶段：1) 基于Qwen3-32B的预训练模型作为基础；2) 将高质量的英语指令数据翻译成泰语；3) 采用泰语适配的AutoIF框架，用于指令和语言约束；4) 使用监督微调方法对模型进行训练，提升其在泰语环境下的指令遵循能力、多轮对话鲁棒性和语言稳定性。整个流程没有进行持续预训练或语料库扩展，而是专注于利用高质量的监督数据进行微调。

**关键创新**：论文最重要的技术创新点在于提出了“质量优先”的微调策略，并将其应用于泰语大型语言模型的训练中。与以往依赖大规模数据的方法不同，该策略更加注重数据的质量和针对性，从而在有限的资源下取得了更好的效果。此外，论文还提出了泰语适配的AutoIF框架，用于指令和语言约束，进一步提升了模型在泰语环境下的性能。

**关键设计**：论文的关键设计包括：1) 精心挑选和翻译高质量的英语指令数据，确保数据的多样性和复杂性；2) 采用泰语适配的AutoIF框架，对生成的文本进行约束，保证语言的流畅性和准确性；3) 使用监督微调方法，通过优化模型的参数，使其更好地适应泰语环境。具体的参数设置、损失函数和网络结构等细节未在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19455v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19455v1/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SiamGPT-32B在SEA-HELM基准测试中，在同等规模的开源泰语模型中取得了最佳的整体性能。在指令遵循、多轮对话和自然语言理解等多个方面均有显著提升，证明了“质量优先”微调策略的有效性。具体的性能提升幅度未在摘要中给出，属于未知信息。

## 🎯 应用场景

SiamGPT的研究成果可应用于多种泰语自然语言处理任务，如智能客服、文本摘要、机器翻译、内容创作等。该模型能够生成更稳定、更符合指令的泰语文本，提升用户体验和工作效率。未来，该研究有望推动泰语自然语言处理技术的发展，促进泰语信息资源的数字化和智能化。

## 📄 摘要（原文）

> Open-weights large language models remain difficult to deploy for Thai due to unstable generation under complex instructions, despite strong English performance. To mitigate these limitations, We present SiamGPT-32B, an open-weights model based on Qwen3-32B, fine-tuned with a Quality-First strategy emphasizing curated supervision over data scale. The fine-tuning pipeline combines translated high-complexity English instruction data with a Thai-adapted AutoIF framework for instruction and linguistic constraints. Using supervised fine-tuning only, without continual pretraining or corpus expansion, SiamGPT-32B improves instruction adherence, multi-turn robustness, and linguistic stability. Evaluations on the SEA-HELM benchmark show that SiamGPT-32B achieves the strongest overall performance among similar-scale open-weights Thai models, with consistent gains in instruction following, multi-turn dialogue, and natural language understanding.


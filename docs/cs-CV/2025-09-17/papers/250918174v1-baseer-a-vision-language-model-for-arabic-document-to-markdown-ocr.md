---
layout: default
title: "Baseer: A Vision-Language Model for Arabic Document-to-Markdown OCR"
---

# Baseer: A Vision-Language Model for Arabic Document-to-Markdown OCR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18174" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18174v1</a>
  <a href="https://arxiv.org/pdf/2509.18174.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18174v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18174v1', 'Baseer: A Vision-Language Model for Arabic Document-to-Markdown OCR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khalil Hennara, Muhammad Hreden, Mohamed Motasim Hamed, Ahmad Bastati, Zeina Aldallal, Sara Chrouf, Safwan AlModhayan

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**Baseer：面向阿拉伯语文档OCR的视觉-语言模型，刷新SOTA**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿拉伯语OCR` `视觉-语言模型` `多模态学习` `文档理解` `领域自适应`

## 📋 核心要点

1. 阿拉伯语OCR因其文字特性（如草书、变音符号）而极具挑战，现有MLLM性能有限。
2. Baseer通过大规模数据集和解码器微调策略，使预训练MLLM适应阿拉伯语文档OCR任务。
3. Baseer在Misraj-DocOCR基准测试中显著优于现有方案，WER达到0.25，确立了新的SOTA。

## 📝 摘要（中文）

由于阿拉伯语的草书、多样的字体、变音符号和从右到左的阅读方向，阿拉伯语文档OCR仍然是一项具有挑战性的任务。虽然现代多模态大型语言模型(MLLM)已经推动了高资源语言的文档理解，但它们在阿拉伯语上的性能仍然有限。本文介绍了Baseer，一个专门为阿拉伯语文档OCR微调的视觉-语言模型。Baseer利用大规模数据集，结合合成和真实文档，采用仅解码器微调策略训练，以适应预训练的MLLM，同时保留一般的视觉特征。我们还提出了Misraj-DocOCR，这是一个高质量、专家验证的基准，专为阿拉伯语OCR系统的严格评估而设计。实验表明，Baseer显著优于现有的开源和商业解决方案，实现了0.25的WER，并在阿拉伯语文档OCR领域建立了新的state-of-the-art。我们的结果突出了通用MLLM的领域特定适应的优势，并为像阿拉伯语这样形态丰富的语言建立了一个高精度OCR的强大基线。

## 🔬 方法详解

**问题定义**：阿拉伯语文档OCR面临诸多挑战，包括草书特性、字体多样性、变音符号以及从右向左的阅读顺序。现有通用多模态大型语言模型（MLLM）在处理阿拉伯语文档时，性能表现不佳，无法满足实际应用的需求。因此，需要一种专门针对阿拉伯语文档优化的OCR模型。

**核心思路**：论文的核心思路是利用预训练的MLLM，通过领域特定的微调，使其适应阿拉伯语文档OCR任务。这种方法旨在利用通用MLLM强大的视觉和语言理解能力，同时通过微调使其更好地处理阿拉伯语的特殊性。

**技术框架**：Baseer的技术框架主要包括以下几个部分：1) 数据集构建：构建包含合成数据和真实数据的阿拉伯语文档图像数据集。2) 模型选择：选择一个预训练的MLLM作为基础模型。3) 微调策略：采用decoder-only的微调策略，即只微调模型的解码器部分，以保留预训练模型的一般视觉特征。4) 评估基准：提出Misraj-DocOCR基准，用于评估阿拉伯语OCR系统的性能。

**关键创新**：该论文的关键创新在于：1) 领域特定微调：针对阿拉伯语文档OCR任务，对通用MLLM进行领域特定微调，显著提升了模型在该任务上的性能。2) 高质量基准：提出了Misraj-DocOCR基准，为阿拉伯语OCR系统的评估提供了一个可靠的平台。

**关键设计**：Baseer的关键设计包括：1) 数据集：使用了大规模的合成数据和真实数据，以提高模型的泛化能力。2) 微调策略：采用decoder-only微调，避免了对预训练模型视觉特征的过度修改。3) 损失函数：使用标准的交叉熵损失函数进行训练。4) 评估指标：使用词错误率（WER）作为主要的评估指标。

## 📊 实验亮点

Baseer在Misraj-DocOCR基准测试中取得了显著成果，词错误率（WER）仅为0.25，大幅超越了现有的开源和商业OCR系统，确立了阿拉伯语文档OCR领域的全新技术标杆。这一结果充分验证了领域特定微调策略在提升MLLM性能方面的有效性。

## 🎯 应用场景

Baseer在多个领域具有广泛的应用前景，包括数字化阿拉伯语书籍和文档、自动处理阿拉伯语发票和表格、提升阿拉伯语搜索引擎的准确性，以及辅助阿拉伯语学习和翻译。该研究有助于保护和传播阿拉伯语文化遗产，并促进阿拉伯语在数字时代的普及和应用。

## 📄 摘要（原文）

> Arabic document OCR remains a challenging task due to the language's cursive script, diverse fonts, diacritics, and right-to-left orientation. While modern Multimodal Large Language Models (MLLMs) have advanced document understanding for high-resource languages, their performance on Arabic remains limited. In this work, we introduce Baseer, a vision-language model fine-tuned specifically for Arabic document OCR. Leveraging a large-scale dataset combining synthetic and real-world documents, Baseer is trained using a decoder-only fine-tuning strategy to adapt a pre-trained MLLM while preserving general visual features. We also present Misraj-DocOCR, a high-quality, expert-verified benchmark designed for rigorous evaluation of Arabic OCR systems. Our experiments show that Baseer significantly outperforms existing open-source and commercial solutions, achieving a WER of 0.25 and establishing a new state-of-the-art in the domain of Arabic document OCR. Our results highlight the benefits of domain-specific adaptation of general-purpose MLLMs and establish a strong baseline for high-accuracy OCR on morphologically rich languages like Arabic.


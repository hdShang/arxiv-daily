---
layout: default
title: "Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples"
---

# Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14518" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14518v2</a>
  <a href="https://arxiv.org/pdf/2505.14518.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14518v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14518v2', 'Teaching Audio-Aware Large Language Models What Does Not Hear: Mitigating Hallucinations through Synthesized Negative Samples')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chun-Yi Kuan, Hung-yi Lee

**分类**: eess.AS, cs.CL, cs.SD

**发布日期**: 2025-05-20 (更新: 2025-07-01)

**备注**: Accepted to Interspeech 2025. Project Website: https://kuan2jiu99.github.io/Balsa

---

## 💡 一句话要点

**提出LISTEN以解决音频感知大语言模型的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频感知` `大语言模型` `对比学习` `负样本` `幻觉现象` `多模态学习` `智能音箱`

## 📋 核心要点

1. 现有音频感知大语言模型常常产生虚构的声音事件，影响其在实际应用中的可靠性。
2. 本文提出LISTEN方法，通过对比训练增强模型区分存在与缺失声音的能力，利用合成负样本进行学习。
3. 实验结果显示，LISTEN有效减轻了幻觉现象，并在音频问答和推理基准上表现优异，且计算效率更高。

## 📝 摘要（中文）

近年来，音频感知大语言模型（ALLMs）的进展使其能够处理和理解音频输入。然而，这些模型常常会产生虚构的声音事件，降低了其在实际应用中的可靠性。为了解决这一问题，本文提出了LISTEN（通过扩展负样本学习识别声音），这是一种对比训练方法，增强了ALLMs区分存在与缺失声音的能力，利用来自基础大语言模型的合成数据。与以往方法不同，我们的方法无需修改LLM参数，并通过轻量级适配器高效整合音频表示。实验表明，LISTEN有效减轻了幻觉现象，同时在现有音频问答和推理基准上保持了出色的性能，并在数据和计算效率上更具优势。

## 🔬 方法详解

**问题定义**：本文旨在解决音频感知大语言模型（ALLMs）在处理音频输入时产生虚构声音事件的问题。现有方法在提高模型理解能力的同时，未能有效减少幻觉现象，导致模型在实际应用中的可靠性下降。

**核心思路**：论文提出的LISTEN方法通过对比训练，利用合成的负样本来增强模型对声音的识别能力。该方法的设计旨在提高模型对缺失声音的敏感性，从而减少幻觉现象的发生。

**技术框架**：LISTEN方法的整体架构包括数据合成模块、对比学习模块和轻量级适配器。数据合成模块生成负样本，对比学习模块用于训练模型识别存在与缺失的声音，而适配器则高效整合音频表示。

**关键创新**：LISTEN的主要创新在于其无需修改大语言模型的参数，通过轻量级适配器实现音频表示的高效整合。这一设计使得模型在保持性能的同时，能够有效减少幻觉现象。

**关键设计**：在LISTEN中，采用了特定的损失函数来优化对比学习过程，确保模型能够准确区分存在与缺失的声音。此外，轻量级适配器的设计使得模型在计算资源上的需求显著降低，提升了整体效率。

## 📊 实验亮点

实验结果表明，LISTEN方法在音频问答和推理基准上表现优异，相较于基线模型，幻觉现象减少了显著的比例，同时在数据和计算效率上也有明显提升，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能音箱、语音助手和自动音频分析等场景。通过提高音频感知大语言模型的可靠性，LISTEN方法能够为这些应用提供更准确的声音识别和理解能力，进而提升用户体验和系统性能。未来，该方法还可能推动更多多模态交互技术的发展。

## 📄 摘要（原文）

> Recent advancements in audio-aware large language models (ALLMs) enable them to process and understand audio inputs. However, these models often hallucinate non-existent sound events, reducing their reliability in real-world applications. To address this, we propose LISTEN (Learning to Identify Sounds Through Extended Negative Samples), a contrastive-like training method that enhances ALLMs' ability to distinguish between present and absent sounds using synthesized data from the backbone LLM. Unlike prior approaches, our method requires no modification to LLM parameters and efficiently integrates audio representations via a lightweight adapter. Experiments show that LISTEN effectively mitigates hallucinations while maintaining impressive performance on existing audio question and reasoning benchmarks. At the same time, it is more efficient in both data and computation.


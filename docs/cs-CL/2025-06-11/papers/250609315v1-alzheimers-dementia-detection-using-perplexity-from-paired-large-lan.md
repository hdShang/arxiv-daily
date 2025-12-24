---
layout: default
title: "Alzheimer's Dementia Detection Using Perplexity from Paired Large Language Models"
---

# Alzheimer's Dementia Detection Using Perplexity from Paired Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09315" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09315v1</a>
  <a href="https://arxiv.org/pdf/2506.09315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09315v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09315v1', 'Alzheimer\'s Dementia Detection Using Perplexity from Paired Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Xiao, Heidi Christensen, Stefan Goetze

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-11

**备注**: To be published in the proceedings of Interspeech 2025

---

## 💡 一句话要点

**基于配对大语言模型的困惑度检测阿尔茨海默病**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿尔茨海默病` `大语言模型` `配对困惑度` `语言能力` `神经退行性疾病` `模型解释` `数据增强`

## 📋 核心要点

1. 阿尔茨海默病的检测方法存在准确性不足和决策过程不透明的问题。
2. 本文提出了一种基于配对困惑度的新方法，利用大语言模型Mistral-7B进行AD检测。
3. 实验结果显示，该方法在准确率上平均提升3.33%，并且具有清晰的决策边界。

## 📝 摘要（中文）

阿尔茨海默病（AD）是一种影响语言能力的神经退行性疾病。本文扩展了配对困惑度方法，通过使用最新的指令跟随版本的Mistral-7B大语言模型来检测AD。与当前最佳配对困惑度方法相比，准确率提高了平均3.33%，与ADReSS 2020挑战基准的顶级方法相比提高了6.35%。进一步分析表明，该方法能够有效检测AD，并具有清晰可解释的决策边界，克服了其他方法的决策过程不透明的问题。此外，通过提示微调的LLM并比较模型生成的响应与人类响应，展示了LLM学习了AD患者的特殊语言模式，为模型解释和数据增强的新方法开辟了可能性。

## 🔬 方法详解

**问题定义**：本文旨在解决阿尔茨海默病（AD）的检测问题，现有方法在准确性和决策透明度上存在不足，导致临床应用受限。

**核心思路**：通过扩展配对困惑度的方法，结合最新的Mistral-7B大语言模型，提升AD检测的准确性和可解释性。设计上强调模型对AD患者语言模式的学习，以增强检测能力。

**技术框架**：整体架构包括数据预处理、模型微调、困惑度计算和决策边界分析等模块。首先对输入数据进行清洗和标注，然后使用Mistral-7B进行微调，最后计算配对困惑度并分析决策边界。

**关键创新**：最重要的创新在于使用指令跟随版本的Mistral-7B模型，显著提高了检测准确性，并提供了可解释的决策过程，与传统方法相比具有明显优势。

**关键设计**：在模型微调过程中，采用了特定的损失函数以优化困惑度计算，并通过对比人类响应与模型生成响应来验证模型的学习效果，确保模型能够捕捉AD患者的语言特征。

## 📊 实验亮点

实验结果表明，所提出的方法在准确率上平均提高了3.33%，相较于ADReSS 2020挑战基准的顶级方法提升了6.35%。此外，模型生成的响应与人类响应的对比分析，进一步验证了模型对AD患者语言模式的学习能力，展示了良好的可解释性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断、老年人语言能力评估和智能健康监测系统。通过提高阿尔茨海默病的检测准确性，能够为早期干预和治疗提供支持，具有重要的社会价值和实际意义。未来，该方法还可能推动更多基于语言模型的医疗应用发展。

## 📄 摘要（原文）

> Alzheimer's dementia (AD) is a neurodegenerative disorder with cognitive decline that commonly impacts language ability. This work extends the paired perplexity approach to detecting AD by using a recent large language model (LLM), the instruction-following version of Mistral-7B. We improve accuracy by an average of 3.33% over the best current paired perplexity method and by 6.35% over the top-ranked method from the ADReSS 2020 challenge benchmark. Our further analysis demonstrates that the proposed approach can effectively detect AD with a clear and interpretable decision boundary in contrast to other methods that suffer from opaque decision-making processes. Finally, by prompting the fine-tuned LLMs and comparing the model-generated responses to human responses, we illustrate that the LLMs have learned the special language patterns of AD speakers, which opens up possibilities for novel methods of model interpretation and data augmentation.


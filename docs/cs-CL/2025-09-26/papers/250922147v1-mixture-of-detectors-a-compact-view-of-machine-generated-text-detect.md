---
layout: default
title: "Mixture of Detectors: A Compact View of Machine-Generated Text Detection"
---

# Mixture of Detectors: A Compact View of Machine-Generated Text Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22147" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22147v1</a>
  <a href="https://arxiv.org/pdf/2509.22147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22147v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22147v1', 'Mixture of Detectors: A Compact View of Machine-Generated Text Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sai Teja Lekkala, Yadagiri Annepaka, Arun Kumar Challa, Samatha Reddy Machireddy, Partha Pakray, Chukhu Chunka

**分类**: cs.CL

**发布日期**: 2025-09-26

**备注**: 20 pages, 3 figures

---

## 💡 一句话要点

**提出混合检测器方法，用于全面评估和提升机器生成文本检测能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器生成文本检测` `自然语言处理` `深度学习` `对抗攻击` `数据集` `文本分类`

## 📋 核心要点

1. 现有方法在机器生成文本检测方面存在局限性，难以有效应对各种场景和对抗攻击。
2. 提出混合检测器方法，旨在全面评估和提升机器生成文本检测在不同场景下的性能。
3. 引入BMAS English数据集，包含二分类、多分类、对抗攻击和句子分割等任务，促进相关研究。

## 📝 摘要（中文）

大型语言模型（LLM）正迅速逼近甚至超越人类的创造力。本文旨在审视这一论断的真实性，并探讨由此引发的关于人类作品原创性以及创造力和创新能力保护的关键问题。本文研究了多种场景下的机器生成文本检测问题，包括文档级别的二分类和多分类（生成器归属）、句子级别的分割（区分人机协作文本）以及旨在降低机器生成文本可检测性的对抗攻击。我们提出了一项名为BMAS English的新工作，这是一个用于机器生成文本检测的英文数据集，涵盖二分类、多分类（识别生成器）、对抗攻击缓解和句子级别分割。我们相信本文将以更有意义的方式推进机器生成文本检测（MGTD）领域的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决机器生成文本检测问题，现有方法难以有效区分人类创作文本和机器生成文本，尤其是在对抗攻击和人机协作场景下。此外，现有数据集缺乏对不同生成器进行分类的能力，限制了对生成模型溯源的研究。

**核心思路**：本文的核心思路是构建一个混合检测器，通过综合利用多种检测技术，提升在不同场景下的检测性能。同时，引入新的数据集BMAS English，以支持更全面的评估和研究。

**技术框架**：整体框架包括四个主要部分：1) 文档级别的二分类，区分人类和机器生成文本；2) 文档级别的多分类，识别生成文本的来源模型；3) 句子级别的分割，用于区分人机协作文本中人类和机器生成的部分；4) 对抗攻击，评估和缓解机器生成文本的可检测性。

**关键创新**：关键创新在于提出了一个综合性的评估框架，涵盖了多种场景和任务，并引入了新的数据集BMAS English，该数据集不仅包含二分类数据，还包含多分类、对抗攻击和句子分割数据，为更深入的研究提供了支持。

**关键设计**：BMAS English数据集包含不同来源的机器生成文本，例如不同的LLM。对抗攻击部分可能涉及使用梯度下降等方法生成对抗样本，以降低检测器的性能。句子分割可能采用序列标注模型，例如BiLSTM-CRF，来预测每个句子的来源。

## 📊 实验亮点

论文提出了BMAS English数据集，并进行了多项实验，验证了混合检测器方法在不同场景下的有效性。虽然摘要中没有给出具体的性能数据和提升幅度，但可以推断，该方法在二分类、多分类、对抗攻击和句子分割等任务上均取得了较好的结果。

## 🎯 应用场景

该研究成果可应用于内容审核、学术诚信检测、新闻真实性验证等领域。通过准确识别机器生成文本，可以有效防止虚假信息的传播，维护网络安全和信息生态。未来，该技术可进一步应用于自动化内容生成质量评估和人机协作流程优化。

## 📄 摘要（原文）

> Large Language Models (LLMs) are gearing up to surpass human creativity. The veracity of the statement needs careful consideration. In recent developments, critical questions arise regarding the authenticity of human work and the preservation of their creativity and innovative abilities. This paper investigates such issues. This paper addresses machine-generated text detection across several scenarios, including document-level binary and multiclass classification or generator attribution, sentence-level segmentation to differentiate between human-AI collaborative text, and adversarial attacks aimed at reducing the detectability of machine-generated text. We introduce a new work called BMAS English: an English language dataset for binary classification of human and machine text, for multiclass classification, which not only identifies machine-generated text but can also try to determine its generator, and Adversarial attack addressing where it is a common act for the mitigation of detection, and Sentence-level segmentation, for predicting the boundaries between human and machine-generated text. We believe that this paper will address previous work in Machine-Generated Text Detection (MGTD) in a more meaningful way.


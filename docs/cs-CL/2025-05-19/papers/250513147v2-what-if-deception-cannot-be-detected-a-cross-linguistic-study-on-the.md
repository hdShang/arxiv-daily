---
layout: default
title: What if Deception Cannot be Detected? A Cross-Linguistic Study on the Limits of Deception Detection from Text
---

# What if Deception Cannot be Detected? A Cross-Linguistic Study on the Limits of Deception Detection from Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13147" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13147v2</a>
  <a href="https://arxiv.org/pdf/2505.13147.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13147v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13147v2', 'What if Deception Cannot be Detected? A Cross-Linguistic Study on the Limits of Deception Detection from Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aswathy Velutharambath, Kai Sassenberg, Roman Klinger

**分类**: cs.CL

**发布日期**: 2025-05-19 (更新: 2025-05-20)

---

## 💡 一句话要点

**提出基于信念的欺骗框架以重新审视文本欺骗检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `欺骗检测` `自然语言处理` `信念框架` `文本分析` `多语言语料库` `模型评估` `语言线索`

## 📋 核心要点

1. 现有的欺骗检测方法在文本中依赖于微妙的语言线索，但这些线索的可靠性受到质疑。
2. 论文提出了一种基于信念的欺骗框架，允许在不考虑事实准确性的情况下研究欺骗线索。
3. 实验结果表明，常见的欺骗线索与欺骗标签之间的相关性微弱，且不同数据集间的预测线索不一致。

## 📝 摘要（中文）

本研究探讨了仅通过书面文本是否能够检测欺骗。欺骗的线索在文本交流中尤为微妙，现有研究的成功可能受到数据收集过程中的伪影影响。我们提出了一种基于信念的欺骗框架，将欺骗定义为作者的主张与真实信念之间的不一致。基于此框架，我们构建了三个语料库DeFaBel，评估了常见的欺骗语言线索，结果显示这些线索与欺骗标签之间的相关性微乎其微，挑战了现有的假设，并呼吁重新思考欺骗在自然语言处理中的研究和建模方式。

## 🔬 方法详解

**问题定义**：本研究旨在解决文本欺骗检测的可靠性问题，现有方法在不同数据集上表现不一致，且常用的语言线索与欺骗标签的相关性较低。

**核心思路**：提出基于信念的欺骗框架，将欺骗定义为作者主张与真实信念之间的不一致，从而使欺骗线索的研究更加独立于事实准确性。

**技术框架**：整体架构包括三个主要阶段：构建DeFaBel语料库、评估语言线索与欺骗标签的相关性、以及使用多种模型进行欺骗检测。

**关键创新**：最重要的创新在于引入基于信念的欺骗框架，挑战了传统的欺骗检测假设，强调了语言线索的局限性。

**关键设计**：在构建语料库时，考虑了信念变化的不同条件，采用了多语言版本，并在模型评估中使用了特征基础模型、预训练语言模型和指令调优的大型语言模型。实验显示，尽管某些模型在已建立的数据集上表现良好，但在DeFaBel上接近随机表现。

## 📊 实验亮点

实验结果显示，DeFaBel语料库中的欺骗线索与欺骗标签之间的相关性微弱，统计上不显著。尽管在其他英语欺骗数据集上某些模型表现出统计显著性，但效应大小较低，且预测线索在不同数据集间不一致，强调了现有方法的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体监控、在线欺诈检测和法律文本分析等。通过重新审视欺骗检测的方式，研究为相关领域提供了新的视角，可能推动更有效的文本分析工具的发展。未来，基于信念的框架有望在多种语言和文化背景下应用，提升欺骗检测的准确性和可靠性。

## 📄 摘要（原文）

> Can deception be detected solely from written text? Cues of deceptive communication are inherently subtle, even more so in text-only communication. Yet, prior studies have reported considerable success in automatic deception detection. We hypothesize that such findings are largely driven by artifacts introduced during data collection and do not generalize beyond specific datasets. We revisit this assumption by introducing a belief-based deception framework, which defines deception as a misalignment between an author's claims and true beliefs, irrespective of factual accuracy, allowing deception cues to be studied in isolation. Based on this framework, we construct three corpora, collectively referred to as DeFaBel, including a German-language corpus of deceptive and non-deceptive arguments and a multilingual version in German and English, each collected under varying conditions to account for belief change and enable cross-linguistic analysis. Using these corpora, we evaluate commonly reported linguistic cues of deception. Across all three DeFaBel variants, these cues show negligible, statistically insignificant correlations with deception labels, contrary to prior work that treats such cues as reliable indicators. We further benchmark against other English deception datasets following similar data collection protocols. While some show statistically significant correlations, effect sizes remain low and, critically, the set of predictive cues is inconsistent across datasets. We also evaluate deception detection using feature-based models, pretrained language models, and instruction-tuned large language models. While some models perform well on established deception datasets, they consistently perform near chance on DeFaBel. Our findings challenge the assumption that deception can be reliably inferred from linguistic cues and call for rethinking how deception is studied and modeled in NLP.


---
layout: default
title: "BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings"
---

# BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15001" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15001v1</a>
  <a href="https://arxiv.org/pdf/2509.15001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15001v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15001v1', 'BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Théo Charlot, Tarek Kunze, Maxime Poli, Alejandrina Cristia, Emmanuel Dupoux, Marvin Lavechin

**分类**: eess.AS, cs.LG, cs.SD

**发布日期**: 2025-09-18

**备注**: 5 pages, 1 figure

---

## 💡 一句话要点

**BabyHuBERT：面向儿童语音的长时录音说话人分割多语种自监督学习**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `儿童语音` `自监督学习` `说话人分割` `多语种` `长时录音` `HuBERT` `语音表征` `语言发展`

## 📋 核心要点

1. 现有语音模型在儿童语音长时录音上表现不佳，因为这些模型主要在干净的成人语音数据上训练，与儿童语音存在显著差异。
2. BabyHuBERT的核心思想是利用大量的多语种儿童语音长时录音进行自监督学习，从而学习到更适合儿童语音的表征。
3. 实验结果表明，BabyHuBERT在说话人分割任务上显著优于现有模型，尤其是在代表性不足的语言上，F1分数提升明显。

## 📝 摘要（中文）

儿童语音长时录音对于研究早期语言发展至关重要，但现有在干净成人数据上训练的语音模型由于声学和语言差异表现不佳。我们提出了BabyHuBERT，这是第一个在超过40种语言的13,000小时多语种儿童语音长时录音上训练的自监督语音表征模型。我们在说话人分割任务上评估了BabyHuBERT，即识别目标儿童何时说话，以及何时是女性成人、男性成人或其他儿童在说话——这是分析自然语言体验的基本预处理步骤。在六个不同的数据集上，BabyHuBERT实现了52.1%到74.4%的F1分数，始终优于W2V2-LL4300（在英语长时录音上训练）和标准HuBERT（在干净成人语音上训练）。值得注意的改进包括在瓦努阿图语料库上超过HuBERT 13.2个绝对F1点，在所罗门群岛语料库上超过15.9个点，证明了其在代表性不足的语言上的有效性。通过共享代码和模型，BabyHuBERT作为儿童语音研究的基础模型，能够对各种下游任务进行微调。

## 🔬 方法详解

**问题定义**：论文旨在解决儿童语音长时录音中的说话人分割问题。现有方法，如在成人语音上训练的HuBERT，在处理儿童语音时性能显著下降，因为儿童语音的声学特征与成人语音差异较大，且长时录音通常包含噪声和多种说话人。

**核心思路**：论文的核心思路是利用自监督学习方法，在大规模多语种儿童语音数据上预训练一个语音表征模型。通过自监督学习，模型可以学习到儿童语音的内在结构和特征，从而更好地适应儿童语音的特点。

**技术框架**：BabyHuBERT的整体框架基于HuBERT模型，但关键在于其训练数据。首先，收集了13,000小时的多语种儿童语音长时录音数据。然后，使用HuBERT的自监督学习框架，对这些数据进行预训练。预训练完成后，可以将BabyHuBERT模型用于下游任务，如说话人分割，通过微调来进一步提升性能。

**关键创新**：BabyHuBERT最重要的创新点在于其训练数据。它是第一个在如此大规模的多语种儿童语音长时录音上训练的自监督语音表征模型。这使得模型能够学习到更具泛化性和鲁棒性的儿童语音特征，从而在说话人分割等任务上取得更好的性能。与现有方法相比，BabyHuBERT更关注儿童语音的特性，而不是简单地将成人语音模型应用于儿童语音。

**关键设计**：BabyHuBERT的关键设计在于其训练数据的选择和预处理。论文作者精心收集了来自40多种语言的儿童语音数据，并对数据进行了清洗和标注。此外，论文作者还探索了不同的自监督学习策略，以提高模型的学习效率和性能。具体的网络结构和损失函数与原始HuBERT模型保持一致，重点在于利用大规模儿童语音数据进行预训练。

## 📊 实验亮点

BabyHuBERT在六个不同的数据集上进行了评估，结果表明其在说话人分割任务上始终优于W2V2-LL4300和标准HuBERT。在瓦努阿图语料库上，BabyHuBERT的F1分数比HuBERT高出13.2个百分点；在所罗门群岛语料库上，BabyHuBERT的F1分数比HuBERT高出15.9个百分点。这些结果表明，BabyHuBERT在处理代表性不足的语言时具有显著优势。

## 🎯 应用场景

BabyHuBERT在儿童语言发展研究中具有广泛的应用前景。它可以用于自动分析儿童的语言环境，例如，识别儿童与哪些人互动，以及他们说了什么。这有助于研究人员更好地了解儿童的语言发展过程，并为早期语言干预提供支持。此外，BabyHuBERT还可以应用于儿童语音识别、语音合成等领域。

## 📄 摘要（原文）

> Child-centered long-form recordings are essential for studying early language development, but existing speech models trained on clean adult data perform poorly due to acoustic and linguistic differences. We introduce BabyHuBERT, the first self-supervised speech representation model trained on 13,000 hours of multilingual child-centered long-form recordings spanning over 40 languages. We evaluate BabyHuBERT on speaker segmentation, identifying when target children speak versus female adults, male adults, or other children -- a fundamental preprocessing step for analyzing naturalistic language experiences. BabyHuBERT achieves F1-scores from 52.1% to 74.4% across six diverse datasets, consistently outperforming W2V2-LL4300 (trained on English long-forms) and standard HuBERT (trained on clean adult speech). Notable improvements include 13.2 absolute F1 points over HuBERT on Vanuatu and 15.9 points on Solomon Islands corpora, demonstrating effectiveness on underrepresented languages. By sharing code and models, BabyHuBERT serves as a foundation model for child speech research, enabling fine-tuning on diverse downstream tasks.


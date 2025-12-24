---
layout: default
title: "SignMouth: Leveraging Mouthing Cues for Sign Language Translation by Multimodal Contrastive Fusion"
---

# SignMouth: Leveraging Mouthing Cues for Sign Language Translation by Multimodal Contrastive Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10266" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10266v2</a>
  <a href="https://arxiv.org/pdf/2509.10266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10266v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10266v2', 'SignMouth: Leveraging Mouthing Cues for Sign Language Translation by Multimodal Contrastive Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenfang Wu, Tingting Yuan, Yupeng Li, Daling Wang, Xiaoming Fu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-12 (更新: 2025-10-28)

---

## 💡 一句话要点

**SignClip：利用口型线索的多模态对比融合手语翻译**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手语翻译` `多模态融合` `对比学习` `口型线索` `非人工信号`

## 📋 核心要点

1. 现有手语翻译方法主要依赖手势等人工信号，忽略了口型等非人工信号所蕴含的重要语言信息。
2. SignClip融合手势和唇动特征，并提出多层次对比学习框架，以保证跨模态语义一致性。
3. 在PHOENIX14T数据集上，SignClip在无词汇设置下，显著超越了现有最佳模型SpaMo。

## 📝 摘要（中文）

手语翻译（SLT）旨在将手语视频翻译成自然语言，是共融交流的重要桥梁。虽然最近的研究利用了强大的视觉骨干网络和大型语言模型，但大多数方法主要关注手势等人工信号，而忽略了口型等非人工线索。事实上，口型在手语中传达了重要的语言信息，并在消除视觉上相似的符号歧义方面发挥着关键作用。本文提出了一种新的框架SignClip，以提高手语翻译的准确性。它融合了人工和非人工线索，特别是空间手势和唇部运动特征。此外，SignClip引入了一个具有多层次对齐目标的层次对比学习框架，确保了符号-唇部和视觉-文本模态之间的语义一致性。在PHOENIX14T和How2Sign两个基准数据集上的大量实验证明了我们方法的优越性。例如，在PHOENIX14T数据集的无词汇设置下，SignClip超越了之前的最先进模型SpaMo，BLEU-4指标从24.32提高到24.71，ROUGE指标从46.57提高到48.38。

## 🔬 方法详解

**问题定义**：手语翻译旨在将手语视频转化为自然语言，但现有方法对手语中非人工线索（如口型）的利用不足，导致翻译精度受限。口型包含重要的语言信息，有助于区分视觉上相似的手语符号，因此如何有效利用口型信息是关键挑战。

**核心思路**：SignClip的核心思路是通过融合人工信号（手势）和非人工信号（口型）来提升手语翻译的准确性。通过多模态对比学习，使手势、口型和目标文本在语义空间中对齐，从而更好地理解手语视频的含义。

**技术框架**：SignClip框架主要包含以下几个模块：1) 特征提取模块：分别提取手势和唇部运动的视觉特征。2) 多模态融合模块：将手势和唇部运动特征进行融合，得到综合的视觉表示。3) 对比学习模块：通过多层次对比学习，使手势-唇部和视觉-文本模态在语义空间中对齐。4) 翻译模块：将融合后的视觉表示输入到翻译模型中，生成目标文本。

**关键创新**：SignClip的关键创新在于：1) 显式地利用了口型信息，弥补了现有方法对非人工线索的忽略。2) 提出了多层次对比学习框架，确保了不同模态之间的语义一致性。3) 融合了空间手势和唇部运动特征，更全面地捕捉了手语视频中的信息。

**关键设计**：在特征提取方面，可以使用预训练的视觉模型（如ResNet、Transformer）来提取手势和唇部运动的特征。在多模态融合方面，可以使用注意力机制或简单的拼接操作。在对比学习方面，可以设计不同的损失函数，如InfoNCE损失，来促使不同模态之间的语义对齐。多层次对比学习可以包括实例级别、片段级别和句子级别的对齐。

## 📊 实验亮点

SignClip在PHOENIX14T和How2Sign两个基准数据集上进行了广泛的实验，结果表明SignClip显著优于现有的手语翻译方法。在PHOENIX14T数据集的无词汇设置下，SignClip的BLEU-4指标从24.32提高到24.71，ROUGE指标从46.57提高到48.38，超越了之前的最佳模型SpaMo。实验结果验证了SignClip在手语翻译方面的有效性和优越性。

## 🎯 应用场景

SignClip在手语翻译领域具有广泛的应用前景，可以帮助听力障碍人士更好地与健听人交流，促进社会共融。该技术可应用于在线手语翻译、手语教学、智能客服等场景，为听力障碍人士提供更便捷、高效的沟通方式。未来，SignClip有望进一步提升手语翻译的准确性和流畅性，为构建无障碍社会做出贡献。

## 📄 摘要（原文）

> Sign language translation (SLT) aims to translate natural language from sign language videos, serving as a vital bridge for inclusive communication. While recent advances leverage powerful visual backbones and large language models, most approaches mainly focus on manual signals (hand gestures) and tend to overlook non-manual cues like mouthing. In fact, mouthing conveys essential linguistic information in sign languages and plays a crucial role in disambiguating visually similar signs. In this paper, we propose SignClip, a novel framework to improve the accuracy of sign language translation. It fuses manual and non-manual cues, specifically spatial gesture and lip movement features. Besides, SignClip introduces a hierarchical contrastive learning framework with multi-level alignment objectives, ensuring semantic consistency across sign-lip and visual-text modalities. Extensive experiments on two benchmark datasets, PHOENIX14T and How2Sign, demonstrate the superiority of our approach. For example, on PHOENIX14T, in the Gloss-free setting, SignClip surpasses the previous state-of-the-art model SpaMo, improving BLEU-4 from 24.32 to 24.71, and ROUGE from 46.57 to 48.38.


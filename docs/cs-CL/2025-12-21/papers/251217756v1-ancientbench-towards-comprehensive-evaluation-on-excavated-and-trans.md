---
layout: default
title: "AncientBench: Towards Comprehensive Evaluation on Excavated and Transmitted Chinese Corpora"
---

# AncientBench: Towards Comprehensive Evaluation on Excavated and Transmitted Chinese Corpora

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17756" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17756v1</a>
  <a href="https://arxiv.org/pdf/2512.17756.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17756v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17756v1', 'AncientBench: Towards Comprehensive Evaluation on Excavated and Transmitted Chinese Corpora')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihan Zhou, Daqian Shi, Rui Song, Lida Shi, Xiaolei Diao, Hao Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-19

---

## 💡 一句话要点

**提出AncientBench，用于全面评估模型对出土和传世古汉语语料的理解能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `古文字理解` `大型语言模型` `出土文献` `基准测试` `考古学` `自然语言处理`

## 📋 核心要点

1. 现有中文基准测试主要针对现代汉语和传世古籍，缺乏对出土古文字的评估。
2. AncientBench从字形、发音、意义和语境四个维度，全面评估模型对古文字的理解能力。
3. 实验结果表明，大型语言模型在古文字理解方面具有潜力，但与人类水平仍存在差距。

## 📝 摘要（中文）

为了评估大型语言模型对古文字的理解能力，尤其是在出土文献场景下的表现，本文提出了AncientBench。该基准测试分为四个维度，对应于古文字理解的四个能力：字形理解、发音理解、意义理解和语境理解。AncientBench包含十个任务，包括部首、声旁、同音字、完形填空、翻译等，为评估提供了一个全面的框架。研究团队邀请了考古研究人员进行实验评估，提出了一个古文字模型作为基线，并对当前性能最佳的大型语言模型进行了广泛的实验。实验结果揭示了大型语言模型在古文字场景中的巨大潜力以及与人类的差距。该研究旨在促进大型语言模型在考古学和古代汉语语言领域的发展和应用。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在古汉语理解方面表现出一定的能力，但缺乏专门针对出土文献的评估基准。现有的中文基准测试主要集中在现代汉语和传世古籍，忽略了出土文献中独特的文字特点和语境，这限制了对模型在考古学和古文字研究领域应用潜力的评估。因此，需要一个能够全面评估模型对出土和传世古汉语语料理解能力的基准测试。

**核心思路**：AncientBench的核心思路是将古文字的理解能力分解为四个关键维度：字形理解、发音理解、意义理解和语境理解。通过设计针对每个维度的任务，可以更全面地评估模型对古文字的掌握程度。此外，该基准测试特别关注出土文献的特点，旨在反映实际考古研究中遇到的挑战。

**技术框架**：AncientBench包含四个维度和十个任务。四个维度分别是：字形理解（评估模型对古文字字形的识别能力）、发音理解（评估模型对古文字发音的理解能力）、意义理解（评估模型对古文字含义的理解能力）和语境理解（评估模型在特定语境下理解古文字的能力）。十个任务包括：部首识别、声旁识别、同音字辨析、完形填空、翻译等。研究团队还提出了一个古文字模型作为基线模型。

**关键创新**：AncientBench的关键创新在于其全面性和针对性。它不仅涵盖了古文字理解的多个维度，还特别关注出土文献的特点。此外，该基准测试的任务设计也具有创新性，例如，完形填空任务可以评估模型在特定语境下理解古文字的能力。

**关键设计**：AncientBench的任务设计考虑了古文字的特点和考古研究的需求。例如，部首和声旁识别任务可以评估模型对古文字字形结构的理解能力，翻译任务可以评估模型对古文字含义的理解能力。此外，研究团队还邀请了考古研究人员参与基准测试的设计和评估，以确保其专业性和实用性。具体的参数设置、损失函数、网络结构等技术细节在论文中针对基线模型有更详细的描述，但整体基准测试更侧重于任务的设计和数据集的构建。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17756v1/img/image_head.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17756v1/img/image_sample.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，目前的大型语言模型在AncientBench上表现出一定的古文字理解能力，但在某些任务上与人类水平仍存在较大差距。例如，在语境理解任务中，模型的表现明显低于人类专家。这表明，大型语言模型在古文字理解方面仍有很大的提升空间，AncientBench可以作为评估和改进模型性能的重要工具。

## 🎯 应用场景

AncientBench可用于评估和提升大型语言模型在考古学、历史学和古文字学等领域的应用能力。通过该基准测试，可以推动模型更好地理解和分析古代文献，辅助考古研究，促进中华文明的传承和发展。未来，可以进一步扩展AncientBench，纳入更多类型的出土文献和更复杂的任务，以更好地满足实际应用需求。

## 📄 摘要（原文）

> Comprehension of ancient texts plays an important role in archaeology and understanding of Chinese history and civilization. The rapid development of large language models needs benchmarks that can evaluate their comprehension of ancient characters. Existing Chinese benchmarks are mostly targeted at modern Chinese and transmitted documents in ancient Chinese, but the part of excavated documents in ancient Chinese is not covered. To meet this need, we propose the AncientBench, which aims to evaluate the comprehension of ancient characters, especially in the scenario of excavated documents. The AncientBench is divided into four dimensions, which correspond to the four competencies of ancient character comprehension: glyph comprehension, pronunciation comprehension, meaning comprehension, and contextual comprehension. The benchmark also contains ten tasks, including radical, phonetic radical, homophone, cloze, translation, and more, providing a comprehensive framework for evaluation. We convened archaeological researchers to conduct experimental evaluations, proposed an ancient model as baseline, and conducted extensive experiments on the currently best-performing large language models. The experimental results reveal the great potential of large language models in ancient textual scenarios as well as the gap with humans. Our research aims to promote the development and application of large language models in the field of archaeology and ancient Chinese language.


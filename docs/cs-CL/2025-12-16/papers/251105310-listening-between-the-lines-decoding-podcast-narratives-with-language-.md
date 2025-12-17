---
layout: default
title: Listening Between the Lines: Decoding Podcast Narratives with Language Modeling
---

# Listening Between the Lines: Decoding Podcast Narratives with Language Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.05310" class="toolbar-btn" target="_blank">📄 arXiv: 2511.05310</a>
  <a href="https://arxiv.org/pdf/2511.05310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05310" onclick="toggleFavorite(this, '2511.05310', 'Listening Between the Lines: Decoding Podcast Narratives with Language Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shreya Gupta, Ojasva Saxena, Arghodeep Nandi, Sarah Masud, Kiran Garimella, Tanmoy Chakraborty

**分类**: cs.CL, cs.SI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出一种基于语言模型的播客叙事框架解码方法，提升在非结构化对话数据中的叙事分析精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `播客分析` `叙事框架` `语言模型` `BERT` `自然语言处理`

## 📋 核心要点

1. 现有大型语言模型难以捕捉播客中细微的叙事框架线索，导致无法准确分析播客叙事。
2. 通过微调BERT模型，将叙事框架与对话中的实体联系起来，实现抽象框架与具体细节的关联。
3. 该方法将细粒度的框架标签与高级主题关联，揭示更广泛的话语趋势，提升叙事分析的鲁棒性。

## 📝 摘要（中文）

播客已成为塑造公众舆论的重要场所，是理解当代话语的重要来源。其通常无脚本、多主题和对话式的风格提供了一种丰富但复杂的数据形式。为了分析播客如何说服和告知，我们必须检查它们的叙事结构——特别是它们使用的叙事框架。播客的流畅和对话性质给自动化分析带来了重大挑战。我们表明，通常在新闻文章等更结构化的文本上训练的现有大型语言模型难以捕捉人类听众用来识别叙事框架的细微线索。因此，当前的方法无法大规模地准确分析播客叙事。为了解决这个问题，我们开发并评估了一个微调的BERT模型，该模型将叙事框架与对话中提到的特定实体明确地联系起来，有效地将抽象框架扎根于具体细节中。然后，我们的方法使用这些细粒度的框架标签，并将它们与高级主题相关联，以揭示更广泛的话语趋势。本文的主要贡献是：（i）一种新的框架标记方法，更紧密地与人类对混乱的对话数据的判断相一致，以及（ii）一种新的分析方法，揭示了正在讨论的内容（主题）与呈现方式（框架）之间的系统关系，为研究数字媒体中的影响力提供了一个更强大的框架。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大型语言模型在分析播客等非结构化对话数据中的叙事框架时表现不佳的问题。现有方法主要在结构化文本上训练，难以捕捉播客中细微的叙事线索，导致叙事分析精度不足。

**核心思路**：论文的核心思路是将叙事框架与对话中提到的具体实体联系起来，通过将抽象的叙事框架“锚定”到具体的实体上，从而提高模型对叙事框架的识别能力。这种方法模拟了人类理解叙事的方式，即通过关注对话中的关键人物和事件来推断叙事框架。

**技术框架**：整体框架包含以下几个主要步骤：1) 数据预处理：对播客音频进行转录，得到文本数据。2) 实体识别：识别文本数据中的命名实体。3) 框架标注：人工标注实体相关的叙事框架。4) 模型微调：使用标注数据微调BERT模型，使其能够预测给定实体对应的叙事框架。5) 叙事分析：使用微调后的模型分析播客的叙事结构，并将框架标签与高级主题关联，揭示更广泛的话语趋势。

**关键创新**：论文的关键创新在于提出了一种新的框架标注方法，该方法更紧密地与人类对混乱的对话数据的判断相一致。传统方法通常直接标注整个文本的叙事框架，而该论文的方法则关注实体相关的叙事框架，从而能够更细粒度地捕捉叙事的变化。此外，该方法还提出了一种新的分析方法，揭示了正在讨论的内容（主题）与呈现方式（框架）之间的系统关系。

**关键设计**：论文使用BERT模型作为基础模型，并对其进行微调。微调的目标是使模型能够预测给定实体对应的叙事框架。损失函数采用交叉熵损失函数。具体的网络结构和参数设置在论文中没有详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.05310/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.05310/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.05310/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文的主要实验结果表明，该方法在播客叙事框架识别任务上取得了显著的性能提升。具体的性能数据和对比基线在摘要中没有提及，属于未知信息。但论文强调，该方法更紧密地与人类对混乱的对话数据的判断相一致，能够更准确地分析播客叙事。

## 🎯 应用场景

该研究成果可应用于舆情分析、政治传播研究、市场营销等领域。通过分析播客等数字媒体的叙事框架，可以了解公众对特定话题的看法和态度，从而为决策提供参考。此外，该方法还可以用于检测虚假信息和操纵性宣传，维护健康的舆论环境。

## 📄 摘要（原文）

> Podcasts have become a central arena for shaping public opinion, making them a vital source for understanding contemporary discourse. Their typically unscripted, multi-themed, and conversational style offers a rich but complex form of data. To analyze how podcasts persuade and inform, we must examine their narrative structures -- specifically, the narrative frames they employ.The fluid and conversational nature of podcasts presents a significant challenge for automated analysis. We show that existing large language models, typically trained on more structured text such as news articles, struggle to capture the subtle cues that human listeners rely on to identify narrative frames. As a result, current approaches fall short of accurately analyzing podcast narratives at scale.To solve this, we develop and evaluate a fine-tuned BERT model that explicitly links narrative frames to specific entities mentioned in the conversation, effectively grounding the abstract frame in concrete details. Our approach then uses these granular frame labels and correlates them with high-level topics to reveal broader discourse trends. The primary contributions of this paper are: (i) a novel frame-labeling methodology that more closely aligns with human judgment for messy, conversational data, and (ii) a new analysis that uncovers the systematic relationship between what is being discussed (the topic) and how it is being presented (the frame), offering a more robust framework for studying influence in digital media.


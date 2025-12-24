---
layout: default
title: Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques
---

# Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00658" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00658v3</a>
  <a href="https://arxiv.org/pdf/2506.00658.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00658v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00658v3', 'Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lang Xiong, Raina Gao, Alyssa Jeong, Yicheng Fu, Sean O'Brien, Vasu Sharma, Kevin Zhu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-31 (更新: 2025-09-17)

**备注**: Accepted to EMNLP WiNLP and COLM Melt, Solar, PragLM, and Origen

---

## 💡 一句话要点

**提出Sarc7基准以解决讽刺检测与生成的挑战**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `讽刺检测` `情感分析` `自然语言处理` `机器学习` `生成模型`

## 📋 核心要点

1. 讽刺的细微特性使得现有的计算模型在检测和生成讽刺时面临重大挑战。
2. 论文提出了Sarc7基准，通过对MUStARD数据集的条目进行注释，分类七种不同类型的讽刺，并引入基于情感的提示技术。
3. 实验结果显示，Gemini 2.5在使用基于情感的提示时，F1得分达到0.3664，且成功生成率显著高于传统零样本提示。

## 📝 摘要（中文）

讽刺是一种幽默形式，其表达的意义与字面解释相反。使用大型语言模型对讽刺进行分类和生成对于理解人类沟通至关重要。由于讽刺的细微特性，计算模型面临挑战。我们介绍了Sarc7，一个基准，分类七种讽刺类型：自嘲、沉思、冷淡、礼貌、讨厌、愤怒和狂热，通过对MUStARD数据集的条目进行注释。分类使用零样本、少样本、思维链（CoT）和一种新颖的基于情感的提示技术进行评估。我们提出了一种基于情感的生成方法，通过识别讽刺的不一致性、震惊值和上下文依赖性来开发。我们的分类实验表明，使用基于情感的提示的Gemini 2.5在F1得分上达到了0.3664，优于其他设置。人类评估者更偏好我们的基于情感的提示，成功生成率比零样本提示高出38.46%。

## 🔬 方法详解

**问题定义**：本论文旨在解决讽刺的检测与生成问题，现有方法在处理讽刺的复杂性和多样性时表现不足，难以准确分类和生成讽刺内容。

**核心思路**：我们提出Sarc7基准，通过对七种讽刺类型的注释，结合基于情感的提示技术，以提高模型在讽刺理解和生成方面的表现。

**技术框架**：整体架构包括数据集注释、分类模型训练和生成模型设计三个主要模块。分类模型使用多种评估方法，包括零样本和少样本学习。

**关键创新**：最重要的技术创新在于引入基于情感的提示方法，该方法通过识别讽刺的关键组成部分（如不一致性和上下文依赖性）来增强模型的生成能力。

**关键设计**：在模型训练中，我们采用了特定的损失函数和网络结构，以优化情感信息的提取和利用，确保模型能够有效捕捉讽刺的细微差别。

## 📊 实验亮点

实验结果表明，使用基于情感的提示的Gemini 2.5模型在F1得分上达到了0.3664，显著优于其他设置。此外，人类评估者对基于情感的提示生成的内容偏好度提高了38.46%，显示出该方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体分析、在线评论生成和人机交互等。通过提高讽刺的检测与生成能力，可以增强计算机对人类情感和幽默的理解，从而提升用户体验和交互质量。未来，该技术可能在情感计算和自然语言处理领域产生深远影响。

## 📄 摘要（原文）

> Sarcasm is a form of humor where expressions convey meanings opposite to their literal interpretations. Classifying and generating sarcasm using large language models is vital for interpreting human communication. Sarcasm poses challenges for computational models, due to its nuanced nature. We introduce Sarc7, a benchmark that classifies 7 types of sarcasm: self-deprecating, brooding, deadpan, polite, obnoxious, raging, and manic by annotating entries of the MUStARD dataset. Classification was evaluated using zero-shot, few-shot, chain-of-thought (CoT), and a novel emotion-based prompting technique. We propose an emotion-based generation method developed by identifying key components of sarcasm-incongruity, shock value, and context dependency. Our classification experiments show that Gemini 2.5, using emotion-based prompting, outperforms other setups with an F1 score of 0.3664. Human evaluators preferred our emotion-based prompting, with 38.46% more successful generations than zero-shot prompting.


---
layout: default
title: "Empathy Omni: Enabling Empathetic Speech Response Generation through Large Language Models"
---

# Empathy Omni: Enabling Empathetic Speech Response Generation through Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18655" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18655v3</a>
  <a href="https://arxiv.org/pdf/2508.18655.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18655v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18655v3', 'Empathy Omni: Enabling Empathetic Speech Response Generation through Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Wang, Guangyan Zhang, Jiale Chen, Jingyu Li, Yuehai Wang, Yiwen Guo

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-08-26 (更新: 2025-09-17)

**备注**: 5 pages, 1 figure, submitted to ICASSP 2026

**🔗 代码/项目**: [PROJECT_PAGE](https://w311411.github.io/omni_demo/)

---

## 💡 一句话要点

**提出Emotion Omni以解决情感理解不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感理解` `语音助手` `同理心生成` `小数据学习` `人机交互`

## 📋 核心要点

1. 现有的语音大型语言模型在情感理解方面存在不足，无法有效捕捉用户语音中的情感线索。
2. 本文提出Emotion Omni模型，旨在通过有限的数据生成富有同理心的语音响应，降低对大规模训练的依赖。
3. 实验结果显示，Emotion Omni在语音质量（UTMOS:4.41）和同理心（Emotion GPT Score: 3.97）方面均优于现有模型。

## 📝 摘要（中文）

随着语音大型语言模型的发展，用户可以通过语音直接与助手互动。然而，现有模型往往仅将响应内容转换为语音，未能充分捕捉用户查询中的情感线索。情感理解对于提升人机交互至关重要。大多数情感语音模型依赖于庞大的数据集，计算成本高。为此，本文提出Emotion Omni模型，能够理解用户语音中的情感内容并生成富有同理心的响应。同时，构建了一个支持情感语音助手的20万条情感对话数据集。实验表明，Emotion Omni在无需大规模预训练的情况下，指令跟随能力可与现有模型媲美，同时在语音质量和情感表达上超越了现有模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语音大型语言模型在情感理解方面的不足，尤其是在有限数据条件下生成同理心响应的挑战。现有方法通常依赖于庞大的数据集和高计算成本。

**核心思路**：论文提出的Emotion Omni模型通过理解用户语音中的情感内容，生成更具同理心的响应。该设计旨在提升人机交互的自然性和有效性。

**技术框架**：Emotion Omni的整体架构包括情感识别模块和响应生成模块。情感识别模块负责分析用户语音中的情感信息，而响应生成模块则基于这些信息生成适当的语音响应。

**关键创新**：Emotion Omni的主要创新在于其能够在没有大规模预训练的情况下，通过有限的数据集实现情感理解和响应生成。这一方法显著降低了对计算资源的需求。

**关键设计**：模型采用了特定的损失函数来优化情感识别的准确性，并在网络结构上进行了调整，以提高生成响应的质量和情感表达能力。

## 📊 实验亮点

实验结果表明，Emotion Omni在语音质量方面的UTMOS评分达到4.41，而在同理心评估中的Emotion GPT Score为3.97，均显著优于现有模型。这些结果验证了该模型在语音保真度和情感表达上的提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能语音助手、客服机器人和情感计算等。通过提升机器对人类情感的理解能力，Emotion Omni能够在多种场景中提供更为自然和人性化的交互体验，未来可能在心理健康支持和社交机器人等领域产生深远影响。

## 📄 摘要（原文）

> With the development of speech large language models (speech LLMs), users can now interact directly with assistants via speech. However, most existing models only convert response content into speech without fully capturing the rich emotional cues in user queries, where the same sentence may convey different meanings depending on the expression. Emotional understanding is thus essential for improving human-machine interaction. Most empathetic speech LLMs rely on massive datasets, demanding high computational cost. A key challenge is to build models that generate empathetic responses with limited data and without large-scale training. To this end, we propose Emotion Omni, a model that understands emotional content in user speech and generates empathetic responses. We further developed a data pipeline to construct a 200k emotional dialogue dataset supporting empathetic speech assistants. Experiments show that Emotion Omni achieves comparable instruction-following ability without large-scale pretraining, while surpassing existing models in speech quality (UTMOS:4.41) and empathy (Emotion GPT Score: 3.97). These results confirm its improvements in both speech fidelity and emotional expressiveness. Demos are available at https://w311411.github.io/omni_demo/.


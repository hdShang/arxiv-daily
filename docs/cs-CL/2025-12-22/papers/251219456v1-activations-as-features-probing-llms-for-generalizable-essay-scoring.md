---
layout: default
title: "Activations as Features: Probing LLMs for Generalizable Essay Scoring Representations"
---

# Activations as Features: Probing LLMs for Generalizable Essay Scoring Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19456" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19456v1</a>
  <a href="https://arxiv.org/pdf/2512.19456.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19456v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19456v1', 'Activations as Features: Probing LLMs for Generalizable Essay Scoring Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinwei Chi, Ke Wang, Yu Chen, Xuanye Lin, Qiang Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**利用LLM激活值进行可泛化Essay评分表征学习，提升跨Prompt场景性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动作文评分` `大型语言模型` `激活值分析` `跨Prompt学习` `表征学习`

## 📋 核心要点

1. 跨Prompt作文评分面临评分标准多样性的挑战，现有方法侧重于优化LLM输出，忽略了中间层激活值可能蕴含的丰富信息。
2. 该论文的核心思想是探索LLM中间层激活值在跨Prompt作文评分中的判别能力，通过分析激活值来理解LLM的评分视角。
3. 实验结果表明，LLM的激活值在评估作文质量方面具有很强的判别能力，并且LLM能够根据不同的Prompt调整评估视角。

## 📝 摘要（中文）

由于评分标准的多样性，自动作文评分(AES)在跨Prompt设置中是一项具有挑战性的任务。以往的研究主要集中于利用大型语言模型(LLM)的输出来提高评分准确性，但我们认为中间层的激活值也可能提供有价值的信息。为了探索这种可能性，我们评估了LLM激活值在跨Prompt作文评分任务中的判别能力。具体来说，我们使用激活值来拟合探针，并进一步分析了不同模型和LLM的输入内容对这种判别能力的影响。通过计算不同Prompt下各种特征维度作文的方向，我们分析了大型语言模型在作文类型和特征方面的评估视角的差异。结果表明，激活值在评估作文质量方面具有很强的判别能力，并且LLM可以调整其评估视角以适应不同的特征和作文类型，从而有效地处理跨Prompt设置中评分标准的多样性。

## 🔬 方法详解

**问题定义**：自动作文评分（AES）旨在自动评估作文质量。在跨Prompt场景下，由于不同Prompt对应的评分标准存在差异，导致模型难以泛化。现有方法主要集中于优化LLM的输出，例如微调LLM或设计复杂的后处理模块，但忽略了LLM中间层激活值可能包含的丰富信息，这些信息可能反映了LLM对作文的深层理解和评估标准。

**核心思路**：该论文的核心思路是利用LLM中间层的激活值作为特征，通过训练简单的探针（probe）来预测作文的质量。这种方法假设LLM的激活值已经包含了对作文质量的有效表征，而探针的作用是将这些表征提取出来并映射到评分空间。通过分析不同Prompt下激活值的变化，可以了解LLM如何根据不同的Prompt调整其评分标准。

**技术框架**：整体框架包括以下几个步骤：1) 使用LLM处理作文文本，并提取指定中间层的激活值。2) 使用提取的激活值作为特征，训练一个线性探针来预测作文的评分。3) 通过计算不同Prompt下作文在不同特征维度上的方向，分析LLM评估视角的差异。4) 评估探针在跨Prompt场景下的泛化性能。

**关键创新**：该论文的关键创新在于将LLM的激活值作为特征，用于跨Prompt作文评分。与以往方法不同，该方法不依赖于对LLM输出的直接优化，而是通过分析LLM内部的表征来理解其评分机制。这种方法可以更好地利用LLM的知识，并提高模型的泛化能力。

**关键设计**：论文中使用了线性探针，这是一种简单的线性模型，用于将激活值映射到评分空间。选择线性探针的原因是其易于训练和解释。论文还计算了不同Prompt下作文在不同特征维度上的方向，这可以帮助理解LLM如何根据不同的Prompt调整其评分标准。具体来说，使用了余弦相似度来衡量不同Prompt下作文方向的差异。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19456v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19456v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19456v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，LLM的激活值在评估作文质量方面具有很强的判别能力。通过训练线性探针，可以在跨Prompt场景下取得良好的评分效果。此外，论文还发现LLM可以根据不同的Prompt调整其评估视角，有效地处理评分标准的多样性。具体性能数据未知，但论文强调了激活值特征的有效性和LLM评估视角的自适应性。

## 🎯 应用场景

该研究成果可应用于自动作文评分系统，尤其是在需要处理多种Prompt的场景下。通过分析LLM的激活值，可以更好地理解LLM的评分机制，并提高评分系统的准确性和泛化能力。此外，该方法还可以用于教育诊断，帮助教师了解学生在不同方面的写作能力。

## 📄 摘要（原文）

> Automated essay scoring (AES) is a challenging task in cross-prompt settings due to the diversity of scoring criteria. While previous studies have focused on the output of large language models (LLMs) to improve scoring accuracy, we believe activations from intermediate layers may also provide valuable information. To explore this possibility, we evaluated the discriminative power of LLMs' activations in cross-prompt essay scoring task. Specifically, we used activations to fit probes and further analyzed the effects of different models and input content of LLMs on this discriminative power. By computing the directions of essays across various trait dimensions under different prompts, we analyzed the variation in evaluation perspectives of large language models concerning essay types and traits. Results show that the activations possess strong discriminative power in evaluating essay quality and that LLMs can adapt their evaluation perspectives to different traits and essay types, effectively handling the diversity of scoring criteria in cross-prompt settings.


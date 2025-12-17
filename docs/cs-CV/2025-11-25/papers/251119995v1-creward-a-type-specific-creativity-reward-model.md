---
layout: default
title: CREward: A Type-Specific Creativity Reward Model
---

# CREward: A Type-Specific Creativity Reward Model

**arXiv**: [2511.19995v1](https://arxiv.org/abs/2511.19995) | [PDF](https://arxiv.org/pdf/2511.19995.pdf)

**作者**: Jiyeon Han, Ali Mahdavi-Amiri, Hao Zhang, Haedong Jeong

---

## 💡 一句话要点

**提出类型特定创造力奖励模型CREward，用于评估和生成创意图像。**

**关键词**: `创造力评估` `奖励模型` `视觉语言模型` `图像生成` `人类感知对齐`

## 📋 核心要点

1. 核心问题：将创造力视为单一量度过于简化，需按类型区分评估。
2. 方法要点：基于人类基准评估和LVLM预测，训练多类型创造力奖励模型。
3. 实验或效果：模型在创造力评估、可解释性和创意样本获取中应用验证。

## 📄 摘要（原文）

> Creativity is a complex phenomenon. When it comes to representing and assessing creativity, treating it as a single undifferentiated quantity would appear naive and underwhelming. In this work, we learn the \emph{first type-specific creativity reward model}, coined CREward, which spans three creativity ``axes," geometry, material, and texture, to allow us to view creativity through the lens of the image formation pipeline. To build our reward model, we first conduct a human benchmark evaluation to capture human perception of creativity for each type across various creative images. We then analyze the correlation between human judgments and predictions by large vision-language models (LVLMs), confirming that LVLMs exhibit strong alignment with human perception. Building on this observation, we collect LVLM-generated labels to train our CREward model that is applicable to both evaluation and generation of creative images. We explore three applications of CREward: creativity assessment, explainable creativity, and creative sample acquisition for both human design inspiration and guiding creative generation through low-rank adaptation.


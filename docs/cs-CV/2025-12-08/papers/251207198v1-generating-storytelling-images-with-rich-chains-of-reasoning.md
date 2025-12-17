---
layout: default
title: Generating Storytelling Images with Rich Chains-of-Reasoning
---

# Generating Storytelling Images with Rich Chains-of-Reasoning

**arXiv**: [2512.07198v1](https://arxiv.org/abs/2512.07198) | [PDF](https://arxiv.org/pdf/2512.07198.pdf)

**作者**: Xiujie Song, Qi Jia, Shota Watanabe, Xiaoyi Pang, Ruijie Chen, Mengyue Wu, Kenny Q. Zhu

---

## 💡 一句话要点

**提出StorytellingPainter两阶段流水线，结合大语言模型与文生图模型生成富含推理链的故事图像**

**关键词**: `故事图像生成` `推理链` `大语言模型` `文生图模型` `评估框架` `轻量模型训练`

## 📋 核心要点

1. 核心问题：故事图像语义复杂且稀缺，生成任务具挑战性
2. 方法要点：利用LLMs进行创意推理，T2I模型视觉合成，构建两阶段生成流水线
3. 实验或效果：开发评估框架验证方法可行性，训练Mini-Storytellers模型缩小开源与专有LLMs差距

## 📄 摘要（原文）

> An image can convey a compelling story by presenting rich, logically connected visual clues. These connections form Chains-of-Reasoning (CoRs) within the image, enabling viewers to infer events, causal relationships, and other information, thereby understanding the underlying story. In this paper, we focus on these semantically rich images and define them as Storytelling Images. Such images have diverse applications beyond illustration creation and cognitive screening, leveraging their ability to convey multi-layered information visually and inspire active interpretation. However, due to their complex semantic nature, Storytelling Images are inherently challenging to create, and thus remain relatively scarce. To address this challenge, we introduce the Storytelling Image Generation task, which explores how generative AI models can be leveraged to create such images. Specifically, we propose a two-stage pipeline, StorytellingPainter, which combines the creative reasoning abilities of Large Language Models (LLMs) with the visual synthesis capabilities of Text-to-Image (T2I) models to generate Storytelling Images. Alongside this pipeline, we develop a dedicated evaluation framework comprising three main evaluators: a Semantic Complexity Evaluator, a KNN-based Diversity Evaluator and a Story-Image Alignment Evaluator. Given the critical role of story generation in the Storytelling Image Generation task and the performance disparity between open-source and proprietary LLMs, we further explore tailored training strategies to reduce this gap, resulting in a series of lightweight yet effective models named Mini-Storytellers. Experimental results demonstrate the feasibility and effectiveness of our approaches. The code is available at https://github.com/xiujiesong/StorytellingImageGeneration.


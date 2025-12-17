---
layout: default
title: Beyond Realism: Learning the Art of Expressive Composition with StickerNet
---

# Beyond Realism: Learning the Art of Expressive Composition with StickerNet

**arXiv**: [2511.20957v1](https://arxiv.org/abs/2511.20957) | [PDF](https://arxiv.org/pdf/2511.20957.pdf)

**作者**: Haoming Lu, David Kocharian, Humphrey Shi

---

## 💡 一句话要点

**提出StickerNet框架以解决图像表达性合成任务，学习真实编辑行为。**

**关键词**: `图像合成` `表达性编辑` `两阶段框架` `真实数据集` `用户意图学习`

## 📋 核心要点

1. 核心问题：传统图像合成强调真实感，但实际编辑中用户追求艺术性和社交吸引力。
2. 方法要点：两阶段框架先识别合成类型，再预测位置、透明度等放置参数。
3. 实验或效果：基于真实编辑数据训练，用户研究显示优于基线并接近人类行为。

## 📄 摘要（原文）

> As a widely used operation in image editing workflows, image composition has traditionally been studied with a focus on achieving visual realism and semantic plausibility. However, in practical editing scenarios of the modern content creation landscape, many compositions are not intended to preserve realism. Instead, users of online platforms motivated by gaining community recognition often aim to create content that is more artistic, playful, or socially engaging. Taking inspiration from this observation, we define the expressive composition task, a new formulation of image composition that embraces stylistic diversity and looser placement logic, reflecting how users edit images on real-world creative platforms. To address this underexplored problem, we present StickerNet, a two-stage framework that first determines the composition type, then predicts placement parameters such as opacity, mask, location, and scale accordingly. Unlike prior work that constructs datasets by simulating object placements on real images, we directly build our dataset from 1.8 million editing actions collected on an anonymous online visual creation and editing platform, each reflecting user-community validated placement decisions. This grounding in authentic editing behavior ensures strong alignment between task definition and training supervision. User studies and quantitative evaluations show that StickerNet outperforms common baselines and closely matches human placement behavior, demonstrating the effectiveness of learning from real-world editing patterns despite the inherent ambiguity of the task. This work introduces a new direction in visual understanding that emphasizes expressiveness and user intent over realism.


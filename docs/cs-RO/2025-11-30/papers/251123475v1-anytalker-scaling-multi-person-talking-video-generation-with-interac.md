---
layout: default
title: AnyTalker: Scaling Multi-Person Talking Video Generation with Interactivity Refinement
---

# AnyTalker: Scaling Multi-Person Talking Video Generation with Interactivity Refinement

**arXiv**: [2511.23475v1](https://arxiv.org/abs/2511.23475) | [PDF](https://arxiv.org/pdf/2511.23475.pdf)

**作者**: Zhizhou Zhong, Yicheng Ji, Zhe Kong, Yiying Liu, Jiarui Wang, Jiasun Feng, Lupeng Liu, Xiangyi Wang, Yanjia Li, Yuqing She, Ying Qin, Huan Li, Shuiyang Mao, Wei Liu, Wenhan Luo

---

## 💡 一句话要点

**提出AnyTalker框架以解决多人物说话视频生成中的数据成本高和交互性差问题。**

**关键词**: `多人物视频生成` `扩散变换器` `身份感知注意力` `交互性优化` `唇同步` `数据高效训练`

## 📋 核心要点

1. 核心问题：多人物数据收集成本高，驱动多身份时交互性难以保持连贯。
2. 方法要点：采用可扩展多流处理架构，引入身份感知注意力机制迭代处理身份-音频对。
3. 实验或效果：仅需单人视频训练，少量多人片段优化交互性，在唇同步、视觉质量和自然交互性上表现优异。

## 📄 摘要（原文）

> Recently, multi-person video generation has started to gain prominence. While a few preliminary works have explored audio-driven multi-person talking video generation, they often face challenges due to the high costs of diverse multi-person data collection and the difficulty of driving multiple identities with coherent interactivity. To address these challenges, we propose AnyTalker, a multi-person generation framework that features an extensible multi-stream processing architecture. Specifically, we extend Diffusion Transformer's attention block with a novel identity-aware attention mechanism that iteratively processes identity-audio pairs, allowing arbitrary scaling of drivable identities. Besides, training multi-person generative models demands massive multi-person data. Our proposed training pipeline depends solely on single-person videos to learn multi-person speaking patterns and refines interactivity with only a few real multi-person clips. Furthermore, we contribute a targeted metric and dataset designed to evaluate the naturalness and interactivity of the generated multi-person videos. Extensive experiments demonstrate that AnyTalker achieves remarkable lip synchronization, visual quality, and natural interactivity, striking a favorable balance between data costs and identity scalability.


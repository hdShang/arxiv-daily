---
layout: default
title: GraphMatch: Fusing Language and Graph Representations in a Dynamic Two-Sided Work Marketplace
---

# GraphMatch: Fusing Language and Graph Representations in a Dynamic Two-Sided Work Marketplace

**arXiv**: [2512.02849v1](https://arxiv.org/abs/2512.02849) | [PDF](https://arxiv.org/pdf/2512.02849.pdf)

**作者**: Mikołaj Sacha, Hammad Jafri, Mattie Terzolo, Ayan Sinha, Andrew Rabinovich

---

## 💡 一句话要点

**提出GraphMatch框架，融合语言与图表示以解决文本丰富动态双边市场的匹配推荐问题。**

**关键词**: `双边市场推荐` `图神经网络` `预训练语言模型` `动态图表示` `对抗负采样` `实时推理`

## 📋 核心要点

1. 核心问题：文本丰富动态双边市场中，内容与交互图随时间演变，推荐匹配面临挑战。
2. 方法要点：结合预训练语言模型与图神经网络，采用对抗负采样和时点子图训练学习表示。
3. 实验或效果：在Upwork数据上优于纯语言或图基线，运行时高效，适合实时推理。

## 📄 摘要（原文）

> Recommending matches in a text-rich, dynamic two-sided marketplace presents unique challenges due to evolving content and interaction graphs. We introduce GraphMatch, a new large-scale recommendation framework that fuses pre-trained language models with graph neural networks to overcome these challenges. Unlike prior approaches centered on standalone models, GraphMatch is a comprehensive recipe built on powerful text encoders and GNNs working in tandem. It employs adversarial negative sampling alongside point-in-time subgraph training to learn representations that capture both the fine-grained semantics of evolving text and the time-sensitive structure of the graph. We evaluated extensively on interaction data from Upwork, a leading labor marketplace, at large scale, and discuss our approach towards low-latency inference suitable for real-time use. In our experiments, GraphMatch outperforms language-only and graph-only baselines on matching tasks while being efficient at runtime. These results demonstrate that unifying language and graph representations yields a highly effective solution to text-rich, dynamic two-sided recommendations, bridging the gap between powerful pretrained LMs and large-scale graphs in practice.


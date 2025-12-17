---
layout: default
title: Map the Flow: Revealing Hidden Pathways of Information in VideoLLMs
---

# Map the Flow: Revealing Hidden Pathways of Information in VideoLLMs

**arXiv**: [2510.13251v1](https://arxiv.org/abs/2510.13251) | [PDF](https://arxiv.org/pdf/2510.13251.pdf)

**作者**: Minji Kim, Taekyung Kim, Bohyung Han

---

## 💡 一句话要点

**揭示VideoLLMs信息流机制以提升视频问答性能与可解释性**

**关键词**: `视频大语言模型` `机制可解释性` `视频问答` `信息流分析` `注意力机制` `模型优化`

## 📋 核心要点

1. 核心问题：VideoLLMs内部信息提取与传播机制不明确，影响模型可解释性。
2. 方法要点：使用机制可解释性技术分析信息流，识别跨帧交互与视频语言集成模式。
3. 实验或效果：通过选择有效信息路径，在保留性能下减少58%注意力边，提升效率。

## 📄 摘要（原文）

> Video Large Language Models (VideoLLMs) extend the capabilities of
> vision-language models to spatiotemporal inputs, enabling tasks such as video
> question answering (VideoQA). Despite recent advances in VideoLLMs, their
> internal mechanisms on where and how they extract and propagate video and
> textual information remain less explored. In this study, we investigate the
> internal information flow of VideoLLMs using mechanistic interpretability
> techniques. Our analysis reveals consistent patterns across diverse VideoQA
> tasks: (1) temporal reasoning in VideoLLMs initiates with active cross-frame
> interactions in early-to-middle layers, (2) followed by progressive
> video-language integration in middle layers. This is facilitated by alignment
> between video representations and linguistic embeddings containing temporal
> concepts. (3) Upon completion of this integration, the model is ready to
> generate correct answers in middle-to-late layers. (4) Based on our analysis,
> we show that VideoLLMs can retain their VideoQA performance by selecting these
> effective information pathways while suppressing a substantial amount of
> attention edges, e.g., 58% in LLaVA-NeXT-7B-Video-FT. These findings provide a
> blueprint on how VideoLLMs perform temporal reasoning and offer practical
> insights for improving model interpretability and downstream generalization.
> Our project page with the source code is available at
> https://map-the-flow.github.io


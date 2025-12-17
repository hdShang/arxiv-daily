---
layout: default
title: Language-Guided Graph Representation Learning for Video Summarization
---

# Language-Guided Graph Representation Learning for Video Summarization

**arXiv**: [2511.10953v1](https://arxiv.org/abs/2511.10953) | [PDF](https://arxiv.org/pdf/2511.10953.pdf)

**作者**: Wenrui Li, Wei Han, Hengyu Man, Wangmeng Zuo, Xiaopeng Fan, Yonghong Tian

---

## 💡 一句话要点

**提出语言引导图表示学习网络以解决视频摘要中的全局依赖和用户定制问题**

**关键词**: `视频摘要` `图表示学习` `多模态融合` `语言引导` `图卷积网络` `EM算法`

## 📋 核心要点

1. 现有方法难以捕捉视频全局依赖和适应多模态用户定制
2. 构建视频图生成器和图推理模块，结合语言引导嵌入生成摘要
3. 实验显示性能优于基准，推理时间和参数分别减少87.8%和91.7%

## 📄 摘要（原文）

> With the rapid growth of video content on social media, video summarization has become a crucial task in multimedia processing. However, existing methods face challenges in capturing global dependencies in video content and accommodating multimodal user customization. Moreover, temporal proximity between video frames does not always correspond to semantic proximity. To tackle these challenges, we propose a novel Language-guided Graph Representation Learning Network (LGRLN) for video summarization. Specifically, we introduce a video graph generator that converts video frames into a structured graph to preserve temporal order and contextual dependencies. By constructing forward, backward and undirected graphs, the video graph generator effectively preserves the sequentiality and contextual relationships of video content. We designed an intra-graph relational reasoning module with a dual-threshold graph convolution mechanism, which distinguishes semantically relevant frames from irrelevant ones between nodes. Additionally, our proposed language-guided cross-modal embedding module generates video summaries with specific textual descriptions. We model the summary generation output as a mixture of Bernoulli distribution and solve it with the EM algorithm. Experimental results show that our method outperforms existing approaches across multiple benchmarks. Moreover, we proposed LGRLN reduces inference time and model parameters by 87.8% and 91.7%, respectively. Our codes and pre-trained models are available at https://github.com/liwrui/LGRLN.


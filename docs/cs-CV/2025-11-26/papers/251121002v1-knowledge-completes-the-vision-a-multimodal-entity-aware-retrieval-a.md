---
layout: default
title: Knowledge Completes the Vision: A Multimodal Entity-aware Retrieval-Augmented Generation Framework for News Image Captioning
---

# Knowledge Completes the Vision: A Multimodal Entity-aware Retrieval-Augmented Generation Framework for News Image Captioning

**arXiv**: [2511.21002v1](https://arxiv.org/abs/2511.21002) | [PDF](https://arxiv.org/pdf/2511.21002.pdf)

**作者**: Xiaoxing You, Qiang Huang, Lingyu Li, Chi Zhang, Xiaopeng Liu, Min Zhang, Jun Yu

---

## 💡 一句话要点

**提出MERGE框架以解决新闻图像描述中的信息不完整与跨模态对齐问题**

**关键词**: `新闻图像描述` `多模态检索增强生成` `实体中心知识库` `跨模态对齐` `视觉实体匹配` `领域适应性`

## 📋 核心要点

1. 核心问题：现有方法存在信息覆盖不全、跨模态对齐弱和视觉实体定位不佳
2. 方法要点：构建实体中心多模态知识库，采用多阶段假设-描述策略增强对齐
3. 实验或效果：在多个数据集上显著提升CIDEr和F1分数，展示强鲁棒性

## 📄 摘要（原文）

> News image captioning aims to produce journalistically informative descriptions by combining visual content with contextual cues from associated articles. Despite recent advances, existing methods struggle with three key challenges: (1) incomplete information coverage, (2) weak cross-modal alignment, and (3) suboptimal visual-entity grounding. To address these issues, we introduce MERGE, the first Multimodal Entity-aware Retrieval-augmented GEneration framework for news image captioning. MERGE constructs an entity-centric multimodal knowledge base (EMKB) that integrates textual, visual, and structured knowledge, enabling enriched background retrieval. It improves cross-modal alignment through a multistage hypothesis-caption strategy and enhances visual-entity matching via dynamic retrieval guided by image content. Extensive experiments on GoodNews and NYTimes800k show that MERGE significantly outperforms state-of-the-art baselines, with CIDEr gains of +6.84 and +1.16 in caption quality, and F1-score improvements of +4.14 and +2.64 in named entity recognition. Notably, MERGE also generalizes well to the unseen Visual News dataset, achieving +20.17 in CIDEr and +6.22 in F1-score, demonstrating strong robustness and domain adaptability.


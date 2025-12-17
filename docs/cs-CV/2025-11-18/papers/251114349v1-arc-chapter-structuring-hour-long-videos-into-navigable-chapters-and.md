---
layout: default
title: ARC-Chapter: Structuring Hour-Long Videos into Navigable Chapters and Hierarchical Summaries
---

# ARC-Chapter: Structuring Hour-Long Videos into Navigable Chapters and Hierarchical Summaries

**arXiv**: [2511.14349v1](https://arxiv.org/abs/2511.14349) | [PDF](https://arxiv.org/pdf/2511.14349.pdf)

**作者**: Junfu Pu, Teng Wang, Yixiao Ge, Yuying Ge, Chen Li, Ying Shan

---

## 💡 一句话要点

**提出ARC-Chapter模型，通过大规模双语章节数据集解决长视频结构化问题**

**关键词**: `长视频结构化` `视频章节化` `多模态融合` `大规模数据集` `评估指标GRACE`

## 📋 核心要点

1. 核心问题：现有方法因小规模粗标注，难以泛化到长视频的细微过渡
2. 方法要点：构建百万级双语章节数据集，融合多模态信息实现层次化标注
3. 实验或效果：显著提升性能，F1和SODA分数分别提高14.0%和11.3%

## 📄 摘要（原文）

> The proliferation of hour-long videos (e.g., lectures, podcasts, documentaries) has intensified demand for efficient content structuring. However, existing approaches are constrained by small-scale training with annotations that are typical short and coarse, restricting generalization to nuanced transitions in long videos. We introduce ARC-Chapter, the first large-scale video chaptering model trained on over million-level long video chapters, featuring bilingual, temporally grounded, and hierarchical chapter annotations. To achieve this goal, we curated a bilingual English-Chinese chapter dataset via a structured pipeline that unifies ASR transcripts, scene texts, visual captions into multi-level annotations, from short title to long summaries. We demonstrate clear performance improvements with data scaling, both in data volume and label intensity. Moreover, we design a new evaluation metric termed GRACE, which incorporates many-to-one segment overlaps and semantic similarity, better reflecting real-world chaptering flexibility. Extensive experiments demonstrate that ARC-Chapter establishes a new state-of-the-art by a significant margin, outperforming the previous best by 14.0% in F1 score and 11.3% in SODA score. Moreover, ARC-Chapter shows excellent transferability, improving the state-of-the-art on downstream tasks like dense video captioning on YouCook2.


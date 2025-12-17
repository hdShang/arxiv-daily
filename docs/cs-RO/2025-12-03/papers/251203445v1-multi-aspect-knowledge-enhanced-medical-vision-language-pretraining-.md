---
layout: default
title: Multi-Aspect Knowledge-Enhanced Medical Vision-Language Pretraining with Multi-Agent Data Generation
---

# Multi-Aspect Knowledge-Enhanced Medical Vision-Language Pretraining with Multi-Agent Data Generation

**arXiv**: [2512.03445v1](https://arxiv.org/abs/2512.03445) | [PDF](https://arxiv.org/pdf/2512.03445.pdf)

**作者**: Xieji Li, Siyuan Yan, Yingsheng Liu, H. Peter Soyer, Monika Janda, Victoria Mar, Zongyuan Ge

---

## 💡 一句话要点

**提出多智能体数据生成与本体多知识增强的医学视觉语言预训练框架，以解决数据噪声和长文本复杂性。**

**关键词**: `医学视觉语言预训练` `多智能体数据生成` `本体知识增强` `皮肤病学分析` `零样本学习` `跨模态检索`

## 📋 核心要点

1. 核心问题：现有方法难以处理网络收集数据的噪声和非结构化长医学文本的复杂性。
2. 方法要点：通过多智能体数据生成系统提升数据质量，并利用本体多知识增强预训练分解长文本进行细粒度对齐。
3. 实验或效果：在皮肤病学领域验证，零样本性能在疾病分类和跨模态检索任务上达到最优，并发布增强数据集。

## 📄 摘要（原文）

> Vision-language pretraining (VLP) has emerged as a powerful paradigm in medical image analysis, enabling representation learning from large-scale image-text pairs without relying on expensive manual annotations. However, existing methods often struggle with the noise inherent in web-collected data and the complexity of unstructured long medical texts. To address these challenges, we propose a novel VLP framework integrating a Multi-Agent data GENeration (MAGEN) system and Ontology-based Multi-Aspect Knowledge-Enhanced (O-MAKE) pretraining. First, MAGEN enhances data quality by synthesizing knowledge-enriched descriptions via a foundation model-assisted captioning and retrieval-based verification pipeline. Second, O-MAKE addresses the difficulty of learning from long, unstructured texts by decomposing them into distinct knowledge aspects. This facilitates fine-grained alignment at both global and patch levels, while explicitly modeling medical concept relationships through ontology-guided mechanisms. We validate our framework in the field of dermatology, where comprehensive experiments demonstrate the effectiveness of each component. Our approach achieves state-of-the-art zero-shot performance on disease classification and cross-modal retrieval tasks across eight datasets. Our code and the augmented dataset Derm1M-AgentAug, comprising over 400k skin-image-text pairs, will be released at https://github.com/SiyuanYan1/Derm1M.


---
layout: default
title: LandSegmenter: Towards a Flexible Foundation Model for Land Use and Land Cover Mapping
---

# LandSegmenter: Towards a Flexible Foundation Model for Land Use and Land Cover Mapping

**arXiv**: [2511.08156v1](https://arxiv.org/abs/2511.08156) | [PDF](https://arxiv.org/pdf/2511.08156.pdf)

**作者**: Chenying Liu, Wei Huang, Xiao Xiang Zhu

---

## 💡 一句话要点

**提出LandSegmenter框架以解决土地利用与覆盖映射中模型泛化性差和数据标注成本高的问题**

**关键词**: `土地利用与覆盖映射` `基础模型` `弱监督学习` `多模态遥感` `零样本学习` `语义分割`

## 📋 核心要点

1. 核心问题：现有LULC模型依赖特定模态和固定分类体系，泛化性差，且任务无关基础模型需微调，任务特定模型需大量标注数据
2. 方法要点：构建弱标签数据集LAS，集成遥感适配器和文本编码器，采用置信度引导融合策略提升零样本性能
3. 实验或效果：在六个数据集上评估，零样本和迁移学习表现优异，弱监督有效构建任务特定基础模型

## 📄 摘要（原文）

> Land Use and Land Cover (LULC) mapping is a fundamental task in Earth Observation (EO). However, current LULC models are typically developed for a specific modality and a fixed class taxonomy, limiting their generability and broader applicability. Recent advances in foundation models (FMs) offer promising opportunities for building universal models. Yet, task-agnostic FMs often require fine-tuning for downstream applications, whereas task-specific FMs rely on massive amounts of labeled data for training, which is costly and impractical in the remote sensing (RS) domain. To address these challenges, we propose LandSegmenter, an LULC FM framework that resolves three-stage challenges at the input, model, and output levels. From the input side, to alleviate the heavy demand on labeled data for FM training, we introduce LAnd Segment (LAS), a large-scale, multi-modal, multi-source dataset built primarily with globally sampled weak labels from existing LULC products. LAS provides a scalable, cost-effective alternative to manual annotation, enabling large-scale FM training across diverse LULC domains. For model architecture, LandSegmenter integrates an RS-specific adapter for cross-modal feature extraction and a text encoder for semantic awareness enhancement. At the output stage, we introduce a class-wise confidence-guided fusion strategy to mitigate semantic omissions and further improve LandSegmenter's zero-shot performance. We evaluate LandSegmenter on six precisely annotated LULC datasets spanning diverse modalities and class taxonomies. Extensive transfer learning and zero-shot experiments demonstrate that LandSegmenter achieves competitive or superior performance, particularly in zero-shot settings when transferred to unseen datasets. These results highlight the efficacy of our proposed framework and the utility of weak supervision for building task-specific FMs.


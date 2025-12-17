---
layout: default
title: Unbiased Semantic Decoding with Vision Foundation Models for Few-shot Segmentation
---

# Unbiased Semantic Decoding with Vision Foundation Models for Few-shot Segmentation

**arXiv**: [2511.15118v1](https://arxiv.org/abs/2511.15118) | [PDF](https://arxiv.org/pdf/2511.15118.pdf)

**作者**: Jin Wang, Bingfeng Zhang, Jian Pang, Weifeng Liu, Baodi Liu, Honglong Chen

---

## 💡 一句话要点

**提出无偏语义解码策略，结合SAM与CLIP提升少样本分割性能**

**关键词**: `少样本分割` `语义解码` `视觉基础模型` `特征增强` `提示生成`

## 📋 核心要点

1. 核心问题：SAM解码依赖精确提示，在少样本分割中易产生偏差，限制泛化能力。
2. 方法要点：设计全局补充和局部引导策略，利用CLIP语义增强SAM特征，生成目标提示嵌入。
3. 实验或效果：无需重新训练基础模型，通过语义引导提升目标区域关注，实现一致预测。

## 📄 摘要（原文）

> Few-shot segmentation has garnered significant attention. Many recent approaches attempt to introduce the Segment Anything Model (SAM) to handle this task. With the strong generalization ability and rich object-specific extraction ability of the SAM model, such a solution shows great potential in few-shot segmentation. However, the decoding process of SAM highly relies on accurate and explicit prompts, making previous approaches mainly focus on extracting prompts from the support set, which is insufficient to activate the generalization ability of SAM, and this design is easy to result in a biased decoding process when adapting to the unknown classes. In this work, we propose an Unbiased Semantic Decoding (USD) strategy integrated with SAM, which extracts target information from both the support and query set simultaneously to perform consistent predictions guided by the semantics of the Contrastive Language-Image Pre-training (CLIP) model. Specifically, to enhance the unbiased semantic discrimination of SAM, we design two feature enhancement strategies that leverage the semantic alignment capability of CLIP to enrich the original SAM features, mainly including a global supplement at the image level to provide a generalize category indicate with support image and a local guidance at the pixel level to provide a useful target location with query image. Besides, to generate target-focused prompt embeddings, a learnable visual-text target prompt generator is proposed by interacting target text embeddings and clip visual features. Without requiring re-training of the vision foundation models, the features with semantic discrimination draw attention to the target region through the guidance of prompt with rich target information.


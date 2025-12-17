---
layout: default
title: Breaking the Visual Shortcuts in Multimodal Knowledge-Based Visual Question Answering
---

# Breaking the Visual Shortcuts in Multimodal Knowledge-Based Visual Question Answering

**arXiv**: [2511.22843v1](https://arxiv.org/abs/2511.22843) | [PDF](https://arxiv.org/pdf/2511.22843.pdf)

**作者**: Dosung Lee, Sangwon Jung, Boyoung Kim, Minyoung Kim, Sungyeon Kim, Junyoung Sung, Paul Hongsuck Seo

---

## 💡 一句话要点

**提出RETINA基准和MIMIR模型以解决多模态知识问答中的视觉捷径问题。**

**关键词**: `多模态知识问答` `视觉捷径` `基准构建` `实体关系` `图像增强` `文档检索`

## 📋 核心要点

1. 现有MKB-VQA基准存在视觉捷径，模型可仅凭图像匹配主实体获得高准确率。
2. 引入RETINA基准，通过LLM驱动构建，查询涉及次要实体并配对相关图像以消除捷径。
3. 提出MIMIR模型，通过增强多相关实体图像丰富文档嵌入，在RETINA上验证有效性。

## 📄 摘要（原文）

> Existing Multimodal Knowledge-Based Visual Question Answering (MKB-VQA) benchmarks suffer from "visual shortcuts", as the query image typically matches the primary subject entity of the target document. We demonstrate that models can exploit these shortcuts, achieving comparable results using visual cues alone. To address this, we introduce Relational Entity Text-Image kNowledge Augmented (RETINA) benchmark, automatically constructed using an LLM-driven pipeline, consisting of 120k training and 2k human-curated test set. RETINA contains queries referencing secondary subjects (i.e. related entities) and pairs them with images of these related entities, removing the visual shortcut. When evaluated on RETINA existing models show significantly degraded performance, confirming their reliance on the shortcut. Furthermore, we propose Multi-Image MultImodal Retriever (MIMIR), which enriches document embeddings by augmenting images of multiple related entities, effectively handling RETINA, unlike prior work that uses only a single image per document. Our experiments validate the limitations of existing benchmarks and demonstrate the effectiveness of RETINA and MIMIR. Our project is available at: Project Page.


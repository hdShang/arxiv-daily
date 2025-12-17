---
layout: default
title: Exploring a Unified Vision-Centric Contrastive Alternatives on Multi-Modal Web Documents
---

# Exploring a Unified Vision-Centric Contrastive Alternatives on Multi-Modal Web Documents

**arXiv**: [2510.18703v1](https://arxiv.org/abs/2510.18703) | [PDF](https://arxiv.org/pdf/2510.18703.pdf)

**作者**: Yiqi Lin, Alex Jinpeng Wang, Linjie Li, Zhengyuan Yang, Mike Zheng Shou

---

## 💡 一句话要点

**提出VC2L框架以解决多模态网页文档中复杂跨模态关系建模问题**

**关键词**: `多模态学习` `对比学习` `视觉Transformer` `跨模态检索` `网页文档理解`

## 📋 核心要点

1. 核心问题：现有对比模型难以处理网页文档中文本与图像交错、松散对齐或视觉嵌入的复杂场景
2. 方法要点：VC2L使用单一视觉Transformer在像素空间统一建模，无需OCR或模态融合策略
3. 实验或效果：在多个检索基准上表现优于或媲美CLIP模型，验证了方法的有效性和可扩展性

## 📄 摘要（原文）

> Contrastive vision-language models such as CLIP have demonstrated strong
> performance across a wide range of multimodal tasks by learning from aligned
> image-text pairs. However, their ability to handle complex, real-world web
> documents remains limited, particularly in scenarios where text and images are
> interleaved, loosely aligned, or embedded in visual form. To address these
> challenges, we propose Vision-Centric Contrastive Learning (VC2L), a unified
> framework that models text, images, and their combinations using a single
> vision transformer. VC2L operates entirely in pixel space by rendering all
> inputs, whether textual, visual, or combined, as images, thus eliminating the
> need for OCR, text tokenization, or modality fusion strategy. To capture
> complex cross-modal relationships in multimodal web documents, VC2L employs a
> snippet-level contrastive learning objective that aligns consecutive multimodal
> segments, leveraging the inherent coherence of documents without requiring
> explicitly paired image-text data. To assess the effectiveness of this
> approach, we introduce three retrieval benchmarks, AnyCIR, SeqCIR, and CSR,
> designed to evaluate cross-modal retrieval, fine-grained sequential
> understanding, and generalization to unseen data, respectively. Empirical
> results show that VC2L achieves competitive or superior performance compared to
> CLIP-style models on both the proposed benchmarks and established datasets such
> as M-BEIR and MTEB. These findings underscore the potential of multimodal web
> data as a valuable training resource for contrastive learning and illustrate
> the scalability of a unified, vision-centric approach for multimodal
> representation learning. Code and models are available at:
> https://github.com/showlab/VC2L.


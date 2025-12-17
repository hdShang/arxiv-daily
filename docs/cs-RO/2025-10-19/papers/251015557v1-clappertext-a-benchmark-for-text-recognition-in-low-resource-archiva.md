---
layout: default
title: ClapperText: A Benchmark for Text Recognition in Low-Resource Archival Documents
---

# ClapperText: A Benchmark for Text Recognition in Low-Resource Archival Documents

**arXiv**: [2510.15557v1](https://arxiv.org/abs/2510.15557) | [PDF](https://arxiv.org/pdf/2510.15557.pdf)

**作者**: Tingyu Lin, Marco Peer, Florian Kleber, Robert Sablatnig

---

## 💡 一句话要点

**提出ClapperText基准数据集，用于低资源档案文档中的文本识别。**

**关键词**: `文本识别基准` `低资源档案文档` `手写文本识别` `视觉退化处理` `少样本学习` `旋转边界框标注`

## 📋 核心要点

1. 核心问题：解决视觉退化、低资源档案文档中手写和印刷文本识别的挑战。
2. 方法要点：基于二战档案视频构建数据集，提供旋转边界框和语义类别标注。
3. 实验或效果：在少量训练数据下微调模型显著提升性能，支持少样本学习。

## 📄 摘要（原文）

> This paper presents ClapperText, a benchmark dataset for handwritten and
> printed text recognition in visually degraded and low-resource settings. The
> dataset is derived from 127 World War II-era archival video segments containing
> clapperboards that record structured production metadata such as date,
> location, and camera-operator identity. ClapperText includes 9,813 annotated
> frames and 94,573 word-level text instances, 67% of which are handwritten and
> 1,566 are partially occluded. Each instance includes transcription, semantic
> category, text type, and occlusion status, with annotations available as
> rotated bounding boxes represented as 4-point polygons to support spatially
> precise OCR applications. Recognizing clapperboard text poses significant
> challenges, including motion blur, handwriting variation, exposure
> fluctuations, and cluttered backgrounds, mirroring broader challenges in
> historical document analysis where structured content appears in degraded,
> non-standard forms. We provide both full-frame annotations and cropped word
> images to support downstream tasks. Using a consistent per-video evaluation
> protocol, we benchmark six representative recognition and seven detection
> models under zero-shot and fine-tuned conditions. Despite the small training
> set (18 videos), fine-tuning leads to substantial performance gains,
> highlighting ClapperText's suitability for few-shot learning scenarios. The
> dataset offers a realistic and culturally grounded resource for advancing
> robust OCR and document understanding in low-resource archival contexts. The
> dataset and evaluation code are available at
> https://github.com/linty5/ClapperText.


---
layout: default
title: MonkeyOCR v1.5 Technical Report: Unlocking Robust Document Parsing for Complex Patterns
---

# MonkeyOCR v1.5 Technical Report: Unlocking Robust Document Parsing for Complex Patterns

**arXiv**: [2511.10390v1](https://arxiv.org/abs/2511.10390) | [PDF](https://arxiv.org/pdf/2511.10390.pdf)

**作者**: Jiarui Zhang, Yuliang Liu, Zijun Wu, Guosheng Pang, Zhili Ye, Yupei Zhong, Junteng Ma, Tao Wei, Haiyang Xu, Weikai Chen, Zeen Wang, Qiangjun Ji, Fanxi Zhou, Qi Zhang, Yuanrui Hu, Jiahao Liu, Zhang Li, Ziyang Zhang, Qiang Liu, Xiang Bai

---

## 💡 一句话要点

**提出MonkeyOCR v1.5统一视觉语言框架以解决复杂文档解析问题**

**关键词**: `文档解析` `视觉语言框架` `表格结构识别` `布局理解` `强化学习` `多模态模型`

## 📋 核心要点

1. 现实文档常含复杂布局，如多级表格和跨页结构，现有OCR系统难以处理。
2. 采用两阶段解析流程，先预测布局与阅读顺序，再局部识别文本、公式和表格。
3. 在OmniDocBench v1.5上实现SOTA性能，优于PPOCR-VL和MinerU 2.5。

## 📄 摘要（原文）

> Document parsing is a core task in document intelligence, supporting applications such as information extraction, retrieval-augmented generation, and automated document analysis. However, real-world documents often feature complex layouts with multi-level tables, embedded images or formulas, and cross-page structures, which remain challenging for existing OCR systems. We introduce MonkeyOCR v1.5, a unified vision-language framework that enhances both layout understanding and content recognition through a two-stage parsing pipeline. The first stage employs a large multimodal model to jointly predict document layout and reading order, leveraging visual information to ensure structural and sequential consistency. The second stage performs localized recognition of text, formulas, and tables within detected regions, maintaining high visual fidelity while reducing error propagation. To address complex table structures, we propose a visual consistency-based reinforcement learning scheme that evaluates recognition quality via render-and-compare alignment, improving structural accuracy without manual annotations. Additionally, two specialized modules, Image-Decoupled Table Parsing and Type-Guided Table Merging, are introduced to enable reliable parsing of tables containing embedded images and reconstruction of tables crossing pages or columns. Comprehensive experiments on OmniDocBench v1.5 demonstrate that MonkeyOCR v1.5 achieves state-of-the-art performance, outperforming PPOCR-VL and MinerU 2.5 while showing exceptional robustness in visually complex document scenarios.


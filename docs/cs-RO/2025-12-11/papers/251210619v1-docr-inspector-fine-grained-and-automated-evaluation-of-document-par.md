---
layout: default
title: DOCR-Inspector: Fine-Grained and Automated Evaluation of Document Parsing with VLM
---

# DOCR-Inspector: Fine-Grained and Automated Evaluation of Document Parsing with VLM

**arXiv**: [2512.10619v1](https://arxiv.org/abs/2512.10619) | [PDF](https://arxiv.org/pdf/2512.10619.pdf)

**作者**: Qintong Zhang, Junyuan Zhang, Zhifei Ren, Linke Ouyang, Zichen Wen, Junbo Niu, Yuan Qu, Bin Wang, Ka-Ho Chow, Conghui He, Wentao Zhang

---

## 💡 一句话要点

**提出DOCR-Inspector，通过细粒度错误检测与VLM评估解决文档解析质量评估难题。**

**关键词**: `文档解析评估` `视觉语言模型` `细粒度错误检测` `质量评估基准` `自动化评估`

## 📋 核心要点

1. 核心问题：标准基准存在偏差，整体评分掩盖错误模式，难以可靠评估真实场景文档解析质量。
2. 方法要点：基于VLM-as-a-Judge，定义28种错误类型，采用Chain-of-Checklist推理进行分层质量评估。
3. 实验或效果：在DOCRcaseBench上超越商业和开源模型，评估结果可指导解析结果优化。

## 📄 摘要（原文）

> Document parsing aims to transform unstructured PDF images into semi-structured data, facilitating the digitization and utilization of information in diverse domains. While vision language models (VLMs) have significantly advanced this task, achieving reliable, high-quality parsing in real-world scenarios remains challenging. Common practice often selects the top-performing model on standard benchmarks. However, these benchmarks may carry dataset-specific biases, leading to inconsistent model rankings and limited correlation with real-world performance. Moreover, benchmark metrics typically provide only overall scores, which can obscure distinct error patterns in output. This raises a key challenge: how can we reliably and comprehensively assess document parsing quality in the wild? We address this problem with DOCR-Inspector, which formalizes document parsing assessment as fine-grained error detection and analysis. Leveraging VLM-as-a-Judge, DOCR-Inspector analyzes a document image and its parsed output, identifies all errors, assigns them to one of 28 predefined types, and produces a comprehensive quality assessment. To enable this capability, we construct DOCRcase-200K for training and propose the Chain-of-Checklist reasoning paradigm to enable the hierarchical structure of parsing quality assessment. For empirical validation, we introduce DOCRcaseBench, a set of 882 real-world document parsing cases with manual annotations. On this benchmark, DOCR-Inspector-7B outperforms commercial models like Gemini 2.5 Pro, as well as leading open-source models. Further experiments demonstrate that its quality assessments provide valuable guidance for parsing results refinement, making DOCR-Inspector both a practical evaluator and a driver for advancing document parsing systems at scale. Model and code are released at: https://github.com/ZZZZZQT/DOCR-Inspector.


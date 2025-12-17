---
layout: default
title: Beyond Pixels: A Training-Free, Text-to-Text Framework for Remote Sensing Image Retrieval
---

# Beyond Pixels: A Training-Free, Text-to-Text Framework for Remote Sensing Image Retrieval

**arXiv**: [2512.10596v1](https://arxiv.org/abs/2512.10596) | [PDF](https://arxiv.org/pdf/2512.10596.pdf)

**作者**: J. Xiao, Y. Guo, X. Zi, K. Thiyagarajan, C. Moreira, M. Prasad

---

## 💡 一句话要点

**提出训练免费、纯文本的TRSLLaVA框架，通过文本到文本匹配解决遥感图像语义检索中的语义鸿沟问题。**

**关键词**: `遥感图像检索` `语义鸿沟` `训练免费方法` `文本到文本匹配` `VLM生成描述` `RSRT数据集`

## 📋 核心要点

1. 核心问题：遥感图像检索存在语义鸿沟，现有方法依赖昂贵领域训练且缺乏零样本基准。
2. 方法要点：引入RSRT数据集，将跨模态检索重构为文本到文本匹配，利用VLM生成描述在统一文本嵌入空间进行检索。
3. 实验或效果：在RSITMD和RSICD基准上，训练免费方法达到42.62%平均召回率，超越标准零样本基线及多个监督模型。

## 📄 摘要（原文）

> Semantic retrieval of remote sensing (RS) images is a critical task fundamentally challenged by the \textquote{semantic gap}, the discrepancy between a model's low-level visual features and high-level human concepts. While large Vision-Language Models (VLMs) offer a promising path to bridge this gap, existing methods often rely on costly, domain-specific training, and there is a lack of benchmarks to evaluate the practical utility of VLM-generated text in a zero-shot retrieval context. To address this research gap, we introduce the Remote Sensing Rich Text (RSRT) dataset, a new benchmark featuring multiple structured captions per image. Based on this dataset, we propose a fully training-free, text-only retrieval reference called TRSLLaVA. Our methodology reformulates cross-modal retrieval as a text-to-text (T2T) matching problem, leveraging rich text descriptions as queries against a database of VLM-generated captions within a unified textual embedding space. This approach completely bypasses model training or fine-tuning. Experiments on the RSITMD and RSICD benchmarks show our training-free method is highly competitive with state-of-the-art supervised models. For instance, on RSITMD, our method achieves a mean Recall of 42.62\%, nearly doubling the 23.86\% of the standard zero-shot CLIP baseline and surpassing several top supervised models. This validates that high-quality semantic representation through structured text provides a powerful and cost-effective paradigm for remote sensing image retrieval.


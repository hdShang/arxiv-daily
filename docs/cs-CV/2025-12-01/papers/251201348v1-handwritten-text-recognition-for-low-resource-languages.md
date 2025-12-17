---
layout: default
title: Handwritten Text Recognition for Low Resource Languages
---

# Handwritten Text Recognition for Low Resource Languages

**arXiv**: [2512.01348v1](https://arxiv.org/abs/2512.01348) | [PDF](https://arxiv.org/pdf/2512.01348.pdf)

**作者**: Sayantan Dey, Alireza Alaei, Partha Pratim Roy

---

## 💡 一句话要点

**提出BharatOCR模型，用于低资源语言（如印地语和乌尔都语）的段落级手写文本识别。**

**关键词**: `手写文本识别` `低资源语言` `段落级OCR` `Vision Transformer` `Transformer解码器` `语言模型优化`

## 📋 核心要点

1. 针对低资源语言段落级手写文本识别难题，缺乏全面语言资源。
2. 采用ViT-Transformer Decoder-LM架构，结合视觉特征提取、序列生成和语言模型优化。
3. 在自定义和公共数据集上评估，实现高字符识别率，超越现有乌尔都语方法。

## 📄 摘要（原文）

> Despite considerable progress in handwritten text recognition, paragraph-level handwritten text recognition, especially in low-resource languages, such as Hindi, Urdu and similar scripts, remains a challenging problem. These languages, often lacking comprehensive linguistic resources, require special attention to develop robust systems for accurate optical character recognition (OCR). This paper introduces BharatOCR, a novel segmentation-free paragraph-level handwritten Hindi and Urdu text recognition. We propose a ViT-Transformer Decoder-LM architecture for handwritten text recognition, where a Vision Transformer (ViT) extracts visual features, a Transformer decoder generates text sequences, and a pre-trained language model (LM) refines the output to improve accuracy, fluency, and coherence. Our model utilizes a Data-efficient Image Transformer (DeiT) model proposed for masked image modeling in this research work. In addition, we adopt a RoBERTa architecture optimized for masked language modeling (MLM) to enhance the linguistic comprehension and generative capabilities of the proposed model. The transformer decoder generates text sequences from visual embeddings. This model is designed to iteratively process a paragraph image line by line, called implicit line segmentation. The proposed model was evaluated using our custom dataset ('Parimal Urdu') and ('Parimal Hindi'), introduced in this research work, as well as two public datasets. The proposed model achieved benchmark results in the NUST-UHWR, PUCIT-OUHL, and Parimal-Urdu datasets, achieving character recognition rates of 96.24%, 92.05%, and 94.80%, respectively. The model also provided benchmark results using the Hindi dataset achieving a character recognition rate of 80.64%. The results obtained from our proposed model indicated that it outperformed several state-of-the-art Urdu text recognition methods.


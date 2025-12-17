---
layout: default
title: LFM2 Technical Report
---

# LFM2 Technical Report

**arXiv**: [2511.23404v1](https://arxiv.org/abs/2511.23404) | [PDF](https://arxiv.org/pdf/2511.23404.pdf)

**作者**: Alexander Amini, Anna Banaszak, Harold Benoit, Arthur Böök, Tarek Dakhran, Song Duong, Alfred Eng, Fernando Fernandes, Marc Härkönen, Anne Harrington, Ramin Hasani, Saniya Karwa, Yuri Khrustalev, Maxime Labonne, Mathias Lechner, Valentine Lechner, Simon Lee, Zetian Li, Noel Loo, Jacob Marks, Edoardo Mosca, Samuel J. Paech, Paul Pak, Rom N. Parnichkun, Alex Quach, Ryan Rogers, Daniela Rus, Nayan Saxena, Bettina Schlager, Tim Seyde, Jimmy T. H. Smith, Aditya Tadimeti, Neehal Tumma

---

## 💡 一句话要点

**提出LFM2系列液体基础模型，用于高效边缘部署和强任务能力。**

**关键词**: `边缘计算` `架构搜索` `知识蒸馏` `多模态模型` `检索增强`

## 📋 核心要点

1. 核心问题：在边缘设备上实现高效推理和强任务性能，受限于延迟和内存。
2. 方法要点：通过硬件在环架构搜索，结合门控短卷积和分组查询注意力，采用蒸馏、课程学习和三阶段后训练。
3. 实验或效果：模型参数350M-8.3B，在IFEval和GSM8K等基准上表现强劲，支持多模态和检索变体。

## 📄 摘要（原文）

> We present LFM2, a family of Liquid Foundation Models designed for efficient on-device deployment and strong task capabilities. Using hardware-in-the-loop architecture search under edge latency and memory constraints, we obtain a compact hybrid backbone that combines gated short convolutions with a small number of grouped query attention blocks, delivering up to 2x faster prefill and decode on CPUs compared to similarly sized models. The LFM2 family covers 350M-8.3B parameters, including dense models (350M, 700M, 1.2B, 2.6B) and a mixture-of-experts variant (8.3B total, 1.5B active), all with 32K context length. LFM2's training pipeline includes a tempered, decoupled Top-K knowledge distillation objective that avoids support mismatch; curriculum learning with difficulty-ordered data; and a three-stage post-training recipe of supervised fine-tuning, length-normalized preference optimization, and model merging. Pre-trained on 10-12T tokens, LFM2 models achieve strong results across diverse benchmarks; for example, LFM2-2.6B reaches 79.56% on IFEval and 82.41% on GSM8K. We further build multimodal and retrieval variants: LFM2-VL for vision-language tasks, LFM2-Audio for speech, and LFM2-ColBERT for retrieval. LFM2-VL supports tunable accuracy-latency tradeoffs via token-efficient visual processing, while LFM2-Audio separates audio input and output pathways to enable real-time speech-to-speech interaction competitive with models 3x larger. LFM2-ColBERT provides a low-latency encoder for queries and documents, enabling high-performance retrieval across multiple languages. All models are released with open weights and deployment packages for ExecuTorch, llama.cpp, and vLLM, making LFM2 a practical base for edge applications that need fast, memory-efficient inference and strong task capabilities.


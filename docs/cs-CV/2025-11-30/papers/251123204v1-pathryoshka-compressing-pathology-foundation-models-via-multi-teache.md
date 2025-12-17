---
layout: default
title: Pathryoshka: Compressing Pathology Foundation Models via Multi-Teacher Knowledge Distillation with Nested Embeddings
---

# Pathryoshka: Compressing Pathology Foundation Models via Multi-Teacher Knowledge Distillation with Nested Embeddings

**arXiv**: [2511.23204v1](https://arxiv.org/abs/2511.23204) | [PDF](https://arxiv.org/pdf/2511.23204.pdf)

**作者**: Christian Grashei, Christian Brechenmacher, Rao Muhammad Umer, Jingsong Liu, Carsten Marr, Ewa Szczurek, Peter J. Schüffler

---

## 💡 一句话要点

**提出Pathryoshka多教师蒸馏框架，以压缩病理学基础模型并支持自适应嵌入维度。**

**关键词**: `病理学基础模型` `知识蒸馏` `模型压缩` `自适应嵌入` `多教师学习` `计算病理学`

## 📋 核心要点

1. 病理学基础模型参数多、嵌入维度高，限制资源紧张下的应用。
2. 结合RADIO蒸馏和Matryoshka表示学习，通过多教师蒸馏压缩模型。
3. 在十个基准测试中，模型大小减少86-92%，性能持平，优于同类单教师模型。

## 📄 摘要（原文）

> Pathology foundation models (FMs) have driven significant progress in computational pathology. However, these high-performing models can easily exceed a billion parameters and produce high-dimensional embeddings, thus limiting their applicability for research or clinical use when computing resources are tight. Here, we introduce Pathryoshka, a multi-teacher distillation framework inspired by RADIO distillation and Matryoshka Representation Learning to reduce pathology FM sizes while allowing for adaptable embedding dimensions. We evaluate our framework with a distilled model on ten public pathology benchmarks with varying downstream tasks. Compared to its much larger teachers, Pathryoshka reduces the model size by 86-92% at on-par performance. It outperforms state-of-the-art single-teacher distillation models of comparable size by a median margin of 7.0 in accuracy. By enabling efficient local deployment without sacrificing accuracy or representational richness, Pathryoshka democratizes access to state-of-the-art pathology FMs for the broader research and clinical community.


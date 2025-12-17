---
layout: default
title: VL-JEPA: Joint Embedding Predictive Architecture for Vision-language
---

# VL-JEPA: Joint Embedding Predictive Architecture for Vision-language

**arXiv**: [2512.10942v1](https://arxiv.org/abs/2512.10942) | [PDF](https://arxiv.org/pdf/2512.10942.pdf)

**作者**: Delong Chen, Mustafa Shukor, Theo Moutakanni, Willy Chung, Jade Yu, Tejaswi Kasarla, Allen Bolourchi, Yann LeCun, Pascale Fung

---

## 💡 一句话要点

**提出VL-JEPA，基于联合嵌入预测架构，在视觉语言任务中预测连续嵌入以提升性能并减少参数。**

**关键词**: `视觉语言模型` `联合嵌入预测` `连续嵌入预测` `选择性解码` `多任务支持`

## 📋 核心要点

1. 核心问题：传统视觉语言模型在token空间自回归生成，可能忽略语义抽象和效率优化。
2. 方法要点：采用联合嵌入预测架构，在抽象表示空间预测目标文本嵌入，减少表面语言变异性影响。
3. 实验或效果：在相同视觉编码器和训练数据下，比标准模型性能更强，参数减少50%，支持选择性解码和多种任务。

## 📄 摘要（原文）

> We introduce VL-JEPA, a vision-language model built on a Joint Embedding Predictive Architecture (JEPA). Instead of autoregressively generating tokens as in classical VLMs, VL-JEPA predicts continuous embeddings of the target texts. By learning in an abstract representation space, the model focuses on task-relevant semantics while abstracting away surface-level linguistic variability. In a strictly controlled comparison against standard token-space VLM training with the same vision encoder and training data, VL-JEPA achieves stronger performance while having 50% fewer trainable parameters. At inference time, a lightweight text decoder is invoked only when needed to translate VL-JEPA predicted embeddings into text. We show that VL-JEPA natively supports selective decoding that reduces the number of decoding operations by 2.85x while maintaining similar performance compared to non-adaptive uniform decoding. Beyond generation, the VL-JEPA's embedding space naturally supports open-vocabulary classification, text-to-video retrieval, and discriminative VQA without any architecture modification. On eight video classification and eight video retrieval datasets, the average performance VL-JEPA surpasses that of CLIP, SigLIP2, and Perception Encoder. At the same time, the model achieves comparable performance as classical VLMs (InstructBLIP, QwenVL) on four VQA datasets: GQA, TallyQA, POPE and POPEv2, despite only having 1.6B parameters.


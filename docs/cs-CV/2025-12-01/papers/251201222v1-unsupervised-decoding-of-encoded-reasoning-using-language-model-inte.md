---
layout: default
title: Unsupervised decoding of encoded reasoning using language model interpretability
---

# Unsupervised decoding of encoded reasoning using language model interpretability

**arXiv**: [2512.01222v1](https://arxiv.org/abs/2512.01222) | [PDF](https://arxiv.org/pdf/2512.01222.pdf)

**作者**: Ching Fang, Samuel Marks

---

## 💡 一句话要点

**提出基于logit lens的无监督解码方法，以评估机制可解释性技术对编码推理的解析能力。**

**关键词**: `机制可解释性` `编码推理解码` `logit lens分析` `无监督解码` `语言模型评估` `ROT-13加密`

## 📋 核心要点

1. 核心问题：大型语言模型的推理过程可能被编码隐藏，需评估现有可解释性技术能否解析此类编码推理。
2. 方法要点：通过微调模型在ROT-13加密下进行链式推理，并利用logit lens分析内部激活来解码推理过程。
3. 实验或效果：logit lens在中间至深层有效解码，结合自动释义实现高精度重建推理文本，表明技术对简单编码推理具有鲁棒性。

## 📄 摘要（原文）

> As large language models become increasingly capable, there is growing concern that they may develop reasoning processes that are encoded or hidden from human oversight. To investigate whether current interpretability techniques can penetrate such encoded reasoning, we construct a controlled testbed by fine-tuning a reasoning model (DeepSeek-R1-Distill-Llama-70B) to perform chain-of-thought reasoning in ROT-13 encryption while maintaining intelligible English outputs. We evaluate mechanistic interpretability methods--in particular, logit lens analysis--on their ability to decode the model's hidden reasoning process using only internal activations. We show that logit lens can effectively translate encoded reasoning, with accuracy peaking in intermediate-to-late layers. Finally, we develop a fully unsupervised decoding pipeline that combines logit lens with automated paraphrasing, achieving substantial accuracy in reconstructing complete reasoning transcripts from internal model representations. These findings suggest that current mechanistic interpretability techniques may be more robust to simple forms of encoded reasoning than previously understood. Our work provides an initial framework for evaluating interpretability methods against models that reason in non-human-readable formats, contributing to the broader challenge of maintaining oversight over increasingly capable AI systems.


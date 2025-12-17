---
layout: default
title: Zero-Shot Textual Explanations via Translating Decision-Critical Features
---

# Zero-Shot Textual Explanations via Translating Decision-Critical Features

**arXiv**: [2512.07245v1](https://arxiv.org/abs/2512.07245) | [PDF](https://arxiv.org/pdf/2512.07245.pdf)

**作者**: Toshinori Yamauchi, Hiroshi Kera, Kazuhiko Kawamoto

---

## 💡 一句话要点

**提出TEXTER方法，通过分离决策关键特征实现零样本文本解释，提升图像分类器透明度。**

**关键词**: `零样本文本解释` `决策关键特征` `图像分类器透明度` `CLIP特征映射` `稀疏自编码器`

## 📋 核心要点

1. 现有零样本方法生成描述可见内容而非预测驱动因素，导致解释不忠实。
2. TEXTER识别预测贡献神经元，强调决策关键特征，映射到CLIP空间检索文本解释。
3. 实验表明TEXTER比现有方法生成更忠实和可解释的文本解释，代码将公开。

## 📄 摘要（原文）

> Textual explanations make image classifier decisions transparent by describing the prediction rationale in natural language. Large vision-language models can generate captions but are designed for general visual understanding, not classifier-specific reasoning. Existing zero-shot explanation methods align global image features with language, producing descriptions of what is visible rather than what drives the prediction. We propose TEXTER, which overcomes this limitation by isolating decision-critical features before alignment. TEXTER identifies the neurons contributing to the prediction and emphasizes the features encoded in those neurons -- i.e., the decision-critical features. It then maps these emphasized features into the CLIP feature space to retrieve textual explanations that reflect the model's reasoning. A sparse autoencoder further improves interpretability, particularly for Transformer architectures. Extensive experiments show that TEXTER generates more faithful and interpretable explanations than existing methods. The code will be publicly released.


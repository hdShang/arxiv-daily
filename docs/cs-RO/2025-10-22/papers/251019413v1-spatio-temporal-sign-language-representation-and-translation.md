---
layout: default
title: Spatio-temporal Sign Language Representation and Translation
---

# Spatio-temporal Sign Language Representation and Translation

**arXiv**: [2510.19413v1](https://arxiv.org/abs/2510.19413) | [PDF](https://arxiv.org/pdf/2510.19413.pdf)

**作者**: Yasser Hamidullah, Josef van Genabith, Cristina España-Bonet

---

## 💡 一句话要点

**提出端到端时空特征学习模型以改进手语翻译性能**

**关键词**: `手语翻译` `时空特征学习` `端到端架构` `视频特征提取` `BLEU评估`

## 📋 核心要点

1. 标准手语翻译方法常忽略视频的时序特征，影响翻译准确性。
2. 采用单一模型学习时空特征表示和翻译，实现端到端架构。
3. 在开发集BLEU达5±1，测试集性能下降至0.11±0.06。

## 📄 摘要（原文）

> This paper describes the DFKI-MLT submission to the WMT-SLT 2022 sign
> language translation (SLT) task from Swiss German Sign Language (video) into
> German (text). State-of-the-art techniques for SLT use a generic seq2seq
> architecture with customized input embeddings. Instead of word embeddings as
> used in textual machine translation, SLT systems use features extracted from
> video frames. Standard approaches often do not benefit from temporal features.
> In our participation, we present a system that learns spatio-temporal feature
> representations and translation in a single model, resulting in a real
> end-to-end architecture expected to better generalize to new data sets. Our
> best system achieved $5\pm1$ BLEU points on the development set, but the
> performance on the test dropped to $0.11\pm0.06$ BLEU points.


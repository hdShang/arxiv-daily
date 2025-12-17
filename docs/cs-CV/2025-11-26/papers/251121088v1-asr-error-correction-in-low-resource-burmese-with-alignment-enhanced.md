---
layout: default
title: ASR Error Correction in Low-Resource Burmese with Alignment-Enhanced Transformers using Phonetic Features
---

# ASR Error Correction in Low-Resource Burmese with Alignment-Enhanced Transformers using Phonetic Features

**arXiv**: [2511.21088v1](https://arxiv.org/abs/2511.21088) | [PDF](https://arxiv.org/pdf/2511.21088.pdf)

**作者**: Ye Bhone Lin, Thura Aung, Ye Kyaw Thu, Thazin Myint Oo

---

## 💡 一句话要点

**提出结合IPA与对齐特征的Transformer模型，以提升低资源缅甸语ASR错误纠正性能**

**关键词**: `自动语音识别错误纠正` `低资源语言处理` `Transformer模型` `IPA特征` `对齐增强` `缅甸语ASR`

## 📋 核心要点

1. 核心问题：低资源缅甸语自动语音识别错误纠正，缺乏专门研究
2. 方法要点：使用序列到序列Transformer，集成IPA音标和对齐信息特征
3. 实验或效果：平均WER从51.56降至39.82，chrF++分数从0.5864提升至0.627

## 📄 摘要（原文）

> This paper investigates sequence-to-sequence Transformer models for automatic speech recognition (ASR) error correction in low-resource Burmese, focusing on different feature integration strategies including IPA and alignment information. To our knowledge, this is the first study addressing ASR error correction specifically for Burmese. We evaluate five ASR backbones and show that our ASR Error Correction (AEC) approaches consistently improve word- and character-level accuracy over baseline outputs. The proposed AEC model, combining IPA and alignment features, reduced the average WER of ASR models from 51.56 to 39.82 before augmentation (and 51.56 to 43.59 after augmentation) and improving chrF++ scores from 0.5864 to 0.627, demonstrating consistent gains over the baseline ASR outputs without AEC. Our results highlight the robustness of AEC and the importance of feature design for improving ASR outputs in low-resource settings.


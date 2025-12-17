---
layout: default
title: It Hears, It Sees too: Multi-Modal LLM for Depression Detection By Integrating Visual Understanding into Audio Language Models
---

# It Hears, It Sees too: Multi-Modal LLM for Depression Detection By Integrating Visual Understanding into Audio Language Models

**arXiv**: [2511.19877v1](https://arxiv.org/abs/2511.19877) | [PDF](https://arxiv.org/pdf/2511.19877.pdf)

**作者**: Xiangyu Zhao, Yaling Shen, Yiwen Jiang, Zimu Wang, Jiahe Liu, Maxmartwell H Cheng, Guilherme C Oliveira, Robert Desimone, Dominic Dwyer, Zongyuan Ge

---

## 💡 一句话要点

**提出多模态LLM框架，通过音视频特征对齐改进抑郁症检测**

**关键词**: `多模态大语言模型` `抑郁症检测` `音视频特征对齐` `心理健康评估` `时间戳级建模`

## 📋 核心要点

1. 核心问题：传统LLM无法处理音频和视觉中的非语言线索，限制心理健康评估。
2. 方法要点：增强音频语言模型，集成视觉理解，实现时间戳级音视频特征对齐。
3. 实验或效果：在DAIC-WoZ数据集上优于单模态和先前多模态方法。

## 📄 摘要（原文）

> Depression is one of the most prevalent mental health disorders globally. In recent years, multi-modal data, such as speech, video, and transcripts, has been increasingly used to develop AI-assisted depression assessment systems. Large language models have further advanced this field due to their strong language understanding and generalization capabilities. However, conventional LLMs remain text-centric and cannot process the rich non-verbal cues found in audio and visual modalities, which are critical components in mental health evaluation. While multi-modal LLMs offer a promising direction, few are tailored for psychological applications. In this study, we propose a novel multi-modal LLM framework for depression detection. Our approach augments an audio language model with visual understanding and aligns audio-visual features at the timestamp level. This fine-grained alignment improves modeling of temporal dynamics across modalities while reducing the need for extensive training data and computational resources. Experiments on the DAIC-WoZ dataset demonstrate that our model outperforms both single-modality approaches and previous multi-modal methods. Moreover, the proposed framework can be extended to incorporate additional physiological signals, paving the way for broader clinical applications beyond mental health.


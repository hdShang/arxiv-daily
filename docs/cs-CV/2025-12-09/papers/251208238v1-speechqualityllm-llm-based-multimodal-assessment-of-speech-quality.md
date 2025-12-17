---
layout: default
title: SpeechQualityLLM: LLM-Based Multimodal Assessment of Speech Quality
---

# SpeechQualityLLM: LLM-Based Multimodal Assessment of Speech Quality

**arXiv**: [2512.08238v1](https://arxiv.org/abs/2512.08238) | [PDF](https://arxiv.org/pdf/2512.08238.pdf)

**作者**: Mahathir Monjur, Shahriar Nirjon

---

## 💡 一句话要点

**提出SpeechQualityLLM，基于LLM的多模态语音质量评估系统，支持自然语言查询以优化语音通信质量监控。**

**关键词**: `语音质量评估` `多模态学习` `语言模型` `自然语言接口` `主观评分预测`

## 📋 核心要点

1. 核心问题：传统语音质量评估方法如PESQ和POLQA依赖受控条件和高成本主观测试，而学习模型如NISQA缺乏交互性和文本解释能力。
2. 方法要点：结合音频编码器和语言模型，在NISQA语料上训练，通过模板问答对覆盖MOS和四个感知维度，支持单端和双端设置。
3. 实验或效果：在NISQA测试集上，双端模型MOS平均绝对误差为0.41，皮尔逊相关系数0.86，并提供灵活的自然语言接口以模拟不同听众和生成多样化判断。

## 📄 摘要（原文）

> Objective speech quality assessment is central to telephony, VoIP, and streaming systems, where large volumes of degraded audio must be monitored and optimized at scale. Classical metrics such as PESQ and POLQA approximate human mean opinion scores (MOS) but require carefully controlled conditions and expensive listening tests, while learning-based models such as NISQA regress MOS and multiple perceptual dimensions from waveforms or spectrograms, achieving high correlation with subjective ratings yet remaining rigid: they do not support interactive, natural-language queries and do not natively provide textual rationales. In this work, we introduce SpeechQualityLLM, a multimodal speech quality question-answering (QA) system that couples an audio encoder with a language model and is trained on the NISQA corpus using template-based question-answer pairs covering overall MOS and four perceptual dimensions (noisiness, coloration, discontinuity, and loudness) in both single-ended (degraded only) and double-ended (degraded plus clean reference) setups. Instead of directly regressing scores, our system is supervised to generate textual answers from which numeric predictions are parsed and evaluated with standard regression and ranking metrics; on held-out NISQA clips, the double-ended model attains a MOS mean absolute error (MAE) of 0.41 with Pearson correlation of 0.86, with competitive performance on dimension-wise tasks. Beyond these quantitative gains, it offers a flexible natural-language interface in which the language model acts as an audio quality expert: practitioners can query arbitrary aspects of degradations, prompt the model to emulate different listener profiles to capture human variability and produce diverse but plausible judgments rather than a single deterministic score, and thereby reduce reliance on large-scale crowdsourced tests and their monetary cost.


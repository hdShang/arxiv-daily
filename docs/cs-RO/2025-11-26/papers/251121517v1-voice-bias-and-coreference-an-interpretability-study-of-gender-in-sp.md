---
layout: default
title: Voice, Bias, and Coreference: An Interpretability Study of Gender in Speech Translation
---

# Voice, Bias, and Coreference: An Interpretability Study of Gender in Speech Translation

**arXiv**: [2511.21517v1](https://arxiv.org/abs/2511.21517) | [PDF](https://arxiv.org/pdf/2511.21517.pdf)

**作者**: Lina Conti, Dennis Fucci, Marco Gaido, Matteo Negri, Guillaume Wisniewski, Luisa Bentivogli

---

## 💡 一句话要点

**揭示语音翻译中基于声学与代词机制解决性别偏见问题**

**关键词**: `语音翻译` `性别偏见` `声学特征` `代词机制` `模型可解释性`

## 📋 核心要点

1. 核心问题：语音翻译中声学线索可能导致性别误判，尤其在语法性别语言中。
2. 方法要点：分析训练数据、内部语言模型偏见和声学信息交互机制。
3. 实验或效果：发现模型利用第一人称代词链接性别信息，提高准确性。

## 📄 摘要（原文）

> Unlike text, speech conveys information about the speaker, such as gender, through acoustic cues like pitch. This gives rise to modality-specific bias concerns. For example, in speech translation (ST), when translating from languages with notional gender, such as English, into languages where gender-ambiguous terms referring to the speaker are assigned grammatical gender, the speaker's vocal characteristics may play a role in gender assignment. This risks misgendering speakers, whether through masculine defaults or vocal-based assumptions. Yet, how ST models make these decisions remains poorly understood. We investigate the mechanisms ST models use to assign gender to speaker-referring terms across three language pairs (en-es/fr/it), examining how training data patterns, internal language model (ILM) biases, and acoustic information interact. We find that models do not simply replicate term-specific gender associations from training data, but learn broader patterns of masculine prevalence. While the ILM exhibits strong masculine bias, models can override these preferences based on acoustic input. Using contrastive feature attribution on spectrograms, we reveal that the model with higher gender accuracy relies on a previously unknown mechanism: using first-person pronouns to link gendered terms back to the speaker, accessing gender information distributed across the frequency spectrum rather than concentrated in pitch.


---
layout: default
title: SurgAnt-ViVQA: Learning to Anticipate Surgical Events through GRU-Driven Temporal Cross-Attention
---

# SurgAnt-ViVQA: Learning to Anticipate Surgical Events through GRU-Driven Temporal Cross-Attention

**arXiv**: [2511.03178v1](https://arxiv.org/abs/2511.03178) | [PDF](https://arxiv.org/pdf/2511.03178.pdf)

**作者**: Shreyas C. Dhake, Jiayuan Huang, Runlong He, Danyal Z. Khan, Evangelos B. Mazomenos, Sophia Bano, Hani J. Marcus, Danail Stoyanov, Matthew J. Clarkson, Mobarak I. Hoque

---

## 💡 一句话要点

**提出SurgAnt-ViVQA模型，通过GRU驱动的时间交叉注意力预测手术事件，以支持内窥镜手术实时辅助。**

**关键词**: `手术视觉问答` `时间建模` `门控交叉注意力` `GRU编码` `参数高效微调` `前瞻预测`

## 📋 核心要点

1. 核心问题：现有视觉问答系统在手术中仅关注当前场景，无法预测未来事件，如手术阶段或器械需求。
2. 方法要点：使用双向GRU编码视频动态，并通过门控交叉注意力将视觉上下文注入语言模型，实现参数高效微调。
3. 实验或效果：在PitVQA-Anticipation和EndoVis数据集上超越基线，时间建模和门控融合显著提升性能。

## 📄 摘要（原文）

> Anticipating forthcoming surgical events is vital for real-time assistance in
> endonasal transsphenoidal pituitary surgery, where visibility is limited and
> workflow changes rapidly. Most visual question answering (VQA) systems reason
> on isolated frames with static vision language alignment, providing little
> support for forecasting next steps or instrument needs. Existing surgical VQA
> datasets likewise center on the current scene rather than the near future. We
> introduce PitVQA-Anticipation, the first VQA dataset designed for forward
> looking surgical reasoning. It comprises 33.5 hours of operative video and
> 734,769 question answer pairs built from temporally grouped clips and expert
> annotations across four tasks: predicting the future phase, next step, upcoming
> instrument, and remaining duration. We further propose SurgAnt-ViVQA, a video
> language model that adapts a large language model using a GRU Gated Temporal
> Cross-Attention module. A bidirectional GRU encodes frame to frame dynamics,
> while an adaptive gate injects visual context into the language stream at the
> token level. Parameter efficient fine tuning customizes the language backbone
> to the surgical domain. SurgAnt-ViVQA tested upon on PitVQA-Anticipation and
> EndoVis datasets, surpassing strong image and video based baselines. Ablations
> show that temporal recurrence and gated fusion drive most of the gains. A frame
> budget study indicates a trade-off: 8 frames maximize fluency, whereas 32
> frames slightly reduce BLEU but improve numeric time estimation. By pairing a
> temporally aware encoder with fine grained gated cross-attention, SurgAnt-ViVQA
> advances surgical VQA from retrospective description to proactive anticipation.
> PitVQA-Anticipation offers a comprehensive benchmark for this setting and
> highlights the importance of targeted temporal modeling for reliable, future
> aware surgical assistance.


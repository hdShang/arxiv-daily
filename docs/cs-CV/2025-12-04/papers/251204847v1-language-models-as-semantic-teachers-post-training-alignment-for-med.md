---
layout: default
title: Language Models as Semantic Teachers: Post-Training Alignment for Medical Audio Understanding
---

# Language Models as Semantic Teachers: Post-Training Alignment for Medical Audio Understanding

**arXiv**: [2512.04847v1](https://arxiv.org/abs/2512.04847) | [PDF](https://arxiv.org/pdf/2512.04847.pdf)

**作者**: Tsai-Ning Wang, Lin-Lin Chen, Neil Zeghidour, Aaqib Saeed

---

## 💡 一句话要点

**提出AcuLa框架，通过音频-语言对齐增强医学音频模型的临床语义理解能力。**

**关键词**: `医学音频理解` `音频-语言对齐` `后训练框架` `语义教师` `临床报告生成` `对比学习`

## 📋 核心要点

1. 预训练音频模型能检测听诊声音的声学模式，但缺乏临床意义理解，限制诊断应用。
2. AcuLa利用医学语言模型作为语义教师，通过表示级对比和自监督学习对齐音频编码器。
3. 在18个心肺任务上实现SOTA，平均AUROC从0.68提升至0.79，COVID-19咳嗽检测AUROC从0.55提升至0.89。

## 📄 摘要（原文）

> Pre-trained audio models excel at detecting acoustic patterns in auscultation sounds but often fail to grasp their clinical significance, limiting their use and performance in diagnostic tasks. To bridge this gap, we introduce AcuLa (Audio-Clinical Understanding via Language Alignment), a lightweight post-training framework that instills semantic understanding into any audio encoder by aligning it with a medical language model, which acts as a "semantic teacher." To enable alignment at scale, we construct a large-scale dataset by leveraging off-the-shelf large language models to translate the rich, structured metadata accompanying existing audio recordings into coherent clinical reports. Our alignment strategy combines a representation-level contrastive objective with a self-supervised modeling, ensuring that the model learns clinical semantics while preserving fine-grained temporal cues. AcuLa achieves state-of-the-art results across 18 diverse cardio-respiratory tasks from 10 different datasets, improving the mean AUROC on classification benchmarks from 0.68 to 0.79 and, on the most challenging COVID-19 cough detection task, boosting the AUROC from 0.55 to 0.89. Our work demonstrates that this audio-language alignment transforms purely acoustic models into clinically-aware diagnostic tools, establishing a novel paradigm for enhancing physiological understanding in audio-based health monitoring.


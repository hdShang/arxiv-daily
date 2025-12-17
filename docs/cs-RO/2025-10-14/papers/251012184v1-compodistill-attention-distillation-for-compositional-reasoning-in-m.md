---
layout: default
title: CompoDistill: Attention Distillation for Compositional Reasoning in Multimodal LLMs
---

# CompoDistill: Attention Distillation for Compositional Reasoning in Multimodal LLMs

**arXiv**: [2510.12184v1](https://arxiv.org/abs/2510.12184) | [PDF](https://arxiv.org/pdf/2510.12184.pdf)

**作者**: Jiwan Kim, Kibum Kim, Sangwoo Seo, Chanyoung Park

---

## 💡 一句话要点

**提出CompoDistill框架，通过注意力对齐解决多模态大模型中视觉感知蒸馏问题**

**关键词**: `多模态大模型` `知识蒸馏` `视觉注意力对齐` `组合推理` `视觉感知` `模型压缩`

## 📋 核心要点

1. 现有知识蒸馏方法在多模态大模型中难以有效传递教师模型的视觉感知能力
2. 通过视觉注意力对齐机制，显式优化学生模型的视觉注意力分布
3. 实验显示在组合推理任务中性能显著提升，并保持视觉问答任务表现

## 📄 摘要（原文）

> Recently, efficient Multimodal Large Language Models (MLLMs) have gained
> significant attention as a solution to their high computational complexity,
> making them more practical for real-world applications. In this regard, the
> knowledge distillation (KD) approach has emerged as a promising alternative,
> which transfers the rich visual and linguistic knowledge from a larger model
> (teacher) to a smaller model (student). However, we observe that existing KD
> methods struggle to effectively distill the teacher MLLM's rich visual
> perception abilities to the student, a challenge that has been largely
> overlooked in previous studies. Through a systematic analysis, we identify
> visual attention misalignment between student and teacher as the main cause of
> this issue. Based on this insight, we propose CompoDistill, a novel KD
> framework that explicitly aligns the student's visual attention with that of
> the teacher to enhance the student's visual perception abilities. Our extensive
> experiments show that CompoDistill significantly improves performance on
> compositional reasoning tasks that require visual perception abilities while
> maintaining strong performance on visual question answering tasks, as done in
> existing studies. Furthermore, CompoDistill demonstrates effectiveness with a
> more advanced backbone, highlighting its generalizability.


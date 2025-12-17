---
layout: default
title: Stable Signer: Hierarchical Sign Language Generative Model
---

# Stable Signer: Hierarchical Sign Language Generative Model

**arXiv**: [2512.04048v1](https://arxiv.org/abs/2512.04048) | [PDF](https://arxiv.org/pdf/2512.04048.pdf)

**作者**: Sen Fang, Yalin Feng, Hongbin Zhong, Yanxin Zhang, Dimitris N. Metaxas

---

## 💡 一句话要点

**提出Stable Signer模型，通过简化任务结构和引入新模块，端到端生成高质量多风格手语视频。**

**关键词**: `手语生成` `端到端模型` `分层生成` `手势渲染` `语义感知损失`

## 📋 核心要点

1. 核心问题：传统手语生成流程冗余，导致文本转换、姿态生成和视频渲染误差累积，进展缓慢。
2. 方法要点：将任务重新定义为分层生成，仅包括文本理解和Pose2Vid，使用SLUL进行文本理解，SLP-MoE块渲染手势。
3. 实验或效果：性能相比当前SOTA方法提升48.6%，通过SAGM损失训练SLUL，生成高质量多风格视频。

## 📄 摘要（原文）

> Sign Language Production (SLP) is the process of converting the complex input text into a real video. Most previous works focused on the Text2Gloss, Gloss2Pose, Pose2Vid stages, and some concentrated on Prompt2Gloss and Text2Avatar stages. However, this field has made slow progress due to the inaccuracy of text conversion, pose generation, and the rendering of poses into real human videos in these stages, resulting in gradually accumulating errors. Therefore, in this paper, we streamline the traditional redundant structure, simplify and optimize the task objective, and design a new sign language generative model called Stable Signer. It redefines the SLP task as a hierarchical generation end-to-end task that only includes text understanding (Prompt2Gloss, Text2Gloss) and Pose2Vid, and executes text understanding through our proposed new Sign Language Understanding Linker called SLUL, and generates hand gestures through the named SLP-MoE hand gesture rendering expert block to end-to-end generate high-quality and multi-style sign language videos. SLUL is trained using the newly developed Semantic-Aware Gloss Masking Loss (SAGM Loss). Its performance has improved by 48.6% compared to the current SOTA generation methods.


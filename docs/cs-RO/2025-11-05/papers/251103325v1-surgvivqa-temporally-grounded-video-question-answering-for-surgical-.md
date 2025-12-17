---
layout: default
title: SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding
---

# SurgViVQA: Temporally-Grounded Video Question Answering for Surgical Scene Understanding

**arXiv**: [2511.03325v1](https://arxiv.org/abs/2511.03325) | [PDF](https://arxiv.org/pdf/2511.03325.pdf)

**作者**: Mauro Orazio Drago, Luca Carlini, Pelinsu Celebi Balyemez, Dennis Pierantozzi, Chiara Lena, Cesare Hassan, Danail Stoyanov, Elena De Momi, Sophia Bano, Mobarak I. Hoque

---

## 💡 一句话要点

**提出SurgViVQA模型以解决手术视频问答中的动态场景理解问题**

**关键词**: `手术视频问答` `时间基础理解` `掩码视频编码` `大语言模型` `动态场景分析` `数据集构建`

## 📋 核心要点

1. 核心问题：现有手术VideoQA方法依赖静态图像特征，忽略动态事件，导致理解不准确。
2. 方法要点：使用掩码视频-文本编码器融合视频与问题特征，结合LLM解码，捕捉运动与工具-组织交互。
3. 实验或效果：在REAL-Colon-VQA和EndoVis18-VQA数据集上，关键词准确率分别提升11%和9%。

## 📄 摘要（原文）

> Video Question Answering (VideoQA) in the surgical domain aims to enhance
> intraoperative understanding by enabling AI models to reason over temporally
> coherent events rather than isolated frames. Current approaches are limited to
> static image features, and available datasets often lack temporal annotations,
> ignoring the dynamics critical for accurate procedural interpretation. We
> propose SurgViVQA, a surgical VideoQA model that extends visual reasoning from
> static images to dynamic surgical scenes. It uses a Masked Video--Text Encoder
> to fuse video and question features, capturing temporal cues such as motion and
> tool--tissue interactions, which a fine-tuned large language model (LLM) then
> decodes into coherent answers. To evaluate its performance, we curated
> REAL-Colon-VQA, a colonoscopic video dataset that includes motion-related
> questions and diagnostic attributes, as well as out-of-template questions with
> rephrased or semantically altered formulations to assess model robustness.
> Experimental validation on REAL-Colon-VQA and the public EndoVis18-VQA dataset
> shows that SurgViVQA outperforms existing image-based VQA benchmark models,
> particularly in keyword accuracy, improving over PitVQA by +11\% on
> REAL-Colon-VQA and +9\% on EndoVis18-VQA. A perturbation study on the questions
> further confirms improved generalizability and robustness to variations in
> question phrasing. SurgViVQA and the REAL-Colon-VQA dataset provide a framework
> for temporally-aware understanding in surgical VideoQA, enabling AI models to
> interpret dynamic procedural contexts more effectively. Code and dataset
> available at https://github.com/madratak/SurgViVQA.


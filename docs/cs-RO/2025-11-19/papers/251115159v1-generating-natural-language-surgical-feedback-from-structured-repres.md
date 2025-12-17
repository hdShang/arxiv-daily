---
layout: default
title: Generating Natural-Language Surgical Feedback: From Structured Representation to Domain-Grounded Evaluation
---

# Generating Natural-Language Surgical Feedback: From Structured Representation to Domain-Grounded Evaluation

**arXiv**: [2511.15159v1](https://arxiv.org/abs/2511.15159) | [PDF](https://arxiv.org/pdf/2511.15159.pdf)

**作者**: Firdavs Nasriddinov, Rafal Kocielnik, Anima Anandkumar, Andrew J. Hung

---

## 💡 一句话要点

**提出基于结构化手术动作三元组的反馈生成方法，以提升手术训练中的自动化指导质量。**

**关键词**: `手术反馈生成` `结构化表示学习` `视频动作识别` `自然语言生成` `临床评估`

## 📋 核心要点

1. 核心问题：自动化生成自然语言手术反馈需理解临床相关表示，以提供及时一致的指导。
2. 方法要点：从真实反馈文本挖掘器械-动作-目标三元组，并用于条件化GPT-4o生成反馈。
3. 实验效果：三元组条件化使反馈生成保真度提升12.4%，可接受生成比例从21%增至42%。

## 📄 摘要（原文）

> High-quality intraoperative feedback from a surgical trainer is pivotal for improving trainee performance and long-term skill acquisition. Automating natural, trainer-style feedback promises timely, accessible, and consistent guidance at scale but requires models that understand clinically relevant representations. We present a structure-aware pipeline that learns a surgical action ontology from real trainer-to-trainee transcripts (33 surgeries) and uses it to condition feedback generation. We contribute by (1) mining Instrument-Action-Target (IAT) triplets from real-world feedback text and clustering surface forms into normalized categories, (2) fine-tuning a video-to-IAT model that leverages the surgical procedure and task contexts as well as fine-grained temporal instrument motion, and (3) demonstrating how to effectively use IAT triplet representations to guide GPT-4o in generating clinically grounded, trainer-style feedback. We show that, on Task 1: Video-to-IAT recognition, our context injection and temporal tracking deliver consistent AUC gains (Instrument: 0.67 to 0.74; Action: 0.60 to 0.63; Tissue: 0.74 to 0.79). For Task 2: feedback text generation (rated on a 1-5 fidelity rubric where 1 = opposite/unsafe, 3 = admissible, and 5 = perfect match to a human trainer), GPT-4o from video alone scores 2.17, while IAT conditioning reaches 2.44 (+12.4%), doubling the share of admissible generations with score >= 3 from 21% to 42%. Traditional text-similarity metrics also improve: word error rate decreases by 15-31% and ROUGE (phrase/substring overlap) increases by 9-64%. Grounding generation in explicit IAT structure improves fidelity and yields clinician-verifiable rationales, supporting auditable use in surgical training.


---
layout: default
title: Knowledge Graph Augmented Large Language Models for Next-Visit Disease Prediction
---

# Knowledge Graph Augmented Large Language Models for Next-Visit Disease Prediction

**arXiv**: [2512.01210v1](https://arxiv.org/abs/2512.01210) | [PDF](https://arxiv.org/pdf/2512.01210.pdf)

**作者**: Ruiyu Wang, Tuan Vinh, Ran Xu, Yuyin Zhou, Jiaying Lu, Carl Yang, Francisco Pasquel

---

## 💡 一句话要点

**提出知识图谱引导的思维链框架，用于电子健康记录中的下次就诊疾病预测。**

**关键词**: `知识图谱增强` `思维链推理` `疾病预测` `电子健康记录` `临床解释`

## 📋 核心要点

1. 现有电子健康记录预测方法解释粗糙，缺乏患者级决策价值。
2. 方法将ICD-9代码映射到PrimeKG，提取疾病相关节点和多跳推理路径作为思维链骨架。
3. 在MIMIC-III和CRADLE数据集上，模型性能超越基线，临床评估偏好其解释。

## 📄 摘要（原文）

> Electronic health records (EHRs) support powerful clinical prediction models, but existing methods typically provide coarse, post hoc explanations that offer limited value for patient-level decision making. We introduce a knowledge graph (KG)-guided chain-of-thought (CoT) framework that generates clinically grounded and temporally consistent reasoning for visit-level disease prediction in MIMIC-III. ICD-9 codes are mapped to PrimeKG, from which disease-relevant nodes and multi-hop reasoning paths are extracted and used as scaffolds for CoT generation; only explanations whose conclusions match observed outcomes are retained. Lightweight LLaMA-3.1-Instruct-8B and Gemma-7B models are then fine-tuned on this supervision corpus. Across ten PrimeKG-mapped diseases and limited training cohorts (400 and 1000 cases), KG-guided models outperform strong classical baselines, achieving AUROC values of 0.66 to 0.70 and macro-AUPR values of 0.40 to 0.47. The models also transfer zero-shot to the CRADLE cohort, improving accuracy from approximately 0.40 to 0.51 up to 0.72 to 0.77. A blinded clinician evaluation shows consistent preference for KG-guided CoT explanations in clarity, relevance, and clinical correctness.


---
layout: default
title: A Scientific Reasoning Model for Organic Synthesis Procedure Generation
---

# A Scientific Reasoning Model for Organic Synthesis Procedure Generation

**arXiv**: [2512.13668v1](https://arxiv.org/abs/2512.13668) | [PDF](https://arxiv.org/pdf/2512.13668.pdf)

**作者**: Guoqing Liu, Junren Li, Zihan Zhao, Eray Inanc, Krzysztof Maziarz, Jose Garrido Torres, Victor Garcia Satorras, Shoko Ueda, Christopher M. Bishop, Marwin Segler

---

## 💡 一句话要点

**提出QFANG科学推理语言模型，以生成有机合成实验程序，解决计算路线设计与实验室执行间的差距。**

**关键词**: `有机合成规划` `科学推理语言模型` `化学引导推理` `强化学习` `实验程序生成`

## 📋 核心要点

1. 核心问题：计算机辅助合成规划中，准确预测可行实验程序是连接计算设计与实际执行的关键挑战。
2. 方法要点：基于化学知识构建Chemistry-Guided Reasoning框架，通过监督微调和强化学习增强模型推理能力。
3. 实验或效果：QFANG在传统NLP指标和化学感知评估中优于先进通用推理模型，并能泛化到特定域外反应类。

## 📄 摘要（原文）

> Solving computer-aided synthesis planning is essential for enabling fully automated, robot-assisted synthesis workflows and improving the efficiency of drug discovery. A key challenge, however, is bridging the gap between computational route design and practical laboratory execution, particularly the accurate prediction of viable experimental procedures for each synthesis step. In this work, we present QFANG, a scientific reasoning language model capable of generating precise, structured experimental procedures directly from reaction equations, with explicit chain-of-thought reasoning. To develop QFANG, we curated a high-quality dataset comprising 905,990 chemical reactions paired with structured action sequences, extracted and processed from patent literature using large language models. We introduce a Chemistry-Guided Reasoning (CGR) framework that produces chain-of-thought data grounded in chemical knowledge at scale. The model subsequently undergoes supervised fine-tuning to elicit complex chemistry reasoning. Finally, we apply Reinforcement Learning from Verifiable Rewards (RLVR) to further enhance procedural accuracy. Experimental results demonstrate that QFANG outperforms advanced general-purpose reasoning models and nearest-neighbor retrieval baselines, measured by traditional NLP similarity metrics and a chemically aware evaluator using an LLM-as-a-judge. Moreover, QFANG generalizes to certain out-of-domain reaction classes and adapts to variations in laboratory conditions and user-specific constraints. We believe that QFANG's ability to generate high-quality synthesis procedures represents an important step toward bridging the gap between computational synthesis planning and fully automated laboratory synthesis.


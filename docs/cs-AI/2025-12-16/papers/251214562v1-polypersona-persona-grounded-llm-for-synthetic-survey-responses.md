---
layout: default
title: Polypersona: Persona-Grounded LLM for Synthetic Survey Responses
---

# Polypersona: Persona-Grounded LLM for Synthetic Survey Responses

**arXiv**: [2512.14562v1](https://arxiv.org/abs/2512.14562) | [PDF](https://arxiv.org/pdf/2512.14562.pdf)

**作者**: Tejaswani Dash, Dinesh Karri, Anudeep Vurity, Gautam Datla, Tazeem Ahmad, Saima Rafi, Rohith Tangudu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

**备注**: Accepted in IEEE Bigdata 2025- LLMs4ALL

---

## 💡 一句话要点

**提出PolyPersona框架，通过角色条件化微调生成多领域合成调查响应，支持高效可扩展的数据生成与评估。**

**关键词**: `角色条件化生成` `合成调查响应` `指令微调` `LoRA适配器` `4位量化` `多领域评估` `紧凑语言模型` `数据生成框架`

## 📋 核心要点

1. 现有方法在生成合成调查响应时，难以有效整合角色信息并保持行为一致性，导致数据质量受限。
2. 论文提出PolyPersona框架，通过角色条件化指令微调和对话式数据管道，确保生成响应与指定角色对齐。
3. 实验显示，紧凑模型如TinyLlama 1.1B和Phi-2在性能上媲美更大基线，BLEU最高达0.090，验证了方法的有效性。

## 📝 摘要（中文）

本文介绍了PolyPersona，一个用于生成跨多个领域的角色条件化调查响应的生成框架。该框架在资源自适应训练设置下，使用参数高效的LoRA适配器和4位量化对紧凑聊天模型进行指令微调。基于对话的数据管道明确保留角色线索，确保生成响应在行为上的一致性。利用此管道，我们构建了一个包含10个领域、433个不同角色的3,568个合成调查响应的数据集，支持受控指令微调和系统化的多领域评估。我们使用多指标评估套件评估生成响应，该套件结合了标准文本生成指标（包括BLEU、ROUGE和BERTScore）和专门设计的调查特定指标，用于评估结构连贯性、风格一致性和情感对齐。实验结果表明，TinyLlama 1.1B和Phi-2等紧凑模型实现了与较大7B至8B基线相当的性能，最高BLEU得分为0.090，ROUGE-1为0.429。这些发现表明，角色条件化微调使小型语言模型能够生成可靠且连贯的合成调查数据。所提出的框架为调查数据生成提供了一种高效且可重复的方法，支持可扩展评估，同时通过透明和开放的协议促进偏见分析。

## 🔬 方法详解

PolyPersona是一个生成框架，整体基于指令微调紧凑聊天模型，核心创新点包括：使用参数高效的LoRA适配器结合4位量化进行资源自适应训练，降低计算成本；设计对话式数据管道，明确保留角色线索（如人口统计特征、行为模式），确保生成响应的行为一致性。与现有方法的主要区别在于，它系统化地整合角色条件化，通过多领域数据集（10个领域、433个角色）支持可控微调和评估，而传统方法往往忽略角色对齐或依赖更大模型，导致效率低下。

## 📊 实验亮点

紧凑模型TinyLlama 1.1B和Phi-2在合成调查响应生成中，性能与7B-8B基线相当，最高BLEU得分0.090、ROUGE-1得分0.429，证明了角色条件化微调的有效性，同时框架构建了包含3,568个响应的多领域数据集，支持系统化评估。

## 🎯 应用场景

该研究可应用于社会科学调查、市场研究、用户体验测试等领域，用于高效生成合成调查数据，支持数据增强、模型评估和偏见分析，降低真实数据收集成本，促进可扩展和可重复的研究。

## 📄 摘要（原文）

> This paper introduces PolyPersona, a generative framework for synthesizing persona-conditioned survey responses across multiple domains. The framework instruction-tunes compact chat models using parameter-efficient LoRA adapters with 4-bit quantization under a resource-adaptive training setup. A dialogue-based data pipeline explicitly preserves persona cues, ensuring consistent behavioral alignment across generated responses. Using this pipeline, we construct a dataset of 3,568 synthetic survey responses spanning ten domains and 433 distinct personas, enabling controlled instruction tuning and systematic multi-domain evaluation. We evaluate the generated responses using a multi-metric evaluation suite that combines standard text generation metrics, including BLEU, ROUGE, and BERTScore, with survey-specific metrics designed to assess structural coherence, stylistic consistency, and sentiment alignment.Experimental results show that compact models such as TinyLlama 1.1B and Phi-2 achieve performance comparable to larger 7B to 8B baselines, with a highest BLEU score of 0.090 and ROUGE-1 of 0.429. These findings demonstrate that persona-conditioned fine-tuning enables small language models to generate reliable and coherent synthetic survey data. The proposed framework provides an efficient and reproducible approach for survey data generation, supporting scalable evaluation while facilitating bias analysis through transparent and open protocols.


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

**提出PolyPersona框架，通过角色条件化微调小型语言模型，实现多领域合成调查数据的高效生成。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `合成调查数据生成` `角色条件化语言模型` `LoRA适配器微调` `多领域评估` `参数高效训练` `文本生成指标` `偏见分析协议` `紧凑模型优化`

## 📋 核心要点

1. 现有方法在生成合成调查数据时，难以确保角色一致性和跨领域适应性，导致数据质量受限。
2. PolyPersona采用基于对话的数据管道和LoRA适配器，对紧凑模型进行角色条件化微调，以高效生成多领域响应。
3. 实验显示，小型模型如TinyLlama 1.1B在BLEU和ROUGE指标上接近大型基线，验证了框架的有效性。

## 📝 摘要（中文）

本文介绍了PolyPersona，一个用于生成跨多个领域的角色条件化调查响应的生成框架。该框架在资源自适应训练设置下，使用参数高效的LoRA适配器和4位量化技术，对紧凑的聊天模型进行指令微调。基于对话的数据管道明确保留了角色线索，确保生成响应在行为上的一致性。利用该管道，我们构建了一个包含3,568个合成调查响应的数据集，涵盖十个领域和433个不同角色，支持可控的指令微调和系统的多领域评估。我们使用多指标评估套件评估生成响应，该套件结合了标准文本生成指标（包括BLEU、ROUGE和BERTScore）和专门设计的调查特定指标，用于评估结构连贯性、风格一致性和情感对齐。实验结果表明，TinyLlama 1.1B和Phi-2等紧凑模型实现了与较大7B至8B基线相当的性能，最高BLEU得分为0.090，ROUGE-1为0.429。这些发现表明，角色条件化微调使小型语言模型能够生成可靠且连贯的合成调查数据。所提出的框架为调查数据生成提供了一种高效且可复现的方法，支持可扩展的评估，同时通过透明和开放的协议促进偏见分析。

## 🔬 方法详解

PolyPersona是一个生成框架，整体基于指令微调的紧凑聊天模型，结合参数高效的LoRA适配器和4位量化技术，在资源自适应训练设置下实现高效训练。关键技术创新点包括：基于对话的数据管道，明确保留角色线索以确保行为一致性；构建多领域合成数据集，支持可控微调和系统评估。与现有方法的主要区别在于，它专注于角色条件化生成，通过透明协议促进偏见分析，并利用小型模型实现与大型模型相当的性能，提高了生成效率和可扩展性。

## 📊 实验亮点

紧凑模型TinyLlama 1.1B和Phi-2在BLEU和ROUGE指标上达到与7B-8B基线相当水平，最高BLEU为0.090，ROUGE-1为0.429，证明了角色条件化微调能有效提升小型模型生成质量。

## 🎯 应用场景

该研究可应用于市场调研、社会科学实验和用户行为分析等领域，通过生成高质量的合成调查数据，支持数据增强、模型评估和偏见研究，降低真实数据收集成本。

## 📄 摘要（原文）

> This paper introduces PolyPersona, a generative framework for synthesizing persona-conditioned survey responses across multiple domains. The framework instruction-tunes compact chat models using parameter-efficient LoRA adapters with 4-bit quantization under a resource-adaptive training setup. A dialogue-based data pipeline explicitly preserves persona cues, ensuring consistent behavioral alignment across generated responses. Using this pipeline, we construct a dataset of 3,568 synthetic survey responses spanning ten domains and 433 distinct personas, enabling controlled instruction tuning and systematic multi-domain evaluation. We evaluate the generated responses using a multi-metric evaluation suite that combines standard text generation metrics, including BLEU, ROUGE, and BERTScore, with survey-specific metrics designed to assess structural coherence, stylistic consistency, and sentiment alignment.Experimental results show that compact models such as TinyLlama 1.1B and Phi-2 achieve performance comparable to larger 7B to 8B baselines, with a highest BLEU score of 0.090 and ROUGE-1 of 0.429. These findings demonstrate that persona-conditioned fine-tuning enables small language models to generate reliable and coherent synthetic survey data. The proposed framework provides an efficient and reproducible approach for survey data generation, supporting scalable evaluation while facilitating bias analysis through transparent and open protocols.


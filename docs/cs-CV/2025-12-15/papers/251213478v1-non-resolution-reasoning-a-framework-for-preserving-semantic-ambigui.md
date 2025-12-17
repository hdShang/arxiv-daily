---
layout: default
title: Non-Resolution Reasoning: A Framework for Preserving Semantic Ambiguity in Language Models
---

# Non-Resolution Reasoning: A Framework for Preserving Semantic Ambiguity in Language Models

**arXiv**: [2512.13478v1](https://arxiv.org/abs/2512.13478) | [PDF](https://arxiv.org/pdf/2512.13478.pdf)

**作者**: Kei Saito

---

## 💡 一句话要点

**提出非解析推理框架以解决语言模型过早语义塌陷问题**

**关键词**: `语义模糊性` `推理框架` `注意力机制` `上下文跟踪` `语言模型架构`

## 📋 核心要点

1. 核心问题：当前语言模型因softmax竞争和贪婪解码导致过早语义塌陷，丢弃有效解释。
2. 方法要点：集成多向量嵌入、非塌陷注意力和上下文身份跟踪，通过外部解析算子控制语义承诺。
3. 实验或效果：合成评估显示，在分布外身份转移任务中准确率达90.9%，远超基线9.1%。

## 📄 摘要（原文）

> Premature semantic collapse -- the forced early commitment to a single meaning -- remains a core architectural limitation of current language models. Softmax-driven competition and greedy decoding cause models to discard valid interpretations before sufficient context is available, resulting in brittle reasoning and context failures. We introduce Non-Resolution Reasoning (NRR), a general computational framework that preserves semantic ambiguity during inference and performs resolution only when explicitly required. NRR integrates three components: (1) Multi-Vector Embeddings that maintain multiple viable interpretations per token, (2) Non-Collapsing Attention that prevents winner-take-all dynamics across layers, and (3) Contextual Identity Tracking (CIT), which assigns context-specific identities to recurring entities (e.g., distinguishing "Dr. Smith the cardiologist" from "Dr. Smith the researcher"). These mechanisms are unified by an external Resolution Operator $ρ$ that makes semantic commitment explicit, controllable, and task-dependent. Unlike standard architectures, NRR separates representation from resolution, allowing a single model to shift between creative, factual, and ambiguity-preserving reasoning without retraining. A synthetic evaluation demonstrates NRR's ability to preserve ambiguity and track context: CIT-enhanced models achieve 90.9% accuracy on out-of-distribution identity-shift tasks, compared to 9.1% for transformer baselines. NRR provides a principled alternative to premature collapse, reframing ambiguity as an explicit representational state rather than a failure mode. The question is not whether AI should resolve ambiguity, but when, how, and under whose control.


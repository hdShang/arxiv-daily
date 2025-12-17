---
layout: default
title: PromptBridge: Cross-Model Prompt Transfer for Large Language Models
---

# PromptBridge: Cross-Model Prompt Transfer for Large Language Models

**arXiv**: [2512.01420v1](https://arxiv.org/abs/2512.01420) | [PDF](https://arxiv.org/pdf/2512.01420.pdf)

**作者**: Yaxuan Wang, Quan Liu, Zhenting Wang, Zichao Li, Wei Wei, Yang Liu, Yujia Bao

---

## 💡 一句话要点

**提出PromptBridge框架以解决大语言模型间提示迁移的性能下降问题**

**关键词**: `大语言模型` `提示工程` `模型漂移` `跨模型迁移` `无训练框架`

## 📋 核心要点

1. 核心问题：模型漂移导致跨模型提示重用性能显著下降
2. 方法要点：通过校准任务学习跨模型提示映射，无需训练
3. 实验或效果：在单代理和多代理设置中提升下游任务准确性

## 📄 摘要（原文）

> Large language models (LLMs) underpin applications in code generation, mathematical reasoning, and agent-based workflows. In practice, systems access LLMs via commercial APIs or open-source deployments, and the model landscape (e.g., GPT, Claude, Llama) evolves rapidly. This rapid evolution forces frequent model switches driven by capability, cost, deployment constraints, and privacy. Yet prompts are highly model-sensitive: reusing a prompt engineered for one model on another often yields substantially worse performance than a prompt optimized for the target model. We term this phenomenon Model Drifting. Through extensive empirical analysis across diverse LLM configurations, we show that model drifting is both common and severe. To address this challenge, we introduce PromptBridge, a training-free framework that preserves prompt effectiveness under model switches, enabling cross-model prompt transfer without costly per-task or per-model re-optimization. PromptBridge requires only a small set of alignment tasks for calibration. It first applies Model-Adaptive Reflective Prompt Evolution (MAP-RPE) to obtain task- and model-specific optimal prompts via iterative reflective refinement and quantitative evaluation. Using the resulting calibrated prompt pairs for the source and target models, PromptBridge learns a cross-model prompt mapping. At test time, i.e., for an unseen task, given a source-model prompt, this mapping directly produces an optimized prompt for the target model. Experiments in single-agent and multi-agent settings show that PromptBridge consistently improves downstream accuracy while reducing migration effort. The code will be available soon.


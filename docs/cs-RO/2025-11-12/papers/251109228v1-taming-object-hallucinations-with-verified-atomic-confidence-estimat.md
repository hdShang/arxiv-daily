---
layout: default
title: Taming Object Hallucinations with Verified Atomic Confidence Estimation
---

# Taming Object Hallucinations with Verified Atomic Confidence Estimation

**arXiv**: [2511.09228v1](https://arxiv.org/abs/2511.09228) | [PDF](https://arxiv.org/pdf/2511.09228.pdf)

**作者**: Jiarui Liu, Weihao Xuan, Zhijing Jin, Mona Diab

---

## 💡 一句话要点

**提出TACO框架以缓解多模态大语言模型中的幻觉问题**

**关键词**: `多模态大语言模型` `幻觉缓解` `置信度估计` `自验证` `基准测试`

## 📋 核心要点

1. 多模态大语言模型常出现物体存在、属性或关系的幻觉错误
2. TACO通过分解响应、改写查询和置信度估计进行自验证
3. 在多个基准测试中，TACO优于直接提示和视觉对比解码方法

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) often suffer from hallucinations, particularly errors in object existence, attributes, or relations, which undermine their reliability. We introduce TACO (Verified Atomic Confidence Estimation), a simple framework that mitigates hallucinations through self-verification and confidence calibration without relying on external vision experts. TACO decomposes responses into atomic queries, paraphrases them to reduce sensitivity to wording, and estimates confidence using self-consistency (black-box) or self-confidence (gray-box) aggregation, before refining answers with a language model. Experiments on five benchmarks (POPE, MME, HallusionBench, AMBER, and MM-Hal Bench) with two MLLMs (\texttt{LLaVA-1.5-7B} and \texttt{CogVLM2}) show that TACO consistently outperforms direct prompting and Visual Contrastive Decoding, reduces systematic biases, and improves confidence calibration, demonstrating its effectiveness in enhancing the faithfulness of MLLMs.


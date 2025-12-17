---
layout: default
title: Hindsight Distillation Reasoning with Knowledge Encouragement Preference for Knowledge-based Visual Question Answering
---

# Hindsight Distillation Reasoning with Knowledge Encouragement Preference for Knowledge-based Visual Question Answering

**arXiv**: [2511.11132v1](https://arxiv.org/abs/2511.11132) | [PDF](https://arxiv.org/pdf/2511.11132.pdf)

**作者**: Yu Zhao, Ying Zhang, Xuhui Sui, Baohang Zhou, Li Shen, Dacheng Tao

---

## 💡 一句话要点

**提出HinD框架与KEPO优化，以解决知识视觉问答中推理过程隐式的问题**

**关键词**: `知识视觉问答` `后见蒸馏推理` `知识鼓励偏好优化` `多模态大语言模型` `推理轨迹生成`

## 📋 核心要点

1. 核心问题：知识视觉问答中推理过程隐式，缺乏多步轨迹
2. 方法要点：使用后见蒸馏构建训练数据，并优化知识生成器偏好
3. 实验或效果：在OK-VQA和A-OKVQA上验证，7B模型实现高性能

## 📄 摘要（原文）

> Knowledge-based Visual Question Answering (KBVQA) necessitates external knowledge incorporation beyond cross-modal understanding. Existing KBVQA methods either utilize implicit knowledge in multimodal large language models (MLLMs) via in-context learning or explicit knowledge via retrieval augmented generation. However, their reasoning processes remain implicit, without explicit multi-step trajectories from MLLMs. To address this gap, we provide a Hindsight Distilled Reasoning (HinD) framework with Knowledge Encouragement Preference Optimization (KEPO), designed to elicit and harness internal knowledge reasoning ability in MLLMs. First, to tackle the reasoning supervision problem, we propose to emphasize the hindsight wisdom of MLLM by prompting a frozen 7B-size MLLM to complete the reasoning process between the question and its ground truth answer, constructing Hindsight-Zero training data. Then we self-distill Hindsight-Zero into Chain-of-Thought (CoT) Generator and Knowledge Generator, enabling the generation of sequential steps and discrete facts. Secondly, to tackle the misalignment between knowledge correctness and confidence, we optimize the Knowledge Generator with KEPO, preferring under-confident but helpful knowledge over the over-confident but unhelpful one. The generated CoT and sampled knowledge are then exploited for answer prediction. Experiments on OK-VQA and A-OKVQA validate the effectiveness of HinD, showing that HinD with elicited reasoning from 7B-size MLLM achieves superior performance without commercial model APIs or outside knowledge.


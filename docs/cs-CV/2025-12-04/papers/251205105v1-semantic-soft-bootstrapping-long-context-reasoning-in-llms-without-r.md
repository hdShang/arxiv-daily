---
layout: default
title: Semantic Soft Bootstrapping: Long Context Reasoning in LLMs without Reinforcement Learning
---

# Semantic Soft Bootstrapping: Long Context Reasoning in LLMs without Reinforcement Learning

**arXiv**: [2512.05105v1](https://arxiv.org/abs/2512.05105) | [PDF](https://arxiv.org/pdf/2512.05105.pdf)

**作者**: Purbesh Mitra, Sennur Ulukus

---

## 💡 一句话要点

**提出语义软自举方法，以自蒸馏技术提升大语言模型在数学推理任务中的长上下文推理能力。**

**关键词**: `长上下文推理` `自蒸馏训练` `数学推理` `大语言模型` `参数高效微调`

## 📋 核心要点

1. 核心问题：强化学习在长上下文推理中面临奖励稀疏和样本效率低等瓶颈，导致训练资源需求高。
2. 方法要点：通过同一模型生成正确与错误响应，构建教师-学生训练对，实现无人工干预的自蒸馏训练。
3. 实验或效果：在GSM8K数据集上微调Qwen2.5-3B-Instruct，在MATH500和AIME2024基准上准确率分别提升10.6%和10%。

## 📄 摘要（原文）

> Long context reasoning in large language models (LLMs) has demonstrated enhancement of their cognitive capabilities via chain-of-thought (CoT) inference. Training such models is usually done via reinforcement learning with verifiable rewards (RLVR) in reasoning based problems, like math and programming. However, RLVR is limited by several bottlenecks, such as, lack of dense reward, and inadequate sample efficiency. As a result, it requires significant compute resources in post-training phase. To overcome these limitations, in this work, we propose \textbf{Semantic Soft Bootstrapping (SSB)}, a self-distillation technique, in which the same base language model plays the role of both teacher and student, but receives different semantic contexts about the correctness of its outcome at training time. The model is first prompted with a math problem and several rollouts are generated. From them, the correct and most common incorrect response are filtered, and then provided to the model in context to produce a more robust, step-by-step explanation with a verified final answer. This pipeline automatically curates a paired teacher-student training set from raw problem-answer data, without any human intervention. This generation process also produces a sequence of logits, which is what the student model tries to match in the training phase just from the bare question alone. In our experiment, Qwen2.5-3B-Instruct on GSM8K dataset via parameter-efficient fine-tuning. We then tested its accuracy on MATH500, and AIME2024 benchmarks. Our experiments show a jump of 10.6%, and 10% improvements in accuracy, respectively, over group relative policy optimization (GRPO), which is a commonly used RLVR algorithm. Our code is available at https://github.com/purbeshmitra/semantic-soft-bootstrapping, and the model, curated dataset is available at https://huggingface.co/purbeshmitra/semantic-soft-bootstrapping.


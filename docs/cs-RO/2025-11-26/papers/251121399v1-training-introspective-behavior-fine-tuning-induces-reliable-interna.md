---
layout: default
title: Training Introspective Behavior: Fine-Tuning Induces Reliable Internal State Detection in a 7B Model
---

# Training Introspective Behavior: Fine-Tuning Induces Reliable Internal State Detection in a 7B Model

**arXiv**: [2511.21399v1](https://arxiv.org/abs/2511.21399) | [PDF](https://arxiv.org/pdf/2511.21399.pdf)

**作者**: Joshua Fonseca Rivera

---

## 💡 一句话要点

**通过微调使7B模型可靠检测单令牌注入的内部状态，提升AI透明度**

**关键词**: `语言模型微调` `内部状态检测` `AI透明度` `激活模式注入` `泛化能力`

## 📋 核心要点

1. 核心问题：语言模型能否通过训练可靠检测注入的激活模式，而非依赖自发涌现。
2. 方法要点：对7B模型进行微调，针对单令牌注入的瞬态激活模式进行训练。
3. 实验效果：准确率从0.4%提升至85%，假阳性率为0%，并泛化到未见概念。

## 📄 摘要（原文）

> Lindsey (2025) investigates introspective awareness in language models through four experiments, finding that models can sometimes detect and identify injected activation patterns -- but unreliably (~20% success in the best model). We focus on the first of these experiments -- self-report of injected "thoughts" -- and ask whether this capability can be directly trained rather than waiting for emergence. Through fine-tuning on transient single-token injections, we transform a 7B parameter model from near-complete failure (0.4% accuracy, 6.7% false positive rate) to reliable detection (85% accuracy on held-out concepts at α=40, 0% false positives). Our model detects fleeting "thoughts" injected at a single token position, retains that information, and reports the semantic content across subsequent generation steps. On this task, our trained model satisfies three of Lindsey's criteria: accuracy (correct identification), grounding (0/60 false positives), and internality (detection precedes verbalization). Generalization to unseen concept vectors (7.5pp gap) demonstrates the model learns a transferable skill rather than memorizing specific vectors, though this does not establish metacognitive representation in Lindsey's sense. These results address an open question raised by Lindsey: whether "training for introspection would help eliminate cross-model differences." We show that at least one component of introspective behavior can be directly induced, offering a pathway to built-in AI transparency.


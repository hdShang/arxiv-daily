---
layout: default
title: FiMMIA: scaling semantic perturbation-based membership inference across modalities
---

# FiMMIA: scaling semantic perturbation-based membership inference across modalities

**arXiv**: [2512.02786v1](https://arxiv.org/abs/2512.02786) | [PDF](https://arxiv.org/pdf/2512.02786.pdf)

**作者**: Anton Emelyanov, Sergei Kudriashov, Alena Fenogenova

---

## 💡 一句话要点

**提出FiMMIA框架以解决多模态大语言模型中的成员推断攻击问题**

**关键词**: `成员推断攻击` `多模态大语言模型` `分布偏移` `扰动方法` `框架设计`

## 📋 核心要点

1. 核心问题：现有成员推断攻击方法在多模态大语言模型中性能不足，因多模态组件适应不稳定和分布偏移。
2. 方法要点：通过识别数据集分布偏移，并扩展基线管道，将基于扰动的成员推断方法泛化至多模态模型。
3. 实验或效果：在多种微调多模态模型上评估，验证了基于扰动的攻击在多模态领域的有效性。

## 📄 摘要（原文）

> Membership Inference Attacks (MIAs) aim to determine whether a specific data point was included in the training set of a target model. Although there are have been numerous methods developed for detecting data contamination in large language models (LLMs), their performance on multimodal LLMs (MLLMs) falls short due to the instabilities introduced through multimodal component adaptation and possible distribution shifts across multiple inputs. In this work, we investigate multimodal membership inference and address two issues: first, by identifying distribution shifts in the existing datasets, and second, by releasing an extended baseline pipeline to detect them. We also generalize the perturbation-based membership inference methods to MLLMs and release \textbf{FiMMIA} -- a modular \textbf{F}ramework for \textbf{M}ultimodal \textbf{MIA}.\footnote{The source code and framework have been made publicly available under the MIT license via \href{https://github.com/ai-forever/data_leakage_detect}{link}.The video demonstration is available on \href{https://youtu.be/a9L4-H80aSg}{YouTube}.} Our approach trains a neural network to analyze the target model's behavior on perturbed inputs, capturing distributional differences between members and non-members. Comprehensive evaluations on various fine-tuned multimodal models demonstrate the effectiveness of our perturbation-based membership inference attacks in multimodal domains.


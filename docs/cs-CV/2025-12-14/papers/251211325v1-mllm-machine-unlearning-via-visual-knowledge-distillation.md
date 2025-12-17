---
layout: default
title: MLLM Machine Unlearning via Visual Knowledge Distillation
---

# MLLM Machine Unlearning via Visual Knowledge Distillation

**arXiv**: [2512.11325v1](https://arxiv.org/abs/2512.11325) | [PDF](https://arxiv.org/pdf/2512.11325.pdf)

**作者**: Yuhang Wang, Zhenxing Niu, Haoxuan Ji, Guangyu He, Haichang Gao, Gang Hua

---

## 💡 一句话要点

**提出视觉知识蒸馏方法以解决多模态大模型中的视觉知识选择性遗忘问题**

**关键词**: `多模态大模型` `机器遗忘` `视觉知识蒸馏` `选择性遗忘` `模型效率` `鲁棒性评估`

## 📋 核心要点

1. 核心问题：现有遗忘方法主要针对LLMs，多模态大模型遗忘研究处于早期阶段，需选择性移除视觉知识。
2. 方法要点：引入视觉知识蒸馏方案，利用模型内部视觉表示作为监督信号，仅微调视觉组件以提升效率。
3. 实验或效果：实验表明方法在有效性和效率上优于现有技术，并首次评估了遗忘对再学习攻击的鲁棒性。

## 📄 摘要（原文）

> Recently, machine unlearning approaches have been proposed to remove sensitive information from well-trained large models. However, most existing methods are tailored for LLMs, while MLLM-oriented unlearning remains at its early stage. Inspired by recent studies exploring the internal mechanisms of MLLMs, we propose to disentangle the visual and textual knowledge embedded within MLLMs and introduce a dedicated approach to selectively erase target visual knowledge while preserving textual knowledge. Unlike previous unlearning methods that rely on output-level supervision, our approach introduces a Visual Knowledge Distillation (VKD) scheme, which leverages intermediate visual representations within the MLLM as supervision signals. This design substantially enhances both unlearning effectiveness and model utility. Moreover, since our method only fine-tunes the visual components of the MLLM, it offers significant efficiency advantages. Extensive experiments demonstrate that our approach outperforms state-of-the-art unlearning methods in terms of both effectiveness and efficiency. Moreover, we are the first to evaluate the robustness of MLLM unlearning against relearning attacks.


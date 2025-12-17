---
layout: default
title: Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs
---

# Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs

**arXiv**: [2510.17771v1](https://arxiv.org/abs/2510.17771) | [PDF](https://arxiv.org/pdf/2510.17771.pdf)

**作者**: Zhining Liu, Ziyi Chen, Hui Liu, Chen Luo, Xianfeng Tang, Suhang Wang, Joy Zeng, Zhenwei Dai, Zhan Shi, Tianxin Wei, Benoit Dumoulin, Hanghang Tong

---

## 💡 一句话要点

**提出基于深度层注意力干预的方法，以解决视觉语言模型中视觉证据感知与答案正确性脱节的问题。**

**关键词**: `视觉语言模型` `注意力机制` `推理干预` `视觉问答` `模型诊断`

## 📋 核心要点

1. 核心问题：视觉语言模型在视觉证据存在时仍输出错误答案，出现'看见但不相信'现象。
2. 方法要点：通过分析层间注意力动态，引入无需训练的推理时干预，突出深度层证据区域。
3. 实验或效果：干预方法在LLaVA、Qwen等模型上一致提升准确性，增强模型可靠性。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) achieve strong results on multimodal tasks such
> as visual question answering, yet they can still fail even when the correct
> visual evidence is present. In this work, we systematically investigate whether
> these failures arise from not perceiving the evidence or from not leveraging it
> effectively. By examining layer-wise attention dynamics, we find that shallow
> layers focus primarily on text, while deeper layers sparsely but reliably
> attend to localized evidence regions. Surprisingly, VLMs often perceive the
> visual evidence when outputting incorrect answers, a phenomenon we term
> ``seeing but not believing'' that widely exists in major VLM families. Building
> on this, we introduce an inference-time intervention that highlights deep-layer
> evidence regions through selective attention-based masking. It requires no
> training and consistently improves accuracy across multiple families, including
> LLaVA, Qwen, Gemma, and InternVL. These results show that VLMs encode reliable
> evidence internally but under-utilize it, making such signals explicit can
> bridge the gap between perception and reasoning, advancing the diagnostic
> understanding and reliability of VLMs.


---
layout: default
title: V-ITI: Mitigating Hallucinations in Multimodal Large Language Models via Visual Inference-Time Intervention
---

# V-ITI: Mitigating Hallucinations in Multimodal Large Language Models via Visual Inference-Time Intervention

**arXiv**: [2512.03542v1](https://arxiv.org/abs/2512.03542) | [PDF](https://arxiv.org/pdf/2512.03542.pdf)

**作者**: Nan Sun, Zhenyu Zhang, Xixun Lin, Kun Wang, Yanmin Shang, Naibin Gu, Shuohuan Wang, Yu Sun, Hua Wu, Haifeng Wang, Yanan Cao

---

## 💡 一句话要点

**提出V-ITI框架，通过视觉推理时干预缓解多模态大语言模型中的幻觉问题**

**关键词**: `多模态大语言模型` `视觉幻觉缓解` `推理时干预` `视觉忽视检测` `激活调制`

## 📋 核心要点

1. 核心问题：多模态大语言模型存在视觉忽视导致的幻觉，现有方法因忽视干预时机而产生过干预问题
2. 方法要点：集成视觉忽视检测器与视觉回忆干预器，仅在检测到视觉忽视时调制激活，避免过干预
3. 实验或效果：在八个基准和不同模型家族上验证，有效缓解幻觉并保持一般任务性能

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) excel in numerous vision-language tasks yet suffer from hallucinations, producing content inconsistent with input visuals, that undermine reliability in precision-sensitive domains. This issue stems from a fundamental problem of visual neglect, where models fail to adequately prioritize input images. Existing methods typically alleviate hallucinations by intervening in the attention score or output logits, focusing on "how to intervene" but overlooking the prerequisite "when to intervene", which leads to the "over-intervention" problem and subsequently introduces new hallucinations and unnecessary computational overhead. To address this gap, we first investigate the mechanism of visual neglect and reveal it can be accurately detected via head-level activation patterns in MLLMs. We thus propose V-ITI, a lightweight visual inference-time intervention framework integrating a Visual Neglect Detector that identifies visual neglect via head-level discriminative probes and a Visual Recall Intervenor that modulates activations with prestored visual activation information only when the visual neglect is detected. Extensive experiments across eight benchmarks and different MLLM families demonstrate that V-ITI consistently mitigates vision-related hallucinations while preserving general task performance.


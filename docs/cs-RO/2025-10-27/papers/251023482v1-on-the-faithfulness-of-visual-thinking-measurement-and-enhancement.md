---
layout: default
title: On the Faithfulness of Visual Thinking: Measurement and Enhancement
---

# On the Faithfulness of Visual Thinking: Measurement and Enhancement

**arXiv**: [2510.23482v1](https://arxiv.org/abs/2510.23482) | [PDF](https://arxiv.org/pdf/2510.23482.pdf)

**作者**: Zujing Liu, Junwen Pan, Qi She, Yuan Gao, Guisong Xia

---

## 💡 一句话要点

**提出SCCM学习策略以增强视觉-语言模型多模态思维链的忠实性**

**关键词**: `多模态思维链` `视觉忠实性` `强化微调` `SCCM学习` `自动评估` `视觉-语言模型`

## 📋 核心要点

1. 核心问题：MCoT中视觉信息不忠实，常被忽略，导致推理过程不可靠
2. 方法要点：引入SCCM学习，鼓励生成充分且最小视觉组件，无需额外标注
3. 实验或效果：在细粒度感知和推理基准上，SCCM一致提升视觉忠实性

## 📄 摘要（原文）

> Recent large vision-language models (LVLMs) can generate vision-text
> multimodal chain-of-thought (MCoT) traces after reinforcement fine-tuning
> (RFT). However, we observe that the visual information incorporated in MCoT is
> often inaccurate, though still yield correct answers, indicating a lack of
> faithfulness in the MCoT reasoning process. We attribute this unfaithfulness to
> the RL reward in RFT, which solely incentivizes the format of interleaved
> vision-text cues, ie, it encourages the model to incorporate visual information
> into its text reasoning steps without considering the correctness of the visual
> information. In this paper, we first probe the faithfulness of MCoT by
> measuring how much the prediction changes when its visual and textual thoughts
> are intervened. Surprisingly, the model's predictions remain nearly unchanged
> under visual intervention but change significantly under textual intervention,
> indicating that the visual evidence is largely ignored. To further analyze
> visual information, we introduce an automated LVLM-based evaluation metric that
> quantifies the faithfulness of visual cues from two perspectives: reliability
> and sufficiency. Our evaluation reveals that the visual information in current
> MCoT traces is simultaneously unreliable and insufficient. To address this
> issue, we propose a novel MCoT learning strategy termed Sufficient-Component
> Cause Model (SCCM) learning. This approach encourages the MCoT to generate
> sufficient yet minimal visual components that are independently capable of
> leading to correct answers. We note that the proposed SCCM is annotation-free
> and compatible with various RFT for MCoT in a plug-and-play manner. Empirical
> results demonstrate that SCCM consistently improves the visual faithfulness
> across a suite of fine-grained perception and reasoning benchmarks. Code is
> available at https://github.com/EugeneLiu01/Faithful_Thinking_with_Image.


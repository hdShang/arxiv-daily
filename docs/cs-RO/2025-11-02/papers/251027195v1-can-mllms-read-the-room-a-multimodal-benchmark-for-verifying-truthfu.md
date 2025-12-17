---
layout: default
title: Can MLLMs Read the Room? A Multimodal Benchmark for Verifying Truthfulness in Multi-Party Social Interactions
---

# Can MLLMs Read the Room? A Multimodal Benchmark for Verifying Truthfulness in Multi-Party Social Interactions

**arXiv**: [2510.27195v1](https://arxiv.org/abs/2510.27195) | [PDF](https://arxiv.org/pdf/2510.27195.pdf)

**作者**: Caixin Kang, Yifei Huang, Liangyang Ouyang, Mingfang Zhang, Yoichi Sato

---

## 💡 一句话要点

**提出多模态交互真实性评估任务与数据集，以评估MLLMs在多党社交互动中的真实性检测能力**

**关键词**: `多模态大语言模型` `欺骗检测` `多党社交互动` `真实性评估` `视觉语言理解`

## 📋 核心要点

1. 核心问题：多党动态对话中自动检测欺骗的挑战，涉及语言和视觉线索的复杂交互
2. 方法要点：基于狼人杀游戏构建多模态数据集，包含同步视频、文本和真实性标签
3. 实验或效果：评估显示GPT-4o等模型性能不足，未能有效结合视觉社交线索

## 📄 摘要（原文）

> As AI systems become increasingly integrated into human lives, endowing them
> with robust social intelligence has emerged as a critical frontier. A key
> aspect of this intelligence is discerning truth from deception, a ubiquitous
> element of human interaction that is conveyed through a complex interplay of
> verbal language and non-verbal visual cues. However, automatic deception
> detection in dynamic, multi-party conversations remains a significant
> challenge. The recent rise of powerful Multimodal Large Language Models
> (MLLMs), with their impressive abilities in visual and textual understanding,
> makes them natural candidates for this task. Consequently, their capabilities
> in this crucial domain are mostly unquantified. To address this gap, we
> introduce a new task, Multimodal Interactive Veracity Assessment (MIVA), and
> present a novel multimodal dataset derived from the social deduction game
> Werewolf. This dataset provides synchronized video, text, with verifiable
> ground-truth labels for every statement. We establish a comprehensive benchmark
> evaluating state-of-the-art MLLMs, revealing a significant performance gap:
> even powerful models like GPT-4o struggle to distinguish truth from falsehood
> reliably. Our analysis of failure modes indicates that these models fail to
> ground language in visual social cues effectively and may be overly
> conservative in their alignment, highlighting the urgent need for novel
> approaches to building more perceptive and trustworthy AI systems.


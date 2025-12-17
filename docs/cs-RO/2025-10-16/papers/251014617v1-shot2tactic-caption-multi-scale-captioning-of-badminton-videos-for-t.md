---
layout: default
title: Shot2Tactic-Caption: Multi-Scale Captioning of Badminton Videos for Tactical Understanding
---

# Shot2Tactic-Caption: Multi-Scale Captioning of Badminton Videos for Tactical Understanding

**arXiv**: [2510.14617v1](https://arxiv.org/abs/2510.14617) | [PDF](https://arxiv.org/pdf/2510.14617.pdf)

**作者**: Ning Ding, Keisuke Fujii, Toru Tamaki

---

## 💡 一句话要点

**提出Shot2Tactic-Caption框架，用于羽毛球视频的多尺度战术理解与描述**

**关键词**: `视频描述` `多尺度理解` `羽毛球战术` `Transformer` `提示引导机制` `战术单元检测`

## 📋 核心要点

1. 核心问题：羽毛球战术理解需描述个体动作和动态战术执行过程
2. 方法要点：采用双分支设计，结合视觉编码器和Transformer，引入战术单元检测器与提示引导机制
3. 实验或效果：在自建数据集上验证有效性，ResNet50编码器和提示机制提升准确性

## 📄 摘要（原文）

> Tactical understanding in badminton involves interpreting not only individual
> actions but also how tactics are dynamically executed over time. In this paper,
> we propose \textbf{Shot2Tactic-Caption}, a novel framework for semantic and
> temporal multi-scale video captioning in badminton, capable of generating
> shot-level captions that describe individual actions and tactic-level captions
> that capture how these actions unfold over time within a tactical execution. We
> also introduce the Shot2Tactic-Caption Dataset, the first badminton captioning
> dataset containing 5,494 shot captions and 544 tactic captions.
> Shot2Tactic-Caption adopts a dual-branch design, with both branches including a
> visual encoder, a spatio-temporal Transformer encoder, and a Transformer-based
> decoder to generate shot and tactic captions. To support tactic captioning, we
> additionally introduce a Tactic Unit Detector that identifies valid tactic
> units, tactic types, and tactic states (e.g., Interrupt, Resume). For tactic
> captioning, we further incorporate a shot-wise prompt-guided mechanism, where
> the predicted tactic type and state are embedded as prompts and injected into
> the decoder via cross-attention. The shot-wise prompt-guided mechanism enables
> our system not only to describe successfully executed tactics but also to
> capture tactical executions that are temporarily interrupted and later resumed.
> Experimental results demonstrate the effectiveness of our framework in
> generating both shot and tactic captions. Ablation studies show that the
> ResNet50-based spatio-temporal encoder outperforms other variants, and that
> shot-wise prompt structuring leads to more coherent and accurate tactic
> captioning.


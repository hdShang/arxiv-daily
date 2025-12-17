---
layout: default
title: FAME: Fairness-aware Attention-modulated Video Editing
---

# FAME: Fairness-aware Attention-modulated Video Editing

**arXiv**: [2510.22960v1](https://arxiv.org/abs/2510.22960) | [PDF](https://arxiv.org/pdf/2510.22960.pdf)

**作者**: Zhangkai Wu, Xuhui Fan, Zhongyuan Xie, Kaize Shi, Zhidong Li, Longbing Cao

---

## 💡 一句话要点

**提出FAME方法以缓解视频编辑中的职业相关性别偏见，同时保持提示对齐和时间一致性。**

**关键词**: `视频编辑` `公平性` `注意力机制` `时间一致性` `去偏技术`

## 📋 核心要点

1. 核心问题：无训练视频编辑模型在渲染职业相关提示时易陷入性别刻板印象。
2. 方法要点：通过软注入去偏标记和调制注意力机制，增强公平性并减少时间不一致。
3. 实验或效果：在FairVE基准上，FAME在公平对齐和语义保真度上优于现有基线。

## 📄 摘要（原文）

> Training-free video editing (VE) models tend to fall back on gender
> stereotypes when rendering profession-related prompts. We propose \textbf{FAME}
> for \textit{Fairness-aware Attention-modulated Video Editing} that mitigates
> profession-related gender biases while preserving prompt alignment and temporal
> consistency for coherent VE. We derive fairness embeddings from existing
> minority representations by softly injecting debiasing tokens into the text
> encoder. Simultaneously, FAME integrates fairness modulation into both temporal
> self attention and prompt-to-region cross attention to mitigate the motion
> corruption and temporal inconsistency caused by directly introducing fairness
> cues. For temporal self attention, FAME introduces a region constrained
> attention mask combined with time decay weighting, which enhances intra-region
> coherence while suppressing irrelevant inter-region interactions. For cross
> attention, it reweights tokens to region matching scores by incorporating
> fairness sensitive similarity masks derived from debiasing prompt embeddings.
> Together, these modulations keep fairness-sensitive semantics tied to the right
> visual regions and prevent temporal drift across frames. Extensive experiments
> on new VE fairness-oriented benchmark \textit{FairVE} demonstrate that FAME
> achieves stronger fairness alignment and semantic fidelity, surpassing existing
> VE baselines.


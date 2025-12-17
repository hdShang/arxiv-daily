---
layout: default
title: HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives
---

# HoloCine: Holistic Generation of Cinematic Multi-Shot Long Video Narratives

**arXiv**: [2510.20822v1](https://arxiv.org/abs/2510.20822) | [PDF](https://arxiv.org/pdf/2510.20822.pdf)

**作者**: Yihao Meng, Hao Ouyang, Yue Yu, Qiuyu Wang, Wen Wang, Ka Leong Cheng, Hanlin Wang, Yixuan Li, Cheng Chen, Yanhong Zeng, Yujun Shen, Huamin Qu

---

## 💡 一句话要点

**提出HoloCine模型以解决文本到视频生成中的叙事一致性问题**

**关键词**: `文本到视频生成` `多镜头叙事` `注意力机制` `长视频生成` `电影制作自动化`

## 📋 核心要点

1. 核心问题：现有文本到视频模型难以生成连贯的多镜头长视频叙事
2. 方法要点：采用窗口交叉注意力和稀疏镜头间自注意力机制，确保全局一致性和效率
3. 实验或效果：在叙事一致性上达到新SOTA，并涌现出持久记忆和电影技术理解能力

## 📄 摘要（原文）

> State-of-the-art text-to-video models excel at generating isolated clips but
> fall short of creating the coherent, multi-shot narratives, which are the
> essence of storytelling. We bridge this "narrative gap" with HoloCine, a model
> that generates entire scenes holistically to ensure global consistency from the
> first shot to the last. Our architecture achieves precise directorial control
> through a Window Cross-Attention mechanism that localizes text prompts to
> specific shots, while a Sparse Inter-Shot Self-Attention pattern (dense within
> shots but sparse between them) ensures the efficiency required for minute-scale
> generation. Beyond setting a new state-of-the-art in narrative coherence,
> HoloCine develops remarkable emergent abilities: a persistent memory for
> characters and scenes, and an intuitive grasp of cinematic techniques. Our work
> marks a pivotal shift from clip synthesis towards automated filmmaking, making
> end-to-end cinematic creation a tangible future. Our code is available at:
> https://holo-cine.github.io/.


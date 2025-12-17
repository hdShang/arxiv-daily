---
layout: default
title: SceneDecorator: Towards Scene-Oriented Story Generation with Scene Planning and Scene Consistency
---

# SceneDecorator: Towards Scene-Oriented Story Generation with Scene Planning and Scene Consistency

**arXiv**: [2510.22994v1](https://arxiv.org/abs/2510.22994) | [PDF](https://arxiv.org/pdf/2510.22994.pdf)

**作者**: Quanjian Song, Donghao Zhou, Jingyu Lin, Fei Shen, Jiaze Wang, Xiaowei Hu, Cunjian Chen, Pheng-Ann Heng

---

## 💡 一句话要点

**提出SceneDecorator框架以解决场景导向故事生成中的场景规划和一致性挑战**

**关键词**: `场景导向故事生成` `场景规划` `场景一致性` `VLM引导` `长时注意力` `训练无关框架`

## 📋 核心要点

1. 核心问题：现有方法忽视场景在故事生成中的作用，导致叙事连贯性和场景一致性不足
2. 方法要点：采用VLM引导场景规划确保全局到局部的叙事连贯，长时场景共享注意力维持一致性
3. 实验或效果：广泛实验显示SceneDecorator性能优越，在艺术、电影和游戏领域有应用潜力

## 📄 摘要（原文）

> Recent text-to-image models have revolutionized image generation, but they
> still struggle with maintaining concept consistency across generated images.
> While existing works focus on character consistency, they often overlook the
> crucial role of scenes in storytelling, which restricts their creativity in
> practice. This paper introduces scene-oriented story generation, addressing two
> key challenges: (i) scene planning, where current methods fail to ensure
> scene-level narrative coherence by relying solely on text descriptions, and
> (ii) scene consistency, which remains largely unexplored in terms of
> maintaining scene consistency across multiple stories. We propose
> SceneDecorator, a training-free framework that employs VLM-Guided Scene
> Planning to ensure narrative coherence across different scenes in a
> ``global-to-local'' manner, and Long-Term Scene-Sharing Attention to maintain
> long-term scene consistency and subject diversity across generated stories.
> Extensive experiments demonstrate the superior performance of SceneDecorator,
> highlighting its potential to unleash creativity in the fields of arts, films,
> and games.


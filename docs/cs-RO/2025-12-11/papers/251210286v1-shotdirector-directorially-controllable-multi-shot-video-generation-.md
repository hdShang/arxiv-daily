---
layout: default
title: ShotDirector: Directorially Controllable Multi-Shot Video Generation with Cinematographic Transitions
---

# ShotDirector: Directorially Controllable Multi-Shot Video Generation with Cinematographic Transitions

**arXiv**: [2512.10286v1](https://arxiv.org/abs/2512.10286) | [PDF](https://arxiv.org/pdf/2512.10286.pdf)

**作者**: Xiaoxue Wu, Xinyuan Chen, Yaohui Wang, Yu Qiao

---

## 💡 一句话要点

**提出ShotDirector框架，通过参数级相机控制和分层编辑模式提示，实现可控多镜头视频生成。**

**关键词**: `多镜头视频生成` `可控镜头过渡` `相机控制` `编辑模式提示` `电影语言`

## 📋 核心要点

1. 核心问题：现有方法忽视镜头过渡的导演设计和电影语言，导致无意图的序列变化。
2. 方法要点：集成6-DoF相机控制模块和分层编辑模式感知提示，结合参数级条件与高层语义指导。
3. 实验或效果：构建ShotWeaver40K数据集，开发评估指标，实验验证框架有效性。

## 📄 摘要（原文）

> Shot transitions play a pivotal role in multi-shot video generation, as they determine the overall narrative expression and the directorial design of visual storytelling. However, recent progress has primarily focused on low-level visual consistency across shots, neglecting how transitions are designed and how cinematographic language contributes to coherent narrative expression. This often leads to mere sequential shot changes without intentional film-editing patterns. To address this limitation, we propose ShotDirector, an efficient framework that integrates parameter-level camera control and hierarchical editing-pattern-aware prompting. Specifically, we adopt a camera control module that incorporates 6-DoF poses and intrinsic settings to enable precise camera information injection. In addition, a shot-aware mask mechanism is employed to introduce hierarchical prompts aware of professional editing patterns, allowing fine-grained control over shot content. Through this design, our framework effectively combines parameter-level conditions with high-level semantic guidance, achieving film-like controllable shot transitions. To facilitate training and evaluation, we construct ShotWeaver40K, a dataset that captures the priors of film-like editing patterns, and develop a set of evaluation metrics for controllable multi-shot video generation. Extensive experiments demonstrate the effectiveness of our framework.


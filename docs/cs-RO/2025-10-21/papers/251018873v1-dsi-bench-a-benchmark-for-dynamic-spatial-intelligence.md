---
layout: default
title: DSI-Bench: A Benchmark for Dynamic Spatial Intelligence
---

# DSI-Bench: A Benchmark for Dynamic Spatial Intelligence

**arXiv**: [2510.18873v1](https://arxiv.org/abs/2510.18873) | [PDF](https://arxiv.org/pdf/2510.18873.pdf)

**作者**: Ziang Zhang, Zehan Wang, Guanghao Zhang, Weilong Dai, Yan Xia, Ziang Yan, Minjie Hong, Zhou Zhao

---

## 💡 一句话要点

**提出DSI-Bench基准以评估动态3D场景中的空间推理能力**

**关键词**: `动态空间推理` `视觉语言模型` `基准评估` `运动模式` `3D场景理解`

## 📋 核心要点

1. 核心问题：视觉语言模型在动态3D场景中难以准确推理观察者和物体的同时运动
2. 方法要点：构建包含近1000个动态视频和1700多个问题的基准，覆盖九种解耦运动模式
3. 实验或效果：评估14个模型，发现模型常混淆运动类型并存在语义偏见

## 📄 摘要（原文）

> Reasoning about dynamic spatial relationships is essential, as both observers
> and objects often move simultaneously. Although vision-language models (VLMs)
> and visual expertise models excel in 2D tasks and static scenarios, their
> ability to fully understand dynamic 3D scenarios remains limited. We introduce
> Dynamic Spatial Intelligence and propose DSI-Bench, a benchmark with nearly
> 1,000 dynamic videos and over 1,700 manually annotated questions covering nine
> decoupled motion patterns of observers and objects. Spatially and temporally
> symmetric designs reduce biases and enable systematic evaluation of models'
> reasoning about self-motion and object motion. Our evaluation of 14 VLMs and
> expert models reveals key limitations: models often conflate observer and
> object motion, exhibit semantic biases, and fail to accurately infer relative
> relationships in dynamic scenarios. Our DSI-Bench provides valuable findings
> and insights about the future development of general and expertise models with
> dynamic spatial intelligence.


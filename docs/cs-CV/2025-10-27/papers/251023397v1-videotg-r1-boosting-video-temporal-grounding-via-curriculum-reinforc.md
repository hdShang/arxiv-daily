---
layout: default
title: VideoTG-R1: Boosting Video Temporal Grounding via Curriculum Reinforcement Learning on Reflected Boundary Annotations
---

# VideoTG-R1: Boosting Video Temporal Grounding via Curriculum Reinforcement Learning on Reflected Boundary Annotations

**arXiv**: [2510.23397v1](https://arxiv.org/abs/2510.23397) | [PDF](https://arxiv.org/pdf/2510.23397.pdf)

**作者**: Lu Dong, Haiyu Zhang, Han Lin, Ziang Yan, Xiangyu Zeng, Hongjie Zhang, Yifei Huang, Yi Wang, Zhen-Hua Ling, Limin Wang, Yali Wang

---

## 💡 一句话要点

**提出VideoTG-R1课程强化学习框架，通过边界反射和难度估计提升视频时序定位性能。**

**关键词**: `视频时序定位` `强化学习` `课程学习` `边界标注` `多模态大语言模型` `视频问答`

## 📋 核心要点

1. 核心问题：视频时序定位中部分标注样本引入歧义，难定位样本在强化学习中奖励低且无偏好。
2. 方法要点：使用边界反射代理过滤部分标注样本，难度估计代理动态屏蔽难样本以优化训练。
3. 实验效果：仅用10%训练数据和21%计算预算，在VTG和VideoQA任务中超越全数据方法。

## 📄 摘要（原文）

> Video temporal grounding (VTG) aims to locate precise segments in videos
> based on language queries, which is a fundamental challenge in video
> understanding. While recent Multimodal Large Language Models (MLLMs) have shown
> promise in tackling VTG through reinforcement learning (RL), they overlook the
> challenges arising from both the quality and difficulty of training samples.
> (1) Partially annotated samples. Many samples contain relevant segments beyond
> the annotated interval, introducing ambiguous supervision. (2) Hard-to-ground
> samples. Samples with poor zero-shot performance produce consistently low and
> indistinguishable rewards during RL training, exhibiting no clear preference
> among multiple outputs and thus hindering learning efficiency. To address these
> challenges, we propose VideoTG-R1, a novel curriculum RL framework with
> reflected boundary annotations, enabling data-efficient training. Specifically,
> we propose a Boundary Reflection Agent that utilizes MLLMs to predict
> query-relevant timestamps outside the annotated intervals, allowing us to
> identify and filter out partially annotated samples, thereby reducing
> ambiguity. Furthermore, we introduce a Difficulty Estimation Agent to assess
> the training difficulty of each sample and design a curriculum RL strategy that
> dynamically masks the videos of hard-to-ground samples according to the
> training steps, easing the training difficulty and providing clearer
> preference. Experiments on the VTG and grounded VideoQA tasks demonstrate the
> effectiveness of our method. Remarkably, with only 10% of the training samples
> and 21% of the computational budget, VideoTG-R1 outperforms full-data
> counterparts under both group relative policy optimization (GRPO) and
> supervised fine-tuning (SFT). The code is available at
> https://github.com/ldong1111/VideoTG-R1.


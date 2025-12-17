---
layout: default
title: Dual Learning with Dynamic Knowledge Distillation and Soft Alignment for Partially Relevant Video Retrieval
---

# Dual Learning with Dynamic Knowledge Distillation and Soft Alignment for Partially Relevant Video Retrieval

**arXiv**: [2510.12283v1](https://arxiv.org/abs/2510.12283) | [PDF](https://arxiv.org/pdf/2510.12283.pdf)

**作者**: Jianfeng Dong, Lei Huang, Daizong Liu, Xianke Chen, Xun Yang, Changting Lin, Xun Wang, Meng Wang

---

## 💡 一句话要点

**提出动态知识蒸馏与软对齐的双学习框架，以解决部分相关长视频检索问题。**

**关键词**: `部分相关视频检索` `知识蒸馏` `双学习框架` `动态软目标` `长视频理解` `视觉语言模型`

## 📋 核心要点

1. 核心问题：长视频中仅部分内容与查询相关，传统方法假设视频已修剪，不适用于实际场景。
2. 方法要点：使用大型教师模型监督轻量学生网络，通过继承和探索分支处理领域差异。
3. 实验效果：在TVR、ActivityNet和Charades-STA数据集上达到最先进性能。

## 📄 摘要（原文）

> Almost all previous text-to-video retrieval works ideally assume that videos
> are pre-trimmed with short durations containing solely text-related content.
> However, in practice, videos are typically untrimmed in long durations with
> much more complicated background content. Therefore, in this paper, we focus on
> the more practical yet challenging task of Partially Relevant Video Retrieval
> (PRVR), which aims to retrieve partially relevant untrimmed videos with the
> given query. To tackle this task, we propose a novel framework that distills
> generalization knowledge from a powerful large-scale vision-language
> pre-trained model and transfers it to a lightweight, task-specific PRVR
> network. Specifically, we introduce a Dual Learning framework with Dynamic
> Knowledge Distillation (DL-DKD++), where a large teacher model provides
> supervision to a compact dual-branch student network. The student model
> comprises two branches: an inheritance branch that absorbs transferable
> knowledge from the teacher, and an exploration branch that learns task-specific
> information from the PRVR dataset to address domain gaps. To further enhance
> learning, we incorporate a dynamic soft-target construction mechanism. By
> replacing rigid hard-target supervision with adaptive soft targets that evolve
> during training, our method enables the model to better capture the
> fine-grained, partial relevance between videos and queries. Experiment results
> demonstrate that our proposed model achieves state-of-the-art performance on
> TVR, ActivityNet, and Charades-STA datasets for PRVR. The code is available at
> https://github.com/HuiGuanLab/DL-DKD.


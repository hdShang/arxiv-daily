---
layout: default
title: While recognizing actions, LMMs struggle to detect core interaction events
---

# While recognizing actions, LMMs struggle to detect core interaction events

**arXiv**: [2511.20162v1](https://arxiv.org/abs/2511.20162) | [PDF](https://arxiv.org/pdf/2511.20162.pdf)

**作者**: Daniel Harari, Michael Sidorov, Liel David, Chen Shterental, Abrham Kahsay Gebreselasie, Muhammad Haris Khan

---

## 💡 一句话要点

**提出大规模交互事件数据集，揭示LMMs在检测物理接触事件时缺乏感知基础。**

**关键词**: `大规模多模态模型` `视频交互事件检测` `感知基础` `数据集构建` `物理接触定位` `动作识别`

## 📋 核心要点

1. 核心问题：LMMs在视频中难以定位交互开始或结束的帧和位置，尽管能识别动作和对象。
2. 方法要点：构建首个大规模数据集，标注20K+视频交互事件，包括接触和释放时刻。
3. 实验或效果：测试Qwen-2.5VL和GPT-4o，模型无法准确检测事件帧和位置，显示感知基础不足。

## 📄 摘要（原文）

> Large multi-modal models (LMMs) show increasing performance in realistic visual tasks for images and, more recently, for videos. For example, given a video sequence, such models are able to describe in detail objects, the surroundings and dynamic actions. In this study, we explored the extent to which these models ground their semantic understanding in the actual visual input. Specifically, given sequences of hands interacting with objects, we asked models when and where the interaction begins or ends. For this purpose, we introduce a first of its kind, large-scale dataset with more than 20K annotated interactions on videos from the Something-Something-V2 dataset. 250 AMTurk human annotators labeled core interaction events, particularly when and where objects and agents become attached ('contact') or detached ('release'). We asked two LMMs (Qwen-2.5VL and GPT-4o) to locate these events in short videos, each with a single event. The results show that although the models can reliably name the target objects, identify the action and provide coherent reasoning, they consistently fail to identify the frame where the interaction begins or ends and cannot localize the event within the scene. Our findings suggest that in struggling to pinpoint the moment and location of physical contact that defines the interaction, the models lack the perceptual grounding required for deeper understanding of dynamic scenes.


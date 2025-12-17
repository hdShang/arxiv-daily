---
layout: default
title: FoundationMotion: Auto-Labeling and Reasoning about Spatial Movement in Videos
---

# FoundationMotion: Auto-Labeling and Reasoning about Spatial Movement in Videos

**arXiv**: [2512.10927v1](https://arxiv.org/abs/2512.10927) | [PDF](https://arxiv.org/pdf/2512.10927.pdf)

**作者**: Yulu Gan, Ligeng Zhu, Dandan Shan, Baifeng Shi, Hongxu Yin, Boris Ivanovic, Song Han, Trevor Darrell, Jitendra Malik, Marco Pavone, Boyi Li

---

## 💡 一句话要点

**提出FoundationMotion自动标注流水线以解决视频运动理解数据稀缺问题**

**关键词**: `视频运动理解` `自动数据标注` `轨迹分析` `大语言模型应用` `模型微调`

## 📋 核心要点

1. 核心问题：现有运动数据集依赖人工标注，规模有限，阻碍模型性能提升。
2. 方法要点：通过目标检测与跟踪提取轨迹，结合LLM自动生成细粒度标注和问答对。
3. 实验或效果：微调开源模型在多个运动理解基准上超越闭源和大型开源基线。

## 📄 摘要（原文）

> Motion understanding is fundamental to physical reasoning, enabling models to infer dynamics and predict future states. However, state-of-the-art models still struggle on recent motion benchmarks, primarily due to the scarcity of large-scale, fine-grained motion datasets. Existing motion datasets are often constructed from costly manual annotation, severely limiting scalability. To address this challenge, we introduce FoundationMotion, a fully automated data curation pipeline that constructs large-scale motion datasets. Our approach first detects and tracks objects in videos to extract their trajectories, then leverages these trajectories and video frames with Large Language Models (LLMs) to generate fine-grained captions and diverse question-answer pairs about motion and spatial reasoning. Using datasets produced by this pipeline, we fine-tune open-source models including NVILA-Video-15B and Qwen2.5-7B, achieving substantial improvements in motion understanding without compromising performance on other tasks. Notably, our models outperform strong closed-source baselines like Gemini-2.5 Flash and large open-source models such as Qwen2.5-VL-72B across diverse motion understanding datasets and benchmarks. FoundationMotion thus provides a scalable solution for curating fine-grained motion datasets that enable effective fine-tuning of diverse models to enhance motion understanding and spatial reasoning capabilities.


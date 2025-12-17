---
layout: default
title: Class Prototypes based Contrastive Learning for Classifying Multi-Label and Fine-Grained Educational Videos
---

# Class Prototypes based Contrastive Learning for Classifying Multi-Label and Fine-Grained Educational Videos

**arXiv**: [2510.11204v1](https://arxiv.org/abs/2510.11204) | [PDF](https://arxiv.org/pdf/2510.11204.pdf)

**作者**: Rohit Gupta, Anirban Roy, Claire Christensen, Sujeong Kim, Sarah Gerard, Madeline Cincebeaux, Ajay Divakaran, Todd Grindal, Mubarak Shah

---

## 💡 一句话要点

**提出基于类原型的对比学习方法，以分类多标签细粒度教育视频。**

**关键词**: `多标签分类` `细粒度分类` `对比学习` `多模态Transformer` `教育视频分析` `类原型学习`

## 📋 核心要点

1. 核心问题：在线视频中检测儿童教育内容，如识字和数学的细粒度子类。
2. 方法要点：使用类原型监督对比学习，最小化类内距离并最大化类间距离。
3. 实验或效果：在APPROVE数据集上优于基线，并验证于Youtube-8M和COIN。

## 📄 摘要（原文）

> The recent growth in the consumption of online media by children during early
> childhood necessitates data-driven tools enabling educators to filter out
> appropriate educational content for young learners. This paper presents an
> approach for detecting educational content in online videos. We focus on two
> widely used educational content classes: literacy and math. For each class, we
> choose prominent codes (sub-classes) based on the Common Core Standards. For
> example, literacy codes include `letter names', `letter sounds', and math codes
> include `counting', `sorting'. We pose this as a fine-grained multilabel
> classification problem as videos can contain multiple types of educational
> content and the content classes can get visually similar (e.g., `letter names'
> vs `letter sounds'). We propose a novel class prototypes based supervised
> contrastive learning approach that can handle fine-grained samples associated
> with multiple labels. We learn a class prototype for each class and a loss
> function is employed to minimize the distances between a class prototype and
> the samples from the class. Similarly, distances between a class prototype and
> the samples from other classes are maximized. As the alignment between visual
> and audio cues are crucial for effective comprehension, we consider a
> multimodal transformer network to capture the interaction between visual and
> audio cues in videos while learning the embedding for videos. For evaluation,
> we present a dataset, APPROVE, employing educational videos from YouTube
> labeled with fine-grained education classes by education researchers. APPROVE
> consists of 193 hours of expert-annotated videos with 19 classes. The proposed
> approach outperforms strong baselines on APPROVE and other benchmarks such as
> Youtube-8M, and COIN. The dataset is available at
> https://github.com/rohit-gupta/MMContrast/tree/main/APPROVE


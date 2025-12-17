---
layout: default
title: Unison: A Fully Automatic, Task-Universal, and Low-Cost Framework for Unified Understanding and Generation
---

# Unison: A Fully Automatic, Task-Universal, and Low-Cost Framework for Unified Understanding and Generation

**arXiv**: [2512.07747v1](https://arxiv.org/abs/2512.07747) | [PDF](https://arxiv.org/pdf/2512.07747.pdf)

**作者**: Shihao Zhao, Yitong Chen, Zeyinzi Jiang, Bojia Zi, Shaozhe Hao, Yu Liu, Chaojie Mao, Kwan-Yee K. Wong

---

## 💡 一句话要点

**提出Unison框架，以低成本实现多模态理解与生成的统一自动化处理**

**关键词**: `多模态学习` `统一理解与生成` `自动化任务解析` `低成本训练` `两阶段框架`

## 📋 核心要点

1. 核心问题：现有统一多模态方法成本高、任务覆盖有限且依赖手动配置参数
2. 方法要点：采用两阶段方案，结合预训练模型，自动解析用户意图和任务元信息
3. 实验或效果：仅用500k样本和50 GPU小时，在多种任务上实现准确自动识别和优越性能

## 📄 摘要（原文）

> Unified understanding and generation is a highly appealing research direction in multimodal learning. There exist two approaches: one trains a transformer via an auto-regressive paradigm, and the other adopts a two-stage scheme connecting pre-trained understanding and generative models for alignment fine-tuning. The former demands massive data and computing resources unaffordable for ordinary researchers. Though the latter requires a lower training cost, existing works often suffer from limited task coverage or poor generation quality. Both approaches lack the ability to parse input meta-information (such as task type, image resolution, video duration, etc.) and require manual parameter configuration that is tedious and non-intelligent. In this paper, we propose Unison which adopts the two-stage scheme while preserving the capabilities of the pre-trained models well. With an extremely low training cost, we cover a variety of multimodal understanding tasks, including text, image, and video understanding, as well as diverse generation tasks, such as text-to-visual content generation, editing, controllable generation, and IP-based reference generation. We also equip our model with the ability to automatically parse user intentions, determine the target task type, and accurately extract the meta-information required for the corresponding task. This enables full automation of various multimodal tasks without human intervention. Experiments demonstrate that, under a low-cost setting of only 500k training samples and 50 GPU hours, our model can accurately and automatically identify tasks and extract relevant parameters, and achieve superior performance across a variety of understanding and generation tasks.


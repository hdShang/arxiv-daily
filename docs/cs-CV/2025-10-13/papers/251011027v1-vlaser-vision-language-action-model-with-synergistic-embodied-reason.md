---
layout: default
title: Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning
---

# Vlaser: Vision-Language-Action Model with Synergistic Embodied Reasoning

**arXiv**: [2510.11027v1](https://arxiv.org/abs/2510.11027) | [PDF](https://arxiv.org/pdf/2510.11027.pdf)

**作者**: Ganlin Yang, Tianyi Zhang, Haoran Hao, Weiyun Wang, Yibin Liu, Dehui Wang, Guanzhou Chen, Zijian Cai, Junting Chen, Weijie Su, Wengang Zhou, Yu Qiao, Jifeng Dai, Jiangmiao Pang, Gen Luo, Wenhai Wang, Yao Mu, Zhi Hou

---

## 💡 一句话要点

**提出Vlaser模型以弥合视觉语言推理与具身策略学习间的差距**

**关键词**: `视觉语言动作模型` `具身推理` `策略学习` `数据集构建` `基准测试` `领域迁移`

## 📋 核心要点

1. 核心问题：现有研究未直接解决上游视觉语言模型推理与下游视觉语言动作策略学习间的关键差距。
2. 方法要点：构建Vlaser模型，集成高层次推理与低层次控制，基于Vlaser-6M数据集实现协同具身推理。
3. 实验或效果：在多个具身推理基准上达到最优性能，并在WidowX和Google Robot基准上取得领先或竞争性结果。

## 📄 摘要（原文）

> While significant research has focused on developing embodied reasoning
> capabilities using Vision-Language Models (VLMs) or integrating advanced VLMs
> into Vision-Language-Action (VLA) models for end-to-end robot control, few
> studies directly address the critical gap between upstream VLM-based reasoning
> and downstream VLA policy learning. In this work, we take an initial step
> toward bridging embodied reasoning with VLA policy learning by introducing
> Vlaser - a Vision-Language-Action Model with synergistic embodied reasoning
> capability, which is a foundational vision-language model designed to integrate
> high-level reasoning with low-level control for embodied agents. Built upon the
> high-quality Vlaser-6M dataset, Vlaser achieves state-of-the-art performance
> across a range of embodied reasoning benchmarks - including spatial reasoning,
> embodied grounding, embodied QA, and task planning. Furthermore, we
> systematically examine how different VLM initializations affect supervised VLA
> fine-tuning, offering novel insights into mitigating the domain shift between
> internet-scale pre-training data and embodied-specific policy learning data.
> Based on these insights, our approach achieves state-of-the-art results on the
> WidowX benchmark and competitive performance on the Google Robot benchmark.


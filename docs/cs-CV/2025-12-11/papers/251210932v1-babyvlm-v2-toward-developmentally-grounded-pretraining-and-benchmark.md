---
layout: default
title: BabyVLM-V2: Toward Developmentally Grounded Pretraining and Benchmarking of Vision Foundation Models
---

# BabyVLM-V2: Toward Developmentally Grounded Pretraining and Benchmarking of Vision Foundation Models

**arXiv**: [2512.10932v1](https://arxiv.org/abs/2512.10932) | [PDF](https://arxiv.org/pdf/2512.10932.pdf)

**作者**: Shengao Wang, Wenqi Wang, Zecheng Wang, Max Whitton, Michael Wakeham, Arjun Chandra, Joey Huang, Pengyue Zhu, Helen Chen, David Li, Jeffrey Li, Shawn Li, Andrew Zagula, Amy Zhao, Andrew Zhu, Sayaka Nakamura, Yuki Yamamoto, Jerry Jun Yokono, Aaron Mueller, Bryan A. Plummer, Kate Saenko, Venkatesh Saligrama, Boqing Gong

---

## 💡 一句话要点

**提出BabyVLM-V2框架，基于婴儿发展轨迹进行视觉基础模型预训练与评估**

**关键词**: `视觉语言模型` `发展性预训练` `婴儿中心数据` `认知评估基准` `多模态任务` `样本效率`

## 📋 核心要点

1. 核心问题：早期儿童发展轨迹为样本高效预训练视觉基础模型提供自然目标
2. 方法要点：通过纵向多模态预训练集和DevCV工具箱，模拟婴儿经验并评估认知能力
3. 实验或效果：紧凑模型在DevCV工具箱上表现竞争性，部分任务超越GPT-4o

## 📄 摘要（原文）

> Early children's developmental trajectories set up a natural goal for sample-efficient pretraining of vision foundation models. We introduce BabyVLM-V2, a developmentally grounded framework for infant-inspired vision-language modeling that extensively improves upon BabyVLM-V1 through a longitudinal, multifaceted pretraining set, a versatile model, and, most importantly, DevCV Toolbox for cognitive evaluation. The pretraining set maximizes coverage while minimizing curation of a longitudinal, infant-centric audiovisual corpus, yielding video-utterance, image-utterance, and multi-turn conversational data that mirror infant experiences. DevCV Toolbox adapts all vision-related measures of the recently released NIH Baby Toolbox into a benchmark suite of ten multimodal tasks, covering spatial reasoning, memory, and vocabulary understanding aligned with early children's capabilities. Experimental results show that a compact model pretrained from scratch can achieve competitive performance on DevCV Toolbox, outperforming GPT-4o on some tasks. We hope the principled, unified BabyVLM-V2 framework will accelerate research in developmentally plausible pretraining of vision foundation models.


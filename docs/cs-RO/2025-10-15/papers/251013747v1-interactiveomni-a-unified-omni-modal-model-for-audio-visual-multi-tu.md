---
layout: default
title: InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue
---

# InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue

**arXiv**: [2510.13747v1](https://arxiv.org/abs/2510.13747) | [PDF](https://arxiv.org/pdf/2510.13747.pdf)

**作者**: Wenwen Tong, Hewei Guo, Dongchuan Ran, Jiangnan Chen, Jiefan Lu, Kaibin Wang, Keqiang Li, Xiaoxu Zhu, Jiakui Li, Kehan Li, Xueheng Li, Lumin Li, Chenxu Guo, Jiasheng Zhou, Jiandong Chen, Xianye Wu, Jiahao Wang, Silei Wu, Lei Chen, Hanming Deng, Yuxuan Song, Dinghao Zhou, Guiping Zhong, Ken Zheng, Shiyin Kang, Lewei Lu

---

## 💡 一句话要点

**提出InteractiveOmni统一全模态模型，用于音频-视觉多轮对话，实现轻量级智能交互。**

**关键词**: `全模态理解` `多轮对话` `语音生成` `轻量级模型` `多模态基准`

## 📋 核心要点

1. 核心问题：构建轻量级全模态模型，支持音频-视觉多轮交互与语音生成。
2. 方法要点：集成视觉、音频编码器、大语言模型和语音解码器，采用多阶段训练策略。
3. 实验或效果：在多项基准测试中优于开源模型，4B版本性能接近更大模型，内存能力突出。

## 📄 摘要（原文）

> We introduce InteractiveOmni, a unified and open-source omni-modal large
> language model for audio-visual multi-turn interaction, ranging from 4B to 8B
> parameters, designed to lead the field of lightweight models by offering
> comprehensive omni-modal understanding and speech generation capabilities. To
> achieve this, we integrate the vision encoder, audio encoder, large language
> model, and speech decoder into a unified model for understanding and generation
> tasks. We design a multi-stage training strategy to ensure robust cross-modal
> capabilities, including pre-training for omni-modal understanding, followed by
> post-training with speech conversation and audio-visual interaction. To enable
> human-like long-term conversational ability, we meticulously curate a
> multi-turn training dataset that enhances the model's ability to handle complex
> and multi-turn interactions. To effectively evaluate the multi-turn memory and
> speech interaction capabilities, we construct the multi-modal multi-turn memory
> benchmark and the multi-turn speech interaction benchmark. Experiments
> demonstrate that InteractiveOmni significantly outperforms leading open-source
> models and provides a more intelligent multi-turn audio-visual experience,
> particularly in its long-term memory capabilities. Notably, InteractiveOmni-4B
> is comparable to the much larger model like Qwen2.5-Omni-7B on general
> benchmarks, and it can retain 97% of the performance of the InteractiveOmni-8B
> while utilizing only 50% of the model size. Achieving state-of-the-art results
> against similarly sized models across image, audio, video understanding, and
> speech generation tasks, InteractiveOmni is an accessible, open-source
> foundation for next-generation intelligent interactive systems.


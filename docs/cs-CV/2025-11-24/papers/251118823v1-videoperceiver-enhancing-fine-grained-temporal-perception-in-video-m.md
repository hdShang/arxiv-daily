---
layout: default
title: VideoPerceiver: Enhancing Fine-Grained Temporal Perception in Video Multimodal Large Language Models
---

# VideoPerceiver: Enhancing Fine-Grained Temporal Perception in Video Multimodal Large Language Models

**arXiv**: [2511.18823v1](https://arxiv.org/abs/2511.18823) | [PDF](https://arxiv.org/pdf/2511.18823.pdf)

**作者**: Fufangchen Zhao, Liao Zhang, Daiqi Shi, Yuanjun Gao, Chen Ye, Yang Cai, Jian Gao, Danfeng Yan

---

## 💡 一句话要点

**提出VideoPerceiver以增强视频多模态大语言模型在细粒度时间感知中的能力**

**关键词**: `视频多模态大语言模型` `细粒度时间感知` `两阶段训练` `关键信息缺失` `相对奖励机制` `罕见事件描述`

## 📋 核心要点

1. 核心问题：VMLLMs在短片段中推理短暂动作或长视频中罕见瞬态事件的能力有限
2. 方法要点：采用两阶段训练框架，包括SFT中的关键信息缺失视频构建和RL中的相对奖励机制
3. 实验或效果：在细粒度动作理解和罕见事件描述基准上显著优于现有VMLLMs，同时保持标准任务性能

## 📄 摘要（原文）

> We propose VideoPerceiver, a novel video multimodal large language model (VMLLM) that enhances fine-grained perception in video understanding, addressing VMLLMs' limited ability to reason about brief actions in short clips or rare transient events in long videos. VideoPerceiver adopts a two-stage training framework. During supervised fine-tuning (SFT), we construct "key-information-missing" videos by extracting event-action keywords from captions, identifying corresponding key frames, and replacing them with adjacent frames. We jointly encode original and modified video tokens with text tokens, aligning intermediate visual representations with keywords via an auxiliary contrastive loss to enhance sensitivity to fine-grained motion cues. In reinforcement learning (RL), both video variants are fed into the model to generate descriptions, and a novel relative reward ensures responses from complete videos outperform those from degraded inputs, explicitly training the model to recover temporally precise action details. We also curate a dataset of 80,000 videos with fine-grained actions and transient events. Experiments show VideoPerceiver substantially outperforms state-of-the-art VMLLMs on fine-grained action understanding and rare event captioning benchmarks, while maintaining strong performance on standard tasks. By prioritizing task-relevant visual features, our work redefines video-language model training for fine-grained perception.


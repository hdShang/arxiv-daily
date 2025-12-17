---
layout: default
title: Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation
---

# Audio-VLA: Adding Contact Audio Perception to Vision-Language-Action Model for Robotic Manipulation

**arXiv**: [2511.09958v1](https://arxiv.org/abs/2511.09958) | [PDF](https://arxiv.org/pdf/2511.09958.pdf)

**作者**: Xiangyi Wei, Haotian Zhang, Xinyi Cao, Siyu Xie, Weifeng Ge, Yang Li, Changbo Wang

---

## 💡 一句话要点

**提出Audio-VLA模型，利用接触音频增强机器人操作中的动态过程感知。**

**关键词**: `机器人操作` `多模态学习` `接触音频感知` `动态过程评估` `跨模态对齐` `LoRA微调`

## 📋 核心要点

1. 视觉-语言-动作模型在感知交互动态过程方面存在局限。
2. 融合视觉与音频模态，采用预训练模型和LoRA微调实现跨模态理解。
3. 在仿真和真实任务中表现优于纯视觉方法，并引入TCR指标评估动态过程。

## 📄 摘要（原文）

> The Vision-Language-Action models (VLA) have achieved significant advances in robotic manipulation recently. However, vision-only VLA models create fundamental limitations, particularly in perceiving interactive and manipulation dynamic processes. This paper proposes Audio-VLA, a multimodal manipulation policy that leverages contact audio to perceive contact events and dynamic process feedback. Audio-VLA overcomes the vision-only constraints of VLA models. Additionally, this paper introduces the Task Completion Rate (TCR) metric to systematically evaluate dynamic operational processes. Audio-VLA employs pre-trained DINOv2 and SigLIP as visual encoders, AudioCLIP as the audio encoder, and Llama2 as the large language model backbone. We apply LoRA fine-tuning to these pre-trained modules to achieve robust cross-modal understanding of both visual and acoustic inputs. A multimodal projection layer aligns features from different modalities into the same feature space. Moreover RLBench and LIBERO simulation environments are enhanced by adding collision-based audio generation to provide realistic sound feedback during object interactions. Since current robotic manipulation evaluations focus on final outcomes rather than providing systematic assessment of dynamic operational processes, the proposed TCR metric measures how well robots perceive dynamic processes during manipulation, creating a more comprehensive evaluation metric. Extensive experiments on LIBERO, RLBench, and two real-world tasks demonstrate Audio-VLA's superior performance over vision-only comparative methods, while the TCR metric effectively quantifies dynamic process perception capabilities.


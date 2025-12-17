---
layout: default
title: Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation
---

# Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation

**arXiv**: [2511.18950v1](https://arxiv.org/abs/2511.18950) | [PDF](https://arxiv.org/pdf/2511.18950.pdf)

**作者**: Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian

---

## 💡 一句话要点

**提出Compressor-VLA以解决视觉-语言-动作模型中视觉令牌冗余问题**

**关键词**: `视觉-语言-动作模型` `令牌压缩` `机器人操作` `指令引导` `计算效率` `sim-to-real迁移`

## 📋 核心要点

1. 核心问题：视觉令牌冗余导致计算开销大，阻碍机器人实时部署
2. 方法要点：结合语义任务压缩器和空间细化压缩器，动态调制压缩
3. 实验或效果：在LIBERO基准上成功率高，FLOPs减少59%，令牌数降3倍以上

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a powerful paradigm in Embodied AI. However, the significant computational overhead of processing redundant visual tokens remains a critical bottleneck for real-time robotic deployment. While standard token pruning techniques can alleviate this, these task-agnostic methods struggle to preserve task-critical visual information. To address this challenge, simultaneously preserving both the holistic context and fine-grained details for precise action, we propose Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. The proposed Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. This compression is dynamically modulated by the natural language instruction, allowing for the adaptive condensation of task-relevant visual information. Experimentally, extensive evaluations demonstrate that Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline. The real-robot deployments on a dual-arm robot platform validate the model's sim-to-real transferability and practical applicability. Moreover, qualitative analyses reveal that our instruction guidance dynamically steers the model's perceptual focus toward task-relevant objects, thereby validating the effectiveness of our approach.


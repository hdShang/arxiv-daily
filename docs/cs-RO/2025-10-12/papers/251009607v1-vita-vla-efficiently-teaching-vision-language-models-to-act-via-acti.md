---
layout: default
title: VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation
---

# VITA-VLA: Efficiently Teaching Vision-Language Models to Act via Action Expert Distillation

**arXiv**: [2510.09607v1](https://arxiv.org/abs/2510.09607) | [PDF](https://arxiv.org/pdf/2510.09607.pdf)

**作者**: Shaoqi Dong, Chaoyou Fu, Haihan Gao, Yi-Fan Zhang, Chi Yan, Chu Wu, Xiaoyu Liu, Yunhang Shen, Jing Huo, Deqiang Jiang, Haoyu Cao, Yang Gao, Xing Sun, Ran He, Caifeng Shan

---

## 💡 一句话要点

**提出基于动作专家蒸馏的框架，高效赋予视觉语言模型动作执行能力**

**关键词**: `视觉语言动作模型` `知识蒸馏` `机器人操作` `动作预测` `高效训练`

## 📋 核心要点

1. 核心问题：训练视觉语言动作模型成本高昂，需从零开始。
2. 方法要点：通过两阶段蒸馏，重用预训练小动作模型知识，添加动作令牌和状态编码器。
3. 实验效果：在LIBERO和真实世界任务中，成功率显著提升，训练成本降低。

## 📄 摘要（原文）

> Vision-Language Action (VLA) models significantly advance robotic
> manipulation by leveraging the strong perception capabilities of pretrained
> vision-language models (VLMs). By integrating action modules into these
> pretrained models, VLA methods exhibit improved generalization. However,
> training them from scratch is costly. In this work, we propose a simple yet
> effective distillation-based framework that equips VLMs with action-execution
> capability by transferring knowledge from pretrained small action models. Our
> architecture retains the original VLM structure, adding only an action token
> and a state encoder to incorporate physical inputs. To distill action
> knowledge, we adopt a two-stage training strategy. First, we perform
> lightweight alignment by mapping VLM hidden states into the action space of the
> small action model, enabling effective reuse of its pretrained action decoder
> and avoiding expensive pretraining. Second, we selectively fine-tune the
> language model, state encoder, and action modules, enabling the system to
> integrate multimodal inputs with precise action generation. Specifically, the
> action token provides the VLM with a direct handle for predicting future
> actions, while the state encoder allows the model to incorporate robot dynamics
> not captured by vision alone. This design yields substantial efficiency gains
> over training large VLA models from scratch. Compared with previous
> state-of-the-art methods, our method achieves 97.3% average success rate on
> LIBERO (11.8% improvement) and 93.5% on LIBERO-LONG (24.5% improvement). In
> real-world experiments across five manipulation tasks, our method consistently
> outperforms the teacher model, achieving 82.0% success rate (17% improvement),
> which demonstrate that action distillation effectively enables VLMs to generate
> precise actions while substantially reducing training costs.


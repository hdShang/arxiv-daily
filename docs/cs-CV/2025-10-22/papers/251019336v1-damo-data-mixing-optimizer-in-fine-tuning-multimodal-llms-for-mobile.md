---
layout: default
title: DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents
---

# DaMo: Data Mixing Optimizer in Fine-tuning Multimodal LLMs for Mobile Phone Agents

**arXiv**: [2510.19336v1](https://arxiv.org/abs/2510.19336) | [PDF](https://arxiv.org/pdf/2510.19336.pdf)

**作者**: Kai Shi, Jun Yang, Ni Yang, Binqiang Pan, Qingsong Xie, Chao Zhang, Zhenyu Yang, Tianhuang Su, Haonan Lu

---

## 💡 一句话要点

**提出DaMo数据混合优化器以提升多模态大模型在移动手机代理中的多任务性能**

**关键词**: `数据混合优化` `多模态大模型` `移动手机代理` `多任务学习` `基准测试`

## 📋 核心要点

1. 核心问题：多模态大模型在移动手机代理中处理多任务时，现有方法难以确定最优训练数据组合。
2. 方法要点：DaMo使用可训练网络预测下游任务性能，以优化数据混合配置。
3. 实验或效果：在PhoneAgentBench上性能提升3.38%，并在多个基准测试中展现优越泛化能力。

## 📄 摘要（原文）

> Mobile Phone Agents (MPAs) have emerged as a promising research direction due
> to their broad applicability across diverse scenarios. While Multimodal Large
> Language Models (MLLMs) serve as the foundation for MPAs, their effectiveness
> in handling multiple mobile phone tasks simultaneously remains limited.
> Although multitask supervised fine-tuning (SFT) is widely adopted for multitask
> learning, existing approaches struggle to determine optimal training data
> compositions for peak performance. To address this challenge, we propose DaMo
> (Data Mixture Optimizer) - a novel solution employing a trainable network that
> predicts optimal data mixtures by forecasting downstream task performance for
> any given dataset ratio. To support comprehensive evaluation, we introduce
> PhoneAgentBench, the first specialized benchmark to evaluate MLLMs on
> multimodal mobile phone tasks, comprising 1235 QA pairs spanning diverse
> real-world industrial mobile application scenarios. Demonstrating strong
> predictive capability (R^2=0.81) in small-scale pilot experiments, DaMo
> efficiently extrapolates optimal data mixing configurations. Our results show
> DaMo achieves a 3.38% performance improvement on PhoneAgentBench compared to
> alternative methods. Furthermore, extensive experiments across established
> benchmarks including BFCL-v3, MME-Reasoning, MME-Perception, and OCRBench
> reveal DaMo's superior generalization, outperforming other approaches by 2.57%
> in terms of average score. When used solely for MLLM optimization on the
> BFCL-v3 task, DaMo improves the metrics by 12.47% than other methods. Notably,
> DaMo maintains robust scalability, preserving its effectiveness when applied to
> other model architectures. The code and dataset are available at
> https://github.com/OPPO-Mente-Lab/DaMo.git


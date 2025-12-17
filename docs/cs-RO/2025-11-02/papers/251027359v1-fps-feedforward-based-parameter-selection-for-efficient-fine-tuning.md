---
layout: default
title: FPS: Feedforward-based Parameter Selection For Efficient Fine-Tuning
---

# FPS: Feedforward-based Parameter Selection For Efficient Fine-Tuning

**arXiv**: [2510.27359v1](https://arxiv.org/abs/2510.27359) | [PDF](https://arxiv.org/pdf/2510.27359.pdf)

**作者**: Kenneth Yang, Wen-Li Wei, Jen-Chun Lin

---

## 💡 一句话要点

**提出前馈参数选择方法以高效微调大规模预训练模型**

**关键词**: `参数高效微调` `前馈选择` `内存优化` `视觉任务` `梯度自由方法`

## 📋 核心要点

1. 现有参数高效微调方法存在推理延迟或高内存使用问题
2. FPS通过单次前向传递基于参数幅度和输入激活选择最优子集
3. 在24个视觉任务上性能可比SOTA，内存使用减少近9倍，选择速度提升约2倍

## 📄 摘要（原文）

> Parameter-Efficient Fine-Tuning (PEFT) has emerged as a key strategy for
> adapting large-scale pre-trained models to downstream tasks, but existing
> approaches face notable limitations. Addition-based methods, such as Adapters
> [1], introduce inference latency and engineering complexity, while
> selection-based methods like Gradient-based Parameter Selection (GPS) [2]
> require a full backward pass, which results in the same peak memory usage as
> full fine-tuning. To address this dilemma, we propose Feedforward-based
> Parameter Selection (FPS), a gradient-free method that identifies an optimal
> parameter subset in a single forward pass. FPS ranks parameters by the product
> of their magnitudes and corresponding input activations, leveraging both
> pre-trained knowledge and downstream data. Evaluated on $24$ visual tasks from
> FGVC and VTAB-1k, FPS achieves performance comparable to state-of-the-art
> methods while reducing peak memory usage by nearly $9 \times$ and accelerating
> parameter selection by about $2 \times$, offering a genuinely memory-efficient
> and practical solution for fine-tuning large-scale pre-trained models.


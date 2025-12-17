---
layout: default
title: Remember Me: Bridging the Long-Range Gap in LVLMs with Three-Step Inference-Only Decay Resilience Strategies
---

# Remember Me: Bridging the Long-Range Gap in LVLMs with Three-Step Inference-Only Decay Resilience Strategies

**arXiv**: [2511.09868v1](https://arxiv.org/abs/2511.09868) | [PDF](https://arxiv.org/pdf/2511.09868.pdf)

**作者**: Peng Gao, Yujian Lee, Xiaofeng Zhang, Zailong Chen, Hui Zhang

---

## 💡 一句话要点

**提出三步骤衰减韧性策略以解决LVLM中长距离依赖建模问题**

**关键词**: `大型视觉语言模型` `长距离依赖` `推理优化` `注意力机制` `视觉问答` `位置编码`

## 📋 核心要点

1. 核心问题：LVLM使用ROPE时，长距离token对注意力衰减，影响全局上下文记忆
2. 方法要点：推理阶段应用三步策略，增强语义信号、调控距离权重、强化远程依赖
3. 实验或效果：在VQA基准上训练免费提升性能，代码已开源

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) have achieved impressive performance across a wide range of multimodal tasks. However, they still face critical challenges in modeling long-range dependencies under the usage of Rotary Positional Encoding (ROPE). Although it can facilitate precise modeling of token positions, it induces progressive attention decay as token distance increases, especially with progressive attention decay over distant token pairs, which severely impairs the model's ability to remember global context. To alleviate this issue, we propose inference-only Three-step Decay Resilience Strategies (T-DRS), comprising (1) Semantic-Driven DRS (SD-DRS), amplifying semantically meaningful but distant signals via content-aware residuals, (2) Distance-aware Control DRS (DC-DRS), which can purify attention by smoothly modulating weights based on positional distances, suppressing noise while preserving locality, and (3) re-Reinforce Distant DRS (reRD-DRS), consolidating the remaining informative remote dependencies to maintain global coherence. Together, the T-DRS recover suppressed long-range token pairs without harming local inductive biases. Extensive experiments on Vision Question Answering (VQA) benchmarks demonstrate that T-DRS can consistently improve performance in a training-free manner. The code can be accessed in https://github.com/labixiaoq-qq/Remember-me

